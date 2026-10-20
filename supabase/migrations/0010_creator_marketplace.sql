-- 0010: creator marketplace. Idempotent. Run after 0009.
-- Teachers, lecturers and tutors apply to become creators, publish courses of video lessons, and learners subscribe to a creator.
-- Ace receives the payment, keeps its agreed fee, and credits the rest to the creator's ledger. Creators request payouts from that ledger.
-- Payment providers are NOT connected here: record_creator_payment() is the one function a payment webhook (service role) will call.
-- Money is stored in minor units (kobo, pesewas, cents) as integers. Nothing here ever stores card or bank account numbers.

-- =====================================================================================
-- 1. Settings
-- =====================================================================================
create table if not exists public.marketplace_settings (
  id               smallint primary key default 1 check (id = 1),
  default_fee_pct  numeric(5,2) not null default 30 check (default_fee_pct between 0 and 100),  -- Ace's share. PLACEHOLDER: set the real agreed figure.
  fee_basis        text not null default 'net' check (fee_basis in ('gross','net')),            -- net = Ace's fee is taken after the payment-provider fee
  payout_hold_days smallint not null default 14 check (payout_hold_days between 0 and 90),       -- earnings become withdrawable after this many days (refund window)
  min_payout_minor integer not null default 1000 check (min_payout_minor >= 0),
  updated_at       timestamptz not null default now()
);
insert into public.marketplace_settings(id) values (1) on conflict (id) do nothing;
alter table public.marketplace_settings enable row level security;
revoke all on public.marketplace_settings from anon, authenticated;
grant select on public.marketplace_settings to authenticated;
drop policy if exists mset_read on public.marketplace_settings;
create policy mset_read on public.marketplace_settings for select to authenticated using (true);

-- =====================================================================================
-- 2. Creators
-- =====================================================================================
create table if not exists public.creator_profiles (
  user_id        uuid primary key references public.profiles(id) on delete cascade,
  handle         text not null unique check (handle ~ '^[a-z0-9-]{3,30}$'),
  display_name   text not null check (char_length(display_name) between 2 and 60),
  headline       text check (char_length(headline) <= 120),
  bio            text check (char_length(bio) <= 1500),
  country_code   text references public.countries(code),
  status         text not null default 'pending' check (status in ('pending','approved','rejected','suspended')),
  fee_pct        numeric(5,2) check (fee_pct between 0 and 100),   -- null = use the marketplace default
  adult_confirmed boolean not null default false,
  terms_version  text,
  terms_accepted_at timestamptz,
  review_note    text,
  created_at     timestamptz not null default now(),
  updated_at     timestamptz not null default now()
);

-- Payout details are kept apart so they are visible only to the owner and platform admins. Free text, no account numbers required:
-- ask the creator for a payout method and a reference the finance team can use (for example a mobile-money number or a bank name and account holder).
create table if not exists public.creator_payout_details (
  user_id    uuid primary key references public.creator_profiles(user_id) on delete cascade,
  method     text not null check (method in ('bank','mobile_money','other')),
  details    text not null check (char_length(details) between 4 and 400),
  updated_at timestamptz not null default now()
);

create table if not exists public.creator_plans (
  id            uuid primary key default gen_random_uuid(),
  creator_id    uuid not null references public.creator_profiles(user_id) on delete cascade,
  name          text not null check (char_length(name) between 2 and 60),
  currency_code text not null,
  amount_minor  integer not null check (amount_minor > 0),
  period        text not null check (period in ('month','year')),
  active        boolean not null default true,
  created_at    timestamptz not null default now()
);

