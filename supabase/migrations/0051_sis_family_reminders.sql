-- 1. SIS-only schools: a school can use the school-management side of Ace (admissions, records, fees, results,
--    calendar, behaviour, dashboard) without the learning tools. schools.product = 'sis' hides the learning tools in
--    Ace Teach and in the student app; 'full' (the default) is everything.
-- 2. The family link now also shows the school side: published term reports, fees, coming events and shared
--    behaviour entries. School admins can create a family link for a student (for SIS-only schools, where students
--    may never open the app).
-- 3. Fee reminders to guardians: a log so a family is reminded at most once a week, and a phone number on guardians.

alter table public.schools add column if not exists product text not null default 'full' check (product in ('full','sis'));
alter table public.guardians add column if not exists phone text check (length(phone) <= 30);

-- ---------- family links made by the school ----------
alter table public.family_links add column if not exists created_by uuid references public.profiles(id) on delete set null;

create or replace function public.school_family_link(p_student uuid, p_label text default null) returns text
language plpgsql security definer set search_path = public as $$
declare s uuid; alphabet text := 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; c text; i int;
begin
  select school_id into s from public.profiles where id = p_student and role = 'student';
  if s is null or not (public.is_school_admin_of(s) or public.is_platform_admin()) then raise exception 'You do not have permission to do that.'; end if;
  if (select count(*) from public.family_links where student_id = p_student and revoked_at is null and expires_at > now()) >= 5 then
    raise exception 'This student already has 5 active family links. Stop one first.';
  end if;
  loop
    c := ''; for i in 1..12 loop c := c || substr(alphabet, 1 + floor(random() * 32)::int, 1); end loop;
    exit when not exists (select 1 from public.family_links where code = c);
  end loop;
  insert into public.family_links (student_id, code, label, expires_at, created_by)
  values (p_student, c, coalesce(nullif(left(trim(coalesce(p_label, '')), 40), ''), 'From the school'), now() + interval '365 days', auth.uid());
  return c;
end $$;

-- links of one student, for the school admin (the student sees their own through the existing policy)
create or replace function public.student_family_links(p_student uuid)
returns table (id uuid, code text, label text, expires_at timestamptz, last_viewed timestamptz, created_at timestamptz, by_school boolean)
language sql stable security definer set search_path = public as $$
  select l.id, l.code, l.label, l.expires_at, l.last_viewed, l.created_at, l.created_by is not null
  from public.family_links l join public.profiles p on p.id = l.student_id
  where l.student_id = p_student and l.revoked_at is null and l.expires_at > now()
    and (public.is_school_admin_of(p.school_id) or public.is_platform_admin())
  order by l.created_at desc $$;

create or replace function public.school_revoke_family_link(p_id uuid) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not exists (select 1 from public.family_links l join public.profiles p on p.id = l.student_id
                 where l.id = p_id and (public.is_school_admin_of(p.school_id) or public.is_platform_admin())) then
    raise exception 'You do not have permission to do that.';
  end if;
  update public.family_links set revoked_at = now() where id = p_id;
end $$;

-- ---------- the family view, now with the school side ----------
create or replace function public.family_view(p_code text)
returns jsonb language plpgsql security definer set search_path = public as $$
declare l family_links; p profiles; s user_stats; sc schools; week jsonb; subj jsonb; att jsonb; crs jsonb; school jsonb;
        norm text := upper(regexp_replace(coalesce(p_code,''), '[^A-Za-z0-9]', '', 'g'));
