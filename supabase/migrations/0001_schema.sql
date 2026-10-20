-- Ace Education: core schema. Run migrations in order (0001 -> 0004).
-- Supabase CLI: `supabase db push`, or paste each file into the SQL editor.

create extension if not exists citext;
create extension if not exists pgcrypto;

-- ---------- enums ----------
do $$ begin
  create type public.app_role as enum
    ('student','teacher','subject_teacher','school_admin','platform_admin');
exception when duplicate_object then null; end $$;

do $$ begin
  create type public.topic_status as enum ('not_started','learning','practised','mastered');
exception when duplicate_object then null; end $$;

-- ---------- reference ----------
create table if not exists public.countries (
  code            text primary key check (code ~ '^[A-Z]{2}$'),
  name            text not null,
  currency_code   text not null,
  currency_symbol text not null,
  language        text not null default 'en',
  privacy_law     text,
  live            boolean not null default false
);

-- ---------- schools ----------
create table if not exists public.schools (
  id           uuid primary key default gen_random_uuid(),
  name         text not null check (length(name) between 2 and 120),
  country_code text not null references public.countries(code),
  region       text,
  school_code  text not null unique,
  active       boolean not null default true,
  created_at   timestamptz not null default now()
);

create table if not exists public.classes (
  id         uuid primary key default gen_random_uuid(),
  school_id  uuid not null references public.schools(id) on delete cascade,
  name       text not null,
  grade      text not null,
  unique (school_id, name)
);

-- ---------- profiles (one per auth user) ----------
create table if not exists public.profiles (
  id              uuid primary key references auth.users(id) on delete cascade,
  role            public.app_role not null default 'student',
  school_id       uuid references public.schools(id) on delete set null,
  class_id        uuid references public.classes(id) on delete set null,
  country_code    text not null references public.countries(code),
  first_name      text not null check (length(first_name) between 1 and 60),
  surname         text not null check (length(surname)  between 1 and 60),
  username        citext unique check (username ~ '^[a-z0-9._-]{3,30}$'),
  student_number  text unique,
  contact_email   citext,
  class_level     text,
  exam_target     text,
  language        text not null default 'en',
  consent_at      timestamptz,
  consent_version text,
  created_at      timestamptz not null default now(),
  last_seen_at    timestamptz
);
create index if not exists profiles_school_idx  on public.profiles (school_id, role);
create index if not exists profiles_contact_idx on public.profiles (contact_email);

create table if not exists public.teacher_subjects (
  teacher_id uuid not null references public.profiles(id) on delete cascade,
  class_id   uuid not null references public.classes(id) on delete cascade,
  subject    text not null,
  primary key (teacher_id, class_id, subject)
);

-- ---------- learning data ----------
create table if not exists public.progress (
  user_id    uuid not null references public.profiles(id) on delete cascade,
  exam       text not null,
  subject    text not null,
  topic      text not null,
  status     public.topic_status not null default 'not_started',
  best_score smallint check (best_score between 0 and 100),
  updated_at timestamptz not null default now(),
  primary key (user_id, exam, subject, topic)
);

create table if not exists public.quiz_attempts (
  id         bigint generated always as identity primary key,
  user_id    uuid not null references public.profiles(id) on delete cascade,
  exam       text not null,
  subject    text not null,
  topic      text,
  kind       text not null default 'quiz' check (kind in ('quiz','mock','daily')),
  total      smallint not null check (total between 1 and 200),
  correct    smallint not null check (correct >= 0),
  seconds    integer check (seconds >= 0),
  created_at timestamptz not null default now(),
  check (correct <= total)
);
create index if not exists quiz_user_idx on public.quiz_attempts (user_id, created_at desc);

create table if not exists public.user_stats (
  user_id    uuid primary key references public.profiles(id) on delete cascade,
  xp         integer not null default 0 check (xp >= 0),
  streak     integer not null default 0 check (streak >= 0),
  last_day   date,
  updated_at timestamptz not null default now()
);

-- ---------- security support ----------
create table if not exists public.login_attempts (
  id         bigint generated always as identity primary key,
  key        text not null,            -- sha256(identifier) or ip
  kind       text not null,            -- 'login' | 'reset' | 'join'
  created_at timestamptz not null default now()
);
create index if not exists login_attempts_idx on public.login_attempts (key, kind, created_at desc);

create table if not exists public.audit_log (
  id         bigint generated always as identity primary key,
  actor      uuid,
  action     text not null,
  target     text,
  detail     jsonb,
  created_at timestamptz not null default now()
);

-- ---------- helpers ----------
create or replace function public.gen_school_code(prefix text default 'SCH')
returns text language plpgsql as $$
declare
  alphabet constant text := 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';  -- no 0/O/1/I
  suffix text; code text; i int;
begin
  loop
    suffix := '';
    for i in 1..4 loop
      suffix := suffix || substr(alphabet, 1 + floor(random()*length(alphabet))::int, 1);
    end loop;
    code := upper(left(regexp_replace(prefix,'[^A-Za-z]','','g'),3)) || '-' || suffix;
    exit when not exists (select 1 from public.schools where school_code = code);
  end loop;
  return code;
end $$;

create or replace function public.gen_student_number(cc text)
returns text language plpgsql as $$
declare n text;
begin
  loop
    n := cc || '-' || to_char(now(),'YY') || '-' || lpad(floor(random()*1000000)::text, 6, '0');
    exit when not exists (select 1 from public.profiles where student_number = n);
  end loop;
  return n;
end $$;
