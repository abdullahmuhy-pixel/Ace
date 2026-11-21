// Fee reminders for school admins.
//   send   { student_ids: [], note? }  -> emails each overdue student's guardians: what is overdue, the balance, how to
//                                        pay (the school's fee note) and the family link to the full statement.
//                                        Families reminded in the last 7 days are skipped unless force is true.
//   copied { student_ids: [] }         -> logs reminders the admin sent by WhatsApp or SMS from the copied text.
// Without RESEND_API_KEY no email is sent: the result says mail_off and the page offers the text to copy instead.
import { createClient } from "npm:@supabase/supabase-js@2";
import { handler, HttpError, caller, sendEmail, throttle, clean, SUPABASE_URL, SITE_URL, audit } from "../_shared/util.ts";

const esc = (s: unknown) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]!));
const money = (v: unknown, c: string) => `${c} ${Number(v ?? 0).toLocaleString("en-GB", { maximumFractionDigits: 2 })}`;

handler(async (req, b, admin) => {
  const { user, profile } = await caller(req, admin, ["school_admin"]);
  await throttle(admin, user.id, "fee-reminders", 20, 60);
  // the list comes from the database as the caller, so it only ever covers their own school
  const asUser = createClient(SUPABASE_URL, Deno.env.get("SUPABASE_ANON_KEY")!, { global: { headers: { Authorization: req.headers.get("authorization")! } }, auth: { persistSession: false } });
  const { data: list, error } = await asUser.rpc("fee_reminder_list");
  if (error) throw new HttpError(400, error.message);
  const want = new Set((Array.isArray(b.student_ids) ? b.student_ids : []).map((x: unknown) => clean(x, 40)));
  const rows = (list ?? []).filter((r: any) => want.has(r.student_id));
  if (!rows.length) throw new HttpError(400, "Choose at least one student who owes fees.");
  if (rows.length > 300) throw new HttpError(400, "Send at most 300 reminders at a time.");

  if (clean(b.action, 10) === "copied") {
    await admin.from("fee_reminders").insert(rows.map((r: any) => ({ school_id: profile.school_id, student_id: r.student_id, channel: "copied", overdue: r.overdue, currency: r.currency, sent_by: user.id })));
    return { ok: true, logged: rows.length };
  }
  if (!Deno.env.get("RESEND_API_KEY")) return { ok: false, mail_off: true };

  const { data: school } = await admin.from("schools").select("name,fee_note").eq("id", profile.school_id).single();
  const note = clean(b.note, 600), week = Date.now() - 7 * 86_400_000, base = SITE_URL.replace(/\/$/, "");
  let sent = 0, skipped = 0, noEmail = 0;
  for (const r of rows) {
    if (b.force !== true && r.last_reminded && new Date(r.last_reminded).getTime() > week) { skipped++; continue; }
    const to = [...new Set((r.guardians ?? []).map((g: any) => g.email).filter(Boolean))] as string[];
    if (!to.length) { noEmail++; continue; }
    // reuse the school's family link for this student, or make one (as the admin, so the permission check applies)
    const { data: links } = await admin.from("family_links").select("code").eq("student_id", r.student_id).not("created_by", "is", null)
      .is("revoked_at", null).gt("expires_at", new Date().toISOString()).limit(1);
    let code = links?.[0]?.code;
    if (!code) { const { data: c } = await asUser.rpc("school_family_link", { p_student: r.student_id, p_label: "Fee reminders" }); code = c; }
    const link = code ? `${base}/family/?c=${code}` : "";
    const html = `<p>Dear parent or guardian,</p>
<p>This is a reminder from <b>${esc(school?.name)}</b> that <b>${money(r.overdue, r.currency)}</b> of school fees for <b>${esc(r.name)}</b>${r.class ? " (" + esc(r.class) + ")" : ""} is now due. The total balance on the account is ${money(r.balance, r.currency)}.</p>
${note ? `<p>${esc(note).replace(/\n/g, "<br>")}</p>` : ""}${school?.fee_note ? `<p style="border:1px solid #ccc;padding:8px">${esc(school.fee_note).replace(/\n/g, "<br>")}</p>` : ""}
${link ? `<p>See the full statement, receipts and term reports: <a href="${link}">${link}</a></p>` : ""}
<p>If you have already paid, thank you, and please ignore this message.</p>`;
    let ok = 0;
    for (const t of to.slice(0, 3)) { try { await sendEmail(t, `${school?.name}: school fees for ${r.name}`, html); ok++; } catch (e) { console.error(e); } }
    if (ok) { sent++; await admin.from("fee_reminders").insert({ school_id: profile.school_id, student_id: r.student_id, channel: "email", sent_to: to.slice(0, 3).join(", "), overdue: r.overdue, currency: r.currency, sent_by: user.id }); }
  }
  await audit(admin, user.id, "fees.reminders", profile.school_id, { sent, skipped, noEmail });
  return { ok: true, sent, skipped, no_email: noEmail };
});
