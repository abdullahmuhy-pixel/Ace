-- 0022 Free and paid tiers. Safe to run more than once.
--  * Ace (AI) gives 5 uses a day on a free account and up to 60 a day with a plan, trial or school licence.
--  * Photo questions, essay / mark-scheme marking and study packs also have their own smaller limits.
--  * New student accounts get a 7-day trial (platform_config.trial_days); existing students without any plan get one now.
--  * Prices for every market are seeded into public.plans (generated and checked by tools/plan_prices.py).

alter table public.platform_config
  add column if not exists ai_free_cap      integer not null default 5  check (ai_free_cap >= 0),
  add column if not exists ai_paid_cap      integer not null default 60 check (ai_paid_cap >= 0),
  add column if not exists free_photo_day   integer not null default 1  check (free_photo_day >= 0),
  add column if not exists free_essay_week  integer not null default 1  check (free_essay_week >= 0),
  add column if not exists free_pack_week   integer not null default 2  check (free_pack_week >= 0),
  add column if not exists paid_photo_day   integer not null default 20 check (paid_photo_day >= 0),
  add column if not exists paid_essay_day   integer not null default 15 check (paid_essay_day >= 0),
  add column if not exists paid_pack_day    integer not null default 15 check (paid_pack_day >= 0),
  add column if not exists free_mocks_per_subject integer not null default 1 check (free_mocks_per_subject >= 0);

create table if not exists public.ai_tool_usage (
  user_id uuid not null references public.profiles(id) on delete cascade,
  day     date not null default current_date,
  kind    text not null check (kind in ('photo','essay','pack')),
  count   integer not null default 0 check (count >= 0),
  primary key (user_id, day, kind)
);
alter table public.ai_tool_usage enable row level security;
drop policy if exists ai_tool_usage_self on public.ai_tool_usage;
create policy ai_tool_usage_self on public.ai_tool_usage for select to authenticated using (user_id = auth.uid());
revoke insert, update, delete on public.ai_tool_usage from authenticated, anon;

