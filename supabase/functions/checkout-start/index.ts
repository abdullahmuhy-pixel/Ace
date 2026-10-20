// Starts a Flutterwave checkout. The price and currency come from public.plans on the server, never from the browser,
// and the tx_ref carries who is paying for what so the webhook can match the payment.
// Secrets: FLW_PUBLIC_KEY.
import { handler, HttpError, caller, clean, addPrice } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  const { user, profile } = await caller(req, admin);
  const code = clean(b.plan_code, 40);
  const { data: plan } = await admin.from("plans").select("*").eq("code", code).eq("active", true).maybeSingle();
  if (!plan) throw new HttpError(404, "That plan is not available.");
  if (plan.country_code && plan.country_code !== profile.country_code) throw new HttpError(400, "That plan is not offered in your country.");

  let who = `u:${user.id}`, qty = 1;
  if (plan.audience === "school") {
    if (profile.role !== "school_admin" || !profile.school_id) throw new HttpError(403, "Only a school admin can buy a school plan.");
    who = `s:${profile.school_id}`;
    // a licence is priced per student: at least 30 for a school, 10 for a tutor workspace
    const { data: sc } = await admin.from("schools").select("kind").eq("id", profile.school_id).single();
    const min = sc?.kind === "tutor" ? 10 : 30;
    qty = Math.floor(Number(b.students));
    if (!Number.isFinite(qty) || qty < min) throw new HttpError(400, `A licence is for at least ${min} students.`);
    if (qty > 20000) throw new HttpError(400, "For more than 20,000 students, contact us.");
  }
  // adding students to a licence that is still running: pay only for the time left (at least one month)
  let amountMinor = plan.amount_minor * qty, mode = "new";
  if (plan.audience === "school" && b.add === true) {
    const { data: cur } = await admin.from("entitlements").select("current_period_end,seats,status").eq("school_id", profile.school_id)
      .eq("status", "active").gt("current_period_end", new Date().toISOString()).order("created_at", { ascending: false }).limit(1).maybeSingle();
    if (!cur?.seats) throw new HttpError(400, "There is no running licence to add students to. Buy a new licence instead.");
    amountMinor = addPrice(plan.amount_minor, qty, Date.parse(cur.current_period_end));
    mode = "add";
  }
  const rand = [...crypto.getRandomValues(new Uint8Array(6))].map((x) => x.toString(16).padStart(2, "0")).join("");
  const tx_ref = `ace~${plan.code}~${who}~${rand}~${qty}~${mode}`;
  const pk = Deno.env.get("FLW_PUBLIC_KEY");
  if (!pk) throw new HttpError(500, "Payments are not set up yet.");
  return {
    tx_ref, public_key: pk, amount: amountMinor / 100, currency: plan.currency_code, students: plan.audience === "school" ? qty : undefined,
    customer: { email: user.email, name: `${profile.first_name} ${profile.surname}` },
    title: "Ace Education", description: plan.audience === "school" ? `${plan.name} × ${qty}` : plan.name,
  };
});
