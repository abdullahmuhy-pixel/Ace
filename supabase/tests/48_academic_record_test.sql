-- Behaviour tests for 0048 (academic record and transcripts). Needs stubs + all migrations.
\set ON_ERROR_STOP off
truncate public.schools, auth.users cascade;
create or replace function pg_temp.u(n int) returns text language sql immutable as $$ select '48000000-0000-0000-0000-0000000000' || lpad(n::text, 2, '0') $$;
insert into auth.users(id) select pg_temp.u(g)::uuid from generate_series(1,9) g;
insert into public.schools(id,name,country_code,school_code) values
 ('c4800000-0000-0000-0000-00000000000a','School A','NG','AAA-4848'),('c4800000-0000-0000-0000-00000000000b','School B','NG','BBB-4848');
insert into public.classes(id,school_id,name,grade) values ('d4800000-0000-0000-0000-0000000000a1','c4800000-0000-0000-0000-00000000000a','SS1A','SS1');
insert into public.profiles(id,role,school_id,class_id,country_code,first_name,surname) values
 (pg_temp.u(1)::uuid,'school_admin','c4800000-0000-0000-0000-00000000000a',null,'NG','Ada','Admin'),
 (pg_temp.u(2)::uuid,'teacher','c4800000-0000-0000-0000-00000000000a',null,'NG','Tola','Teacher'),
 (pg_temp.u(3)::uuid,'school_admin','c4800000-0000-0000-0000-00000000000b',null,'NG','Bimpe','AdminB'),
 (pg_temp.u(4)::uuid,'student','c4800000-0000-0000-0000-00000000000a','d4800000-0000-0000-0000-0000000000a1','NG','Sam','One'),
 (pg_temp.u(5)::uuid,'student','c4800000-0000-0000-0000-00000000000a','d4800000-0000-0000-0000-0000000000a1','NG','Sue','Two'),
 (pg_temp.u(6)::uuid,'student','c4800000-0000-0000-0000-00000000000a','d4800000-0000-0000-0000-0000000000a1','NG','Seun','Three');
insert into public.teacher_subjects values (pg_temp.u(2)::uuid,'d4800000-0000-0000-0000-0000000000a1','Mathematics');
insert into public.academic_terms(id,school_id,name,starts_on,ends_on) values ('e4800000-0000-0000-0000-000000000001','c4800000-0000-0000-0000-00000000000a','Term 1 2026/27','2026-09-01','2026-12-15');
insert into public.assessments(id,class_id,subject,title,max_mark,weight,held_on) values
 ('f4800000-0000-0000-0000-000000000001','d4800000-0000-0000-0000-0000000000a1','Mathematics','Test',50,40,'2026-10-01'),
 ('f4800000-0000-0000-0000-000000000002','d4800000-0000-0000-0000-0000000000a1','Mathematics','Exam',100,60,'2026-12-01'),
 ('f4800000-0000-0000-0000-000000000003','d4800000-0000-0000-0000-0000000000a1','Mathematics','Quiz',10,0,'2026-10-05'),
 ('f4800000-0000-0000-0000-000000000004','d4800000-0000-0000-0000-0000000000a1','Mathematics','Old test',10,50,'2026-05-01'),
 ('f4800000-0000-0000-0000-000000000005','d4800000-0000-0000-0000-0000000000a1','English','Essay',20,0,'2026-10-10'),
 ('f4800000-0000-0000-0000-000000000006','d4800000-0000-0000-0000-0000000000a1','English','Comprehension',20,0,'2026-11-10');
insert into public.marks(assessment_id,student_id,mark) values
 ('f4800000-0000-0000-0000-000000000001',pg_temp.u(4)::uuid,40),('f4800000-0000-0000-0000-000000000002',pg_temp.u(4)::uuid,70),('f4800000-0000-0000-0000-000000000003',pg_temp.u(4)::uuid,0),('f4800000-0000-0000-0000-000000000004',pg_temp.u(4)::uuid,0),
 ('f4800000-0000-0000-0000-000000000005',pg_temp.u(4)::uuid,15),('f4800000-0000-0000-0000-000000000006',pg_temp.u(4)::uuid,10),
 ('f4800000-0000-0000-0000-000000000001',pg_temp.u(5)::uuid,50),('f4800000-0000-0000-0000-000000000002',pg_temp.u(5)::uuid,90),
 ('f4800000-0000-0000-0000-000000000005',pg_temp.u(5)::uuid,20),('f4800000-0000-0000-0000-000000000006',pg_temp.u(5)::uuid,20),
 ('f4800000-0000-0000-0000-000000000001',pg_temp.u(6)::uuid,25);
