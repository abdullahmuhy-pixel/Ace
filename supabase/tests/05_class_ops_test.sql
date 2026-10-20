-- Behaviour tests for 0005. Run on a database that has the stubs and migrations 0001-0005 applied.
\set ON_ERROR_STOP off
truncate public.schools, auth.users, public.promo_codes cascade;
insert into auth.users(id) values
 ('a0000000-0000-0000-0000-000000000001'),('a0000000-0000-0000-0000-000000000002'),('a0000000-0000-0000-0000-000000000003'),
 ('a0000000-0000-0000-0000-000000000004'),('a0000000-0000-0000-0000-000000000005'),('b0000000-0000-0000-0000-000000000001'),('b0000000-0000-0000-0000-000000000002');
insert into public.schools(id,name,country_code,school_code) values
 ('c0000000-0000-0000-0000-00000000000a','School A','NG','AAA-1111'),('c0000000-0000-0000-0000-00000000000b','School B','GH','BBB-2222');
insert into public.classes(id,school_id,name,grade) values
 ('d0000000-0000-0000-0000-0000000000a1','c0000000-0000-0000-0000-00000000000a','A1','SS3'),
 ('d0000000-0000-0000-0000-0000000000a2','c0000000-0000-0000-0000-00000000000a','A2','SS3'),
 ('d0000000-0000-0000-0000-0000000000b1','c0000000-0000-0000-0000-00000000000b','B1','SHS3');
insert into public.profiles(id,role,school_id,class_id,country_code,first_name,surname) values
 ('a0000000-0000-0000-0000-000000000001','school_admin','c0000000-0000-0000-0000-00000000000a',null,'NG','Ada','Admin'),
 ('a0000000-0000-0000-0000-000000000002','teacher','c0000000-0000-0000-0000-00000000000a','d0000000-0000-0000-0000-0000000000a1','NG','Tola','Teacher'),
 ('a0000000-0000-0000-0000-000000000003','student','c0000000-0000-0000-0000-00000000000a','d0000000-0000-0000-0000-0000000000a1','NG','Sam','One'),
 ('a0000000-0000-0000-0000-000000000004','student','c0000000-0000-0000-0000-00000000000a','d0000000-0000-0000-0000-0000000000a2','NG','Sue','Two'),
 ('a0000000-0000-0000-0000-000000000005','student','c0000000-0000-0000-0000-00000000000a','d0000000-0000-0000-0000-0000000000a1','NG','Seun','Three'),
 ('b0000000-0000-0000-0000-000000000001','teacher','c0000000-0000-0000-0000-00000000000b','d0000000-0000-0000-0000-0000000000b1','GH','Kofi','TeacherB'),
 ('b0000000-0000-0000-0000-000000000002','student','c0000000-0000-0000-0000-00000000000b','d0000000-0000-0000-0000-0000000000b1','GH','Ama','StudentB');
insert into public.teacher_subjects values ('a0000000-0000-0000-0000-000000000002','d0000000-0000-0000-0000-0000000000a1','Mathematics'),
 ('b0000000-0000-0000-0000-000000000001','d0000000-0000-0000-0000-0000000000b1','Mathematics');

create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin
  perform set_config('request.jwt.claim.sub', u, false); end $$;

create temp table res(name text, pass boolean);
grant all on res to public;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true;
begin
  begin execute sqltext; exception when others then ok := false; end;
  insert into res values (n, ok = expect_ok);
end $$;
create or replace function pg_temp.cnt(n text, sqltext text, expected int) returns void language plpgsql as $$
declare c int;
begin execute 'select count(*) from (' || sqltext || ') q' into c; insert into res values (n || ' (got ' || c || ')', c = expected); end $$;

