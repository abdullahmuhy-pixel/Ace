-- 0017: saved conversations with Ace, the AI tutor. Each chat is one row; its messages live in a jsonb array
--   so the app can save a whole chat in one upsert. Students see and change only their own chats.
--   Safe to run more than once.

create table if not exists public.ai_chats (
  id          uuid primary key,
  user_id     uuid not null references public.profiles(id) on delete cascade default auth.uid(),
  title       text not null default 'New chat' check (length(title) between 1 and 120),
  portal      text not null default 'school' check (portal in ('school','campus','academy')),
  mode        text not null default 'buddy' check (length(mode) <= 20),
  subject     text check (length(subject) <= 80),
  exam        text check (length(exam) <= 80),
  topic       text check (length(topic) <= 200),
  extra       text check (length(extra) <= 2000),
  turns       jsonb not null default '[]'::jsonb check (jsonb_typeof(turns) = 'array' and jsonb_array_length(turns) <= 400 and pg_column_size(turns) < 600000),
  pinned      boolean not null default false,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);
create index if not exists ai_chats_user_updated on public.ai_chats (user_id, updated_at desc);

alter table public.ai_chats enable row level security;
drop policy if exists ai_chats_own on public.ai_chats;
create policy ai_chats_own on public.ai_chats for all to authenticated
  using (user_id = auth.uid()) with check (user_id = auth.uid());

grant select, insert, update, delete on public.ai_chats to authenticated;

-- keep at most 200 chats per student: the oldest unpinned ones are removed when a new one is added
create or replace function public.ai_chats_trim() returns trigger language plpgsql security definer set search_path = public as $$
begin
  delete from public.ai_chats where id in (
    select id from public.ai_chats where user_id = new.user_id and not pinned
    order by updated_at desc offset 200);
  return null;
end $$;
drop trigger if exists ai_chats_trim on public.ai_chats;
create trigger ai_chats_trim after insert on public.ai_chats for each row execute function public.ai_chats_trim();
