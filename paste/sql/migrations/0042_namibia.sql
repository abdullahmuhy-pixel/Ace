-- 0042 Adds Namibia (NSSCO and NSSCAS, DNEA) to the countries table, switches it live and seeds its plan prices. Safe to run more than once.
insert into public.countries (code, name, currency_code, currency_symbol, language, privacy_law, live)
values ('NA', 'Namibia', 'NAD', 'N$', 'en', 'Article 13 of the Constitution (privacy)', true)
on conflict (code) do update set
  name = excluded.name, currency_code = excluded.currency_code, currency_symbol = excluded.currency_symbol,
  language = excluded.language, privacy_law = excluded.privacy_law, live = excluded.live;

insert into public.plans (code, name, country_code, currency_code, amount_minor, period, audience, seats, active) values
 ('na_month', 'Ace Monthly', 'NA', 'NAD', 5900, 'month', 'student', 1, true),
 ('na_term', 'Ace Termly', 'NA', 'NAD', 14900, 'term', 'student', 1, true),
 ('na_year', 'Ace Yearly', 'NA', 'NAD', 44900, 'year', 'student', 1, true),
 ('na_group', 'Ace Group (4 people)', 'NA', 'NAD', 109900, 'year', 'student', 4, true),
 ('na_school', 'School licence (per student, 1 year)', 'NA', 'NAD', 13500, 'year', 'school', 1, true)
on conflict (code) do update set name = excluded.name, country_code = excluded.country_code, currency_code = excluded.currency_code,
  amount_minor = excluded.amount_minor, period = excluded.period, audience = excluded.audience, seats = excluded.seats, active = excluded.active;
