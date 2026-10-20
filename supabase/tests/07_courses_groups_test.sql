-- Behaviour tests for 0007. Needs stubs + migrations 0001-0007.
\set ON_ERROR_STOP off
truncate public.schools, auth.users, public.courses, public.plans cascade;
create or replace function pg_temp.u(n int) returns text language sql immutable as $$ select '77000000-0000-0000-0000-0000000000' || lpad(n::text, 2, '0') $$;
insert into auth.users(id) select pg_temp.u(g)::uuid from generate_series(1,16) g;
insert into public.schools(id,name,country_code,school_code) values
 ('c7000000-0000-0000-0000-00000000000a','School A','NG','AAA-7777'),('c7000000-0000-0000-0000-00000000000b','School B','NG','BBB-7777');
insert into public.classes(id,school_id,name,grade) values
 ('d7000000-0000-0000-0000-0000000000a1','c7000000-0000-0000-0000-00000000000a','A1','SS3'),
 ('d7000000-0000-0000-0000-0000000000a2','c7000000-0000-0000-0000-00000000000a','A2','SS3'),
 ('d7000000-0000-0000-0000-0000000000b1','c7000000-0000-0000-0000-00000000000b','B1','SS3');
-- 1 teacher A, 2..6 students A1 (2 is S1), 7 student A2, 8 teacher B, 9 student B, 10,11 university (same institution), 12 university (other), 13 platform admin, 14 school admin A
insert into public.profiles(id,role,school_id,class_id,country_code,first_name,surname) values
 (pg_temp.u(1)::uuid,'teacher','c7000000-0000-0000-0000-00000000000a','d7000000-0000-0000-0000-0000000000a1','NG','Tola','Teacher'),
 (pg_temp.u(2)::uuid,'student','c7000000-0000-0000-0000-00000000000a','d7000000-0000-0000-0000-0000000000a1','NG','Sam','One'),
 (pg_temp.u(3)::uuid,'student','c7000000-0000-0000-0000-00000000000a','d7000000-0000-0000-0000-0000000000a1','NG','Sue','Two'),
 (pg_temp.u(4)::uuid,'student','c7000000-0000-0000-0000-00000000000a','d7000000-0000-0000-0000-0000000000a1','NG','Seun','Three'),
 (pg_temp.u(5)::uuid,'student','c7000000-0000-0000-0000-00000000000a','d7000000-0000-0000-0000-0000000000a1','NG','Sade','Four'),
 (pg_temp.u(6)::uuid,'student','c7000000-0000-0000-0000-00000000000a','d7000000-0000-0000-0000-0000000000a1','NG','Soji','Five'),
 (pg_temp.u(7)::uuid,'student','c7000000-0000-0000-0000-00000000000a','d7000000-0000-0000-0000-0000000000a2','NG','Sola','Six'),
 (pg_temp.u(8)::uuid,'teacher','c7000000-0000-0000-0000-00000000000b','d7000000-0000-0000-0000-0000000000b1','NG','Kunle','TeacherB'),
 (pg_temp.u(9)::uuid,'student','c7000000-0000-0000-0000-00000000000b','d7000000-0000-0000-0000-0000000000b1','NG','Bola','Seven'),
 (pg_temp.u(10)::uuid,'student',null,null,'NG','Uche','Uni'),(pg_temp.u(11)::uuid,'student',null,null,'NG','Uzo','Uni'),(pg_temp.u(12)::uuid,'student',null,null,'NG','Ugo','Other'),
 (pg_temp.u(13)::uuid,'platform_admin',null,null,'NG','Pat','Admin'),
 (pg_temp.u(14)::uuid,'school_admin','c7000000-0000-0000-0000-00000000000a',null,'NG','Ada','Admin');
update public.profiles set level='university', institution='University of Lagos' where id = pg_temp.u(10)::uuid;
update public.profiles set level='university', institution='  university  of   lagos ' where id = pg_temp.u(11)::uuid;
update public.profiles set level='university', institution='University of Ibadan' where id = pg_temp.u(12)::uuid;
insert into public.teacher_subjects values (pg_temp.u(1)::uuid,'d7000000-0000-0000-0000-0000000000a1','Mathematics'),(pg_temp.u(8)::uuid,'d7000000-0000-0000-0000-0000000000b1','Mathematics');
-- a tiny course: 2 lessons, 4 questions, pass mark 75
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count) values ('test-course','Test Course','all',75,2,4);
insert into public.course_lessons values ('test-course','l1',0),('test-course','l2',1);
insert into public.course_keys values ('test-course','q1',0,'why1'),('test-course','q2',1,'why2'),('test-course','q3',2,'why3'),('test-course','q4',3,'why4');
insert into public.push_subscriptions(endpoint,user_id,p256dh,auth) values ('https://push.example/1', pg_temp.u(2)::uuid, 'k', 'a');

