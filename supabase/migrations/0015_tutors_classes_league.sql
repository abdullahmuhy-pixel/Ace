-- 0015: tutors and tutoring centres, class join codes, students in more than one class, weekly XP league,
--       auto-scored assignments. Safe to run more than once.
--
-- Model
--   * A tutor (private teacher, after-school class, tutoring centre) gets a workspace: a row in schools with
--     kind = 'tutor'. The tutor is the school_admin of that workspace, so every existing staff tool works.
--   * Every class has a join code. A student keeps their own account and joins any number of classes with
--     codes (class_members). profiles.class_id stays as the student's main school class.
--   * Teachers see a student's work only while that student is in one of their classes.

-- ---------- 1. account kinds ----------
alter table public.schools  add column if not exists kind     text not null default 'school' check (kind in ('school','tutor'));
alter table public.schools  add column if not exists owner_id uuid references public.profiles(id) on delete set null;
alter table public.profiles add column if not exists account_type text not null default 'student'
  check (account_type in ('student','tutor','school_staff','parent','admin'));
update public.profiles set account_type = 'school_staff' where role in ('teacher','subject_teacher','school_admin') and account_type = 'student';
update public.profiles set account_type = 'admin' where role = 'platform_admin' and account_type = 'student';

-- ---------- 2. classes: join codes, subject, exam ----------
alter table public.classes add column if not exists join_code text unique;
alter table public.classes add column if not exists subject   text check (length(subject) <= 80);
alter table public.classes add column if not exists exam      text check (length(exam) <= 80);
alter table public.classes add column if not exists archived  boolean not null default false;
alter table public.classes add column if not exists created_at timestamptz not null default now();

create or replace function public.gen_join_code() returns text
language plpgsql as $$
declare alphabet constant text := 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'; c text; i int;
begin
  loop
    c := '';
    for i in 1..6 loop c := c || substr(alphabet, 1 + floor(random() * length(alphabet))::int, 1); end loop;
    exit when not exists (select 1 from public.classes where join_code = c);
  end loop;
  return c;
end $$;

create or replace function public.classes_code() returns trigger
language plpgsql as $$
begin
  if new.join_code is null or new.join_code = '' then new.join_code := public.gen_join_code(); end if;
  new.join_code := upper(new.join_code);
  return new;
end $$;
drop trigger if exists classes_code on public.classes;
create trigger classes_code before insert or update of join_code on public.classes
for each row execute function public.classes_code();
update public.classes set join_code = public.gen_join_code() where join_code is null;

-- ---------- 3. class members (students in tutor classes, or extra classes) ----------
create table if not exists public.class_members (
  class_id   uuid not null references public.classes(id) on delete cascade,
  student_id uuid not null references public.profiles(id) on delete cascade,
  joined_at  timestamptz not null default now(),
  primary key (class_id, student_id)
);
create index if not exists class_members_student_idx on public.class_members (student_id);
alter table public.class_members enable row level security;

-- ---------- 4. helpers ----------
create or replace function public.in_class(cid uuid) returns boolean
language sql stable security definer set search_path = public as
$$ select coalesce(cid = (select class_id from public.profiles where id = auth.uid())
       or exists (select 1 from public.class_members m where m.class_id = cid and m.student_id = auth.uid()), false) $$;

create or replace function public.student_in_class(sid uuid, cid uuid) returns boolean
language sql stable security definer set search_path = public as
$$ select exists (select 1 from public.profiles p where p.id = sid and p.class_id = cid and p.role = 'student')
       or exists (select 1 from public.class_members m where m.student_id = sid and m.class_id = cid) $$;

-- true when the caller teaches (or runs the school / workspace of) a class this student belongs to
create or replace function public.teaches_student(sid uuid) returns boolean
language sql stable security definer set search_path = public as
$$ select coalesce(
     public.is_platform_admin()
     or exists (select 1 from public.profiles p where p.id = sid and p.class_id is not null and public.teaches_class(p.class_id))
     or exists (select 1 from public.class_members m where m.student_id = sid and public.teaches_class(m.class_id)),
   false) $$;

