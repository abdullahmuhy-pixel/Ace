-- Pin the search path of the admissions reference generator (Supabase security advisor).
alter function public.gen_application_ref() set search_path = public;
