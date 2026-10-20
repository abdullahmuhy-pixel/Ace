-- 0011 Security hardening (defence in depth). Safe to run more than once.
-- Row Level Security already protects every table. This migration also removes privileges that no
-- client ever needs, so a future policy mistake cannot expose data to visitors who are not signed in.

-- 1. No client role needs TRUNCATE, TRIGGER or REFERENCES. TRUNCATE in particular ignores RLS.
do $$
declare r record;
begin
  for r in select c.relname from pg_class c join pg_namespace n on n.oid = c.relnamespace
           where n.nspname = 'public' and c.relkind in ('r','v','m','p') loop
    execute format('revoke truncate, trigger, references on public.%I from anon, authenticated', r.relname);
  end loop;
end $$;

-- 2. Visitors who are not signed in (anon) may only read the public catalogue tables.
do $$
declare r record;
  keep text[] := array['countries','courses','plans','platform_config',
                       'creator_profiles','creator_courses','creator_lessons','creator_plans'];
begin
  for r in select c.relname from pg_class c join pg_namespace n on n.oid = c.relnamespace
           where n.nspname = 'public' and c.relkind in ('r','v','m','p') loop
    execute format('revoke all on public.%I from anon', r.relname);
    if r.relname = any(keep) then
      execute format('grant select on public.%I to anon', r.relname);
    end if;
  end loop;
end $$;

-- 3. Helper functions that only make sense for a signed-in user are closed to anon.
--    (Policies on the anon-readable tables above only call is_platform_admin, which stays open.)
do $$
declare f record;
begin
  for f in select p.oid::regprocedure as sig from pg_proc p join pg_namespace n on n.oid = p.pronamespace
           where n.nspname = 'public'
             and p.proname in ('can_message','class_school','student_in_class','teaches_class','is_school_admin_of',
                               'is_staff','my_ai_usage','my_class','my_role','my_school','has_access') loop
    execute format('revoke execute on function %s from public, anon', f.sig);
    execute format('grant execute on function %s to authenticated', f.sig);
  end loop;
end $$;

-- 4. Tables created later by this role get the same treatment by default.
alter default privileges in schema public revoke truncate, trigger, references on tables from anon, authenticated;
