-- 0023 School and tutor licences, the free teacher plan, and verified certificates with a plan. Safe to run more than once.
--  * Free (no licence or trial): a school or tutor workspace can run 1 active class of up to 40 students.
--  * Licence: priced per student per year (plans with audience 'school'); covers every student in the school and
--    every student in its classes, up to the number of students bought (entitlements.seats).
--  * New schools get a 30-day trial (platform_config.school_trial_days); schools and workspaces that exist now get one too.
--  * Course certificates: passing still records the score, but the verified certificate is issued only with a plan,
--    trial or school licence. claim_certificate() issues it later for a course already passed.

alter table public.platform_config
  add column if not exists school_trial_days  integer not null default 30 check (school_trial_days between 0 and 120),
  add column if not exists free_classes       integer not null default 1  check (free_classes >= 0),
  add column if not exists free_class_size    integer not null default 40 check (free_class_size >= 1);
alter table public.entitlements add column if not exists seats integer check (seats is null or seats between 1 and 100000);

create or replace function public.school_has_access(p_school uuid) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.entitlements e where e.school_id = p_school
    and ((e.status = 'active' and coalesce(e.current_period_end, 'infinity') > now())
      or (e.status = 'trialing' and coalesce(e.trial_ends_at, '-infinity') > now()))) $$;
revoke all on function public.school_has_access(uuid) from public, anon, authenticated;
grant execute on function public.school_has_access(uuid) to service_role;

-- the licence (or trial) row a school is using now, newest first
create or replace function public._school_ent(p_school uuid) returns public.entitlements
language sql stable security definer set search_path = public as $$
  select e.* from public.entitlements e where e.school_id = p_school
    and ((e.status = 'active' and coalesce(e.current_period_end, 'infinity') > now())
      or (e.status = 'trialing' and coalesce(e.trial_ends_at, '-infinity') > now()))
  order by (e.status = 'active') desc, e.created_at desc limit 1 $$;
revoke all on function public._school_ent(uuid) from public, anon, authenticated;

-- students who belong to a school: its own students plus anyone in one of its classes
create or replace function public.school_students(p_school uuid) returns integer
language sql stable security definer set search_path = public as $$
  select count(*)::int from (
    select p.id from public.profiles p where p.school_id = p_school and p.role = 'student'
    union
    select cm.student_id from public.class_members cm join public.classes c on c.id = cm.class_id where c.school_id = p_school) x $$;
revoke all on function public.school_students(uuid) from public, anon, authenticated;

create or replace function public.class_size(p_class uuid) returns integer
language sql stable security definer set search_path = public as $$
  select count(*)::int from (
    select p.id from public.profiles p where p.class_id = p_class and p.role = 'student'
    union
    select cm.student_id from public.class_members cm where cm.class_id = p_class) x $$;
revoke all on function public.class_size(uuid) from public, anon, authenticated;

-- access now also comes from a licence held by the workspace of any class the student has joined with a code
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
      and e.status = 'active' and coalesce(e.current_period_end, 'infinity') > now())
  or exists (   -- a class whose school or tutor workspace has a licence or trial
    select 1 from public.class_members cm join public.classes c on c.id = cm.class_id
    where cm.student_id = p_user and not c.archived and public.school_has_access(c.school_id)) $$;
revoke all on function public.user_has_access(uuid) from public, anon, authenticated;
grant execute on function public.user_has_access(uuid) to service_role;

-- ---------- limits on classes and students ----------
create or replace function public.check_class_limit() returns trigger
language plpgsql security definer set search_path = public as $$
declare cfg public.platform_config; n integer;
begin
  if tg_op = 'UPDATE' and not (old.archived and not new.archived) then return new; end if;
  if new.archived or public.school_has_access(new.school_id) then return new; end if;
  select * into cfg from public.platform_config where id = 'global';
  select count(*) into n from public.classes where school_id = new.school_id and not archived and id <> new.id;
  if n >= cfg.free_classes then
    raise exception 'The free plan includes % active class. Archive a class or buy a licence to add more.', cfg.free_classes using errcode = 'P0001';
  end if;
  return new;
