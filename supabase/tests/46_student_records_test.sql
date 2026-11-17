-- Behaviour tests for 0046 (student records). Needs stubs + all migrations.
\set ON_ERROR_STOP off
truncate public.schools, auth.users cascade;
create or replace function pg_temp.u(n int) returns text language sql immutable as $$ select '46000000-0000-0000-0000-0000000000' || lpad(n::text, 2, '0') $$;
insert into auth.users(id) select pg_temp.u(g)::uuid from generate_series(1,12) g;
insert into public.schools(id,name,country_code,school_code,admission_prefix) values
 ('c4600000-0000-0000-0000-00000000000a','School A','NG','AAA-4646','GRF'),('c4600000-0000-0000-0000-00000000000b','School B','NG','BBB-4646',null);
insert into public.classes(id,school_id,name,grade) values
 ('d4600000-0000-0000-0000-0000000000a1','c4600000-0000-0000-0000-00000000000a','A1','SS1'),
 ('d4600000-0000-0000-0000-0000000000a2','c4600000-0000-0000-0000-00000000000a','A2','SS2'),
 ('d4600000-0000-0000-0000-0000000000b1','c4600000-0000-0000-0000-00000000000b','B1','SS1');
-- 1 admin A, 2 teacher A (teaches A1), 3 admin B, 4,5,6 students A1, 7 student B
insert into public.profiles(id,role,school_id,class_id,country_code,first_name,surname) values
 (pg_temp.u(1)::uuid,'school_admin','c4600000-0000-0000-0000-00000000000a',null,'NG','Ada','Admin'),
 (pg_temp.u(2)::uuid,'teacher','c4600000-0000-0000-0000-00000000000a',null,'NG','Tola','Teacher'),
 (pg_temp.u(3)::uuid,'school_admin','c4600000-0000-0000-0000-00000000000b',null,'NG','Bimpe','AdminB'),
 (pg_temp.u(4)::uuid,'student','c4600000-0000-0000-0000-00000000000a','d4600000-0000-0000-0000-0000000000a1','NG','Sam','One'),
 (pg_temp.u(5)::uuid,'student','c4600000-0000-0000-0000-00000000000a','d4600000-0000-0000-0000-0000000000a1','NG','Sue','Two'),
 (pg_temp.u(6)::uuid,'student','c4600000-0000-0000-0000-00000000000a','d4600000-0000-0000-0000-0000000000a1','NG','Seun','Three'),
 (pg_temp.u(7)::uuid,'student','c4600000-0000-0000-0000-00000000000b','d4600000-0000-0000-0000-0000000000b1','NG','Bola','Four');
insert into public.teacher_subjects values (pg_temp.u(2)::uuid,'d4600000-0000-0000-0000-0000000000a1','Mathematics');

create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin perform set_config('request.jwt.claim.sub', u, false); end $$;
create temp table res(name text, pass boolean); grant all on res to public;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true; begin begin execute sqltext; exception when others then ok := false; end; insert into res values (n, ok = expect_ok); end $$;
create or replace function pg_temp.cnt(n text, sqltext text, expected int) returns void language plpgsql as $$
declare c int; begin begin execute 'select count(*) from (' || sqltext || ') q' into c; exception when others then c := -1; end; insert into res values (n || ' (got ' || c || ')', c = expected); end $$;
create or replace function pg_temp.val(n text, sqltext text, expected text) returns void language plpgsql as $$
declare v text; begin begin execute sqltext into v; exception when others then v := 'ERROR:' || sqlerrm; end; insert into res values (n || ' (got ' || coalesce(v,'null') || ')', v is not distinct from expected); end $$;

select pg_temp.val('first student numbered', $q$select admission_no from public.profiles where id='46000000-0000-0000-0000-000000000004'$q$, 'GRF-' || to_char(now(),'YYYY') || '-0001');
select pg_temp.val('third student numbered', $q$select admission_no from public.profiles where id='46000000-0000-0000-0000-000000000006'$q$, 'GRF-' || to_char(now(),'YYYY') || '-0003');
select pg_temp.val('staff get no number', $q$select coalesce(admission_no,'none') from public.profiles where id='46000000-0000-0000-0000-000000000001'$q$, 'none');
select pg_temp.val('school without prefix gives none', $q$select coalesce(admission_no,'none') from public.profiles where id='46000000-0000-0000-0000-000000000007'$q$, 'none');
select pg_temp.val('school A seats count 3', $q$select public.school_students('c4600000-0000-0000-0000-00000000000a')::text$q$, '3');

