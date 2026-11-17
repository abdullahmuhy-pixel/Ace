-- Behaviour tests for 0044 (admissions). Needs stubs + all migrations.
\set ON_ERROR_STOP off
truncate public.schools, auth.users cascade;
create or replace function pg_temp.u(n int) returns text language sql immutable as $$ select '44000000-0000-0000-0000-0000000000' || lpad(n::text, 2, '0') $$;
insert into auth.users(id) select pg_temp.u(g)::uuid from generate_series(1,8) g;
insert into public.schools(id,name,country_code,school_code) values
 ('c4400000-0000-0000-0000-00000000000a','School A','NG','AAA-4444'),('c4400000-0000-0000-0000-00000000000b','School B','NG','BBB-4444');
insert into public.classes(id,school_id,name,grade) values
 ('d4400000-0000-0000-0000-0000000000a1','c4400000-0000-0000-0000-00000000000a','A1','SS1'),
 ('d4400000-0000-0000-0000-0000000000b1','c4400000-0000-0000-0000-00000000000b','B1','SS1');
-- 1 admin A, 2 teacher A, 3 admin B, 4 platform admin, 5 student A (new), 6 student B
insert into public.profiles(id,role,school_id,class_id,country_code,first_name,surname) values
 (pg_temp.u(1)::uuid,'school_admin','c4400000-0000-0000-0000-00000000000a',null,'NG','Ada','Admin'),
 (pg_temp.u(2)::uuid,'teacher','c4400000-0000-0000-0000-00000000000a',null,'NG','Tola','Teacher'),
 (pg_temp.u(3)::uuid,'school_admin','c4400000-0000-0000-0000-00000000000b',null,'NG','Bimpe','AdminB'),
 (pg_temp.u(4)::uuid,'platform_admin',null,null,'NG','Pat','Ace'),
 (pg_temp.u(5)::uuid,'student','c4400000-0000-0000-0000-00000000000a','d4400000-0000-0000-0000-0000000000a1','NG','New','Pupil'),
 (pg_temp.u(6)::uuid,'student','c4400000-0000-0000-0000-00000000000b','d4400000-0000-0000-0000-0000000000b1','NG','Other','Pupil');

create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin perform set_config('request.jwt.claim.sub', u, false); end $$;
create temp table res(name text, pass boolean); grant all on res to public;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true; begin begin execute sqltext; exception when others then ok := false; end; insert into res values (n, ok = expect_ok); end $$;
create or replace function pg_temp.cnt(n text, sqltext text, expected int) returns void language plpgsql as $$
declare c int; begin begin execute 'select count(*) from (' || sqltext || ') q' into c; exception when others then c := -1; end; insert into res values (n || ' (got ' || c || ')', c = expected); end $$;
create or replace function pg_temp.val(n text, sqltext text, expected text) returns void language plpgsql as $$
declare v text; begin begin execute sqltext into v; exception when others then v := 'ERROR:' || sqlerrm; end; insert into res values (n || ' (got ' || coalesce(v,'null') || ')', v is not distinct from expected); end $$;

-- as the service role (the edge function)
select pg_temp.val('reference format', $q$select (public.gen_application_ref() ~ '^AP[0-9]{2}-[A-HJ-NP-Z2-9]{6}$')::text$q$, 'true');
insert into public.applications(id,school_id,reference,code_hash,first_name,surname,grade_applied,guardian_email,consent_at) values
 ('a4400000-0000-0000-0000-000000000001','c4400000-0000-0000-0000-00000000000a',public.gen_application_ref(),repeat('a',64),'Kemi','Ade','SS1','mum@example.com',now()),
 ('a4400000-0000-0000-0000-000000000002','c4400000-0000-0000-0000-00000000000b',public.gen_application_ref(),repeat('b',64),'Bayo','Ola','SS1','dad@example.com',now());
insert into public.application_documents(application_id,kind,file_name,mime,size_bytes,path) values
 ('a4400000-0000-0000-0000-000000000001','Birth certificate','bc.pdf','application/pdf',1000,'c4400000-0000-0000-0000-00000000000a/a1/bc.pdf');
