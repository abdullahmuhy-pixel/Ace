-- Fee statements: itemised term invoices, instalment plans, receipted payments and voids.
-- public.fees stays the invoice (one per student per term). Its amount is now the sum of its items and its paid
-- column the sum of its payments that are not voided: both are kept by triggers and cannot be edited directly.
-- Payments are never edited or deleted, only voided with a reason, so the statement always adds up.

alter table public.schools add column if not exists receipt_seq integer not null default 0 check (receipt_seq >= 0);
alter table public.schools add column if not exists fee_currency text check (fee_currency is null or fee_currency ~ '^[A-Z]{3}$');
alter table public.schools add column if not exists fee_note text check (length(fee_note) <= 600);   -- bank details etc., printed on statements

alter table public.fees add column if not exists created_at timestamptz not null default now();

create table if not exists public.fee_items (
  id         uuid primary key default gen_random_uuid(),
  fee_id     uuid not null references public.fees(id) on delete cascade,
  label      text not null check (length(label) between 1 and 80),
  amount     numeric(12,2) not null check (amount between -100000000 and 100000000),   -- negative = discount or bursary
  created_at timestamptz not null default now()
);
create index if not exists fee_items_fee_idx on public.fee_items (fee_id);

create table if not exists public.fee_instalments (
  id      uuid primary key default gen_random_uuid(),
  fee_id  uuid not null references public.fees(id) on delete cascade,
  due_on  date not null,
  amount  numeric(12,2) not null check (amount > 0),
  unique (fee_id, due_on)
);

create table if not exists public.fee_payments (
  id           uuid primary key default gen_random_uuid(),
  fee_id       uuid not null references public.fees(id) on delete cascade,
  school_id    uuid not null references public.schools(id) on delete cascade,
  student_id   uuid not null references public.profiles(id) on delete cascade,
  receipt_no   text not null,
  amount       numeric(12,2) not null check (amount > 0),
  paid_on      date not null default current_date check (paid_on <= current_date + 1),
  method       text not null default 'cash' check (method in ('cash','bank','mobile_money','card','cheque','other')),
  reference    text check (length(reference) <= 80),
  note         text check (length(note) <= 300),
  recorded_by  uuid references public.profiles(id) on delete set null,
  created_at   timestamptz not null default now(),
  voided_at    timestamptz,
  voided_by    uuid references public.profiles(id) on delete set null,
  void_reason  text check (length(void_reason) <= 300),
  unique (school_id, receipt_no)
);
create index if not exists fee_payments_fee_idx on public.fee_payments (fee_id);
create index if not exists fee_payments_student_idx on public.fee_payments (student_id, paid_on);

-- ---------- keep fees.amount and fees.paid in step ----------
create or replace function public.fees_guard() returns trigger language plpgsql set search_path = public as $$
begin
  if coalesce(current_setting('ace.fee_sync', true), '') <> 'on' and (new.amount is distinct from old.amount or new.paid is distinct from old.paid) then
    raise exception 'Change the fee items or record a payment instead of editing totals.';
  end if;
  return new;
end $$;
drop trigger if exists fees_guard on public.fees;
create trigger fees_guard before update on public.fees for each row execute function public.fees_guard();

create or replace function public.fee_resync(p_fee uuid) returns void language plpgsql security definer set search_path = public as $$
begin
  perform set_config('ace.fee_sync', 'on', true);
  update public.fees f set
    amount = greatest(0, coalesce((select sum(i.amount) from public.fee_items i where i.fee_id = f.id), f.amount)),
    paid   = coalesce((select sum(p.amount) from public.fee_payments p where p.fee_id = f.id and p.voided_at is null), 0)
  where f.id = p_fee;
  perform set_config('ace.fee_sync', 'off', true);
end $$;

create or replace function public.fee_children_sync() returns trigger language plpgsql security definer set search_path = public as $$
begin
  perform public.fee_resync(coalesce(new.fee_id, old.fee_id));
  return null;
end $$;
drop trigger if exists fee_items_sync on public.fee_items;
create trigger fee_items_sync after insert or update or delete on public.fee_items for each row execute function public.fee_children_sync();
drop trigger if exists fee_payments_sync on public.fee_payments;
create trigger fee_payments_sync after insert or update on public.fee_payments for each row execute function public.fee_children_sync();

