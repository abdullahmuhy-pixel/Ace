// Turns a username or student number into the Supabase Auth email so the client can call signInWithPassword.
// Unknown usernames get a plausible address back, so it never reveals which accounts exist.
// An email address is different: it is never mapped to a username here. When a student types the contact email of a
// username account, the client sends the password too; this function checks it with Supabase Auth and returns the
// session only if it is right, so nobody can learn which username belongs to an email.
import { handler, HttpError, clientIp, throttle, sha256, clean, studentEmail, USERNAME_RE, anonClient } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const id = clean(b.identifier, 120).toLowerCase();
  if (!id) throw new HttpError(400, "Enter your username and password.");
  await throttle(admin, clientIp(req), "login", 60, 15);
  await throttle(admin, await sha256(id), "login", 12, 15);

  if (id.includes("@")) {
    const password = String(b.password ?? "");
    const wrong = new HttpError(401, "Wrong username or password.");
    if (password.length < 8 || password.length > 72) throw wrong;
    const { data } = await admin.from("profiles").select("id").eq("contact_email", id).limit(2);
    if (data?.length !== 1) throw wrong;
    const { data: u } = await admin.auth.admin.getUserById(data[0].id);
    const authEmail = u?.user?.email;
    if (!authEmail || authEmail === id) throw wrong;      // the client already tried the email itself
    const { data: s, error } = await anonClient().auth.signInWithPassword({ email: authEmail, password });
    if (error || !s.session) throw wrong;
    return { session: { access_token: s.session.access_token, refresh_token: s.session.refresh_token } };
  }

  let profileId: string | null = null;
  if (/^[a-z]{2}-\d{2}-\d{6}$/.test(id)) {
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
  return { email: studentEmail(id.replace(/[^a-z0-9._-]/g, "x")) };
});
