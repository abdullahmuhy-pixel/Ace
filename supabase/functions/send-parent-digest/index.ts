// Weekly progress email to guardians of one class. Called by a teacher or school admin from their dashboard
// (or by a scheduled job with a staff token). Only guardians who opted in AND have a recorded consent date get mail.
// Secrets: RESEND_API_KEY, MAIL_FROM.
import { handler, HttpError, caller, sendEmail, throttle } from "../_shared/util.ts";

const esc = (s: unknown) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]!));

handler(async (req, b, admin) => {
  const { user, profile } = await caller(req, admin, ["teacher", "subject_teacher", "school_admin", "platform_admin"]);
  await throttle(admin, user.id, "digest", 3, 60);
  const classId = String(b.class_id ?? "");
  if (!classId) throw new HttpError(400, "Choose a class.");

  const { data: cls } = await admin.from("classes").select("id,name,school_id").eq("id", classId).maybeSingle();
  if (!cls) throw new HttpError(404, "Class not found.");
  if (profile.role !== "platform_admin") {
    if (cls.school_id !== profile.school_id) throw new HttpError(403, "That is not your school.");
    if (profile.role !== "school_admin") {
      const { data: t } = await admin.from("teacher_subjects").select("class_id").eq("teacher_id", user.id).eq("class_id", classId).limit(1);
      if (!t?.length) throw new HttpError(403, "You do not teach this class.");
    }
  }

  const { data: students } = await admin.from("profiles").select("id,first_name").eq("class_id", classId).eq("role", "student");
  const ids = (students ?? []).map((s: any) => s.id);
  if (!ids.length) return { sent: 0, skipped: 0 };
  const { data: gs } = await admin.from("guardians").select("student_id,email,name").in("student_id", ids)
    .eq("digest_opt_in", true).not("consent_at", "is", null).limit(200);
  const since = new Date(Date.now() - 7 * 86_400_000).toISOString();
  const day = since.slice(0, 10);
  const { data: att } = await admin.from("quiz_attempts").select("user_id,total,correct").in("user_id", ids).gte("created_at", since);
  const { data: st } = await admin.from("user_stats").select("user_id,streak,xp").in("user_id", ids);
  const { data: ab } = await admin.from("attendance").select("student_id,status").eq("class_id", classId).gte("day", day);

  let sent = 0, failed = 0;
  for (const g of gs ?? []) {
    const stu = students!.find((s: any) => s.id === g.student_id)!;
    const a = (att ?? []).filter((x: any) => x.user_id === g.student_id);
    const q = a.reduce((n: number, x: any) => n + x.total, 0), c = a.reduce((n: number, x: any) => n + x.correct, 0);
    const s = (st ?? []).find((x: any) => x.user_id === g.student_id);
    const days = (ab ?? []).filter((x: any) => x.student_id === g.student_id);
    const present = days.filter((x: any) => x.status === "present" || x.status === "late").length;
    const html = `<p>Hello${g.name ? " " + esc(g.name) : ""},</p>
<p>Here is ${esc(stu.first_name)}'s week on Ace Education (${esc(cls.name)}).</p>
<ul><li>Questions answered: <b>${q}</b>${q ? `, ${Math.round((100 * c) / q)}% correct` : ""}</li>
<li>Current study streak: <b>${s?.streak ?? 0}</b> days</li>${days.length ? `<li>Attendance: <b>${present} of ${days.length}</b> days present</li>` : ""}</ul>
<p>A few minutes of practice each day works better than a long session once a week.</p>
<p style="color:#666;font-size:12px">You receive this because you agreed to progress emails for ${esc(stu.first_name)}. Ask the school to stop them at any time.</p>`;
    try { await sendEmail(g.email, `${stu.first_name}'s week on Ace Education`, html); sent++; } catch (e) { console.error(e); failed++; }
  }
  return { sent, failed, skipped: ids.length - new Set((gs ?? []).map((g: any) => g.student_id)).size };
});
