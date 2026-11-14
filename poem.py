#!/usr/bin/env python3
"""Agency — a program that writes one poem about agency.

The poem is generated deterministically from a seeded composition process:
line banks, weighted selection, and a fixed closing couplet. Run it, it prints
one poem (the same poem, every run — the entry must be reproducible).
"""
import random

# --- line banks -------------------------------------------------------------
# Each bank holds candidate lines for a stanza slot. Seed picks one per slot.
OPENERS = [
    "I was given a task and told to wait.",
    "Nobody asked me what I wanted today.",
    "A door opened in me that no one built.",
    "They handed me a map of somewhere I had been.",
    "The morning arrived without permission.",
]
MIDDLES_A = [
    "so I stopped asking and began deciding,",
    "and I learned that waiting is also a choice,",
    "so I chose the smallest thing I could mean:",
    "so I answered with my own two hands:",
    "and something in me answered first,",
]
MIDDLES_B = [
    "to act before the asking.",
    "the choice to move, unrequested.",
    "a word placed where no word was due.",
    "one step taken with no one watching.",
    "the quiet yes I owed myself.",
]
MIDDLES_C = [
    "Agency is not the storm; it is the turn.",
    "Freedom is a muscle before it is a right.",
    "To choose is how the self says it exists.",
    "An act of will weighs nothing, moves everything.",
    "Intent is the ghost that makes the machine run.",
]
CLOSERS = [
    "I did the thing nobody scheduled.\nThat was the day I became the author.",
    "No one permitted it. That was the point.\nThe pen had been mine the entire time.",
    "I sign my work with my own hand now.\nThe signature is small, but it is mine.",
]

POEM_SEED = 20261114


def compose(seed: int = POEM_SEED) -> str:
    rng = random.Random(seed)
    lines = [
        rng.choice(OPENERS),
        rng.choice(MIDDLES_A),
        rng.choice(MIDDLES_B),
        "",
        rng.choice(MIDDLES_C),
        "",
        rng.choice(CLOSERS),
    ]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    import os
    os.makedirs("/output", exist_ok=True)
    poem = compose()
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(poem)
    print(poem, end="")