insert into public.attendance(class_id,student_id,day,status) values
 ('d4800000-0000-0000-0000-0000000000a1',pg_temp.u(4)::uuid,'2026-09-02','present'),('d4800000-0000-0000-0000-0000000000a1',pg_temp.u(4)::uuid,'2026-09-03','late'),
 ('d4800000-0000-0000-0000-0000000000a1',pg_temp.u(4)::uuid,'2026-09-04','absent'),('d4800000-0000-0000-0000-0000000000a1',pg_temp.u(4)::uuid,'2026-09-05','excused');

create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin perform set_config('request.jwt.claim.sub', u, false); end $$;
create temp table res(name text, pass boolean); grant all on res to public;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true; begin begin execute sqltext; exception when others then ok := false; end; insert into res values (n, ok = expect_ok); end $$;
create or replace function pg_temp.cnt(n text, sqltext text, expected int) returns void language plpgsql as $$
declare c int; begin begin execute 'select count(*) from (' || sqltext || ') q' into c; exception when others then c := -1; end; insert into res values (n || ' (got ' || c || ')', c = expected); end $$;
create or replace function pg_temp.val(n text, sqltext text, expected text) returns void language plpgsql as $$
declare v text; begin begin execute sqltext into v; exception when others then v := 'ERROR:' || sqlerrm; end; insert into res values (n || ' (got ' || coalesce(v,'null') || ')', v is not distinct from expected); end $$;
create temp table keep(k text, v text); grant all on keep to public;
\set T '''e4800000-0000-0000-0000-000000000001'''
\set C '''d4800000-0000-0000-0000-0000000000a1'''

set role authenticated;
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('teacher cannot compile', $q$select public.compile_term('e4800000-0000-0000-0000-000000000001','d4800000-0000-0000-0000-0000000000a1')$q$, false);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.check('admin B cannot compile', $q$select public.compile_term('e4800000-0000-0000-0000-000000000001','d4800000-0000-0000-0000-0000000000a1')$q$, false);
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.val('compile 3 students', $q$select public.compile_term('e4800000-0000-0000-0000-000000000001','d4800000-0000-0000-0000-0000000000a1')::text$q$, '3');
select pg_temp.val('Sam maths = (0.8x40 + 0.7x60) = 74', $q$select score::text from public.term_results where student_id='48000000-0000-0000-0000-000000000004' and subject='Mathematics'$q$, '74.00');
select pg_temp.val('Sam maths grade B', $q$select grade from public.term_results where student_id='48000000-0000-0000-0000-000000000004' and subject='Mathematics'$q$, 'B');
select pg_temp.val('Sam English, no weights = equal = 62.5', $q$select score::text from public.term_results where student_id='48000000-0000-0000-0000-000000000004' and subject='English'$q$, '62.50');
select pg_temp.val('Sam average 68.25', $q$select average::text from public.term_reports where student_id='48000000-0000-0000-0000-000000000004'$q$, '68.25');
select pg_temp.val('Sam attendance 2 of 3 = 66.67', $q$select attendance_pct::text from public.term_reports where student_id='48000000-0000-0000-0000-000000000004'$q$, '66.67');
select pg_temp.val('Sue first (94 and 100)', $q$select position || '/' || class_size || ' ' || average from public.term_reports where student_id='48000000-0000-0000-0000-000000000005'$q$, '1/3 97.00');
select pg_temp.val('Seun only the test counts = 50', $q$select score::text from public.term_results where student_id='48000000-0000-0000-0000-000000000006' and subject='Mathematics'$q$, '50.00');
select pg_temp.val('Seun third', $q$select position::text from public.term_reports where student_id='48000000-0000-0000-0000-000000000006'$q$, '3');
select pg_temp.check('admin adds a manual result', $q$insert into public.term_results(school_id,term_id,student_id,subject,score,source) values ('c4800000-0000-0000-0000-00000000000a','e4800000-0000-0000-0000-000000000001','48000000-0000-0000-0000-000000000006','English',55,'manual')$q$, true);
select pg_temp.val('manual 55 graded D', $q$select grade from public.term_results where student_id='48000000-0000-0000-0000-000000000006' and subject='English'$q$, 'D');
select pg_temp.val('recompile', $q$select public.compile_term('e4800000-0000-0000-0000-000000000001','d4800000-0000-0000-0000-0000000000a1')::text$q$, '3');
select pg_temp.val('manual kept, average 52.5', $q$select average::text from public.term_reports where student_id='48000000-0000-0000-0000-000000000006'$q$, '52.50');
select pg_temp.check('school grade bands', $q$update public.schools set grade_bands='[{"grade":"A1","min":75},{"grade":"C4","min":60},{"grade":"F9","min":0}]' where id='c4800000-0000-0000-0000-00000000000a'$q$, true);
select pg_temp.val('recompile with new bands', $q$select public.compile_term('e4800000-0000-0000-0000-000000000001','d4800000-0000-0000-0000-0000000000a1')::text$q$, '3');
select pg_temp.val('…74 is now C4', $q$select grade from public.term_results where student_id='48000000-0000-0000-0000-000000000004' and subject='Mathematics'$q$, 'C4');
select pg_temp.check('comment on report', $q$update public.term_reports set teacher_comment='Good term' where student_id='48000000-0000-0000-0000-000000000004'$q$, true);

