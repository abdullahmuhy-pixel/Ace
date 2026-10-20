// Open sign-up for a private tutor, after-school teacher or tutoring centre. Rate-limited by IP.
// Creates the auth user (their real email), a tutor workspace (schools.kind = 'tutor') they own and run as
// school_admin, and optionally a first class with a join code to hand to students.
import { handler, HttpError, clientIp, throttle, clean, EMAIL_RE, audit } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  await throttle(admin, clientIp(req), "signup", 10, 60);

  const cc = clean(b.country_code, 2).toUpperCase();
  const first = clean(b.first_name), sur = clean(b.surname);
  const email = clean(b.email, 120).toLowerCase();
  const password = String(b.password ?? "");
  const workspace = clean(b.workspace, 120) || `${first} ${sur}'s classes`;
  const className = clean(b.class_name, 80), classLevel = clean(b.class_level, 40), subject = clean(b.subject, 80), exam = clean(b.exam, 80);

  if (!cc || !first || !sur) throw new HttpError(400, "Fill in every field.");
  if (!EMAIL_RE.test(email)) throw new HttpError(400, "Enter a valid email address. You sign in with it.");
  if (password.length < 8 || password.length > 72) throw new HttpError(400, "Password must be 8-72 characters.");
  if (b.consent !== true) throw new HttpError(400, "You must accept the Terms and Privacy Policy.");

  const { data: country } = await admin.from("countries").select("code").eq("code", cc).maybeSingle();
  if (!country) throw new HttpError(400, "Unknown country.");
  const { data: used } = await admin.from("profiles").select("id").eq("contact_email", email).limit(1);
  if (used?.length) throw new HttpError(409, "There is already an account with that email. Sign in instead.");

  const { data: created, error: cErr } = await admin.auth.admin.createUser({
    email, password, email_confirm: true, user_metadata: { role: "tutor", country: cc },
  });
  if (cErr || !created.user) throw new HttpError(409, "Could not create that account. Is the email already in use?");
  const uid = created.user.id;

  const { data: code } = await admin.rpc("gen_school_code", { prefix: workspace });
  const { data: ws, error: wErr } = await admin.from("schools")
    .insert({ name: workspace, country_code: cc, school_code: code, kind: "tutor" }).select("id").single();
  if (wErr || !ws) { await admin.auth.admin.deleteUser(uid); throw new HttpError(400, "Could not set up your workspace. Try again."); }

  const { error: pErr } = await admin.from("profiles").insert({
    id: uid, role: "school_admin", account_type: "tutor", school_id: ws.id, country_code: cc,
    first_name: first, surname: sur, contact_email: email,
    consent_at: new Date().toISOString(), consent_version: clean(b.consent_version, 20) || "2026-10",
  });
  if (pErr) {
    await admin.from("schools").delete().eq("id", ws.id);
    await admin.auth.admin.deleteUser(uid);
    throw new HttpError(400, "Could not create that account. Check your details and try again.");
  }
  await admin.from("schools").update({ owner_id: uid }).eq("id", ws.id);

  let joinCode: string | null = null;
  if (className) {
    const { data: cls } = await admin.from("classes")
      .insert({ school_id: ws.id, name: className, grade: classLevel || "Mixed", subject: subject || null, exam: exam || null })
      .select("join_code").single();
    joinCode = cls?.join_code ?? null;
  }
  await audit(admin, uid, "tutor.signup", ws.id, { cc });
  return { ok: true, login_email: email, workspace_id: ws.id, join_code: joinCode, country: cc };
});
