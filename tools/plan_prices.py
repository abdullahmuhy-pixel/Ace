#!/usr/bin/env python3
"""Ace plan prices per market (Oct 2026). Prints the SQL that seeds public.plans and checks every price rule.
Run: python3 tools/plan_prices.py > /tmp/plans.sql"""
from decimal import Decimal as D
# code: (country or None, currency, month, term, year, group-of-4 year)
P = {
 'gb': ('GB', 'GBP', '4.99', '12.99', '39.99', '99'),
 'ie': ('IE', 'EUR', '4.99', '12.99', '39.99', '99'),
 'mt': ('MT', 'EUR', '4.99', '12.99', '39.99', '99'),
 'es': ('ES', 'EUR', '4.99', '12.99', '39.99', '99'),
 'fr': ('FR', 'EUR', '4.99', '12.99', '39.99', '99'),
 'ca': ('CA', 'CAD', '7.99', '19.99', '59.99', '149'),
 'za': ('ZA', 'ZAR', '59', '149', '449', '1099'),
 'bw': ('BW', 'BWP', '40', '100', '300', '750'),
 'ng': ('NG', 'NGN', '1500', '4000', '12000', '30000'),
 'gh': ('GH', 'GHS', '20', '50', '150', '375'),
 'ke': ('KE', 'KES', '200', '500', '1500', '3750'),
 'ug': ('UG', 'UGX', '7000', '18000', '50000', '125000'),
 'tz': ('TZ', 'TZS', '5000', '12000', '35000', '87500'),
 'zm': ('ZM', 'ZMW', '40', '100', '300', '750'),
 'sl': ('SL', 'SLE', '40', '100', '300', '750'),
 'gm': ('GM', 'GMD', '150', '400', '1000', '2500'),
 'zw': ('ZW', 'USD', '2', '5', '15', '37.50'),
 'lr': ('LR', 'USD', '2', '5', '15', '37.50'),
}
CAMPUS = ('USD', '4.99', '39.99')   # Ace Campus, any country
rows = []
def minor(x): v = D(x) * 100; assert v == v.to_integral_value(), x; return int(v)
for k, (cc, cur, m, t, y, g) in P.items():
    m, t, y, g = map(D, (m, t, y, g))
    # rules: a term saves on 3 months, a year saves on 12 months and on 4 terms, the group is 2.2-2.5x one year
    assert t < 3 * m and y < 4 * t and y < 12 * m, k
    assert D('6') <= y / m <= D('8.1'), (k, y / m)
    assert D('2.2') <= g / y <= D('2.5'), (k, g / y)
    rows += [(f'{k}_month', 'Ace Monthly', cc, cur, minor(m), 'month', 1),
             (f'{k}_term', 'Ace Termly', cc, cur, minor(t), 'term', 1),
             (f'{k}_year', 'Ace Yearly', cc, cur, minor(y), 'year', 1),
             (f'{k}_group', 'Ace Group (4 people)', cc, cur, minor(g), 'year', 4)]
cur, m, y = CAMPUS
rows += [('campus_month', 'Ace Campus Monthly', None, cur, minor(m), 'month', 1),
         ('campus_year', 'Ace Campus Yearly', None, cur, minor(y), 'year', 1)]
assert len({r[0] for r in rows}) == len(rows) == 18 * 4 + 2
q = lambda s: 'null' if s is None else "'" + s.replace("'", "''") + "'"
print('insert into public.plans (code, name, country_code, currency_code, amount_minor, period, audience, seats, active) values')
print(',\n'.join(f" ({q(c)}, {q(n)}, {q(cc)}, {q(cu)}, {a}, {q(p)}, 'student', {s}, true)" for c, n, cc, cu, a, p, s in rows))
print("on conflict (code) do update set name = excluded.name, country_code = excluded.country_code, currency_code = excluded.currency_code,\n"
      "  amount_minor = excluded.amount_minor, period = excluded.period, seats = excluded.seats, active = excluded.active;")

def js_month_map():
    """Monthly price per country for the upgrade sheet in app/tiers.js (keep in step: tools/check_all.py compares them)."""
    import json
    m = {cc: [cur, minor(mo)] for k, (cc, cur, mo, t, y, g) in P.items()}
    m['CAMPUS'] = [CAMPUS[0], minor(CAMPUS[1])]
    return json.dumps(m, separators=(',', ':'))
