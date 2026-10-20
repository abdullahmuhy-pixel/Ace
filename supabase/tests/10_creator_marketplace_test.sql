-- Behaviour tests for 0010. Needs stubs + migrations 0001-0010.
\set ON_ERROR_STOP off
truncate public.schools, auth.users cascade;
create or replace function pg_temp.u(n int) returns text language sql immutable as $$ select 'aa000000-0000-0000-0000-0000000000' || lpad(n::text, 2, '0') $$;
insert into auth.users(id) select pg_temp.u(g)::uuid from generate_series(1,8) g;
insert into public.profiles(id,role,country_code,first_name,surname) values
 (pg_temp.u(1)::uuid,'platform_admin','NG','Pat','Admin'),(pg_temp.u(2)::uuid,'student','NG','Cora','Creator'),(pg_temp.u(3)::uuid,'student','NG','Sam','Subscriber'),
 (pg_temp.u(4)::uuid,'student','NG','Nia','Nonsub'),(pg_temp.u(5)::uuid,'student','NG','Pete','Pending');
update public.marketplace_settings set default_fee_pct = 30, fee_basis = 'net', payout_hold_days = 14, min_payout_minor = 1000;

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

-- ===== applying =====
select pg_temp.as_user('');
select pg_temp.check('signed-out cannot apply', $q$select public.apply_creator('cora-teaches','Cora','h','b','NG',true,'v1')$q$, false);
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('under-18 flag blocks application', $q$select public.apply_creator('cora-teaches','Cora','h','b','NG',false,'v1')$q$, false);
select pg_temp.check('bad handle rejected', $q$select public.apply_creator('Co ra!','Cora','h','b','NG',true,'v1')$q$, false);
select pg_temp.check('terms are required', $q$select public.apply_creator('cora-teaches','Cora','h','b','NG',true,'')$q$, false);
select pg_temp.check('valid application', $q$select public.apply_creator('cora-teaches','Cora Creator','Maths tutor','Ten years of teaching.','NG',true,'v1')$q$, true);
select pg_temp.check('cannot apply twice', $q$select public.apply_creator('cora-two','Cora','h','b','NG',true,'v1')$q$, false);
select pg_temp.check('cannot self-approve', $q$update public.creator_profiles set status = 'approved' where user_id = auth.uid()$q$, false);
select pg_temp.check('cannot set own fee', $q$update public.creator_profiles set fee_pct = 0 where user_id = auth.uid()$q$, false);
select pg_temp.check('can edit own bio', $q$update public.creator_profiles set bio = 'Updated bio' where user_id = auth.uid()$q$, true);
select pg_temp.check('pending creator cannot create a course', $q$insert into public.creator_courses(creator_id,slug,title,summary,field) values (auth.uid(),'early-course','Early course','A summary of ten chars','sci')$q$, false);
select pg_temp.check('pending creator cannot create a plan', $q$insert into public.creator_plans(creator_id,name,currency_code,amount_minor,period) values (auth.uid(),'Basic','NGN',500000,'month')$q$, false);
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.cnt('public cannot see pending creators', $q$select * from public.creator_profiles$q$, 0);
select pg_temp.check('non-admin cannot approve', $q$select public.review_creator(public.u_dummy(),'approved')$q$, false);
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('admin approves creator at 25 percent', format($q$select public.review_creator(%L,'approved',25,'ok')$q$, pg_temp.u(2)), true);
select pg_temp.val('creator status approved', format($q$select status from public.creator_profiles where user_id = %L$q$, pg_temp.u(2)), 'approved');

