-- Academic record: school terms, term results compiled from the gradebook (and editable), published term reports,
-- and transcripts with a public verification code.
-- Results live outside the class gradebook, so they survive class changes, promotions and students leaving.
-- Students (and the transcript) only ever see published reports.

alter table public.schools add column if not exists grade_bands jsonb
  check (grade_bands is null or (jsonb_typeof(grade_bands) = 'array' and jsonb_array_length(grade_bands) between 2 and 15));

-- ---------- terms ----------
create table if not exists public.academic_terms (
  id         uuid primary key default gen_random_uuid(),
  school_id  uuid not null references public.schools(id) on delete cascade,
  name       text not null check (length(name) between 1 and 40),
  starts_on  date not null,
  ends_on    date not null,
  created_at timestamptz not null default now(),
  check (ends_on >= starts_on and ends_on <= starts_on + 400),
  unique (school_id, name)
);
alter table public.academic_terms enable row level security;
drop policy if exists academic_terms_read on public.academic_terms;
create policy academic_terms_read on public.academic_terms for select to authenticated using (school_id = public.my_school() or public.is_platform_admin());
drop policy if exists academic_terms_admin on public.academic_terms;
create policy academic_terms_admin on public.academic_terms for all to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin())
  with check (public.is_school_admin_of(school_id) or public.is_platform_admin());

-- ---------- reports and results ----------
create table if not exists public.term_reports (
  id              uuid primary key default gen_random_uuid(),
  school_id       uuid not null references public.schools(id) on delete cascade,
  term_id         uuid not null references public.academic_terms(id) on delete cascade,
  student_id      uuid not null references public.profiles(id) on delete cascade,
  class_id        uuid references public.classes(id) on delete set null,
  class_name      text check (length(class_name) <= 80),
  average         numeric(5,2) check (average between 0 and 100),
  position        integer check (position > 0),
  class_size      integer check (class_size > 0),
  attendance_pct  numeric(5,2) check (attendance_pct between 0 and 100),
  teacher_comment text check (length(teacher_comment) <= 1000),
  head_comment    text check (length(head_comment) <= 1000),
  published_at    timestamptz,
  published_by    uuid references public.profiles(id) on delete set null,
  updated_at      timestamptz not null default now(),
  unique (term_id, student_id)
);
create table if not exists public.term_results (
  id         uuid primary key default gen_random_uuid(),
  school_id  uuid not null references public.schools(id) on delete cascade,
  term_id    uuid not null references public.academic_terms(id) on delete cascade,
  student_id uuid not null references public.profiles(id) on delete cascade,
  subject    text not null check (length(subject) between 1 and 80),
  score      numeric(5,2) check (score between 0 and 100),
  grade      text check (length(grade) <= 8),
  comment    text check (length(comment) <= 300),
  source     text not null default 'manual' check (source in ('gradebook','manual')),
  updated_by uuid references public.profiles(id) on delete set null,
  updated_at timestamptz not null default now(),
  unique (term_id, student_id, subject)
);
create index if not exists term_results_student_idx on public.term_results (student_id, term_id);
create index if not exists term_reports_student_idx on public.term_reports (student_id);

alter table public.term_reports enable row level security;
alter table public.term_results enable row level security;
drop policy if exists term_reports_admin on public.term_reports;
create policy term_reports_admin on public.term_reports for all to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin())
  with check ((public.is_school_admin_of(school_id) or public.is_platform_admin())
              and exists (select 1 from public.academic_terms t where t.id = term_id and t.school_id = term_reports.school_id)
              and exists (select 1 from public.profiles p where p.id = student_id and p.school_id = term_reports.school_id and p.role = 'student'));
drop policy if exists term_reports_teacher on public.term_reports;
create policy term_reports_teacher on public.term_reports for select to authenticated using (public.teaches_student(student_id));
drop policy if exists term_reports_self on public.term_reports;
create policy term_reports_self on public.term_reports for select to authenticated using (student_id = auth.uid() and published_at is not null);

drop policy if exists term_results_admin on public.term_results;
create policy term_results_admin on public.term_results for all to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin())
  with check ((public.is_school_admin_of(school_id) or public.is_platform_admin())
              and exists (select 1 from public.academic_terms t where t.id = term_id and t.school_id = term_results.school_id)
              and exists (select 1 from public.profiles p where p.id = student_id and p.school_id = term_results.school_id and p.role = 'student'));
drop policy if exists term_results_teacher on public.term_results;
create policy term_results_teacher on public.term_results for select to authenticated using (public.teaches_student(student_id));
drop policy if exists term_results_self on public.term_results;
create policy term_results_self on public.term_results for select to authenticated
  using (student_id = auth.uid() and exists (select 1 from public.term_reports r where r.term_id = term_results.term_id and r.student_id = auth.uid() and r.published_at is not null));
