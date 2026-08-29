# Sample Output — Track D · Brand Guidelines & Design System

> **This is a demonstration.** *Halcyon* is a fictional company invented to show the shape and
> resolution of a Track D document. No real client's material appears here.
>
> Produced from a 13-turn interview. Format: structured Markdown. Language: English.
> Condensed — a real Track D output runs roughly twice this length.

---

## 1. Executive summary

Halcyon makes sleep and recovery hardware for people who treat rest as training, not
indulgence. The identity has to hold two ideas that usually fight: **clinical credibility**
and **physical calm**. Everything below resolves that tension the same way — precise
structure, unhurried motion, warm materials. The system is deliberately quiet: one accent
colour, two type weights per composition, and motion slow enough to read as intentional
rather than sluggish. Where competitors signal performance through speed and contrast,
Halcyon signals it through restraint.

---

## 2. Brand essence

> *"Recovery is a discipline, not a reward."*
> — Founder, interview turn 4. Retained verbatim; it is the truest line in the brand.

Halcyon is the instrument, not the indulgence. Nothing in the system should read as spa,
wellness, or luxury softness. Think laboratory that happens to be warm.

---

## 3. Logo system

| Lockup | Use | Minimum width |
|---|---|---|
| Horizontal wordmark | Default; web header, video end card | 120 px / 24 mm |
| Stacked | Square placements, packaging | 64 px |
| Monogram `H` | Favicon, app icon, watermark | 24 px |

- **Clear space:** the height of the `H` on all sides. Non-negotiable in video overlays.
- **Backgrounds:** Ink or Bone only. Never on Ember. Never on photography without a scrim.
- **Misuse:** no rotation, no gradient fills, no drop shadows, no outline version, never
  re-typeset in another face.

---

## 4. Colour system

| Token | Role | HEX | RGB | CMYK |
|---|---|---|---|---|
| `color-ink` | Primary ground | `#12151A` | 18 21 26 | 78 66 55 71 |
| `color-bone` | Primary surface | `#F4F1EA` | 244 241 234 | 3 3 8 0 |
| `color-ember` | Single accent | `#D9603B` | 217 96 59 | 8 76 82 1 |
| `color-slate` | Secondary text | `#6B7280` | 107 114 128 | 60 48 39 9 |
| `color-signal` | Success / ready | `#3F7D5C` | 63 125 92 | 76 33 71 18 |
| `color-alert` | Error | `#A83A32` | 168 58 50 | 25 89 88 20 |

**Neutral ramp:** `#12151A` · `#2A2F38` · `#4A515C` · `#6B7280` · `#9CA3AF` · `#D6D3CC` · `#F4F1EA`

**Verified contrast pairs (WCAG AA+):**
Bone on Ink 15.8:1 · Ink on Bone 15.8:1 · Ember on Ink 6.1:1 · Slate on Bone 4.7:1
Ember on Bone is **3.1:1 — fails for body text.** Accent use only, at 18 px+ or as a fill.

**Dark mode** is the default state, not the variant. Light mode inverts ground and surface;
Ember is unchanged in both.

**Gradients:** one permitted — Ink → `#1C2128` at 8°, for video backgrounds only. No
multi-hue gradients anywhere.

---

## 5. Type system

| Role | Face | Weight | Size | Line-height | Tracking |
|---|---|---|---|---|---|
| Display | Söhne Breit | 500 | 56–96 px | 1.05 | −0.02em |
| H1 | Söhne | 500 | 40 px | 1.15 | −0.01em |
| H2 | Söhne | 400 | 28 px | 1.25 | 0 |
| Body | Söhne | 400 | 17 px | 1.6 | 0 |
| Caption / UI | Söhne Mono | 400 | 13 px | 1.4 | 0.04em |
| Data readout | Söhne Mono | 500 | 24–48 px | 1.1 | 0.02em |

- **Scale ratio:** 1.25 (major third).
- **Never more than two weights in a single composition.** This is the rule that carries the
  restraint; it is the first thing to check in review.
- Mono is reserved for measured values — hours slept, HRV, temperature. It is the voice of
  the instrument. Never use it for marketing copy.
- **Licensing:** Söhne requires a web licence and a separate broadcast/video licence.
  `[Assumption — confirm]` the video licence was not verified during the interview.

---

## 6. Layout & spacing

- **Grid:** 12-column, 72 px gutter desktop, 4-column / 16 px mobile.
- **Spacing scale (8 px base):** 4 · 8 · 16 · 24 · 40 · 64 · 104 · 168.
- **Radius:** 2 px. Almost sharp. Never pill, never fully square.
- **Elevation:** none. Separation is done with ground colour, never shadow.
- **Breakpoints:** 480 · 768 · 1024 · 1440.

---

## 7. Icon, illustration & photography

