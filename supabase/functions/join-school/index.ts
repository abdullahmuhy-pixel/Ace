// Student self-registration with a school code the teacher handed out.
import { handler, HttpError, clientIp, throttle, clean, studentEmail, USERNAME_RE, EMAIL_RE, audit } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  await throttle(admin, clientIp(req), "join", 20, 60);

  const code = clean(b.school_code, 20).toUpperCase();
  const first = clean(b.first_name), sur = clean(b.surname);
  const username = clean(b.username, 30).toLowerCase();
  const email = clean(b.email, 120).toLowerCase();
  const password = String(b.password ?? "");

  if (!code || !first || !sur || !username) throw new HttpError(400, "Fill in every field.");
  if (!USERNAME_RE.test(username)) throw new HttpError(400, "Username: 3-30 letters, numbers, dot, dash or underscore.");
  if (password.length < 8 || password.length > 72) throw new HttpError(400, "Password must be 8-72 characters.");
  if (email && !EMAIL_RE.test(email)) throw new HttpError(400, "That email address looks wrong.");
  if (b.consent !== true) throw new HttpError(400, "You must accept the Terms and Privacy Policy.");

  const { data: school } = await admin.from("schools").select("id,country_code,active").eq("school_code", code).maybeSingle();
  if (!school || !school.active) throw new HttpError(404, "We could not find that school code. Check it with your teacher.");

  const { data: taken } = await admin.from("profiles").select("id").eq("username", username).maybeSingle();
  if (taken) throw new HttpError(409, "That username is taken. Try another.");

  let classId: string | null = null;
  if (b.class_level) {
    const { data: cls } = await admin.from("classes").select("id").eq("school_id", school.id).eq("grade", clean(b.class_level)).limit(1);
    classId = cls?.[0]?.id ?? null;
  }

  const authEmail = studentEmail(username);
  const { data: created, error: cErr } = await admin.auth.admin.createUser({
    email: authEmail, password, email_confirm: true,
    user_metadata: { role: "student", country: school.country_code },
  });
  if (cErr || !created.user) throw new HttpError(409, "Could not create that account. Try a different username.");

  const { data: num } = await admin.rpc("gen_student_number", { cc: school.country_code });
  const { error: pErr } = await admin.from("profiles").insert({
    id: created.user.id, role: "student", school_id: school.id, class_id: classId,
    country_code: school.country_code, first_name: first, surname: sur, username,
    student_number: num, contact_email: email || null,
    class_level: clean(b.class_level) || null, exam_target: clean(b.exam_target) || null,
    consent_at: new Date().toISOString(), consent_version: clean(b.consent_version, 20) || "2026-10",
  });
  if (pErr) {
    await admin.auth.admin.deleteUser(created.user.id);   // no orphan auth users
    throw new HttpError(400, "Could not create that account. Check your details and try again.");
  }
  await admin.from("user_stats").insert({ user_id: created.user.id });
  await audit(admin, created.user.id, "student.join", school.id);
  return { ok: true, login_email: authEmail, student_number: num, country: school.country_code };
});