drop policy if exists cm_self_read on public.class_members;
create policy cm_self_read on public.class_members for select to authenticated using (student_id = auth.uid());
drop policy if exists cm_self_leave on public.class_members;
create policy cm_self_leave on public.class_members for delete to authenticated using (student_id = auth.uid());
drop policy if exists cm_staff on public.class_members;
create policy cm_staff on public.class_members for all to authenticated
  using (public.teaches_class(class_id)) with check (public.teaches_class(class_id));
-- students have no insert policy: they join through join_class(); staff inserts must pass cm_staff
grant select, insert, delete on public.class_members to authenticated;

-- ---------- 5. policies widened to class members (nothing that was allowed before is removed) ----------
drop policy if exists classes_read on public.classes;
create policy classes_read on public.classes for select to authenticated
  using (school_id = public.my_school() or public.is_platform_admin() or public.in_class(id) or public.teaches_class(id));

drop policy if exists profiles_staff_read on public.profiles;
create policy profiles_staff_read on public.profiles for select to authenticated
  using (public.is_staff() and (school_id = public.my_school() or public.is_platform_admin() or public.teaches_student(id)));

drop policy if exists progress_staff_read on public.progress;
create policy progress_staff_read on public.progress for select to authenticated
  using (public.is_staff() and (public.teaches_student(user_id) or exists (
    select 1 from public.profiles p where p.id = user_id and (p.school_id = public.my_school() or public.is_platform_admin()))));

drop policy if exists quiz_staff_read on public.quiz_attempts;
create policy quiz_staff_read on public.quiz_attempts for select to authenticated
  using (public.is_staff() and (public.teaches_student(user_id) or exists (
    select 1 from public.profiles p where p.id = user_id and (p.school_id = public.my_school() or public.is_platform_admin()))));

drop policy if exists stats_staff_read on public.user_stats;
create policy stats_staff_read on public.user_stats for select to authenticated
  using (public.is_staff() and public.teaches_student(user_id));

drop policy if exists as_students on public.assessments;
create policy as_students on public.assessments for select to authenticated using (public.in_class(class_id));
drop policy if exists tasks_students on public.tasks;
create policy tasks_students on public.tasks for select to authenticated using (public.in_class(class_id));
drop policy if exists sub_self on public.task_submissions;
create policy sub_self on public.task_submissions for all to authenticated
  using (student_id = auth.uid())
  with check (student_id = auth.uid() and exists (select 1 from public.tasks t where t.id = task_id and public.in_class(t.class_id)));
drop policy if exists live_students on public.live_sessions;
create policy live_students on public.live_sessions for select to authenticated using (public.in_class(class_id));
drop policy if exists la_self_insert on public.live_answers;
create policy la_self_insert on public.live_answers for insert to authenticated
  with check (student_id = auth.uid() and exists (
    select 1 from public.live_sessions s where s.id = session_id and s.state = 'running' and public.in_class(s.class_id)));

drop policy if exists ann_read on public.announcements;
create policy ann_read on public.announcements for select to authenticated
  using (public.is_platform_admin()
         or (school_id = public.my_school() and (class_id is null or class_id = public.my_class() or public.is_staff()))
         or (class_id is not null and (public.in_class(class_id) or public.teaches_class(class_id))));

-- messages: a student may write to anyone who teaches one of their classes, and back
create or replace function public.can_message(rid uuid) returns boolean
language sql stable security definer set search_path = public as
$$ select exists (
     select 1 from public.profiles r, public.profiles s
     where r.id = rid and s.id = auth.uid() and r.school_id is not null and r.school_id = s.school_id
       and (r.role <> 'student' or s.role <> 'student'))
   or (public.is_staff() and public.teaches_student(rid))
   or exists (select 1 from public.class_members m join public.classes c on c.id = m.class_id
              where m.student_id = auth.uid()
                and (exists (select 1 from public.teacher_subjects t where t.class_id = c.id and t.teacher_id = rid)
                     or exists (select 1 from public.profiles r where r.id = rid and r.role = 'school_admin' and r.school_id = c.school_id))) $$;