- **Icons:** 1.5 px stroke, square cap, 24 px grid. Line only, never filled.
- **Illustration:** none. The system deliberately has no illustration layer.
- **Photography:** real, available light, shot at dawn or dusk. Single subject, mid-shot or
  detail. Skin and textile texture retained — **never retouched smooth.** No stock. No
  smiling-at-camera.

---

## 8. Motion language

The governing decision, from turn 9: motion is **physical, but heavily damped.** Things have
mass and settle; nothing bounces, nothing snaps.

**Easing curves**

| Token | Curve | Use |
|---|---|---|
| `ease-settle` | `cubic-bezier(0.22, 0.61, 0.36, 1)` | Default. Every entrance. |
| `ease-lift` | `cubic-bezier(0.55, 0, 0.68, 0.53)` | Exits, dismissals |
| `ease-instrument` | `cubic-bezier(0.83, 0, 0.17, 1)` | Data readouts, numeric counts |

`ease-instrument` is the only curve permitted to feel mechanical, and only ever on numbers.

**Duration scale**

| Token | ms | Use |
|---|---|---|
| `dur-fast` | 220 | Micro-interaction, hover, toggle |
| `dur-base` | 420 | Standard entrance, card, panel |
| `dur-slow` | 900 | Scene change, hero reveal |
| `dur-breath` | 1600 | Ambient background drift only |

**Signature transition — "the settle."** Content enters at `translateY(24px)` and
`opacity: 0`, resolving on `ease-settle` over `dur-base`, with a 60 ms stagger between
sibling elements. Downward-to-rest, always. Nothing in this brand ever enters from above or
from the side. Applied consistently, the film is recognisable as Halcyon with the logo
removed — which is the test.

**Entrance / exit vocabulary**

- Enter: fade + 24 px rise. Never scale, never slide horizontally.
- Exit: fade only, `dur-fast`, `ease-lift`. Exits are faster than entrances — leaving is
  never ceremonial.
- Masks: horizontal wipe, left to right, for imagery only.

**Logo sting — 2.4 s total**

| Time | Beat |
|---|---|
| 0.00–0.60 s | Ink ground. Monogram `H` fades up at 40% scale-in from 0.94, `ease-settle`. |
| 0.60–1.10 s | Wordmark wipes in left-to-right behind a 1 px Ember rule travelling ahead of it. |
| 1.10–1.60 s | Ember rule continues off-frame right and disappears. Hold. |
| 1.60–2.10 s | **Full stillness.** Nothing moves. This beat is the brand. |
| 2.10–2.40 s | Cut to black, or dissolve to first frame over 300 ms. |

**Kinetic type:** by line, never by word. Word-by-word reads as urgency and is off-brand.
**Loops:** background drift only, 12 s seamless, maximum 3 px of travel.

---

## 9. Video art direction

- **Grade:** warm-neutral, low contrast. Lifted blacks to `#12151A` — never crushed to true
  black. Highlights rolled off early; no clipping. Reference: Kodak Vision3 250D, lightly
  applied.
- **Saturation:** −8% globally, with Ember protected via a qualifier so the accent survives.
- **Film emulation:** fine grain, 4–6% opacity. No halation, no gate weave.
- **Framing:** locked off or on a slow dolly. **No handheld.** 50 mm and 85 mm equivalents
  only; no wide-angle, no drone.
- **Cut rhythm:** target average shot length **4.5 s**. Longer than social convention, and
  deliberately so — the pacing is the argument.
- **A-roll / b-roll:** 40 / 60. Product and hands over faces.

**Aspect matrix**

| Ratio | Use | Layout note |
|---|---|---|
| 16:9 | Site hero, YouTube | Full type scale. Wordmark bottom-left, 64 px inset. |
| 9:16 | Reels, TikTok, Stories | Display drops to 48 px. Subject in upper third; lower third stays clear for captions. |
| 1:1 | Feed | Centre-weighted. Monogram only, never the wordmark. |
| 4:5 | Feed (preferred) | Same as 1:1 with 104 px top and bottom padding. |

- **Safe areas:** 14% bottom and 8% top clear of type on all vertical ratios.
- **Captions:** burned in, Söhne 400, Bone, 90% opacity, no box, no outline, no shadow.
  Positioned at 18% from bottom. **By phrase, never word-by-word** — consistent with the
  kinetic type rule.
- **End card:** Ink ground, monogram centred, URL in Söhne Mono 13 px below. Hold 1.8 s.
- **Watermark:** none. The system is quiet enough not to need one.

---

## 10. Sound identity

- **Sonic logo:** a single low struck tone at 96 Hz with a long natural decay (~2.1 s),
  landing on the stillness beat of the logo sting at 1.60 s. One note. Never a melody.
