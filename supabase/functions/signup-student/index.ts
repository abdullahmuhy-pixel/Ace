// Open self sign-up for an individual student (no school). Rate-limited by IP.
import { handler, HttpError, clientIp, throttle, clean, studentEmail, USERNAME_RE, EMAIL_RE, audit } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  await throttle(admin, clientIp(req), "signup", 10, 60);

  const cc = clean(b.country_code, 2).toUpperCase();
  const first = clean(b.first_name), sur = clean(b.surname);
  const username = clean(b.username, 30).toLowerCase();
  const email = clean(b.email, 120).toLowerCase();
  const password = String(b.password ?? "");

  if (!cc || !first || !sur || !username) throw new HttpError(400, "Fill in every field.");
  if (!USERNAME_RE.test(username)) throw new HttpError(400, "Username: 3-30 letters, numbers, dot, dash or underscore.");
  if (password.length < 8 || password.length > 72) throw new HttpError(400, "Password must be 8-72 characters.");
  if (!EMAIL_RE.test(email)) throw new HttpError(400, "Enter a valid email address. We use it if you forget your password.");
  if (b.consent !== true) throw new HttpError(400, "You must accept the Terms and Privacy Policy.");

  const { data: country } = await admin.from("countries").select("code").eq("code", cc).maybeSingle();
  if (!country) throw new HttpError(400, "Unknown country.");

  const { data: taken } = await admin.from("profiles").select("id").eq("username", username).maybeSingle();
  if (taken) throw new HttpError(409, "That username is taken. Try another.");

  const authEmail = studentEmail(username);
  const { data: created, error: cErr } = await admin.auth.admin.createUser({
    email: authEmail, password, email_confirm: true,
    user_metadata: { role: "student", country: cc },
  });
  if (cErr || !created.user) throw new HttpError(409, "Could not create that account. Try a different username.");

  const { data: num } = await admin.rpc("gen_student_number", { cc });
  const { error: pErr } = await admin.from("profiles").insert({
    id: created.user.id, role: "student", school_id: null, class_id: null,
    country_code: cc, first_name: first, surname: sur, username,
    student_number: num, contact_email: email,
    class_level: clean(b.class_level) || null, exam_target: clean(b.exam_target) || null,
    consent_at: new Date().toISOString(), consent_version: clean(b.consent_version, 20) || "2026-10",
  });
  if (pErr) {
    await admin.auth.admin.deleteUser(created.user.id);
    throw new HttpError(400, "Could not create that account. Check your details and try again.");
  }
  await admin.from("user_stats").insert({ user_id: created.user.id });
  await audit(admin, created.user.id, "student.signup", cc);
  return { ok: true, login_email: authEmail, student_number: num, country: cc };
});
