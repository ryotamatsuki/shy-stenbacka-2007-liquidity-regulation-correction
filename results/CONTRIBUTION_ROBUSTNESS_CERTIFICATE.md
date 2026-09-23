# Contribution Robustness Certificate

Date: 2026-09-23

## Headline claims

1. **Eq. (7) derivative correction** — PASS.
   - Direct reconstruction from source Eqs. (2)–(6).
   - Symbolic differentiation.
   - Independent exact rational evaluator.
   - Lean algebra certificate.
   - Classification: MODEL-SPECIFIC.

2. **Corrected reduced best response and strict concavity** — PASS.
   - Global maximum only within the one-dimensional reduced affine-share problem.
   - Classification: CONDITIONALLY PORTABLE mechanics; source-specific coefficients.

3. **Corrected symmetric rate and fee** — PASS.
   - Fixed-(	heta) theorem plus clipped rational-expectations implementation.
   - Classification: MODEL-SPECIFIC.

4. **Proposition 1(c) r-invariance correction** — PASS.
   - (di^*/dr>0), (df^*/dr<0) on the nondegenerate useful branch.
   - Classification: MODEL-SPECIFIC.

5. **Boundary completion** — PASS.
   - reserve clipping, δ=0, δ=1, v=r, r=0 handled separately.
   - Classification: MODEL/INSTITUTION-SPECIFIC.

6. **Proposition 2(a) moving-boundary correction** — PASS.
   - For (v>r>0), source candidate is strictly dominated by
     ((δ,ρ)=(1,1/2)) by
     (r(v-r)^2/[2(r+v)^2]).
   - Independent clipped-policy grid confirms.
   - Classification: MODEL-SPECIFIC.

7. **Full unrestricted banking-game uniqueness** — NOT CLAIMED.
   - Source does not fully specify all off-path asymmetric/clipped continuations.

## Falsification attempts survived

- exact source counterexample and same-regime finite deviation;
- rational parameter attacks;
- δ near 0 and 1;
- reserve clipping boundary and over-reserving region;
- v>r, v<r, v=r, r=0;
- small τ;
- positive and negative rate values;
- separate endpoint instrument sets;
- symbolic / exact-evaluator / Lean implementation diversity.

## Source-version caveat

The complete author/institution-hosted mathematical manuscript is frozen and
fully equation-audited. Direct equation-level comparison against the full Wiley
Version of Record remains unavailable. Publication-facing statements therefore
must retain source-version qualification until that check is performed.

Overall certificate: **PASS WITH VOR SOURCE-VERSION QUALIFICATION**.
