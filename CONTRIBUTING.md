# Contributing

The question banks are the whole product. Everything else is scaffolding.

A question earns its place by unlocking an answer that the obvious version of the question
does not. *"What are your brand values?"* returns adjectives. *"Describe a decision the
company made that cost it money but was right"* returns a value. That is the bar.

## Good contributions

- **A better question.** Same dimension, sharper extraction. Say in the PR what the old one
  returned and what yours returns instead.
- **A missing dimension.** Something a track should cover and doesn't. Open an issue first so
  we can agree it belongs before you write the bank.
- **A new track.** Photography, UI/UX, podcast and audio branding, architecture, and product
  copy are all plausible. Match the existing file shape: coverage ledger → question bank →
  document blueprint.
- **A translation.** The protocol is language-agnostic, but the example phrasings inside the
  question banks are not. Idiomatic translations of the plain-language variants are
  especially valuable.
- **A sample output.** Real sessions, with the client anonymised, are the most useful thing
  you can add — they show the standard better than any description.

## The rules that don't bend

Before opening a PR, check your change against these. They are what make the interview
tolerable rather than exhausting:

1. **Two questions per turn, three maximum.** Any change that encourages batching questions
   will be rejected, however thorough it is.
2. **Every question carries example answers, a scale, or a menu.** Answering must be possible
   in fifteen seconds.
3. **Every question has a one-line reason it matters.** If you cannot write that line, the
   question is not earning its place.
4. **Plain-language variants for non-experts.** Clients use this too. A question only a
   specialist can parse needs a sensory equivalent alongside it.
5. **The output is decision-grade.** Blueprints must produce concrete values — hex codes,
   milliseconds, LUFS, easing curves — never adjectives.

## Practical

- One logical change per PR.
- Edit the `references/` file for the track you're changing; only touch `SKILL.md` for
  protocol-level changes, and explain why.
- Test it. Run a real session end to end before proposing a change to the flow, and say in
  the PR what you observed.

Issues describing where a session went wrong are as welcome as PRs. A transcript of an
interview that stalled is genuinely useful data.