-- One AI use of a given kind ('chat', 'photo', 'essay', 'pack'). Checks every limit, then counts the use atomically.
-- reason: 'ok', 'off' (school turned AI off), 'tool' (limit for this tool), 'daily' (daily cap), 'school' (school's own cap)
create or replace function public.consume_ai_kind(p_user uuid, p_kind text)
returns table (allowed boolean, used integer, cap integer, mode text, reason text, paid boolean)
language plpgsql security definer set search_path = public as $$
declare s record; cfg public.platform_config; is_paid boolean; dcap integer; u integer; tu integer; tcap integer; twin date; swin date; su integer;
begin
  if p_kind is null or p_kind not in ('chat','photo','essay','pack') then p_kind := 'chat'; end if;
  select sc.ai_mode, sc.ai_cap, sc.ai_period into s
    from public.profiles p left join public.schools sc on sc.id = p.school_id where p.id = p_user;
  if not found then return query select false, 0, 0, 'off'::text, 'off'::text, false; return; end if;
  select * into cfg from public.platform_config where id = 'global';
  mode := coalesce(s.ai_mode, 'limited');
  if mode = 'off' then return query select false, 0, 0, mode, 'off'::text, false; return; end if;
  is_paid := public.user_has_access(p_user);
  dcap := case when is_paid then cfg.ai_paid_cap else cfg.ai_free_cap end;

  insert into public.ai_usage (user_id, day, count) values (p_user, current_date, 0) on conflict do nothing;
  perform 1 from public.ai_usage where user_id = p_user and day = current_date for update;   -- serialises this user's uses

  if p_kind <> 'chat' then
    if is_paid then
      tcap := case p_kind when 'photo' then cfg.paid_photo_day when 'essay' then cfg.paid_essay_day else cfg.paid_pack_day end;
      twin := current_date;
    else
      tcap := case p_kind when 'photo' then cfg.free_photo_day when 'essay' then cfg.free_essay_week else cfg.free_pack_week end;
      twin := case p_kind when 'photo' then current_date else current_date - 6 end;
    end if;
    select coalesce(sum(t.count), 0) into tu from public.ai_tool_usage t where t.user_id = p_user and t.kind = p_kind and t.day >= twin;
    if tu >= tcap then return query select false, tu, tcap, mode, 'tool'::text, is_paid; return; end if;
  end if;

  select a.count into u from public.ai_usage a where a.user_id = p_user and a.day = current_date;
  if u >= dcap then return query select false, u, dcap, mode, 'daily'::text, is_paid; return; end if;

  if mode = 'limited' and s.ai_cap is not null then   -- a school can set a tighter cap of its own
    swin := case when coalesce(s.ai_period, 'daily') = 'weekly' then current_date - 6 else current_date end;
    select coalesce(sum(a.count), 0) into su from public.ai_usage a where a.user_id = p_user and a.day >= swin;
    if su >= s.ai_cap then return query select false, su, s.ai_cap, mode, 'school'::text, is_paid; return; end if;
  end if;

  update public.ai_usage a set count = a.count + 1 where a.user_id = p_user and a.day = current_date;
  if p_kind <> 'chat' then
    insert into public.ai_tool_usage (user_id, day, kind, count) values (p_user, current_date, p_kind, 1)
      on conflict (user_id, day, kind) do update set count = public.ai_tool_usage.count + 1;
  end if;
  return query select true, u + 1, dcap, mode, 'ok'::text, is_paid;
end $$;
revoke all on function public.consume_ai_kind(uuid, text) from public, anon, authenticated;
grant execute on function public.consume_ai_kind(uuid, text) to service_role;

-- gives a use back when the model call failed, so a student never loses their one free photo to an outage
create or replace function public.refund_ai(p_user uuid, p_kind text)
returns void language sql security definer set search_path = public as $$
  update public.ai_usage set count = greatest(count - 1, 0) where user_id = p_user and day = current_date;
  update public.ai_tool_usage set count = greatest(count - 1, 0) where user_id = p_user and day = current_date and kind = p_kind $$;
revoke all on function public.refund_ai(uuid, text) from public, anon, authenticated;
grant execute on function public.refund_ai(uuid, text) to service_role;

-- older edge functions still call consume_ai(user): treat it as a chat use
create or replace function public.consume_ai(p_user uuid)
returns table (allowed boolean, used integer, cap integer, mode text)
language sql security definer set search_path = public as $$
  select k.allowed, k.used, k.cap, k.mode from public.consume_ai_kind(p_user, 'chat') k $$;
revoke all on function public.consume_ai(uuid) from public, anon, authenticated;
grant execute on function public.consume_ai(uuid) to service_role;

-- what the app shows: "2 of 5 used today"
create or replace function public.my_ai_usage() returns table (used integer, cap integer, mode text)
language sql stable security definer set search_path = public as $$
  select coalesce((select a.count from public.ai_usage a where a.user_id = auth.uid() and a.day = current_date), 0),
         case when public.user_has_access(auth.uid()) then c.ai_paid_cap else c.ai_free_cap end,
         coalesce(sc.ai_mode, 'limited')
  from public.profiles p left join public.schools sc on sc.id = p.school_id
  cross join public.platform_config c where p.id = auth.uid() and c.id = 'global' $$;

-- everything the app needs to show limits and upgrade prompts, in one call
create or replace function public.my_limits() returns jsonb
language plpgsql stable security definer set search_path = public as $$
declare me uuid := auth.uid(); c public.platform_config; pd boolean; e record; tu jsonb; mk jsonb;
begin
  if me is null then return null; end if;
  select * into c from public.platform_config where id = 'global';
  pd := public.user_has_access(me);
  select status, trial_ends_at, current_period_end, plan_code into e from public.entitlements
   where user_id = me order by created_at desc limit 1;
  select jsonb_build_object(
    'photo', coalesce(sum(count) filter (where kind = 'photo' and day >= case when pd then current_date else current_date end), 0),
    'essay', coalesce(sum(count) filter (where kind = 'essay' and day >= case when pd then current_date else current_date - 6 end), 0),
    'pack',  coalesce(sum(count) filter (where kind = 'pack'  and day >= case when pd then current_date else current_date - 6 end), 0))
    into tu from public.ai_tool_usage where user_id = me and day >= current_date - 6;
  select coalesce(jsonb_object_agg(subject, n), '{}'::jsonb) into mk
    from (select subject, count(*) n from public.quiz_attempts where user_id = me and kind = 'mock' group by subject) x;
  return jsonb_build_object(
    'paid', pd,
    'status', e.status, 'trial_ends_at', e.trial_ends_at, 'paid_until', e.current_period_end, 'plan', e.plan_code,
    'ai', jsonb_build_object('used', coalesce((select a.count from public.ai_usage a where a.user_id = me and a.day = current_date), 0),
                             'cap', case when pd then c.ai_paid_cap else c.ai_free_cap end),
    'photo', jsonb_build_object('used', tu->'photo', 'cap', case when pd then c.paid_photo_day else c.free_photo_day end, 'per', 'day'),
    'essay', jsonb_build_object('used', tu->'essay', 'cap', case when pd then c.paid_essay_day else c.free_essay_week end, 'per', case when pd then 'day' else 'week' end),
    'pack',  jsonb_build_object('used', tu->'pack',  'cap', case when pd then c.paid_pack_day  else c.free_pack_week  end, 'per', case when pd then 'day' else 'week' end),
    'free_mocks', c.free_mocks_per_subject,
    'mocks', mk);
end $$;
revoke all on function public.my_limits() from public, anon;
grant execute on function public.my_limits() to authenticated;

-- 7-day trial for every new student account (once)
create or replace function public.start_trial() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if new.role = 'student' and not exists (select 1 from public.entitlements where user_id = new.id) then
    insert into public.entitlements (user_id, status, trial_ends_at)
    select new.id, 'trialing', now() + make_interval(days => c.trial_days) from public.platform_config c where c.id = 'global';
  end if;
  return new;
end $$;
revoke all on function public.start_trial() from public, anon, authenticated;
drop trigger if exists profiles_start_trial on public.profiles;
create trigger profiles_start_trial after insert on public.profiles for each row execute function public.start_trial();

-- students who signed up before tiers existed get the same 7 days, starting now (runs once: they then have a row)
insert into public.entitlements (user_id, status, trial_ends_at)
select p.id, 'trialing', now() + make_interval(days => c.trial_days)
from public.profiles p cross join public.platform_config c
where c.id = 'global' and p.role = 'student' and not exists (select 1 from public.entitlements e where e.user_id = p.id);

-- prices (tools/plan_prices.py)
insert into public.plans (code, name, country_code, currency_code, amount_minor, period, audience, seats, active) values
 ('gb_month', 'Ace Monthly', 'GB', 'GBP', 499, 'month', 'student', 1, true),
 ('gb_term', 'Ace Termly', 'GB', 'GBP', 1299, 'term', 'student', 1, true),
 ('gb_year', 'Ace Yearly', 'GB', 'GBP', 3999, 'year', 'student', 1, true),
 ('gb_group', 'Ace Group (4 people)', 'GB', 'GBP', 9900, 'year', 'student', 4, true),
 ('ie_month', 'Ace Monthly', 'IE', 'EUR', 499, 'month', 'student', 1, true),
 ('ie_term', 'Ace Termly', 'IE', 'EUR', 1299, 'term', 'student', 1, true),
 ('ie_year', 'Ace Yearly', 'IE', 'EUR', 3999, 'year', 'student', 1, true),
 ('ie_group', 'Ace Group (4 people)', 'IE', 'EUR', 9900, 'year', 'student', 4, true),
 ('mt_month', 'Ace Monthly', 'MT', 'EUR', 499, 'month', 'student', 1, true),
 ('mt_term', 'Ace Termly', 'MT', 'EUR', 1299, 'term', 'student', 1, true),
 ('mt_year', 'Ace Yearly', 'MT', 'EUR', 3999, 'year', 'student', 1, true),
 ('mt_group', 'Ace Group (4 people)', 'MT', 'EUR', 9900, 'year', 'student', 4, true),
 ('es_month', 'Ace Monthly', 'ES', 'EUR', 499, 'month', 'student', 1, true),
 ('es_term', 'Ace Termly', 'ES', 'EUR', 1299, 'term', 'student', 1, true),
 ('es_year', 'Ace Yearly', 'ES', 'EUR', 3999, 'year', 'student', 1, true),
 ('es_group', 'Ace Group (4 people)', 'ES', 'EUR', 9900, 'year', 'student', 4, true),
 ('fr_month', 'Ace Monthly', 'FR', 'EUR', 499, 'month', 'student', 1, true),
 ('fr_term', 'Ace Termly', 'FR', 'EUR', 1299, 'term', 'student', 1, true),
 ('fr_year', 'Ace Yearly', 'FR', 'EUR', 3999, 'year', 'student', 1, true),
 ('fr_group', 'Ace Group (4 people)', 'FR', 'EUR', 9900, 'year', 'student', 4, true),
 ('ca_month', 'Ace Monthly', 'CA', 'CAD', 799, 'month', 'student', 1, true),
 ('ca_term', 'Ace Termly', 'CA', 'CAD', 1999, 'term', 'student', 1, true),
 ('ca_year', 'Ace Yearly', 'CA', 'CAD', 5999, 'year', 'student', 1, true),
 ('ca_group', 'Ace Group (4 people)', 'CA', 'CAD', 14900, 'year', 'student', 4, true),
 ('za_month', 'Ace Monthly', 'ZA', 'ZAR', 5900, 'month', 'student', 1, true),
 ('za_term', 'Ace Termly', 'ZA', 'ZAR', 14900, 'term', 'student', 1, true),
 ('za_year', 'Ace Yearly', 'ZA', 'ZAR', 44900, 'year', 'student', 1, true),
 ('za_group', 'Ace Group (4 people)', 'ZA', 'ZAR', 109900, 'year', 'student', 4, true),
 ('bw_month', 'Ace Monthly', 'BW', 'BWP', 4000, 'month', 'student', 1, true),
 ('bw_term', 'Ace Termly', 'BW', 'BWP', 10000, 'term', 'student', 1, true),
 ('bw_year', 'Ace Yearly', 'BW', 'BWP', 30000, 'year', 'student', 1, true),
 ('bw_group', 'Ace Group (4 people)', 'BW', 'BWP', 75000, 'year', 'student', 4, true),
 ('ng_month', 'Ace Monthly', 'NG', 'NGN', 150000, 'month', 'student', 1, true),
 ('ng_term', 'Ace Termly', 'NG', 'NGN', 400000, 'term', 'student', 1, true),
 ('ng_year', 'Ace Yearly', 'NG', 'NGN', 1200000, 'year', 'student', 1, true),
 ('ng_group', 'Ace Group (4 people)', 'NG', 'NGN', 3000000, 'year', 'student', 4, true),
 ('gh_month', 'Ace Monthly', 'GH', 'GHS', 2000, 'month', 'student', 1, true),
 ('gh_term', 'Ace Termly', 'GH', 'GHS', 5000, 'term', 'student', 1, true),
 ('gh_year', 'Ace Yearly', 'GH', 'GHS', 15000, 'year', 'student', 1, true),
 ('gh_group', 'Ace Group (4 people)', 'GH', 'GHS', 37500, 'year', 'student', 4, true),
 ('ke_month', 'Ace Monthly', 'KE', 'KES', 20000, 'month', 'student', 1, true),
 ('ke_term', 'Ace Termly', 'KE', 'KES', 50000, 'term', 'student', 1, true),
 ('ke_year', 'Ace Yearly', 'KE', 'KES', 150000, 'year', 'student', 1, true),
 ('ke_group', 'Ace Group (4 people)', 'KE', 'KES', 375000, 'year', 'student', 4, true),
 ('ug_month', 'Ace Monthly', 'UG', 'UGX', 700000, 'month', 'student', 1, true),
 ('ug_term', 'Ace Termly', 'UG', 'UGX', 1800000, 'term', 'student', 1, true),
 ('ug_year', 'Ace Yearly', 'UG', 'UGX', 5000000, 'year', 'student', 1, true),
 ('ug_group', 'Ace Group (4 people)', 'UG', 'UGX', 12500000, 'year', 'student', 4, true),
 ('tz_month', 'Ace Monthly', 'TZ', 'TZS', 500000, 'month', 'student', 1, true),
 ('tz_term', 'Ace Termly', 'TZ', 'TZS', 1200000, 'term', 'student', 1, true),
 ('tz_year', 'Ace Yearly', 'TZ', 'TZS', 3500000, 'year', 'student', 1, true),
 ('tz_group', 'Ace Group (4 people)', 'TZ', 'TZS', 8750000, 'year', 'student', 4, true),
 ('zm_month', 'Ace Monthly', 'ZM', 'ZMW', 4000, 'month', 'student', 1, true),
 ('zm_term', 'Ace Termly', 'ZM', 'ZMW', 10000, 'term', 'student', 1, true),
 ('zm_year', 'Ace Yearly', 'ZM', 'ZMW', 30000, 'year', 'student', 1, true),
 ('zm_group', 'Ace Group (4 people)', 'ZM', 'ZMW', 75000, 'year', 'student', 4, true),
 ('sl_month', 'Ace Monthly', 'SL', 'SLE', 4000, 'month', 'student', 1, true),
 ('sl_term', 'Ace Termly', 'SL', 'SLE', 10000, 'term', 'student', 1, true),
 ('sl_year', 'Ace Yearly', 'SL', 'SLE', 30000, 'year', 'student', 1, true),
 ('sl_group', 'Ace Group (4 people)', 'SL', 'SLE', 75000, 'year', 'student', 4, true),
 ('gm_month', 'Ace Monthly', 'GM', 'GMD', 15000, 'month', 'student', 1, true),
 ('gm_term', 'Ace Termly', 'GM', 'GMD', 40000, 'term', 'student', 1, true),
 ('gm_year', 'Ace Yearly', 'GM', 'GMD', 100000, 'year', 'student', 1, true),
 ('gm_group', 'Ace Group (4 people)', 'GM', 'GMD', 250000, 'year', 'student', 4, true),
 ('zw_month', 'Ace Monthly', 'ZW', 'USD', 200, 'month', 'student', 1, true),
 ('zw_term', 'Ace Termly', 'ZW', 'USD', 500, 'term', 'student', 1, true),
 ('zw_year', 'Ace Yearly', 'ZW', 'USD', 1500, 'year', 'student', 1, true),
 ('zw_group', 'Ace Group (4 people)', 'ZW', 'USD', 3750, 'year', 'student', 4, true),
 ('lr_month', 'Ace Monthly', 'LR', 'USD', 200, 'month', 'student', 1, true),
 ('lr_term', 'Ace Termly', 'LR', 'USD', 500, 'term', 'student', 1, true),
 ('lr_year', 'Ace Yearly', 'LR', 'USD', 1500, 'year', 'student', 1, true),
 ('lr_group', 'Ace Group (4 people)', 'LR', 'USD', 3750, 'year', 'student', 4, true),
 ('campus_month', 'Ace Campus Monthly', null, 'USD', 499, 'month', 'student', 1, true),
 ('campus_year', 'Ace Campus Yearly', null, 'USD', 3999, 'year', 'student', 1, true)
on conflict (code) do update set name = excluded.name, country_code = excluded.country_code, currency_code = excluded.currency_code,
  amount_minor = excluded.amount_minor, period = excluded.period, seats = excluded.seats, active = excluded.active;