-- ===== building a course =====
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('approved creator makes a plan', $q$insert into public.creator_plans(creator_id,name,currency_code,amount_minor,period) values (auth.uid(),'Monthly','NGN',500000,'month')$q$, true);
select pg_temp.check('creator cannot insert a course already approved', $q$insert into public.creator_courses(creator_id,slug,title,summary,field,status) values (auth.uid(),'sneaky','Sneaky course','A summary of ten chars','sci','approved')$q$, false);
select pg_temp.check('creator makes a draft course', $q$insert into public.creator_courses(creator_id,slug,title,summary,field) values (auth.uid(),'algebra-from-zero','Algebra from Zero','Learn algebra step by step with video lessons.','sci')$q$, true);
insert into kv select 'course', id::text from public.creator_courses where slug = 'algebra-from-zero';
select pg_temp.check('submit blocked with no lessons', format($q$select public.submit_creator_course(%L)$q$, (select v from kv where k='course')), false);
select pg_temp.check('add lesson 1 (preview)', format($q$insert into public.creator_lessons(course_id,position,title,duration_sec,is_preview) values (%L,0,'Welcome',300,true)$q$, (select v from kv where k='course')), true);
select pg_temp.check('add lesson 2', format($q$insert into public.creator_lessons(course_id,position,title,duration_sec) values (%L,1,'Variables',900)$q$, (select v from kv where k='course')), true);
select pg_temp.check('add lesson 3', format($q$insert into public.creator_lessons(course_id,position,title,duration_sec) values (%L,2,'Equations',1200)$q$, (select v from kv where k='course')), true);
select pg_temp.check('duplicate position rejected', format($q$insert into public.creator_lessons(course_id,position,title) values (%L,2,'Dupe')$q$, (select v from kv where k='course')), false);
select pg_temp.check('submit blocked: lessons have no content', format($q$select public.submit_creator_course(%L)$q$, (select v from kv where k='course')), false);
insert into public.creator_lesson_content(lesson_id, body, video_provider, video_ref) select id, 'Notes for ' || title, 'bunny', 'vid-' || position from public.creator_lessons where course_id = (select v from kv where k='course')::uuid;
select pg_temp.check('submit now succeeds', format($q$select public.submit_creator_course(%L)$q$, (select v from kv where k='course')), true);
select pg_temp.check('creator cannot edit lessons while submitted', format($q$update public.creator_lessons set title = 'Changed' where course_id = %L$q$, (select v from kv where k='course')), true);
select pg_temp.val('lesson edit blocked while under review (no rows changed)', format($q$select count(*)::text from public.creator_lessons where course_id = %L and title = 'Changed'$q$, (select v from kv where k='course')), '0');
select pg_temp.check('creator cannot approve own course', format($q$update public.creator_courses set status = 'approved' where id = %L$q$, (select v from kv where k='course')), true);
select pg_temp.val('course still submitted', format($q$select status from public.creator_courses where id = %L$q$, (select v from kv where k='course')), 'submitted');
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.cnt('students cannot see unapproved courses', $q$select * from public.creator_courses$q$, 0);
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('admin approves the course', format($q$select public.review_creator_course(%L,'approved')$q$, (select v from kv where k='course')), true);
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.cnt('students now see the approved course', $q$select * from public.creator_courses$q$, 1);
select pg_temp.cnt('students see the 3 lesson titles', $q$select * from public.creator_lessons$q$, 3);
select pg_temp.cnt('students cannot read protected content table', $q$select * from public.creator_lesson_content$q$, 0);
select pg_temp.check('non-subscriber can open the preview lesson', format($q$select * from public.get_lesson_content(%L)$q$, (select id from public.creator_lessons where position = 0 and course_id = (select v from kv where k='course')::uuid)), true);
select pg_temp.check('non-subscriber blocked on a paid lesson', format($q$select * from public.get_lesson_content(%L)$q$, (select id from public.creator_lessons where position = 1 and course_id = (select v from kv where k='course')::uuid)), false);
select pg_temp.check('students cannot call the payment recorder', format($q$select public.record_creator_payment(%L,%L,500000,7500,'test','x1')$q$, pg_temp.u(3), (select id from public.creator_plans limit 1)), false);

