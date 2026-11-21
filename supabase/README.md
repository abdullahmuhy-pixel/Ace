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

## Admissions (migration 0044)
Families apply to a school online at `/apply/?s=<SCHOOL CODE>` without an account; school admins review, decide and enrol
in Ace Teach, **Admissions**.
1. Run `0044_admissions.sql`. On Supabase it also creates the private storage bucket `admissions` (PDF, JPG, PNG, 5 MB).
   If the bucket is missing, create it in Storage with those limits and keep it private.
2. Deploy the functions: `supabase functions deploy admissions admissions-manage` (both are in `config.toml` with
   `verify_jwt = false`; `admissions-manage` checks the caller itself, `admissions` is public and throttled per IP).
3. `RESEND_API_KEY` and `MAIL_FROM` send the confirmation, decision and welcome emails; `SITE_URL` builds the links in them.
4. Personal data: declined and withdrawn applications should go after a year. An Ace platform admin calls
   `admissions-manage` with `{ "action": "purge" }` (deletes the rows and the files); schedule it monthly if you can.
Behaviour tests: `supabase/tests/44_admissions_test.sql` (41 checks: who can read what, the status rules, enrolment, purge).

## Student records (migration 0046)
Admission numbers per school (prefix, optional year, running number; set in Ace Teach, Settings), enrolment status
(active, suspended, withdrawn, transferred, graduated) with a logged history, and a record card per student
(`student_records`). Leavers drop out of their classes and stop counting towards seats; their record stays.
`move_students()` replaces direct updates of `profiles.class_id`, which the column grants never allowed.
Tests: `supabase/tests/46_student_records_test.sql` (36 checks).

## Fee statements (migration 0047)
Itemised term invoices (`fee_items`, negative lines for discounts and bursaries), instalment plans (`fee_instalments`)
and receipted payments (`fee_payments`, never edited or deleted, only voided with a reason). `fees.amount` and
`fees.paid` are kept by triggers and cannot be edited directly. School admins call `bill_students`, `record_payment`
and `void_payment`; `fee_overdue` gives what is due now. Ace Teach, Fees: invoices, who owes, receipts log, billing,
statements and receipts to print. Tests: `supabase/tests/47_fee_statements_test.sql` (35 checks).

## Academic record and transcripts (migration 0048)
`academic_terms` (per school, with dates), `term_results` (score out of 100 and grade per subject; compiled from the
gradebook by `compile_term`, or entered by hand) and `term_reports` (average, position, attendance, comments).
`publish_term` makes a class's reports visible to its students and locks them. Grade bands per school
(`schools.grade_bands`, default A–F). `transcripts`: students ask with `request_transcript`, admins
`issue_transcript` (frozen snapshot of published reports, code TR + 10 characters) or decline/withdraw with
`decide_transcript`; anyone checks a code with `verify_transcript` on /verify/. Students see it all in the app,
Tools, My results. Tests: `supabase/tests/48_academic_record_test.sql` (42 checks).

## School calendar and behaviour log (migration 0049)
`school_events`: events, holidays, exam weeks, closures, meetings and deadlines per school, for everyone or staff only
(school admins edit; students see the everyone items in the app). `behaviour_entries`: merits, concerns and incidents
by the student's teachers or school admins (teachers can fix or delete their own entry for 24 hours), and welfare
notes that only school admins can read and that are never shared. Entries marked for the family show in the
student's app. `class_behaviour()` summarises a class over a period. Tests: `supabase/tests/49_calendar_behaviour_test.sql` (27 checks).
