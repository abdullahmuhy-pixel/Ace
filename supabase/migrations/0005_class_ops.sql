-- Ace Education 0005: class operations, server-side AI cap, plans, promo codes, parent contacts,
-- live quiz, push subscriptions, content reports. Everything here is behind row-level security.
-- Ideas taken from MatricAce's teacher/admin portals, rebuilt on Ace's auth model: Supabase Auth users,
-- one profiles row each, and no password columns anywhere. Run after 0004.

-- ---------- helpers ----------
create or replace function public.my_class() returns uuid
language sql stable security definer set search_path = public as
$$ select class_id from public.profiles where id = auth.uid() $$;

-- true when the caller runs this class: its school admin, a teacher or subject teacher assigned to it, or platform admin
create or replace function public.teaches_class(cid uuid) returns boolean
language sql stable security definer set search_path = public as
$$ select coalesce(
     public.is_platform_admin()
     or exists (select 1 from public.classes c where c.id = cid and public.is_school_admin_of(c.school_id))
     or exists (select 1 from public.teacher_subjects t where t.class_id = cid and t.teacher_id = auth.uid()),
   false) $$;

create or replace function public.student_in_class(sid uuid, cid uuid) returns boolean
language sql stable security definer set search_path = public as
$$ select exists (select 1 from public.profiles p where p.id = sid and p.class_id = cid and p.role = 'student') $$;

create or replace function public.class_school(cid uuid) returns uuid
language sql stable security definer set search_path = public as
$$ select school_id from public.classes where id = cid $$;

-- ---------- attendance ----------
create table if not exists public.attendance (
  class_id   uuid not null references public.classes(id) on delete cascade,
  student_id uuid not null references public.profiles(id) on delete cascade,
  day        date not null,
  status     text not null check (status in ('present','absent','late','excused')),
  noted_by   uuid references public.profiles(id) on delete set null,
  primary key (class_id, student_id, day)
);
create index if not exists attendance_student_idx on public.attendance (student_id, day desc);
alter table public.attendance enable row level security;
drop policy if exists att_staff on public.attendance;
create policy att_staff on public.attendance for all to authenticated
  using (public.teaches_class(class_id))
  with check (public.teaches_class(class_id) and public.student_in_class(student_id, class_id));
drop policy if exists att_self on public.attendance;
create policy att_self on public.attendance for select to authenticated using (student_id = auth.uid());

-- ---------- continuous assessment (SBA) ----------
create table if not exists public.assessments (
  id         uuid primary key default gen_random_uuid(),
  class_id   uuid not null references public.classes(id) on delete cascade,
  subject    text not null,
  title      text not null check (length(title) between 1 and 120),
  kind       text not null default 'test' check (kind in ('test','task','oral','project','exam')),
  max_mark   numeric not null check (max_mark > 0),
  weight     numeric not null default 0 check (weight between 0 and 100),
  held_on    date,
  created_by uuid references public.profiles(id) on delete set null,
  created_at timestamptz not null default now()
);
create index if not exists assessments_class_idx on public.assessments (class_id, subject);
alter table public.assessments enable row level security;
drop policy if exists as_staff on public.assessments;
create policy as_staff on public.assessments for all to authenticated
  using (public.teaches_class(class_id)) with check (public.teaches_class(class_id));
drop policy if exists as_students on public.assessments;
create policy as_students on public.assessments for select to authenticated using (class_id = public.my_class());

create table if not exists public.marks (
  assessment_id uuid not null references public.assessments(id) on delete cascade,
  student_id    uuid not null references public.profiles(id) on delete cascade,
  mark          numeric not null check (mark >= 0),
  comment       text check (length(comment) <= 500),
  updated_at    timestamptz not null default now(),
  primary key (assessment_id, student_id)
);
alter table public.marks enable row level security;
drop policy if exists marks_staff on public.marks;
create policy marks_staff on public.marks for all to authenticated
  using (exists (select 1 from public.assessments a where a.id = assessment_id and public.teaches_class(a.class_id)))
  with check (exists (select 1 from public.assessments a where a.id = assessment_id and public.teaches_class(a.class_id)
                      and public.student_in_class(student_id, a.class_id)));
