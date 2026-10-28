-- 0030: Ace Academy courses added this round (cost-management-accounting auditing-basics taxation-basics investment-markets microfinance-basics insurance-basics financial-modelling public-finance-basics). Idempotent: safe to run again.
-- Course: Cost and Management Accounting. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('cost-management-accounting','Cost and Management Accounting','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='cost-management-accounting';
insert into public.course_keys(course,qid,answer,why) values
  ('cost-management-accounting','q1',1,'It does not change with output in the short term.'),
  ('cost-management-accounting','q2',3,'120 000 / 8000.'),
  ('cost-management-accounting','q3',0,'20 + 12 + 45.'),
  ('cost-management-accounting','q4',2,'50 - 30.'),
  ('cost-management-accounting','q5',2,'40 000 / 20.'),
  ('cost-management-accounting','q6',0,'20 / 50.'),
  ('cost-management-accounting','q7',3,'1000 / 3000.'),
  ('cost-management-accounting','q8',1,'Fixed overhead is carried in closing stock.'),
  ('cost-management-accounting','q9',0,'(10 - 11) x 2100.'),
  ('cost-management-accounting','q10',2,'(2000 - 2100) x 10.'),
  ('cost-management-accounting','q11',1,'Sunk costs cannot be changed.'),
  ('cost-management-accounting','q12',3,'35 - 28.'),
  ('cost-management-accounting','q13',3,'60 000 / 400 000.'),
  ('cost-management-accounting','q14',1,'60 000 - 48 000.');
insert into public.course_lessons(course,lesson_id,position) values
  ('cost-management-accounting','cost-concepts',0),
  ('cost-management-accounting','cvp',1),
  ('cost-management-accounting','costing-methods',2),
  ('cost-management-accounting','budgets-variances',3),
  ('cost-management-accounting','decisions',4),
  ('cost-management-accounting','performance',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='cost-management-accounting' and lesson_id not in ('cost-concepts','cvp','costing-methods','budgets-variances','decisions','performance');
-- Course: Auditing Fundamentals. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('auditing-basics','Auditing Fundamentals','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='auditing-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('auditing-basics','q1',1,'It gives reasonable assurance on the statements.'),
  ('auditing-basics','q2',3,'Auditors give an opinion on them.'),
  ('auditing-basics','q3',0,'2 000 000 x 0.05.'),
  ('auditing-basics','q4',2,'0.05 / 0.3.'),
  ('auditing-basics','q5',2,'Detection risk must be lower.'),
  ('auditing-basics','q6',0,'Splitting duties prevents concealment.'),
  ('auditing-basics','q7',3,'External, direct, documented evidence is strongest.'),
  ('auditing-basics','q8',1,'1 000 000 / 50.'),
  ('auditing-basics','q9',0,'5% of 12 000.'),
  ('auditing-basics','q10',2,'Remove opportunity with controls.'),
  ('auditing-basics','q11',1,'Financial interests create self-interest threats.'),
  ('auditing-basics','q12',3,'"Except for" a matter.'),
  ('auditing-basics','q13',3,'The statements are not fairly presented.'),
  ('auditing-basics','q14',1,'A questioning mind.');
insert into public.course_lessons(course,lesson_id,position) values
  ('auditing-basics','what-is-audit',0),
  ('auditing-basics','risk-materiality',1),
  ('auditing-basics','internal-controls',2),
  ('auditing-basics','evidence-sampling',3),
  ('auditing-basics','fraud-ethics',4),
  ('auditing-basics','reporting',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='auditing-basics' and lesson_id not in ('what-is-audit','risk-materiality','internal-controls','evidence-sampling','fraud-ethics','reporting');
-- Course: Taxation Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('taxation-basics','Taxation Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='taxation-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('taxation-basics','q1',1,'It is charged on spending.'),
  ('taxation-basics','q2',3,'Most income taxes are progressive.'),
  ('taxation-basics','q3',0,'0 + 40 000 + 45 000.'),
  ('taxation-basics','q4',2,'85 000 / 450 000.'),
  ('taxation-basics','q5',2,'The marginal rate applies.'),
  ('taxation-basics','q6',0,'150 000 x 20%.'),
  ('taxation-basics','q7',3,'500 000 + 20 000 - 30 000.'),
  ('taxation-basics','q8',1,'490 000 x 0.27.'),
  ('taxation-basics','q9',0,'30 000 - 18 000.'),
  ('taxation-basics','q10',2,'Exempt supplies cannot reclaim.'),
  ('taxation-basics','q11',1,'1000 goes to the revenue authority.'),
  ('taxation-basics','q12',3,'It is illegal.'),
  ('taxation-basics','q13',3,'They allocate taxing rights between countries.'),
  ('taxation-basics','q14',1,'Transfer pricing rules.');
insert into public.course_lessons(course,lesson_id,position) values
  ('taxation-basics','principles',0),
  ('taxation-basics','personal-income',1),
  ('taxation-basics','business-tax',2),
  ('taxation-basics','vat',3),
  ('taxation-basics','withholding-compliance',4),
  ('taxation-basics','planning-ethics',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='taxation-basics' and lesson_id not in ('principles','personal-income','business-tax','vat','withholding-compliance','planning-ethics');
-- Course: Investment and Financial Markets. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('investment-markets','Investment and Financial Markets','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='investment-markets';
insert into public.course_keys(course,qid,answer,why) values
  ('investment-markets','q1',1,'Secure the basics first.'),
  ('investment-markets','q2',3,'The risk-return trade-off.'),
  ('investment-markets','q3',0,'10 000 x 1.08¹⁰.'),
  ('investment-markets','q4',2,'72 / 8.'),
  ('investment-markets','q5',2,'Compounding on monthly contributions.'),
  ('investment-markets','q6',0,'50 / 5.'),
  ('investment-markets','q7',3,'2 / 50.'),
  ('investment-markets','q8',1,'Older lower coupons become less attractive.'),
  ('investment-markets','q9',0,'100 / 950.'),
  ('investment-markets','q10',2,'7.2 + 2.8.'),
  ('investment-markets','q11',1,'It spreads company-specific risk.'),
  ('investment-markets','q12',3,'Fees compound too.'),
  ('investment-markets','q13',3,'It collapses when new money stops.'),
  ('investment-markets','q14',1,'Licensing gives some protection.');
insert into public.course_lessons(course,lesson_id,position) values
  ('investment-markets','risk-return',0),
  ('investment-markets','compounding',1),
  ('investment-markets','shares-bonds',2),
  ('investment-markets','diversification',3),
  ('investment-markets','funds-costs',4),
  ('investment-markets','behaviour-scams',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='investment-markets' and lesson_id not in ('risk-return','compounding','shares-bonds','diversification','funds-costs','behaviour-scams');
-- Course: Microfinance Fundamentals. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('microfinance-basics','Microfinance Fundamentals','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='microfinance-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('microfinance-basics','q1',1,'Often lacking collateral or access.'),
  ('microfinance-basics','q2',3,'Peer guarantees and support.'),
  ('microfinance-basics','q3',0,'Delivery costs are high relative to loan size.'),
  ('microfinance-basics','q4',2,'10 000 x 0.02 x 12.'),
  ('microfinance-basics','q5',2,'12 400 / 12.'),
  ('microfinance-basics','q6',0,'Flat rates understate the true cost.'),
  ('microfinance-basics','q7',3,'Compare total cost.'),
  ('microfinance-basics','q8',1,'Ability to repay.'),
  ('microfinance-basics','q9',0,'8000 - 5500.'),
  ('microfinance-basics','q10',2,'2500 x 0.5.'),
  ('microfinance-basics','q11',1,'150 000 / 2 000 000.'),
  ('microfinance-basics','q12',3,'Responsible treatment.'),
  ('microfinance-basics','q13',3,'Short terms and fees add up.'),
  ('microfinance-basics','q14',1,'Licensing and cost transparency.');
insert into public.course_lessons(course,lesson_id,position) values
  ('microfinance-basics','what-is-microfinance',0),
  ('microfinance-basics','products',1),
  ('microfinance-basics','pricing',2),
  ('microfinance-basics','credit-assessment',3),
  ('microfinance-basics','portfolio-quality',4),
  ('microfinance-basics','protection-digital',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='microfinance-basics' and lesson_id not in ('what-is-microfinance','products','pricing','credit-assessment','portfolio-quality','protection-digital');
-- Course: Insurance Fundamentals. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('insurance-basics','Insurance Fundamentals','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='insurance-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('insurance-basics','q1',1,'Risk pooling.'),
  ('insurance-basics','q2',3,'1000 x 0.02 x 50 000.'),
  ('insurance-basics','q3',0,'1000 x 1.3.'),
  ('insurance-basics','q4',2,'All material facts must be disclosed.'),
  ('insurance-basics','q5',2,'No profit from loss.'),
  ('insurance-basics','q6',0,'The insurer steps into your rights.'),
  ('insurance-basics','q7',3,'Third-party liability.'),
  ('insurance-basics','q8',1,'20 000 - 2500.'),
  ('insurance-basics','q9',0,'You carry more of each claim.'),
  ('insurance-basics','q10',2,'600/800 x 100 000.'),
  ('insurance-basics','q11',1,'Always read exclusions.'),
  ('insurance-basics','q12',3,'Common in funeral and medical cover.'),
  ('insurance-basics','q13',3,'Prompt reporting and evidence.'),
  ('insurance-basics','q14',1,'It is a crime and raises premiums for all.');
insert into public.course_lessons(course,lesson_id,position) values
  ('insurance-basics','how-insurance-works',0),
  ('insurance-basics','principles',1),
  ('insurance-basics','types',2),
  ('insurance-basics','premiums-excess',3),
  ('insurance-basics','choosing-policies',4),
  ('insurance-basics','claims-fraud',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='insurance-basics' and lesson_id not in ('how-insurance-works','principles','types','premiums-excess','choosing-policies','claims-fraud');
-- Course: Financial Modelling in Spreadsheets. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('financial-modelling','Financial Modelling in Spreadsheets','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='financial-modelling';
insert into public.course_keys(course,qid,answer,why) values
  ('financial-modelling','q1',1,'Separate inputs make models transparent.'),
  ('financial-modelling','q2',3,'Put assumptions in input cells.'),
  ('financial-modelling','q3',0,'PMT(1%, 36, -100000).'),
  ('financial-modelling','q4',2,'36 x 3321.43 - 100 000.'),
  ('financial-modelling','q5',2,'Discounted inflows exceed the cost.'),
  ('financial-modelling','q6',0,'The rate where NPV is zero.'),
  ('financial-modelling','q7',3,'NPV discounts the first listed value by one period.'),
  ('financial-modelling','q8',1,'500 000 x 1.08².'),
  ('financial-modelling','q9',0,'42 000 - 30 000.'),
  ('financial-modelling','q10',2,'It reduces profit but not cash.'),
  ('financial-modelling','q11',1,'Use a check row.'),
  ('financial-modelling','q12',3,'The project no longer pays.'),
  ('financial-modelling','q13',3,'Sensitivity changes one at a time.'),
  ('financial-modelling','q14',1,'Known answers reveal errors.');
insert into public.course_lessons(course,lesson_id,position) values
  ('financial-modelling','model-design',0),
  ('financial-modelling','time-value',1),
  ('financial-modelling','forecasting',2),
  ('financial-modelling','three-statements',3),
  ('financial-modelling','scenarios',4),
  ('financial-modelling','checking-presenting',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='financial-modelling' and lesson_id not in ('model-design','time-value','forecasting','three-statements','scenarios','checking-presenting');
-- Course: Public Finance Basics. Paste into Supabase > SQL Editor and Run. Safe to run again.
insert into public.courses(slug,title,level,pass_mark,lesson_count,quiz_count,active) values ('public-finance-basics','Public Finance Basics','all',70,6,14,true)
  on conflict (slug) do update set title=excluded.title, level=excluded.level, pass_mark=excluded.pass_mark, lesson_count=excluded.lesson_count, quiz_count=excluded.quiz_count, active=true, updated_at=now();
delete from public.course_keys where course='public-finance-basics';
insert into public.course_keys(course,qid,answer,why) values
  ('public-finance-basics','q1',1,'Non-excludable services are under-provided by markets.'),
  ('public-finance-basics','q2',3,'Costs fall on third parties.'),
  ('public-finance-basics','q3',0,'300 / 1500.'),
  ('public-finance-basics','q4',2,'Consumption is steadier than commodity prices.'),
  ('public-finance-basics','q5',2,'Capital spending builds assets.'),
  ('public-finance-basics','q6',0,'1 / (1 - 0.8).'),
  ('public-finance-basics','q7',3,'10 x 5.'),
  ('public-finance-basics','q8',1,'330 - 300.'),
  ('public-finance-basics','q9',0,'900 / 1500.'),
  ('public-finance-basics','q10',2,'90 / 300.'),
  ('public-finance-basics','q11',1,'Revenue must exceed non-interest spending.'),
  ('public-finance-basics','q12',3,'Independent external audit.'),
  ('public-finance-basics','q13',3,'Competition and openness.'),
  ('public-finance-basics','q14',1,'Sub-national governments share responsibilities.');
insert into public.course_lessons(course,lesson_id,position) values
  ('public-finance-basics','role-of-government',0),
  ('public-finance-basics','revenue',1),
  ('public-finance-basics','spending-fiscal-policy',2),
  ('public-finance-basics','deficits-debt',3),
  ('public-finance-basics','pfm-procurement',4),
  ('public-finance-basics','accountability',5)
  on conflict (course,lesson_id) do update set position=excluded.position;
delete from public.course_lessons where course='public-finance-basics' and lesson_id not in ('role-of-government','revenue','spending-fiscal-policy','deficits-debt','pfm-procurement','accountability');
