# Stage 9 — Repository / Reproducibility Setup

Date: 2026-09-23
Input SHA: `8a4a93df6dba95e0671d3dd4aebdefb25e0925de`

## Repository controls
- substantive work remains on `research/stage-14-submission-qa`;
- main is unchanged;
- copyrighted source PDFs are external references only;
- exact source/version qualification is recorded;
- Python and Lean dependencies are pinned;
- CI runs symbolic, exact-independent and formal checks.

## Reproducibility layers
1. SymPy derivative reconstruction from the Eq. (7) integral.
2. Fraction/Simpson exact independent evaluator.
3. Boundary/planner regression tests.
4. Lean/mathlib formal algebra certificates.
5. manuscript build hook in `scripts/verify_all.sh`, activated once Stage 10 supplies the manuscript.

## Fresh-environment evidence
GitHub Actions run `35821143026` passes the mathematical-regression and
formal-verification jobs on GitHub-hosted Ubuntu runners.

## Verdict
**PASS.**

Next-stage contract: construct the manuscript section-by-section without changing
the Stage-8 theorem set.