-- teacher A1: sets up an assessment and a mark
set role authenticated;
select pg_temp.as_user('a0000000-0000-0000-0000-000000000002');
select pg_temp.check('teacher creates assessment', $q$insert into assessments(id,class_id,subject,title,max_mark,weight) values ('e0000000-0000-0000-0000-000000000001','d0000000-0000-0000-0000-0000000000a1','Mathematics','Test 1',50,40)$q$, true);
select pg_temp.check('teacher cannot create assessment in another class', $q$insert into assessments(class_id,subject,title,max_mark) values ('d0000000-0000-0000-0000-0000000000a2','Mathematics','x',10)$q$, false);
select pg_temp.check('teacher cannot create assessment in other school', $q$insert into assessments(class_id,subject,title,max_mark) values ('d0000000-0000-0000-0000-0000000000b1','Mathematics','x',10)$q$, false);
select pg_temp.check('mark within max', $q$insert into marks values ('e0000000-0000-0000-0000-000000000001','a0000000-0000-0000-0000-000000000003',40,null)$q$, true);
select pg_temp.check('mark above max rejected', $q$insert into marks(assessment_id,student_id,mark) values ('e0000000-0000-0000-0000-000000000001','a0000000-0000-0000-0000-000000000005',51)$q$, false);
select pg_temp.check('mark for student from another class rejected', $q$insert into marks(assessment_id,student_id,mark) values ('e0000000-0000-0000-0000-000000000001','a0000000-0000-0000-0000-000000000004',10)$q$, false);
select pg_temp.check('attendance for own class', $q$insert into attendance values ('d0000000-0000-0000-0000-0000000000a1','a0000000-0000-0000-0000-000000000003','2026-10-01','present',null)$q$, true);
select pg_temp.check('attendance for other class rejected', $q$insert into attendance values ('d0000000-0000-0000-0000-0000000000a2','a0000000-0000-0000-0000-000000000004','2026-10-01','present',null)$q$, false);
select pg_temp.check('teacher posts class announcement', $q$insert into announcements(school_id,class_id,title,body) values ('c0000000-0000-0000-0000-00000000000a','d0000000-0000-0000-0000-0000000000a1','Mock Friday','Bring a calculator')$q$, true);
select pg_temp.check('teacher cannot post school-wide announcement', $q$insert into announcements(school_id,class_id,title,body) values ('c0000000-0000-0000-0000-00000000000a',null,'All','x')$q$, false);
select pg_temp.check('teacher sets a task', $q$insert into tasks(id,class_id,subject,title) values ('f0000000-0000-0000-0000-000000000001','d0000000-0000-0000-0000-0000000000a1','Mathematics','Exercise 4')$q$, true);
select pg_temp.check('teacher messages own student', $q$insert into messages(school_id,sender_id,recipient_id,body) values ('c0000000-0000-0000-0000-00000000000a','a0000000-0000-0000-0000-000000000002','a0000000-0000-0000-0000-000000000003','Well done')$q$, true);
select pg_temp.check('teacher cannot message other school student', $q$insert into messages(school_id,sender_id,recipient_id,body) values ('c0000000-0000-0000-0000-00000000000a','a0000000-0000-0000-0000-000000000002','b0000000-0000-0000-0000-000000000002','hi')$q$, false);
select pg_temp.check('teacher cannot send as someone else', $q$insert into messages(school_id,sender_id,recipient_id,body) values ('c0000000-0000-0000-0000-00000000000a','a0000000-0000-0000-0000-000000000001','a0000000-0000-0000-0000-000000000003','spoof')$q$, false);
select pg_temp.check('teacher records guardian', $q$insert into guardians(student_id,email,name) values ('a0000000-0000-0000-0000-000000000003','parent@example.com','Mr One')$q$, true);
select pg_temp.check('teacher cannot see other school guardian insert', $q$insert into guardians(student_id,email) values ('b0000000-0000-0000-0000-000000000002','x@example.com')$q$, false);