revoke all on public.academic_terms, public.term_reports, public.term_results from anon;

-- results of a published report are frozen: unpublish first
create or replace function public.term_results_frozen() returns trigger language plpgsql set search_path = public as $$
declare t uuid := coalesce(new.term_id, old.term_id); s uuid := coalesce(new.student_id, old.student_id);
begin
  if exists (select 1 from public.term_reports r where r.term_id = t and r.student_id = s and r.published_at is not null) then
    raise exception 'This report is published. Unpublish it to change results.';
  end if;
  return coalesce(new, old);
end $$;
drop trigger if exists term_results_frozen on public.term_results;
create trigger term_results_frozen before insert or update or delete on public.term_results for each row execute function public.term_results_frozen();

create or replace function public.term_reports_frozen() returns trigger language plpgsql set search_path = public as $$
begin
  if old.published_at is not null and new.published_at is not null and coalesce(current_setting('ace.term_sync', true), '') <> 'on' then
    raise exception 'This report is published. Unpublish it to change it.';
  end if;
  new.updated_at := now();
  return new;
end $$;
drop trigger if exists term_reports_frozen on public.term_reports;
create trigger term_reports_frozen before update on public.term_reports for each row execute function public.term_reports_frozen();

-- ---------- grading ----------
create or replace function public.term_results_grade() returns trigger language plpgsql security definer set search_path = public as $$
begin
  if new.score is not null then new.grade := public.grade_for(new.school_id, new.score); end if;
  new.updated_at := now();
  return new;
end $$;
drop trigger if exists term_results_grade on public.term_results;
create trigger term_results_grade before insert or update on public.term_results for each row execute function public.term_results_grade();

create or replace function public.grade_for(p_school uuid, p_score numeric) returns text
language sql stable security definer set search_path = public as $$
  select case when p_score is null then null else (
    select b->>'grade' from jsonb_array_elements(coalesce((select grade_bands from public.schools where id = p_school),
      '[{"grade":"A","min":80},{"grade":"B","min":70},{"grade":"C","min":60},{"grade":"D","min":50},{"grade":"E","min":40},{"grade":"F","min":0}]'::jsonb)) b
    where p_score >= (b->>'min')::numeric order by (b->>'min')::numeric desc limit 1) end $$;

-- Builds (or rebuilds) the term results of everyone currently in a class from the gradebook:
-- per subject, the weighted percentage of assessments held in the term (equal weights when none are set).
-- Results entered by hand are kept. Published reports are skipped. Returns the number of students compiled.
create or replace function public.compile_term(p_term uuid, p_class uuid) returns integer
language plpgsql security definer set search_path = public as $$
declare t public.academic_terms; c public.classes; k int := 0; st record;
begin
  select * into t from public.academic_terms where id = p_term;
  select * into c from public.classes where id = p_class;
  if t.id is null or c.id is null or t.school_id <> c.school_id or not (public.is_school_admin_of(t.school_id) or public.is_platform_admin()) then
    raise exception 'You do not have permission to do that.';
  end if;
  for st in select p.id from public.profiles p where p.class_id = p_class and p.role = 'student' and p.enrolment_status in ('active','suspended')
              and not exists (select 1 from public.term_reports r where r.term_id = p_term and r.student_id = p.id and r.published_at is not null) loop
    delete from public.term_results where term_id = p_term and student_id = st.id and source = 'gradebook';
    insert into public.term_results (school_id, term_id, student_id, subject, score, source, updated_by)
    select t.school_id, p_term, st.id, a.subject,
           least(100, round(100 * sum(m.mark / a.max_mark * (case when w.any_weight then a.weight else 1 end)) / nullif(sum(case when w.any_weight then a.weight else 1 end), 0), 2)),
           'gradebook', auth.uid()
    from public.assessments a
    join public.marks m on m.assessment_id = a.id and m.student_id = st.id
    join (select subject, bool_or(weight > 0) as any_weight from public.assessments
          where class_id = p_class and coalesce(held_on, created_at::date) between t.starts_on and t.ends_on group by subject) w on w.subject = a.subject
    where a.class_id = p_class and coalesce(a.held_on, a.created_at::date) between t.starts_on and t.ends_on
      and (not w.any_weight or a.weight > 0)
      and not exists (select 1 from public.term_results x where x.term_id = p_term and x.student_id = st.id and x.subject = a.subject)
    group by a.subject;
    insert into public.term_reports (school_id, term_id, student_id, class_id, class_name, attendance_pct)
    values (t.school_id, p_term, st.id, p_class, c.name,
            (select round(100.0 * count(*) filter (where a.status in ('present','late')) / nullif(count(*) filter (where a.status <> 'excused'), 0), 2)
               from public.attendance a where a.student_id = st.id and a.day between t.starts_on and t.ends_on))
    on conflict (term_id, student_id) do update set class_id = excluded.class_id, class_name = excluded.class_name, attendance_pct = excluded.attendance_pct;
    k := k + 1;
  end loop;
  perform public.rank_term(p_term, p_class);
  return k;
