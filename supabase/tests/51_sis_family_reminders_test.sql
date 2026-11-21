-- Behaviour tests for 0051 (SIS-only schools, school family links and the family view, fee reminder list).
\set ON_ERROR_STOP off
truncate public.schools, auth.users cascade;
create or replace function pg_temp.u(n int) returns text language sql immutable as $$ select '51000000-0000-0000-0000-0000000000' || lpad(n::text, 2, '0') $$;
insert into auth.users(id) select pg_temp.u(g)::uuid from generate_series(1,9) g;
insert into public.schools(id,name,country_code,school_code,fee_note) values ('c5100000-0000-0000-0000-00000000000a','School A','NG','AAA-5151','Zenith 123'),('c5100000-0000-0000-0000-00000000000b','School B','NG','BBB-5151',null);
insert into public.classes(id,school_id,name,grade) values ('d5100000-0000-0000-0000-0000000000a1','c5100000-0000-0000-0000-00000000000a','SS1A','SS1');
insert into public.profiles(id,role,school_id,class_id,country_code,first_name,surname) values
 (pg_temp.u(1)::uuid,'school_admin','c5100000-0000-0000-0000-00000000000a',null,'NG','Ada','Admin'),
 (pg_temp.u(2)::uuid,'teacher','c5100000-0000-0000-0000-00000000000a',null,'NG','Tola','Teach'),
 (pg_temp.u(3)::uuid,'school_admin','c5100000-0000-0000-0000-00000000000b',null,'NG','Bimpe','AdminB'),
 (pg_temp.u(4)::uuid,'student','c5100000-0000-0000-0000-00000000000a','d5100000-0000-0000-0000-0000000000a1','NG','Sam','One'),
 (pg_temp.u(5)::uuid,'student','c5100000-0000-0000-0000-00000000000a','d5100000-0000-0000-0000-0000000000a1','NG','Sue','Two');
insert into public.guardians(student_id,name,email,phone) values (pg_temp.u(4)::uuid,'Funke','funke@example.com','+234 803 000 1111');
insert into public.academic_terms(id,school_id,name,starts_on,ends_on) values ('e5100000-0000-0000-0000-000000000001','c5100000-0000-0000-0000-00000000000a','Term 1','2026-09-01','2026-12-15');
insert into public.term_reports(school_id,term_id,student_id,class_id,class_name,average,published_at) values ('c5100000-0000-0000-0000-00000000000a','e5100000-0000-0000-0000-000000000001',pg_temp.u(4)::uuid,'d5100000-0000-0000-0000-0000000000a1','SS1A',74,now());
insert into public.term_reports(school_id,term_id,student_id,class_id,class_name,average) values ('c5100000-0000-0000-0000-00000000000a','e5100000-0000-0000-0000-000000000001',pg_temp.u(5)::uuid,'d5100000-0000-0000-0000-0000000000a1','SS1A',50);
insert into public.school_events(school_id,title,kind,starts_on,ends_on,audience) values ('c5100000-0000-0000-0000-00000000000a','Sports day','event',current_date+3,current_date+3,'everyone'),('c5100000-0000-0000-0000-00000000000a','Staff training','meeting',current_date+4,current_date+4,'staff');
insert into public.behaviour_entries(school_id,student_id,kind,points,description,visible_to_family) values ('c5100000-0000-0000-0000-00000000000a',pg_temp.u(4)::uuid,'merit',1,'Kind to others',true),('c5100000-0000-0000-0000-00000000000a',pg_temp.u(4)::uuid,'concern',-1,'Late',false);
create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin perform set_config('request.jwt.claim.sub', u, false); end $$;
create temp table res(name text, pass boolean); grant all on res to public;
create temp table k(k text, v text); grant all on k to public;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true; begin begin execute sqltext; exception when others then ok := false; end; insert into res values (n, ok = expect_ok); end $$;
create or replace function pg_temp.val(n text, sqltext text, expected text) returns void language plpgsql as $$
declare v text; begin begin execute sqltext into v; exception when others then v := 'ERROR:' || sqlerrm; end; insert into res values (n || ' (got ' || coalesce(v,'null') || ')', v is not distinct from expected); end $$;

