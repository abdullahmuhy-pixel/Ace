-- Behaviour tests for 0049 (calendar and behaviour log). Needs stubs + all migrations.
\set ON_ERROR_STOP off
truncate public.schools, auth.users cascade;
create or replace function pg_temp.u(n int) returns text language sql immutable as $$ select '49000000-0000-0000-0000-0000000000' || lpad(n::text, 2, '0') $$;
insert into auth.users(id) select pg_temp.u(g)::uuid from generate_series(1,9) g;
insert into public.schools(id,name,country_code,school_code) values
 ('c4900000-0000-0000-0000-00000000000a','School A','NG','AAA-4949'),('c4900000-0000-0000-0000-00000000000b','School B','NG','BBB-4949');
insert into public.classes(id,school_id,name,grade) values
 ('d4900000-0000-0000-0000-0000000000a1','c4900000-0000-0000-0000-00000000000a','A1','SS1'),('d4900000-0000-0000-0000-0000000000a2','c4900000-0000-0000-0000-00000000000a','A2','SS2');
-- 1 admin A, 2 teacher of A1, 3 teacher of A2 only, 4 5 students A1, 6 student A2, 7 admin B
insert into public.profiles(id,role,school_id,class_id,country_code,first_name,surname) values
 (pg_temp.u(1)::uuid,'school_admin','c4900000-0000-0000-0000-00000000000a',null,'NG','Ada','Admin'),
 (pg_temp.u(2)::uuid,'teacher','c4900000-0000-0000-0000-00000000000a',null,'NG','Tola','One'),
 (pg_temp.u(3)::uuid,'teacher','c4900000-0000-0000-0000-00000000000a',null,'NG','Tobi','Two'),
 (pg_temp.u(4)::uuid,'student','c4900000-0000-0000-0000-00000000000a','d4900000-0000-0000-0000-0000000000a1','NG','Sam','One'),
 (pg_temp.u(5)::uuid,'student','c4900000-0000-0000-0000-00000000000a','d4900000-0000-0000-0000-0000000000a1','NG','Sue','Two'),
 (pg_temp.u(6)::uuid,'student','c4900000-0000-0000-0000-00000000000a','d4900000-0000-0000-0000-0000000000a2','NG','Seun','Three'),
 (pg_temp.u(7)::uuid,'school_admin','c4900000-0000-0000-0000-00000000000b',null,'NG','Bimpe','AdminB');
insert into public.teacher_subjects values (pg_temp.u(2)::uuid,'d4900000-0000-0000-0000-0000000000a1','Mathematics'),(pg_temp.u(3)::uuid,'d4900000-0000-0000-0000-0000000000a2','English');
create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin perform set_config('request.jwt.claim.sub', u, false); end $$;
create temp table res(name text, pass boolean); grant all on res to public;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true; begin begin execute sqltext; exception when others then ok := false; end; insert into res values (n, ok = expect_ok); end $$;
create or replace function pg_temp.cnt(n text, sqltext text, expected int) returns void language plpgsql as $$
declare c int; begin begin execute 'select count(*) from (' || sqltext || ') q' into c; exception when others then c := -1; end; insert into res values (n || ' (got ' || c || ')', c = expected); end $$;
create or replace function pg_temp.val(n text, sqltext text, expected text) returns void language plpgsql as $$
declare v text; begin begin execute sqltext into v; exception when others then v := 'ERROR:' || sqlerrm; end; insert into res values (n || ' (got ' || coalesce(v,'null') || ')', v is not distinct from expected); end $$;

set role authenticated;
-- calendar
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('admin adds holiday', $q$insert into public.school_events(school_id,title,kind,starts_on,ends_on) values ('c4900000-0000-0000-0000-00000000000a','Mid-term break','holiday','2026-10-26','2026-10-30')$q$, true);
select pg_temp.check('admin adds staff meeting', $q$insert into public.school_events(school_id,title,kind,starts_on,ends_on,audience) values ('c4900000-0000-0000-0000-00000000000a','Staff meeting','meeting','2026-10-20','2026-10-20','staff')$q$, true);
select pg_temp.check('end before start rejected', $q$insert into public.school_events(school_id,title,starts_on,ends_on) values ('c4900000-0000-0000-0000-00000000000a','x','2026-10-20','2026-10-19')$q$, false);
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('teacher cannot add events', $q$insert into public.school_events(school_id,title,starts_on,ends_on) values ('c4900000-0000-0000-0000-00000000000a','x','2026-10-20','2026-10-20')$q$, false);
select pg_temp.cnt('teacher sees both', 'select * from public.school_events', 2);
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.cnt('student sees only the holiday', 'select * from public.school_events', 1);
select pg_temp.as_user(pg_temp.u(7));
select pg_temp.cnt('other school sees none', 'select * from public.school_events', 0);