create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin perform set_config('request.jwt.claim.sub', u, false); end $$;
create temp table res(name text, pass boolean); grant all on res to public;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true; begin begin execute sqltext; exception when others then ok := false; end; insert into res values (n, ok = expect_ok); end $$;
create or replace function pg_temp.cnt(n text, sqltext text, expected int) returns void language plpgsql as $$
declare c int; begin begin execute 'select count(*) from (' || sqltext || ') q' into c; exception when others then c := -1; end; insert into res values (n || ' (got ' || c || ')', c = expected); end $$;
create or replace function pg_temp.val(n text, sqltext text, expected text) returns void language plpgsql as $$
declare v text; begin begin execute sqltext into v; exception when others then v := 'ERROR:' || sqlerrm; end; insert into res values (n || ' (got ' || coalesce(v,'null') || ')', v is not distinct from expected); end $$;
create temp table kv(k text, v text); grant all on kv to public;
set role authenticated;

-- ===== courses =====
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('quiz blocked before lessons', $q$select public.submit_course_quiz('test-course','{"q1":0}')$q$, false);
select pg_temp.check('unknown lesson rejected', $q$select public.mark_lesson('test-course','nope')$q$, false);
select pg_temp.check('mark lesson 1', $q$select public.mark_lesson('test-course','l1')$q$, true);
select pg_temp.check('mark lesson 1 again (idempotent)', $q$select public.mark_lesson('test-course','l1')$q$, true);
select pg_temp.val('lessons_done has 1', $q$select cardinality(lessons_done)::text from public.course_progress where course='test-course'$q$, '1');
select pg_temp.check('quiz still blocked with 1 of 2 lessons', $q$select public.submit_course_quiz('test-course','{}')$q$, false);
select pg_temp.check('mark lesson 2', $q$select public.mark_lesson('test-course','l2')$q$, true);
select pg_temp.cnt('answer keys are unreadable', $q$select * from public.course_keys$q$, -1);
select pg_temp.check('cannot write progress directly', $q$insert into public.course_progress(user_id,course,lessons_done) values (auth.uid(),'test-course','{l1,l2}')$q$, false);
select pg_temp.check('cannot write certificates directly', $q$insert into public.certificates(code,user_id,course,score,holder_name) values ('FAKE00000001',auth.uid(),'test-course',100,'X')$q$, false);
select pg_temp.val('2 of 4 right = 50, not passed', $q$select (public.submit_course_quiz('test-course','{"q1":0,"q2":1,"q3":0,"q4":0}')->>'score')||'/'||(public.submit_course_quiz('test-course','{"q1":0,"q2":1,"q3":0,"q4":0}')->>'passed')$q$, '50/false');
select pg_temp.cnt('no certificate after failing', $q$select * from public.certificates$q$, 0);
select pg_temp.val('missing answers count wrong', $q$select public.submit_course_quiz('test-course','{"q1":0}')->>'correct'$q$, '1');
select pg_temp.val('review gives why for wrong answers only', $q$select (select count(*) from jsonb_array_elements(public.submit_course_quiz('test-course','{"q1":0,"q2":1,"q3":2,"q4":0}')->'review') e where e ? 'why')::text$q$, '1');
select pg_temp.check('5th attempt allowed', $q$select public.submit_course_quiz('test-course','{"q1":0,"q2":1,"q3":0,"q4":0}')$q$, true);
select pg_temp.check('5 attempts per day: this is the 6th', $q$select public.submit_course_quiz('test-course','{"q1":0,"q2":1,"q3":2,"q4":3}')$q$, false);
reset role; delete from public.course_attempts; set role authenticated; select pg_temp.as_user(pg_temp.u(2));
select pg_temp.val('3 of 4 = 75 passes', $q$select (public.submit_course_quiz('test-course','{"q1":0,"q2":1,"q3":2,"q4":0}')->>'passed')$q$, 'true');
select pg_temp.cnt('own certificate visible', $q$select * from public.certificates$q$, 1);
insert into kv select 'code', code from public.certificates;
select pg_temp.val('second pass returns the same code', $q$select (public.submit_course_quiz('test-course','{"q1":0,"q2":1,"q3":2,"q4":3}')->>'code') = (select v from kv where k='code')$q$, 'true');
select pg_temp.cnt('still one certificate', $q$select * from public.certificates$q$, 1);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.cnt('others cannot see my certificate', $q$select * from public.certificates$q$, 0);
reset role; set role anon;
select pg_temp.val('anyone can verify by code (any case/dashes)', $q$select holder_name||'|'||course_title||'|'||score from public.verify_certificate(lower(substr((select v from kv where k='code'),1,4)||'-'||substr((select v from kv where k='code'),5)))$q$, 'Sam One|Test Course|75');
select pg_temp.cnt('unknown code verifies nothing', $q$select * from public.verify_certificate('ZZZZZZZZZZZZ')$q$, 0);
select pg_temp.check('anon cannot read certificates (no grant after 0011)', $q$select * from public.certificates$q$, false);
select pg_temp.cnt('anon can see the course catalogue', $q$select * from public.courses$q$, 1);
reset role; set role authenticated;