create or replace function public.fees_no_delete_paid() returns trigger language plpgsql set search_path = public as $$
begin
  if exists (select 1 from public.fee_payments p where p.fee_id = old.id and p.voided_at is null) then
    raise exception 'This invoice has payments. Void them first.';
  end if;
  return old;
end $$;
drop trigger if exists fees_no_delete_paid on public.fees;
create trigger fees_no_delete_paid before delete on public.fees for each row execute function public.fees_no_delete_paid();

-- invoices recorded before this migration: one item for the old amount, one opening payment for what was paid
insert into public.fee_items (fee_id, label, amount)
select f.id, 'Fees', f.amount from public.fees f where not exists (select 1 from public.fee_items i where i.fee_id = f.id);
do $$ declare f record; k int := 0; begin
  for f in select * from public.fees where paid > 0 and not exists (select 1 from public.fee_payments p where p.fee_id = fees.id) order by created_at loop
    k := k + 1;
    update public.schools set receipt_seq = receipt_seq + 1 where id = f.school_id;
    insert into public.fee_payments (fee_id, school_id, student_id, receipt_no, amount, paid_on, method, note)
    values (f.id, f.school_id, f.student_id, 'OPEN-' || lpad(k::text, 5, '0'), f.paid, coalesce(f.updated_at::date, current_date), 'other', 'Paid before receipts were kept in Ace');
  end loop;
end $$;

-- ---------- RLS ----------
alter table public.fee_items enable row level security;
alter table public.fee_instalments enable row level security;
alter table public.fee_payments enable row level security;
do $$ declare t text; begin
  foreach t in array array['fee_items','fee_instalments'] loop
    execute format('drop policy if exists %1$s_admin on public.%1$s', t);
    execute format($p$create policy %1$s_admin on public.%1$s for all to authenticated
      using (exists (select 1 from public.fees f where f.id = fee_id and (public.is_school_admin_of(f.school_id) or public.is_platform_admin())))
      with check (exists (select 1 from public.fees f where f.id = fee_id and (public.is_school_admin_of(f.school_id) or public.is_platform_admin())))$p$, t);
    execute format('drop policy if exists %1$s_self on public.%1$s', t);
    execute format('create policy %1$s_self on public.%1$s for select to authenticated using (exists (select 1 from public.fees f where f.id = fee_id and f.student_id = auth.uid()))', t);
  end loop;
end $$;
drop policy if exists fee_payments_read on public.fee_payments;
create policy fee_payments_read on public.fee_payments for select to authenticated
  using (public.is_school_admin_of(school_id) or public.is_platform_admin() or student_id = auth.uid());
revoke insert, update, delete on public.fee_payments from anon, authenticated;
revoke all on public.fee_items, public.fee_instalments, public.fee_payments from anon;

-- ---------- actions (school admins) ----------
create or replace function public._fee_admin(p_fee uuid) returns public.fees
language plpgsql stable security definer set search_path = public as $$
declare f public.fees;
begin
  select * into f from public.fees where id = p_fee;
  if not found or not (public.is_school_admin_of(f.school_id) or public.is_platform_admin()) then raise exception 'You do not have permission to do that.'; end if;
  return f;
end $$;

create or replace function public.record_payment(p_fee uuid, p_amount numeric, p_paid_on date default current_date, p_method text default 'cash',
  p_reference text default null, p_note text default null) returns public.fee_payments
language plpgsql security definer set search_path = public as $$
declare f public.fees; s public.schools; r public.fee_payments;
begin
  f := public._fee_admin(p_fee);
  if p_amount is null or p_amount <= 0 then raise exception 'Enter an amount above zero.'; end if;
  update public.schools set receipt_seq = receipt_seq + 1 where id = f.school_id returning * into s;
  insert into public.fee_payments (fee_id, school_id, student_id, receipt_no, amount, paid_on, method, reference, note, recorded_by)
  values (f.id, f.school_id, f.student_id, 'R' || to_char(coalesce(p_paid_on, current_date), 'YY') || '-' || lpad(s.receipt_seq::text, 5, '0'),
          round(p_amount, 2), coalesce(p_paid_on, current_date), coalesce(p_method, 'cash'), nullif(trim(p_reference), ''), nullif(trim(p_note), ''), auth.uid())
  returning * into r;
  return r;
end $$;