drop policy if exists marks_self on public.marks;
create policy marks_self on public.marks for select to authenticated using (student_id = auth.uid());

create or replace function public.check_mark() returns trigger
language plpgsql as $$
declare mx numeric;
begin
  select max_mark into mx from public.assessments where id = new.assessment_id;
  if new.mark > mx then raise exception 'mark % is above the maximum %', new.mark, mx; end if;
  new.updated_at := now();
  return new;
end $$;
drop trigger if exists marks_check on public.marks;
create trigger marks_check before insert or update on public.marks for each row execute function public.check_mark();

-- weighted continuous-assessment percentage per student and subject (weights of 0 are ignored)
create or replace view public.sba_summary with (security_invoker = true) as
select a.class_id, m.student_id, a.subject,
       round(100.0 * sum(m.mark / a.max_mark * a.weight) / nullif(sum(a.weight), 0), 1) as weighted_pct,
       sum(a.weight) as weight_total,
       count(*) as items
from public.marks m join public.assessments a on a.id = m.assessment_id
where a.weight > 0
group by a.class_id, m.student_id, a.subject;
grant select on public.sba_summary to authenticated;

-- ---------- tasks and submissions ----------
create table if not exists public.tasks (
  id         uuid primary key default gen_random_uuid(),
  class_id   uuid not null references public.classes(id) on delete cascade,
  subject    text,
  title      text not null check (length(title) between 1 and 160),
  body       text check (length(body) <= 4000),
  due_on     date,
  topic_ref  jsonb,           -- {exam, subject, topic}: lets a task point at a syllabus topic
  created_by uuid references public.profiles(id) on delete set null,
  created_at timestamptz not null default now()
);
alter table public.tasks enable row level security;
drop policy if exists tasks_staff on public.tasks;
create policy tasks_staff on public.tasks for all to authenticated
  using (public.teaches_class(class_id)) with check (public.teaches_class(class_id));
drop policy if exists tasks_students on public.tasks;
create policy tasks_students on public.tasks for select to authenticated using (class_id = public.my_class());

create table if not exists public.task_submissions (
  task_id      uuid not null references public.tasks(id) on delete cascade,
  student_id   uuid not null references public.profiles(id) on delete cascade,
  body         text check (length(body) <= 8000),
  submitted_at timestamptz not null default now(),
  mark         numeric check (mark >= 0),
  feedback     text check (length(feedback) <= 2000),
  marked_by    uuid references public.profiles(id) on delete set null,
  primary key (task_id, student_id)
);
alter table public.task_submissions enable row level security;
drop policy if exists sub_self on public.task_submissions;
create policy sub_self on public.task_submissions for all to authenticated
  using (student_id = auth.uid())
  with check (student_id = auth.uid() and exists (select 1 from public.tasks t where t.id = task_id and t.class_id = public.my_class()));
drop policy if exists sub_staff on public.task_submissions;
create policy sub_staff on public.task_submissions for all to authenticated
  using (exists (select 1 from public.tasks t where t.id = task_id and public.teaches_class(t.class_id)))
  with check (exists (select 1 from public.tasks t where t.id = task_id and public.teaches_class(t.class_id)));

-- students can write their answer but never their own mark or feedback
create or replace function public.guard_submission() returns trigger
language plpgsql as $$
begin
  if not public.is_staff() then
    if tg_op = 'INSERT' then
      new.mark := null; new.feedback := null; new.marked_by := null;
    else
      new.mark := old.mark; new.feedback := old.feedback; new.marked_by := old.marked_by;
    end if;
  elsif new.mark is distinct from old.mark or new.feedback is distinct from old.feedback then
    new.marked_by := auth.uid();
  end if;
  return new;
end $$;
drop trigger if exists sub_guard on public.task_submissions;
create trigger sub_guard before insert or update on public.task_submissions for each row execute function public.guard_submission();

