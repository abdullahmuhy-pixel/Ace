-- 0016: classroom tools for teachers, tutors and school admins, plus dashboard analytics.
--   curriculum pacing, class Q&A board, class library, live-lesson link, rubrics, timetables, fees,
--   class / school / platform insight functions. Needs 0015. Safe to run more than once.

-- ---------- plans can be sold to tutors too ----------
alter table public.plans drop constraint if exists plans_audience_check;
alter table public.plans add constraint plans_audience_check check (audience in ('student','school','tutor'));

-- ---------- live lesson link on a class ----------
alter table public.classes add column if not exists meet_url text check (meet_url is null or meet_url ~* '^https://');

-- ---------- curriculum pacing: which syllabus topics a class has been taught ----------
create table if not exists public.class_pacing (
  class_id     uuid not null references public.classes(id) on delete cascade,
  subject      text not null check (length(subject) <= 80),
  topic        text not null check (length(topic) <= 200),
  planned_week date,
  taught_on    date,
  note         text check (length(note) <= 300),
  updated_by   uuid references public.profiles(id) on delete set null,
  updated_at   timestamptz not null default now(),
  primary key (class_id, subject, topic)
);
alter table public.class_pacing enable row level security;
drop policy if exists pacing_staff on public.class_pacing;
create policy pacing_staff on public.class_pacing for all to authenticated
  using (public.teaches_class(class_id)) with check (public.teaches_class(class_id));
drop policy if exists pacing_students on public.class_pacing;
create policy pacing_students on public.class_pacing for select to authenticated using (public.in_class(class_id));

-- ---------- class Q&A board ----------
create table if not exists public.class_questions (
  id          bigint generated always as identity primary key,
  class_id    uuid not null references public.classes(id) on delete cascade,
  author_id   uuid not null references public.profiles(id) on delete cascade,
  subject     text check (length(subject) <= 80),
  body        text not null check (length(body) between 3 and 1000),
  answer      text check (length(answer) <= 3000),
  answered_by uuid references public.profiles(id) on delete set null,
  answered_at timestamptz,
  hidden      boolean not null default false,
  created_at  timestamptz not null default now()
);
create index if not exists cq_class_idx on public.class_questions (class_id, created_at desc);
alter table public.class_questions enable row level security;
drop policy if exists cq_read on public.class_questions;
create policy cq_read on public.class_questions for select to authenticated
  using (public.teaches_class(class_id) or (public.in_class(class_id) and (not hidden or author_id = auth.uid())));
drop policy if exists cq_ask on public.class_questions;
create policy cq_ask on public.class_questions for insert to authenticated
  with check (author_id = auth.uid() and public.in_class(class_id) and answer is null and answered_by is null and not hidden);
drop policy if exists cq_staff on public.class_questions;
create policy cq_staff on public.class_questions for update to authenticated
  using (public.teaches_class(class_id)) with check (public.teaches_class(class_id));
drop policy if exists cq_delete on public.class_questions;
create policy cq_delete on public.class_questions for delete to authenticated
  using (public.teaches_class(class_id) or (author_id = auth.uid() and answer is null));
create or replace function public.cq_stamp() returns trigger
language plpgsql as $$
begin
  if new.answer is distinct from old.answer then new.answered_by := auth.uid(); new.answered_at := now(); end if;
  return new;
end $$;
drop trigger if exists cq_stamp on public.class_questions;
create trigger cq_stamp before update on public.class_questions for each row execute function public.cq_stamp();

-- ---------- class library: links, notes and videos shared with a class ----------
create table if not exists public.class_resources (
  id         uuid primary key default gen_random_uuid(),
  class_id   uuid not null references public.classes(id) on delete cascade,
  title      text not null check (length(title) between 1 and 140),
  kind       text not null default 'link' check (kind in ('link','note','video','file')),
  url        text check (url is null or url ~* '^https://'),
  body       text check (length(body) <= 6000),
  subject    text check (length(subject) <= 80),
  created_by uuid references public.profiles(id) on delete set null,
  created_at timestamptz not null default now()
);
create index if not exists cr_class_idx on public.class_resources (class_id, created_at desc);
alter table public.class_resources enable row level security;
drop policy if exists cr_staff on public.class_resources;
create policy cr_staff on public.class_resources for all to authenticated
  using (public.teaches_class(class_id)) with check (public.teaches_class(class_id));
drop policy if exists cr_students on public.class_resources;
create policy cr_students on public.class_resources for select to authenticated using (public.in_class(class_id));

-- ---------- reusable marking rubrics ----------
create table if not exists public.rubrics (
  id         uuid primary key default gen_random_uuid(),
  owner_id   uuid not null default auth.uid() references public.profiles(id) on delete cascade,
  title      text not null check (length(title) between 1 and 120),
  criteria   jsonb not null default '[]',      -- [{name, max, levels:[{label, desc}]}]
  created_at timestamptz not null default now()
);
alter table public.rubrics enable row level security;
drop policy if exists rubrics_own on public.rubrics;
create policy rubrics_own on public.rubrics for all to authenticated
  using (owner_id = auth.uid()) with check (owner_id = auth.uid() and public.is_staff());

