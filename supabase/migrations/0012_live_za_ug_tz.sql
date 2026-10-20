-- 0012 Switch South Africa, Uganda and Tanzania live (tested by the owner on 2026-10-14). Safe to re-run.
update public.countries set live = true where code in ('ZA','UG','TZ');
select code, name, live from public.countries order by code;
