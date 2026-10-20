-- 0008: read-only "family view". A student (or a university student's parent) shares a revocable link code.
-- No parent accounts, no passwords. The code shows a weekly progress summary only: no messages, notes, group posts or mark comments.
-- Idempotent. Run after 0007.
create table if not exists public.family_links (
  id          uuid primary key default gen_random_uuid(),
  student_id  uuid not null references public.profiles(id) on delete cascade,
  code        text not null unique check (code ~ '^[A-HJ-NP-Z2-9]{12}$'),
  label       text check (length(label) <= 40),
  expires_at  timestamptz not null default now() + interval '90 days',
  revoked_at  timestamptz,
  last_viewed timestamptz,
  created_at  timestamptz not null default now()
);
create index if not exists family_links_student on public.family_links (student_id);
alter table public.family_links enable row level security;
drop policy if exists fl_own_read on public.family_links;
create policy fl_own_read on public.family_links for select to authenticated using (student_id = auth.uid());
-- writes only through the functions below
revoke insert, update, delete on public.family_links from anon, authenticated;
revoke all on public.family_links from anon;

create or replace function public.create_family_link(p_label text default null)
returns text language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid(); alphabet text := 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; c text; i int;
begin
  if uid is null then raise exception 'Sign in first.'; end if;
  if (select count(*) from family_links where student_id = uid and revoked_at is null and expires_at > now()) >= 3 then
    raise exception 'You already have 3 active links. Stop one first.';
  end if;
  loop
    c := ''; for i in 1..12 loop c := c || substr(alphabet, 1 + floor(random()*32)::int, 1); end loop;
    exit when not exists (select 1 from family_links where code = c);
  end loop;
  insert into family_links(student_id, code, label) values (uid, c, nullif(left(trim(coalesce(p_label,'')),40),''));
  return c;
end $$;

create or replace function public.revoke_family_link(p_id uuid)
returns void language sql security definer set search_path = public as $$
  update public.family_links set revoked_at = now() where id = p_id and student_id = auth.uid() and revoked_at is null $$;

-- what the family page shows. Anyone holding a valid code can call this, so it returns the minimum.
create or replace function public.family_view(p_code text)
returns jsonb language plpgsql security definer set search_path = public as $$
declare l family_links; p profiles; s user_stats; week jsonb; subj jsonb; att jsonb; crs jsonb;
        norm text := upper(regexp_replace(coalesce(p_code,''), '[^A-Za-z0-9]', '', 'g'));
begin
  select * into l from family_links where family_links.code = norm and revoked_at is null and expires_at > now();
  if not found then return null; end if;
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
  return jsonb_build_object('first_name', p.first_name, 'level', p.level, 'streak', coalesce(s.streak,0), 'xp', coalesce(s.xp,0),
    'week', week, 'subjects', subj, 'attendance_30d', att, 'courses', crs, 'link_label', l.label, 'expires_at', l.expires_at);
end $$;

revoke all on function public.create_family_link(text), public.revoke_family_link(uuid), public.family_view(text) from public, anon;
grant execute on function public.create_family_link(text), public.revoke_family_link(uuid) to authenticated;
grant execute on function public.family_view(text) to anon, authenticated;
