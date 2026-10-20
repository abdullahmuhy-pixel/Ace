// Daily reminder: tells each student with a push subscription how many revision items are due.
// Called by a scheduler (see .github/workflows/reminders.yml) with the header x-cron-secret. Secrets: CRON_SECRET, VAPID_*.
import webpush from "npm:web-push@3.6.7";
import { handler, HttpError } from "../_shared/util.ts";

function timingSafeEqual(a: string, b: string) {
  if (a.length !== b.length) return false;
  let d = 0; for (let i = 0; i < a.length; i++) d |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return d === 0;
}

handler(async (req, _b, admin) => {
  const secret = Deno.env.get("CRON_SECRET");
  if (!secret || !timingSafeEqual(req.headers.get("x-cron-secret") ?? "", secret)) throw new HttpError(401, "Not allowed.");
  const pub = Deno.env.get("VAPID_PUBLIC_KEY"), priv = Deno.env.get("VAPID_PRIVATE_KEY");
  if (!pub || !priv) throw new HttpError(500, "Notifications are not set up yet.");
  webpush.setVapidDetails(Deno.env.get("VAPID_SUBJECT") ?? Deno.env.get("SITE_URL") ?? "https://example.com", pub, priv);
  const { data: due, error } = await admin.rpc("due_revision_counts");
  if (error) { console.error(error); throw new HttpError(500, "Could not read reminders."); }
  let sent = 0, failed = 0;
  for (const row of due ?? []) {
    const { data: subs } = await admin.from("push_subscriptions").select("endpoint,p256dh,auth").eq("user_id", row.user_id);
    const n = Number(row.due);
    const payload = JSON.stringify({ title: "Time to revise", body: n === 1 ? "1 topic is ready to review. It takes about 2 minutes." : `${n} topics are ready to review.`, url: "./" });
    await Promise.all((subs ?? []).map(async (s: any) => {
      try { await webpush.sendNotification({ endpoint: s.endpoint, keys: { p256dh: s.p256dh, auth: s.auth } }, payload); sent++; }
      catch (e: any) { failed++; if (e?.statusCode === 404 || e?.statusCode === 410) await admin.from("push_subscriptions").delete().eq("endpoint", s.endpoint); }
    }));
  }
  return { users: (due ?? []).length, sent, failed };
});
