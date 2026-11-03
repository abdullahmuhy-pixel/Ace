-- 0041 Adds Germany (Abitur, German interface) to the countries table, switches it live and seeds its plan prices. Safe to run more than once.
insert into public.countries (code, name, currency_code, currency_symbol, language, privacy_law, live)
values ('DE', 'Deutschland', 'EUR', '€', 'de', 'DSGVO', true)
on conflict (code) do update set
  name = excluded.name, currency_code = excluded.currency_code, currency_symbol = excluded.currency_symbol,
  language = excluded.language, privacy_law = excluded.privacy_law, live = excluded.live;

insert into public.plans (code, name, country_code, currency_code, amount_minor, period, audience, seats, active) values
 ('de_month', 'Ace Monthly', 'DE', 'EUR', 499, 'month', 'student', 1, true),
 ('de_term', 'Ace Termly', 'DE', 'EUR', 1299, 'term', 'student', 1, true),
 ('de_year', 'Ace Yearly', 'DE', 'EUR', 3999, 'year', 'student', 1, true),
 ('de_group', 'Ace Group (4 people)', 'DE', 'EUR', 9900, 'year', 'student', 4, true),
 ('de_school', 'School licence (per student, 1 year)', 'DE', 'EUR', 1200, 'year', 'school', 1, true)
on conflict (code) do update set name = excluded.name, country_code = excluded.country_code, currency_code = excluded.currency_code,
  amount_minor = excluded.amount_minor, period = excluded.period, audience = excluded.audience, seats = excluded.seats, active = excluded.active;