end $$;

-- averages and positions within the class (ties share a position)
create or replace function public.rank_term(p_term uuid, p_class uuid) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not exists (select 1 from public.academic_terms t where t.id = p_term and (public.is_school_admin_of(t.school_id) or public.is_platform_admin())) then
    raise exception 'You do not have permission to do that.';
  end if;
  update public.term_reports r set average = x.avg
    from (select student_id, round(avg(score), 2) avg from public.term_results where term_id = p_term and score is not null group by student_id) x
   where r.term_id = p_term and r.class_id = p_class and r.student_id = x.student_id and r.published_at is null;
  update public.term_reports r set position = x.pos, class_size = x.n
    from (select id, rank() over (order by average desc) pos, count(*) over () n from public.term_reports
           where term_id = p_term and class_id = p_class and average is not null) x
   where r.id = x.id and r.published_at is null;
end $$;

create or replace function public.publish_term(p_term uuid, p_class uuid, p_publish boolean) returns integer
language plpgsql security definer set search_path = public as $$
declare k int;
begin
  if not exists (select 1 from public.academic_terms t where t.id = p_term and (public.is_school_admin_of(t.school_id) or public.is_platform_admin())) then
    raise exception 'You do not have permission to do that.';
  end if;
  if p_publish then perform public.rank_term(p_term, p_class); end if;
  perform set_config('ace.term_sync', 'on', true);
  update public.term_reports set published_at = case when p_publish then now() else null end, published_by = case when p_publish then auth.uid() else null end
   where term_id = p_term and class_id = p_class and (published_at is null) = p_publish;
  get diagnostics k = row_count;
  perform set_config('ace.term_sync', 'off', true);
  return k;
end $$;

-- ---------- transcripts ----------
create table if not exists public.transcripts (
  id             uuid primary key default gen_random_uuid(),
  school_id      uuid not null references public.schools(id) on delete cascade,
  student_id     uuid not null references public.profiles(id) on delete cascade,
  status         text not null default 'requested' check (status in ('requested','issued','declined')),
  purpose        text check (length(purpose) <= 200),
  code           text unique check (code is null or code ~ '^TR[A-HJ-NP-Z2-9]{10}$'),
  snapshot       jsonb,
  requested_at   timestamptz not null default now(),
  decided_at     timestamptz,
  decided_by     uuid references public.profiles(id) on delete set null,
  decline_reason text check (length(decline_reason) <= 300),
  revoked_at     timestamptz
);
create index if not exists transcripts_school_idx on public.transcripts (school_id, status, requested_at desc);
alter table public.transcripts enable row level security;
drop policy if exists transcripts_admin_read on public.transcripts;
create policy transcripts_admin_read on public.transcripts for select to authenticated using (public.is_school_admin_of(school_id) or public.is_platform_admin());
drop policy if exists transcripts_self on public.transcripts;
create policy transcripts_self on public.transcripts for select to authenticated using (student_id = auth.uid());
revoke insert, update, delete on public.transcripts from anon, authenticated;
revoke select on public.transcripts from anon;

create or replace function public.request_transcript(p_purpose text default null) returns uuid
language plpgsql security definer set search_path = public as $$
declare p public.profiles; v_id uuid;
begin
  select * into p from public.profiles where id = auth.uid();
  if p.role <> 'student' or p.school_id is null then raise exception 'Only students of a school can request a transcript.'; end if;
  if not exists (select 1 from public.term_reports r where r.student_id = p.id and r.school_id = p.school_id and r.published_at is not null) then
    raise exception 'Your school has not published any term results for you yet.';
  end if;
  if exists (select 1 from public.transcripts where student_id = p.id and status = 'requested') then raise exception 'You already have a request waiting.'; end if;
  if (select count(*) from public.transcripts where student_id = p.id and requested_at > now() - interval '30 days') >= 5 then raise exception 'Too many requests this month.'; end if;
  insert into public.transcripts (school_id, student_id, purpose) values (p.school_id, p.id, nullif(left(trim(p_purpose), 200), '')) returning transcripts.id into v_id;
  return v_id;
end $$;