-- ===== study groups =====
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('student makes a class group', $q$insert into kv select 'g1', public.create_group('Maths revision','Past questions','class')$q$, true);
select pg_temp.check('links in names refused', $q$select public.create_group('visit www.spam.com','x','class')$q$, false);
select pg_temp.check('student makes a school group', $q$insert into kv select 'g2', public.create_group('SS3 all','Whole year','school')$q$, true);
select pg_temp.check('student cannot make an institution group', $q$select public.create_group('Uni group','x','institution')$q$, false);
select pg_temp.check('third group', $q$select public.create_group('Third','x','class')$q$, true);
select pg_temp.check('fourth group refused (limit 3)', $q$select public.create_group('Fourth','x','class')$q$, false);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.cnt('classmate discovers 3 groups', $q$select * from public.discover_groups()$q$, 3);
select pg_temp.check('classmate joins', $q$select public.join_group((select v::uuid from kv where k='g1'))$q$, true);
select pg_temp.as_user(pg_temp.u(7));
select pg_temp.cnt('other class sees only the school group', $q$select * from public.discover_groups()$q$, 1);
select pg_temp.check('other class cannot join a class group', $q$select public.join_group((select v::uuid from kv where k='g1'))$q$, false);
select pg_temp.as_user(pg_temp.u(9));
select pg_temp.cnt('other school discovers nothing', $q$select * from public.discover_groups()$q$, 0);
select pg_temp.check('other school cannot join', $q$select public.join_group((select v::uuid from kv where k='g2'))$q$, false);
select pg_temp.cnt('other school cannot select groups', $q$select * from public.study_groups$q$, 0);
select pg_temp.as_user(pg_temp.u(10));
select pg_temp.cnt('university student sees no school groups', $q$select * from public.discover_groups()$q$, 0);

-- posting
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.check('non-member cannot post', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'hello')$q$, false);
select pg_temp.check('classmate 4 joins', $q$select public.join_group((select v::uuid from kv where k='g1'))$q$, true);
select pg_temp.as_user(pg_temp.u(5)); select public.join_group((select v::uuid from kv where k='g1'));
select pg_temp.as_user(pg_temp.u(6)); select public.join_group((select v::uuid from kv where k='g1'));
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('post ok', $q$insert into kv select 'p1', public.post_to_group((select v::uuid from kv where k='g1'),'Who can explain quadratic equations?')::text$q$, true);
select pg_temp.check('link refused', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'see https://x.example/a')$q$, false);
select pg_temp.check('bare domain refused', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'go to cheat.com now')$q$, false);
select pg_temp.check('e-mail refused', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'mail me bob@mail.example')$q$, false);
select pg_temp.check('phone number refused', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'call 0803 123 4567')$q$, false);
select pg_temp.check('maths with numbers is fine', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'x = 12 and y = 345 so z = 6')$q$, true);
select pg_temp.check('empty post refused', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'   ')$q$, false);
select pg_temp.check('post 3', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'three')$q$, true);
select pg_temp.check('post 4', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'four')$q$, true);
select pg_temp.check('post 5', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'five')$q$, true);
select pg_temp.check('post 6', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'six')$q$, true);
select pg_temp.check('7th post in a minute refused', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'seven')$q$, false);
reset role; update public.group_posts set created_at = now() - interval '2 hours'; set role authenticated;

