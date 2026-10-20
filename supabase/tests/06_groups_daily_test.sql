-- Behaviour tests for 0006. Needs stubs + migrations 0001-0006.
\set ON_ERROR_STOP off
truncate public.schools, auth.users, public.plans cascade;
insert into auth.users(id) select ('e0000000-0000-0000-0000-00000000000'||g)::uuid from generate_series(1,7) g;
insert into public.profiles(id,role,country_code,first_name,surname) select ('e0000000-0000-0000-0000-00000000000'||g)::uuid,'student','NG','U'||g,'S' from generate_series(1,7) g;
-- 1 owner, 2..5 candidates, 6 plain user with no plan, 7 owner of a single plan
insert into public.plans(code,name,currency_code,amount_minor,period,seats) values
 ('solo','Solo','NGN',100000,'month',1),('group4','Group of 4','NGN',250000,'month',4);
insert into public.entitlements(id,user_id,plan_code,status,current_period_end) values
 ('f0000000-0000-0000-0000-000000000001','e0000000-0000-0000-0000-000000000001','group4','active',now()+interval '20 days'),
 ('f0000000-0000-0000-0000-000000000007','e0000000-0000-0000-0000-000000000007','solo','active',now()+interval '20 days');

create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin perform set_config('request.jwt.claim.sub', u, false); end $$;
create temp table res(name text, pass boolean); grant all on res to public;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true; begin begin execute sqltext; exception when others then ok := false; end; insert into res values (n, ok = expect_ok); end $$;
create or replace function pg_temp.cnt(n text, sqltext text, expected int) returns void language plpgsql as $$
declare c int; begin execute 'select count(*) from (' || sqltext || ') q' into c; insert into res values (n || ' (got ' || c || ')', c = expected); end $$;
create or replace function pg_temp.val(n text, sqltext text, expected text) returns void language plpgsql as $$
declare v text; begin execute sqltext into v; insert into res values (n || ' (got ' || coalesce(v,'null') || ')', v is not distinct from expected); end $$;
create temp table codes(k int, c text); grant all on codes to public;
set role authenticated;

-- levels
select pg_temp.as_user('e0000000-0000-0000-0000-000000000002');
select pg_temp.check('set level university', $q$select public.set_my_level('university','Uni of Lagos','Engineering',2)$q$, true);
select pg_temp.val('level saved', $q$select level||'/'||study_year from public.profiles where id=auth.uid()$q$, 'university/2');
select pg_temp.check('bad level rejected', $q$select public.set_my_level('wizard',null,null,1)$q$, false);
select pg_temp.check('year cleared for secondary', $q$select public.set_my_level('secondary',null,null,3)$q$, true);
select pg_temp.val('year null for secondary', $q$select coalesce(study_year::text,'null') from public.profiles where id=auth.uid()$q$, 'null');
select pg_temp.check('cannot self-promote role', $q$update public.profiles set role='platform_admin' where id=auth.uid()$q$, false);

-- goals: own only
select pg_temp.check('write own goal', $q$insert into public.student_goals(user_id,target_course) values (auth.uid(),'Medicine')$q$, true);
select pg_temp.check('cannot write others goal', $q$insert into public.student_goals(user_id,target_course) values ('e0000000-0000-0000-0000-000000000003','X')$q$, false);

-- access before sharing
select pg_temp.val('non-member has no access', $q$select public.has_access()::text$q$, 'false');

-- invites
select pg_temp.as_user('e0000000-0000-0000-0000-000000000006');
select pg_temp.check('no plan: cannot invite', $q$select public.create_invite()$q$, false);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000007');
select pg_temp.check('solo plan: cannot invite', $q$select public.create_invite()$q$, false);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000001');
select pg_temp.check('owner invites 1', $q$insert into codes select 1, public.create_invite('sibling')$q$, true);
select pg_temp.check('owner invites 2', $q$insert into codes select 2, public.create_invite('friend')$q$, true);
select pg_temp.check('owner invites 3', $q$insert into codes select 3, public.create_invite('friend')$q$, true);
select pg_temp.check('4th invite refused (3 member seats)', $q$select public.create_invite()$q$, false);
select pg_temp.cnt('owner sees 3 invites', $q$select * from public.plan_invites$q$, 3);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000002');
select pg_temp.cnt('others cannot read invites', $q$select * from public.plan_invites$q$, 0);
select pg_temp.check('cannot insert invite directly', $q$insert into public.plan_invites(code,entitlement_id,created_by) values ('HACK','f0000000-0000-0000-0000-000000000001',auth.uid())$q$, false);
select pg_temp.check('cannot insert seat directly', $q$insert into public.plan_seats(entitlement_id,member_id) values ('f0000000-0000-0000-0000-000000000001',auth.uid())$q$, false);

