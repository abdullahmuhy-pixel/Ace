// Starts a Flutterwave checkout. The price and currency come from public.plans on the server, never from the browser,
// and the tx_ref carries who is paying for what so the webhook can match the payment.
// Secrets: FLW_PUBLIC_KEY.
import { handler, HttpError, caller, clean } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const { user, profile } = await caller(req, admin);
  const code = clean(b.plan_code, 40);
  const { data: plan } = await admin.from("plans").select("*").eq("code", code).eq("active", true).maybeSingle();
  if (!plan) throw new HttpError(404, "That plan is not available.");
  if (plan.country_code && plan.country_code !== profile.country_code) throw new HttpError(400, "That plan is not offered in your country.");

  let who = `u:${user.id}`;
  if (plan.audience === "school") {
    if (profile.role !== "school_admin" || !profile.school_id) throw new HttpError(403, "Only a school admin can buy a school plan.");
    who = `s:${profile.school_id}`;
  }
  const rand = [...crypto.getRandomValues(new Uint8Array(6))].map((x) => x.toString(16).padStart(2, "0")).join("");
  const tx_ref = `ace~${plan.code}~${who}~${rand}`;
  const pk = Deno.env.get("FLW_PUBLIC_KEY");
  if (!pk) throw new HttpError(500, "Payments are not set up yet.");
  return {
    tx_ref, public_key: pk, amount: plan.amount_minor / 100, currency: plan.currency_code,
    customer: { email: user.email, name: `${profile.first_name} ${profile.surname}` },
    title: "Ace Education", description: plan.name,
  };
});