-- Issues a transcript from the published reports (answers a request when one is waiting). The snapshot is frozen.
create or replace function public.issue_transcript(p_student uuid, p_purpose text default null) returns public.transcripts
language plpgsql security definer set search_path = public as $$
declare p public.profiles; s public.schools; snap jsonb; tr public.transcripts; a text := 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; c text;
begin
  select * into p from public.profiles where id = p_student and role = 'student';
  if p.id is null or not (public.is_school_admin_of(p.school_id) or public.is_platform_admin()) then raise exception 'You do not have permission to do that.'; end if;
  select * into s from public.schools where id = p.school_id;
  select jsonb_build_object(
    'name', p.first_name || ' ' || p.surname, 'admission_no', p.admission_no, 'school', s.name, 'country', s.country_code,
    'date_of_birth', (select date_of_birth from public.student_records where student_id = p.id),
    'admitted_on', (select admitted_on from public.student_records where student_id = p.id),
    'left_on', (select left_on from public.student_records where student_id = p.id), 'status', p.enrolment_status,
    'terms', coalesce((select jsonb_agg(jsonb_build_object('term', t.name, 'starts_on', t.starts_on, 'class', r.class_name, 'average', r.average,
                'position', r.position, 'class_size', r.class_size, 'attendance_pct', r.attendance_pct,
                'results', coalesce((select jsonb_agg(jsonb_build_object('subject', x.subject, 'score', x.score, 'grade', x.grade) order by x.subject)
                                     from public.term_results x where x.term_id = r.term_id and x.student_id = p.id), '[]'::jsonb)) order by t.starts_on)
              from public.term_reports r join public.academic_terms t on t.id = r.term_id
              where r.student_id = p.id and r.school_id = p.school_id and r.published_at is not null), '[]'::jsonb)) into snap;
  if jsonb_array_length(snap->'terms') = 0 then raise exception 'There are no published term results for this student yet.'; end if;
  loop
    c := 'TR' || (select string_agg(substr(a, 1 + floor(random() * 32)::int, 1), '') from generate_series(1, 10));
    exit when not exists (select 1 from public.transcripts where code = c);
  end loop;
  update public.transcripts set status = 'issued', code = c, snapshot = snap, decided_at = now(), decided_by = auth.uid()
   where id = (select id from public.transcripts where student_id = p.id and status = 'requested' order by requested_at limit 1)
  returning * into tr;
  if tr.id is null then
    insert into public.transcripts (school_id, student_id, status, purpose, code, snapshot, decided_at, decided_by)
    values (p.school_id, p.id, 'issued', nullif(left(trim(p_purpose), 200), ''), c, snap, now(), auth.uid()) returning * into tr;
  end if;
  return tr;
end $$;

create or replace function public.decide_transcript(p_id uuid, p_action text, p_reason text default null) returns void
language plpgsql security definer set search_path = public as $$
declare tr public.transcripts;
begin
  select * into tr from public.transcripts where id = p_id;
  if tr.id is null or not (public.is_school_admin_of(tr.school_id) or public.is_platform_admin()) then raise exception 'You do not have permission to do that.'; end if;
  if p_action = 'decline' and tr.status = 'requested' then
    update public.transcripts set status = 'declined', decline_reason = nullif(trim(p_reason), ''), decided_at = now(), decided_by = auth.uid() where id = p_id;
  elsif p_action = 'revoke' and tr.status = 'issued' and tr.revoked_at is null then
    update public.transcripts set revoked_at = now() where id = p_id;
  else raise exception 'That cannot be done to this transcript.';
  end if;
end $$;

-- Public check of a transcript code: anyone holding the code (an employer, a university) sees what was issued.
create or replace function public.verify_transcript(p_code text)
returns table (school text, issued_at timestamptz, revoked boolean, snapshot jsonb)
language sql stable security definer set search_path = public as $$
  select s.name, t.decided_at, t.revoked_at is not null, case when t.revoked_at is null then t.snapshot end
  from public.transcripts t join public.schools s on s.id = t.school_id
  where t.status = 'issued' and t.code = upper(regexp_replace(trim(p_code), '[^A-Za-z0-9]', '', 'g')) $$;

revoke all on function public.term_results_frozen(), public.term_reports_frozen(), public.term_results_grade() from public, anon, authenticated;
revoke all on function public.grade_for(uuid, numeric), public.compile_term(uuid, uuid), public.rank_term(uuid, uuid), public.publish_term(uuid, uuid, boolean),
  public.request_transcript(text), public.issue_transcript(uuid, text), public.decide_transcript(uuid, text, text), public.verify_transcript(text) from public, anon;
grant execute on function public.grade_for(uuid, numeric), public.compile_term(uuid, uuid), public.rank_term(uuid, uuid), public.publish_term(uuid, uuid, boolean),
  public.request_transcript(text), public.issue_transcript(uuid, text), public.decide_transcript(uuid, text, text) to authenticated;
grant execute on function public.verify_transcript(text) to anon, authenticated;
