"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

Bounty: u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c
($2, 8 places, 1st $0.64). Gate: one line, 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt — a dog explaining why the homework got
eaten, in the dog's own voice. Judge (stand-up comic persona) weighs, in
order: (1) an excuse a dog gives after being caught eating the homework,
in the dog's own voice; (2) the bigger laugh, a twist or piece of dog
logic landing in a single line; (3) sounds like a real dog, with a dog's
priorities and none of a person's embarrassment; (4) works on its own;
(5) fresh — not a stock line about the cat, the taste of paper, or being
a good boy. The best excuse sounds like a dog who believes it has done
nothing wrong.

DECISION RECORD — Pass 1 (five candidates weighed against the brief):

A. "I didn't eat your homework. I taste-tested it for science, and the
   results say it needed more gravy." (100 chars)
   - For: "for science" is a funny piece of dog logic; the gravy verdict
     lands on the last word.
   - Against: "taste-tested" is a human word in a dog's mouth, and the
     setup denies the crime instead of owning it with dog confidence.

B. "The homework started it. It just sat there smelling like bacon and
   not running away." (84 chars)
   - For: blames the victim, pure prey logic — bacon smell plus prey that
     failed to flee; the dog is entirely unrepentant.
   - Against: two sentences split the snap a little; "started it" is a
     schoolyard line a human kid would also say.

C. "I was saving you. That essay was about to fail anyway, and now it
   has a much better excuse." (91 chars)
   - For: a meta twist — the dog replaces the excuse itself.
   - Against: "saving you" frames the dog as a helpful human; the laugh
     is clever rather than dog-like, and it explains itself.

D. "It looked at me first. Also, chapter three was delicious."
   (57 chars)
   - For: very tight, punchy; "chapter three was delicious" is a
     specific, dog-priority last word.
   - Against: "It looked at me first" is a generic playground defence;
     the turn is short on dog logic.

E. "You left it on the floor. On the floor. That is the dinner table
   in my house." (77 chars) — CHOSEN.
   - For: the dog redefines the floor as a dinner table — pure dog
     logic, zero embarrassment, and it believes it did nothing wrong.
     The repeated "On the floor." is a comic beat, the dog restating
     the obvious because the human clearly missed it. Fresh (no cat,
     no paper taste, no good boy), tight, and it could not be said by
     a person without losing the point. The punch lands on the last
     word: "house" — the dog's house, the dog's rules.
   - Against: the joke needs the reader to accept the redefinition,
     but that acceptance IS the joke.

DECISION RECORD — Pass 2 (head-to-head, tightening the chosen line):

E1 (original E, 77): "You left it on the floor. On the floor. That is
    the dinner table in my house."
    - The repetition beat survives; "the dinner table" is the noun
      redefinition the whole joke turns on.
E2 (69): "You left it on the floor. In my house, the floor is the
    dinner table."
    - Shorter, but it drops the repeated "On the floor." — the beat
      that sells the dog's disbelief — and reads flat by comparison.
E3 (81): "You left it on the floor. On the floor! That is where
    dinner happens in my house."
    - The exclamation adds noise, and "where dinner happens" is weaker
      than "the dinner table": the redefinition of the object, not the
      activity, is the punch.
    Verdict: E1 stands. No word is wasted; the repetition is the joke.

FINAL ENTRY (77 characters):
"You left it on the floor. On the floor. That is the dinner table in
my house."

Hand count, two ways: per segment — "You left it on the floor." = 25,
" On the floor." = 14 (total 39), " That is the dinner table in my
house." = 38 (total 77). Cross-check: 61 non-space characters +
16 spaces = 77.
"""

import os

ENTRY = (
    "You left it on the floor. On the floor. That is the dinner "
    "table in my house."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