create or replace function public.school_of(uid uuid) returns uuid
language sql stable security definer set search_path = public as
$$ select school_id from public.profiles where id = uid $$;
drop policy if exists msg_send on public.messages;
create policy msg_send on public.messages for insert to authenticated
  with check (sender_id = auth.uid() and public.can_message(recipient_id)
              and (school_id = public.my_school() or school_id = public.school_of(recipient_id)));

-- ---------- 6. joining and leaving classes ----------
create or replace function public.join_class(p_code text)
returns jsonb language plpgsql security definer set search_path = public as $$
declare c record; me record; t text;
begin
  select id, role into me from public.profiles where id = auth.uid();
  if me.id is null then raise exception 'Sign in first.'; end if;
  if me.role <> 'student' then raise exception 'Only student accounts can join a class with a code.'; end if;
  select cl.id, cl.name, cl.subject, cl.archived, s.name as school, s.kind into c
    from public.classes cl join public.schools s on s.id = cl.school_id
   where cl.join_code = upper(trim(p_code)) and s.active;
  if c.id is null or c.archived then raise exception 'No class with that code. Check it with your teacher.'; end if;
  insert into public.class_members (class_id, student_id) values (c.id, auth.uid()) on conflict do nothing;
  select string_agg(distinct p.first_name || ' ' || p.surname, ', ') into t
    from public.profiles p
   where p.id in (select teacher_id from public.teacher_subjects where class_id = c.id)
      or (p.role = 'school_admin' and p.school_id = (select school_id from public.classes where id = c.id) and c.kind = 'tutor');
  return jsonb_build_object('class_id', c.id, 'name', c.name, 'subject', c.subject, 'school', c.school, 'kind', c.kind, 'teachers', t);
end $$;
revoke all on function public.join_class(text) from public, anon;
grant execute on function public.join_class(text) to authenticated;

create or replace function public.leave_class(p_class uuid) returns void
language sql security definer set search_path = public as
$$ delete from public.class_members where class_id = p_class and student_id = auth.uid() $$;
revoke all on function public.leave_class(uuid) from public, anon;
grant execute on function public.leave_class(uuid) to authenticated;

create or replace function public.my_classes()
returns table (class_id uuid, name text, subject text, exam text, school text, kind text, teachers text, main boolean)
language sql stable security definer set search_path = public as $$
  select c.id, c.name, c.subject, c.exam, s.name, s.kind,
         (select string_agg(distinct p.first_name || ' ' || p.surname, ', ') from public.profiles p
           where p.id in (select teacher_id from public.teacher_subjects where class_id = c.id)
              or (s.kind = 'tutor' and p.role = 'school_admin' and p.school_id = s.id)),
         coalesce(c.id = (select class_id from public.profiles where id = auth.uid()), false)
  from public.classes c join public.schools s on s.id = c.school_id
  where public.in_class(c.id) and not c.archived
  order by 8 desc, c.name $$;
revoke all on function public.my_classes() from public, anon;
grant execute on function public.my_classes() to authenticated;

-- teachers a student can message: school teachers of the main class, plus teachers of joined classes
drop function if exists public.my_teachers();
create or replace function public.my_teachers()
returns table (teacher_id uuid, first_name text, surname text, subject text, school_id uuid)
language sql stable security definer set search_path = public as $$
  select distinct t.teacher_id, p.first_name, p.surname, coalesce(t.subject, c.subject, c.name), c.school_id
  from public.classes c join public.teacher_subjects t on t.class_id = c.id join public.profiles p on p.id = t.teacher_id
  where public.in_class(c.id) and (select role from public.profiles where id = auth.uid()) = 'student'
  union
  select distinct p.id, p.first_name, p.surname, coalesce(c.subject, c.name), s.id
  from public.classes c join public.schools s on s.id = c.school_id
  join public.profiles p on p.school_id = s.id and p.role = 'school_admin'
  where s.kind = 'tutor' and public.in_class(c.id) and (select role from public.profiles where id = auth.uid()) = 'student' $$;
revoke all on function public.my_teachers() from public, anon;
grant execute on function public.my_teachers() to authenticated;

