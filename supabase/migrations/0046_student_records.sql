-- Student records: school admission numbers, enrolment status with history, and a record card per student.
-- Also fixes moving students between classes: profiles.class_id is not in the column grants, so the portal's
-- direct update failed; school admins now move students through move_students().

-- ---------- admission numbers (per school, e.g. GRF-2026-0142) ----------
alter table public.schools add column if not exists admission_prefix text check (admission_prefix is null or admission_prefix ~ '^[A-Z0-9]{1,10}$');
alter table public.schools add column if not exists admission_seq    integer not null default 0 check (admission_seq >= 0);
alter table public.schools add column if not exists admission_digits integer not null default 4 check (admission_digits between 3 and 6);
alter table public.schools add column if not exists admission_year   boolean not null default true;

alter table public.profiles add column if not exists admission_no      text check (admission_no is null or length(admission_no) between 1 and 30);
alter table public.profiles add column if not exists enrolment_status  text not null default 'active'
  check (enrolment_status in ('active','suspended','withdrawn','transferred','graduated'));
alter table public.profiles add column if not exists status_changed_at timestamptz;
create unique index if not exists profiles_admission_no_uq on public.profiles (school_id, admission_no) where admission_no is not null;

create or replace function public.next_admission_no(p_school uuid) returns text
language plpgsql security definer set search_path = public as $$
declare s public.schools; n text;
begin
  loop
    update public.schools set admission_seq = admission_seq + 1 where id = p_school and admission_prefix is not null returning * into s;
    if not found then return null; end if;
    n := s.admission_prefix || case when s.admission_year then '-' || to_char(now(), 'YYYY') else '' end || '-' || lpad(s.admission_seq::text, s.admission_digits, '0');
    exit when not exists (select 1 from public.profiles where school_id = p_school and admission_no = n);
  end loop;
  return n;
end $$;

-- every new student in a numbering school gets the next number; a student who changes school gets a new one
create or replace function public.assign_admission_no() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if new.role = 'student' and new.school_id is not null then
    if tg_op = 'UPDATE' and new.school_id is distinct from old.school_id and new.admission_no is not distinct from old.admission_no then
      new.admission_no := null;
    end if;
    if new.admission_no is null then new.admission_no := public.next_admission_no(new.school_id); end if;
  end if;
  return new;
end $$;
drop trigger if exists profiles_admission_no on public.profiles;
create trigger profiles_admission_no before insert or update of school_id on public.profiles
for each row execute function public.assign_admission_no();

-- ---------- the record card ----------
create table if not exists public.student_records (
  student_id      uuid primary key references public.profiles(id) on delete cascade,
  school_id       uuid not null references public.schools(id) on delete cascade,
  date_of_birth   date check (date_of_birth between date '1930-01-01' and current_date),
  gender          text check (length(gender) <= 30),
  address         text check (length(address) <= 300),
  phone           text check (length(phone) <= 30),
  previous_school text check (length(previous_school) <= 120),
  admitted_on     date,
  left_on         date,
  leaving_reason  text check (length(leaving_reason) <= 300),
  destination     text check (length(destination) <= 120),
  notes           text check (length(notes) <= 2000),
  updated_by      uuid references public.profiles(id) on delete set null,
  updated_at      timestamptz not null default now()
);
alter table public.student_records enable row level security;
drop policy if exists student_records_admin on public.student_records;
create policy student_records_admin on public.student_records for all to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin())
  with check ((public.is_school_admin_of(school_id) or public.is_platform_admin())
              and exists (select 1 from public.profiles p where p.id = student_id and p.school_id = student_records.school_id and p.role = 'student'));
drop policy if exists student_records_teacher_read on public.student_records;
create policy student_records_teacher_read on public.student_records for select to authenticated
  using (public.teaches_student(student_id));
revoke all on public.student_records from anon;

create table if not exists public.enrolment_events (
  id           bigint generated always as identity primary key,
  student_id   uuid not null references public.profiles(id) on delete cascade,
  school_id    uuid not null references public.schools(id) on delete cascade,
  from_status  text,
  to_status    text not null,
  effective_on date not null default current_date,
  reason       text check (length(reason) <= 300),
  actor        uuid references public.profiles(id) on delete set null,
  created_at   timestamptz not null default now()
);
create index if not exists enrolment_events_student_idx on public.enrolment_events (student_id, created_at);
alter table public.enrolment_events enable row level security;
drop policy if exists enrolment_events_read on public.enrolment_events;
create policy enrolment_events_read on public.enrolment_events for select to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin());
revoke insert, update, delete on public.enrolment_events from anon, authenticated;
revoke select on public.enrolment_events from anon;

