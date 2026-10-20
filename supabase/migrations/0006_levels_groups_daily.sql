-- 0006: education levels (secondary -> university), shared "group" plans (1 payer + up to 3 members),
-- "what my teacher taught today" notes, spaced revision, and study goals for the roadmap.
-- Idempotent. Run after 0005.

-- ---------- levels ----------
alter table public.profiles add column if not exists level text not null default 'secondary';
alter table public.profiles add column if not exists institution text;
alter table public.profiles add column if not exists programme text;
alter table public.profiles add column if not exists study_year smallint;
do $$ begin
  alter table public.profiles add constraint profiles_level_chk check (level in ('secondary','university','other'));
exception when duplicate_object then null; end $$;
do $$ begin
  alter table public.profiles add constraint profiles_year_chk check (study_year is null or study_year between 1 and 8);
exception when duplicate_object then null; end $$;

-- a user changes only these presentation fields about themselves (never role, school or country)
create or replace function public.set_my_level(p_level text, p_institution text, p_programme text, p_year int)
returns void language plpgsql security definer set search_path = public as $$
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  if p_level not in ('secondary','university','other') then raise exception 'bad level'; end if;
  update public.profiles set level = p_level,
    institution = left(nullif(trim(p_institution), ''), 120),
    programme   = left(nullif(trim(p_programme), ''), 120),
    study_year  = case when p_level = 'university' then p_year else null end
  where id = auth.uid() and role = 'student';
end $$;
revoke all on function public.set_my_level(text,text,text,int) from public, anon;
grant execute on function public.set_my_level(text,text,text,int) to authenticated;

-- ---------- study goals (drive the roadmap) ----------
create table if not exists public.student_goals (
  user_id           uuid primary key references public.profiles(id) on delete cascade,
  target_course     text,
  target_university text,
  target_country    text references public.countries(code),
  target_result     text,          -- e.g. "5 credits incl. Maths and English", "AAB", "3.8 GPA"
  target_year       smallint check (target_year between 2020 and 2100),
  updated_at        timestamptz not null default now()
);
alter table public.student_goals enable row level security;
drop policy if exists goals_own on public.student_goals;
create policy goals_own on public.student_goals for all to authenticated
  using (user_id = auth.uid()) with check (user_id = auth.uid());

-- ---------- group plans ----------
alter table public.plans add column if not exists seats smallint not null default 1;
do $$ begin
  alter table public.plans add constraint plans_seats_chk check (seats between 1 and 4);
exception when duplicate_object then null; end $$;

create table if not exists public.plan_seats (
  id             uuid primary key default gen_random_uuid(),
  entitlement_id uuid not null references public.entitlements(id) on delete cascade,
  member_id      uuid not null references public.profiles(id) on delete cascade,
  relation       text check (relation in ('friend','sibling','child','classmate','other')),
  joined_at      timestamptz not null default now(),
  removed_at     timestamptz,
  removed_by     uuid references public.profiles(id) on delete set null
);
-- a person holds at most one active seat
create unique index if not exists plan_seats_one_active on public.plan_seats (member_id) where removed_at is null;
create index if not exists plan_seats_ent on public.plan_seats (entitlement_id) where removed_at is null;

create table if not exists public.plan_invites (
  code           text primary key,
  entitlement_id uuid not null references public.entitlements(id) on delete cascade,
  created_by     uuid not null references public.profiles(id) on delete cascade,
  relation       text check (relation in ('friend','sibling','child','classmate','other')),
  expires_at     timestamptz not null default now() + interval '7 days',
  used_by        uuid references public.profiles(id) on delete set null,
  used_at        timestamptz,
  created_at     timestamptz not null default now()
);
create index if not exists plan_invites_ent on public.plan_invites (entitlement_id);

alter table public.plan_seats   enable row level security;
alter table public.plan_invites enable row level security;
-- writes only through the functions below
revoke insert, update, delete on public.plan_seats, public.plan_invites from anon, authenticated;
drop policy if exists seats_read on public.plan_seats;
create policy seats_read on public.plan_seats for select to authenticated
  using (member_id = auth.uid()
      or exists (select 1 from public.entitlements e where e.id = entitlement_id and e.user_id = auth.uid()));