-- reading
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.cnt('member reads the feed', $q$select * from public.group_feed((select v::uuid from kv where k='g1'))$q$, 6);
select pg_temp.val('author shown as First S.', $q$select author from public.group_feed((select v::uuid from kv where k='g1')) limit 1$q$, 'Sam O.');
select pg_temp.as_user(pg_temp.u(7));
select pg_temp.cnt('non-member cannot read the feed', $q$select * from public.group_feed((select v::uuid from kv where k='g1'))$q$, -1);
select pg_temp.cnt('non-member cannot select posts', $q$select * from public.group_posts$q$, 0);
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.cnt('class teacher reads without joining', $q$select * from public.group_feed((select v::uuid from kv where k='g1'))$q$, 6);
select pg_temp.as_user(pg_temp.u(14));
select pg_temp.cnt('school admin reads school groups', $q$select * from public.group_feed((select v::uuid from kv where k='g2'))$q$, 0);
select pg_temp.as_user(pg_temp.u(8));
select pg_temp.cnt('teacher of another school cannot read', $q$select * from public.group_feed((select v::uuid from kv where k='g1'))$q$, -1);

-- reports and moderation
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('cannot report own post', $q$select public.report_post((select v::bigint from kv where k='p1'),'spam')$q$, false);
select pg_temp.as_user(pg_temp.u(3)); select pg_temp.check('report 1', $q$select public.report_post((select v::bigint from kv where k='p1'),'rude')$q$, true);
select pg_temp.check('same reporter twice does not double count', $q$select public.report_post((select v::bigint from kv where k='p1'),'rude again')$q$, true);
select pg_temp.as_user(pg_temp.u(4)); select public.report_post((select v::bigint from kv where k='p1'),'rude');
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.cnt('2 distinct reports: still visible', $q$select * from public.group_feed((select v::uuid from kv where k='g1')) where id=(select v::bigint from kv where k='p1')$q$, 1);
select pg_temp.as_user(pg_temp.u(5)); select public.report_post((select v::bigint from kv where k='p1'),'rude');
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.cnt('3 distinct reports hide the post', $q$select * from public.group_feed((select v::uuid from kv where k='g1')) where id=(select v::bigint from kv where k='p1')$q$, 0);
select pg_temp.check('ordinary member cannot moderate', $q$select public.moderate_post((select v::bigint from kv where k='p1'),'restore')$q$, false);
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.cnt('teacher sees it in the queue', $q$select * from public.mod_queue()$q$, 1);
select pg_temp.val('teacher sees the hidden post with 3 reports', $q$select reports||'/'||hidden from public.group_feed((select v::uuid from kv where k='g1')) where id=(select v::bigint from kv where k='p1')$q$, '3/true');
select pg_temp.check('teacher restores', $q$select public.moderate_post((select v::bigint from kv where k='p1'),'restore')$q$, true);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.cnt('visible again', $q$select * from public.group_feed((select v::uuid from kv where k='g1')) where id=(select v::bigint from kv where k='p1')$q$, 1);
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('teacher removes', $q$select public.moderate_post((select v::bigint from kv where k='p1'),'remove')$q$, true);
select pg_temp.val('removed body blanked', $q$select body from public.group_feed((select v::uuid from kv where k='g1')) where id=(select v::bigint from kv where k='p1')$q$, '[removed]');
select pg_temp.cnt('removal is logged', $q$select * from public.mod_actions$q$, 3);
select pg_temp.as_user(pg_temp.u(8));
select pg_temp.cnt('other school cannot read the mod log', $q$select * from public.mod_actions$q$, 0);

-- mute and remove (group creator Sam is a mod)
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('mod mutes a member', $q$select public.mute_member((select v::uuid from kv where k='g1'), pg_temp.u(3)::uuid, 2)$q$, true);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.check('muted member cannot post', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'hello')$q$, false);
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.check('ordinary member cannot mute', $q$select public.mute_member((select v::uuid from kv where k='g1'), pg_temp.u(5)::uuid, 2)$q$, false);
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('cannot mute yourself', $q$select public.mute_member((select v::uuid from kv where k='g1'), pg_temp.u(2)::uuid, 2)$q$, false);
select pg_temp.check('mod removes a member', $q$select public.remove_member((select v::uuid from kv where k='g1'), pg_temp.u(6)::uuid)$q$, true);
select pg_temp.as_user(pg_temp.u(6));
select pg_temp.check('removed member cannot post', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'hello')$q$, false);
select pg_temp.as_user(pg_temp.u(5)); select public.leave_group((select v::uuid from kv where k='g1'));
select pg_temp.check('left member cannot post', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'hello')$q$, false);

