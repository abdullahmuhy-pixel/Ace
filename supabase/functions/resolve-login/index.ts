// Turns "email, username or student number" into the Supabase Auth email so the client can call
// signInWithPassword. Unknown identifiers get a plausible address back, so it never reveals
// which accounts exist.
import { handler, HttpError, clientIp, throttle, sha256, clean, studentEmail, USERNAME_RE } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const id = clean(b.identifier, 120).toLowerCase();
  if (!id) throw new HttpError(400, "Enter your username and password.");
  await throttle(admin, clientIp(req), "login", 60, 15);
  await throttle(admin, await sha256(id), "login", 12, 15);

  let profileId: string | null = null;
  if (id.includes("@")) {
    const { data } = await admin.from("profiles").select("id").eq("contact_email", id).limit(2);
    if (data?.length === 1) profileId = data[0].id;
  } else if (/^[a-z]{2}-\d{2}-\d{6}$/.test(id)) {
    const { data } = await admin.from("profiles").select("id").eq("student_number", id.toUpperCase()).maybeSingle();
    profileId = data?.id ?? null;
  } else if (USERNAME_RE.test(id)) {
    const { data } = await admin.from("profiles").select("id").eq("username", id).maybeSingle();
    profileId = data?.id ?? null;
  }

  if (profileId) {
    const { data } = await admin.auth.admin.getUserById(profileId);
    if (data?.user?.email) return { email: data.user.email };
  }
  return { email: id.includes("@") ? id : studentEmail(id.replace(/[^a-z0-9._-]/g, "x")) };
});
