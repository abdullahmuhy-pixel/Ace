// Teacher / school admin: create many student accounts at once. Returns the temporary
// passwords ONCE, to print and hand out. Students are asked to change them at first login.
import { handler, HttpError, caller, clean, randomPassword, studentEmail, audit, throttle } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const { user, profile } = await caller(req, admin, ["teacher", "subject_teacher", "school_admin", "platform_admin"]);
  await throttle(admin, user.id, "bulk", 15, 60);   // up to 3,000 accounts an hour per teacher
  const list: any[] = Array.isArray(b.students) ? b.students : [];
  if (!list.length || list.length > 200) throw new HttpError(400, "Send between 1 and 200 students.");

  const { data: cls } = await admin.from("classes").select("id,school_id,grade").eq("id", clean(b.class_id, 40)).maybeSingle();
  if (!cls) throw new HttpError(404, "Class not found.");
  if (profile.role !== "platform_admin" && cls.school_id !== profile.school_id)
    throw new HttpError(403, "That class belongs to another school.");
  const { data: school } = await admin.from("schools").select("country_code").eq("id", cls.school_id).single();

  const results: any[] = [];
  for (const s of list) {
    const first = clean(s.first_name), sur = clean(s.surname);
    if (!first || !sur) { results.push({ first_name: first, surname: sur, error: "Missing name" }); continue; }
    const base = (first[0] + sur).toLowerCase().replace(/[^a-z0-9]/g, "").slice(0, 22) || "student";
    let username = "", ok = false, pw = "", num: string | null = null, uid = "";
    for (let i = 0; i < 6 && !ok; i++) {
      username = base + (i === 0 ? "" : Math.floor(100 + Math.random() * 900));
      const { data: t } = await admin.from("profiles").select("id").eq("username", username).maybeSingle();
      if (t) continue;
      pw = randomPassword();
      const { data: u, error } = await admin.auth.admin.createUser({
        email: studentEmail(username), password: pw, email_confirm: true,
        user_metadata: { role: "student", must_change_password: true },
      });
      if (error || !u.user) continue;
      const r = await admin.rpc("gen_student_number", { cc: school!.country_code });
      num = r.data as string;
      const { error: pErr } = await admin.from("profiles").insert({
        id: u.user.id, role: "student", school_id: cls.school_id, class_id: cls.id,
        country_code: school!.country_code, first_name: first, surname: sur, username,
        student_number: num, contact_email: clean(s.email, 120).toLowerCase() || null,
        class_level: cls.grade, exam_target: clean(b.exam_target) || null,
      });
      if (pErr) { await admin.auth.admin.deleteUser(u.user.id); continue; }
      await admin.from("user_stats").insert({ user_id: u.user.id });
      uid = u.user.id; ok = true;
    }
    results.push(ok ? { first_name: first, surname: sur, username, student_number: num, temp_password: pw }
                    : { first_name: first, surname: sur, error: "Could not create" });
  }
  await audit(admin, user.id, "students.bulk_create", cls.id, { count: results.filter((r) => !r.error).length });
  return { ok: true, results };
});
