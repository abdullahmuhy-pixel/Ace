-- 0043 Adds Malawi (MSCE, MANEB) to the countries table, switches it live and seeds its plan prices. Safe to run more than once.
insert into public.countries (code, name, currency_code, currency_symbol, language, privacy_law, live)
values ('MW', 'Malawi', 'MWK', 'K', 'en', 'Data Protection Act, 2024', true)
on conflict (code) do update set
  name = excluded.name, currency_code = excluded.currency_code, currency_symbol = excluded.currency_symbol,
  language = excluded.language, privacy_law = excluded.privacy_law, live = excluded.live;

insert into public.plans (code, name, country_code, currency_code, amount_minor, period, audience, seats, active) values
 ('mw_month', 'Ace Monthly', 'MW', 'MWK', 300000, 'month', 'student', 1, true),
 ('mw_term', 'Ace Termly', 'MW', 'MWK', 750000, 'term', 'student', 1, true),
 ('mw_year', 'Ace Yearly', 'MW', 'MWK', 2250000, 'year', 'student', 1, true),
 ('mw_group', 'Ace Group (4 people)', 'MW', 'MWK', 5250000, 'year', 'student', 4, true),
 ('mw_school', 'School licence (per student, 1 year)', 'MW', 'MWK', 675000, 'year', 'school', 1, true)
on conflict (code) do update set name = excluded.name, country_code = excluded.country_code, currency_code = excluded.currency_code,
  amount_minor = excluded.amount_minor, period = excluded.period, audience = excluded.audience, seats = excluded.seats, active = excluded.active;