-- joining
select pg_temp.check('bad code', $q$select public.join_plan('NOPE1234')$q$, false);
select pg_temp.check('member 2 joins (lowercase code ok)', $q$select public.join_plan((select lower(c) from codes where k=1))$q$, true);
select pg_temp.val('member has access', $q$select public.has_access()::text$q$, 'true');
select pg_temp.check('same code cannot be reused', $q$select public.join_plan((select c from codes where k=1))$q$, false);
select pg_temp.check('already seated: cannot take a second seat', $q$select public.join_plan((select c from codes where k=2))$q$, false);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000001');
select pg_temp.check('owner cannot use own invite', $q$select public.join_plan((select c from codes where k=2))$q$, false);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000007');
select pg_temp.check('another group payer cannot join (solo owner may)', $q$select public.join_plan((select c from codes where k=2))$q$, true);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000003');
select pg_temp.check('member 3 joins', $q$select public.join_plan((select c from codes where k=3))$q$, true);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000001');
select pg_temp.cnt('owner sees 3 members', $q$select * from public.my_group_members()$q$, 3);
select pg_temp.check('owner cannot create invite: plan full', $q$select public.create_invite()$q$, false);

select pg_temp.val('owner status', $q$select kind||'/'||seats||'/'||used||'/'||pending from public.my_plan_status()$q$, 'owner/4/3/0');
select pg_temp.as_user('e0000000-0000-0000-0000-000000000006');
select pg_temp.val('no plan status', $q$select kind from public.my_plan_status()$q$, 'none');
select pg_temp.as_user('e0000000-0000-0000-0000-000000000003');
select pg_temp.val('member status', $q$select kind||'/'||seats from public.my_plan_status()$q$, 'member/4');
-- member privacy: member 2 sees only own seat; cannot see owner's invites or other members
select pg_temp.as_user('e0000000-0000-0000-0000-000000000002');
select pg_temp.cnt('member sees only own seat', $q$select * from public.plan_seats$q$, 1);
select pg_temp.cnt('member cannot list members', $q$select * from public.my_group_members()$q$, 0);
select pg_temp.check('member cannot remove another member', $q$select public.leave_or_remove('e0000000-0000-0000-0000-000000000003')$q$, false);

-- leaving + cooldown
select pg_temp.check('member 2 leaves', $q$select public.leave_or_remove()$q$, true);
select pg_temp.val('access gone after leaving', $q$select public.has_access()::text$q$, 'false');
select pg_temp.as_user('e0000000-0000-0000-0000-000000000001');
select pg_temp.check('owner makes a new invite', $q$insert into codes select 4, public.create_invite()$q$, true);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000002');
select pg_temp.check('30-day switch wait enforced', $q$select public.join_plan((select c from codes where k=4))$q$, false);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000004');
select pg_temp.check('new person takes the freed seat', $q$select public.join_plan((select c from codes where k=4))$q$, true);

-- owner removes member
select pg_temp.as_user('e0000000-0000-0000-0000-000000000001');
select pg_temp.check('owner removes member 4', $q$select public.leave_or_remove('e0000000-0000-0000-0000-000000000004')$q$, true);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000004');
select pg_temp.val('removed member loses access', $q$select public.has_access()::text$q$, 'false');