select pg_temp.check('no contact details rejected', $q$insert into public.applications(school_id,reference,code_hash,first_name,surname,grade_applied,consent_at) values ('c4400000-0000-0000-0000-00000000000a','AP26-ZZZZZZ',repeat('c',64),'X','Y','SS1',now())$q$, false);
select pg_temp.check('consent required', $q$insert into public.applications(school_id,reference,code_hash,first_name,surname,grade_applied,guardian_email) values ('c4400000-0000-0000-0000-00000000000a','AP26-ZZZZZY',repeat('c',64),'X','Y','SS1','a@b.co')$q$, false);
select pg_temp.check('exe upload rejected', $q$insert into public.application_documents(application_id,kind,file_name,mime,size_bytes,path) values ('a4400000-0000-0000-0000-000000000001','x','x.exe','application/x-msdownload',10,'p/x.exe')$q$, false);
select pg_temp.check('6 MB upload rejected', $q$insert into public.application_documents(application_id,kind,file_name,mime,size_bytes,path) values ('a4400000-0000-0000-0000-000000000001','x','x.pdf','application/pdf',6291456,'p/x2.pdf')$q$, false);

-- reading
set role authenticated;
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.cnt('admin A sees only school A applications', 'select * from public.applications', 1);
select pg_temp.cnt('admin A sees its documents', 'select * from public.application_documents', 1);
select pg_temp.check('admin A cannot update directly', $q$update public.applications set status='accepted'$q$, false);
select pg_temp.check('admin A cannot call the transition itself', $q$select public.application_transition('a4400000-0000-0000-0000-000000000001','accepted','44000000-0000-0000-0000-000000000001')$q$, false);
select pg_temp.check('admin A can open admissions', $q$update public.schools set admissions_open=true, admissions_docs='{Birth certificate}' where id='c4400000-0000-0000-0000-00000000000a'$q$, true);
select pg_temp.val('setting saved', $q$select admissions_open::text from public.schools where id='c4400000-0000-0000-0000-00000000000a'$q$, 'true');
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.cnt('teacher sees no applications', 'select * from public.applications', 0);
select pg_temp.cnt('teacher sees no documents', 'select * from public.application_documents', 0);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.cnt('admin B sees only school B', $q$select * from public.applications where school_id='c4400000-0000-0000-0000-00000000000a'$q$, 0);
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.cnt('platform admin sees all', 'select * from public.applications', 2);
select pg_temp.as_user(pg_temp.u(5));
select pg_temp.cnt('student sees none', 'select * from public.applications', 0);
reset role;
set role anon;
select pg_temp.cnt('anon sees none', 'select * from public.applications', -1);
reset role;
select pg_temp.as_user('');