-- ---------- actions for school admins ----------
create or replace function public._admin_of_student(p_student uuid) returns uuid
language plpgsql stable security definer set search_path = public as $$
declare s uuid;
begin
  select school_id into s from public.profiles where id = p_student and role = 'student';
  if s is null or not (public.is_school_admin_of(s) or public.is_platform_admin()) then
    raise exception 'You do not have permission to do that.';
  end if;
  return s;
end $$;

-- Leaving statuses take the student out of their classes (they no longer use a seat) but keep the record.
create or replace function public.set_enrolment_status(p_student uuid, p_status text, p_reason text default null, p_effective date default current_date)
returns text language plpgsql security definer set search_path = public as $$
declare s uuid; old text; leaving boolean := p_status in ('withdrawn','transferred','graduated');
begin
  s := public._admin_of_student(p_student);
  if p_status not in ('active','suspended','withdrawn','transferred','graduated') then raise exception 'Unknown status.'; end if;
  select enrolment_status into old from public.profiles where id = p_student for update;
  if old = p_status then raise exception 'The student already has that status.'; end if;
  update public.profiles set enrolment_status = p_status, status_changed_at = now(),
         class_id = case when leaving then null else class_id end
   where id = p_student;
  if leaving then
    delete from public.class_members m using public.classes c where c.id = m.class_id and c.school_id = s and m.student_id = p_student;
  end if;
  insert into public.student_records (student_id, school_id) values (p_student, s) on conflict (student_id) do nothing;
  update public.student_records set
         left_on = case when leaving then coalesce(p_effective, current_date) when p_status = 'active' then null else left_on end,
         leaving_reason = case when leaving then nullif(trim(p_reason), '') when p_status = 'active' then null else leaving_reason end,
         updated_by = auth.uid(), updated_at = now()
   where student_id = p_student;
  insert into public.enrolment_events (student_id, school_id, from_status, to_status, effective_on, reason, actor)
  values (p_student, s, old, p_status, coalesce(p_effective, current_date), nullif(trim(p_reason), ''), auth.uid());
  return p_status;
end $$;

create or replace function public.set_admission_no(p_student uuid, p_no text) returns text
language plpgsql security definer set search_path = public as $$
declare s uuid; n text := nullif(upper(trim(p_no)), '');
begin
  s := public._admin_of_student(p_student);
  if n is not null and n !~ '^[A-Z0-9/-]{1,30}$' then raise exception 'Use letters, digits, - and / only.'; end if;
  if n is not null and exists (select 1 from public.profiles where school_id = s and admission_no = n and id <> p_student) then
    raise exception 'Another student already has that number.';
  end if;
  update public.profiles set admission_no = n where id = p_student;
  return n;
end $$;

-- gives a number to every student in the caller's school who has none, oldest first
create or replace function public.number_students(p_school uuid) returns integer
language plpgsql security definer set search_path = public as $$
declare r record; k int := 0;
begin
  if not (public.is_school_admin_of(p_school) or public.is_platform_admin()) then raise exception 'You do not have permission to do that.'; end if;
  if (select admission_prefix from public.schools where id = p_school) is null then raise exception 'Set a prefix for admission numbers first.'; end if;
  for r in select id from public.profiles where school_id = p_school and role = 'student' and admission_no is null order by created_at, surname loop
    update public.profiles set admission_no = public.next_admission_no(p_school) where id = r.id; k := k + 1;
  end loop;
  return k;
end $$;

-- move students into a class of the same school (also used for "move a whole class")
create or replace function public.move_students(p_students uuid[], p_class uuid) returns integer
language plpgsql security definer set search_path = public as $$
declare s uuid; k int;
begin
  select school_id into s from public.classes where id = p_class;
  if s is null or not (public.is_school_admin_of(s) or public.is_platform_admin()) then raise exception 'You do not have permission to do that.'; end if;
  update public.profiles set class_id = p_class
   where id = any(p_students) and school_id = s and role = 'student' and enrolment_status in ('active','suspended');
  get diagnostics k = row_count;
  return k;
end $$;

-- students who have left no longer count towards the school's seats
create or replace function public.school_students(p_school uuid) returns integer
language sql stable security definer set search_path = public as $$
  select count(*)::int from (
    select p.id from public.profiles p where p.school_id = p_school and p.role = 'student' and p.enrolment_status in ('active','suspended')
    union
    select cm.student_id from public.class_members cm join public.classes c on c.id = cm.class_id where c.school_id = p_school) x $$;

revoke all on function public.next_admission_no(uuid), public.assign_admission_no(), public._admin_of_student(uuid), public.school_students(uuid) from public, anon, authenticated;
revoke all on function public.set_enrolment_status(uuid, text, text, date), public.set_admission_no(uuid, text),
  public.number_students(uuid), public.move_students(uuid[], uuid) from public, anon;
grant execute on function public.set_enrolment_status(uuid, text, text, date), public.set_admission_no(uuid, text),
  public.number_students(uuid), public.move_students(uuid[], uuid) to authenticated;