end $$;
drop trigger if exists classes_limit on public.classes;
create trigger classes_limit before insert or update of archived on public.classes
for each row execute function public.check_class_limit();

-- one student joining a class: the free class size, or the number of students the licence covers
create or replace function public._check_seat(p_class uuid, p_student uuid) returns void
language plpgsql security definer set search_path = public as $$
declare sch uuid; cfg public.platform_config; e public.entitlements;
begin
  if p_class is null then return; end if;
  select school_id into sch from public.classes where id = p_class;
  if sch is null then return; end if;
  if exists (select 1 from public.profiles where id = p_student and class_id = p_class)
     or exists (select 1 from public.class_members where class_id = p_class and student_id = p_student) then return; end if;
  e := public._school_ent(sch);
  if e.id is null then
    select * into cfg from public.platform_config where id = 'global';
    if public.class_size(p_class) >= cfg.free_class_size then
      raise exception 'This class is full on the free plan (% students). Ask your teacher about a licence.', cfg.free_class_size using errcode = 'P0001';
    end if;
  elsif e.seats is not null and public.school_students(sch) >= e.seats
        and not exists (select 1 from public.profiles where id = p_student and school_id = sch)
        and not exists (select 1 from public.class_members cm join public.classes c on c.id = cm.class_id where cm.student_id = p_student and c.school_id = sch) then
    raise exception 'The licence covers % students and they are all in use. Ask the school to add more.', e.seats using errcode = 'P0001';
  end if;
end $$;
revoke all on function public._check_seat(uuid, uuid) from public, anon, authenticated;

create or replace function public.check_member_seat() returns trigger
language plpgsql security definer set search_path = public as $$
begin perform public._check_seat(new.class_id, new.student_id); return new; end $$;
drop trigger if exists class_members_seat on public.class_members;
create trigger class_members_seat before insert on public.class_members
for each row execute function public.check_member_seat();

create or replace function public.check_profile_seat() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if new.role = 'student' and new.class_id is not null and (tg_op = 'INSERT' or new.class_id is distinct from old.class_id) then
    perform public._check_seat(new.class_id, new.id);
  end if;
  return new;
end $$;
drop trigger if exists profiles_seat on public.profiles;
create trigger profiles_seat before insert or update of class_id on public.profiles
for each row execute function public.check_profile_seat();

-- ---------- trials for schools ----------
create or replace function public.start_school_trial() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if new.kind = 'school' and not exists (select 1 from public.entitlements where school_id = new.id) then
    insert into public.entitlements (school_id, status, trial_ends_at)
    select new.id, 'trialing', now() + make_interval(days => c.school_trial_days) from public.platform_config c where c.id = 'global';
  end if;
  return new;
end $$;
revoke all on function public.start_school_trial() from public, anon, authenticated;
drop trigger if exists schools_start_trial on public.schools;
create trigger schools_start_trial after insert on public.schools for each row execute function public.start_school_trial();

-- every school and tutor workspace that exists now gets 30 days to set up (runs once: they then have a row)
insert into public.entitlements (school_id, status, trial_ends_at)
select s.id, 'trialing', now() + make_interval(days => c.school_trial_days)
from public.schools s cross join public.platform_config c
where c.id = 'global' and not exists (select 1 from public.entitlements e where e.school_id = s.id);

-- what the staff portal shows on Settings > Plan
create or replace function public.my_school_plan() returns jsonb
language plpgsql stable security definer set search_path = public as $$
declare me record; e public.entitlements; c public.platform_config; s record;
begin
  select id, role, school_id into me from public.profiles where id = auth.uid();
  if me.school_id is null or me.role not in ('school_admin','teacher','subject_teacher') then return null; end if;
  select id, kind, country_code into s from public.schools where id = me.school_id;
  select * into c from public.platform_config where id = 'global';
  e := public._school_ent(me.school_id);
  return jsonb_build_object(
    'licensed', e.id is not null, 'status', e.status, 'trial_ends_at', e.trial_ends_at, 'paid_until', e.current_period_end,
    'seats', e.seats, 'students', public.school_students(me.school_id),
    'classes', (select count(*) from public.classes where school_id = me.school_id and not archived),
    'free_classes', c.free_classes, 'free_class_size', c.free_class_size,
    'kind', s.kind, 'country', s.country_code, 'min_students', case when s.kind = 'tutor' then 10 else 30 end,
    'plan', (select jsonb_build_object('code', p.code, 'currency', p.currency_code, 'per_student', p.amount_minor)
               from public.plans p where p.audience = 'school' and p.active and p.country_code = s.country_code limit 1));
