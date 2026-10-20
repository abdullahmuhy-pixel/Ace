-- 0021 Adds France (baccalauréat, French interface) to the countries table and switches it live. Safe to run more than once.
insert into public.countries (code, name, currency_code, currency_symbol, language, privacy_law, live)
values ('FR', 'France', 'EUR', '€', 'fr', 'RGPD', true)
on conflict (code) do update set
  name = excluded.name, currency_code = excluded.currency_code, currency_symbol = excluded.currency_symbol,
  language = excluded.language, privacy_law = excluded.privacy_law, live = excluded.live;