create table if not exists public.creator_courses (
  id          uuid primary key default gen_random_uuid(),
  creator_id  uuid not null references public.creator_profiles(user_id) on delete cascade,
  slug        text not null unique check (slug ~ '^[a-z0-9-]{3,60}$'),
  title       text not null check (char_length(title) between 3 and 120),
  summary     text not null check (char_length(summary) between 10 and 600),
  field       text not null check (field in ('it','biz','fin','health','edu','hum','soc','sci','eng','law','creative','life')),
  level       text not null default 'all' check (level in ('all','secondary','university','professional')),
  language    text not null default 'en' check (language in ('en','es','fr','sw','ar','pt','other')),
  status      text not null default 'draft' check (status in ('draft','submitted','approved','rejected','unpublished')),
  review_note text,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);
create index if not exists creator_courses_creator on public.creator_courses(creator_id);
create index if not exists creator_courses_status on public.creator_courses(status);

-- Public part of a lesson: what a visitor may see in the syllabus.
create table if not exists public.creator_lessons (
  id           uuid primary key default gen_random_uuid(),
  course_id    uuid not null references public.creator_courses(id) on delete cascade,
  position     smallint not null check (position >= 0),
  title        text not null check (char_length(title) between 2 and 120),
  duration_sec integer check (duration_sec between 0 and 21600),
  is_preview   boolean not null default false,        -- free for everyone
  created_at   timestamptz not null default now(),
  unique (course_id, position)
);
-- Protected part: notes and video reference. Only reachable through get_lesson_content(), which checks the subscription.
create table if not exists public.creator_lesson_content (
  lesson_id      uuid primary key references public.creator_lessons(id) on delete cascade,
  body           text check (char_length(body) <= 20000),
  video_provider text check (video_provider in ('bunny','cloudflare','vimeo','youtube','other')),
  video_ref      text check (char_length(video_ref) <= 300)
);

-- =====================================================================================
-- 3. Subscriptions, payments, ledger, payouts
-- =====================================================================================
create table if not exists public.creator_subscriptions (
  id                   uuid primary key default gen_random_uuid(),
  subscriber_id        uuid not null references public.profiles(id) on delete cascade,
  creator_id           uuid not null references public.creator_profiles(user_id) on delete cascade,
  plan_id              uuid not null references public.creator_plans(id),
  status               text not null default 'active' check (status in ('active','past_due','cancelled','expired')),
  current_period_end   timestamptz not null,
  cancel_at_period_end boolean not null default false,
  created_at           timestamptz not null default now(),
  updated_at           timestamptz not null default now()
);
create unique index if not exists creator_subs_one_live on public.creator_subscriptions(subscriber_id, creator_id) where status in ('active','past_due');

create table if not exists public.creator_payments (
  id                 uuid primary key default gen_random_uuid(),
  subscription_id    uuid references public.creator_subscriptions(id) on delete set null,
  creator_id         uuid not null references public.creator_profiles(user_id),
  subscriber_id      uuid references public.profiles(id) on delete set null,
  currency_code      text not null,
  gross_minor        bigint not null check (gross_minor > 0),
  provider_fee_minor bigint not null default 0 check (provider_fee_minor >= 0),
  platform_fee_minor bigint not null check (platform_fee_minor >= 0),
  creator_share_minor bigint not null check (creator_share_minor >= 0),
  fee_pct            numeric(5,2) not null,
  fee_basis          text not null,
  provider           text not null,
  provider_ref       text not null,
  status             text not null default 'succeeded' check (status in ('succeeded','refunded')),
  created_at         timestamptz not null default now(),
  unique (provider, provider_ref),
  check (platform_fee_minor + creator_share_minor + case when fee_basis = 'net' then provider_fee_minor else 0 end = gross_minor)
);

create table if not exists public.payout_requests (
  id            uuid primary key default gen_random_uuid(),
  creator_id    uuid not null references public.creator_profiles(user_id),
  currency_code text not null,
  amount_minor  bigint not null check (amount_minor > 0),
  status        text not null default 'requested' check (status in ('requested','paid','rejected')),
  requested_at  timestamptz not null default now(),
  decided_by    uuid references public.profiles(id),
  decided_at    timestamptz,
  provider_ref  text,
  note          text
);
create unique index if not exists payout_one_open on public.payout_requests(creator_id, currency_code) where status = 'requested';