set role authenticated;
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('admin A edits a record', $q$insert into public.student_records(student_id,school_id,date_of_birth,address) values ('46000000-0000-0000-0000-000000000004','c4600000-0000-0000-0000-00000000000a','2010-05-01','12 Allen Ave')$q$, true);
select pg_temp.check('admin A cannot file a record for school B student', $q$insert into public.student_records(student_id,school_id) values ('46000000-0000-0000-0000-000000000007','c4600000-0000-0000-0000-00000000000a')$q$, false);
select pg_temp.check('admin A cannot change student number column directly', $q$update public.profiles set admission_no='X' where id='46000000-0000-0000-0000-000000000004'$q$, false);
select pg_temp.val('admin A sets a custom number', $q$select public.set_admission_no('46000000-0000-0000-0000-000000000005','grf/old/77')$q$, 'GRF/OLD/77');
select pg_temp.check('duplicate number rejected', $q$select public.set_admission_no('46000000-0000-0000-0000-000000000006','GRF/OLD/77')$q$, false);
select pg_temp.check('admin A cannot touch school B student', $q$select public.set_enrolment_status('46000000-0000-0000-0000-000000000007','suspended')$q$, false);
select pg_temp.val('suspend keeps class', $q$select public.set_enrolment_status('46000000-0000-0000-0000-000000000004','suspended','Fees')$q$, 'suspended');
select pg_temp.val('still in class', $q$select class_id::text from public.profiles where id='46000000-0000-0000-0000-000000000004'$q$, 'd4600000-0000-0000-0000-0000000000a1');
select pg_temp.check('same status twice rejected', $q$select public.set_enrolment_status('46000000-0000-0000-0000-000000000004','suspended')$q$, false);
select pg_temp.val('graduate', $q$select public.set_enrolment_status('46000000-0000-0000-0000-000000000006','graduated','Finished SS3','2026-07-20')$q$, 'graduated');
select pg_temp.val('graduate leaves class', $q$select coalesce(class_id::text,'none') from public.profiles where id='46000000-0000-0000-0000-000000000006'$q$, 'none');
select pg_temp.val('left_on recorded', $q$select left_on::text from public.student_records where student_id='46000000-0000-0000-0000-000000000006'$q$, '2026-07-20');
select pg_temp.cnt('admin A sees 2 events', 'select * from public.enrolment_events', 2);
select pg_temp.check('events cannot be written directly', $q$insert into public.enrolment_events(student_id,school_id,to_status) values ('46000000-0000-0000-0000-000000000004','c4600000-0000-0000-0000-00000000000a','active')$q$, false);
select pg_temp.val('move two students', $q$select public.move_students(array['46000000-0000-0000-0000-000000000004','46000000-0000-0000-0000-000000000005','46000000-0000-0000-0000-000000000006']::uuid[],'d4600000-0000-0000-0000-0000000000a2')::text$q$, '2');
select pg_temp.check('cannot move into school B class', $q$select public.move_students(array['46000000-0000-0000-0000-000000000004']::uuid[],'d4600000-0000-0000-0000-0000000000b1')$q$, false);
select pg_temp.val('…and nobody moved', $q$select class_id::text from public.profiles where id='46000000-0000-0000-0000-000000000004'$q$, 'd4600000-0000-0000-0000-0000000000a2');
select pg_temp.val('reactivate', $q$select public.set_enrolment_status('46000000-0000-0000-0000-000000000006','active','Repeating SS3')$q$, 'active');
select pg_temp.val('left_on cleared', $q$select coalesce(left_on::text,'none') from public.student_records where student_id='46000000-0000-0000-0000-000000000006'$q$, 'none');

select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('teacher cannot change status', $q$select public.set_enrolment_status('46000000-0000-0000-0000-000000000005','withdrawn')$q$, false);
select pg_temp.cnt('teacher sees no events', 'select * from public.enrolment_events', 0);
select pg_temp.check('teacher cannot edit records', $q$update public.student_records set notes='x'$q$, true);

select pg_temp.as_user(pg_temp.u(3));
select pg_temp.check('admin B cannot number school A', $q$select public.number_students('c4600000-0000-0000-0000-00000000000a')$q$, false);
select pg_temp.check('admin B needs a prefix first', $q$select public.number_students('c4600000-0000-0000-0000-00000000000b')$q$, false);
select pg_temp.check('admin B sets a prefix', $q$update public.schools set admission_prefix='BBS', admission_year=false, admission_seq=99 where id='c4600000-0000-0000-0000-00000000000b'$q$, true);
select pg_temp.val('admin B numbers existing students', $q$select public.number_students('c4600000-0000-0000-0000-00000000000b')::text$q$, '1');
select pg_temp.val('number continues from 100 without year', $q$select admission_no from public.profiles where id='46000000-0000-0000-0000-000000000007'$q$, 'BBS-0100');
reset role;
select pg_temp.as_user('');
select pg_temp.val('teacher edit changed nothing', $q$select coalesce(notes,'none') from public.student_records where student_id='46000000-0000-0000-0000-000000000004'$q$, 'none');

select pg_temp.val('withdrawn student frees a seat', $q$select public.school_students('c4600000-0000-0000-0000-00000000000a')::text$q$, '3');
update public.profiles set enrolment_status='withdrawn' where id='46000000-0000-0000-0000-000000000005';
select pg_temp.val('…now 2 seats', $q$select public.school_students('c4600000-0000-0000-0000-00000000000a')::text$q$, '2');
update public.profiles set school_id='c4600000-0000-0000-0000-00000000000b', class_id=null where id='46000000-0000-0000-0000-000000000004';
select pg_temp.val('transfer to another school renumbers', $q$select admission_no from public.profiles where id='46000000-0000-0000-0000-000000000004'$q$, 'BBS-0101');

select (select count(*) filter (where pass) from res) || ' / ' || count(*) || ' passed' as summary from res;
select name as failed from res where not pass;