-- transitions (service role, actor passed in)
select pg_temp.check('admin B cannot decide school A', $q$select public.application_transition('a4400000-0000-0000-0000-000000000001','accepted','44000000-0000-0000-0000-000000000003')$q$, false);
select pg_temp.check('teacher cannot decide', $q$select public.application_transition('a4400000-0000-0000-0000-000000000001','accepted','44000000-0000-0000-0000-000000000002')$q$, false);
select pg_temp.check('staff cannot withdraw', $q$select public.application_transition('a4400000-0000-0000-0000-000000000001','withdrawn','44000000-0000-0000-0000-000000000001')$q$, false);
select pg_temp.check('enrolled cannot be set as a status', $q$select public.application_transition('a4400000-0000-0000-0000-000000000001','enrolled','44000000-0000-0000-0000-000000000001')$q$, false);
select pg_temp.check('cannot enrol before accepting', $q$select public.application_mark_enrolled('a4400000-0000-0000-0000-000000000001','44000000-0000-0000-0000-000000000005','d4400000-0000-0000-0000-0000000000a1','44000000-0000-0000-0000-000000000001')$q$, false);
select pg_temp.val('admin A moves to interview', $q$select public.application_transition('a4400000-0000-0000-0000-000000000001','interview','44000000-0000-0000-0000-000000000001','Strong maths','Please come for an interview on Monday at 9:00.')$q$, 'interview');
select pg_temp.check('same status twice rejected', $q$select public.application_transition('a4400000-0000-0000-0000-000000000001','interview','44000000-0000-0000-0000-000000000001')$q$, false);
select pg_temp.val('admin A accepts', $q$select public.application_transition('a4400000-0000-0000-0000-000000000001','accepted','44000000-0000-0000-0000-000000000001')$q$, 'accepted');
select pg_temp.val('decided_by recorded', $q$select decided_by::text from public.applications where id='a4400000-0000-0000-0000-000000000001'$q$, '44000000-0000-0000-0000-000000000001');
select pg_temp.check('enrol into another school''s class rejected', $q$select public.application_mark_enrolled('a4400000-0000-0000-0000-000000000001','44000000-0000-0000-0000-000000000005','d4400000-0000-0000-0000-0000000000b1','44000000-0000-0000-0000-000000000001')$q$, false);
select pg_temp.check('enrol another school''s student rejected', $q$select public.application_mark_enrolled('a4400000-0000-0000-0000-000000000001','44000000-0000-0000-0000-000000000006','d4400000-0000-0000-0000-0000000000a1','44000000-0000-0000-0000-000000000001')$q$, false);
select pg_temp.check('enrol', $q$select public.application_mark_enrolled('a4400000-0000-0000-0000-000000000001','44000000-0000-0000-0000-000000000005','d4400000-0000-0000-0000-0000000000a1','44000000-0000-0000-0000-000000000001')$q$, true);
select pg_temp.val('status enrolled', $q$select status from public.applications where id='a4400000-0000-0000-0000-000000000001'$q$, 'enrolled');
select pg_temp.check('enrolled is final', $q$select public.application_transition('a4400000-0000-0000-0000-000000000001','declined','44000000-0000-0000-0000-000000000001')$q$, false);
select pg_temp.cnt('three events logged', $q$select * from public.application_events where application_id='a4400000-0000-0000-0000-000000000001'$q$, 3);
select pg_temp.val('applicant message kept', $q$select message from public.application_events where to_status='interview'$q$, 'Please come for an interview on Monday at 9:00.');
select pg_temp.check('note by admin B rejected', $q$select public.application_set_note('a4400000-0000-0000-0000-000000000001','44000000-0000-0000-0000-000000000003','x')$q$, false);
select pg_temp.check('note by admin A', $q$select public.application_set_note('a4400000-0000-0000-0000-000000000001','44000000-0000-0000-0000-000000000001','Sibling in SS3')$q$, true);
select pg_temp.val('applicant withdraws B', $q$select public.application_transition('a4400000-0000-0000-0000-000000000002','withdrawn',null)$q$, 'withdrawn');
select pg_temp.check('withdrawn is final', $q$select public.application_transition('a4400000-0000-0000-0000-000000000002','reviewing','44000000-0000-0000-0000-000000000003')$q$, false);
select pg_temp.cnt('nothing purged yet', 'select * from public.purge_old_applications(365)', 0);
update public.applications set updated_at = now() - interval '400 days' where id='a4400000-0000-0000-0000-000000000002';
insert into public.application_documents(application_id,kind,file_name,mime,size_bytes,path) values ('a4400000-0000-0000-0000-000000000002','Report','r.png','image/png',10,'c4400000-0000-0000-0000-00000000000b/a2/r.png');
select pg_temp.val('purge returns file paths', $q$select string_agg(p, ',') from public.purge_old_applications(365) p$q$, 'c4400000-0000-0000-0000-00000000000b/a2/r.png');
select pg_temp.cnt('old withdrawn application gone', $q$select * from public.applications where id='a4400000-0000-0000-0000-000000000002'$q$, 0);
select pg_temp.cnt('enrolled application kept', $q$select * from public.applications where id='a4400000-0000-0000-0000-000000000001'$q$, 1);

select (select count(*) filter (where pass) from res) || ' / ' || count(*) || ' passed' as summary from res;
select name as failed from res where not pass;
