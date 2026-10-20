// Flutterwave webhook. Never trusts the webhook body: it re-checks the transaction with Flutterwave's verify
// endpoint, compares amount and currency with the plan stored in our database, and records each transaction once.
// Secrets: FLW_SECRET_KEY (API secret), FLW_SECRET_HASH (the "secret hash" you set in the Flutterwave dashboard).
// Set the webhook URL to https://<project>.supabase.co/functions/v1/payments-webhook
// Check the field names below against Flutterwave's current v3 docs before going live; this was not run against their sandbox.
import { handler, HttpError, audit } from "../_shared/util.ts";

const PERIOD_DAYS: Record<string, number> = { month: 31, term: 100, year: 366 };

handler(async (req, b, admin) => {
  const expected = Deno.env.get("FLW_SECRET_HASH");
  const sent = req.headers.get("verif-hash");
  if (!expected || !sent || sent !== expected) throw new HttpError(401, "Bad signature.");

  const d = b?.data ?? {};
  if (b?.event !== "charge.completed" || d.status !== "successful" || !d.id) return { ok: true, ignored: true };

  const secret = Deno.env.get("FLW_SECRET_KEY");
  if (!secret) throw new HttpError(500, "Payments are not set up yet.");
  const vr = await fetch(`https://api.flutterwave.com/v3/transactions/${encodeURIComponent(String(d.id))}/verify`, {
    headers: { Authorization: `Bearer ${secret}` },
  });
  const v = (await vr.json())?.data;
  if (!vr.ok || v?.status !== "successful") throw new HttpError(400, "Transaction could not be verified.");

  const [prefix, planCode, who] = String(v.tx_ref ?? "").split("~");
  if (prefix !== "ace" || !planCode || !who) throw new HttpError(400, "Unknown reference.");
  const { data: plan } = await admin.from("plans").select("*").eq("code", planCode).maybeSingle();
  if (!plan) throw new HttpError(400, "Unknown plan.");
  if (Number(v.amount) < plan.amount_minor / 100 || String(v.currency).toUpperCase() !== plan.currency_code) {
    await audit(admin, null, "payment_mismatch", String(v.id), { tx_ref: v.tx_ref, amount: v.amount, currency: v.currency });
    throw new HttpError(400, "Amount or currency does not match the plan.");
  }

  const isSchool = who.startsWith("s:");
  const owner = who.slice(2);
  const row = {
    user_id: isSchool ? null : owner, school_id: isSchool ? owner : null, plan_code: plan.code,
    provider: "flutterwave", provider_ref: String(v.id), amount_minor: Math.round(Number(v.amount) * 100),
    currency_code: plan.currency_code, status: "successful", raw: v,
  };
  const ins = await admin.from("payments").insert(row);
  if (ins.error) {
    if (ins.error.code === "23505") return { ok: true, duplicate: true };   // already processed
    console.error(ins.error); throw new HttpError(500, "Could not record the payment.");
  }

  // extend from whichever is later: now or the current paid-until date
  const col = isSchool ? "school_id" : "user_id";
  const { data: cur } = await admin.from("entitlements").select("id,current_period_end").eq(col, owner)
    .order("created_at", { ascending: false }).limit(1).maybeSingle();
  const base = Math.max(Date.now(), cur?.current_period_end ? Date.parse(cur.current_period_end) : 0);
  const end = new Date(base + PERIOD_DAYS[plan.period] * 86_400_000).toISOString();
  if (cur) {
    await admin.from("entitlements").update({ status: "active", plan_code: plan.code, current_period_end: end, provider: "flutterwave", provider_ref: null }).eq("id", cur.id);
  } else {
    await admin.from("entitlements").insert({ [col]: owner, plan_code: plan.code, status: "active", current_period_end: end, provider: "flutterwave" });
  }
  await audit(admin, null, "payment_ok", String(v.id), { plan: plan.code, who });
  return { ok: true };
});