begin
  if public._too_many('family', 30, 10) then return null; end if;
  select * into l from family_links where family_links.code = norm and revoked_at is null and expires_at > now();
  if not found then perform public._note_fail('family'); return null; end if;
  update family_links set last_viewed = now() where id = l.id;
  select * into p from profiles where id = l.student_id;
  select * into s from user_stats where user_id = l.student_id;
  select coalesce(jsonb_agg(jsonb_build_object('day', d, 'questions', q, 'correct', c) order by d), '[]') into week
    from (select g::date d, coalesce(sum(a.total),0)::int q, coalesce(sum(a.correct),0)::int c
          from generate_series(current_date - 6, current_date, '1 day') g
          left join quiz_attempts a on a.user_id = l.student_id and a.created_at::date = g::date
          group by g) x;
  select coalesce(jsonb_agg(jsonb_build_object('subject', subject, 'questions', q, 'correct', c) order by q desc), '[]') into subj
    from (select subject, sum(total)::int q, sum(correct)::int c from quiz_attempts
          where user_id = l.student_id and created_at > now() - interval '30 days' group by subject order by sum(total) desc limit 8) y;
  select coalesce(jsonb_object_agg(status, n), '{}') into att
    from (select status, count(*)::int n from attendance where student_id = l.student_id and day > current_date - 30 group by status) z;
  select coalesce(jsonb_agg(jsonb_build_object('title', c.title, 'lessons', cardinality(cp.lessons_done), 'of', c.lesson_count,
         'certified', exists(select 1 from certificates ce where ce.user_id = l.student_id and ce.course = c.slug))), '[]') into crs
    from course_progress cp join courses c on c.slug = cp.course where cp.user_id = l.student_id;

  if p.school_id is not null then
    select * into sc from schools where id = p.school_id;
    school := jsonb_build_object(
      'name', sc.name, 'product', sc.product, 'surname', p.surname, 'admission_no', p.admission_no, 'status', p.enrolment_status,
      'class', (select name from classes where id = p.class_id),
      'reports', (select coalesce(jsonb_agg(jsonb_build_object('term', t.name, 'class', r.class_name, 'average', r.average, 'position', r.position,
                     'class_size', r.class_size, 'attendance_pct', r.attendance_pct, 'teacher_comment', r.teacher_comment, 'head_comment', r.head_comment,
                     'results', coalesce((select jsonb_agg(jsonb_build_object('subject', x.subject, 'score', x.score, 'grade', x.grade) order by x.subject)
                                          from term_results x where x.term_id = r.term_id and x.student_id = p.id), '[]')) order by t.starts_on desc), '[]')
                  from (select * from term_reports where student_id = p.id and published_at is not null) r join academic_terms t on t.id = r.term_id),
      'fees', (select coalesce(jsonb_agg(jsonb_build_object('term', f.term, 'currency', f.currency_code, 'amount', f.amount, 'paid', f.paid,
                  'due_on', f.due_on, 'overdue', public.fee_overdue_any(f.id),
                  'items', coalesce((select jsonb_agg(jsonb_build_object('label', i.label, 'amount', i.amount) order by i.created_at) from fee_items i where i.fee_id = f.id), '[]'),
                  'instalments', coalesce((select jsonb_agg(jsonb_build_object('due_on', n.due_on, 'amount', n.amount) order by n.due_on) from fee_instalments n where n.fee_id = f.id), '[]'),
                  'payments', coalesce((select jsonb_agg(jsonb_build_object('receipt', y.receipt_no, 'paid_on', y.paid_on, 'amount', y.amount) order by y.paid_on)
                                        from fee_payments y where y.fee_id = f.id and y.voided_at is null), '[]')) order by f.created_at), '[]')
               from fees f where f.student_id = p.id),
      'fee_note', sc.fee_note,
      'events', (select coalesce(jsonb_agg(jsonb_build_object('title', e.title, 'kind', e.kind, 'starts_on', e.starts_on, 'ends_on', e.ends_on, 'note', e.note) order by e.starts_on), '[]')
                 from (select * from school_events where school_id = p.school_id and audience = 'everyone' and ends_on >= current_date order by starts_on limit 10) e),
      'term', (select jsonb_build_object('name', name, 'ends_on', ends_on) from academic_terms where school_id = p.school_id and current_date between starts_on and ends_on limit 1),
      'behaviour', (select coalesce(jsonb_agg(jsonb_build_object('kind', b.kind, 'category', b.category, 'description', b.description, 'occurred_on', b.occurred_on) order by b.occurred_on desc), '[]')
                    from (select * from behaviour_entries where student_id = p.id and visible_to_family order by occurred_on desc limit 10) b));
  end if;
  return jsonb_build_object('first_name', p.first_name, 'level', p.level, 'streak', coalesce(s.streak,0), 'xp', coalesce(s.xp,0),
    'week', week, 'subjects', subj, 'attendance_30d', att, 'courses', crs, 'link_label', l.label, 'expires_at', l.expires_at, 'school', school);