-- ---------- announcements ----------
create table if not exists public.announcements (
  id         uuid primary key default gen_random_uuid(),
  school_id  uuid not null references public.schools(id) on delete cascade,
  class_id   uuid references public.classes(id) on delete cascade,   -- null = whole school
  title      text not null check (length(title) between 1 and 140),
  body       text not null check (length(body) <= 4000),
  created_by uuid references public.profiles(id) on delete set null,
  created_at timestamptz not null default now()
);
create index if not exists ann_school_idx on public.announcements (school_id, created_at desc);
alter table public.announcements enable row level security;
drop policy if exists ann_read on public.announcements;
create policy ann_read on public.announcements for select to authenticated
  using (public.is_platform_admin()
         or (school_id = public.my_school() and (class_id is null or class_id = public.my_class() or public.is_staff())));
drop policy if exists ann_write on public.announcements;
create policy ann_write on public.announcements for all to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin()
         or (class_id is not null and public.teaches_class(class_id)))
  with check (public.is_platform_admin()
         or (public.is_school_admin_of(school_id) and (class_id is null or public.class_school(class_id) = school_id))
         or (class_id is not null and public.teaches_class(class_id) and public.class_school(class_id) = school_id));

-- ---------- private messages (a student and a staff member of the same school) ----------
create table if not exists public.messages (
  id           bigint generated always as identity primary key,
  school_id    uuid not null references public.schools(id) on delete cascade,
  sender_id    uuid not null references public.profiles(id) on delete cascade,
  recipient_id uuid not null references public.profiles(id) on delete cascade,
  body         text not null check (length(body) between 1 and 2000),
  created_at   timestamptz not null default now(),
  read_at      timestamptz
);
create index if not exists msg_recipient_idx on public.messages (recipient_id, created_at desc);
create index if not exists msg_sender_idx on public.messages (sender_id, created_at desc);
alter table public.messages enable row level security;
create or replace function public.can_message(rid uuid) returns boolean
language sql stable security definer set search_path = public as
$$ select exists (
     select 1 from public.profiles r, public.profiles s
     where r.id = rid and s.id = auth.uid() and r.school_id is not null and r.school_id = s.school_id
       and (r.role <> 'student' or s.role <> 'student')) $$;
drop policy if exists msg_read on public.messages;
create policy msg_read on public.messages for select to authenticated
  using (sender_id = auth.uid() or recipient_id = auth.uid());
drop policy if exists msg_send on public.messages;
create policy msg_send on public.messages for insert to authenticated
  with check (sender_id = auth.uid() and school_id = public.my_school() and public.can_message(recipient_id));
drop policy if exists msg_mark_read on public.messages;
create policy msg_mark_read on public.messages for update to authenticated
  using (recipient_id = auth.uid()) with check (recipient_id = auth.uid());
revoke update, delete on public.messages from authenticated, anon;
grant update (read_at) on public.messages to authenticated;

-- ---------- AI help: caps decided and counted on the server ----------
alter table public.schools add column if not exists ai_mode   text not null default 'full'  check (ai_mode in ('full','limited','off'));
alter table public.schools add column if not exists ai_cap    integer not null default 15   check (ai_cap >= 0);
alter table public.schools add column if not exists ai_period text not null default 'daily' check (ai_period in ('daily','weekly'));

create table if not exists public.platform_config (
  id             text primary key default 'global' check (id = 'global'),
  ai_default_cap integer not null default 15 check (ai_default_cap >= 0),
  trial_days     integer not null default 7  check (trial_days between 0 and 60),
  maintenance    boolean not null default false,
  banner         text check (length(banner) <= 300),
  updated_at     timestamptz not null default now()
);
insert into public.platform_config (id) values ('global') on conflict do nothing;
alter table public.platform_config enable row level security;
drop policy if exists cfg_read on public.platform_config;
create policy cfg_read on public.platform_config for select using (true);
drop policy if exists cfg_write on public.platform_config;
create policy cfg_write on public.platform_config for update to authenticated
  using (public.is_platform_admin()) with check (public.is_platform_admin());