-- The ledger is the single source of truth for what Ace owes each creator. Positive = owed to the creator, negative = paid or reserved.
create table if not exists public.creator_ledger (
  id            bigint generated always as identity primary key,
  creator_id    uuid not null references public.creator_profiles(user_id),
  kind          text not null check (kind in ('earning','refund','payout','payout_reversal','adjustment')),
  currency_code text not null,
  amount_minor  bigint not null check (amount_minor <> 0),
  payment_id    uuid references public.creator_payments(id),
  payout_id     uuid references public.payout_requests(id),
  available_at  timestamptz not null default now(),
  note          text,
  created_at    timestamptz not null default now()
);
create index if not exists creator_ledger_creator on public.creator_ledger(creator_id, currency_code);

create table if not exists public.creator_reports (
  id         bigint generated always as identity primary key,
  reporter   uuid references public.profiles(id) on delete set null,
  course_id  uuid references public.creator_courses(id) on delete cascade,
  reason     text not null check (char_length(reason) between 5 and 600),
  status     text not null default 'open' check (status in ('open','actioned','dismissed')),
  created_at timestamptz not null default now()
);

-- =====================================================================================
-- 4. Row level security
-- =====================================================================================
alter table public.creator_profiles       enable row level security;
alter table public.creator_payout_details enable row level security;
alter table public.creator_plans          enable row level security;
alter table public.creator_courses        enable row level security;
alter table public.creator_lessons        enable row level security;
alter table public.creator_lesson_content enable row level security;
alter table public.creator_subscriptions  enable row level security;
alter table public.creator_payments       enable row level security;
alter table public.payout_requests        enable row level security;
alter table public.creator_ledger         enable row level security;
alter table public.creator_reports        enable row level security;

revoke all on public.creator_profiles, public.creator_payout_details, public.creator_plans, public.creator_courses, public.creator_lessons,
  public.creator_lesson_content, public.creator_subscriptions, public.creator_payments, public.payout_requests, public.creator_ledger,
  public.creator_reports from anon, authenticated;

create or replace function public.is_approved_creator(u uuid default auth.uid()) returns boolean
language sql stable security definer set search_path = public as
$$ select exists (select 1 from public.creator_profiles where user_id = u and status = 'approved') $$;

