-- 0040 Adds Portugal (Exames Nacionais, European Portuguese interface) to the countries table, switches it live and seeds its plan prices. Safe to run more than once.
insert into public.countries (code, name, currency_code, currency_symbol, language, privacy_law, live)
values ('PT', 'Portugal', 'EUR', '€', 'pt', 'RGPD', true)
on conflict (code) do update set
  name = excluded.name, currency_code = excluded.currency_code, currency_symbol = excluded.currency_symbol,
  language = excluded.language, privacy_law = excluded.privacy_law, live = excluded.live;

insert into public.plans (code, name, country_code, currency_code, amount_minor, period, audience, seats, active) values
 ('pt_month', 'Ace Monthly', 'PT', 'EUR', 399, 'month', 'student', 1, true),
 ('pt_term', 'Ace Termly', 'PT', 'EUR', 999, 'term', 'student', 1, true),
 ('pt_year', 'Ace Yearly', 'PT', 'EUR', 2999, 'year', 'student', 1, true),
 ('pt_group', 'Ace Group (4 people)', 'PT', 'EUR', 7400, 'year', 'student', 4, true),
 ('pt_school', 'School licence (per student, 1 year)', 'PT', 'EUR', 900, 'year', 'school', 1, true)
on conflict (code) do update set name = excluded.name, country_code = excluded.country_code, currency_code = excluded.currency_code,
  amount_minor = excluded.amount_minor, period = excluded.period, audience = excluded.audience, seats = excluded.seats, active = excluded.active;
