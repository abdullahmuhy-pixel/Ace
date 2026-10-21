import { createClient, SupabaseClient } from "npm:@supabase/supabase-js@2";

export const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const ANON = Deno.env.get("SUPABASE_ANON_KEY")!;
const SERVICE = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
// Students log in with a username, but Supabase Auth needs an email. Each student gets
// a synthetic address on this domain. No mail is ever sent to it.
export const STUDENT_DOMAIN = Deno.env.get("STUDENT_EMAIL_DOMAIN") ?? "students.aceeducation.app";
export const SITE_URL = Deno.env.get("SITE_URL") ?? "http://localhost:3000";

// Which websites may call these functions from a browser. Set ALLOWED_ORIGINS (comma-separated) to your own
// addresses. Without it, only the live site and the address in SITE_URL are allowed (never "any site").
const originOf = (u: string) => { try { return new URL(u).origin; } catch { return ""; } };
const ORIGINS = (Deno.env.get("ALLOWED_ORIGINS") ?? ["https://abdullahmuhy-pixel.github.io", originOf(SITE_URL)].filter(Boolean).join(","))
  .split(",").map((s) => s.trim()).filter(Boolean);

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
  constructor(public status: number, message: string, public extra?: Record<string, unknown>) { super(message); }
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
      if (e instanceof HttpError) return json(req, { ...(e.extra ?? {}), error: e.message }, e.status);
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

// ---------------- AI: which model each job uses, and the free / paid limits ----------------
// "fast" is the cheap everyday model (chat, hints, study packs). "smart" is the stronger model for jobs where accuracy
// matters most: marking essays and answers, solving maths from a photo, and teacher worksheets and quizzes.
// Secrets (optional): AI_MODEL_FAST, AI_MODEL_SMART. If a model is not available on the account, Ace falls back to
// AI_MODEL_FALLBACK so students still get an answer.
export type AiTier = "fast" | "smart";
const AI_MODELS: Record<AiTier, string> = {
  fast: Deno.env.get("AI_MODEL_FAST") ?? "claude-haiku-5-5",
  smart: Deno.env.get("AI_MODEL_SMART") ?? "claude-sonnet-5-5",
};
const AI_FALLBACK = Deno.env.get("AI_MODEL_FALLBACK") ?? "claude-haiku-4-5-20251001";

/** Calls Claude and returns the text of the answer. `maxTokens` is the room for the visible answer. */
export async function askClaude(o: { tier: AiTier; system: string; messages: unknown[]; maxTokens: number; failMsg?: string }) {
  const key = Deno.env.get("ANTHROPIC_API_KEY");
  if (!key) throw new HttpError(500, "Ace is not set up yet.");
  const call = (model: string) => {
    const body: Record<string, unknown> = { model, system: o.system, messages: o.messages, max_tokens: o.maxTokens };
    if (/^claude-(haiku|sonnet|opus)-5/.test(model)) {
      // 5.x models think before answering and bill the thinking as output: keep it light and leave room for the answer
      body.output_config = { effort: o.tier === "smart" ? "medium" : "low" };
      body.max_tokens = o.maxTokens + (o.tier === "smart" ? 4000 : 1500);
    }
    return fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: { "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json" },
      body: JSON.stringify(body),
    });
  };
  let model = AI_MODELS[o.tier];
  let r = await call(model);
  if (!r.ok && (r.status === 400 || r.status === 404) && model !== AI_FALLBACK) {
    console.error("anthropic", model, r.status, await r.text(), "-> retrying with", AI_FALLBACK);
    model = AI_FALLBACK;
    r = await call(model);
  }
  if (!r.ok) { console.error("anthropic", model, r.status, await r.text()); throw new HttpError(502, o.failMsg ?? "Ace could not answer. Try again in a moment."); }
  const out = await r.json();
  const text = (out.content ?? []).filter((c: any) => c.type === "text").map((c: any) => c.text).join("\n").trim();
  return { text, model };
}

export type AiKind = "chat" | "photo" | "essay" | "pack";
/** Counts one AI use against the caller's free or paid limits (public.consume_ai_kind). Throws 403/429 with a code the app understands. */
export async function aiGate(admin: SupabaseClient, userId: string, kind: AiKind) {
  const { data, error } = await admin.rpc("consume_ai_kind", { p_user: userId, p_kind: kind });
  if (error) { console.error(error); throw new HttpError(500, "Ace is not available right now."); }
  const g = Array.isArray(data) ? data[0] : data;
  if (g?.allowed) return g as { used: number; cap: number; mode: string; paid: boolean };
  const extra = { code: g?.reason ?? "daily", kind, used: g?.used ?? 0, cap: g?.cap ?? 0, paid: !!g?.paid };
  if (g?.reason === "off") throw new HttpError(403, "Your school has turned off AI help.", extra);
  if (g?.reason === "school") throw new HttpError(429, `You have used all ${g.cap} AI questions your school allows for this period.`, extra);
  if (g?.reason === "tool") {
    const what = kind === "photo" ? "photo questions" : kind === "essay" ? "essay and answer markings" : "study packs";
    throw new HttpError(429, g.paid
      ? `You have used today's ${g.cap} ${what}. They reset tomorrow.`
      : `Free accounts get ${g.cap} ${what} a ${kind === "photo" ? "day" : "week"}. Upgrade to get more.`, extra);
  }
  throw new HttpError(429, g?.paid
    ? `You have used today's ${g?.cap} Ace messages. They reset tomorrow.`
    : `You have used your ${g?.cap ?? 5} free Ace messages for today. Upgrade for up to 60 a day, or come back tomorrow.`, extra);
}

/** Runs the model call for a use that aiGate already counted; gives the use back if the call fails. */
export async function withRefund<T>(admin: SupabaseClient, userId: string, kind: AiKind, fn: () => Promise<T>): Promise<T> {
  try { return await fn(); }
  catch (e) { await admin.rpc("refund_ai", { p_user: userId, p_kind: kind }).then(() => {}, () => {}); throw e; }
}

/** Price in minor units for adding `qty` students to a licence that runs until `endMs`: the share of a year left,
 *  never less than one month. Used by checkout-start and checked again by payments-webhook. */
export function addPrice(perStudentMinor: number, qty: number, endMs: number, now = Date.now()) {
  const days = Math.max(31, Math.ceil((endMs - now) / 86_400_000));
  return Math.ceil(perStudentMinor * qty * Math.min(days, 366) / 366);
}
