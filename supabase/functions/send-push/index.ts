// Staff push notification to a class: {class_id, title, body}. Only the class's teachers, its school admin and platform admins can send.
// Secrets: VAPID_PUBLIC_KEY, VAPID_PRIVATE_KEY (generate once with `npx web-push generate-vapid-keys`), optional VAPID_SUBJECT (default SITE_URL).
import webpush from "npm:web-push@3.6.7";
import { handler, HttpError, caller, throttle, clean, SITE_URL, audit } from "../_shared/util.ts";

export function configure() {
  const pub = Deno.env.get("VAPID_PUBLIC_KEY"), priv = Deno.env.get("VAPID_PRIVATE_KEY");
  if (!pub || !priv) throw new HttpError(500, "Notifications are not set up yet.");
  webpush.setVapidDetails(Deno.env.get("VAPID_SUBJECT") ?? SITE_URL, pub, priv);
}

handler(async (req, b, admin) => {
  const { user } = await caller(req, admin, ["teacher", "subject_teacher", "school_admin", "platform_admin"]);
  await throttle(admin, user.id, "push", 10, 60);
  const classId = clean(b.class_id, 40), title = clean(b.title, 80), body = clean(b.body, 200);
  if (!classId || !title) throw new HttpError(400, "A class and a title are required.");
  const { data: ok } = await admin.rpc("staff_can_reach", { p_staff: user.id, p_class: classId });
  if (ok !== true) throw new HttpError(403, "You cannot send to that class.");
  configure();
  const { data: studs } = await admin.from("profiles").select("id").eq("class_id", classId).eq("role", "student");
  const ids = (studs ?? []).map((s: any) => s.id);
  if (!ids.length) return { sent: 0, failed: 0 };
  const { data: subs } = await admin.from("push_subscriptions").select("endpoint,p256dh,auth").in("user_id", ids);
  let sent = 0, failed = 0;
  const payload = JSON.stringify({ title, body, url: "./" });
  await Promise.all((subs ?? []).map(async (s: any) => {
    try { await webpush.sendNotification({ endpoint: s.endpoint, keys: { p256dh: s.p256dh, auth: s.auth } }, payload); sent++; }
    catch (e: any) { failed++; if (e?.statusCode === 404 || e?.statusCode === 410) await admin.from("push_subscriptions").delete().eq("endpoint", s.endpoint); }
  }));
  await audit(admin, user.id, "push_class", classId, { sent, failed });
  return { sent, failed };
});
