# Ace Education: Supabase setup

## 1. Database
Run in order (SQL editor, or `supabase db push` with these in `supabase/migrations/`):
`0001_schema.sql` -> `0002_rls.sql` -> `0003_views_triggers.sql` -> `0004_seed.sql`
Delete the demo school (`GRF-2K4Q`) from 0004 before going live.

## 2. Edge functions
```
supabase functions deploy join-school lookup-school resolve-login request-reset reset-password \
  create-school invite-staff bulk-create-students delete-account
```
Append `functions/config.toml` to your project's `supabase/config.toml` (turns the gateway JWT check off;
each function checks the caller itself and the public ones are rate-limited).

Secrets (`supabase secrets set KEY=value`):
| Secret | Purpose |
|---|---|
| `SITE_URL` | where staff invite emails send people (your site URL) |
| `ALLOWED_ORIGINS` | comma list of your site origins; default `*` |
| `STUDENT_EMAIL_DOMAIN` | synthetic login domain, default `students.aceeducation.app` (never receives mail) |
| `RESEND_API_KEY`, `MAIL_FROM` | sends reset codes. Without a key the code is only written to the function log |

`SUPABASE_URL`, `SUPABASE_ANON_KEY` and `SUPABASE_SERVICE_ROLE_KEY` are provided automatically.

## 3. Auth settings (Dashboard -> Authentication)
- Email provider on; **turn off "Allow new users to sign up"** (accounts are created only by the functions).
- Password minimum length 8. Site URL = your site; add it to redirect URLs.
- Optional: schedule `select public.purge_login_attempts();` daily (pg_cron).

## 4. First platform admin
Create a user in the dashboard (Authentication -> Users), then in SQL:
```sql
insert into public.profiles (id, role, country_code, first_name, surname, contact_email)
values ('<that user id>', 'platform_admin', 'NG', 'Your', 'Name', 'you@example.com');
```
That admin calls `create-school` to onboard schools; school admins call `invite-staff` and
`bulk-create-students`.

## 5. Login page and student app
Both read `/config.js` at the repo root (`supabaseUrl`, `supabaseAnonKey`). The login page, the student app and
the website are deployed under one domain by `.github/workflows/pages.yml`, so the session is shared.
The student app syncs `progress`, `quiz_attempts` and `user_stats` when a student is signed in (RLS limits each
student to their own rows) and falls back to local-only guest mode otherwise.

## 6. Migration 0005 and the newer functions
`0005_class_ops.sql` adds attendance, assessments and marks, tasks, announcements, messages, live quiz, guardians,
plans, payments, promo codes, AI usage, push subscriptions, content reports and an error log. Behaviour tests are in
`supabase/tests/05_class_ops_test.sql` (64 checks, run by CI against a throwaway Postgres).

| Function | Purpose | Extra secrets |
|---|---|---|
| `ai-tutor` | AI tutor with server-counted free / paid limits (`consume_ai_kind`) and a cheap or strong model per tool | `ANTHROPIC_API_KEY`, optional `AI_MODEL_FAST`, `AI_MODEL_SMART` |
| `checkout-start` | Starts a Flutterwave payment for a plan stored in `plans` | `FLW_PUBLIC_KEY`, `SITE_URL` |
| `payments-webhook` | Verifies the payment with Flutterwave, then grants access | `FLW_SECRET_KEY`, `FLW_SECRET_HASH` |
| `send-parent-digest` | Emails a class digest to guardians who opted in and consented | `RESEND_API_KEY`, `MAIL_FROM` |

## 7. Migrations 0006 and 0007, new functions
- `0006`: levels, shared (group) plans, taught-today notes, spaced revision, goals.
- `0007`: courses and certificates, moderated study groups, push helpers. Load the catalogue with the files in `paste/sql/seed-parts` (idempotent).
- `0008`: family view. A student creates up to 3 revocable 90-day links; `family_view(code)` (anon-callable) returns a weekly summary only: first name, streak, questions, subjects, attendance counts, course progress. Never messages, notes, group posts or surnames.
- New functions: `taught-today`, `notes-pack`, `send-push`, `revision-reminders`. Secrets: `VAPID_PUBLIC_KEY`, `VAPID_PRIVATE_KEY`, `VAPID_SUBJECT`, `CRON_SECRET` (see DEPLOY.md).
