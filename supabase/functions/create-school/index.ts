// Platform admin only: onboard a school and invite its first admin.
import { handler, HttpError, caller, clean, EMAIL_RE, SITE_URL, audit } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const { user } = await caller(req, admin, ["platform_admin"]);
  const name = clean(b.name, 120), cc = clean(b.country_code, 2).toUpperCase();
  const email = clean(b.admin_email, 120).toLowerCase();
  if (!name || !cc || !EMAIL_RE.test(email) || !clean(b.admin_first) || !clean(b.admin_surname))
    throw new HttpError(400, "Name, country and the admin's name and email are required.");
  const { data: country } = await admin.from("countries").select("code").eq("code", cc).maybeSingle();
  if (!country) throw new HttpError(400, "Unknown country code.");

  const { data: code } = await admin.rpc("gen_school_code", { prefix: name });
  const { data: school, error } = await admin.from("schools")
    .insert({ name, country_code: cc, region: clean(b.region, 80) || null, school_code: code }).select().single();
  if (error) throw new HttpError(400, "Could not create the school.");

  const { data: inv, error: iErr } = await admin.auth.admin.inviteUserByEmail(email, { redirectTo: SITE_URL });
  if (iErr || !inv.user) {
    await admin.from("schools").delete().eq("id", school.id);
    throw new HttpError(400, "Could not invite that admin. Is the email already in use?");
  }
  await admin.from("profiles").insert({
    id: inv.user.id, role: "school_admin", school_id: school.id, country_code: cc,
    first_name: clean(b.admin_first), surname: clean(b.admin_surname), contact_email: email,
  });
  await audit(admin, user.id, "school.create", school.id, { name, cc });
  return { ok: true, school_id: school.id, school_code: code };
});
