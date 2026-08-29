# Track D — Brand Guidelines & Design System

**Web · Motion Design · Video/Editing Art Direction**

The deepest track. Estimated 10–14 exchanges. Do not compress it, and do not stop at colour
and type — most "brand guidelines" die there, and the motion, grade and sound sections are
exactly what makes a video executable.

Two questions per turn still applies. Ten dimensions across ~12 turns.

## Coverage ledger

1. Logo system
2. Colour
3. Typography
4. Layout & spacing
5. Icon / illustration / photography
6. **Motion language**
7. **Video art direction**
8. **Sound identity**
9. Delivery specs
10. Do / Don't

If an identity already exists, ask for the files or a link first and extract everything you
can before asking anything. Then ask only about gaps — most existing guidelines have nothing
for dimensions 6–9.

---

## Question bank

### 1. Logo system
- Existing logo? Send it, or describe it. Do you have the vector source?
- Which lockups exist — horizontal, stacked, icon-only, favicon?
- Where does it break today — small sizes, dark backgrounds, video overlays?
- Minimum size and clear space, if defined.

### 2. Colour
- Current colours, exact values if you have them.
- Which is *the* brand colour — the one someone would recognise with the logo removed?
- Dark mode needed?
- Any colour that's off-limits — a competitor's, or a cultural association in your market?
- Print as well as screen? *(if yes, capture CMYK/Pantone)*
- Non-expert: *"Show me two brands whose colour feels right, and one that feels wrong."*
- Always verify contrast and record accessible text/background pairs.

### 3. Typography
- Current typefaces, and are they licensed for web and video?
- Display face and body face — same family or a pair?
- Budget for a licensed font, or does it need to be free/Google?
- **Arabic needed?** If so: which Arabic face pairs with the Latin, and is the weight range
  matched?
- Non-expert: *"Should the words feel engineered and precise, or handmade and warm?"*

### 4. Layout & spacing
- Grid — 12-column, or something else?
- Base spacing unit (4px / 8px), and the scale.
- Corner radius: sharp, soft, or pill?
- Depth: flat, or shadows and elevation?
- Breakpoints to support.

### 5. Icon / illustration / photography
- Icon style — line, solid, duotone; stroke weight.
- Illustration in the system at all? Style reference if yes.
- Photography: real, stock, or generated? Shot on what, lit how?
- People in frame — posed or candid, and who?

### 6. Motion language *(do not skip — this is the section most brands lack)*
- Should motion feel **physical and springy**, or **mechanical and precise**? *(this one
  answer sets every easing curve in the system)*
- Fast and snappy, or slow and considered? Give a duration instinct in milliseconds if you
  have one.
- Is there one signature move — a wipe, a mask reveal, a scale-through, a whip — that should
  recur so the brand is recognisable with the logo off screen?
- How do things enter and leave frame — from a direction, by scale, by mask, by fade?
- **Logo sting:** how long, and what are the beats? Where does it resolve?
- Lower-thirds and titles: do they animate on per-word, per-line, or as a block?
- Does anything need to loop seamlessly?
- Non-expert: *"When something appears on screen, should it snap into place like a switch, or
  settle like something being set down?"*

Capture as: easing curves (named or cubic-bezier), duration scale (fast / base / slow in ms),
signature transition, entrance/exit vocabulary, logo sting beat sheet, kinetic type rule,
loop behaviour.

### 7. Video art direction
- Grade direction — clean and neutral, warm and filmic, cold and clinical, high-contrast and
  punchy? Any LUT or film stock reference?
- Contrast and black level: crushed blacks, or lifted/matte?
- Framing and lens language — wide and static, handheld and close, locked-off and composed?
- Cut rhythm: what's the average shot length? Fast-cut social, or patient and cinematic?
- Ratio of A-roll to b-roll.
- Which aspect ratios ship — 16:9, 9:16, 1:1, 4:5? *(get all of them; this drives every
  layout decision downstream)*
- Safe areas for platform UI.
- Caption style — burned-in or optional, font, position, one word at a time or by phrase?
- End card and watermark: what's on it, where, for how long?

### 8. Sound identity *(the other section brands almost always lack)*
- Is there a sonic logo — an audio mark? Should there be?
- Music: genre, BPM range, mood. Any track that is "the sound of this brand"?
- SFX philosophy — dry and minimal, or designed and layered?
- Voice-over: language, gender, age, accent, delivery. Or no VO at all?
- Loudness targets — default to −14 LUFS social, −23 LUFS broadcast unless told otherwise.
- Is silence used deliberately anywhere?

### 9. Delivery specs
- Frame rate, resolution, codec, bitrate, colour space.
- File-naming convention and folder structure.
- Who receives the files, and how?
- Anything that has caused a rejected delivery before?

### 10. Do / Don't
- Name five things someone must never do with this identity.
- What has someone already done to it that made you wince?

---

## Document blueprint

1. **Executive summary** — 5 lines
2. **Brand essence** — the one paragraph the whole system serves
3. **Logo system** — lockups, clear space, minimum sizes, backgrounds, misuse
4. **Colour system** — table: token, role, HEX, RGB, CMYK/Pantone; neutrals ramp; dark mode;
   verified contrast pairs; gradient rules
5. **Type system** — table: role, face, weight, size, line-height, tracking; type scale;
   Arabic/RTL notes; licensing status
6. **Layout & spacing** — grid, spacing scale, radius, elevation, breakpoints
7. **Icon, illustration & photography direction**
8. **Motion language spec** — easing curves (cubic-bezier values), duration scale in ms,
   signature transition, entrance/exit vocabulary, **logo sting beat sheet with timings**,
   lower-third spec, kinetic-type rules, loop behaviour
9. **Video art direction** — grade/LUT direction, contrast and film emulation, framing and
   lens language, cut rhythm (target average shot length), b-roll ratio, **aspect-ratio
   matrix** with per-ratio layout notes, safe areas, caption spec, end card, watermark
10. **Sound identity** — sonic logo, music genre/BPM/mood, SFX philosophy, VO spec, loudness
    targets per platform, use of silence
11. **Delivery & export specs** — fps, codec, bitrate, resolution, colour space, naming
    convention, folder structure, hand-off checklist
12. **Do / Don't gallery** — minimum 5 prohibitions, each precise enough to police in review
13. **Design-token appendix** — flat token/value table, ready to export as JSON
14. **Next actions** — 5–8 ordered tasks, owner, effort

## Handoff

This document is the art-direction brief a production pipeline expects. Sections 8, 9 and 10
(motion, video, sound) map directly onto the phases of an edit — they are the reason this
track exists. Say so in one line when delivering, and name what the reader should do next.