-- ---------- timetables ----------
create table if not exists public.timetable_slots (
  id         uuid primary key default gen_random_uuid(),
  school_id  uuid not null references public.schools(id) on delete cascade,
  class_id   uuid not null references public.classes(id) on delete cascade,
  weekday    smallint not null check (weekday between 1 and 7),
  starts     time not null,
  ends       time not null check (ends > starts),
  subject    text not null check (length(subject) <= 80),
  teacher_id uuid references public.profiles(id) on delete set null,
  room       text check (length(room) <= 40)
);
create index if not exists tt_class_idx on public.timetable_slots (class_id, weekday, starts);
alter table public.timetable_slots enable row level security;
drop policy if exists tt_admin on public.timetable_slots;
create policy tt_admin on public.timetable_slots for all to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin())
  with check ((public.is_school_admin_of(school_id) or public.is_platform_admin()) and public.class_school(class_id) = school_id);
drop policy if exists tt_read on public.timetable_slots;
create policy tt_read on public.timetable_slots for select to authenticated
  using ((public.is_staff() and school_id = public.my_school()) or public.in_class(class_id) or public.teaches_class(class_id));

-- ---------- school fees (record keeping only; payments happen outside Ace) ----------
create table if not exists public.fees (
  id            uuid primary key default gen_random_uuid(),
  school_id     uuid not null references public.schools(id) on delete cascade,
  student_id    uuid not null references public.profiles(id) on delete cascade,
  term          text not null check (length(term) between 1 and 40),
  amount        numeric(12,2) not null check (amount >= 0),
  paid          numeric(12,2) not null default 0 check (paid >= 0),
  currency_code text not null check (currency_code ~ '^[A-Z]{3}$'),
  due_on        date,
  note          text check (length(note) <= 300),
  updated_at    timestamptz not null default now(),
  unique (student_id, term)
);
alter table public.fees enable row level security;
drop policy if exists fees_admin on public.fees;
create policy fees_admin on public.fees for all to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin())
  with check ((public.is_school_admin_of(school_id) or public.is_platform_admin())
              and exists (select 1 from public.profiles p where p.id = student_id and p.school_id = fees.school_id));
drop policy if exists fees_self on public.fees;
create policy fees_self on public.fees for select to authenticated using (student_id = auth.uid());
drop trigger if exists fees_touch on public.fees;
create trigger fees_touch before update on public.fees for each row execute function public.touch_updated_at();

-- ---------- insight functions for dashboards ----------
-- One row per student in a class (school class or joined class) with activity and results.
create or replace function public.class_insights(p_class uuid)
returns table (student_id uuid, first_name text, surname text, username text, student_number text, class_level text,
               xp integer, streak integer, last_day date, last_seen_at timestamptz, attempts_30d bigint,
               avg_pct_30d numeric, answered bigint, topics_mastered bigint, attendance_pct numeric, joined_at timestamptz, via text)
language sql stable security definer set search_path = public as $$
  with st as (
    select p.*, m.joined_at, case when p.class_id = p_class then 'school' else 'code' end as via
    from public.profiles p left join public.class_members m on m.student_id = p.id and m.class_id = p_class
    where p.role = 'student' and (p.class_id = p_class or m.class_id is not null))
  select st.id, st.first_name, st.surname, st.username, st.student_number, st.class_level,
         coalesce(s.xp,0), coalesce(s.streak,0), s.last_day, st.last_seen_at,
         (select count(*) from public.quiz_attempts a where a.user_id = st.id and a.created_at > now() - interval '30 days'),
         (select round(100.0*sum(a.correct)/nullif(sum(a.total),0),1) from public.quiz_attempts a where a.user_id = st.id and a.created_at > now() - interval '30 days'),
         coalesce((select sum(a.total) from public.quiz_attempts a where a.user_id = st.id),0),
         (select count(*) from public.progress g where g.user_id = st.id and g.status = 'mastered'),
         (select round(100.0*count(*) filter (where t.status in ('present','late'))/nullif(count(*),0),0) from public.attendance t where t.student_id = st.id and t.class_id = p_class),
         st.joined_at, st.via
  from st left join public.user_stats s on s.user_id = st.id
  where public.teaches_class(p_class)
  order by st.surname, st.first_name $$;

-- Average score by subject for the students of a class (last 60 days).
create or replace function public.class_subject_perf(p_class uuid)
returns table (subject text, attempts bigint, students bigint, avg_pct numeric)
language sql stable security definer set search_path = public as $$
  select a.subject, count(*), count(distinct a.user_id), round(100.0*sum(a.correct)/nullif(sum(a.total),0),1)
  from public.quiz_attempts a
  where public.teaches_class(p_class) and a.kind <> 'daily' and a.created_at > now() - interval '60 days'
    and a.user_id in (select p.id from public.profiles p where p.class_id = p_class
                      union select m.student_id from public.class_members m where m.class_id = p_class)
  group by a.subject order by 4 nulls last $$;