-- behaviour
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('teacher gives a merit to own student', $q$insert into public.behaviour_entries(school_id,student_id,kind,category,points,description,visible_to_family) values ('c4900000-0000-0000-0000-00000000000a','49000000-0000-0000-0000-000000000004','merit','Helpfulness',2,'Helped a classmate with fractions',true)$q$, true);
select pg_temp.check('teacher records a concern', $q$insert into public.behaviour_entries(school_id,student_id,kind,category,points,description) values ('c4900000-0000-0000-0000-00000000000a','49000000-0000-0000-0000-000000000004','concern','Homework',-1,'No homework three times')$q$, true);
select pg_temp.check('merit with negative points rejected', $q$insert into public.behaviour_entries(school_id,student_id,kind,points,description) values ('c4900000-0000-0000-0000-00000000000a','49000000-0000-0000-0000-000000000004','merit',-2,'x')$q$, false);
select pg_temp.check('teacher cannot write welfare', $q$insert into public.behaviour_entries(school_id,student_id,kind,description) values ('c4900000-0000-0000-0000-00000000000a','49000000-0000-0000-0000-000000000004','welfare','x')$q$, false);
select pg_temp.check('teacher cannot log a student they do not teach', $q$insert into public.behaviour_entries(school_id,student_id,kind,points,description) values ('c4900000-0000-0000-0000-00000000000a','49000000-0000-0000-0000-000000000006','merit',1,'x')$q$, false);
select pg_temp.check('teacher cannot write in another name', $q$insert into public.behaviour_entries(school_id,student_id,kind,points,description,recorded_by) values ('c4900000-0000-0000-0000-00000000000a','49000000-0000-0000-0000-000000000004','merit',1,'x','49000000-0000-0000-0000-000000000003')$q$, false);
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('admin writes welfare note', $q$insert into public.behaviour_entries(school_id,student_id,kind,description) values ('c4900000-0000-0000-0000-00000000000a','49000000-0000-0000-0000-000000000004','welfare','Family moving house; check in weekly')$q$, true);
select pg_temp.check('welfare cannot be shared with family', $q$insert into public.behaviour_entries(school_id,student_id,kind,description,visible_to_family) values ('c4900000-0000-0000-0000-00000000000a','49000000-0000-0000-0000-000000000004','welfare','x',true)$q$, false);
select pg_temp.check('admin records an incident for A2', $q$insert into public.behaviour_entries(school_id,student_id,kind,points,description,action_taken) values ('c4900000-0000-0000-0000-00000000000a','49000000-0000-0000-0000-000000000006','incident',-3,'Fight at break','Parents called')$q$, true);
select pg_temp.cnt('admin sees all 4', 'select * from public.behaviour_entries', 4);
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.cnt('teacher of A1 sees 2 (no welfare, no A2)', 'select * from public.behaviour_entries', 2);
select pg_temp.check('teacher fixes own entry', $q$update public.behaviour_entries set description='Helped two classmates' where kind='merit'$q$, true);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.cnt('teacher of A2 sees 1', 'select * from public.behaviour_entries', 1);
select pg_temp.check('…cannot change the admin''s entry', $q$update public.behaviour_entries set points=0$q$, true);
select pg_temp.val('…and nothing changed', $q$select points::text from public.behaviour_entries$q$, '-3');
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.cnt('student sees only the shared merit', 'select * from public.behaviour_entries', 1);
select pg_temp.as_user(pg_temp.u(7));
select pg_temp.cnt('admin B sees none', 'select * from public.behaviour_entries', 0);
select pg_temp.cnt('admin B cannot summarise A1', $q$select * from public.class_behaviour('d4900000-0000-0000-0000-0000000000a1','2026-01-01','2099-01-01')$q$, 0);
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.val('class summary for Sam', $q$select merits || '/' || concerns || '/' || points from public.class_behaviour('d4900000-0000-0000-0000-0000000000a1','2026-01-01','2099-01-01') where student_id='49000000-0000-0000-0000-000000000004'$q$, '1/1/1');
select pg_temp.cnt('summary lists the whole class', $q$select * from public.class_behaviour('d4900000-0000-0000-0000-0000000000a1','2026-01-01','2099-01-01')$q$, 2);
reset role;
select pg_temp.as_user('');
select (select count(*) filter (where pass) from res) || ' / ' || count(*) || ' passed' as summary from res;
select name as failed from res where not pass;
