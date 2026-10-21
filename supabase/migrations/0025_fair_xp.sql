-- 0025 Fair XP and streaks. Safe to run more than once.
-- Students write their own stats row (progress is earned in the app, often offline), so the server now limits
-- what a write can change instead of trusting it:
--   * XP can go up by at most 500 per save and 3,000 per day (a very heavy study day is well under this).
--   * The weekly league total (week_xp) is only ever worked out here from real XP gains; writes to it are ignored.
--   * A streak can grow by at most one day per new study day, and the last study day cannot be in the future.
--   * Students can no longer delete their stats row (which would reset the limits).
--   * At most 300 quiz or mock results a day per student.
-- Server-side writes (edge functions, admin tools: no signed-in user) are not limited.

alter table public.user_stats add column if not exists day_key date;
alter table public.user_stats add column if not exists day_xp integer not null default 0 check (day_xp >= 0);

create or replace function public.guard_stats() returns trigger
language plpgsql as $$
declare wk date := date_trunc('week', now())::date; gain integer; room integer;
begin
  if coalesce(auth.uid()::text, '') = '' then          -- service role / admin: trust, but keep the week total right
    gain := greatest(0, new.xp - coalesce(case when tg_op = 'UPDATE' then old.xp end, 0));
  elsif tg_op = 'INSERT' then
    new.xp := least(greatest(coalesce(new.xp, 0), 0), 2000);
    new.streak := least(greatest(coalesce(new.streak, 0), 0), 60);
    if new.last_day > current_date + 1 then new.last_day := current_date; end if;
    new.day_key := current_date; new.day_xp := new.xp; new.week_start := null; new.week_xp := 0;
    gain := new.xp;
  else
    -- XP: at most +500 per save and +3,000 per day
    if old.day_key is distinct from current_date then new.day_key := current_date; new.day_xp := 0;
    else new.day_key := old.day_key; new.day_xp := old.day_xp; end if;
    gain := greatest(0, new.xp - old.xp);
    room := greatest(0, 3000 - new.day_xp);
    gain := least(gain, 500, room);
    new.xp := case when new.xp < old.xp then new.xp else old.xp + gain end;
    new.day_xp := new.day_xp + gain;
    -- the league total is never taken from the client
    new.week_xp := old.week_xp; new.week_start := old.week_start;
    -- streaks: one more day only when a new study day is recorded
    if new.last_day > current_date + 1 then new.last_day := old.last_day; end if;
    if new.streak > old.streak then
      if old.last_day is null or new.last_day > old.last_day then new.streak := old.streak + 1;
      else new.streak := old.streak; end if;
    end if;
  end if;
  if new.week_start is distinct from wk then new.week_start := wk; new.week_xp := gain;
  else new.week_xp := coalesce(new.week_xp, 0) + gain; end if;
  return new;
end $$;

drop trigger if exists stats_clamp on public.user_stats;
drop trigger if exists stats_week on public.user_stats;
drop trigger if exists stats_guard on public.user_stats;
create trigger stats_guard before insert or update on public.user_stats for each row execute function public.guard_stats();
revoke delete on public.user_stats from authenticated, anon;

create or replace function public.guard_attempts() returns trigger
language plpgsql as $$
begin
  if coalesce(auth.uid()::text, '') <> '' and
     (select count(*) from public.quiz_attempts where user_id = new.user_id and created_at > now() - interval '1 day') >= 300 then
    raise exception 'Too many results saved today. Try again tomorrow.';
  end if;
  return new;
end $$;
drop trigger if exists attempts_guard on public.quiz_attempts;
create trigger attempts_guard before insert on public.quiz_attempts for each row execute function public.guard_attempts();
