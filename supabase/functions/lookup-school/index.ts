// Join flow step 1: turn a school code into the school's name, country and class levels.
// Throttled, and returns nothing else, so codes cannot be mined for data.
import { handler, HttpError, clientIp, throttle, clean } from "../_shared/util.ts";

handler(async (req, b, admin) => {
  await throttle(admin, clientIp(req), "join", 40, 60);
  const code = clean(b.school_code, 20).toUpperCase();
  if (code.length < 4) throw new HttpError(400, "Enter the school code your teacher gave you.");
  const { data: s } = await admin.from("schools").select("id,name,country_code,region,active").eq("school_code", code).maybeSingle();
  if (!s || !s.active) throw new HttpError(404, "We could not find that school code. Check it with your teacher.");
  const { data: cls } = await admin.from("classes").select("grade").eq("school_id", s.id);
  return { name: s.name, region: s.region, country_code: s.country_code,
           grades: [...new Set((cls ?? []).map((c) => c.grade))] };
});
