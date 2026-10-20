-- Class dashboard for teachers + housekeeping triggers.

-- security_invoker so the view respects the caller's RLS (staff see their school only)
create or replace view public.class_overview with (security_invoker = true) as
select p.id            as student_id,
       p.first_name, p.surname, p.class_id, p.school_id, p.exam_target,
       coalesce(s.xp,0)      as xp,
       coalesce(s.streak,0)  as streak,
       s.last_day,
       coalesce(q.attempts,0) as attempts,
       q.avg_pct,
       coalesce(m.mastered,0) as topics_mastered
from public.profiles p
left join public.user_stats s on s.user_id = p.id
left join lateral (
  select count(*) attempts, round(100.0*sum(correct)/nullif(sum(total),0),1) avg_pct
  from public.quiz_attempts a
  where a.user_id = p.id and a.created_at > now() - interval '30 days') q on true
left join lateral (
  select count(*) mastered from public.progress g
  where g.user_id = p.id and g.status = 'mastered') m on true
where p.role = 'student';

grant select on public.class_overview to authenticated;

-- keep progress.updated_at honest
create or replace function public.touch_updated_at() returns trigger
language plpgsql as $$ begin new.updated_at := now(); return new; end $$;

drop trigger if exists progress_touch on public.progress;
create trigger progress_touch before update on public.progress
for each row execute function public.touch_updated_at();

drop trigger if exists stats_touch on public.user_stats;
create trigger stats_touch before update on public.user_stats
for each row execute function public.touch_updated_at();

-- never let a quiz row claim more XP than the app can award: stats are clamped
create or replace function public.clamp_stats() returns trigger
language plpgsql as $$
begin
  if tg_op = 'INSERT' then
    new.xp := least(new.xp, 2000);
  elsif new.xp - old.xp > 2000 then
    new.xp := old.xp + 2000;
  end if;
  return new;
end $$;

drop trigger if exists stats_clamp on public.user_stats;
create trigger stats_clamp before insert or update on public.user_stats
for each row execute function public.clamp_stats();

-- retention: purge old throttling rows (schedule with pg_cron or a Supabase scheduled function)
create or replace function public.purge_login_attempts() returns void
language sql security definer set search_path = public as
$$ delete from public.login_attempts where created_at < now() - interval '2 days' $$;
revoke all on function public.purge_login_attempts() from public, anon, authenticated;
