<div align="center">

# Deep Brand & Identity Extractor

**An AI interviewer that turns "make it feel premium" into a spec you can actually execute.**

Colour tokens. Type scales. Easing curves. LUT direction. Cut rhythm. LUFS targets.
Aspect matrix. In about twenty minutes, from a conversation.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-orange.svg)](#install)
[![Works with any assistant](https://img.shields.io/badge/also-any%20LLM-blue.svg)](#option-2--any-other-assistant)

</div>

---

## The Pain

A client says: *"Make it modern. Clean. Premium. You know — like Apple."*

You nod. You build. You send v1.

They say: *"Hmm. Not quite what I pictured."*

Nobody is wrong here. That's what makes it so expensive. The client genuinely knows what they
want — they just have no vocabulary to hand it over. And you genuinely delivered *a* correct
interpretation of "premium." There were maybe forty of those available.

So the revisions begin. Round two. Round three. The timeline slips, the margin evaporates,
and somewhere around round four the relationship quietly sours — not because anyone did bad
work, but because **the brief never existed in the first place.**

Here's the part that stings: the fix has always been known. You ask forty precise questions
up front. What easing feels right — springy or mechanical? Crushed blacks or lifted? What's
the average shot length? Warm grade or clinical? Are we at −14 LUFS for social or −23 for
broadcast? Which of these four aspect ratios actually ship?

Nobody asks them. Asking forty questions takes an hour you don't have, it makes you look
uncertain in a first meeting, and clients get exhausted by question eight and start answering
"whatever you think is best" — which is the same as not asking at all.

And the brand guidelines PDF the client proudly sends over? Logo, colours, two typefaces,
some clear-space diagrams. **Nothing about motion. Nothing about grade. Nothing about sound.**
Which are, inconveniently, the three things a video is actually made of.

---

## The Person

This is built for the people caught on both sides of that gap.

**Video editors, motion designers and creative freelancers** — anyone who has burned a
weekend on revisions that a ten-minute conversation could have prevented, and who wants to
walk into a project with a written spec instead of a vibe.

**Design studios and brand consultants** — running discovery across a roster of clients, who
need the intake to be consistent, thorough, and not dependent on which strategist happened to
take the call.

**Founders, marketers and clients themselves** — people who know exactly how they want to be
seen but have never been handed the vocabulary to say it. You should not have to learn the
words *tracking*, *cubic-bezier* or *masterbrand* to get what you want. The interview meets
you where you are and translates on your behalf.

If you have ever written "just make it pop" — or received it — this was built for you.

---

## The Promise

**One conversation in. One execution-ready document out.**

Not a mood board. Not a personality quiz. Not a forty-page PDF of adjectives. A specification
precise enough that a designer, a developer and an editor can each work from it and produce
things that look like they came from the same company.

The interview follows five rules that make it survivable:

| | |
|---|---|
| **Two questions per turn** | Never a wall of forms. You can answer any turn in fifteen seconds. |
| **It adapts to you** | A motion designer gets asked about easing curves. A founder gets asked whether things should "snap like a switch or settle like something set down." Same answer extracted, different words. |
| **It never invents** | Anything inferred rather than confirmed is tagged `[Assumption — confirm]`. No fabricated metrics, no invented history. |
| **It works in your language** | Pick one at the start — English, Arabic, anything. Full RTL handling, including Arabic type pairing and motion-direction mirroring. |
| **It knows when it's done** | An internal coverage ledger tracks every dimension as `empty` / `thin` / `solid`. The interview ends when the ledger is full, not when you get bored. |

### Four tracks

Pick the one that matches the job. Only that track's question bank loads.

| Track | For | You get |
|---|---|---|
| **A · Portfolio & Website** | Freelancers building a site that wins one specific kind of work | Positioning, sitemap, page-by-page content plan, case-study template, voice guide with sample copy |
| **B · Personal Branding & Client Targeting** | Freelancers who need clients, not just a portfolio | Productised offer, ICP card, pricing table **with your floor**, channel plan, ready-to-send outreach scripts, objection handling |
| **C · Corporate Brand Strategy** | Companies defining who they are | Purpose, behavioural values, competitive map, positioning statement, archetype, messaging hierarchy at 10/50/150 words |
| **D · Brand Guidelines & Design System** | Anyone who has to *make things* | Everything below ⬇ |

### Why Track D exists

Standard brand guidelines stop at logo, colour and type. Track D keeps going into the
territory that video and motion work actually depends on:

- **Motion language** — easing curves as real `cubic-bezier` values, a duration scale in
  milliseconds, the one signature transition that makes the brand recognisable with the logo
  off screen, entrance/exit vocabulary, and a logo-sting beat sheet with timings
- **Video art direction** — grade and LUT direction, contrast and film emulation, framing and
  lens language, target average shot length, b-roll ratio, the full aspect-ratio matrix with
  per-ratio layout notes, safe areas, caption spec, end card
- **Sound identity** — sonic logo, music genre/BPM/mood, SFX philosophy, voice-over spec, and
  loudness targets per platform
- **Delivery specs** — fps, codec, bitrate, colour space, naming convention, folder
  structure, hand-off checklist
- **A design-token appendix** — flat token/value table, ready to export as JSON and drop
  straight into code

📄 **[See a full sample output →](examples/sample-brand-guidelines.md)**

---

## Install

### Option 1 · Claude Code (recommended)

```bash
git clone https://github.com/hozaifa-fazari/deep-brand-extractor.git
```

```bash
mkdir -p ~/.claude/skills/deep-brand && cp -r deep-brand-extractor/SKILL.md deep-brand-extractor/references ~/.claude/skills/deep-brand/
```

On Windows, the destination is `%USERPROFILE%\.claude\skills\deep-brand\`.

Then, from any project:

```
/deep-brand
```

Arguments skip the opening steps:

```
/deep-brand D
/deep-brand arabic
/deep-brand resume
```

### Option 2 · Any other assistant

No Claude Code? Copy [`references/portable-system-prompt.md`](references/portable-system-prompt.md)
into a system prompt, a Custom GPT, a Gem, or just paste it as your first message. Self-contained,
same protocol.

---

## How a session runs

```
Language  →  Objective  →  Interview  →  Checkpoint  →  Format  →  Delivery
```

The **checkpoint** is the step people underestimate. Before writing anything long, the AI
plays back a one-line summary of every dimension it captured and asks you to correct it.
Catching a misread positioning statement takes ten seconds there — and would take a full
rewrite afterwards.

At **delivery**, pick your format: structured Markdown, Notion-style, JSON (for Track D this
becomes a design-token file), plain text, or a hybrid. The document is written to
`brand/<slug>-<track>.md` in your project.

---

## What this does *not* do

Worth being straight about, because the boundary matters:

- **It writes the spec. It does not make the film.** Track D will hand you a complete motion
  and grade direction. Turning that into a rendered piece is craft work, and no interview
  replaces it.
- **It cannot see your footage or your logo.** It captures decisions and intent.
- **It is a strong first draft of strategy, not a substitute for a strategist.** It asks the
  questions a good one would ask. The judgement call on whether the answers are *right*
  is still human.

Which is roughly the honest summary of any good tool: it removes the part that was tedious,
and leaves the part that was actually the job.

---

## Contributing

The question banks are the heart of this, and they get better with more practitioners in
them. If you run a session and find a question that unlocked something — or one that
consistently falls flat — open a PR against the relevant file in `references/`.

Particularly wanted: question banks for adjacent disciplines (photography, UI/UX, podcast and
audio branding), and translations of the interview into more languages.

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Author

Built by **Hozaifa Fazari** — video editor and motion designer, Alexandria, Egypt — after one
too many projects where the brief arrived in round three.

Track D is the document I wish clients sent me. So I built the thing that produces it.

🔗 Portfolio · https://hozaifa-fazari.github.io/Portfolio
💬 **Ran a session? I'll read your output.** Open a
[Discussion](https://github.com/hozaifa-fazari/deep-brand-extractor/discussions) or send it
over — I review a few each week and give notes on what's still thin before anyone starts
building from it. Genuinely free; the outputs make the question banks better.

If the guidelines are done and the thing itself still needs making, that's the work I do.

---

## License

MIT — see [LICENSE](LICENSE). Use it commercially, fork it, ship it inside your own client
onboarding. Attribution appreciated, not required.

<div align="center">
<sub>If this saved you a revision round, a ⭐ helps other people find it.</sub>
</div>
