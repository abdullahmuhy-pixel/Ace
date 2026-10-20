// Ace, the AI study buddy. The browser never sees the Anthropic key and never decides its own limit:
// this function checks the caller's JWT, asks the database whether the school/platform cap allows one more
// question (public.consume_ai counts it atomically), then calls the model.
//
// Secrets: ANTHROPIC_API_KEY (required), AI_MODEL (default claude-haiku-4-5-20251001),
//          AI_REQUIRE_ACCESS=true to also require an active plan or trial (default false during the pilot).
import { handler, HttpError, caller, throttle, clean } from "../_shared/util.ts";

const MODEL = Deno.env.get("AI_MODEL") ?? "claude-haiku-4-5-20251001";
const MAX_TURNS = 10;
const MAX_CHARS = 2000;
const MAX_CHARS_LONG = 5000;

const MODES: Record<string, string> = {
  tutor: "TUTOR MODE: do not give the final answer. Ask one guiding question or give one hint at a time, then wait for the student's reply.",
  essay: "ESSAY GRADER: the student pastes an essay or long answer. Mark it like an examiner for this exam and subject: give an estimated mark or grade band, 3 strengths, 3 specific improvements, and one model rewrite of a weak sentence. Say clearly that this is an estimate, not an official mark.",
  markscheme: "MARK SCHEME CHECKER: the student pastes a question, their answer and, if they have it, the mark scheme. Mark point by point, say which marks are earned and what is missing. If no scheme is pasted, say you are using typical marking points that may differ from the official scheme.",
  qgen: "QUESTION GENERATOR: from the notes the student pastes, write 5 exam-style questions (a mix of multiple choice and short answer) and put the answers after a line that says Answers:.",
  solver: "SMART SOLVER: solve the Maths or Science problem step by step, state each formula and the units, and finish with a quick check of the answer.",
};
// A photo of a question is read with the same model (Claude Haiku 4.5 reads images).
const LONG_MODES = new Set(["essay", "markscheme", "qgen"]);

// Teacher and tutor tools (staff accounts only)
const TEACHER_MODES: Record<string, string> = {
  lessonplan: "LESSON PLAN: write a ready-to-teach lesson plan for this topic and exam. Sections: Objectives (3), Prior knowledge, Starter (5 min), Teaching steps with timings, One worked example with full working, Class activity, 5 quick check questions with answers, Homework, Support for weaker students, Stretch for stronger students.",
  worksheet: "WORKSHEET: write 10 practice questions that build from easy to full exam style for this topic, numbered, with mark allocations. Then a line that says Answer key: followed by worked answers and marking points.",
  quizjson: "QUIZ: output ONLY a JSON array, no other text, of the number of multiple-choice questions requested (default 10). Each item: {\"q\": question, \"o\": [four options], \"a\": index of the correct option 0-3, \"e\": one-sentence explanation}. Exactly one correct option, plausible distractors, check every answer.",
  answer: "CLASS ANSWER: a student asked the question below. Write a clear answer the teacher can post for the whole class: explain step by step in plain words, include one short worked example if it helps, and end with one quick check question.",
  comment: "REPORT COMMENT: from the student details given, write a 2-3 sentence report-card comment in a warm, professional tone: one specific strength, one area to improve, and one clear target. No grades unless given.",
};

function teacherPrompt(c: { country: string; exam: string; subject: string; topic: string; lang: string; mode: string }) {
  return `You are Ace, an assistant for a teacher or tutor preparing students for exams.
Country: ${c.country || "not given"}. Exam: ${c.exam || "not given"}. Subject: ${c.subject || "not given"}. Topic: ${c.topic || "not given"}.
Write in ${c.lang === "es" ? "Spanish" : "English"}. Follow the syllabus and conventions of this exam and country: currency, units, spelling and examples. Check all arithmetic.
${TEACHER_MODES[c.mode]}`;
}

const LEARNER: Record<string, [string, string, string]> = {
  secondary: ["exam-prep tutor for a secondary-school student", "Exam", "in plain words a teenager can follow"],
  university: ["tutor for a university student (Ace Campus)", "Course track", "at first-year university level: precise, with correct notation, still clear and friendly"],
  academy: ["coach for an adult learner taking a certificate course (Ace Academy)", "Course", "in plain, practical words for an adult who may be new to the subject"],
};

function systemPrompt(c: { country: string; exam: string; subject: string; topic: string; lang: string; mode?: string; level?: string }) {
  const lv = LEARNER[c.level || "secondary"] || LEARNER.secondary;
  return `You are Ace, a friendly, encouraging ${lv[0]}.
Country: ${c.country || "not given"}. ${lv[1]}: ${c.exam || "not given"}. Subject: ${c.subject || "not given"}. Topic: ${c.topic || "not given"}.
Reply in ${c.lang === "es" ? "Spanish" : "English"}, ${lv[2]}. Use the currency, units, spellings and examples that fit the student's country.
Explain step by step and show working. Check your arithmetic before you state a number. If the student asks for an answer to a question, guide them through it and let them do the last step.
Stay on schoolwork. If the student seems distressed, be kind and suggest they talk to a teacher, parent or another trusted adult. Do not ask for or repeat personal details such as full names, addresses or phone numbers.
${c.mode && MODES[c.mode] ? MODES[c.mode] + "\n" : ""}Keep answers under ${c.mode && LONG_MODES.has(c.mode) ? 450 : 250} words unless the student asks for more.`;
}

