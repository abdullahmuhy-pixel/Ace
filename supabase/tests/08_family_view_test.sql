-- Behaviour tests for 0008 (family view). Needs stubs + migrations 0001-0008.
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

create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin perform set_config('request.jwt.claim.sub', u, false); end $$;
create temp table res(name text, pass boolean); grant all on res to public;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true; begin begin execute sqltext; exception when others then ok := false; end; insert into res values (n, ok = expect_ok); end $$;
create or replace function pg_temp.cnt(n text, sqltext text, expected int) returns void language plpgsql as $$
declare c int; begin begin execute 'select count(*) from (' || sqltext || ') q' into c; exception when others then c := -1; end; insert into res values (n || ' (got ' || c || ')', c = expected); end $$;
create or replace function pg_temp.val(n text, sqltext text, expected text) returns void language plpgsql as $$
declare v text; begin begin execute sqltext into v; exception when others then v := 'ERROR:' || sqlerrm; end; insert into res values (n || ' (got ' || coalesce(v,'null') || ')', v is not distinct from expected); end $$;
create temp table kv(k text, v text); grant all on kv to public;
insert into public.user_stats(user_id,xp,streak) values (pg_temp.u(2)::uuid, 120, 4);
insert into public.quiz_attempts(user_id,exam,subject,total,correct,created_at) values
 (pg_temp.u(2)::uuid,'WAEC','Mathematics',10,7,now()), (pg_temp.u(2)::uuid,'WAEC','Mathematics',10,9,now() - interval '2 days'),
 (pg_temp.u(2)::uuid,'WAEC','Biology',5,5,now() - interval '40 days');
insert into public.attendance values ('d7000000-0000-0000-0000-0000000000a1', pg_temp.u(2)::uuid, current_date, 'present', null),
 ('d7000000-0000-0000-0000-0000000000a1', pg_temp.u(2)::uuid, current_date - 1, 'absent', null);
insert into public.messages(school_id,sender_id,recipient_id,body) select 'c7000000-0000-0000-0000-00000000000a', pg_temp.u(1)::uuid, pg_temp.u(2)::uuid, 'PRIVATE-TEACHER-NOTE' where exists (select 1 from information_schema.tables where table_name='messages');
set role authenticated;
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('student creates a link', $q$insert into kv select 'code', public.create_family_link('Mum')$q$, true);
select pg_temp.val('code is 12 safe characters', $q$select (v ~ '^[A-HJ-NP-Z2-9]{12}$')::text from kv where k='code'$q$, 'true');
select pg_temp.check('2nd link', $q$select public.create_family_link('Dad')$q$, true);
select pg_temp.check('3rd link', $q$select public.create_family_link(null)$q$, true);
select pg_temp.check('4th link refused', $q$select public.create_family_link('x')$q$, false);
select pg_temp.cnt('student sees own 3 links', $q$select * from public.family_links$q$, 3);
select pg_temp.check('cannot insert link directly', $q$insert into public.family_links(student_id,code) values (auth.uid(),'AAAAAAAAAAAA')$q$, false);
select pg_temp.check('cannot extend expiry directly', $q$update public.family_links set expires_at = now() + interval '10 years'$q$, false);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.cnt('other student sees none', $q$select * from public.family_links$q$, 0);
select pg_temp.check('other student cannot revoke', $q$select public.revoke_family_link((select id from public.family_links limit 1))$q$, true);
reset role;
select pg_temp.val('other student revoke did nothing', $q$select count(*)::text from public.family_links where revoked_at is not null$q$, '0');
set role anon;
select pg_temp.val('anon: valid code returns first name', $q$select public.family_view((select v from kv where k='code'))->>'first_name'$q$, 'Sam');
select pg_temp.val('anon: lower case and spaces accepted', $q$select public.family_view(' ' || lower((select v from kv where k='code')) || ' ')->>'first_name'$q$, 'Sam');
select pg_temp.val('anon: streak', $q$select public.family_view((select v from kv where k='code'))->>'streak'$q$, '4');
select pg_temp.val('anon: week has 7 days', $q$select jsonb_array_length(public.family_view((select v from kv where k='code'))->'week')::text$q$, '7');
select pg_temp.val('anon: questions this week = 20', $q$select (select sum((e->>'questions')::int) from jsonb_array_elements(public.family_view((select v from kv where k='code'))->'week') e)::text$q$, '20');
select pg_temp.val('anon: 30-day subjects exclude 40-day-old Biology', $q$select jsonb_array_length(public.family_view((select v from kv where k='code'))->'subjects')::text$q$, '1');
select pg_temp.val('anon: maths 16 of 20', $q$select (public.family_view((select v from kv where k='code'))->'subjects'->0->>'correct')||'/'||(public.family_view((select v from kv where k='code'))->'subjects'->0->>'questions')$q$, '16/20');
select pg_temp.val('anon: attendance counts', $q$select (public.family_view((select v from kv where k='code'))->'attendance_30d')::text$q$, '{"absent": 1, "present": 1}');
select pg_temp.val('anon: no private text leaks', $q$select (position('PRIVATE' in public.family_view((select v from kv where k='code'))::text) > 0)::text$q$, 'false');
select pg_temp.val('anon: no surname or email leaks', $q$select (public.family_view((select v from kv where k='code'))::text ~* 'One|@')::text$q$, 'false');
select pg_temp.val('anon: wrong code returns null', $q$select coalesce(public.family_view('AAAAAAAAAAAA')::text,'null')$q$, 'null');
select pg_temp.val('anon: empty code returns null', $q$select coalesce(public.family_view('')::text,'null')$q$, 'null');
select pg_temp.val('anon: null code returns null', $q$select coalesce(public.family_view(null)::text,'null')$q$, 'null');
select pg_temp.check('anon cannot read the table', $q$select * from public.family_links$q$, false);
select pg_temp.check('anon cannot create links', $q$select public.create_family_link('x')$q$, false);
reset role;
select pg_temp.val('last_viewed recorded', $q$select (last_viewed is not null)::text from public.family_links where code=(select v from kv where k='code')$q$, 'true');
set role authenticated;
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('student revokes own link', $q$select public.revoke_family_link((select id from public.family_links where label='Mum'))$q$, true);
set role anon;
select pg_temp.val('revoked code stops working', $q$select coalesce(public.family_view((select v from kv where k='code'))::text,'null')$q$, 'null');
reset role;
insert into kv select 'dad', code from public.family_links where label='Dad';
update public.family_links set expires_at = now() - interval '1 day' where label='Dad';
set role anon;
select pg_temp.val('expired code stops working', $q$select coalesce(public.family_view((select v from kv where k='dad'))::text,'null')$q$, 'null');
reset role;
select case when pass then 'PASS' else 'FAIL' end||'|'||name from res order by pass, name;
select count(*) filter (where pass)||'|'||count(*) filter (where not pass) from res;
