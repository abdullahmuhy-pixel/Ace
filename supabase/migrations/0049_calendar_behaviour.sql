-- School calendar and the behaviour and welfare log.
--
-- Calendar: events, holidays, exam weeks and closures per school (terms already live in academic_terms).
-- Everyone in the school reads events meant for everyone; staff-only events are for staff. School admins edit.
--
-- Behaviour: merits, concerns and incidents recorded by the student's teachers or school admins, plus welfare notes
-- that only school admins can read. Entries marked for the family are shown to the student in the app.

-- ---------- calendar ----------
create table if not exists public.school_events (
  id         uuid primary key default gen_random_uuid(),
  school_id  uuid not null references public.schools(id) on delete cascade,
  title      text not null check (length(title) between 1 and 120),
  kind       text not null default 'event' check (kind in ('event','holiday','exam','closure','meeting','deadline')),
  starts_on  date not null,
  ends_on    date not null,
  audience   text not null default 'everyone' check (audience in ('everyone','staff')),
  note       text check (length(note) <= 500),
  created_by uuid references public.profiles(id) on delete set null,
  created_at timestamptz not null default now(),
  check (ends_on >= starts_on and ends_on <= starts_on + 120)
);
create index if not exists school_events_idx on public.school_events (school_id, starts_on);
alter table public.school_events enable row level security;
drop policy if exists school_events_read on public.school_events;
create policy school_events_read on public.school_events for select to authenticated
  using (public.is_platform_admin() or (school_id = public.my_school() and (audience = 'everyone' or public.is_staff())));
drop policy if exists school_events_admin on public.school_events;
create policy school_events_admin on public.school_events for all to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin())
  with check (public.is_school_admin_of(school_id) or public.is_platform_admin());
revoke all on public.school_events from anon;

-- ---------- behaviour and welfare ----------
create table if not exists public.behaviour_entries (
  id                uuid primary key default gen_random_uuid(),
  school_id         uuid not null references public.schools(id) on delete cascade,
  student_id        uuid not null references public.profiles(id) on delete cascade,
  kind              text not null check (kind in ('merit','concern','incident','welfare')),
  category          text check (length(category) <= 60),
  points            integer not null default 0 check (points between -10 and 10),
  description       text not null check (length(description) between 1 and 1000),
  action_taken      text check (length(action_taken) <= 500),
  visible_to_family boolean not null default false,
  occurred_on       date not null default current_date check (occurred_on <= current_date + 1),
  recorded_by       uuid references public.profiles(id) on delete set null default auth.uid(),
  created_at        timestamptz not null default now(),
  check (kind <> 'welfare' or not visible_to_family),
  check ((kind = 'merit' and points >= 0) or (kind in ('concern','incident') and points <= 0) or (kind = 'welfare' and points = 0))
);
create index if not exists behaviour_student_idx on public.behaviour_entries (student_id, occurred_on desc);
create index if not exists behaviour_school_idx on public.behaviour_entries (school_id, occurred_on desc);
alter table public.behaviour_entries enable row level security;

-- school admins: everything in their school
drop policy if exists behaviour_admin on public.behaviour_entries;
create policy behaviour_admin on public.behaviour_entries for all to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin())
  with check ((public.is_school_admin_of(school_id) or public.is_platform_admin())
              and exists (select 1 from public.profiles p where p.id = student_id and p.school_id = behaviour_entries.school_id and p.role = 'student'));
-- teachers: read and add merits, concerns and incidents for students they teach (never welfare)
drop policy if exists behaviour_teacher_read on public.behaviour_entries;
create policy behaviour_teacher_read on public.behaviour_entries for select to authenticated
  using (kind <> 'welfare' and public.teaches_student(student_id));
drop policy if exists behaviour_teacher_add on public.behaviour_entries;
create policy behaviour_teacher_add on public.behaviour_entries for insert to authenticated
  with check (kind <> 'welfare' and recorded_by = auth.uid() and public.teaches_student(student_id)
              and school_id = (select p.school_id from public.profiles p where p.id = student_id));
-- teachers may correct or remove their own entry on the day it was written
drop policy if exists behaviour_teacher_fix on public.behaviour_entries;
create policy behaviour_teacher_fix on public.behaviour_entries for update to authenticated
  using (recorded_by = auth.uid() and kind <> 'welfare' and created_at > now() - interval '24 hours')
  with check (recorded_by = auth.uid() and kind <> 'welfare' and public.teaches_student(student_id));
drop policy if exists behaviour_teacher_del on public.behaviour_entries;
create policy behaviour_teacher_del on public.behaviour_entries for delete to authenticated
  using (recorded_by = auth.uid() and kind <> 'welfare' and created_at > now() - interval '24 hours');
-- students: their own entries that were shared with the family
drop policy if exists behaviour_self on public.behaviour_entries;
create policy behaviour_self on public.behaviour_entries for select to authenticated
  using (student_id = auth.uid() and visible_to_family);
revoke all on public.behaviour_entries from anon;

-- one row per student of a class: merits, concerns and points over a period (for teachers of the class and admins)
create or replace function public.class_behaviour(p_class uuid, p_from date, p_to date)
returns table (student_id uuid, merits bigint, concerns bigint, points bigint, last_on date)
language sql stable security definer set search_path = public as $$
  select p.id,
         count(b.id) filter (where b.kind = 'merit'),
         count(b.id) filter (where b.kind in ('concern','incident')),
         coalesce(sum(b.points), 0),
         max(b.occurred_on)
  from public.profiles p
  left join public.class_members m on m.student_id = p.id and m.class_id = p_class
  left join public.behaviour_entries b on b.student_id = p.id and b.kind <> 'welfare' and b.occurred_on between p_from and p_to
  where p.role = 'student' and (p.class_id = p_class or m.class_id is not null)
    and (public.teaches_class(p_class) or public.is_school_admin_of(public.class_school(p_class)) or public.is_platform_admin())
  group by p.id $$;
revoke all on function public.class_behaviour(uuid, date, date) from public, anon;
grant execute on function public.class_behaviour(uuid, date, date) to authenticated;