revoke insert, delete on public.platform_config from authenticated, anon;

create table if not exists public.ai_usage (
  user_id uuid not null references public.profiles(id) on delete cascade,
  day     date not null default current_date,
  count   integer not null default 0 check (count >= 0),
  primary key (user_id, day)
);
alter table public.ai_usage enable row level security;
drop policy if exists ai_usage_self on public.ai_usage;
create policy ai_usage_self on public.ai_usage for select to authenticated using (user_id = auth.uid());
drop policy if exists ai_usage_staff on public.ai_usage;
create policy ai_usage_staff on public.ai_usage for select to authenticated
  using (public.is_staff() and exists (select 1 from public.profiles p where p.id = user_id and p.school_id = public.my_school()));
revoke insert, update, delete on public.ai_usage from authenticated, anon;

-- Atomically checks the cap and, when allowed, counts one use. Called only by the ai-tutor edge function.
create or replace function public.consume_ai(p_user uuid)
returns table (allowed boolean, used integer, cap integer, mode text)
language plpgsql security definer set search_path = public as $$
declare s record; d_cap integer; win date; u integer;
begin
  select sc.ai_mode, sc.ai_cap, sc.ai_period into s
    from public.profiles p left join public.schools sc on sc.id = p.school_id where p.id = p_user;
  select ai_default_cap into d_cap from public.platform_config where id = 'global';
  if not found then return query select false, 0, 0, 'off'::text; return; end if;
  mode := coalesce(s.ai_mode, 'limited'); cap := coalesce(s.ai_cap, d_cap);
  win := case when coalesce(s.ai_period, 'daily') = 'weekly' then current_date - 6 else current_date end;
  if mode = 'off' then return query select false, 0, 0, mode; return; end if;
  insert into public.ai_usage (user_id, day, count) values (p_user, current_date, 0) on conflict do nothing;
  perform 1 from public.ai_usage where user_id = p_user and day = current_date for update;
  select coalesce(sum(a.count), 0) into u from public.ai_usage a where a.user_id = p_user and a.day >= win;
  if mode = 'full' or u < cap then
    update public.ai_usage a set count = a.count + 1 where a.user_id = p_user and a.day = current_date;
    return query select true, u + 1, case when mode = 'full' then null else cap end, mode;
  else
    return query select false, u, cap, mode;
  end if;
end $$;
revoke all on function public.consume_ai(uuid) from public, anon, authenticated;
grant execute on function public.consume_ai(uuid) to service_role;

-- what the app shows: "7 of 15 used"
create or replace function public.my_ai_usage() returns table (used integer, cap integer, mode text)
language sql stable security definer set search_path = public as $$
  select coalesce((select sum(a.count)::int from public.ai_usage a where a.user_id = auth.uid()
                   and a.day >= case when coalesce(sc.ai_period,'daily') = 'weekly' then current_date - 6 else current_date end), 0),
         case when coalesce(sc.ai_mode,'limited') = 'full' then null else coalesce(sc.ai_cap, (select ai_default_cap from public.platform_config)) end,
         coalesce(sc.ai_mode, 'limited')
  from public.profiles p left join public.schools sc on sc.id = p.school_id where p.id = auth.uid() $$;

-- ---------- plans, entitlements, payments ----------
create table if not exists public.plans (
  code         text primary key,
  name         text not null,
  country_code text references public.countries(code),   -- null = any country
  currency_code text not null,
  amount_minor integer not null check (amount_minor >= 0),  -- smallest unit: kobo, pesewas, cents
  period       text not null check (period in ('month','term','year')),
  audience     text not null default 'student' check (audience in ('student','school')),
  active       boolean not null default true
);
alter table public.plans enable row level security;
drop policy if exists plans_read on public.plans;
create policy plans_read on public.plans for select using (active);
drop policy if exists plans_admin on public.plans;
create policy plans_admin on public.plans for all to authenticated
  using (public.is_platform_admin()) with check (public.is_platform_admin());