-- institution groups for university students
select pg_temp.as_user(pg_temp.u(10));
select pg_temp.check('university student creates institution group', $q$insert into kv select 'g3', public.create_group('UNILAG study circle','','institution')$q$, true);
select pg_temp.check('cannot make a school group without a school', $q$select public.create_group('x y z','','school')$q$, false);
select pg_temp.as_user(pg_temp.u(11));
select pg_temp.cnt('same institution (spacing/case differ) discovers it', $q$select * from public.discover_groups()$q$, 1);
select pg_temp.check('same institution joins', $q$select public.join_group((select v::uuid from kv where k='g3'))$q$, true);
select pg_temp.as_user(pg_temp.u(12));
select pg_temp.cnt('other institution sees nothing', $q$select * from public.discover_groups()$q$, 0);
select pg_temp.check('other institution cannot join', $q$select public.join_group((select v::uuid from kv where k='g3'))$q$, false);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.check('secondary student cannot join university group', $q$select public.join_group((select v::uuid from kv where k='g3'))$q$, false);
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.cnt('school staff cannot read university groups', $q$select * from public.study_groups where scope='institution'$q$, 0);
select pg_temp.as_user(pg_temp.u(13));
select pg_temp.cnt('platform admin can read all groups', $q$select * from public.study_groups$q$, 4);

-- archive
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('creator archives', $q$select public.archive_group((select v::uuid from kv where k='g1'))$q$, true);
select pg_temp.check('no posting in archived group', $q$select public.post_to_group((select v::uuid from kv where k='g1'),'hello')$q$, false);
select pg_temp.check('students cannot write groups directly', $q$update public.study_groups set name='hacked'$q$, false);
select pg_temp.check('students cannot write posts directly', $q$insert into public.group_posts(group_id,author_id,body) values ((select v::uuid from kv where k='g2'),auth.uid(),'x')$q$, false);

-- my_teachers
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.val('student sees own class teacher', $q$select count(*)::text||'/'||min(first_name) from public.my_teachers()$q$, '1/Tola');
select pg_temp.as_user(pg_temp.u(9));
select pg_temp.val('other school student sees only their teacher', $q$select min(first_name) from public.my_teachers()$q$, 'Kunle');
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.cnt('staff get nothing from my_teachers', $q$select * from public.my_teachers()$q$, 0);
select pg_temp.as_user(pg_temp.u(10));
select pg_temp.cnt('university student without a class gets nothing', $q$select * from public.my_teachers()$q$, 0);

-- push helpers: service role only
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('users cannot call due_revision_counts', $q$select * from public.due_revision_counts()$q$, false);
reset role;
insert into public.revision_items(user_id,exam,subject,topic,due_on) values (pg_temp.u(2)::uuid,'WASSCE','Maths','Algebra',current_date);
set role service_role;
select pg_temp.cnt('due counts for users with a push subscription', $q$select * from public.due_revision_counts()$q$, 1);
select pg_temp.val('teacher can reach own class', $q$select public.staff_can_reach(pg_temp.u(1)::uuid,'d7000000-0000-0000-0000-0000000000a1')::text$q$, 'true');
select pg_temp.val('teacher cannot reach other class', $q$select public.staff_can_reach(pg_temp.u(1)::uuid,'d7000000-0000-0000-0000-0000000000a2')::text$q$, 'false');
select pg_temp.val('school admin reaches school classes', $q$select public.staff_can_reach(pg_temp.u(14)::uuid,'d7000000-0000-0000-0000-0000000000a2')::text$q$, 'true');
select pg_temp.val('other school teacher cannot reach', $q$select public.staff_can_reach(pg_temp.u(8)::uuid,'d7000000-0000-0000-0000-0000000000a1')::text$q$, 'false');

reset role;
select case when pass then 'PASS' else 'FAIL' end||'|'||name from res order by pass, name;
select count(*) filter (where pass)||'|'||count(*) filter (where not pass) from res;