end $$;

-- fee_overdue() checks the caller; the family view and reminders run without one, so this version is internal only
create or replace function public.fee_overdue_any(p_fee uuid) returns numeric
language sql stable security definer set search_path = public as $$
  select greatest(0, case
    when exists (select 1 from public.fee_instalments i where i.fee_id = f.id)
      then coalesce((select sum(i.amount) from public.fee_instalments i where i.fee_id = f.id and i.due_on <= current_date), 0) - f.paid
    when f.due_on is not null and f.due_on <= current_date then f.amount - f.paid
    else 0 end)
  from public.fees f where f.id = p_fee $$;

-- ---------- fee reminders ----------
create table if not exists public.fee_reminders (
  id         bigint generated always as identity primary key,
  school_id  uuid not null references public.schools(id) on delete cascade,
  student_id uuid not null references public.profiles(id) on delete cascade,
  channel    text not null check (channel in ('email','copied')),
  sent_to    text check (length(sent_to) <= 200),
  overdue    numeric(12,2),
  currency   text,
  sent_by    uuid references public.profiles(id) on delete set null,
  sent_at    timestamptz not null default now()
);
create index if not exists fee_reminders_idx on public.fee_reminders (school_id, student_id, sent_at desc);
alter table public.fee_reminders enable row level security;
drop policy if exists fee_reminders_read on public.fee_reminders;
create policy fee_reminders_read on public.fee_reminders for select to authenticated using (public.is_school_admin_of(school_id) or public.is_platform_admin());
revoke insert, update, delete on public.fee_reminders from anon, authenticated;
revoke select on public.fee_reminders from anon;

-- who is overdue in the caller's school, with every guardian contact and when they were last reminded
create or replace function public.fee_reminder_list() returns jsonb
language plpgsql stable security definer set search_path = public as $$
declare s uuid := public.my_school();
begin
  if s is null or not public.is_school_admin_of(s) then raise exception 'You do not have permission to do that.'; end if;
  return (select coalesce(jsonb_agg(x order by (x->>'overdue')::numeric desc), '[]') from (
    select jsonb_build_object('student_id', p.id, 'name', p.first_name || ' ' || p.surname, 'admission_no', p.admission_no,
      'class', (select name from classes where id = p.class_id), 'currency', o.cur, 'overdue', o.od, 'balance', o.bal,
      'guardians', coalesce((select jsonb_agg(jsonb_build_object('name', g.name, 'email', g.email, 'phone', g.phone)) from guardians g where g.student_id = p.id), '[]'),
      'phone', coalesce((select phone from student_records where student_id = p.id), (select guardian_phone from applications where student_id = p.id limit 1)),
      'last_reminded', (select max(sent_at) from fee_reminders r where r.student_id = p.id)) x
    from profiles p
    join (select f.student_id, min(f.currency_code) cur, sum(public.fee_overdue_any(f.id)) od, sum(f.amount - f.paid) bal
          from fees f where f.school_id = s group by f.student_id) o on o.student_id = p.id
    where p.school_id = s and o.od > 0) y);
end $$;

revoke all on function public.school_family_link(uuid, text), public.student_family_links(uuid), public.school_revoke_family_link(uuid),
  public.fee_reminder_list() from public, anon;
grant execute on function public.school_family_link(uuid, text), public.student_family_links(uuid), public.school_revoke_family_link(uuid),
  public.fee_reminder_list() to authenticated;
revoke all on function public.fee_overdue_any(uuid) from public, anon, authenticated;
revoke all on function public.family_view(text) from public;
grant execute on function public.family_view(text) to anon, authenticated;