create table if not exists public.entitlements (
  id                 uuid primary key default gen_random_uuid(),
  user_id            uuid references public.profiles(id) on delete cascade,
  school_id          uuid references public.schools(id) on delete cascade,
  plan_code          text references public.plans(code),
  status             text not null check (status in ('trialing','active','past_due','canceled','expired')),
  trial_ends_at      timestamptz,
  current_period_end timestamptz,
  provider           text,
  provider_ref       text unique,
  created_at         timestamptz not null default now(),
  check (user_id is not null or school_id is not null)
);
create index if not exists ent_user_idx on public.entitlements (user_id);
create index if not exists ent_school_idx on public.entitlements (school_id);
alter table public.entitlements enable row level security;
drop policy if exists ent_self on public.entitlements;
create policy ent_self on public.entitlements for select to authenticated
  using (user_id = auth.uid() or school_id = public.my_school() or public.is_platform_admin());
revoke insert, update, delete on public.entitlements from authenticated, anon;

create or replace function public.has_access() returns boolean
language sql stable security definer set search_path = public as $$
  select exists (
    select 1 from public.entitlements e
    where (e.user_id = auth.uid() or e.school_id = public.my_school())
      and ((e.status = 'active'   and coalesce(e.current_period_end, 'infinity') > now())
        or (e.status = 'trialing' and coalesce(e.trial_ends_at, '-infinity') > now()))) $$;

create table if not exists public.payments (
  id           uuid primary key default gen_random_uuid(),
  user_id      uuid references public.profiles(id) on delete set null,
  school_id    uuid references public.schools(id) on delete set null,
  plan_code    text references public.plans(code),
  provider     text not null,
  provider_ref text not null,
  amount_minor integer not null,
  currency_code text not null,
  status       text not null,
  raw          jsonb,
  created_at   timestamptz not null default now(),
  unique (provider, provider_ref)
);
alter table public.payments enable row level security;
revoke all on public.payments from anon, authenticated;

-- every new student account starts a trial (length from platform_config); created from the signup edge functions
create or replace function public.start_trial(p_user uuid) returns void
language plpgsql security definer set search_path = public as $$
declare n integer;
begin
  select trial_days into n from public.platform_config where id = 'global';
  if coalesce(n, 0) = 0 then return; end if;
  if exists (select 1 from public.entitlements where user_id = p_user) then return; end if;
  insert into public.entitlements (user_id, status, trial_ends_at, provider) values (p_user, 'trialing', now() + make_interval(days => n), 'trial');
end $$;
revoke all on function public.start_trial(uuid) from public, anon, authenticated;
grant execute on function public.start_trial(uuid) to service_role;

-- ---------- promo codes (atomic: the count and the check happen in one transaction) ----------
create table if not exists public.promo_codes (
  code       citext primary key check (code ~ '^[A-Za-z0-9_-]{3,32}$'),
  kind       text not null check (kind in ('trial_extension','free_days')),
  value      integer not null check (value between 1 and 365),
  max_uses   integer check (max_uses > 0),
  used_count integer not null default 0,
  expires_at timestamptz,
  active     boolean not null default true
);
create table if not exists public.promo_redemptions (
  code        citext not null references public.promo_codes(code) on delete cascade,
  user_id     uuid not null references public.profiles(id) on delete cascade,
  redeemed_at timestamptz not null default now(),
  primary key (code, user_id)
);
alter table public.promo_codes enable row level security;
alter table public.promo_redemptions enable row level security;
drop policy if exists promo_admin on public.promo_codes;
create policy promo_admin on public.promo_codes for all to authenticated
  using (public.is_platform_admin()) with check (public.is_platform_admin());
drop policy if exists redeem_self on public.promo_redemptions;
create policy redeem_self on public.promo_redemptions for select to authenticated
  using (user_id = auth.uid() or public.is_platform_admin());
revoke insert, update, delete on public.promo_redemptions from authenticated, anon;

