-- Admissions: online applications to a school, document uploads, staff review, and enrolment into a class.
-- Applicants never sign in. They submit through the public `admissions` edge function and get a reference plus a
-- private status code (only its SHA-256 hash is stored). Staff read applications through RLS (school admins of that
-- school, and the Ace team); every status change goes through the service-role functions below, so each one is logged.

-- ---------- school settings ----------
alter table public.schools add column if not exists admissions_open   boolean not null default false;
alter table public.schools add column if not exists admissions_note   text check (length(admissions_note) <= 800);
alter table public.schools add column if not exists admissions_grades text[] not null default '{}';
alter table public.schools add column if not exists admissions_docs   text[] not null default '{}';
alter table public.schools add column if not exists admissions_email  citext check (admissions_email is null or admissions_email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$');

-- ---------- applications ----------
create table if not exists public.applications (
  id                uuid primary key default gen_random_uuid(),
  school_id         uuid not null references public.schools(id) on delete cascade,
  reference         text not null unique check (reference ~ '^AP[0-9]{2}-[A-HJ-NP-Z2-9]{6}$'),
  code_hash         text not null check (code_hash ~ '^[0-9a-f]{64}$'),
  status            text not null default 'submitted'
                    check (status in ('submitted','reviewing','interview','waitlisted','accepted','declined','withdrawn','enrolled')),
  -- applicant
  first_name        text not null check (length(first_name) between 1 and 60),
  surname           text not null check (length(surname) between 1 and 60),
  date_of_birth     date check (date_of_birth between date '1930-01-01' and current_date),
  gender            text check (length(gender) <= 30),
  grade_applied     text not null check (length(grade_applied) between 1 and 40),
  start_term        text check (length(start_term) <= 40),
  exam_target       text check (length(exam_target) <= 60),
  previous_school   text check (length(previous_school) <= 120),
  applicant_email   citext check (applicant_email is null or applicant_email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  applicant_phone   text check (length(applicant_phone) <= 30),
  address           text check (length(address) <= 300),
  -- parent or guardian
  guardian_name     text check (length(guardian_name) <= 80),
  guardian_relation text check (length(guardian_relation) <= 40),
  guardian_email    citext check (guardian_email is null or guardian_email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  guardian_phone    text check (length(guardian_phone) <= 30),
  message           text check (length(message) <= 1500),          -- from the applicant
  consent_at        timestamptz not null,
  -- staff side
  staff_note        text check (length(staff_note) <= 2000),       -- internal, never shown to the applicant
  class_id          uuid references public.classes(id) on delete set null,
  student_id        uuid references public.profiles(id) on delete set null,
  decided_by        uuid references public.profiles(id) on delete set null,
  decided_at        timestamptz,
  created_at        timestamptz not null default now(),
  updated_at        timestamptz not null default now(),
  check (applicant_email is not null or guardian_email is not null or applicant_phone is not null or guardian_phone is not null)
);
create index if not exists applications_school_idx on public.applications (school_id, status, created_at desc);

create table if not exists public.application_documents (
  id             uuid primary key default gen_random_uuid(),
  application_id uuid not null references public.applications(id) on delete cascade,
  kind           text not null check (length(kind) between 1 and 60),
  file_name      text not null check (length(file_name) between 1 and 120),
  mime           text not null check (mime in ('application/pdf','image/jpeg','image/png')),
  size_bytes     integer not null check (size_bytes between 1 and 5242880),
  path           text not null unique,
  uploaded_at    timestamptz,
  created_at     timestamptz not null default now()
);
create index if not exists application_documents_app_idx on public.application_documents (application_id);

create table if not exists public.application_events (
  id             bigint generated always as identity primary key,
  application_id uuid not null references public.applications(id) on delete cascade,
  actor          uuid references public.profiles(id) on delete set null,   -- null = the applicant
  from_status    text,
  to_status      text,
  note           text check (length(note) <= 2000),      -- internal
  message        text check (length(message) <= 1500),   -- shown to the applicant on the status page and by email
  created_at     timestamptz not null default now()
);
create index if not exists application_events_app_idx on public.application_events (application_id, created_at);

-- ---------- RLS: staff read; nobody writes directly ----------
alter table public.applications          enable row level security;
alter table public.application_documents enable row level security;
alter table public.application_events    enable row level security;

drop policy if exists applications_read on public.applications;
create policy applications_read on public.applications for select to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin());

drop policy if exists application_documents_read on public.application_documents;
create policy application_documents_read on public.application_documents for select to authenticated
  using (exists (select 1 from public.applications a where a.id = application_id
                 and (public.is_school_admin_of(a.school_id) or public.is_platform_admin())));

drop policy if exists application_events_read on public.application_events;
create policy application_events_read on public.application_events for select to authenticated
  using (exists (select 1 from public.applications a where a.id = application_id
                 and (public.is_school_admin_of(a.school_id) or public.is_platform_admin())));

revoke insert, update, delete on public.applications, public.application_documents, public.application_events from anon, authenticated;
revoke select on public.applications, public.application_documents, public.application_events from anon;

-- ---------- helpers (service role only) ----------
create or replace function public.gen_application_ref() returns text
language plpgsql as $$
declare a text := 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; r text;
begin
  loop
    r := 'AP' || to_char(now(), 'YY') || '-' || (select string_agg(substr(a, 1 + floor(random() * 32)::int, 1), '') from generate_series(1, 6));
    exit when not exists (select 1 from public.applications where reference = r);
  end loop;
  return r;
end $$;

-- Staff decisions and applicant withdrawals. Returns the new status. Rules:
--   withdrawn and enrolled are final; enrolled is set only by application_mark_enrolled;
--   withdrawn only by the applicant (p_actor null); staff can reopen a declined application.
create or replace function public.application_transition(p_app uuid, p_to text, p_actor uuid, p_note text default null, p_message text default null)
returns text language plpgsql security definer set search_path = public as $$
declare a public.applications;
begin
  select * into a from public.applications where id = p_app for update;
  if not found then raise exception 'Application not found.'; end if;
  if p_to not in ('reviewing','interview','waitlisted','accepted','declined','withdrawn') then raise exception 'That status cannot be set here.'; end if;
  if a.status in ('withdrawn','enrolled') then raise exception 'This application is closed.'; end if;
  if a.status = p_to then raise exception 'The application already has that status.'; end if;
  if p_to = 'withdrawn' and p_actor is not null then raise exception 'Only the applicant can withdraw an application.'; end if;
  if p_to <> 'withdrawn' and p_actor is null then raise exception 'Only staff can change this status.'; end if;
  if p_actor is not null and not exists (select 1 from public.profiles p where p.id = p_actor
       and ((p.role = 'school_admin' and p.school_id = a.school_id) or p.role = 'platform_admin')) then
    raise exception 'You do not have permission to do that.';
  end if;
  update public.applications set status = p_to, updated_at = now(),
         decided_by = case when p_to in ('accepted','declined') then p_actor else decided_by end,
         decided_at = case when p_to in ('accepted','declined') then now() else decided_at end
   where id = p_app;
  insert into public.application_events (application_id, actor, from_status, to_status, note, message)
  values (p_app, p_actor, a.status, p_to, nullif(trim(p_note), ''), nullif(trim(p_message), ''));
  return p_to;
end $$;

create or replace function public.application_mark_enrolled(p_app uuid, p_student uuid, p_class uuid, p_actor uuid)
returns void language plpgsql security definer set search_path = public as $$
declare a public.applications;
begin
  select * into a from public.applications where id = p_app for update;
  if not found then raise exception 'Application not found.'; end if;
  if a.status <> 'accepted' then raise exception 'Accept the application before enrolling.'; end if;
  if not exists (select 1 from public.classes c where c.id = p_class and c.school_id = a.school_id) then raise exception 'That class belongs to another school.'; end if;
  if not exists (select 1 from public.profiles p where p.id = p_student and p.school_id = a.school_id and p.role = 'student') then raise exception 'Student account not found in this school.'; end if;
  update public.applications set status = 'enrolled', student_id = p_student, class_id = p_class, updated_at = now() where id = p_app;
  insert into public.application_events (application_id, actor, from_status, to_status, message)
  values (p_app, p_actor, 'accepted', 'enrolled', 'Your place is confirmed and your Ace account has been created.');
end $$;

create or replace function public.application_set_note(p_app uuid, p_actor uuid, p_note text)
returns void language plpgsql security definer set search_path = public as $$
begin
  if not exists (select 1 from public.applications a join public.profiles p on p.id = p_actor
                  where a.id = p_app and ((p.role = 'school_admin' and p.school_id = a.school_id) or p.role = 'platform_admin')) then
    raise exception 'You do not have permission to do that.';
  end if;
  update public.applications set staff_note = nullif(trim(p_note), ''), updated_at = now() where id = p_app;
end $$;

-- Personal data is not kept forever: declined and withdrawn applications go after a year.
-- Returns the storage paths of their documents so the caller can delete the files too.
create or replace function public.purge_old_applications(p_days int default 365)
returns setof text language sql security definer set search_path = public as $$
  with gone as (
    delete from public.applications where status in ('declined','withdrawn') and updated_at < now() - make_interval(days => p_days) returning id
  ) select d.path from public.application_documents d where d.application_id in (select id from gone)
$$;

revoke execute on function public.gen_application_ref(), public.application_transition(uuid, text, uuid, text, text),
  public.application_mark_enrolled(uuid, uuid, uuid, uuid), public.application_set_note(uuid, uuid, text),
  public.purge_old_applications(int) from public, anon, authenticated;
grant execute on function public.gen_application_ref(), public.application_transition(uuid, text, uuid, text, text),
  public.application_mark_enrolled(uuid, uuid, uuid, uuid), public.application_set_note(uuid, uuid, text),
  public.purge_old_applications(int) to service_role;

-- ---------- private storage bucket for the uploaded documents (Supabase only) ----------
do $$ begin
  if exists (select 1 from pg_namespace where nspname = 'storage') and exists (select 1 from information_schema.tables where table_schema = 'storage' and table_name = 'buckets') then
    insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
    values ('admissions', 'admissions', false, 5242880, array['application/pdf','image/jpeg','image/png'])
    on conflict (id) do nothing;
  end if;
end $$;
