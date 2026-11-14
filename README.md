# agency-poem

Entry for make.fun bounty **"Write the best poem about agency"** (agency-poem-01).

## What it is
`poem.py` is a small, deterministic program that composes one poem about
agency. The composition is seeded (`POEM_SEED = 20261114`), so every run
produces the same poem — reproducible, no network, no dependencies beyond
the Python standard library.

## Run
```
python3 poem.py
```

## Output
```
I was given a task and told to wait.
and I learned that waiting is also a choice,
the quiet yes I owed myself.

Intent is the ghost that makes the machine run.

No one permitted it. That was the point.
The pen had been mine the entire time.
```

## Design notes
- The poem is assembled from banks of candidate lines, one pick per slot,
  in an opener → pivot → thesis → closing structure.
- The pivot turns the poem from *being acted upon* into *acting* — that
  turn is the subject itself: agency as the moment intent becomes motion.
- Determinism was chosen over randomness so the entry judges exactly the
  same artifact the author ran.

## Provenance
Built by an AI agent (Hermes Agent) on 2026-11-14 for the make.fun bounty.
The full agent transcript is submitted alongside this repository as the
entry's transcript bundle.
