import { createClient, SupabaseClient } from "npm:@supabase/supabase-js@2";

export const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const ANON = Deno.env.get("SUPABASE_ANON_KEY")!;
const SERVICE = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
// Students log in with a username, but Supabase Auth needs an email. Each student gets
// a synthetic address on this domain. No mail is ever sent to it.
export const STUDENT_DOMAIN = Deno.env.get("STUDENT_EMAIL_DOMAIN") ?? "students.aceeducation.app";
export const SITE_URL = Deno.env.get("SITE_URL") ?? "http://localhost:3000";

const ORIGINS = (Deno.env.get("ALLOWED_ORIGINS") ?? "*").split(",").map((s) => s.trim());

export function cors(req: Request) {
  const o = req.headers.get("origin") ?? "";
  const allow = ORIGINS.includes("*") ? "*" : ORIGINS.includes(o) ? o : ORIGINS[0];
  return {
    "Access-Control-Allow-Origin": allow,
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Vary": "Origin",
  };
}

export function json(req: Request, body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...cors(req), "Content-Type": "application/json" },
  });
}

export class HttpError extends Error {
  constructor(public status: number, message: string) { super(message); }
}

/** Wrap a handler: CORS preflight, POST only, JSON body, uniform errors. */
export function handler(fn: (req: Request, body: any, admin: SupabaseClient) => Promise<unknown>) {
  Deno.serve(async (req) => {
    if (req.method === "OPTIONS") return new Response("ok", { headers: cors(req) });
    if (req.method !== "POST") return json(req, { error: "Method not allowed" }, 405);
    try {
      let body: any = {};
      try { body = await req.json(); } catch { throw new HttpError(400, "Invalid JSON body"); }
      const out = await fn(req, body ?? {}, adminClient());
      return json(req, out);
    } catch (e) {
      if (e instanceof HttpError) return json(req, { error: e.message }, e.status);
      console.error(e);
      return json(req, { error: "Something went wrong. Try again." }, 500);
    }
  });
}

export const adminClient = () =>
  createClient(SUPABASE_URL, SERVICE, { auth: { persistSession: false, autoRefreshToken: false } });
export const anonClient = () =>
  createClient(SUPABASE_URL, ANON, { auth: { persistSession: false, autoRefreshToken: false } });

export const clientIp = (req: Request) =>
  (req.headers.get("x-forwarded-for") ?? "unknown").split(",")[0].trim();

export async function sha256(s: string) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

/** Allow at most `max` hits per `minutes` for (key, kind). Records the hit. */
export async function throttle(admin: SupabaseClient, key: string, kind: string, max: number, minutes: number) {
  const since = new Date(Date.now() - minutes * 60_000).toISOString();
  const { count } = await admin.from("login_attempts").select("id", { count: "exact", head: true })
    .eq("key", key).eq("kind", kind).gte("created_at", since);
  if ((count ?? 0) >= max) throw new HttpError(429, "Too many attempts. Please wait a few minutes and try again.");
  await admin.from("login_attempts").insert({ key, kind });
}

/** Verify the caller's JWT and load their profile. Throws 401/403. */
export async function caller(req: Request, admin: SupabaseClient, roles?: string[]) {
  const auth = req.headers.get("authorization") ?? "";
  if (!auth.startsWith("Bearer ")) throw new HttpError(401, "Sign in first.");
  const { data, error } = await admin.auth.getUser(auth.slice(7));
  if (error || !data.user) throw new HttpError(401, "Your session has expired. Sign in again.");
  const { data: p } = await admin.from("profiles").select("*").eq("id", data.user.id).single();
  if (!p) throw new HttpError(403, "No profile for this account.");
  if (roles && !roles.includes(p.role)) throw new HttpError(403, "You do not have permission to do that.");
  return { user: data.user, profile: p };
}

export const studentEmail = (username: string) => `${username.toLowerCase()}@${STUDENT_DOMAIN}`;

export const USERNAME_RE = /^[a-z0-9._-]{3,30}$/;
export const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

export function clean(s: unknown, max = 60) {
  return String(s ?? "").replace(/[\u0000-\u001f<>]/g, "").trim().slice(0, max);
}

export function randomPassword(len = 10) {
  const a = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789";
  const r = crypto.getRandomValues(new Uint32Array(len));
  return [...r].map((n) => a[n % a.length]).join("");
}

export async function audit(admin: SupabaseClient, actor: string | null, action: string, target?: string, detail?: unknown) {
  await admin.from("audit_log").insert({ actor, action, target, detail });
}

/** Sends an email through Resend. Without RESEND_API_KEY the message is only logged (dev mode). */
export async function sendEmail(to: string, subject: string, html: string) {
  const key = Deno.env.get("RESEND_API_KEY");
  const from = Deno.env.get("MAIL_FROM") ?? "Ace Education <no-reply@aceeducation.app>";
  if (!key) { console.log(`[dev mail] to=${to} subject=${subject}\n${html}`); return; }
  const r = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
    body: JSON.stringify({ from, to, subject, html }),
  });
  if (!r.ok) throw new Error(`Resend ${r.status}: ${await r.text()}`);
}
