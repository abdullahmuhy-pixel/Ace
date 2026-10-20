// Right to erasure. A user deletes their own account (type DELETE to confirm); a school admin
// can delete a student of their school. The profile and all progress cascade away.
import { handler, HttpError, caller, clean, audit } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const { user, profile } = await caller(req, admin);
  if (clean(b.confirm, 10) !== "DELETE") throw new HttpError(400, 'Type DELETE to confirm.');
  let target = user.id;
  if (b.user_id && b.user_id !== user.id) {
    if (!["school_admin", "platform_admin"].includes(profile.role)) throw new HttpError(403, "You do not have permission to do that.");
    const { data: t } = await admin.from("profiles").select("id,school_id,role").eq("id", clean(b.user_id, 40)).maybeSingle();
    if (!t) throw new HttpError(404, "Account not found.");
    if (profile.role === "school_admin" && (t.school_id !== profile.school_id || t.role === "platform_admin"))
      throw new HttpError(403, "You do not have permission to do that.");
    target = t.id;
  }
  const { error } = await admin.auth.admin.deleteUser(target);
  if (error) throw new HttpError(400, "Could not delete the account.");
  await audit(admin, user.id, "account.delete", target);
  return { ok: true };
});
