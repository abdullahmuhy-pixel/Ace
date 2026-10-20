-- 0018: study friends. Students add each other with a private friend code (no search, no public profiles),
--   see each other's streak and whether they studied today, keep a shared "friend streak", and send one
--   friendly nudge a day. Friends see only a first name and the first letter of the surname.
--   Safe to run more than once. Needs 0015 (user_stats.week_xp).

alter table public.profiles add column if not exists friend_code text unique check (friend_code ~ '^[A-Z2-9]{8}$');

create table if not exists public.friendships (
  a            uuid not null references public.profiles(id) on delete cascade,
  b            uuid not null references public.profiles(id) on delete cascade,
  status       text not null default 'pending' check (status in ('pending','accepted')),
  requested_by uuid not null references public.profiles(id) on delete cascade,
  created_at   timestamptz not null default now(),
  primary key (a, b),
  check (a < b)
);
alter table public.friendships enable row level security;
drop policy if exists friendships_read on public.friendships;
create policy friendships_read on public.friendships for select to authenticated using (auth.uid() in (a, b));
-- all writes go through the functions below

create table if not exists public.nudges (
  from_id  uuid not null references public.profiles(id) on delete cascade,
  to_id    uuid not null references public.profiles(id) on delete cascade,
  day      date not null default current_date,
  seen     boolean not null default false,
  primary key (from_id, to_id, day)
);
alter table public.nudges enable row level security;
drop policy if exists nudges_read on public.nudges;
create policy nudges_read on public.nudges for select to authenticated using (auth.uid() in (from_id, to_id));

-- days with any study activity (quizzes, daily challenge, topics finished)
create or replace function public.study_days(p_user uuid, p_from date)
returns table (d date) language sql stable security definer set search_path = public as $$
  select distinct created_at::date from quiz_attempts where user_id = p_user and created_at >= p_from
  union
  select distinct updated_at::date from progress where user_id = p_user and updated_at >= p_from
$$;
revoke all on function public.study_days(uuid, date) from public, anon, authenticated;

create or replace function public.are_friends(x uuid, y uuid) returns boolean language sql stable security definer set search_path = public as $$
  select exists (select 1 from friendships where a = least(x, y) and b = greatest(x, y) and status = 'accepted')
$$;

create or replace function public.my_friend_code() returns text language plpgsql security definer set search_path = public as $$
declare c text; me uuid := auth.uid();
begin
  if me is null then raise exception 'Sign in first.'; end if;
  select friend_code into c from profiles where id = me;
  while c is null loop
    c := (select string_agg(substr('ABCDEFGHJKLMNPQRSTUVWXYZ23456789', 1 + floor(random() * 32)::int, 1), '') from generate_series(1, 8));
    begin update profiles set friend_code = c where id = me; exception when unique_violation then c := null; end;
  end loop;
  return c;
end $$;

create or replace function public.add_friend(p_code text) returns text language plpgsql security definer set search_path = public as $$
declare me uuid := auth.uid(); other uuid; r friendships;
begin
  if me is null then raise exception 'Sign in first.'; end if;
  select id into other from profiles where friend_code = upper(regexp_replace(coalesce(p_code, ''), '[^A-Za-z0-9]', '', 'g'));
  if other is null then raise exception 'No one has that friend code. Check it and try again.'; end if;
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

create or replace function public.respond_friend(p_other uuid, p_accept boolean) returns void language plpgsql security definer set search_path = public as $$
declare me uuid := auth.uid();
begin
  if p_accept then
    update friendships set status = 'accepted' where a = least(me, p_other) and b = greatest(me, p_other) and status = 'pending' and requested_by <> me;
  else
    delete from friendships where a = least(me, p_other) and b = greatest(me, p_other);
  end if;
end $$;

create or replace function public.remove_friend(p_other uuid) returns void language sql security definer set search_path = public as $$
  delete from friendships where a = least(auth.uid(), p_other) and b = greatest(auth.uid(), p_other);
$$;

-- consecutive days, ending today (or yesterday if neither has studied yet today), on which both studied
create or replace function public.friend_streak(x uuid, y uuid) returns integer language plpgsql stable security definer set search_path = public as $$
declare n int := 0; d date := current_date; both_days date[];
begin
  select array_agg(sx.d) into both_days from study_days(x, current_date - 400) sx join study_days(y, current_date - 400) sy on sy.d = sx.d;
  if both_days is null then return 0; end if;
  if not (d = any(both_days)) then d := d - 1; end if;
  while d = any(both_days) loop n := n + 1; d := d - 1; end loop;
  return n;
end $$;
revoke all on function public.friend_streak(uuid, uuid) from public, anon, authenticated;

create or replace function public.my_friends()
returns table (friend_id uuid, name text, status text, incoming boolean, streak int, studied_today boolean, week_xp int, friend_streak int, nudged_today boolean, nudged_me boolean)
language sql stable security definer set search_path = public as $$
  with mine as (
    select case when f.a = auth.uid() then f.b else f.a end as other, f.status, f.requested_by
    from friendships f where auth.uid() in (f.a, f.b)
  )
  select m.other,
         trim(coalesce(p.first_name, 'Friend') || ' ' || coalesce(left(p.surname, 1) || '.', '')),
         m.status, (m.status = 'pending' and m.requested_by <> auth.uid()),
         case when m.status = 'accepted' then coalesce(case when us.last_day >= current_date - 1 then us.streak else 0 end, 0) end,
         case when m.status = 'accepted' then exists (select 1 from study_days(m.other, current_date) s) end,
         case when m.status = 'accepted' then coalesce(case when us.week_start = date_trunc('week', current_date)::date then us.week_xp else 0 end, 0) end,
         case when m.status = 'accepted' then public.friend_streak(auth.uid(), m.other) end,
         exists (select 1 from nudges n where n.from_id = auth.uid() and n.to_id = m.other and n.day = current_date),
         exists (select 1 from nudges n where n.from_id = m.other and n.to_id = auth.uid() and n.day = current_date)
  from mine m join profiles p on p.id = m.other left join user_stats us on us.user_id = m.other
  order by (m.status = 'pending') desc, 8 desc nulls last, 2
$$;

create or replace function public.nudge_friend(p_other uuid) returns void language plpgsql security definer set search_path = public as $$
begin
  if not public.are_friends(auth.uid(), p_other) then raise exception 'You can only nudge friends.'; end if;
  insert into nudges (from_id, to_id) values (auth.uid(), p_other) on conflict do nothing;
end $$;

create or replace function public.my_nudges() returns table (name text) language sql security definer set search_path = public as $$
  update nudges set seen = true where to_id = auth.uid() and day = current_date and not seen;
  select trim(coalesce(p.first_name, 'A friend')) from nudges n join profiles p on p.id = n.from_id
  where n.to_id = auth.uid() and n.day = current_date and public.are_friends(n.from_id, n.to_id);
$$;

grant execute on function public.my_friend_code(), public.add_friend(text), public.respond_friend(uuid, boolean),
  public.remove_friend(uuid), public.my_friends(), public.nudge_friend(uuid), public.my_nudges() to authenticated;
revoke execute on function public.are_friends(uuid, uuid) from public, anon;
