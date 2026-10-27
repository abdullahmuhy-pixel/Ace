-- 0026 Adds Italy (Esame di Maturità, Italian interface) to the countries table, switches it live and seeds its plan prices. Safe to run more than once.
insert into public.countries (code, name, currency_code, currency_symbol, language, privacy_law, live)
values ('IT', 'Italia', 'EUR', '€', 'it', 'GDPR', true)
on conflict (code) do update set
  name = excluded.name, currency_code = excluded.currency_code, currency_symbol = excluded.currency_symbol,
  language = excluded.language, privacy_law = excluded.privacy_law, live = excluded.live;

insert into public.plans (code, name, country_code, currency_code, amount_minor, period, audience, seats, active) values
 ('it_month', 'Ace Monthly', 'IT', 'EUR', 499, 'month', 'student', 1, true),
 ('it_term', 'Ace Termly', 'IT', 'EUR', 1299, 'term', 'student', 1, true),
 ('it_year', 'Ace Yearly', 'IT', 'EUR', 3999, 'year', 'student', 1, true),
 ('it_group', 'Ace Group (4 people)', 'IT', 'EUR', 9900, 'year', 'student', 4, true),
 ('it_school', 'School licence (per student, 1 year)', 'IT', 'EUR', 1200, 'year', 'school', 1, true)
on conflict (code) do update set name = excluded.name, country_code = excluded.country_code, currency_code = excluded.currency_code,
  amount_minor = excluded.amount_minor, period = excluded.period, audience = excluded.audience, seats = excluded.seats, active = excluded.active;
