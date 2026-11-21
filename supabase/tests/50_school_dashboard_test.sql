-- Behaviour tests for 0050 (management dashboard). Numbers below were worked out by hand.
\set ON_ERROR_STOP off
truncate public.schools, auth.users cascade;
create or replace function pg_temp.u(n int) returns text language sql immutable as $$ select '50000000-0000-0000-0000-0000000000' || lpad(n::text, 2, '0') $$;
insert into auth.users(id) select pg_temp.u(g)::uuid from generate_series(1,9) g;
insert into public.schools(id,name,country_code,school_code) values ('c5000000-0000-0000-0000-00000000000a','School A','NG','AAA-5050'),('c5000000-0000-0000-0000-00000000000b','School B','NG','BBB-5050');
insert into public.classes(id,school_id,name,grade) values ('d5000000-0000-0000-0000-0000000000a1','c5000000-0000-0000-0000-00000000000a','SS1A','SS1'),('d5000000-0000-0000-0000-0000000000a2','c5000000-0000-0000-0000-00000000000a','SS2A','SS2');
insert into public.profiles(id,role,school_id,class_id,country_code,first_name,surname,enrolment_status) values
 (pg_temp.u(1)::uuid,'school_admin','c5000000-0000-0000-0000-00000000000a',null,'NG','Ada','Admin','active'),
 (pg_temp.u(2)::uuid,'teacher','c5000000-0000-0000-0000-00000000000a',null,'NG','Tola','Teach','active'),
 (pg_temp.u(3)::uuid,'school_admin','c5000000-0000-0000-0000-00000000000b',null,'NG','Bimpe','AdminB','active'),
 (pg_temp.u(4)::uuid,'student','c5000000-0000-0000-0000-00000000000a','d5000000-0000-0000-0000-0000000000a1','NG','S','One','active'),
 (pg_temp.u(5)::uuid,'student','c5000000-0000-0000-0000-00000000000a','d5000000-0000-0000-0000-0000000000a1','NG','S','Two','active'),
 (pg_temp.u(6)::uuid,'student','c5000000-0000-0000-0000-00000000000a','d5000000-0000-0000-0000-0000000000a2','NG','S','Three','suspended'),
 (pg_temp.u(7)::uuid,'student','c5000000-0000-0000-0000-00000000000a',null,'NG','S','Four','graduated');
insert into public.teacher_subjects values (pg_temp.u(2)::uuid,'d5000000-0000-0000-0000-0000000000a1','Mathematics'),(pg_temp.u(2)::uuid,'d5000000-0000-0000-0000-0000000000a2','Mathematics');
insert into public.timetable_slots(school_id,class_id,weekday,starts,ends,subject,teacher_id) values
 ('c5000000-0000-0000-0000-00000000000a','d5000000-0000-0000-0000-0000000000a1',1,'08:00','09:00','Mathematics',pg_temp.u(2)::uuid),
 ('c5000000-0000-0000-0000-00000000000a','d5000000-0000-0000-0000-0000000000a2',2,'10:00','10:40','Mathematics',pg_temp.u(2)::uuid);
insert into public.academic_terms(id,school_id,name,starts_on,ends_on) values ('e5000000-0000-0000-0000-000000000001','c5000000-0000-0000-0000-00000000000a','Term 1','2026-09-01','2026-12-15');
insert into public.student_records(student_id,school_id,admitted_on) values (pg_temp.u(4)::uuid,'c5000000-0000-0000-0000-00000000000a','2026-09-02'),(pg_temp.u(5)::uuid,'c5000000-0000-0000-0000-00000000000a','2025-01-10'),(pg_temp.u(6)::uuid,'c5000000-0000-0000-0000-00000000000a','2025-01-10'),(pg_temp.u(7)::uuid,'c5000000-0000-0000-0000-00000000000a','2021-01-10');
insert into public.enrolment_events(student_id,school_id,from_status,to_status,effective_on) values (pg_temp.u(7)::uuid,'c5000000-0000-0000-0000-00000000000a','active','graduated','2026-10-01');
insert into public.term_reports(school_id,term_id,student_id,class_id,class_name) values
 ('c5000000-0000-0000-0000-00000000000a','e5000000-0000-0000-0000-000000000001',pg_temp.u(4)::uuid,'d5000000-0000-0000-0000-0000000000a1','SS1A'),
 ('c5000000-0000-0000-0000-00000000000a','e5000000-0000-0000-0000-000000000001',pg_temp.u(5)::uuid,'d5000000-0000-0000-0000-0000000000a1','SS1A');
