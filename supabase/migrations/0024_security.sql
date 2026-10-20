-- 0024 Security hardening. Safe to run more than once.
--  1. Codes (class, school, friend, family links) come from the cryptographic generator behind gen_random_uuid(),
--     not random(), so they cannot be predicted.
--  2. Guessing codes is rate limited: 10 wrong class or friend codes and 5 wrong promo codes an hour per account,
--     30 wrong family-link codes per 10 minutes per address.
--  3. A teacher can only add a student to a class directly when the student already belongs to that school;
--     everyone else joins with the class code. (Before this, any tutor could add any student id to a class and then
--     read that student's profile.)
--  4. A school admin can no longer change the fields only Ace staff should change (active, kind, owner, country, code).
--  5. Signed-out visitors can no longer call the friend functions or read creators' fee and review fields.

-- ---------- 1. secure random ----------
create or replace function public.secure_random() returns double precision
language sql volatile as $$
  select ((get_byte(b, 0)::bigint << 40) + (get_byte(b, 1)::bigint << 32) + (get_byte(b, 2)::bigint << 24)
        + (get_byte(b, 3)::bigint << 16) + (get_byte(b, 4)::bigint << 8) + get_byte(b, 5)::bigint) / 281474976710656.0
  from (select uuid_send(gen_random_uuid()) as b) x $$;

create or replace function public.gen_school_code(prefix text default 'SCH')
returns text language plpgsql as $$
declare
  alphabet constant text := 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';  -- no 0/O/1/I
  suffix text; code text; i int;
begin
  loop
    suffix := '';
    for i in 1..4 loop
      suffix := suffix || substr(alphabet, 1 + floor(public.secure_random()*length(alphabet))::int, 1);
    end loop;
    code := upper(left(regexp_replace(prefix,'[^A-Za-z]','','g'),3)) || '-' || suffix;
    exit when not exists (select 1 from public.schools where school_code = code);
  end loop;
  return code;
end $$;

create or replace function public.gen_student_number(cc text)
returns text language plpgsql as $$
declare n text;
begin
  loop
    n := cc || '-' || to_char(now(),'YY') || '-' || lpad(floor(public.secure_random()*1000000)::text, 6, '0');
    exit when not exists (select 1 from public.profiles where student_number = n);
  end loop;
  return n;
end $$;

create or replace function public.create_family_link(p_label text default null)
returns text language plpgsql security definer set search_path = public as $$
declare uid uuid := auth.uid(); alphabet text := 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; c text; i int;
begin
  if uid is null then raise exception 'Sign in first.'; end if;
  if (select count(*) from family_links where student_id = uid and revoked_at is null and expires_at > now()) >= 3 then
    raise exception 'You already have 3 active links. Stop one first.';
  end if;
  loop
    c := ''; for i in 1..12 loop c := c || substr(alphabet, 1 + floor(public.secure_random()*32)::int, 1); end loop;
    exit when not exists (select 1 from family_links where code = c);
  end loop;
  insert into family_links(student_id, code, label) values (uid, c, nullif(left(trim(coalesce(p_label,'')),40),''));
  return c;
end $$;

create or replace function public.gen_join_code() returns text
language plpgsql as $$
declare alphabet constant text := 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'; c text; i int;
begin
  loop
    c := '';
    for i in 1..6 loop c := c || substr(alphabet, 1 + floor(public.secure_random() * length(alphabet))::int, 1); end loop;
    exit when not exists (select 1 from public.classes where join_code = c);
  end loop;
  return c;
end $$;

create or replace function public.my_friend_code() returns text language plpgsql security definer set search_path = public as $$
declare c text; me uuid := auth.uid();
begin
  if me is null then raise exception 'Sign in first.'; end if;
  select friend_code into c from profiles where id = me;
  while c is null loop
    c := (select string_agg(substr('ABCDEFGHJKLMNPQRSTUVWXYZ23456789', 1 + floor(public.secure_random() * 32)::int, 1), '') from generate_series(1, 8));
    begin update profiles set friend_code = c where id = me; exception when unique_violation then c := null; end;
  end loop;
  return c;
end $$;

-- ---------- 2. throttling code guesses ----------
create table if not exists public.code_attempts (
  key  text not null,
  kind text not null,
  at   timestamptz not null default now()
);
create index if not exists code_attempts_idx on public.code_attempts (key, kind, at);
alter table public.code_attempts enable row level security;
revoke all on public.code_attempts from anon, authenticated;

-- who is trying: the signed-in account, or the caller's address for signed-out requests
create or replace function public._attempt_key() returns text
language sql stable as $$
  select coalesce(auth.uid()::text,
    'ip:' || coalesce(nullif(trim(split_part(coalesce(nullif(current_setting('request.headers', true), '')::json ->> 'x-forwarded-for', ''), ',', 1)), ''), 'unknown')) $$;
create or replace function public._too_many(p_kind text, p_max int, p_minutes int) returns boolean
language sql stable security definer set search_path = public as $$
  select count(*) >= p_max from public.code_attempts
  where key = public._attempt_key() and kind = p_kind and at > now() - make_interval(mins => p_minutes) $$;
create or replace function public._note_fail(p_kind text) returns void
language sql security definer set search_path = public as $$
  insert into public.code_attempts (key, kind) values (public._attempt_key(), p_kind);
  delete from public.code_attempts where at < now() - interval '2 days' and random() < 0.01 $$;
revoke all on function public._too_many(text, int, int), public._note_fail(text) from public, anon, authenticated;

create or replace function public.join_class(p_code text)
returns jsonb language plpgsql security definer set search_path = public as $$
declare c record; me record; t text;
begin
  select id, role into me from public.profiles where id = auth.uid();
  if me.id is null then raise exception 'Sign in first.'; end if;
  if me.role <> 'student' then raise exception 'Only student accounts can join a class with a code.'; end if;
  if public._too_many('join', 10, 60) then return jsonb_build_object('error', 'Too many wrong codes. Wait an hour and try again.'); end if;
  select cl.id, cl.name, cl.subject, cl.archived, s.name as school, s.kind into c
    from public.classes cl join public.schools s on s.id = cl.school_id
   where cl.join_code = upper(trim(p_code)) and s.active;
  if c.id is null or c.archived then
    perform public._note_fail('join');   -- kept: the function returns instead of raising, so the attempt is counted
    return jsonb_build_object('error', 'No class with that code. Check it with your teacher.');
  end if;
  insert into public.class_members (class_id, student_id) values (c.id, auth.uid()) on conflict do nothing;
  select string_agg(distinct p.first_name || ' ' || p.surname, ', ') into t
    from public.profiles p
   where p.id in (select teacher_id from public.teacher_subjects where class_id = c.id)
      or (p.role = 'school_admin' and p.school_id = (select school_id from public.classes where id = c.id) and c.kind = 'tutor');
  return jsonb_build_object('class_id', c.id, 'name', c.name, 'subject', c.subject, 'school', c.school, 'kind', c.kind, 'teachers', t);
end $$;

create or replace function public.add_friend(p_code text) returns text language plpgsql security definer set search_path = public as $$
declare me uuid := auth.uid(); other uuid; r friendships;
begin
  if me is null then raise exception 'Sign in first.'; end if;
  if public._too_many('friend', 10, 60) then return 'error:Too many wrong codes. Wait an hour and try again.'; end if;
  select id into other from profiles where friend_code = upper(regexp_replace(coalesce(p_code, ''), '[^A-Za-z0-9]', '', 'g'));
  if other is null then perform public._note_fail('friend'); return 'error:No one has that friend code. Check it and try again.'; end if;
  if other = me then raise exception 'That is your own code. Share it with a friend instead.'; end if;
  if (select count(*) from friendships where me in (a, b)) >= 50 then raise exception 'You can have up to 50 friends.'; end if;
  select * into r from friendships where a = least(me, other) and b = greatest(me, other);
  if r.a is null then
    insert into friendships (a, b, requested_by) values (least(me, other), greatest(me, other), me);
    return 'sent';
  elsif r.status = 'pending' and r.requested_by <> me then
    update friendships set status = 'accepted' where a = r.a and b = r.b; return 'accepted';
  elsif r.status = 'accepted' then return 'already';
  else return 'sent'; end if;
end $$;

create or replace function public.redeem_promo(p_code text) returns jsonb
language plpgsql security definer set search_path = public as $$
declare pc public.promo_codes; uid uuid := auth.uid(); ent uuid; base timestamptz;
begin
  if uid is null then raise exception 'sign in first'; end if;
  if public._too_many('promo', 5, 60) then return jsonb_build_object('ok', false, 'error', 'Too many wrong codes. Wait an hour and try again.'); end if;
  select * into pc from public.promo_codes where code = p_code::citext for update;
  if not found or not pc.active or (pc.expires_at is not null and pc.expires_at < now())
     or (pc.max_uses is not null and pc.used_count >= pc.max_uses) then
    perform public._note_fail('promo');
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

create or replace function public.family_view(p_code text)
returns jsonb language plpgsql security definer set search_path = public as $$
declare l family_links; p profiles; s user_stats; week jsonb; subj jsonb; att jsonb; crs jsonb;
        norm text := upper(regexp_replace(coalesce(p_code,''), '[^A-Za-z0-9]', '', 'g'));
begin
  if public._too_many('family', 30, 10) then return null; end if;
  select * into l from family_links where family_links.code = norm and revoked_at is null and expires_at > now();
  if not found then perform public._note_fail('family'); return null; end if;
  update family_links set last_viewed = now() where id = l.id;
  select * into p from profiles where id = l.student_id;
  select * into s from user_stats where user_id = l.student_id;
  select coalesce(jsonb_agg(jsonb_build_object('day', d, 'questions', q, 'correct', c) order by d), '[]') into week
    from (select g::date d, coalesce(sum(a.total),0)::int q, coalesce(sum(a.correct),0)::int c
          from generate_series(current_date - 6, current_date, '1 day') g
          left join quiz_attempts a on a.user_id = l.student_id and a.created_at::date = g::date
          group by g) x;
  select coalesce(jsonb_agg(jsonb_build_object('subject', subject, 'questions', q, 'correct', c) order by q desc), '[]') into subj
    from (select subject, sum(total)::int q, sum(correct)::int c from quiz_attempts
          where user_id = l.student_id and created_at > now() - interval '30 days' group by subject order by sum(total) desc limit 8) y;
  select coalesce(jsonb_object_agg(status, n), '{}') into att
    from (select status, count(*)::int n from attendance where student_id = l.student_id and day > current_date - 30 group by status) z;
  select coalesce(jsonb_agg(jsonb_build_object('title', c.title, 'lessons', cardinality(cp.lessons_done), 'of', c.lesson_count,
         'certified', exists(select 1 from certificates ce where ce.user_id = l.student_id and ce.course = c.slug))), '[]') into crs
    from course_progress cp join courses c on c.slug = cp.course where cp.user_id = l.student_id;
  return jsonb_build_object('first_name', p.first_name, 'level', p.level, 'streak', coalesce(s.streak,0), 'xp', coalesce(s.xp,0),
    'week', week, 'subjects', subj, 'attendance_30d', att, 'courses', crs, 'link_label', l.label, 'expires_at', l.expires_at);
end $$;

-- group-plan invites: same throttle; a wrong code now returns 'error:...' (the app shows it) so the attempt is kept
drop function if exists public.join_plan(text);
create or replace function public.join_plan(p_code text)
returns text language plpgsql security definer set search_path = public as $$
declare i record; used int; lim int;
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  select * into i from public.plan_invites where code = upper(trim(p_code)) for update;
  if public._too_many('plan', 10, 60) then return 'error:Too many wrong codes. Wait an hour and try again.'; end if;
  if not found or i.used_at is not null or i.expires_at <= now() then perform public._note_fail('plan'); return 'error:This invite is not valid.'; end if;
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
  return 'ok';
end $$;
revoke all on function public.join_plan(text) from public, anon;
grant execute on function public.join_plan(text) to authenticated;

-- ---------- 3. adding students to a class ----------
drop policy if exists cm_staff on public.class_members;
create policy cm_staff on public.class_members for all to authenticated
  using (public.teaches_class(class_id))
  with check (public.teaches_class(class_id) and exists (
    select 1 from public.profiles p join public.classes c on c.id = class_members.class_id
    where p.id = class_members.student_id and p.role = 'student' and p.school_id = c.school_id));

-- ---------- 4. fields on schools that only Ace staff change ----------
create or replace function public.schools_guard() returns trigger
language plpgsql as $$
begin
  if coalesce(auth.uid()::text, '') <> '' and not coalesce(public.is_platform_admin(), false) and (
       new.active is distinct from old.active or new.kind is distinct from old.kind or new.owner_id is distinct from old.owner_id
    or new.country_code is distinct from old.country_code or new.school_code is distinct from old.school_code) then
    raise exception 'Only Ace staff can change that.';
  end if;
  return new;
end $$;
drop trigger if exists schools_guard on public.schools;
create trigger schools_guard before update on public.schools for each row execute function public.schools_guard();

-- ---------- 5. what signed-out visitors can reach ----------
do $$ declare f text; begin
  foreach f in array array['add_friend(text)','my_friend_code()','my_friends()','my_nudges()','nudge_friend(uuid)','remove_friend(uuid)',
                           'respond_friend(uuid, boolean)','has_creator_access(uuid)','is_approved_creator(uuid)','join_class(text)',
                           'redeem_promo(text)','create_family_link(text)'] loop
    execute format('revoke all on function public.%s from public, anon', f);
    execute format('grant execute on function public.%s to authenticated', f);
  end loop;
end $$;
revoke select on public.creator_profiles from anon;
grant select (user_id, handle, display_name, headline, bio, country_code, status, created_at) on public.creator_profiles to anon;
