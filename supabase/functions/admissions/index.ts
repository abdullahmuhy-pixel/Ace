// Public admissions: a family applies to a school without an account.
//   info     { school_code }                           -> what the school asks for
//   submit   { school_code, applicant..., documents }  -> reference, private status code, signed upload links
//   uploaded { reference, code, document_ids }         -> marks files that really arrived in storage
//   status   { reference, code }                       -> current status and the school's messages
//   withdraw { reference, code }
// Throttled per IP. The status code is shown once and emailed; only its SHA-256 hash is stored.
import { handler, HttpError, clientIp, throttle, clean, sha256, sendEmail, EMAIL_RE, SITE_URL } from "../_shared/util.ts";

const BUCKET = "admissions";
const TYPES: Record<string, string> = { "application/pdf": "pdf", "image/jpeg": "jpg", "image/png": "png" };
const MAX_FILES = 6, MAX_BYTES = 5 * 1024 * 1024;
const SAFE = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
const STATUS_TEXT: Record<string, string> = {
  submitted: "Received. The school has not looked at it yet.",
  reviewing: "The school is reviewing your application.",
  interview: "The school would like to meet the applicant.",
  waitlisted: "You are on the waiting list.",
  accepted: "Accepted. The school will contact you about enrolment.",
  declined: "The school was not able to offer a place.",
  withdrawn: "You withdrew this application.",
  enrolled: "Enrolled. The student's Ace account has been created.",
};
const esc = (s: unknown) => String(s ?? "").replace(/[&<>"]/g, (m) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[m]!));
const newCode = () => [...crypto.getRandomValues(new Uint32Array(10))].map((n) => SAFE[n % 32]).join("");
const normRef = (s: unknown) => clean(s, 20).toUpperCase().replace(/\s+/g, "");
const normCode = (s: unknown) => clean(s, 20).toUpperCase().replace(/[^A-Z0-9]/g, "");
const date = (s: unknown) => { const v = clean(s, 10); return /^\d{4}-\d{2}-\d{2}$/.test(v) ? v : null; };
const email = (s: unknown) => { const v = clean(s, 120).toLowerCase(); if (!v) return null; if (!EMAIL_RE.test(v)) throw new HttpError(400, "Check the email address."); return v; };
const phone = (s: unknown) => clean(s, 30).replace(/[^0-9+()\s-]/g, "") || null;

async function school(admin: any, code: unknown) {
  const c = clean(code, 20).toUpperCase();
  if (c.length < 4) throw new HttpError(400, "This link is missing the school code.");
  const { data: s } = await admin.from("schools")
    .select("id,name,country_code,region,active,admissions_open,admissions_note,admissions_grades,admissions_docs,admissions_email")
    .eq("school_code", c).maybeSingle();
  if (!s || !s.active) throw new HttpError(404, "We could not find that school.");
  return s;
}

async function mine(admin: any, b: any) {
  const ref = normRef(b.reference), code = normCode(b.code);
  if (!/^AP\d{2}-[A-Z0-9]{6}$/.test(ref) || code.length !== 10) throw new HttpError(400, "Enter the reference and the status code from your confirmation.");
  const { data: a } = await admin.from("applications").select("*, schools(name)").eq("reference", ref).maybeSingle();
  if (!a || a.code_hash !== await sha256(code)) throw new HttpError(404, "No application matches that reference and code.");
  return a;
}

handler(async (req, b, admin) => {
  const ip = clientIp(req), action = clean(b.action, 20);

  if (action === "info") {
    await throttle(admin, ip, "apply-info", 60, 60);
    const s = await school(admin, b.school_code);
    let grades: string[] = s.admissions_grades ?? [];
    if (!grades.length) { const { data: c } = await admin.from("classes").select("grade").eq("school_id", s.id); grades = [...new Set((c ?? []).map((x: any) => x.grade))].sort() as string[]; }
    return { name: s.name, region: s.region, country_code: s.country_code, open: !!s.admissions_open,
             note: s.admissions_note ?? "", grades, documents: s.admissions_docs ?? [] };
  }

  if (action === "submit") {
    await throttle(admin, ip, "apply-submit", 5, 60);
    const s = await school(admin, b.school_code);
    if (!s.admissions_open) throw new HttpError(400, "This school is not taking applications online right now.");
    if (b.consent !== true) throw new HttpError(400, "Tick the box to agree to the school using these details.");
    const first = clean(b.first_name), sur = clean(b.surname), grade = clean(b.grade_applied, 40);
    if (!first || !sur || !grade) throw new HttpError(400, "Enter the applicant's names and the class applied for.");
    const row: any = {
      school_id: s.id, first_name: first, surname: sur, grade_applied: grade, date_of_birth: date(b.date_of_birth),
      gender: clean(b.gender, 30) || null, start_term: clean(b.start_term, 40) || null, exam_target: clean(b.exam_target, 60) || null,
      previous_school: clean(b.previous_school, 120) || null, applicant_email: email(b.applicant_email), applicant_phone: phone(b.applicant_phone),
      address: clean(b.address, 300) || null, guardian_name: clean(b.guardian_name, 80) || null, guardian_relation: clean(b.guardian_relation, 40) || null,
      guardian_email: email(b.guardian_email), guardian_phone: phone(b.guardian_phone), message: clean(b.message, 1500) || null,
      consent_at: new Date().toISOString(),
    };
    if (!row.applicant_email && !row.guardian_email && !row.applicant_phone && !row.guardian_phone) throw new HttpError(400, "Give at least one email address or phone number so the school can reach you.");
    const docs: any[] = Array.isArray(b.documents) ? b.documents : [];
    if (docs.length > MAX_FILES) throw new HttpError(400, `Attach at most ${MAX_FILES} files.`);
    for (const d of docs) {
      if (!TYPES[d?.mime]) throw new HttpError(400, "Files must be PDF, JPG or PNG.");
      if (!(d.size > 0 && d.size <= MAX_BYTES)) throw new HttpError(400, "Each file must be 5 MB or smaller.");
    }
    const code = newCode();
    const { data: ref } = await admin.rpc("gen_application_ref");
    row.reference = ref; row.code_hash = await sha256(code);
    const { data: app, error } = await admin.from("applications").insert(row).select("id,reference").single();
    if (error || !app) { console.error(error); throw new HttpError(400, "Could not save the application. Check the details and try again."); }
    await admin.from("application_events").insert({ application_id: app.id, to_status: "submitted" });

    const uploads: any[] = [];
    for (const d of docs) {
      const id = crypto.randomUUID(), path = `${s.id}/${app.id}/${id}.${TYPES[d.mime]}`;
      const { error: dErr } = await admin.from("application_documents").insert({ id, application_id: app.id, kind: clean(d.kind, 60) || "Document",
        file_name: clean(d.name, 120) || "file", mime: d.mime, size_bytes: Math.round(d.size), path });
      if (dErr) continue;
      const { data: up } = await admin.storage.from(BUCKET).createSignedUploadUrl(path);
      if (up) uploads.push({ document_id: id, path, token: up.token, signed_url: up.signedUrl });
    }

    const to = row.guardian_email || row.applicant_email, statusUrl = `${SITE_URL.replace(/\/$/, "")}/apply/?ref=${encodeURIComponent(app.reference)}`;
    if (to) await sendEmail(to, `Application to ${s.name}: ${app.reference}`,
      `<p>Thank you. ${esc(s.name)} has received the application for <b>${esc(first)} ${esc(sur)}</b> (${esc(grade)}).</p>
       <p>Reference: <b>${app.reference}</b><br>Status code: <b>${code}</b></p>
       <p>Keep the status code private. Use both to check progress or withdraw: <a href="${statusUrl}">${statusUrl}</a></p>`).catch(console.error);
    const { data: admins } = await admin.from("profiles").select("contact_email").eq("school_id", s.id).eq("role", "school_admin");
    const notify = [s.admissions_email, ...(admins ?? []).map((x: any) => x.contact_email)].filter(Boolean);
    for (const n of [...new Set(notify)].slice(0, 5)) await sendEmail(n as string, `New application: ${first} ${sur} (${grade})`,
      `<p>A new application (${app.reference}) is waiting in Ace Teach, Admissions.</p>`).catch(console.error);
    return { reference: app.reference, code, uploads, emailed: !!to };
  }

  if (action === "uploaded") {
    await throttle(admin, ip, "apply-check", 40, 60);
    const a = await mine(admin, b);
    const ids: string[] = (Array.isArray(b.document_ids) ? b.document_ids : []).map((x: unknown) => clean(x, 40)).slice(0, MAX_FILES);
    const { data: docs } = await admin.from("application_documents").select("id,path").eq("application_id", a.id).in("id", ids.length ? ids : ["00000000-0000-0000-0000-000000000000"]);
    let ok = 0;
    for (const d of docs ?? []) {
      const dir = d.path.slice(0, d.path.lastIndexOf("/")), file = d.path.slice(d.path.lastIndexOf("/") + 1);
      const { data: list } = await admin.storage.from(BUCKET).list(dir, { search: file });
      if ((list ?? []).some((f: any) => f.name === file)) { await admin.from("application_documents").update({ uploaded_at: new Date().toISOString() }).eq("id", d.id); ok++; }
    }
    return { ok: true, uploaded: ok };
  }

  if (action === "status" || action === "withdraw") {
    await throttle(admin, ip, "apply-check", 40, 60);
    let a = await mine(admin, b);
    if (action === "withdraw") {
      const { error } = await admin.rpc("application_transition", { p_app: a.id, p_to: "withdrawn", p_actor: null, p_note: null, p_message: null });
      if (error) throw new HttpError(400, error.message);
      a = await mine(admin, b);
    }
    const { data: ev } = await admin.from("application_events").select("to_status,message,created_at").eq("application_id", a.id).order("created_at");
    const { data: docs } = await admin.from("application_documents").select("kind,file_name,uploaded_at").eq("application_id", a.id);
    return {
      reference: a.reference, school: a.schools?.name ?? "", name: `${a.first_name} ${a.surname}`, grade: a.grade_applied,
      status: a.status, status_text: STATUS_TEXT[a.status] ?? a.status, submitted_at: a.created_at, updated_at: a.updated_at,
      can_withdraw: !["withdrawn", "enrolled", "declined"].includes(a.status),
      timeline: (ev ?? []).map((e: any) => ({ status: e.to_status, message: e.message, at: e.created_at })),
      documents: (docs ?? []).map((d: any) => ({ kind: d.kind, name: d.file_name, received: !!d.uploaded_at })),
    };
  }

  throw new HttpError(400, "Unknown action.");
});