- **Music:** ambient / modern classical. **58–72 BPM.** Piano, felt textures, low strings. No
  drums, ever. No build-and-drop structure.
- **SFX philosophy:** dry and sparse. Diegetic only — fabric, a latch, breath. **No whooshes,
  no risers, no impacts.** If a transition needs a sound to work, the transition is wrong.
- **Voice-over:** optional, and absent by default. When used: female, 30s, unhurried,
  close-mic'd with audible breath retained. Never announcer-cadence.
- **Loudness:** −14 LUFS social · −16 LUFS web embed · −23 LUFS broadcast. True peak −1.0 dBTP.
- **Silence:** mandatory. Every piece over 20 s carries at least one full second of near-
  silence (music only, below −40 dB). It is a brand asset, not dead air.

---

## 11. Delivery & export specs

- **Frame rate:** 25 fps master. 30 fps only for platform-required deliverables.
- **Master:** ProRes 422 HQ, Rec.709, 1920×1080 or 3840×2160.
- **Delivery:** H.264, 16 Mbps 1080p / 40 Mbps 4K, AAC 320 kbps.
- **Naming:** `HAL_<project>_<ratio>_<version>_<YYMMDD>.mp4` → `HAL_launch_9x16_v03_260412.mp4`
- **Structure:** `01_footage / 02_audio / 03_graphics / 04_project / 05_exports`
- **Hand-off checklist:** loudness verified · captions burned and spell-checked · all four
  ratios exported · end-card hold ≥1.8 s · logo clear space verified at smallest placement.

---

## 12. Do / Don't

| ✗ Never | Why |
|---|---|
| Bounce, overshoot or elastic easing | Reads as playful. Directly contradicts the damped-motion decision. |
| Whooshes or risers on transitions | The sound system is diegetic. A whoosh marks the edit as generic. |
| Word-by-word kinetic type | Reads as urgency; the brand's entire argument is unhurried. |
| True black `#000000` | Breaks the lifted-black grade and flattens the warmth. |
| More than two type weights in one composition | The single rule that keeps the system restrained. |
| Ember as body-text colour | Fails contrast on Bone at 3.1:1. |
| Stock photography of people sleeping | Confirmed at interview as the category cliché to avoid. |

---

## 13. Design-token appendix

```json
{
  "color": {
    "ink": "#12151A", "bone": "#F4F1EA", "ember": "#D9603B",
    "slate": "#6B7280", "signal": "#3F7D5C", "alert": "#A83A32"
  },
  "space": [4, 8, 16, 24, 40, 64, 104, 168],
  "radius": "2px",
  "type": {
    "display": { "family": "Söhne Breit", "weight": 500, "tracking": "-0.02em" },
    "body":    { "family": "Söhne", "weight": 400, "size": "17px", "leading": 1.6 },
    "mono":    { "family": "Söhne Mono", "weight": 400, "tracking": "0.04em" },
    "scale": 1.25
  },
  "motion": {
    "ease": {
      "settle":     "cubic-bezier(0.22, 0.61, 0.36, 1)",
      "lift":       "cubic-bezier(0.55, 0, 0.68, 0.53)",
      "instrument": "cubic-bezier(0.83, 0, 0.17, 1)"
    },
    "duration": { "fast": 220, "base": 420, "slow": 900, "breath": 1600 },
    "stagger": 60,
    "signature": { "translateY": "24px", "ease": "settle", "duration": "base" }
  },
  "video": {
    "fps": 25, "colorSpace": "Rec.709", "averageShotLength": 4.5,
    "ratios": ["16:9", "9:16", "1:1", "4:5"],
    "loudness": { "social": -14, "web": -16, "broadcast": -23, "truePeak": -1.0 }
  }
}
```

---

## 14. Next actions

| # | Task | Owner | Effort |
|---|---|---|---|
| 1 | Confirm Söhne broadcast/video licence — flagged as an assumption in §5 | Client | 30 min |
| 2 | Build the logo-sting master in After Effects to the §8 beat sheet, all four ratios | Motion | 1 day |
| 3 | Commission the 96 Hz sonic logo; deliver stem + full mix | Sound | 2 days |
| 4 | Build the Halcyon LUT from the §9 grade direction; test against existing footage | Colour | 4 hrs |
| 5 | Export tokens (§13) into the web repo as CSS custom properties | Dev | 2 hrs |
| 6 | Shoot the founding photography set to §7 direction — dawn light, no retouching | Photo | 1 day |
| 7 | Build a caption template to §9 spec in Premiere and After Effects | Motion | 2 hrs |
| 8 | Review round: check every existing asset against the §12 Don't table | Creative dir | 3 hrs |

---

<sub>Generated with **Deep Brand & Identity Extractor** — https://github.com/hozaifa-fazari/deep-brand-extractor</sub>