set role authenticated;
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('bill Sam 100 due already', $q$select public.bill_students(array['51000000-0000-0000-0000-000000000004']::uuid[],'Term 1','NGN','[{"label":"Tuition","amount":100}]','[{"due_on":"2026-09-10","amount":100}]')$q$, true);
select pg_temp.check('bill Sue 80 due later', $q$select public.bill_students(array['51000000-0000-0000-0000-000000000005']::uuid[],'Term 1','NGN','[{"label":"Tuition","amount":80}]','[{"due_on":"2099-01-10","amount":80}]')$q$, true);
select pg_temp.check('Sam pays 40', $q$select public.record_payment((select id from public.fees where student_id='51000000-0000-0000-0000-000000000004'),40,'2026-09-15','cash')$q$, true);
select pg_temp.check('admin switches to SIS only', $q$update public.schools set product='sis' where id='c5100000-0000-0000-0000-00000000000a'$q$, true);
select pg_temp.check('unknown product rejected', $q$update public.schools set product='x' where id='c5100000-0000-0000-0000-00000000000a'$q$, false);
insert into k select 'code', public.school_family_link('51000000-0000-0000-0000-000000000004','Mother');
select pg_temp.val('code has 12 characters', $q$select length(v)::text from k where k='code'$q$, '12');
select pg_temp.val('admin lists the link', $q$select count(*)::text || ' ' || bool_and(by_school)::text from public.student_family_links('51000000-0000-0000-0000-000000000004')$q$, '1 true');
select pg_temp.val('reminder list: only Sam, 60 overdue', $q$select jsonb_array_length(public.fee_reminder_list())::text || ' ' || (public.fee_reminder_list()->0->>'name') || ' ' || (public.fee_reminder_list()->0->>'overdue') || ' ' || (public.fee_reminder_list()->0->'guardians'->0->>'phone')$q$, '1 Sam One 60.00 +234 803 000 1111');
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('teacher cannot make a family link', $q$select public.school_family_link('51000000-0000-0000-0000-000000000004')$q$, false);
select pg_temp.check('teacher cannot get the reminder list', $q$select public.fee_reminder_list()$q$, false);
select pg_temp.check('teacher cannot switch the product', $q$update public.schools set product='full' where id='c5100000-0000-0000-0000-00000000000a'$q$, true);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.check('admin B cannot make a link for A', $q$select public.school_family_link('51000000-0000-0000-0000-000000000004')$q$, false);
select pg_temp.val('admin B cannot list A links', $q$select count(*)::text from public.student_family_links('51000000-0000-0000-0000-000000000004')$q$, '0');
select pg_temp.check('admin B cannot stop A links', $q$select public.school_revoke_family_link((select id from public.family_links limit 1))$q$, false);
reset role;
select pg_temp.val('product still sis', $q$select product from public.schools where id='c5100000-0000-0000-0000-00000000000a'$q$, 'sis');
select pg_temp.as_user('');
set role anon;
create temp table fv(j jsonb); 
reset role; grant all on fv to public; set role anon;
insert into fv select public.family_view((select v from k where k='code'));
select pg_temp.val('family sees school and product', $q$select (j->'school'->>'name') || ' ' || (j->'school'->>'product') from fv$q$, 'School A sis');
select pg_temp.val('one published report', $q$select jsonb_array_length(j->'school'->'reports')::text || ' ' || (j->'school'->'reports'->0->>'average') from fv$q$, '1 74.00');
select pg_temp.val('fees with overdue and receipt', $q$select (j->'school'->'fees'->0->>'amount') || '/' || (j->'school'->'fees'->0->>'paid') || '/' || (j->'school'->'fees'->0->>'overdue') || '/' || (j->'school'->'fees'->0->'payments'->0->>'receipt') from fv$q$, '100.00/40.00/60.00/R26-00001');
select pg_temp.val('payment details shown', $q$select j->'school'->>'fee_note' from fv$q$, 'Zenith 123');
select pg_temp.val('only the everyone event', $q$select jsonb_array_length(j->'school'->'events')::text || ' ' || (j->'school'->'events'->0->>'title') from fv$q$, '1 Sports day');
select pg_temp.val('only the shared behaviour entry', $q$select jsonb_array_length(j->'school'->'behaviour')::text || ' ' || (j->'school'->'behaviour'->0->>'description') from fv$q$, '1 Kind to others');
select pg_temp.check('anon cannot call the reminder list', $q$select public.fee_reminder_list()$q$, false);
select pg_temp.check('anon cannot make links', $q$select public.school_family_link('51000000-0000-0000-0000-000000000004')$q$, false);
reset role;
set role authenticated;
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('admin stops the link', $q$select public.school_revoke_family_link((select id from public.student_family_links('51000000-0000-0000-0000-000000000004') limit 1))$q$, true);
reset role;
set role anon;
select pg_temp.val('stopped link opens nothing', $q$select coalesce(public.family_view((select v from k where k='code'))::text,'none')$q$, 'none');
reset role;
select (select count(*) filter (where pass) from res) || ' / ' || count(*) || ' passed' as summary from res;
select name as failed from res where not pass;