-- ===== payments and the split (service role = the webhook) =====
reset role; set role service_role;
insert into kv select 'plan', id::text from public.creator_plans limit 1;
select pg_temp.val('payment 1 recorded', format($q$select (public.record_creator_payment(%L,%L,500000,7500,'test','pay-1') is not null)::text$q$, pg_temp.u(3), (select v from kv where k='plan')), 'true');
select pg_temp.val('platform fee = 25 percent of net (492,500)', $q$select platform_fee_minor::text from public.creator_payments where provider_ref = 'pay-1'$q$, '123125');
select pg_temp.val('creator share = net minus fee', $q$select creator_share_minor::text from public.creator_payments where provider_ref = 'pay-1'$q$, '369375');
select pg_temp.val('parts add up to gross minus provider fee', $q$select (platform_fee_minor + creator_share_minor + provider_fee_minor)::text from public.creator_payments where provider_ref = 'pay-1'$q$, '500000');
select pg_temp.val('payment is idempotent', format($q$select (public.record_creator_payment(%L,%L,500000,7500,'test','pay-1') = (select id from public.creator_payments where provider_ref = 'pay-1'))::text$q$, pg_temp.u(3), (select v from kv where k='plan')), 'true');
select pg_temp.val('only one earning row after retry', $q$select count(*)::text from public.creator_ledger where kind = 'earning'$q$, '1');
select pg_temp.val('one live subscription', $q$select count(*)::text from public.creator_subscriptions where status = 'active'$q$, '1');
select pg_temp.check('bad amounts rejected', format($q$select public.record_creator_payment(%L,%L,1000,1000,'test','bad')$q$, pg_temp.u(3), (select v from kv where k='plan')), false);
select pg_temp.val('rounding: 33,333 gross, 1,000 fee, 25 percent', format($q$select (public.record_creator_payment(%L,%L,33333,1000,'test','pay-2') is not null)::text$q$, pg_temp.u(3), (select v from kv where k='plan')), 'true');
select pg_temp.val('rounding: platform part', $q$select platform_fee_minor::text from public.creator_payments where provider_ref = 'pay-2'$q$, '8083');
select pg_temp.val('rounding: creator part', $q$select creator_share_minor::text from public.creator_payments where provider_ref = 'pay-2'$q$, '24250');
select pg_temp.val('second payment extends the same subscription', $q$select count(*)::text from public.creator_subscriptions$q$, '1');

-- ===== what each person can see =====
reset role; set role authenticated;
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.check('subscriber can watch a paid lesson', format($q$select * from public.get_lesson_content(%L)$q$, (select id from public.creator_lessons where position = 1 and course_id = (select v from kv where k='course')::uuid)), true);
select pg_temp.val('subscriber receives the video reference', format($q$select video_ref from public.get_lesson_content(%L)$q$, (select id from public.creator_lessons where position = 2 and course_id = (select v from kv where k='course')::uuid)), 'vid-2');
select pg_temp.cnt('subscriber sees own subscription', $q$select * from public.creator_subscriptions$q$, 1);
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.cnt('other student sees no subscriptions', $q$select * from public.creator_subscriptions$q$, 0);
select pg_temp.cnt('other student sees no payments', $q$select * from public.creator_payments$q$, 0);
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.cnt('creator cannot see subscribers', $q$select * from public.creator_subscriptions$q$, 0);
select pg_temp.val('creator stats count 1 subscriber', $q$select active_subscribers::text from public.creator_stats()$q$, '1');
select pg_temp.val('creator stats lifetime earned', $q$select lifetime_earned_minor::text from public.creator_stats()$q$, '393625');
select pg_temp.cnt('creator sees own 2 payments', $q$select * from public.creator_payments$q$, 2);
select pg_temp.check('creator cannot write the ledger', $q$insert into public.creator_ledger(creator_id,kind,currency_code,amount_minor) values (auth.uid(),'adjustment','NGN',99999999)$q$, false);
select pg_temp.check('creator cannot edit a payment', $q$update public.creator_payments set creator_share_minor = 99999999$q$, false);
select pg_temp.val('earnings are pending during the hold', $q$select pending_minor::text from public.creator_balance()$q$, '393625');
select pg_temp.val('nothing available during the hold', $q$select available_minor::text from public.creator_balance()$q$, '0');