create or replace function public.void_payment(p_payment uuid, p_reason text) returns void
language plpgsql security definer set search_path = public as $$
declare p public.fee_payments;
begin
  select * into p from public.fee_payments where id = p_payment for update;
  if not found then raise exception 'Payment not found.'; end if;
  perform public._fee_admin(p.fee_id);
  if p.voided_at is not null then raise exception 'That payment is already void.'; end if;
  if coalesce(trim(p_reason), '') = '' then raise exception 'Give a reason for voiding the payment.'; end if;
  update public.fee_payments set voided_at = now(), voided_by = auth.uid(), void_reason = trim(p_reason) where id = p_payment;
end $$;

-- Bills each listed student for a term: items [{label, amount}], optional instalments [{due_on, amount}] that must add
-- up to the total. Students already billed for that term, students of other schools and leavers are skipped.
create or replace function public.bill_students(p_students uuid[], p_term text, p_currency text, p_items jsonb, p_instalments jsonb default '[]'::jsonb)
returns integer language plpgsql security definer set search_path = public as $$
declare s uuid; total numeric; inst numeric; st uuid; f uuid; k int := 0; it jsonb;
begin
  select school_id into s from public.profiles where id = p_students[1];
  if s is null or not (public.is_school_admin_of(s) or public.is_platform_admin()) then raise exception 'You do not have permission to do that.'; end if;
  if coalesce(trim(p_term), '') = '' or length(p_term) > 40 then raise exception 'Name the term (up to 40 characters).'; end if;
  if p_currency !~ '^[A-Z]{3}$' then raise exception 'Use a three-letter currency code such as NGN.'; end if;
  if jsonb_typeof(p_items) <> 'array' or jsonb_array_length(p_items) = 0 or jsonb_array_length(p_items) > 20 then raise exception 'Add between one and 20 fee items.'; end if;
  select sum((x->>'amount')::numeric) into total from jsonb_array_elements(p_items) x;
  if total is null or total < 0 then raise exception 'The items must add up to zero or more.'; end if;
  if jsonb_array_length(coalesce(p_instalments, '[]'::jsonb)) > 0 then
    select sum((x->>'amount')::numeric) into inst from jsonb_array_elements(p_instalments) x;
    if inst <> total then raise exception 'The instalments add up to % but the fees total %.', inst, total; end if;
  end if;
  foreach st in array p_students loop
    continue when not exists (select 1 from public.profiles where id = st and school_id = s and role = 'student' and enrolment_status in ('active','suspended'));
    continue when exists (select 1 from public.fees where student_id = st and term = trim(p_term));
    insert into public.fees (school_id, student_id, term, amount, currency_code, due_on)
    values (s, st, trim(p_term), total, p_currency,
            (select min((x->>'due_on')::date) from jsonb_array_elements(coalesce(p_instalments, '[]'::jsonb)) x)) returning id into f;
    for it in select * from jsonb_array_elements(p_items) loop
      insert into public.fee_items (fee_id, label, amount) values (f, left(trim(it->>'label'), 80), round((it->>'amount')::numeric, 2));
    end loop;
    insert into public.fee_instalments (fee_id, due_on, amount)
    select f, (x->>'due_on')::date, round((x->>'amount')::numeric, 2) from jsonb_array_elements(coalesce(p_instalments, '[]'::jsonb)) x;
    k := k + 1;
  end loop;
  return k;
end $$;

-- What a student owes now: unpaid instalments that are due (or the whole balance once the invoice is due).
create or replace function public.fee_overdue(p_fee uuid) returns numeric
language sql stable security definer set search_path = public as $$
  select greatest(0, case
    when exists (select 1 from public.fee_instalments i where i.fee_id = f.id)
      then coalesce((select sum(i.amount) from public.fee_instalments i where i.fee_id = f.id and i.due_on <= current_date), 0) - f.paid
    when f.due_on is not null and f.due_on <= current_date then f.amount - f.paid
    else 0 end)
  from public.fees f where f.id = p_fee and (public.is_school_admin_of(f.school_id) or public.is_platform_admin() or f.student_id = auth.uid())
$$;

revoke all on function public.fee_resync(uuid), public.fee_children_sync(), public._fee_admin(uuid) from public, anon, authenticated;
revoke all on function public.record_payment(uuid, numeric, date, text, text, text), public.void_payment(uuid, text),
  public.bill_students(uuid[], text, text, jsonb, jsonb), public.fee_overdue(uuid) from public, anon;
grant execute on function public.record_payment(uuid, numeric, date, text, text, text), public.void_payment(uuid, text),
  public.bill_students(uuid[], text, text, jsonb, jsonb), public.fee_overdue(uuid) to authenticated;