end $$;
revoke all on function public.my_school_plan() from public, anon;
grant execute on function public.my_school_plan() to authenticated;

-- ---------- certificates with a plan ----------
create or replace function public.submit_course_quiz(p_course text, p_answers jsonb) returns jsonb
language plpgsql security definer set search_path = public as $$
declare locked boolean := false; c record; done int; total int; ok int := 0; sc int; passed boolean; cert text; nm text; rev jsonb := '[]'::jsonb; k record; given int;
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  select * into c from public.courses where slug = p_course and active;
  if not found then raise exception 'unknown course'; end if;
  select count(*) into done from public.course_lessons l
    where l.course = p_course and l.lesson_id = any(coalesce((select lessons_done from public.course_progress where user_id = auth.uid() and course = p_course), '{}'));
  if done < c.lesson_count then raise exception 'Finish all % lessons before the quiz.', c.lesson_count; end if;
  if (select count(*) from public.course_attempts where user_id = auth.uid() and course = p_course and created_at > now() - interval '1 day') >= 5 then
    raise exception 'You have used 5 attempts today. Review the lessons and try again tomorrow.'; end if;
  select count(*) into total from public.course_keys where course = p_course;
  if total = 0 then raise exception 'This course quiz is not available yet.'; end if;
  for k in select * from public.course_keys where course = p_course order by qid loop
    given := case when jsonb_typeof(p_answers -> k.qid) = 'number' then (p_answers ->> k.qid)::int else null end;
    if given is not distinct from k.answer then ok := ok + 1;
      rev := rev || jsonb_build_array(jsonb_build_object('qid', k.qid, 'ok', true));
    else rev := rev || jsonb_build_array(jsonb_build_object('qid', k.qid, 'ok', false, 'why', k.why)); end if;
  end loop;
  sc := round(100.0 * ok / total); passed := sc >= c.pass_mark;
  insert into public.course_attempts(user_id, course, score) values (auth.uid(), p_course, sc);
  update public.course_progress set best_score = greatest(coalesce(best_score, 0), sc), updated_at = now()
    where user_id = auth.uid() and course = p_course;
  if passed then
    select code into cert from public.certificates where user_id = auth.uid() and course = p_course;
    if cert is null and not public.user_has_access(auth.uid()) then
      locked := true;   -- the pass is saved (best_score); the verified certificate comes with a plan: claim_certificate()
    elsif cert is null then
      select first_name || ' ' || surname into nm from public.profiles where id = auth.uid();
      cert := upper(substr(replace(gen_random_uuid()::text, '-', ''), 1, 12));
      insert into public.certificates(code, user_id, course, score, holder_name) values (cert, auth.uid(), p_course, sc, nm);
    end if;
  end if;
  return jsonb_build_object('score', sc, 'passed', passed, 'correct', ok, 'total', total, 'pass_mark', c.pass_mark, 'code', cert, 'locked', locked, 'review', rev);
end $$;
revoke all on function public.submit_course_quiz(text,jsonb) from public, anon;
grant execute on function public.submit_course_quiz(text,jsonb) to authenticated;

