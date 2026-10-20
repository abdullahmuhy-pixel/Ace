-- 0020 Adds Botswana (BGCSE, BEC) to the countries table and switches it live. Safe to run more than once.
insert into public.countries (code, name, currency_code, currency_symbol, language, privacy_law, live)
values ('BW', 'Botswana', 'BWP', 'P', 'en', 'Data Protection Act', true)
on conflict (code) do update set
  name = excluded.name, currency_code = excluded.currency_code, currency_symbol = excluded.currency_symbol,
  language = excluded.language, privacy_law = excluded.privacy_law, live = excluded.live;