-- expiry of the owner's plan ends sharing
reset role;
update public.entitlements set current_period_end = now() - interval '1 day' where id='f0000000-0000-0000-0000-000000000001';
set role authenticated;
select pg_temp.as_user('e0000000-0000-0000-0000-000000000003');
select pg_temp.val('expired owner plan: member loses access', $q$select public.has_access()::text$q$, 'false');
reset role;
update public.entitlements set current_period_end = now() + interval '20 days', status='trialing', trial_ends_at = now()+interval '5 days' where id='f0000000-0000-0000-0000-000000000001';
set role authenticated;
select pg_temp.val('trial plan is not shared', $q$select public.has_access()::text$q$, 'false');
reset role;
update public.entitlements set status='active' where id='f0000000-0000-0000-0000-000000000001';
set role authenticated;
select pg_temp.val('active again: member has access', $q$select public.has_access()::text$q$, 'true');
select pg_temp.check('user_has_access not callable by users', $q$select public.user_has_access(auth.uid())$q$, false);

-- class notes
select pg_temp.as_user('e0000000-0000-0000-0000-000000000005');
select pg_temp.check('add note', $q$insert into public.class_notes(user_id,subject,entered_text) values (auth.uid(),'Mathematics','Mr Bello taught simultaneous equations by elimination')$q$, true);
select pg_temp.check('too short note refused', $q$insert into public.class_notes(user_id,subject,entered_text) values (auth.uid(),'Mathematics','a')$q$, false);
select pg_temp.check('note for someone else refused', $q$insert into public.class_notes(user_id,subject,entered_text) values ('e0000000-0000-0000-0000-000000000003','Maths','hello there')$q$, false);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000003');
select pg_temp.cnt('others cannot read my notes', $q$select * from public.class_notes$q$, 0);
select pg_temp.as_user('e0000000-0000-0000-0000-000000000005');
select pg_temp.cnt('I read my note', $q$select * from public.class_notes$q$, 1);
select pg_temp.check('daily note limit of 30', $q$do $d$ begin for i in 1..31 loop insert into public.class_notes(user_id,subject,entered_text) values (auth.uid(),'Maths','note number '||i); end loop; end $d$$q$, false);

-- revision
select pg_temp.check('schedule revision', $q$select public.add_revision('WASSCE','Mathematics','Simultaneous equations',(select id from public.class_notes limit 1))$q$, true);
select pg_temp.check('cannot insert revision directly', $q$insert into public.revision_items(user_id,subject,topic) values (auth.uid(),'a','b')$q$, false);
select pg_temp.check('cannot move due date directly', $q$update public.revision_items set due_on=current_date$q$, false);
select pg_temp.check('not due yet: cannot complete', $q$select public.complete_revision((select id from public.revision_items where topic='Simultaneous equations'),true)$q$, false);
reset role;
update public.revision_items set due_on = current_date where topic='Simultaneous equations';
set role authenticated;
select pg_temp.as_user('e0000000-0000-0000-0000-000000000005');
select pg_temp.val('correct: next review in 3 days', $q$select (public.complete_revision((select id from public.revision_items where topic='Simultaneous equations'),true) - current_date)::text$q$, '3');
reset role; update public.revision_items set due_on=current_date where topic='Simultaneous equations'; set role authenticated;
select pg_temp.as_user('e0000000-0000-0000-0000-000000000005');
select pg_temp.val('correct again: 7 days', $q$select (public.complete_revision((select id from public.revision_items where topic='Simultaneous equations'),true) - current_date)::text$q$, '7');
reset role; update public.revision_items set due_on=current_date where topic='Simultaneous equations'; set role authenticated;
select pg_temp.as_user('e0000000-0000-0000-0000-000000000005');
select pg_temp.val('wrong answer resets to tomorrow', $q$select (public.complete_revision((select id from public.revision_items where topic='Simultaneous equations'),false) - current_date)::text$q$, '1');
select pg_temp.as_user('e0000000-0000-0000-0000-000000000003');
select pg_temp.cnt('others cannot see my revision', $q$select * from public.revision_items$q$, 0);
select pg_temp.check('others cannot complete mine', $q$select public.complete_revision((select id from public.revision_items limit 1),true)$q$, false);

reset role;
select case when pass then 'PASS' else 'FAIL' end||'|'||name from res order by pass, name;
select count(*) filter (where pass)||'|'||count(*) filter (where not pass) from res;