-- student 3 (class A1)
select pg_temp.as_user('a0000000-0000-0000-0000-000000000003');
select pg_temp.cnt('student sees own class assessments', 'select 1 from assessments', 1);
select pg_temp.cnt('student sees only own marks', 'select 1 from marks', 1);
select pg_temp.cnt('student sees own attendance', 'select 1 from attendance', 1);
select pg_temp.cnt('student sees class announcement', 'select 1 from announcements', 1);
select pg_temp.cnt('student sees task', 'select 1 from tasks', 1);
select pg_temp.cnt('student sees message to them', 'select 1 from messages', 1);
select pg_temp.cnt('student cannot read guardians', 'select 1 from guardians', 0);
select pg_temp.check('student cannot edit mark', $q$update marks set mark=50$q$, true);   -- update allowed to run but must affect 0 rows
select pg_temp.cnt('student mark unchanged', 'select 1 from marks where mark = 40', 1);
select pg_temp.check('student cannot create assessment', $q$insert into assessments(class_id,subject,title,max_mark) values ('d0000000-0000-0000-0000-0000000000a1','Mathematics','x',10)$q$, false);
select pg_temp.check('student submits task', $q$insert into task_submissions(task_id,student_id,body,mark,feedback) values ('f0000000-0000-0000-0000-000000000001','a0000000-0000-0000-0000-000000000003','my answer',99,'self-graded')$q$, true);
select pg_temp.cnt('submission mark was stripped', 'select 1 from task_submissions where mark is null and feedback is null', 1);
select pg_temp.check('student cannot submit for another student', $q$insert into task_submissions(task_id,student_id,body) values ('f0000000-0000-0000-0000-000000000001','a0000000-0000-0000-0000-000000000005','x')$q$, false);
select pg_temp.check('student can message teacher', $q$insert into messages(school_id,sender_id,recipient_id,body) values ('c0000000-0000-0000-0000-00000000000a','a0000000-0000-0000-0000-000000000003','a0000000-0000-0000-0000-000000000002','Thanks')$q$, true);
select pg_temp.check('student cannot message student', $q$insert into messages(school_id,sender_id,recipient_id,body) values ('c0000000-0000-0000-0000-00000000000a','a0000000-0000-0000-0000-000000000003','a0000000-0000-0000-0000-000000000004','hi')$q$, false);
select pg_temp.check('student cannot read ai consume rpc', $q$select * from consume_ai('a0000000-0000-0000-0000-000000000003')$q$, false);
select pg_temp.check('student cannot write ai_usage', $q$insert into ai_usage(user_id,count) values ('a0000000-0000-0000-0000-000000000003',-5)$q$, false);
select pg_temp.check('student cannot create entitlement', $q$insert into entitlements(user_id,status) values ('a0000000-0000-0000-0000-000000000003','active')$q$, false);
select pg_temp.check('student cannot read payments', 'select * from payments', false);
select pg_temp.check('student reports content', $q$insert into content_reports(user_id,country_code,note) values ('a0000000-0000-0000-0000-000000000003','NG','Answer B looks wrong')$q$, true);
select pg_temp.check('student cannot change platform config', $q$update platform_config set trial_days=60$q$, true);
select pg_temp.cnt('platform config unchanged', 'select 1 from platform_config where trial_days = 7', 1);

-- student 4 (class A2) sees none of class A1
select pg_temp.as_user('a0000000-0000-0000-0000-000000000004');
select pg_temp.cnt('other class student sees no assessment', 'select 1 from assessments', 0);
select pg_temp.cnt('other class student sees no task', 'select 1 from tasks', 0);
select pg_temp.cnt('other class student sees no class announcement', 'select 1 from announcements', 0);
select pg_temp.cnt('other class student sees no messages', 'select 1 from messages', 0);

-- school B teacher sees nothing of school A
select pg_temp.as_user('b0000000-0000-0000-0000-000000000001');
select pg_temp.cnt('other school teacher sees no assessments', 'select 1 from assessments', 0);
select pg_temp.cnt('other school teacher sees no marks', 'select 1 from marks', 0);
select pg_temp.cnt('other school teacher sees no guardians', 'select 1 from guardians', 0);
select pg_temp.cnt('other school teacher sees no attendance', 'select 1 from attendance', 0);

-- teacher A1 marks the submission; SBA view
select pg_temp.as_user('a0000000-0000-0000-0000-000000000002');
select pg_temp.check('teacher marks submission', $q$update task_submissions set mark=8, feedback='Good' where task_id='f0000000-0000-0000-0000-000000000001'$q$, true);
select pg_temp.cnt('mark recorded with marker', 'select 1 from task_submissions where mark = 8 and marked_by is not null', 1);
select pg_temp.cnt('sba weighted pct is 80', 'select 1 from sba_summary where weighted_pct = 80.0', 1);