-- maths 80, 40; english 60, 50 -> average 57.5; passes (>=50) 3 of 4 = 75%; maths pass rate 50%, english 100%
insert into public.term_results(school_id,term_id,student_id,subject,score) values
 ('c5000000-0000-0000-0000-00000000000a','e5000000-0000-0000-0000-000000000001',pg_temp.u(4)::uuid,'Mathematics',80),
 ('c5000000-0000-0000-0000-00000000000a','e5000000-0000-0000-0000-000000000001',pg_temp.u(5)::uuid,'Mathematics',40),
 ('c5000000-0000-0000-0000-00000000000a','e5000000-0000-0000-0000-000000000001',pg_temp.u(4)::uuid,'English',60),
 ('c5000000-0000-0000-0000-00000000000a','e5000000-0000-0000-0000-000000000001',pg_temp.u(5)::uuid,'English',50);
-- attendance: S1 present x4 -> 100%; S2 present, absent, absent, excused -> 1/3 -> below 90; overall 5 of 7 = 71.4%
insert into public.attendance(class_id,student_id,day,status) values
 ('d5000000-0000-0000-0000-0000000000a1',pg_temp.u(4)::uuid,'2026-09-02','present'),('d5000000-0000-0000-0000-0000000000a1',pg_temp.u(4)::uuid,'2026-09-03','present'),
 ('d5000000-0000-0000-0000-0000000000a1',pg_temp.u(4)::uuid,'2026-09-04','late'),('d5000000-0000-0000-0000-0000000000a1',pg_temp.u(4)::uuid,'2026-09-05','present'),
 ('d5000000-0000-0000-0000-0000000000a1',pg_temp.u(5)::uuid,'2026-09-02','present'),('d5000000-0000-0000-0000-0000000000a1',pg_temp.u(5)::uuid,'2026-09-03','absent'),
 ('d5000000-0000-0000-0000-0000000000a1',pg_temp.u(5)::uuid,'2026-09-04','absent'),('d5000000-0000-0000-0000-0000000000a1',pg_temp.u(5)::uuid,'2026-09-05','excused');
insert into public.behaviour_entries(school_id,student_id,kind,category,points,description,occurred_on) values
 ('c5000000-0000-0000-0000-00000000000a',pg_temp.u(5)::uuid,'concern','Homework',-1,'x','2026-09-10'),('c5000000-0000-0000-0000-00000000000a',pg_temp.u(5)::uuid,'concern','Homework',-1,'x','2026-09-11'),
 ('c5000000-0000-0000-0000-00000000000a',pg_temp.u(5)::uuid,'incident','Fighting',-3,'x','2026-09-12'),('c5000000-0000-0000-0000-00000000000a',pg_temp.u(4)::uuid,'merit','Effort',1,'x','2026-09-12');
create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin perform set_config('request.jwt.claim.sub', u, false); end $$;
create temp table res(name text, pass boolean); grant all on res to public;
create temp table d(j jsonb); grant all on d to public;
create or replace function pg_temp.val(n text, sqltext text, expected text) returns void language plpgsql as $$
declare v text; begin begin execute sqltext into v; exception when others then v := 'ERROR:' || sqlerrm; end; insert into res values (n || ' (got ' || coalesce(v,'null') || ')', v is not distinct from expected); end $$;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true; begin begin execute sqltext; exception when others then ok := false; end; insert into res values (n, ok = expect_ok); end $$;

