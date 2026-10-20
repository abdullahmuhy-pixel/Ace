// Step 2 of password reset: check the code and set the new password.
import { handler, HttpError, clientIp, throttle, sha256, clean, anonClient, EMAIL_RE, audit } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const email = clean(b.email, 120).toLowerCase();
  const code = clean(b.code, 6);
  const pw = String(b.new_password ?? "");
  if (!EMAIL_RE.test(email) || !/^\d{6}$/.test(code)) throw new HttpError(400, "Enter the 6-digit code.");
  if (pw.length < 8 || pw.length > 72) throw new HttpError(400, "Password must be 8-72 characters.");
  await throttle(admin, clientIp(req), "reset", 30, 60);
  await throttle(admin, await sha256(email), "reset-verify", 6, 15);

  const bad = new HttpError(400, "That code is wrong or has expired.");
  const { data: rows } = await admin.from("profiles").select("id").eq("contact_email", email).limit(2);
  if (rows?.length !== 1) throw bad;
  const { data: u } = await admin.auth.admin.getUserById(rows[0].id);
  if (!u?.user?.email) throw bad;

  const { data: v, error } = await anonClient().auth.verifyOtp({ email: u.user.email, token: code, type: "recovery" });
  if (error || v.user?.id !== rows[0].id) throw bad;

  const { error: uErr } = await admin.auth.admin.updateUserById(rows[0].id, { password: pw });
  if (uErr) throw new HttpError(400, "Could not update the password. Try a stronger one.");
  await admin.auth.admin.signOut(v.session!.access_token, "global").catch(() => {});
  await audit(admin, rows[0].id, "password.reset");
  return { ok: true };
});