-- admin
select pg_temp.as_user('a0000000-0000-0000-0000-000000000001');
select pg_temp.check('admin posts school-wide announcement', $q$insert into announcements(school_id,class_id,title,body) values ('c0000000-0000-0000-0000-00000000000a',null,'Term dates','Closes 12 Dec')$q$, true);
select pg_temp.check('admin cannot post to other school', $q$insert into announcements(school_id,class_id,title,body) values ('c0000000-0000-0000-0000-00000000000b',null,'x','y')$q$, false);
select pg_temp.check('admin sets AI cap', $q$update schools set ai_mode='limited', ai_cap=2 where id='c0000000-0000-0000-0000-00000000000a'$q$, true);

-- server side: AI cap and promo
reset role;
create temp table ai as select * from consume_ai('a0000000-0000-0000-0000-000000000003') union all select * from consume_ai('a0000000-0000-0000-0000-000000000003') union all select * from consume_ai('a0000000-0000-0000-0000-000000000003');
insert into res select 'AI cap: 2 allowed then blocked (allowed=' || string_agg(allowed::text, ',') || ')', string_agg(allowed::text, ',') = 'true,true,false' from ai;
insert into promo_codes(code,kind,value,max_uses) values ('WELCOME7','trial_extension',7,1);
set role authenticated;
select pg_temp.as_user('a0000000-0000-0000-0000-000000000003');
select pg_temp.check('promo redeems', $q$select redeem_promo('welcome7')$q$, true);
select pg_temp.cnt('promo granted access', 'select 1 where has_access()', 1);
select pg_temp.cnt('second redeem refused', $q$select 1 where (redeem_promo('WELCOME7')->>'ok')::boolean$q$, 0);
select pg_temp.as_user('a0000000-0000-0000-0000-000000000005');
select pg_temp.cnt('promo with no uses left refused', $q$select 1 where (redeem_promo('WELCOME7')->>'ok')::boolean$q$, 0);
select pg_temp.check('student cannot read promo_codes', $q$select code from promo_codes$q$, true);
select pg_temp.cnt('promo_codes hidden from students', 'select 1 from promo_codes', 0);
reset role;

-- live quiz scoring: students never see the key
insert into live_sessions(id,class_id,host_id,code,state,questions) values ('11111111-0000-0000-0000-000000000001','d0000000-0000-0000-0000-0000000000a1','a0000000-0000-0000-0000-000000000002','ABC123','running','[{"q":"2+2","o":["3","4","5","6"]}]');
insert into live_keys values ('11111111-0000-0000-0000-000000000001','[1]');
set role authenticated;
select pg_temp.as_user('a0000000-0000-0000-0000-000000000003');
select pg_temp.cnt('student cannot read live key', 'select 1 from live_keys', 0);
select pg_temp.check('student answers live question', $q$insert into live_answers(session_id,student_id,q_index,choice) values ('11111111-0000-0000-0000-000000000001','a0000000-0000-0000-0000-000000000003',0,1)$q$, true);
select pg_temp.cnt('answer scored correct', 'select 1 from live_answers where correct', 1);
select pg_temp.check('student cannot answer twice', $q$insert into live_answers(session_id,student_id,q_index,choice) values ('11111111-0000-0000-0000-000000000001','a0000000-0000-0000-0000-000000000003',0,2)$q$, false);
select pg_temp.as_user('a0000000-0000-0000-0000-000000000004');
select pg_temp.check('other class cannot answer', $q$insert into live_answers(session_id,student_id,q_index,choice) values ('11111111-0000-0000-0000-000000000001','a0000000-0000-0000-0000-000000000004',0,1)$q$, false);
reset role;

select case when pass then 'PASS' else 'FAIL' end as result, name from res order by pass, name;
select count(*) filter (where pass) as passed, count(*) filter (where not pass) as failed from res;
