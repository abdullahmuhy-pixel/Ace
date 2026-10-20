# Linking Supabase to GitHub

After this, a new migration pushed to `main` (for example `supabase/migrations/0020_something.sql`) is applied to the database automatically. You no longer paste each one into the SQL Editor.

## Step 1: record the migrations you already ran (once)
Open Supabase → SQL Editor, paste `paste/sql/migrations/repair_migration_history.sql`, and click Run.
It should list 19 rows, 0001 to 0019. Run it **after** 0017, 0018 and 0019 are in your database.
Without this step, Supabase would try to run 0001 again and fail.

## Step 2: connect the repository
Supabase dashboard → Project Settings → Integrations → GitHub → Connect.
- Repository: `abdullahmuhy-pixel/Ace`
- Supabase directory: `supabase`
- Production branch: `main`, with "Deploy to production" turned on
- Leave "Automatic branching" off. Preview branches are a paid feature, and you don't need them.

## Step 3: check it worked
Push any small change under `supabase/` and open Integrations → GitHub. The latest run should be green.

## Status
Linked on 2026-10-20. Migrations 0001 to 0019 are recorded as applied.

## Rules from now on
- Number new migrations 0020, 0021 and so on. Never edit a migration that has already run; add a new one instead.
- Secrets stay in Edge Functions → Secrets. Never put them in this folder: the repository is public.
- If edge functions don't update automatically, deploy them from the dashboard as you do now.
