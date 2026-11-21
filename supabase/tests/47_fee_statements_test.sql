-- Behaviour tests for 0047 (fee statements). Needs stubs + all migrations.
\set ON_ERROR_STOP off
truncate public.schools, auth.users cascade;
create or replace function pg_temp.u(n int) returns text language sql immutable as $$ select '47000000-0000-0000-0000-0000000000' || lpad(n::text, 2, '0') $$;
insert into auth.users(id) select pg_temp.u(g)::uuid from generate_series(1,9) g;
insert into public.schools(id,name,country_code,school_code) values
 ('c4700000-0000-0000-0000-00000000000a','School A','NG','AAA-4747'),('c4700000-0000-0000-0000-00000000000b','School B','NG','BBB-4747');
insert into public.classes(id,school_id,name,grade) values ('d4700000-0000-0000-0000-0000000000a1','c4700000-0000-0000-0000-00000000000a','A1','SS1');
-- 1 admin A, 2 teacher A, 3 admin B, 4 5 6 students A (6 graduated), 7 student B
insert into public.profiles(id,role,school_id,class_id,country_code,first_name,surname,enrolment_status) values
 (pg_temp.u(1)::uuid,'school_admin','c4700000-0000-0000-0000-00000000000a',null,'NG','Ada','Admin','active'),
 (pg_temp.u(2)::uuid,'teacher','c4700000-0000-0000-0000-00000000000a',null,'NG','Tola','Teacher','active'),
 (pg_temp.u(3)::uuid,'school_admin','c4700000-0000-0000-0000-00000000000b',null,'NG','Bimpe','AdminB','active'),
 (pg_temp.u(4)::uuid,'student','c4700000-0000-0000-0000-00000000000a','d4700000-0000-0000-0000-0000000000a1','NG','Sam','One','active'),
 (pg_temp.u(5)::uuid,'student','c4700000-0000-0000-0000-00000000000a','d4700000-0000-0000-0000-0000000000a1','NG','Sue','Two','active'),
 (pg_temp.u(6)::uuid,'student','c4700000-0000-0000-0000-00000000000a',null,'NG','Seun','Three','graduated'),
 (pg_temp.u(7)::uuid,'student','c4700000-0000-0000-0000-00000000000b',null,'NG','Bola','Four','active');
create or replace function pg_temp.as_user(u text) returns void language plpgsql as $$ begin perform set_config('request.jwt.claim.sub', u, false); end $$;
create temp table res(name text, pass boolean); grant all on res to public;
create or replace function pg_temp.check(n text, sqltext text, expect_ok boolean) returns void language plpgsql as $$
declare ok boolean := true; begin begin execute sqltext; exception when others then ok := false; end; insert into res values (n, ok = expect_ok); end $$;
create or replace function pg_temp.cnt(n text, sqltext text, expected int) returns void language plpgsql as $$
declare c int; begin begin execute 'select count(*) from (' || sqltext || ') q' into c; exception when others then c := -1; end; insert into res values (n || ' (got ' || c || ')', c = expected); end $$;
create or replace function pg_temp.val(n text, sqltext text, expected text) returns void language plpgsql as $$
declare v text; begin begin execute sqltext into v; exception when others then v := 'ERROR:' || sqlerrm; end; insert into res values (n || ' (got ' || coalesce(v,'null') || ')', v is not distinct from expected); end $$;
create temp table ids(k text, v uuid); grant all on ids to public;

