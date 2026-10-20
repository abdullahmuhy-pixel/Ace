// Finish sign-up for someone who signed in with Google (or another OAuth provider).
// Supabase creates the auth user during the OAuth round trip; this creates the matching student profile,
// which every other part of Ace expects. Safe to call twice: an existing profile is returned untouched.
import { handler, HttpError, clientIp, throttle, clean, audit } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  await throttle(admin, clientIp(req), "oauth-profile", 20, 60);

  const auth = req.headers.get("authorization") ?? "";
  if (!auth.startsWith("Bearer ")) throw new HttpError(401, "Sign in first.");
  const { data: got, error } = await admin.auth.getUser(auth.slice(7));
  const user = got?.user;
  if (error || !user) throw new HttpError(401, "Your session has expired. Sign in again.");

  const { data: existing } = await admin.from("profiles").select("id,country_code,first_name,role").eq("id", user.id).maybeSingle();
  if (existing) return { ok: true, existing: true, country: existing.country_code, first_name: existing.first_name, role: existing.role };

  const cc = clean(b.country_code, 2).toUpperCase();
  const first = clean(b.first_name), sur = clean(b.surname);
  if (!cc || !first || !sur) throw new HttpError(400, "Fill in every field.");
  if (b.consent !== true) throw new HttpError(400, "You must accept the Terms and Privacy Policy.");
  const { data: country } = await admin.from("countries").select("code").eq("code", cc).maybeSingle();
  if (!country) throw new HttpError(400, "Unknown country.");

  // A readable, unique username from the email address, so the student can also be found by teachers later.
  const base = (String(user.email ?? first).split("@")[0].toLowerCase().replace(/[^a-z0-9._-]/g, "").slice(0, 22) || "student").padEnd(3, "0");
  let username = base;
  for (let i = 0; i < 8; i++) {
    const { data: taken } = await admin.from("profiles").select("id").eq("username", username).maybeSingle();
    if (!taken) break;
    username = `${base}${Math.floor(1000 + Math.random() * 9000)}`;
  }

  // Teachers and tutors who used Google get their own workspace instead of a student profile.
  if (b.account_type === "tutor") {
    const workspace = clean(b.workspace, 120) || `${first} ${sur}'s classes`;
    const { data: code } = await admin.rpc("gen_school_code", { prefix: workspace });
    const { data: ws, error: wErr } = await admin.from("schools")
      .insert({ name: workspace, country_code: cc, school_code: code, kind: "tutor", owner_id: null }).select("id").single();
    if (wErr || !ws) throw new HttpError(400, "Could not set up your workspace. Try again.");
    const { error: tErr } = await admin.from("profiles").insert({
      id: user.id, role: "school_admin", account_type: "tutor", school_id: ws.id, country_code: cc,
      first_name: first, surname: sur, contact_email: user.email ?? null,
      consent_at: new Date().toISOString(), consent_version: clean(b.consent_version, 20) || "2026-10",
    });
    if (tErr) { await admin.from("schools").delete().eq("id", ws.id); throw new HttpError(400, "Could not finish setting up that account."); }
    await admin.from("schools").update({ owner_id: user.id }).eq("id", ws.id);
    await audit(admin, user.id, "tutor.signup.oauth", ws.id, { cc });
    return { ok: true, existing: false, country: cc, first_name: first, role: "school_admin", account_type: "tutor" };
  }

  const { data: num } = await admin.rpc("gen_student_number", { cc });
  const { error: pErr } = await admin.from("profiles").insert({
    id: user.id, role: "student", school_id: null, class_id: null,
    country_code: cc, first_name: first, surname: sur, username,
    student_number: num, contact_email: user.email ?? null,
    class_level: clean(b.class_level) || null, exam_target: clean(b.exam_target) || null,
    consent_at: new Date().toISOString(), consent_version: clean(b.consent_version, 20) || "2026-10",
  });
  if (pErr) throw new HttpError(400, "Could not finish setting up that account. Check your details and try again.");
  await admin.from("user_stats").insert({ user_id: user.id });
  await audit(admin, user.id, "student.signup.oauth", cc, { provider: user.app_metadata?.provider ?? "oauth" });
  return { ok: true, existing: false, country: cc, first_name: first, role: "student", username, student_number: num };
});