async function hasAccess(admin: any, userId: string) {
  const { data, error } = await admin.rpc("user_has_access", { p_user: userId });
  if (error) { console.error(error); return false; }
  return data === true;   // includes school licences and seats in a paid group plan
}

handler(async (req, b, admin) => {
  const { user, profile } = await caller(req, admin);
  await throttle(admin, user.id, "ai", 20, 1);

  const isStaff = ["teacher", "subject_teacher", "school_admin", "platform_admin"].includes(profile.role);
  const tmode = isStaff && typeof b?.context?.mode === "string" && TEACHER_MODES[b.context.mode] ? b.context.mode : "";
  const mode = typeof b?.context?.mode === "string" && ["tutor", "essay", "markscheme", "qgen", "solver"].includes(b.context.mode) ? b.context.mode : "";
  const lim = LONG_MODES.has(mode) || tmode ? MAX_CHARS_LONG : MAX_CHARS;
  const raw = Array.isArray(b.messages) ? b.messages.slice(-MAX_TURNS) : [];
  const messages = raw
    .map((m: any) => ({ role: m?.role === "assistant" ? "assistant" : "user", content: String(m?.content ?? "").slice(0, lim) }))
    .filter((m: any, i: number, arr: any[]) => m.content.trim() || (b?.image && i === arr.length - 1));
  if (!messages.length || messages[messages.length - 1].role !== "user") throw new HttpError(400, "Ask a question first.");
  while (messages.length && messages[0].role !== "user") messages.shift();

  // Optional photo of a question (snap a question): attached to the latest student message only.
  const img = b?.image;
  let photo: { media_type: string; data: string } | null = null;
  if (img && typeof img === "object") {
    const mt = String(img.media_type ?? "");
    const data = String(img.data ?? "").replace(/^data:[^,]+,/, "");
    if (!["image/jpeg", "image/png", "image/webp", "image/gif"].includes(mt)) throw new HttpError(400, "Send the photo as a JPG or PNG.");
    if (!/^[A-Za-z0-9+/=]+$/.test(data) || data.length > 2_000_000) throw new HttpError(400, "That photo is too large. Try a closer, smaller photo.");
    photo = { media_type: mt, data };
  }
  const apiMessages: any[] = messages.map((m: any, i: number) => (photo && i === messages.length - 1)
    ? { role: "user", content: [{ type: "image", source: { type: "base64", media_type: photo.media_type, data: photo.data } }, { type: "text", text: m.content || "Help me with the question in this photo." }] }
    : m);

  if (Deno.env.get("AI_REQUIRE_ACCESS") === "true" && !(await hasAccess(admin, user.id))) {
    throw new HttpError(402, "Your free trial has ended. Ask your school or choose a plan to keep using Ace.");
  }

  const { data: gate, error: gerr } = await admin.rpc("consume_ai", { p_user: user.id });
  if (gerr) { console.error(gerr); throw new HttpError(500, "Ace is not available right now."); }
  const g = Array.isArray(gate) ? gate[0] : gate;
  if (!g?.allowed) {
    throw new HttpError(429, g?.mode === "off"
      ? "Your school has turned off AI help."
      : `You have used all ${g?.cap ?? ""} AI questions for this period. Try again later.`);
  }

  const key = Deno.env.get("ANTHROPIC_API_KEY");
  if (!key) throw new HttpError(500, "Ace is not set up yet.");
  const ctx = b.context ?? {};
  const r = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json" },
    body: JSON.stringify({
      model: MODEL,
      max_tokens: tmode ? 2400 : LONG_MODES.has(mode) ? 1100 : 700,
      system: tmode ? teacherPrompt({
        country: clean(ctx.country, 40), exam: clean(ctx.exam, 60), subject: clean(ctx.subject, 60),
        topic: clean(ctx.topic, 160), mode: tmode, lang: ctx.lang === "es" || profile.language === "es" ? "es" : "en",
      }) : systemPrompt({
        country: clean(ctx.country, 40), exam: clean(ctx.exam, 60), subject: clean(ctx.subject, 60),
        topic: clean(ctx.topic, 120), mode, level: ["university", "academy"].includes(ctx.level) ? ctx.level : "secondary",
        lang: ctx.lang === "es" || profile.language === "es" ? "es" : "en",
      }),
      messages: apiMessages,
    }),
  });
  if (!r.ok) { console.error("anthropic", r.status, await r.text()); throw new HttpError(502, "Ace could not answer. Try again in a moment."); }
  const out = await r.json();
  const reply = (out.content ?? []).filter((c: any) => c.type === "text").map((c: any) => c.text).join("\n").trim();
  return { reply: reply || "I could not come up with an answer. Try asking in a different way.", used: g.used, cap: g.cap, mode: g.mode, tool: tmode || null };
});