set role authenticated;
select pg_temp.as_user(pg_temp.u(1));
-- 150,000 tuition + 30,000 boarding - 20,000 bursary = 160,000, in instalments 100,000 + 60,000
select pg_temp.check('instalments must add up', $q$select public.bill_students(array['47000000-0000-0000-0000-000000000004']::uuid[],'Term 1','NGN','[{"label":"Tuition","amount":150000},{"label":"Boarding","amount":30000},{"label":"Bursary","amount":-20000}]','[{"due_on":"2026-01-10","amount":100000},{"due_on":"2026-03-01","amount":50000}]')$q$, false);
select pg_temp.val('bill A1 + graduate + other school', $q$select public.bill_students(array['47000000-0000-0000-0000-000000000004','47000000-0000-0000-0000-000000000005','47000000-0000-0000-0000-000000000006','47000000-0000-0000-0000-000000000007']::uuid[],'Term 1','NGN','[{"label":"Tuition","amount":150000},{"label":"Boarding","amount":30000},{"label":"Bursary","amount":-20000}]','[{"due_on":"2026-01-10","amount":100000},{"due_on":"2099-03-01","amount":60000}]')::text$q$, '2');
select pg_temp.val('billing again skips', $q$select public.bill_students(array['47000000-0000-0000-0000-000000000004']::uuid[],'Term 1','NGN','[{"label":"Tuition","amount":1}]')::text$q$, '0');
insert into ids select 'f4', id from public.fees where student_id='47000000-0000-0000-0000-000000000004';
select pg_temp.val('invoice total = items', $q$select amount::text from public.fees where student_id='47000000-0000-0000-0000-000000000004'$q$, '160000.00');
select pg_temp.val('due date = first instalment', $q$select due_on::text from public.fees where student_id='47000000-0000-0000-0000-000000000004'$q$, '2026-01-10');
select pg_temp.val('overdue = first instalment', $q$select public.fee_overdue((select v from ids where k='f4'))::text$q$, '100000.00');
select pg_temp.check('cannot edit total directly', $q$update public.fees set amount=1 where student_id='47000000-0000-0000-0000-000000000004'$q$, false);
select pg_temp.check('cannot edit paid directly', $q$update public.fees set paid=160000 where student_id='47000000-0000-0000-0000-000000000004'$q$, false);
select pg_temp.check('due date still editable', $q$update public.fees set due_on='2026-01-11', note='ok' where student_id='47000000-0000-0000-0000-000000000004'$q$, true);
select pg_temp.val('pay 70,000', $q$select receipt_no from public.record_payment((select v from ids where k='f4'),70000,'2026-01-05','bank','TRX-1')$q$, 'R26-00001');
select pg_temp.val('pay 40,000', $q$select receipt_no from public.record_payment((select v from ids where k='f4'),40000,current_date,'mobile_money')$q$, 'R' || to_char(current_date,'YY') || '-00002');
select pg_temp.val('paid = 110,000', $q$select paid::text from public.fees where id=(select v from ids where k='f4')$q$, '110000.00');
select pg_temp.val('nothing overdue now', $q$select public.fee_overdue((select v from ids where k='f4'))::text$q$, '0');
select pg_temp.check('zero payment rejected', $q$select public.record_payment((select v from ids where k='f4'),0)$q$, false);
select pg_temp.check('payments cannot be inserted directly', $q$insert into public.fee_payments(fee_id,school_id,student_id,receipt_no,amount) values ((select v from ids where k='f4'),'c4700000-0000-0000-0000-00000000000a','47000000-0000-0000-0000-000000000004','X',1)$q$, false);
select pg_temp.check('payments cannot be deleted', $q$delete from public.fee_payments$q$, false);
select pg_temp.cnt('…and none were', 'select * from public.fee_payments', 2);
select pg_temp.check('void needs a reason', $q$select public.void_payment((select id from public.fee_payments where receipt_no='R26-00001'),'')$q$, false);
select pg_temp.check('void', $q$select public.void_payment((select id from public.fee_payments where receipt_no='R26-00001'),'Cheque bounced')$q$, true);
select pg_temp.val('paid drops to 40,000', $q$select paid::text from public.fees where id=(select v from ids where k='f4')$q$, '40000.00');
select pg_temp.val('overdue = 60,000', $q$select public.fee_overdue((select v from ids where k='f4'))::text$q$, '60000.00');
select pg_temp.check('void twice rejected', $q$select public.void_payment((select id from public.fee_payments where receipt_no='R26-00001'),'again')$q$, false);
select pg_temp.check('add a late item', $q$insert into public.fee_items(fee_id,label,amount) values ((select v from ids where k='f4'),'Excursion',5000)$q$, true);
select pg_temp.val('total now 165,000', $q$select amount::text from public.fees where id=(select v from ids where k='f4')$q$, '165000.00');
select pg_temp.check('invoice with payments cannot be deleted', $q$delete from public.fees where id=(select v from ids where k='f4')$q$, false);
select pg_temp.check('unpaid invoice can be deleted', $q$delete from public.fees where student_id='47000000-0000-0000-0000-000000000005'$q$, true);

select pg_temp.as_user(pg_temp.u(2));
select pg_temp.cnt('teacher sees no payments', 'select * from public.fee_payments', 0);
select pg_temp.check('teacher cannot record payment', $q$select public.record_payment((select v from ids where k='f4'),10)$q$, false);
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.check('admin B cannot record payment in A', $q$select public.record_payment((select v from ids where k='f4'),10)$q$, false);
select pg_temp.check('admin B cannot bill A students', $q$select public.bill_students(array['47000000-0000-0000-0000-000000000004']::uuid[],'Term 2','NGN','[{"label":"T","amount":1}]')$q$, false);
select pg_temp.cnt('admin B sees no A items', 'select * from public.fee_items', 0);
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.cnt('student sees own payments', 'select * from public.fee_payments', 2);
select pg_temp.cnt('student sees own items', 'select * from public.fee_items', 4);
select pg_temp.val('student sees own overdue', $q$select public.fee_overdue((select v from ids where k='f4'))::text$q$, '60000.00');
select pg_temp.as_user(pg_temp.u(5));
select pg_temp.cnt('other student sees nothing', 'select * from public.fee_payments', 0);
reset role;
select pg_temp.as_user('');
select (select count(*) filter (where pass) from res) || ' / ' || count(*) || ' passed' as summary from res;
select name as failed from res where not pass;