create or replace function public.redeem_promo(p_code text) returns jsonb
language plpgsql security definer set search_path = public as $$
declare pc public.promo_codes; uid uuid := auth.uid(); ent uuid; base timestamptz;
begin
  if uid is null then raise exception 'sign in first'; end if;
  select * into pc from public.promo_codes where code = p_code::citext for update;
  if not found or not pc.active or (pc.expires_at is not null and pc.expires_at < now())
     or (pc.max_uses is not null and pc.used_count >= pc.max_uses) then
    return jsonb_build_object('ok', false, 'error', 'This code is not valid.');
  end if;
  if exists (select 1 from public.promo_redemptions where code = pc.code and user_id = uid) then
    return jsonb_build_object('ok', false, 'error', 'You already used this code.');
  end if;
  select id, greatest(coalesce(trial_ends_at, now()), coalesce(current_period_end, now()), now()) into ent, base
    from public.entitlements where user_id = uid order by created_at desc limit 1;
  if ent is null then
    insert into public.entitlements (user_id, status, trial_ends_at, provider)
      values (uid, 'trialing', now() + make_interval(days => pc.value), 'promo');
  elsif pc.kind = 'trial_extension' then
    update public.entitlements set status = case when status = 'active' then status else 'trialing' end,
           trial_ends_at = base + make_interval(days => pc.value) where id = ent;
  else
    update public.entitlements set status = 'active', current_period_end = base + make_interval(days => pc.value) where id = ent;
  end if;
  insert into public.promo_redemptions (code, user_id) values (pc.code, uid);
  update public.promo_codes set used_count = used_count + 1 where code = pc.code;
  return jsonb_build_object('ok', true, 'days', pc.value);
end $$;
revoke all on function public.redeem_promo(text) from public, anon;
grant execute on function public.redeem_promo(text) to authenticated;

