// Step 1 of password reset: email a 6-digit code to the contact email on the account.
import { handler, HttpError, clientIp, throttle, sha256, clean, sendEmail, EMAIL_RE } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const email = clean(b.email, 120).toLowerCase();
  if (!EMAIL_RE.test(email)) throw new HttpError(400, "Enter the email on your account.");
  await throttle(admin, clientIp(req), "reset", 15, 60);
  await throttle(admin, await sha256(email), "reset", 4, 60);

  const { data: rows } = await admin.from("profiles").select("id").eq("contact_email", email).limit(2);
  if (rows?.length === 1) {
    const { data: u } = await admin.auth.admin.getUserById(rows[0].id);
    if (u?.user?.email) {
      const { data, error } = await admin.auth.admin.generateLink({ type: "recovery", email: u.user.email });
      const code = data?.properties?.email_otp;
      if (!error && code) {
        await sendEmail(email, "Your Ace Education reset code",
          `<p>Your password reset code is:</p><p style="font-size:28px;letter-spacing:6px"><b>${code}</b></p>` +
          `<p>It expires in 10 minutes. If you did not ask for this, ignore this email.</p>`);
      }
    }
  }
  return { ok: true };   // same answer whether or not the account exists
});
