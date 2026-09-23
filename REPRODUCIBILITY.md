# Reproducibility

Canonical branch: `research/stage-14-submission-qa`.

## Python
Requires Python 3.12+.

```bash
python -m pip install -r requirements.txt
python code/stage04_symbolic.py
python code/stage04a_independent.py
```

The first script differentiates the reconstructed Eq. (7) symbolically. The
second is implementation-independent: it uses exact rational arithmetic and
exact Simpson evaluation of the quadratic primitive profit integrand.

## Lean
Pinned toolchain and dependency graph:
- `lean-toolchain`
- `lakefile.lean`
- `lake-manifest.json`

Run:
```bash
lake build
```

The CI also performs an axiom/kernel audit and rejects proof placeholders.

## Full verification
```bash
bash scripts/verify_all.sh
```

The manuscript build target is added in Stage 10 and is then included in the
same verification entrypoint.

## Source provenance
Copyrighted source PDFs are not redistributed. URLs, version status and
equation mapping are recorded in `sources/SOURCE_MANIFEST.md` and
`sources/THEOREM_LEDGER.md`.

## Determinism
All regression examples use exact rational values. No Monte Carlo seed or
external data download is required for the mathematical test suite.