-- issues the certificate for a course the caller already passed, once they have a plan, trial or school licence
create or replace function public.claim_certificate(p_course text) returns jsonb
language plpgsql security definer set search_path = public as $$
declare c record; best int; cert text; nm text;
begin
  if auth.uid() is null then raise exception 'not signed in'; end if;
  select * into c from public.courses where slug = p_course;
  if not found then raise exception 'unknown course'; end if;
  select code into cert from public.certificates where user_id = auth.uid() and course = p_course;
  if cert is not null then return jsonb_build_object('code', cert); end if;
  select best_score into best from public.course_progress where user_id = auth.uid() and course = p_course;
  if coalesce(best, 0) < c.pass_mark then raise exception 'Pass the course quiz first.'; end if;
  if not public.user_has_access(auth.uid()) then raise exception 'Verified certificates come with an Ace plan.'; end if;
  select first_name || ' ' || surname into nm from public.profiles where id = auth.uid();
  cert := upper(substr(replace(gen_random_uuid()::text, '-', ''), 1, 12));
  insert into public.certificates(code, user_id, course, score, holder_name) values (cert, auth.uid(), p_course, best, nm);
  return jsonb_build_object('code', cert, 'score', best);
end $$;
revoke all on function public.claim_certificate(text) from public, anon;
grant execute on function public.claim_certificate(text) to authenticated;

-- courses passed without a certificate yet (to offer "claim")
create or replace function public.my_passed_uncertified() returns table (course text, score integer)
language sql stable security definer set search_path = public as $$
  select cp.course, cp.best_score from public.course_progress cp join public.courses c on c.slug = cp.course
  where cp.user_id = auth.uid() and cp.best_score >= c.pass_mark
    and not exists (select 1 from public.certificates ce where ce.user_id = auth.uid() and ce.course = cp.course) $$;
revoke all on function public.my_passed_uncertified() from public, anon;
grant execute on function public.my_passed_uncertified() to authenticated;

-- ---------- school licence prices (tools/plan_prices.py --school) ----------
insert into public.plans (code, name, country_code, currency_code, amount_minor, period, audience, seats, active) values
 ('gb_school', 'School licence (per student, 1 year)', 'GB', 'GBP', 1200, 'year', 'school', 1, true),
 ('ie_school', 'School licence (per student, 1 year)', 'IE', 'EUR', 1200, 'year', 'school', 1, true),
 ('mt_school', 'School licence (per student, 1 year)', 'MT', 'EUR', 1200, 'year', 'school', 1, true),
 ('es_school', 'School licence (per student, 1 year)', 'ES', 'EUR', 1200, 'year', 'school', 1, true),
 ('fr_school', 'School licence (per student, 1 year)', 'FR', 'EUR', 1200, 'year', 'school', 1, true),
 ('ca_school', 'School licence (per student, 1 year)', 'CA', 'CAD', 1800, 'year', 'school', 1, true),
 ('za_school', 'School licence (per student, 1 year)', 'ZA', 'ZAR', 13500, 'year', 'school', 1, true),
 ('bw_school', 'School licence (per student, 1 year)', 'BW', 'BWP', 9000, 'year', 'school', 1, true),
 ('ng_school', 'School licence (per student, 1 year)', 'NG', 'NGN', 360000, 'year', 'school', 1, true),
 ('gh_school', 'School licence (per student, 1 year)', 'GH', 'GHS', 4500, 'year', 'school', 1, true),
 ('ke_school', 'School licence (per student, 1 year)', 'KE', 'KES', 45000, 'year', 'school', 1, true),
 ('ug_school', 'School licence (per student, 1 year)', 'UG', 'UGX', 1500000, 'year', 'school', 1, true),
 ('tz_school', 'School licence (per student, 1 year)', 'TZ', 'TZS', 1050000, 'year', 'school', 1, true),
 ('zm_school', 'School licence (per student, 1 year)', 'ZM', 'ZMW', 9000, 'year', 'school', 1, true),
 ('sl_school', 'School licence (per student, 1 year)', 'SL', 'SLE', 9000, 'year', 'school', 1, true),
 ('gm_school', 'School licence (per student, 1 year)', 'GM', 'GMD', 30000, 'year', 'school', 1, true),
 ('zw_school', 'School licence (per student, 1 year)', 'ZW', 'USD', 450, 'year', 'school', 1, true),
 ('lr_school', 'School licence (per student, 1 year)', 'LR', 'USD', 450, 'year', 'school', 1, true)
on conflict (code) do update set name = excluded.name, country_code = excluded.country_code, currency_code = excluded.currency_code,
  amount_minor = excluded.amount_minor, period = excluded.period, seats = excluded.seats, active = excluded.active;