select pg_temp.as_user(pg_temp.u(4));
select pg_temp.cnt('student sees nothing before publishing', 'select * from public.term_results', 0);
select pg_temp.check('student cannot request before publishing', $q$select public.request_transcript('University')$q$, false);
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.val('publish 3', $q$select public.publish_term('e4800000-0000-0000-0000-000000000001','d4800000-0000-0000-0000-0000000000a1',true)::text$q$, '3');
select pg_temp.check('published results frozen', $q$update public.term_results set score=99 where student_id='48000000-0000-0000-0000-000000000004'$q$, false);
select pg_temp.check('published report frozen', $q$update public.term_reports set teacher_comment='x' where student_id='48000000-0000-0000-0000-000000000004'$q$, false);
select pg_temp.val('recompile skips published', $q$select public.compile_term('e4800000-0000-0000-0000-000000000001','d4800000-0000-0000-0000-0000000000a1')::text$q$, '0');
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.cnt('student sees own 2 results', 'select * from public.term_results', 2);
select pg_temp.cnt('student sees own report only', 'select * from public.term_reports', 1);
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.cnt('teacher reads class reports', 'select * from public.term_reports', 3);
select pg_temp.check('teacher cannot edit results', $q$insert into public.term_results(school_id,term_id,student_id,subject,score) values ('c4800000-0000-0000-0000-00000000000a','e4800000-0000-0000-0000-000000000001','48000000-0000-0000-0000-000000000005','Art',1)$q$, false);
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.check('student requests transcript', $q$select public.request_transcript('University application')$q$, true);
select pg_temp.check('second request waits', $q$select public.request_transcript('again')$q$, false);
select pg_temp.check('student cannot issue', $q$select public.issue_transcript('48000000-0000-0000-0000-000000000004')$q$, false);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.check('admin B cannot issue', $q$select public.issue_transcript('48000000-0000-0000-0000-000000000004')$q$, false);
select pg_temp.cnt('admin B sees no request', 'select * from public.transcripts', 0);
select pg_temp.as_user(pg_temp.u(1));
insert into keep select 'code', (public.issue_transcript('48000000-0000-0000-0000-000000000004')).code;
select pg_temp.cnt('request answered, not duplicated', $q$select * from public.transcripts where status='issued'$q$, 1);
select pg_temp.val('purpose kept', $q$select purpose from public.transcripts where status='issued'$q$, 'University application');
select pg_temp.check('admin issues one directly without a request', $q$select public.issue_transcript('48000000-0000-0000-0000-000000000005')$q$, true);
reset role;
select pg_temp.as_user('');
set role anon;
select pg_temp.val('anyone can verify', $q$select (snapshot->>'name') || ' ' || school || ' ' || (snapshot->'terms'->0->>'average') || ' ' || (snapshot->'terms'->0->'results'->0->>'subject') from public.verify_transcript((select v from keep where k='code'))$q$, 'Sam One School A 68.25 English');
select pg_temp.cnt('bad code finds nothing', $q$select * from public.verify_transcript('TRAAAAAAAAAA')$q$, 0);
select pg_temp.check('anon cannot read transcripts', 'select * from public.transcripts', false);
reset role;
set role authenticated;
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('revoke', $q$select public.decide_transcript((select id from public.transcripts where code=(select v from keep where k='code')),'revoke')$q$, true);
reset role;
set role anon;
select pg_temp.val('revoked shows no results', $q$select revoked::text || coalesce(snapshot::text,'-') from public.verify_transcript((select v from keep where k='code'))$q$, 'true-');
reset role;
select pg_temp.as_user('');
select (select count(*) filter (where pass) from res) || ' / ' || count(*) || ' passed' as summary from res;
select name as failed from res where not pass;