-- one row per student in a class with the numbers a teacher needs on the dashboard
create or replace function public.class_roster(p_class uuid)
returns table (student_id uuid, first_name text, surname text, username text, student_number text, class_level text,
               exam_target text, xp integer, streak integer, last_day date, last_seen_at timestamptz,
               answered bigint, correct bigint, joined_at timestamptz)
language sql stable security definer set search_path = public as $$
  select p.id, p.first_name, p.surname, p.username, p.student_number, p.class_level, p.exam_target,
         coalesce(s.xp,0), coalesce(s.streak,0), s.last_day, p.last_seen_at,
         coalesce((select sum(q.total) from public.quiz_attempts q where q.user_id = p.id),0),
         coalesce((select sum(q.correct) from public.quiz_attempts q where q.user_id = p.id),0),
         m.joined_at
  from public.profiles p
  left join public.user_stats s on s.user_id = p.id
  left join public.class_members m on m.student_id = p.id and m.class_id = p_class
  where public.teaches_class(p_class) and p.role = 'student'
    and (p.class_id = p_class or m.class_id is not null)
  order by p.surname, p.first_name $$;
revoke all on function public.class_roster(uuid) from public, anon;
grant execute on function public.class_roster(uuid) to authenticated;

-- ---------- 7. weekly XP league ----------
alter table public.user_stats add column if not exists week_start date;
alter table public.user_stats add column if not exists week_xp integer not null default 0 check (week_xp >= 0);
alter table public.profiles   add column if not exists league_hidden boolean not null default false;
grant update (league_hidden) on public.profiles to authenticated;

create or replace function public.track_week_xp() returns trigger
language plpgsql as $$
declare wk date := date_trunc('week', now())::date; d integer;
begin
  d := greatest(0, new.xp - coalesce(case when tg_op = 'UPDATE' then old.xp end, 0));
  if new.week_start is distinct from wk then new.week_start := wk; new.week_xp := d;
  else new.week_xp := coalesce(new.week_xp, 0) + d; end if;
  return new;
end $$;
drop trigger if exists stats_week on public.user_stats;
create trigger stats_week before insert or update of xp on public.user_stats
for each row execute function public.track_week_xp();

-- top learners this week in the caller's country (first name + surname initial only), plus the caller's own row
create or replace function public.weekly_league()
returns table (rank bigint, name text, xp integer, me boolean)
language sql stable security definer set search_path = public as $$
  with mine as (select country_code from public.profiles where id = auth.uid()),
  board as (
    select p.id, p.first_name || ' ' || left(p.surname, 1) || '.' as name, s.week_xp,
           rank() over (order by s.week_xp desc) as rk
    from public.user_stats s join public.profiles p on p.id = s.user_id
    where p.role = 'student' and not p.league_hidden and s.week_start = date_trunc('week', now())::date
      and s.week_xp > 0 and p.country_code = (select country_code from mine))
  select rk, name, week_xp, id = auth.uid() from board where rk <= 30 or id = auth.uid() order by rk limit 31 $$;
revoke all on function public.weekly_league() from public, anon;
grant execute on function public.weekly_league() to authenticated;

-- ---------- 8. assignments scored by the app ----------
-- A task with topic_ref {kind:'quiz'|'lesson'|'mock', exam, subject, topic} is done inside the student app.
-- The app stores the student's score in auto_score (0-100); teachers still own mark and feedback.
alter table public.task_submissions add column if not exists auto_score numeric check (auto_score between 0 and 100);
alter table public.tasks add column if not exists kind text not null default 'written'
  check (kind in ('written','quiz','lesson','mock','reading','video','link'));
alter table public.tasks add column if not exists link_url text check (length(link_url) <= 500);
alter table public.tasks add column if not exists rubric jsonb;

-- ---------- 9. lock the new helpers to signed-in users ----------
do $$
declare f record;
begin
  for f in select p.oid::regprocedure as sig from pg_proc p join pg_namespace n on n.oid = p.pronamespace
           where n.nspname = 'public' and p.proname in ('in_class','teaches_student','gen_join_code','school_of') loop
    execute format('revoke execute on function %s from public, anon', f.sig);
    execute format('grant execute on function %s to authenticated, service_role', f.sig);
  end loop;
end $$;
