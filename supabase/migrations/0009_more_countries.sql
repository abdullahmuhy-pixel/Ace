-- Adds South Africa (and later Uganda and Tanzania) to the countries table. Safe to run more than once.
insert into public.countries (code,name,currency_code,currency_symbol,language,privacy_law,live) values
 ('ZA','South Africa','ZAR','R','en','POPIA',false),
 ('UG','Uganda','UGX','USh','en','DPPA 2019',false),
 ('TZ','Tanzania','TZS','TSh','en','PDPA 2022',false)
on conflict (code) do update set
  name=excluded.name, currency_code=excluded.currency_code,
  currency_symbol=excluded.currency_symbol, language=excluded.language,
  privacy_law=excluded.privacy_law;