-- ---------- parent / guardian contacts (digest emails only after consent is recorded) ----------
create table if not exists public.guardians (
  id            uuid primary key default gen_random_uuid(),
  student_id    uuid not null references public.profiles(id) on delete cascade,
  name          text check (length(name) <= 80),
  email         citext not null check (email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$'),
  digest_opt_in boolean not null default false,
  consent_at    timestamptz,           -- when the guardian agreed; the digest job skips rows where this is null
  created_by    uuid references public.profiles(id) on delete set null,
  created_at    timestamptz not null default now(),
  unique (student_id, email)
);
alter table public.guardians enable row level security;
drop policy if exists guardians_staff on public.guardians;
create policy guardians_staff on public.guardians for all to authenticated
  using (public.is_platform_admin() or (public.is_staff() and exists (
          select 1 from public.profiles p where p.id = student_id and p.school_id = public.my_school())))
  with check (public.is_platform_admin() or (public.is_staff() and exists (
          select 1 from public.profiles p where p.id = student_id and p.school_id = public.my_school())));

-- ---------- live class quiz ----------
create table if not exists public.live_sessions (
  id            uuid primary key default gen_random_uuid(),
  class_id      uuid not null references public.classes(id) on delete cascade,
  host_id       uuid not null references public.profiles(id) on delete cascade,
  code          text not null unique check (code ~ '^[A-Z0-9]{5,8}$'),
  state         text not null default 'lobby' check (state in ('lobby','running','ended')),
  questions     jsonb not null default '[]',      -- [{q, o:[..]}] with no answers in it
  current_index integer not null default 0,
  created_at    timestamptz not null default now()
);
create table if not exists public.live_keys (       -- answers live apart from the questions so students can never read them
  session_id uuid primary key references public.live_sessions(id) on delete cascade,
  answers    jsonb not null                          -- [0,2,1,...]
);
create table if not exists public.live_answers (
  session_id  uuid not null references public.live_sessions(id) on delete cascade,
  student_id  uuid not null references public.profiles(id) on delete cascade,
  q_index     integer not null check (q_index >= 0),
  choice      smallint not null check (choice between 0 and 3),
  correct     boolean,
  answered_at timestamptz not null default now(),
  primary key (session_id, student_id, q_index)
);
alter table public.live_sessions enable row level security;
alter table public.live_keys enable row level security;
alter table public.live_answers enable row level security;
drop policy if exists live_host on public.live_sessions;
create policy live_host on public.live_sessions for all to authenticated
  using (public.teaches_class(class_id)) with check (public.teaches_class(class_id) and host_id = auth.uid());
drop policy if exists live_students on public.live_sessions;
create policy live_students on public.live_sessions for select to authenticated using (class_id = public.my_class());
drop policy if exists keys_host on public.live_keys;
create policy keys_host on public.live_keys for all to authenticated
  using (exists (select 1 from public.live_sessions s where s.id = session_id and public.teaches_class(s.class_id)))
  with check (exists (select 1 from public.live_sessions s where s.id = session_id and public.teaches_class(s.class_id)));
drop policy if exists la_self_insert on public.live_answers;
create policy la_self_insert on public.live_answers for insert to authenticated
  with check (student_id = auth.uid() and exists (
    select 1 from public.live_sessions s where s.id = session_id and s.state = 'running' and s.class_id = public.my_class()));
drop policy if exists la_read on public.live_answers;
create policy la_read on public.live_answers for select to authenticated
  using (student_id = auth.uid() or exists (select 1 from public.live_sessions s where s.id = session_id and public.teaches_class(s.class_id)));
revoke update, delete on public.live_answers from authenticated, anon;

create or replace function public.score_live_answer() returns trigger
language plpgsql security definer set search_path = public as $$
declare k jsonb;
begin
  select answers into k from public.live_keys where session_id = new.session_id;
  new.correct := (k is not null and (k ->> new.q_index)::int = new.choice);
  return new;
end $$;
drop trigger if exists live_score on public.live_answers;
create trigger live_score before insert on public.live_answers for each row execute function public.score_live_answer();

-- ---------- push subscriptions, content reports, client errors ----------
create table if not exists public.push_subscriptions (
  endpoint   text primary key,
  user_id    uuid not null references public.profiles(id) on delete cascade,
  p256dh     text not null,
  auth       text not null,
  created_at timestamptz not null default now()
);
alter table public.push_subscriptions enable row level security;
drop policy if exists push_self on public.push_subscriptions;
create policy push_self on public.push_subscriptions for all to authenticated
  using (user_id = auth.uid()) with check (user_id = auth.uid());

create table if not exists public.content_reports (
  id           bigint generated always as identity primary key,
  user_id      uuid references public.profiles(id) on delete set null,
  country_code text references public.countries(code),
  exam         text, subject text, topic text,
  item         text check (item in ('note','question','flashcard','other')),
  note         text not null check (length(note) between 3 and 1500),
  status       text not null default 'open' check (status in ('open','fixed','rejected')),
  created_at   timestamptz not null default now()
);
alter table public.content_reports enable row level security;
drop policy if exists rep_insert on public.content_reports;
create policy rep_insert on public.content_reports for insert to authenticated with check (user_id = auth.uid());
drop policy if exists rep_read on public.content_reports;
create policy rep_read on public.content_reports for select to authenticated using (user_id = auth.uid() or public.is_platform_admin());
drop policy if exists rep_admin on public.content_reports;
create policy rep_admin on public.content_reports for update to authenticated using (public.is_platform_admin()) with check (public.is_platform_admin());

create table if not exists public.app_errors (
  id         bigint generated always as identity primary key,
  user_id    uuid,
  page       text check (length(page) <= 200),
  message    text check (length(message) <= 600),
  created_at timestamptz not null default now()
);
alter table public.app_errors enable row level security;
drop policy if exists err_insert on public.app_errors;
create policy err_insert on public.app_errors for insert to authenticated with check (user_id is null or user_id = auth.uid());
drop policy if exists err_read on public.app_errors;
create policy err_read on public.app_errors for select to authenticated using (public.is_platform_admin());

-- ---------- data that was out of date in the seed ----------
update public.countries set live = true;

-- internal helpers must not be callable by the public API unless meant to be
revoke all on function public.score_live_answer(), public.guard_submission(), public.check_mark() from public, anon, authenticated;
