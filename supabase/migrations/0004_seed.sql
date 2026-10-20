insert into public.countries (code,name,currency_code,currency_symbol,language,privacy_law,live) values
 ('NG','Nigeria','NGN','₦','en','NDPA 2023',true),
 ('GH','Ghana','GHS','GH₵','en','Data Protection Act 2012',true),
 ('SL','Sierra Leone','SLE','Le','en',null,true),
 ('GM','The Gambia','GMD','D','en',null,true),
 ('KE','Kenya','KES','KSh','en','Data Protection Act 2019',false),
 ('ZM','Zambia','ZMW','K','en','Data Protection Act 2021',false),
 ('GB','United Kingdom','GBP','£','en','UK GDPR',false),
 ('CA','Canada','CAD','$','en','PIPEDA',false),
 ('ES','España','EUR','€','es','RGPD',false),
 ('IE','Ireland','EUR','€','en','GDPR',false)
on conflict (code) do update set
  name=excluded.name, currency_code=excluded.currency_code,
  currency_symbol=excluded.currency_symbol, language=excluded.language,
  privacy_law=excluded.privacy_law, live=excluded.live;

-- Demo school so you can test the join flow end to end (delete in production).
insert into public.schools (name,country_code,region,school_code)
values ('Greenfield College (Demo)','NG','Lagos','GRF-2K4Q')
on conflict (school_code) do nothing;
