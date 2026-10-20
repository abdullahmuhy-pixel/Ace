// A teacher, tutor or school admin resets the password of a student account they manage
// (username accounts created by a school or tutor, which have no real email). Returns a new temporary password.
import { handler, HttpError, caller, randomPassword, STUDENT_DOMAIN, audit } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const { user, profile } = await caller(req, admin, ["teacher", "subject_teacher", "school_admin", "platform_admin"]);
  const sid = String(b.student_id ?? "");
  if (!/^[0-9a-f-]{36}$/i.test(sid)) throw new HttpError(400, "Choose a student.");
  const { data: st } = await admin.from("profiles").select("id,role,school_id,class_id,first_name").eq("id", sid).maybeSingle();
  if (!st || st.role !== "student") throw new HttpError(404, "Student not found.");

  // Only accounts that belong to the caller's own school or workspace (not independent learners who joined with a code).
  let allowed = profile.role === "platform_admin" || (st.school_id && st.school_id === profile.school_id && profile.role === "school_admin");
  if (!allowed && st.class_id && st.school_id === profile.school_id) {
    const { data: t } = await admin.from("teacher_subjects").select("class_id").eq("teacher_id", user.id).eq("class_id", st.class_id).limit(1);
    allowed = !!t?.length;
  }
  if (!allowed) throw new HttpError(403, "You can only reset passwords for students your school or centre created.");

  const { data: au } = await admin.auth.admin.getUserById(sid);
  if (!au?.user?.email?.endsWith("@" + STUDENT_DOMAIN)) throw new HttpError(400, "This student signed up with their own email. They can reset it from the sign-in page.");
  const pw = randomPassword();
  const { error } = await admin.auth.admin.updateUserById(sid, { password: pw, user_metadata: { ...(au.user.user_metadata ?? {}), must_change_password: true } });
  if (error) throw new HttpError(400, "Could not reset that password.");
  await audit(admin, user.id, "student.password_reset", sid);
  return { ok: true, temp_password: pw };
});
