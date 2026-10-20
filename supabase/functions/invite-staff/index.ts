// School admin: invite a teacher or subject teacher to their own school.
import { handler, HttpError, caller, clean, EMAIL_RE, SITE_URL, audit } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const { user, profile } = await caller(req, admin, ["school_admin", "platform_admin"]);
  const schoolId = profile.role === "platform_admin" ? clean(b.school_id, 40) : profile.school_id;
  if (!schoolId) throw new HttpError(400, "Which school?");
  const role = b.role === "subject_teacher" ? "subject_teacher" : "teacher";
  const email = clean(b.email, 120).toLowerCase();
  if (!EMAIL_RE.test(email) || !clean(b.first_name) || !clean(b.surname)) throw new HttpError(400, "Name and email are required.");

  const { data: school } = await admin.from("schools").select("country_code").eq("id", schoolId).single();
  if (!school) throw new HttpError(404, "School not found.");

  const { data: inv, error } = await admin.auth.admin.inviteUserByEmail(email, { redirectTo: SITE_URL });
  if (error || !inv.user) throw new HttpError(400, "Could not invite that person. Is the email already in use?");
  const { error: pErr } = await admin.from("profiles").insert({
    id: inv.user.id, role, school_id: schoolId, country_code: school.country_code,
    first_name: clean(b.first_name), surname: clean(b.surname), contact_email: email,
  });
  if (pErr) { await admin.auth.admin.deleteUser(inv.user.id); throw new HttpError(400, "Could not save that teacher."); }

  // optional class/subject assignments (only for classes in this school)
  const wanted: { class_id: string; subject: string }[] = Array.isArray(b.assignments) ? b.assignments.slice(0, 40) : [];
  if (wanted.length) {
    const { data: ok } = await admin.from("classes").select("id").eq("school_id", schoolId).in("id", wanted.map((w) => w.class_id));
    const allowed = new Set((ok ?? []).map((c) => c.id));
    const rows = wanted.filter((w) => allowed.has(w.class_id) && clean(w.subject, 60))
      .map((w) => ({ teacher_id: inv.user!.id, class_id: w.class_id, subject: clean(w.subject, 60) }));
    if (rows.length) await admin.from("teacher_subjects").insert(rows);
  }
  await audit(admin, user.id, "staff.invite", inv.user.id, { role });
  return { ok: true, user_id: inv.user.id };
});
