-- Row-level security. Principle: students see only themselves; staff see only
-- their own school; platform_admin sees everything. Sensitive writes (creating
-- accounts, schools, role changes) go through edge functions using the service role.

-- ---------- helper functions (security definer so policies don't recurse) ----------
create or replace function public.my_role() returns public.app_role
language sql stable security definer set search_path = public as
$$ select role from public.profiles where id = auth.uid() $$;

create or replace function public.my_school() returns uuid
language sql stable security definer set search_path = public as
$$ select school_id from public.profiles where id = auth.uid() $$;

create or replace function public.is_staff() returns boolean
language sql stable security definer set search_path = public as
$$ select coalesce(public.my_role() in ('teacher','subject_teacher','school_admin','platform_admin'), false) $$;

create or replace function public.is_platform_admin() returns boolean
language sql stable security definer set search_path = public as
$$ select coalesce(public.my_role() = 'platform_admin', false) $$;

create or replace function public.is_school_admin_of(sid uuid) returns boolean
language sql stable security definer set search_path = public as
$$ select exists (select 1 from public.profiles
                  where id = auth.uid() and role = 'school_admin' and school_id = sid) $$;

-- ---------- enable RLS everywhere ----------
alter table public.countries        enable row level security;
alter table public.schools          enable row level security;
alter table public.classes          enable row level security;
alter table public.profiles         enable row level security;
alter table public.teacher_subjects enable row level security;
alter table public.progress         enable row level security;
alter table public.quiz_attempts    enable row level security;
alter table public.user_stats       enable row level security;
alter table public.login_attempts   enable row level security;   -- no policies: service role only
alter table public.audit_log        enable row level security;   -- no policies: service role only

-- ---------- countries: public read ----------
drop policy if exists countries_read on public.countries;
create policy countries_read on public.countries for select using (true);

-- ---------- schools ----------
drop policy if exists schools_read on public.schools;
create policy schools_read on public.schools for select to authenticated
  using (id = public.my_school() or public.is_platform_admin());

drop policy if exists schools_update on public.schools;
create policy schools_update on public.schools for update to authenticated
  using (public.is_school_admin_of(id) or public.is_platform_admin())
  with check (public.is_school_admin_of(id) or public.is_platform_admin());

-- ---------- classes ----------
drop policy if exists classes_read on public.classes;
create policy classes_read on public.classes for select to authenticated
  using (school_id = public.my_school() or public.is_platform_admin());

drop policy if exists classes_write on public.classes;
create policy classes_write on public.classes for all to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin())
  with check (public.is_school_admin_of(school_id) or public.is_platform_admin());

-- ---------- profiles ----------
drop policy if exists profiles_self_read on public.profiles;
create policy profiles_self_read on public.profiles for select to authenticated
  using (id = auth.uid());

drop policy if exists profiles_staff_read on public.profiles;
create policy profiles_staff_read on public.profiles for select to authenticated
  using (public.is_staff() and (school_id = public.my_school() or public.is_platform_admin()));

drop policy if exists profiles_self_update on public.profiles;
create policy profiles_self_update on public.profiles for update to authenticated
  using (id = auth.uid()) with check (id = auth.uid());

drop policy if exists profiles_admin_update on public.profiles;
create policy profiles_admin_update on public.profiles for update to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin())
  with check (public.is_school_admin_of(school_id) or public.is_platform_admin());

-- Column-level lock: users may only change these columns themselves. Role, school,
-- username, student number and consent are changed by edge functions (service role).
revoke update on public.profiles from authenticated, anon;
grant  update (first_name, surname, language, exam_target, class_level, last_seen_at)
  on public.profiles to authenticated;
revoke insert, delete on public.profiles from authenticated, anon;

-- ---------- teacher_subjects ----------
drop policy if exists ts_read on public.teacher_subjects;
create policy ts_read on public.teacher_subjects for select to authenticated
  using (teacher_id = auth.uid()
         or exists (select 1 from public.classes c
                    where c.id = class_id and (c.school_id = public.my_school()) and public.is_staff())
         or public.is_platform_admin());

drop policy if exists ts_write on public.teacher_subjects;
create policy ts_write on public.teacher_subjects for all to authenticated
  using (exists (select 1 from public.classes c where c.id = class_id and public.is_school_admin_of(c.school_id))
         or public.is_platform_admin())
  with check (exists (select 1 from public.classes c where c.id = class_id and public.is_school_admin_of(c.school_id))
         or public.is_platform_admin());

-- ---------- progress / quiz attempts / stats ----------
drop policy if exists progress_self on public.progress;
create policy progress_self on public.progress for all to authenticated
  using (user_id = auth.uid()) with check (user_id = auth.uid());

drop policy if exists progress_staff_read on public.progress;
create policy progress_staff_read on public.progress for select to authenticated
  using (public.is_staff() and exists (
    select 1 from public.profiles p
    where p.id = user_id and (p.school_id = public.my_school() or public.is_platform_admin())));

drop policy if exists quiz_self_read on public.quiz_attempts;
create policy quiz_self_read on public.quiz_attempts for select to authenticated
  using (user_id = auth.uid());

drop policy if exists quiz_self_insert on public.quiz_attempts;
create policy quiz_self_insert on public.quiz_attempts for insert to authenticated
  with check (user_id = auth.uid());

drop policy if exists quiz_staff_read on public.quiz_attempts;
create policy quiz_staff_read on public.quiz_attempts for select to authenticated
  using (public.is_staff() and exists (
    select 1 from public.profiles p
    where p.id = user_id and (p.school_id = public.my_school() or public.is_platform_admin())));

drop policy if exists stats_self on public.user_stats;
create policy stats_self on public.user_stats for all to authenticated
  using (user_id = auth.uid()) with check (user_id = auth.uid());

drop policy if exists stats_staff_read on public.user_stats;
create policy stats_staff_read on public.user_stats for select to authenticated
  using (public.is_staff() and exists (
    select 1 from public.profiles p
    where p.id = user_id and (p.school_id = public.my_school() or public.is_platform_admin())));

-- quiz attempts are append-only for students
revoke update, delete on public.quiz_attempts from authenticated, anon;

-- tables with no policies must also have no grants
revoke all on public.login_attempts, public.audit_log from anon, authenticated;
