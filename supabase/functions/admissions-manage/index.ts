// School admins (and the Ace team) work through applications here.
//   status  { application_id, status, note?, message?, notify? }  -> logged change, optional email to the family
//   note    { application_id, note }                             -> internal note
//   doc_url { document_id }                                      -> 5-minute signed link to an uploaded file
//   enrol   { application_id, class_id, email_family? }          -> creates the student account, returns the temporary password once
//   purge   {}  (Ace team)                                       -> deletes declined/withdrawn applications older than a year, with their files
import { handler, HttpError, caller, clean, randomPassword, studentEmail, audit, throttle, sendEmail, SITE_URL } from "../_shared/util.ts";

const BUCKET = "admissions";
const esc = (s: unknown) => String(s ?? "").replace(/[&<>"]/g, (m) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[m]!));
const LABEL: Record<string, string> = { reviewing: "Under review", interview: "Interview", waitlisted: "Waiting list", accepted: "Accepted", declined: "Not offered a place" };

handler(async (req, b, admin) => {
  const { user, profile } = await caller(req, admin, ["school_admin", "platform_admin"]);
  await throttle(admin, user.id, "admissions", 300, 60);
  const action = clean(b.action, 20);

  if (action === "purge") {
    if (profile.role !== "platform_admin") throw new HttpError(403, "Only the Ace team can do that.");
    const { data: paths, error } = await admin.rpc("purge_old_applications", { p_days: 365 });
    if (error) throw new HttpError(400, error.message);
    const list = (paths ?? []).map((p: any) => typeof p === "string" ? p : p.purge_old_applications).filter(Boolean);
    for (let i = 0; i < list.length; i += 100) await admin.storage.from(BUCKET).remove(list.slice(i, i + 100));
    await audit(admin, user.id, "admissions.purge", null as any, { files: list.length });
    return { ok: true, files: list.length };
  }

  // everything else is about one application the caller may manage
  let appId = clean(b.application_id, 40);
  if (action === "doc_url") {
    const { data: d } = await admin.from("application_documents").select("application_id,path,file_name").eq("id", clean(b.document_id, 40)).maybeSingle();
    if (!d) throw new HttpError(404, "File not found.");
    appId = d.application_id;
    await load(appId);
    const { data: s } = await admin.storage.from(BUCKET).createSignedUrl(d.path, 300, { download: d.file_name });
    if (!s) throw new HttpError(404, "That file was never uploaded.");
    return { url: s.signedUrl };
  }
  const a = await load(appId);
  const family = a.guardian_email || a.applicant_email;

  if (action === "status") {
    const to = clean(b.status, 20), message = clean(b.message, 1500), note = clean(b.note, 2000);
    const { error } = await admin.rpc("application_transition", { p_app: a.id, p_to: to, p_actor: user.id, p_note: note || null, p_message: message || null });
    if (error) throw new HttpError(400, error.message);
    let emailed = false;
    if (b.notify === true && family && LABEL[to]) {
      const url = `${SITE_URL.replace(/\/$/, "")}/apply/?ref=${encodeURIComponent(a.reference)}`;
      await sendEmail(family, `${a.schools.name}: application ${a.reference} — ${LABEL[to]}`,
        `<p>There is an update on the application for <b>${esc(a.first_name)} ${esc(a.surname)}</b>: <b>${LABEL[to]}</b>.</p>${message ? `<p>${esc(message).replace(/\n/g, "<br>")}</p>` : ""}
         <p>See the full status with your reference and status code: <a href="${url}">${url}</a></p>`).then(() => emailed = true).catch(console.error);
    }
    await audit(admin, user.id, "admissions.status", a.id, { to });
    return { ok: true, status: to, emailed };
  }

  if (action === "note") {
    const { error } = await admin.rpc("application_set_note", { p_app: a.id, p_actor: user.id, p_note: clean(b.note, 2000) });
    if (error) throw new HttpError(400, error.message);
    return { ok: true };
  }

  if (action === "enrol") {
    if (a.status !== "accepted") throw new HttpError(400, "Accept the application before enrolling.");
    const { data: cls } = await admin.from("classes").select("id,school_id,grade").eq("id", clean(b.class_id, 40)).maybeSingle();
    if (!cls || cls.school_id !== a.school_id) throw new HttpError(400, "Choose a class in this school.");
    const base = (a.first_name[0] + a.surname).toLowerCase().replace(/[^a-z0-9]/g, "").slice(0, 22) || "student";
    let username = "", pw = "", uid = "", num = "";
    for (let i = 0; i < 6 && !uid; i++) {
      username = base + (i === 0 ? "" : Math.floor(100 + Math.random() * 900));
      const { data: t } = await admin.from("profiles").select("id").eq("username", username).maybeSingle();
      if (t) continue;
      pw = randomPassword();
      const { data: u, error } = await admin.auth.admin.createUser({ email: studentEmail(username), password: pw, email_confirm: true,
        user_metadata: { role: "student", must_change_password: true } });
      if (error || !u.user) continue;
      num = (await admin.rpc("gen_student_number", { cc: a.schools.country_code })).data as string;
      const { error: pErr } = await admin.from("profiles").insert({ id: u.user.id, role: "student", school_id: a.school_id, class_id: cls.id,
        country_code: a.schools.country_code, first_name: a.first_name, surname: a.surname, username, student_number: num,
        contact_email: a.applicant_email, class_level: cls.grade, exam_target: a.exam_target });
      if (pErr) { await admin.auth.admin.deleteUser(u.user.id); continue; }
      await admin.from("user_stats").insert({ user_id: u.user.id });
      uid = u.user.id;
    }
    if (!uid) throw new HttpError(500, "Could not create the student account. Try again.");
    const { error: eErr } = await admin.rpc("application_mark_enrolled", { p_app: a.id, p_student: uid, p_class: cls.id, p_actor: user.id });
    if (eErr) { await admin.auth.admin.deleteUser(uid); throw new HttpError(400, eErr.message); }
    if (a.guardian_email) await admin.from("guardians").insert({ student_id: uid, name: a.guardian_name, email: a.guardian_email, created_by: user.id });
    let emailed = false;
    if (b.email_family === true && family) {
      const login = `${SITE_URL.replace(/\/$/, "")}/login/`;
      await sendEmail(family, `${a.schools.name}: welcome, ${a.first_name}`,
        `<p>${esc(a.first_name)} ${esc(a.surname)} is enrolled at <b>${esc(a.schools.name)}</b>.</p>
         <p>Sign in to Ace at <a href="${login}">${login}</a><br>Username: <b>${username}</b><br>Temporary password: <b>${pw}</b><br>Student number: <b>${num}</b></p>
         <p>Ace asks for a new password at the first sign-in.</p>`).then(() => emailed = true).catch(console.error);
    }
    await audit(admin, user.id, "admissions.enrol", a.id, { student: uid });
    return { ok: true, username, temp_password: pw, student_number: num, emailed };
  }

  throw new HttpError(400, "Unknown action.");

  async function load(id: string) {
    const { data: a } = await admin.from("applications").select("*, schools(name,country_code)").eq("id", id).maybeSingle();
    if (!a) throw new HttpError(404, "Application not found.");
    if (profile.role !== "platform_admin" && !(profile.role === "school_admin" && profile.school_id === a.school_id))
      throw new HttpError(403, "That application belongs to another school.");
    return a;
  }
});