-- Topics the class finds hardest (needs at least 2 attempts on the topic).
create or replace function public.class_topic_perf(p_class uuid)
returns table (subject text, topic text, attempts bigint, students bigint, avg_pct numeric)
language sql stable security definer set search_path = public as $$
  select a.subject, a.topic, count(*), count(distinct a.user_id), round(100.0*sum(a.correct)/nullif(sum(a.total),0),1)
  from public.quiz_attempts a
  where public.teaches_class(p_class) and a.topic is not null and a.created_at > now() - interval '90 days'
    and a.user_id in (select p.id from public.profiles p where p.class_id = p_class
                      union select m.student_id from public.class_members m where m.class_id = p_class)
  group by a.subject, a.topic having count(*) >= 2 order by 5, 3 desc limit 40 $$;

-- Practice activity per day for the last 30 days.
create or replace function public.class_activity(p_class uuid)
returns table (day date, attempts bigint, active bigint)
language sql stable security definer set search_path = public as $$
  select d::date, count(a.id), count(distinct a.user_id)
  from generate_series((now() - interval '29 days')::date, now()::date, interval '1 day') d
  left join public.quiz_attempts a on a.created_at::date = d::date
    and a.user_id in (select p.id from public.profiles p where p.class_id = p_class
                      union select m.student_id from public.class_members m where m.class_id = p_class)
  where public.teaches_class(p_class)
  group by d order by d $$;

-- School admin overview: every class with its size, activity and average.
create or replace function public.school_summary()
returns table (class_id uuid, name text, grade text, students bigint, active_7d bigint, avg_pct numeric, teachers text, join_code text)
language sql stable security definer set search_path = public as $$
  select c.id, c.name, c.grade,
         (select count(*) from public.profiles p where p.role = 'student' and (p.class_id = c.id or p.id in (select student_id from public.class_members m where m.class_id = c.id))),
         (select count(distinct a.user_id) from public.quiz_attempts a where a.created_at > now() - interval '7 days'
            and a.user_id in (select p.id from public.profiles p where p.class_id = c.id union select m.student_id from public.class_members m where m.class_id = c.id)),
         (select round(100.0*sum(a.correct)/nullif(sum(a.total),0),1) from public.quiz_attempts a where a.kind <> 'daily' and a.created_at > now() - interval '60 days'
            and a.user_id in (select p.id from public.profiles p where p.class_id = c.id union select m.student_id from public.class_members m where m.class_id = c.id)),
         (select string_agg(distinct p.first_name || ' ' || p.surname, ', ') from public.teacher_subjects t join public.profiles p on p.id = t.teacher_id where t.class_id = c.id),
         c.join_code
  from public.classes c
  where c.school_id = (select school_id from public.profiles where id = auth.uid())
    and (public.is_school_admin_of(c.school_id) or public.is_platform_admin())
    and not c.archived
  order by c.grade, c.name $$;

-- Founder console: platform-wide numbers. Platform admins only.
create or replace function public.platform_overview()
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare r jsonb;
begin
  if not public.is_platform_admin() then raise exception 'Platform admins only.'; end if;
  select jsonb_build_object(
    'students',       (select count(*) from profiles where role = 'student'),
    'independent',    (select count(*) from profiles where role = 'student' and school_id is null),
    'tutors',         (select count(*) from schools where kind = 'tutor'),
    'schools',        (select count(*) from schools where kind = 'school'),
    'teachers',       (select count(*) from profiles where role in ('teacher','subject_teacher')),
    'classes',        (select count(*) from classes where not archived),
    'active_today',   (select count(*) from user_stats where last_day = current_date),
    'active_7d',      (select count(distinct user_id) from quiz_attempts where created_at > now() - interval '7 days'),
    'answers_7d',     (select coalesce(sum(total),0) from quiz_attempts where created_at > now() - interval '7 days'),
    'signups', (select coalesce(jsonb_agg(jsonb_build_object('day', d, 'n', n) order by d), '[]') from (
        select g::date d, (select count(*) from profiles p where p.created_at::date = g::date) n
        from generate_series((now() - interval '29 days')::date, now()::date, interval '1 day') g) x),
    'by_country', (select coalesce(jsonb_agg(jsonb_build_object('cc', country_code, 'students', s, 'teachers', t) order by s desc), '[]') from (
        select country_code, count(*) filter (where role = 'student') s, count(*) filter (where role <> 'student') t
        from profiles group by country_code) y),
    'revenue', (select coalesce(jsonb_agg(jsonb_build_object('currency', currency_code, 'total', total, 'count', n)), '[]') from (
        select currency_code, sum(amount_minor)/100.0 total, count(*) n from payments where status in ('successful','paid','succeeded') group by currency_code) z),
    'ai_7d', (select coalesce(sum(count),0) from ai_usage where day > current_date - 7)
  ) into r;
  return r;
end $$;

do $$
declare f record;
begin
  for f in select p.oid::regprocedure as sig from pg_proc p join pg_namespace n on n.oid = p.pronamespace
           where n.nspname = 'public' and p.proname in ('class_insights','class_subject_perf','class_topic_perf','class_activity','school_summary','platform_overview') loop
    execute format('revoke execute on function %s from public, anon', f.sig);
    execute format('grant execute on function %s to authenticated', f.sig);
  end loop;
end $$;