set role authenticated;
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('teacher cannot open the dashboard', 'select public.school_dashboard()', false);
select pg_temp.as_user(pg_temp.u(1));
-- money: invoice 100 paid 30 due long ago -> overdue 70; payment of 30 inside the term
select pg_temp.check('bill', $q$select public.bill_students(array['50000000-0000-0000-0000-000000000004']::uuid[],'Term 1','NGN','[{"label":"Fees","amount":100}]','[{"due_on":"2026-09-10","amount":100}]')$q$, true);
select pg_temp.check('pay', $q$select public.record_payment((select id from public.fees limit 1),30,'2026-09-15','cash')$q$, true);
insert into d select public.school_dashboard(null, null, 'e5000000-0000-0000-0000-000000000001');
select pg_temp.val('period is the term', $q$select (j->'period'->>'from') || '..' || (j->'period'->>'to') from d$q$, '2026-09-01..2026-12-15');
select pg_temp.val('current students 3 (graduate excluded)', $q$select j->'enrolment'->>'current' from d$q$, '3');
select pg_temp.val('joined this term 1', $q$select j->'enrolment'->>'joined' from d$q$, '1');
select pg_temp.val('left this term 1', $q$select j->'enrolment'->>'left' from d$q$, '1');
select pg_temp.val('SS1A has 2', $q$select x->>'students' from d, jsonb_array_elements(j->'enrolment'->'by_class') x where x->>'class'='SS1A'$q$, '2');
select pg_temp.val('12 months of trend', $q$select jsonb_array_length(j->'enrolment'->'months')::text from d$q$, '12');
select pg_temp.val('average 57.5', $q$select j->'results'->>'average' from d$q$, '57.5');
select pg_temp.val('pass rate 75', $q$select j->'results'->>'pass_rate' from d$q$, '75.0');
select pg_temp.val('maths pass rate 50, listed first', $q$select (j->'results'->'by_subject'->0->>'subject') || ' ' || (j->'results'->'by_subject'->0->>'pass_rate') from d$q$, 'Mathematics 50.0');
select pg_temp.val('SS1A results average 57.5', $q$select x->>'average' from d, jsonb_array_elements(j->'results'->'by_class') x where x->>'class'='SS1A'$q$, '57.5');
select pg_temp.val('attendance 71.4', $q$select j->'attendance'->>'rate' from d$q$, '71.4');
select pg_temp.val('one student below 90%', $q$select j->'attendance'->>'below_90' from d$q$, '1');
select pg_temp.val('fees', $q$select (j->'fees'->0->>'billed') || '/' || (j->'fees'->0->>'paid') || '/' || (j->'fees'->0->>'outstanding') || '/' || (j->'fees'->0->>'overdue') || '/' || (j->'fees'->0->>'collected_in_period') from d$q$, '100.00/30.00/70.00/70.00/30.00');
select pg_temp.val('behaviour 1 merit 3 concerns', $q$select (j->'behaviour'->>'merits') || '/' || (j->'behaviour'->>'concerns') || '/' || (j->'behaviour'->>'students_3plus') from d$q$, '1/3/1');
select pg_temp.val('top concern Homework x2', $q$select (j->'behaviour'->'top_concerns'->0->>'category') || ' ' || (j->'behaviour'->'top_concerns'->0->>'n') from d$q$, 'Homework 2');
select pg_temp.val('teacher workload', $q$select (x->>'classes') || '/' || (x->>'students') || '/' || (x->>'periods') || '/' || (x->>'hours') from d, jsonb_array_elements(j->'teachers') x where x->>'name'='Tola Teach'$q$, '2/3/2/1.7');
select pg_temp.as_user(pg_temp.u(3));
delete from d; insert into d select public.school_dashboard();
select pg_temp.val('school B sees its own empty numbers', $q$select j->'enrolment'->>'current' from d$q$, '0');
reset role;
select pg_temp.as_user('');
select (select count(*) filter (where pass) from res) || ' / ' || count(*) || ' passed' as summary from res;
select name as failed from res where not pass;