-- ===== payouts =====
select pg_temp.check('no payout without payout details', $q$select public.request_payout('NGN',5000)$q$, false);
insert into public.creator_payout_details(user_id, method, details) values (pg_temp.u(2)::uuid, 'mobile_money', 'Provider X, 0800 000 0000, Cora Creator');
select pg_temp.check('no payout while earnings are on hold', $q$select public.request_payout('NGN',5000)$q$, false);
reset role; update public.marketplace_settings set payout_hold_days = 0; update public.creator_ledger set available_at = now() - interval '1 day'; set role authenticated;
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.val('available after the hold', $q$select available_minor::text from public.creator_balance()$q$, '393625');
select pg_temp.check('below minimum payout rejected', $q$select public.request_payout('NGN',500)$q$, false);
select pg_temp.check('more than available rejected', $q$select public.request_payout('NGN',400000)$q$, false);
select pg_temp.check('payout of 300,000 accepted', $q$select public.request_payout('NGN',300000)$q$, true);
select pg_temp.val('available falls by the reserved amount', $q$select available_minor::text from public.creator_balance()$q$, '93625');
select pg_temp.check('second open payout rejected', $q$select public.request_payout('NGN',5000)$q$, false);
insert into kv select 'payout', id::text from public.payout_requests;
select pg_temp.check('creator cannot approve own payout', format($q$select public.decide_payout(%L,'paid','ref')$q$, (select v from kv where k='payout')), false);
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('admin rejects the payout', format($q$select public.decide_payout(%L,'rejected',null,'wrong details')$q$, (select v from kv where k='payout')), true);
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.val('rejected payout returns the money', $q$select available_minor::text from public.creator_balance()$q$, '393625');
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('a decided payout cannot be decided again', format($q$select public.decide_payout(%L,'paid','ref')$q$, (select v from kv where k='payout')), false);
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.check('new payout of 393,625 accepted', $q$select public.request_payout('NGN',393625)$q$, true);
insert into kv select 'payout2', id::text from public.payout_requests where status = 'requested';
select pg_temp.as_user(pg_temp.u(1));
select pg_temp.check('admin marks it paid', format($q$select public.decide_payout(%L,'paid','BANK-REF-1')$q$, (select v from kv where k='payout2')), true);
select pg_temp.as_user(pg_temp.u(2));
select pg_temp.val('balance is zero after the payout', $q$select available_minor::text from public.creator_balance()$q$, '0');
select pg_temp.val('withdrawn total', $q$select withdrawn_minor::text from public.creator_balance()$q$, '393625');

-- ===== refunds and cancellation =====
reset role; set role service_role;
select pg_temp.val('refund runs', $q$select (public.refund_creator_payment((select id from public.creator_payments where provider_ref = 'pay-2'), 'customer request')::text = '')::text$q$, 'true');
select pg_temp.val('refund is a negative ledger line', $q$select amount_minor::text from public.creator_ledger where kind = 'refund'$q$, '-24250');
select pg_temp.val('second refund does nothing', $q$select (public.refund_creator_payment((select id from public.creator_payments where provider_ref = 'pay-2'))::text = '')::text$q$, 'true');
select pg_temp.val('still one refund line', $q$select count(*)::text from public.creator_ledger where kind = 'refund'$q$, '1');
reset role; set role authenticated;
select pg_temp.as_user(pg_temp.u(3));
select pg_temp.check('refund ends access to paid lessons', format($q$select * from public.get_lesson_content(%L)$q$, (select id from public.creator_lessons where position = 1 and course_id = (select v from kv where k='course')::uuid)), false);
select pg_temp.as_user(pg_temp.u(4));
select pg_temp.check('anyone can report a course', format($q$select public.report_creator_course_dummy()$q$), false);
select pg_temp.check('report a course', format($q$select public.report_creator_content(%L,'This looks copied from a textbook.')$q$, (select v from kv where k='course')), true);
select pg_temp.cnt('students cannot read reports', $q$select * from public.creator_reports$q$, 0);

reset role;
select name, pass from res where not pass;
select count(*) filter (where pass) as passed, count(*) filter (where not pass) as failed from res;