-- Is the signed-in user allowed to see paid content of this creator?
create or replace function public.has_creator_access(p_creator uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select auth.uid() is not null and (
    p_creator = auth.uid()
    or coalesce(public.is_platform_admin(), false)
    or exists (select 1 from public.creator_subscriptions s
               where s.subscriber_id = auth.uid() and s.creator_id = p_creator
                 and s.status in ('active','past_due') and s.current_period_end > now())) $$;

-- creator profiles: public can see approved creators; owner sees own; admin sees all. Owner edits own text fields only.
grant select, insert, update on public.creator_profiles to authenticated;
grant select on public.creator_profiles to anon;
drop policy if exists cp_read on public.creator_profiles;
create policy cp_read on public.creator_profiles for select using (status = 'approved' or user_id = auth.uid() or public.is_platform_admin());
drop policy if exists cp_update_own on public.creator_profiles;
create policy cp_update_own on public.creator_profiles for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
-- creators may not change their own status, fee or review note: a trigger enforces that for everyone except platform admins and service role
create or replace function public.creator_profiles_guard() returns trigger language plpgsql as $$
begin
  if tg_op = 'UPDATE' and coalesce(auth.uid()::text, '') <> '' and not coalesce(public.is_platform_admin(), false) then
    if new.status is distinct from old.status or new.fee_pct is distinct from old.fee_pct or new.review_note is distinct from old.review_note
       or new.user_id is distinct from old.user_id or new.handle is distinct from old.handle then
      raise exception 'These fields can only be changed by Ace staff.';
    end if;
  end if;
  new.updated_at := now();
  return new;
end $$;
drop trigger if exists creator_profiles_guard on public.creator_profiles;
create trigger creator_profiles_guard before update on public.creator_profiles for each row execute function public.creator_profiles_guard();
-- inserts are only through apply_creator()
revoke insert on public.creator_profiles from authenticated;

grant select, insert, update, delete on public.creator_payout_details to authenticated;
drop policy if exists cpd_own on public.creator_payout_details;
create policy cpd_own on public.creator_payout_details for all to authenticated
  using (user_id = auth.uid() or public.is_platform_admin()) with check (user_id = auth.uid());

grant select on public.creator_plans to anon;
grant select, insert, update, delete on public.creator_plans to authenticated;
drop policy if exists plans_read on public.creator_plans;
create policy plans_read on public.creator_plans for select using (active and exists (select 1 from public.creator_profiles c where c.user_id = creator_id and c.status = 'approved') or creator_id = auth.uid() or public.is_platform_admin());
drop policy if exists plans_write on public.creator_plans;
create policy plans_write on public.creator_plans for all to authenticated
  using (creator_id = auth.uid() and public.is_approved_creator()) with check (creator_id = auth.uid() and public.is_approved_creator());

grant select on public.creator_courses to anon;
grant select, insert, update, delete on public.creator_courses to authenticated;
drop policy if exists cc_read on public.creator_courses;
create policy cc_read on public.creator_courses for select using (
  (status = 'approved' and exists (select 1 from public.creator_profiles c where c.user_id = creator_id and c.status = 'approved'))
  or creator_id = auth.uid() or public.is_platform_admin());
drop policy if exists cc_insert on public.creator_courses;
create policy cc_insert on public.creator_courses for insert to authenticated
  with check (creator_id = auth.uid() and public.is_approved_creator() and status = 'draft');
drop policy if exists cc_update on public.creator_courses;
create policy cc_update on public.creator_courses for update to authenticated
  using (creator_id = auth.uid() and status in ('draft','rejected','unpublished'))
  with check (creator_id = auth.uid() and status in ('draft','rejected','unpublished'));
drop policy if exists cc_delete on public.creator_courses;
create policy cc_delete on public.creator_courses for delete to authenticated using (creator_id = auth.uid() and status in ('draft','rejected'));

grant select on public.creator_lessons to anon;
grant select, insert, update, delete on public.creator_lessons to authenticated;
drop policy if exists cl_read on public.creator_lessons;
create policy cl_read on public.creator_lessons for select using (exists (select 1 from public.creator_courses c where c.id = course_id and
  ((c.status = 'approved' and exists (select 1 from public.creator_profiles p where p.user_id = c.creator_id and p.status = 'approved')) or c.creator_id = auth.uid() or public.is_platform_admin())));
drop policy if exists cl_write on public.creator_lessons;
create policy cl_write on public.creator_lessons for all to authenticated
  using (exists (select 1 from public.creator_courses c where c.id = course_id and c.creator_id = auth.uid() and c.status in ('draft','rejected','unpublished')))
  with check (exists (select 1 from public.creator_courses c where c.id = course_id and c.creator_id = auth.uid() and c.status in ('draft','rejected','unpublished')));

-- protected lesson content: owner and admin only. Everyone else uses get_lesson_content().
grant select, insert, update, delete on public.creator_lesson_content to authenticated;
drop policy if exists clc_owner on public.creator_lesson_content;
create policy clc_owner on public.creator_lesson_content for all to authenticated
  using (exists (select 1 from public.creator_lessons l join public.creator_courses c on c.id = l.course_id where l.id = lesson_id and (c.creator_id = auth.uid() or public.is_platform_admin())))
  with check (exists (select 1 from public.creator_lessons l join public.creator_courses c on c.id = l.course_id where l.id = lesson_id and c.creator_id = auth.uid() and c.status in ('draft','rejected','unpublished')));

-- subscriptions: a subscriber sees their own. Creators never see subscriber identities, only counts through creator_stats().
grant select on public.creator_subscriptions to authenticated;
drop policy if exists cs_own on public.creator_subscriptions;
create policy cs_own on public.creator_subscriptions for select to authenticated using (subscriber_id = auth.uid() or public.is_platform_admin());

-- payments, ledger, payouts: creators read their own rows, nobody writes directly
grant select on public.creator_payments, public.creator_ledger, public.payout_requests to authenticated;
drop policy if exists cpay_read on public.creator_payments;
create policy cpay_read on public.creator_payments for select to authenticated using (creator_id = auth.uid() or public.is_platform_admin());
drop policy if exists cled_read on public.creator_ledger;
create policy cled_read on public.creator_ledger for select to authenticated using (creator_id = auth.uid() or public.is_platform_admin());
drop policy if exists pr_read on public.payout_requests;
create policy pr_read on public.payout_requests for select to authenticated using (creator_id = auth.uid() or public.is_platform_admin());

grant select on public.creator_reports to authenticated;
drop policy if exists rep_admin on public.creator_reports;
create policy rep_admin on public.creator_reports for select to authenticated using (public.is_platform_admin());

-- =====================================================================================
-- 5. Functions
-- =====================================================================================
create or replace function public.apply_creator(p_handle text, p_display_name text, p_headline text, p_bio text, p_country text, p_adult boolean, p_terms text)
returns void language plpgsql security definer set search_path = public as $$
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  if not coalesce(p_adult, false) then raise exception 'Creators must be 18 or older.'; end if;
  if coalesce(p_terms, '') = '' then raise exception 'Please accept the creator terms.'; end if;
  if exists (select 1 from public.creator_profiles where user_id = auth.uid()) then raise exception 'You have already applied.'; end if;
  insert into public.creator_profiles(user_id, handle, display_name, headline, bio, country_code, adult_confirmed, terms_version, terms_accepted_at)
  values (auth.uid(), lower(trim(p_handle)), trim(p_display_name), nullif(trim(coalesce(p_headline, '')), ''), nullif(trim(coalesce(p_bio, '')), ''), p_country, true, p_terms, now());
  insert into public.audit_log(actor, action, target) values (auth.uid(), 'creator.apply', auth.uid()::text);
end $$;
revoke all on function public.apply_creator(text,text,text,text,text,boolean,text) from public, anon;
grant execute on function public.apply_creator(text,text,text,text,text,boolean,text) to authenticated;

create or replace function public.review_creator(p_user uuid, p_decision text, p_fee_pct numeric default null, p_note text default null)
returns void language plpgsql security definer set search_path = public as $$
begin
  if not coalesce(public.is_platform_admin(), false) then raise exception 'not allowed'; end if;
  if p_decision not in ('approved','rejected','suspended') then raise exception 'bad decision'; end if;
  update public.creator_profiles set status = p_decision, fee_pct = coalesce(p_fee_pct, fee_pct), review_note = p_note, updated_at = now() where user_id = p_user;
  if not found then raise exception 'unknown creator'; end if;
  insert into public.audit_log(actor, action, target, detail) values (auth.uid(), 'creator.' || p_decision, p_user::text, jsonb_build_object('fee_pct', p_fee_pct, 'note', p_note));
end $$;
revoke all on function public.review_creator(uuid,text,numeric,text) from public, anon;
grant execute on function public.review_creator(uuid,text,numeric,text) to authenticated;

create or replace function public.submit_creator_course(p_course uuid) returns void
language plpgsql security definer set search_path = public as $$
declare n int;
begin
  if not public.is_approved_creator() then raise exception 'Your creator account is not approved.'; end if;
  select count(*) into n from public.creator_lessons where course_id = p_course;
  if n < 3 then raise exception 'Add at least 3 lessons before you submit.'; end if;
  if exists (select 1 from public.creator_lessons l left join public.creator_lesson_content c on c.lesson_id = l.id
             where l.course_id = p_course and coalesce(nullif(trim(c.video_ref), ''), nullif(trim(c.body), '')) is null) then
    raise exception 'Every lesson needs a video or written notes.'; end if;
  update public.creator_courses set status = 'submitted', review_note = null, updated_at = now()
    where id = p_course and creator_id = auth.uid() and status in ('draft','rejected','unpublished');
  if not found then raise exception 'This course cannot be submitted.'; end if;
end $$;
revoke all on function public.submit_creator_course(uuid) from public, anon;
grant execute on function public.submit_creator_course(uuid) to authenticated;

create or replace function public.review_creator_course(p_course uuid, p_decision text, p_note text default null) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not coalesce(public.is_platform_admin(), false) then raise exception 'not allowed'; end if;
  if p_decision not in ('approved','rejected','unpublished') then raise exception 'bad decision'; end if;
  update public.creator_courses set status = p_decision, review_note = p_note, updated_at = now() where id = p_course;
  if not found then raise exception 'unknown course'; end if;
  insert into public.audit_log(actor, action, target, detail) values (auth.uid(), 'creator_course.' || p_decision, p_course::text, jsonb_build_object('note', p_note));
end $$;
revoke all on function public.review_creator_course(uuid,text,text) from public, anon;
grant execute on function public.review_creator_course(uuid,text,text) to authenticated;

-- The only way to read a lesson's notes and video reference.
create or replace function public.get_lesson_content(p_lesson uuid)
returns table (title text, body text, video_provider text, video_ref text)
language plpgsql stable security definer set search_path = public as $$
declare l record;
begin
  select ls.id, ls.title, ls.is_preview, c.creator_id, c.status as cstatus, p.status as pstatus into l
    from public.creator_lessons ls join public.creator_courses c on c.id = ls.course_id join public.creator_profiles p on p.user_id = c.creator_id where ls.id = p_lesson;
  if not found then raise exception 'unknown lesson'; end if;
  if not (l.creator_id = auth.uid() or coalesce(public.is_platform_admin(), false)) then
    if l.cstatus <> 'approved' or l.pstatus <> 'approved' then raise exception 'unknown lesson'; end if;
    if not l.is_preview and not public.has_creator_access(l.creator_id) then raise exception 'Subscribe to this creator to watch this lesson.'; end if;
  end if;
  return query select l.title, c.body, c.video_provider, c.video_ref from public.creator_lesson_content c where c.lesson_id = p_lesson;
end $$;
revoke all on function public.get_lesson_content(uuid) from public;
grant execute on function public.get_lesson_content(uuid) to anon, authenticated;

-- Called by the payment webhook (service role only). Idempotent on (provider, provider_ref).
create or replace function public.record_creator_payment(p_subscriber uuid, p_plan uuid, p_gross bigint, p_provider_fee bigint, p_provider text, p_ref text)
returns uuid language plpgsql security definer set search_path = public as $$
declare pl record; cr record; st record; sub uuid; pid uuid; pct numeric; base bigint; pfee bigint; cshare bigint; step interval; hold smallint;
begin
  select id into pid from public.creator_payments where provider = p_provider and provider_ref = p_ref;
  if pid is not null then return pid; end if;
  select * into pl from public.creator_plans where id = p_plan and active; if not found then raise exception 'unknown plan'; end if;
  select * into cr from public.creator_profiles where user_id = pl.creator_id and status = 'approved'; if not found then raise exception 'creator not approved'; end if;
  select * into st from public.marketplace_settings where id = 1;
  if p_gross <= 0 or p_provider_fee < 0 or p_provider_fee >= p_gross then raise exception 'bad amounts'; end if;
  pct := coalesce(cr.fee_pct, st.default_fee_pct);
  base := case st.fee_basis when 'net' then p_gross - p_provider_fee else p_gross end;
  pfee := round(base * pct / 100.0)::bigint;
  cshare := base - pfee;
  step := case pl.period when 'year' then interval '1 year' else interval '1 month' end;
  select id into sub from public.creator_subscriptions where subscriber_id = p_subscriber and creator_id = pl.creator_id and status in ('active','past_due');
  if sub is null then
    insert into public.creator_subscriptions(subscriber_id, creator_id, plan_id, current_period_end) values (p_subscriber, pl.creator_id, p_plan, now() + step) returning id into sub;
  else
    update public.creator_subscriptions set status = 'active', plan_id = p_plan, current_period_end = greatest(current_period_end, now()) + step, updated_at = now() where id = sub;
  end if;
  insert into public.creator_payments(subscription_id, creator_id, subscriber_id, currency_code, gross_minor, provider_fee_minor, platform_fee_minor, creator_share_minor, fee_pct, fee_basis, provider, provider_ref)
  values (sub, pl.creator_id, p_subscriber, pl.currency_code, p_gross, p_provider_fee, pfee, cshare, pct, st.fee_basis, p_provider, p_ref) returning id into pid;
  insert into public.creator_ledger(creator_id, kind, currency_code, amount_minor, payment_id, available_at)
  values (pl.creator_id, 'earning', pl.currency_code, cshare, pid, now() + make_interval(days => st.payout_hold_days)) ;
  return pid;
end $$;
revoke all on function public.record_creator_payment(uuid,uuid,bigint,bigint,text,text) from public, anon, authenticated;
grant execute on function public.record_creator_payment(uuid,uuid,bigint,bigint,text,text) to service_role;

create or replace function public.refund_creator_payment(p_payment uuid, p_note text default null) returns void
language plpgsql security definer set search_path = public as $$
declare p record;
begin
  select * into p from public.creator_payments where id = p_payment for update; if not found then raise exception 'unknown payment'; end if;
  if p.status = 'refunded' then return; end if;
  update public.creator_payments set status = 'refunded' where id = p_payment;
  insert into public.creator_ledger(creator_id, kind, currency_code, amount_minor, payment_id, note) values (p.creator_id, 'refund', p.currency_code, -p.creator_share_minor, p_payment, p_note);
  update public.creator_subscriptions set status = 'cancelled', current_period_end = now(), updated_at = now() where id = p.subscription_id;
end $$;
revoke all on function public.refund_creator_payment(uuid,text) from public, anon, authenticated;
grant execute on function public.refund_creator_payment(uuid,text) to service_role;

create or replace function public.cancel_creator_subscription(p_sub uuid) returns void
language sql security definer set search_path = public as $$
  update public.creator_subscriptions set cancel_at_period_end = true, updated_at = now() where id = p_sub and subscriber_id = auth.uid() and status in ('active','past_due') $$;
revoke all on function public.cancel_creator_subscription(uuid) from public, anon;
grant execute on function public.cancel_creator_subscription(uuid) to authenticated;

create or replace function public.creator_balance()
returns table (currency_code text, available_minor bigint, pending_minor bigint, withdrawn_minor bigint)
language sql stable security definer set search_path = public as $$
  select l.currency_code,
         coalesce(sum(l.amount_minor) filter (where l.kind not in ('payout','payout_reversal') and l.available_at <= now()), 0)
           + coalesce(sum(l.amount_minor) filter (where l.kind in ('payout','payout_reversal')), 0),
         coalesce(sum(l.amount_minor) filter (where l.kind not in ('payout','payout_reversal') and l.available_at > now()), 0),
         -coalesce(sum(l.amount_minor) filter (where l.kind in ('payout','payout_reversal')), 0)
  from public.creator_ledger l where l.creator_id = auth.uid() group by l.currency_code $$;
revoke all on function public.creator_balance() from public, anon;
grant execute on function public.creator_balance() to authenticated;

create or replace function public.creator_stats()
returns table (active_subscribers bigint, courses bigint, lifetime_earned_minor bigint)
language sql stable security definer set search_path = public as $$
  select (select count(*) from public.creator_subscriptions where creator_id = auth.uid() and status in ('active','past_due') and current_period_end > now()),
         (select count(*) from public.creator_courses where creator_id = auth.uid() and status = 'approved'),
         coalesce((select sum(creator_share_minor) from public.creator_payments where creator_id = auth.uid() and status = 'succeeded'), 0) $$;
revoke all on function public.creator_stats() from public, anon;
grant execute on function public.creator_stats() to authenticated;

create or replace function public.request_payout(p_currency text, p_amount bigint) returns uuid
language plpgsql security definer set search_path = public as $$
declare avail bigint; mn int; pid uuid;
begin
  if not public.is_approved_creator() then raise exception 'Your creator account is not approved.'; end if;
  if not exists (select 1 from public.creator_payout_details where user_id = auth.uid()) then raise exception 'Add your payout details first.'; end if;
  select min_payout_minor into mn from public.marketplace_settings where id = 1;
  if p_amount < mn then raise exception 'The minimum payout is % (in the smallest currency unit).', mn; end if;
  perform 1 from public.creator_profiles where user_id = auth.uid() for update;   -- serialise requests per creator
  select coalesce(sum(amount_minor) filter (where kind not in ('payout','payout_reversal') and available_at <= now()), 0)
       + coalesce(sum(amount_minor) filter (where kind in ('payout','payout_reversal')), 0) into avail
    from public.creator_ledger where creator_id = auth.uid() and currency_code = p_currency;
  if p_amount > avail then raise exception 'You can withdraw up to % right now.', avail; end if;
  if exists (select 1 from public.payout_requests where creator_id = auth.uid() and currency_code = p_currency and status = 'requested') then raise exception 'You already have a payout waiting.'; end if;
  insert into public.payout_requests(creator_id, currency_code, amount_minor) values (auth.uid(), p_currency, p_amount) returning id into pid;
  insert into public.creator_ledger(creator_id, kind, currency_code, amount_minor, payout_id, note) values (auth.uid(), 'payout', p_currency, -p_amount, pid, 'reserved');
  return pid;
end $$;
revoke all on function public.request_payout(text,bigint) from public, anon;
grant execute on function public.request_payout(text,bigint) to authenticated;

create or replace function public.decide_payout(p_payout uuid, p_decision text, p_ref text default null, p_note text default null) returns void
language plpgsql security definer set search_path = public as $$
declare r record;
begin
  if not coalesce(public.is_platform_admin(), false) then raise exception 'not allowed'; end if;
  if p_decision not in ('paid','rejected') then raise exception 'bad decision'; end if;
  select * into r from public.payout_requests where id = p_payout for update;
  if not found or r.status <> 'requested' then raise exception 'This payout is not waiting.'; end if;
  update public.payout_requests set status = p_decision, decided_by = auth.uid(), decided_at = now(), provider_ref = p_ref, note = p_note where id = p_payout;
  if p_decision = 'rejected' then
    insert into public.creator_ledger(creator_id, kind, currency_code, amount_minor, payout_id, note) values (r.creator_id, 'payout_reversal', r.currency_code, r.amount_minor, p_payout, p_note);
  end if;
  insert into public.audit_log(actor, action, target, detail) values (auth.uid(), 'payout.' || p_decision, p_payout::text, jsonb_build_object('amount_minor', r.amount_minor, 'currency', r.currency_code, 'ref', p_ref));
end $$;
revoke all on function public.decide_payout(uuid,text,text,text) from public, anon;
grant execute on function public.decide_payout(uuid,text,text,text) to authenticated;

create or replace function public.report_creator_content(p_course uuid, p_reason text) returns void
language sql security definer set search_path = public as $$
  insert into public.creator_reports(reporter, course_id, reason) values (auth.uid(), p_course, left(p_reason, 600)) $$;
revoke all on function public.report_creator_content(uuid,text) from public, anon;
grant execute on function public.report_creator_content(uuid,text) to authenticated;
