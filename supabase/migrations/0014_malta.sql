-- 0014 Adds Malta (MATSEC SEC) to the countries table and switches it live. Safe to run more than once.
insert into public.countries (code, name, currency_code, currency_symbol, language, privacy_law, live)
values ('MT', 'Malta', 'EUR', '€', 'en', 'GDPR', true)
on conflict (code) do update set
  name = excluded.name, currency_code = excluded.currency_code, currency_symbol = excluded.currency_symbol,
  language = excluded.language, privacy_law = excluded.privacy_law, live = excluded.live;
select code, name, currency_code, live from public.countries order by code;