drop policy if exists invites_read on public.plan_invites;
create policy invites_read on public.plan_invites for select to authenticated
  using (exists (select 1 from public.entitlements e where e.id = entitlement_id and e.user_id = auth.uid()));

-- access check usable by edge functions (service role) and by has_access()
create or replace function public.user_has_access(p_user uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (
    select 1 from public.entitlements e
    where (e.user_id = p_user or e.school_id = (select school_id from public.profiles where id = p_user))
      and ((e.status = 'active'   and coalesce(e.current_period_end, 'infinity') > now())
        or (e.status = 'trialing' and coalesce(e.trial_ends_at, '-infinity') > now())))
  or exists (   -- a seat in someone else's paid (not trial) group plan
    select 1 from public.plan_seats s join public.entitlements e on e.id = s.entitlement_id
    where s.member_id = p_user and s.removed_at is null
      and e.status = 'active' and coalesce(e.current_period_end, 'infinity') > now()) $$;
revoke all on function public.user_has_access(uuid) from public, anon, authenticated;
grant execute on function public.user_has_access(uuid) to service_role;

create or replace function public.has_access() returns boolean
language sql stable security definer set search_path = public as $$
  select public.user_has_access(auth.uid()) $$;

-- the paid group entitlement the caller owns, with its seat limit
create or replace function public._my_group(p_lock boolean default false)
returns table (ent_id uuid, seats int) language plpgsql security definer set search_path = public as $$
begin
  return query
  select e.id, pl.seats::int from public.entitlements e join public.plans pl on pl.code = e.plan_code
  where e.user_id = auth.uid() and e.status = 'active' and coalesce(e.current_period_end,'infinity') > now()
    and pl.seats > 1
  order by pl.seats desc, e.current_period_end desc nulls last limit 1;
end $$;
revoke all on function public._my_group(boolean) from public, anon, authenticated;

-- owner creates an invite code. Seats in use + unused invites can never exceed seats - 1 (the owner takes one).
create or replace function public.create_invite(p_relation text default 'friend')
returns text language plpgsql security definer set search_path = public as $$
declare g record; used int; pending int; c text;
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  select * into g from public._my_group();
  if g.ent_id is null then raise exception 'You need an active group plan to invite people.'; end if;
  perform 1 from public.entitlements where id = g.ent_id for update;
  select count(*) into used from public.plan_seats where entitlement_id = g.ent_id and removed_at is null;
  select count(*) into pending from public.plan_invites
    where entitlement_id = g.ent_id and used_at is null and expires_at > now();
  if used + pending >= g.seats - 1 then raise exception 'All seats are taken or already reserved by invites.'; end if;
  c := upper(substr(replace(gen_random_uuid()::text, '-', ''), 1, 8));
  insert into public.plan_invites(code, entitlement_id, created_by, relation)
    values (c, g.ent_id, auth.uid(), case when p_relation in ('friend','sibling','child','classmate','other') then p_relation else 'other' end);
  return c;
end $$;
revoke all on function public.create_invite(text) from public, anon;
grant execute on function public.create_invite(text) to authenticated;

-- member joins with a code. One active seat per person; 30-day wait after leaving or being removed;
-- an owner of a paid plan cannot also take a seat; students of a school licence may still join.
create or replace function public.join_plan(p_code text)
returns void language plpgsql security definer set search_path = public as $$
declare i record; used int; lim int;
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  select * into i from public.plan_invites where code = upper(trim(p_code)) for update;
  if not found or i.used_at is not null or i.expires_at <= now() then raise exception 'This invite is not valid.'; end if;
  if i.created_by = auth.uid() then raise exception 'You cannot use your own invite.'; end if;
  perform 1 from public.entitlements e where e.id = i.entitlement_id and e.status = 'active'
    and coalesce(e.current_period_end,'infinity') > now() for update;
  if not found then raise exception 'This plan is no longer active.'; end if;
  if exists (select 1 from public.plan_seats where member_id = auth.uid() and removed_at is null) then
    raise exception 'You already have a seat in a group plan. Leave it first.'; end if;
  if exists (select 1 from public.plan_seats where member_id = auth.uid() and removed_at > now() - interval '30 days') then
    raise exception 'You can switch group plans once every 30 days.'; end if;
  if exists (select 1 from public.entitlements e join public.plans p on p.code = e.plan_code
             where e.user_id = auth.uid() and e.status = 'active' and p.seats > 1
               and coalesce(e.current_period_end,'infinity') > now()) then
    raise exception 'You already pay for a group plan.'; end if;
  select pl.seats into lim from public.entitlements e join public.plans pl on pl.code = e.plan_code where e.id = i.entitlement_id;
  select count(*) into used from public.plan_seats where entitlement_id = i.entitlement_id and removed_at is null;
  if used >= lim - 1 then raise exception 'This plan is full.'; end if;
  insert into public.plan_seats(entitlement_id, member_id, relation) values (i.entitlement_id, auth.uid(), i.relation);
  update public.plan_invites set used_by = auth.uid(), used_at = now() where code = i.code;
end $$;
revoke all on function public.join_plan(text) from public, anon;
grant execute on function public.join_plan(text) to authenticated;

-- owner removes a member, or a member leaves (p_member = null)
create or replace function public.leave_or_remove(p_member uuid default null)
returns void language plpgsql security definer set search_path = public as $$
declare tgt uuid := coalesce(p_member, auth.uid()); n int;
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  update public.plan_seats s set removed_at = now(), removed_by = auth.uid()
   where s.member_id = tgt and s.removed_at is null
     and (tgt = auth.uid() or exists (select 1 from public.entitlements e where e.id = s.entitlement_id and e.user_id = auth.uid()));
  get diagnostics n = row_count;
  if n = 0 then raise exception 'No such seat.'; end if;
end $$;
revoke all on function public.leave_or_remove(uuid) from public, anon;
grant execute on function public.leave_or_remove(uuid) to authenticated;

-- owner sees who holds seats: names, relation, joined and last active. Never scores or chats.
create or replace function public.my_group_members()
returns table (member_id uuid, first_name text, surname text, relation text, level text, joined_at timestamptz, last_seen_at timestamptz)
language sql stable security definer set search_path = public as $$
  select s.member_id, p.first_name, p.surname, s.relation, p.level, s.joined_at, p.last_seen_at
  from public.plan_seats s join public.entitlements e on e.id = s.entitlement_id join public.profiles p on p.id = s.member_id
  where e.user_id = auth.uid() and s.removed_at is null order by s.joined_at $$;
revoke all on function public.my_group_members() from public, anon;
grant execute on function public.my_group_members() to authenticated;

-- ---------- "what my teacher taught today" ----------
create table if not exists public.class_notes (
  id            uuid primary key default gen_random_uuid(),
  user_id       uuid not null references public.profiles(id) on delete cascade,
  taught_on     date not null default current_date,
  exam          text,
  subject       text not null check (length(subject) between 1 and 80),
  entered_text  text not null check (length(entered_text) between 3 and 2000),
  topic         text check (length(topic) <= 160),      -- matched syllabus topic, if any
  summary       jsonb,                                   -- AI output: {summary, key_terms, example, questions}
  created_at    timestamptz not null default now()
);
create index if not exists class_notes_user on public.class_notes (user_id, taught_on desc);
alter table public.class_notes enable row level security;
drop policy if exists notes_own on public.class_notes;
create policy notes_own on public.class_notes for all to authenticated
  using (user_id = auth.uid()) with check (user_id = auth.uid());

-- at most 30 notes a day per student
create or replace function public.limit_notes() returns trigger language plpgsql as $$
begin
  if (select count(*) from public.class_notes where user_id = new.user_id and created_at > now() - interval '1 day') >= 30 then
    raise exception 'Daily note limit reached.'; end if;
  return new;
end $$;
drop trigger if exists trg_limit_notes on public.class_notes;
create trigger trg_limit_notes before insert on public.class_notes for each row execute function public.limit_notes();

-- ---------- spaced revision ----------
create table if not exists public.revision_items (
  id        uuid primary key default gen_random_uuid(),
  user_id   uuid not null references public.profiles(id) on delete cascade,
  note_id   uuid references public.class_notes(id) on delete set null,
  exam      text,
  subject   text not null,
  topic     text not null,
  step      smallint not null default 0 check (step between 0 and 5),
  due_on    date not null default current_date + 1,
  done_at   timestamptz,
  created_at timestamptz not null default now(),
  unique (user_id, exam, subject, topic)
);
create index if not exists rev_due on public.revision_items (user_id, due_on) where done_at is null;
alter table public.revision_items enable row level security;
drop policy if exists rev_read on public.revision_items;
create policy rev_read on public.revision_items for select to authenticated using (user_id = auth.uid());
drop policy if exists rev_delete on public.revision_items;
create policy rev_delete on public.revision_items for delete to authenticated using (user_id = auth.uid());
revoke insert, update on public.revision_items from anon, authenticated;   -- scheduling only via the functions

create or replace function public.add_revision(p_exam text, p_subject text, p_topic text, p_note uuid default null)
returns uuid language plpgsql security definer set search_path = public as $$
declare r uuid;
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  if length(coalesce(p_subject,'')) = 0 or length(coalesce(p_topic,'')) = 0 then raise exception 'subject and topic needed'; end if;
  if p_note is not null and not exists (select 1 from public.class_notes where id = p_note and user_id = auth.uid()) then
    raise exception 'unknown note'; end if;
  insert into public.revision_items(user_id, note_id, exam, subject, topic)
    values (auth.uid(), p_note, left(p_exam,60), left(p_subject,80), left(p_topic,160))
  on conflict (user_id, exam, subject, topic) do update set done_at = null, step = 0, due_on = current_date + 1
  returning id into r;
  return r;
end $$;
revoke all on function public.add_revision(text,text,text,uuid) from public, anon;
grant execute on function public.add_revision(text,text,text,uuid) to authenticated;

-- steps: review after 1, 3, 7, 21, 45 days. A wrong answer sends the item back to tomorrow.
create or replace function public.complete_revision(p_id uuid, p_correct boolean)
returns date language plpgsql security definer set search_path = public as $$
declare it record; gaps int[] := array[1,3,7,21,45]; ns int; nd date;
begin
  select * into it from public.revision_items where id = p_id and user_id = auth.uid() for update;
  if not found then raise exception 'unknown item'; end if;
  if it.due_on > current_date then raise exception 'not due yet'; end if;
  if not p_correct then ns := 0; nd := current_date + 1;
  elsif it.step >= 4 then update public.revision_items set done_at = now(), step = 5 where id = p_id; return null;
  else ns := it.step + 1; nd := current_date + gaps[ns + 1]; end if;
  update public.revision_items set step = ns, due_on = nd where id = p_id;
  return nd;
end $$;
revoke all on function public.complete_revision(uuid,boolean) from public, anon;
grant execute on function public.complete_revision(uuid,boolean) to authenticated;

-- what the Share screen needs: am I a payer, a member, or neither
create or replace function public.my_plan_status()
returns table (kind text, seats int, used int, pending int, expires timestamptz, plan_name text)
language plpgsql stable security definer set search_path = public as $$
declare g record;
begin
  select * into g from public._my_group();
  if g.ent_id is not null then
    return query select 'owner'::text, g.seats,
      (select count(*)::int from public.plan_seats where entitlement_id = g.ent_id and removed_at is null),
      (select count(*)::int from public.plan_invites where entitlement_id = g.ent_id and used_at is null and expires_at > now()),
      e.current_period_end, pl.name
    from public.entitlements e join public.plans pl on pl.code = e.plan_code where e.id = g.ent_id;
    return;
  end if;
  return query select 'member'::text, pl.seats::int, null::int, null::int, e.current_period_end, pl.name
    from public.plan_seats s join public.entitlements e on e.id = s.entitlement_id join public.plans pl on pl.code = e.plan_code
    where s.member_id = auth.uid() and s.removed_at is null limit 1;
  if not found then return query select 'none'::text, null::int, null::int, null::int, null::timestamptz, null::text; end if;
end $$;
revoke all on function public.my_plan_status() from public, anon;
grant execute on function public.my_plan_status() to authenticated;
