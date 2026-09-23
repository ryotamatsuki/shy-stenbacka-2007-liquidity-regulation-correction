# Stage 7.5A — Generality / Quantifier / Portability Red-Team

Date: 2026-09-23
Input SHA: `efbaabea82380f9656d4f2260fc43e82f5f74c21`

## Pre-specified tests

1. **Normalization release.** The derivation keeps (r,v,τ,ρ,δ) symbolic; the headline derivative mismatch is not tied to the exact counterexample normalization.
2. **Fixed θ versus reserve clipping.** The reduced best-response theorem is stated for fixed (	heta_j,	heta_k); symmetric implementation separately substitutes (	heta=min\{2ρ/δ,1\}).
3. **Endpoints.** δ=0 and δ=1 are solved from their own active instrument sets.
4. **Equivalent rate/fee representation.** Fees are recovered only through the source cutoff identity; no alternate normalization changes the derivative result.
5. **v=r equality.** The omitted equality correspondence is stated explicitly and not obtained by forcing either strict-inequality branch.
6. **Planner clipping.** The regulator problem is checked both below and above (ρ=δ/2); excess reserve requirements cannot overturn the boundary optimum for (r>0).
7. **Off-path continuation.** No source-unprovided rule is added to promote the reduced solution into full-game uniqueness.

## Classification

| Claim | Classification | Reason |
|---|---|---|
| Eq. (7) derivative mismatch | MODEL-SPECIFIC | tied to the printed source objective, robust to parameter normalization |
| corrected reduced BR | CONDITIONALLY PORTABLE | generic quadratic mechanics, but coefficients are source-model specific |
| r-dependence of rates/fees | MODEL-SPECIFIC | follows from the source investment-margin term |
| reserve clipping | INSTITUTION-SPECIFIC | depends on the source reserve/withdrawal mechanism |
| δ endpoints | MODEL-SPECIFIC | source instrument-set degeneration |
| Proposition 2(a) correction | MODEL-SPECIFIC | constrained optimization of source Eq. (14) |
| full-game uniqueness | UNRESOLVED / NOT CLAIMED | source off-path continuation incomplete |

## Quantifier audit

Publication theorems must state:
- (τ>0);
- fixed-(	heta) scope for the reduced bank problem;
- (0<δ<1) for generic rate/fee interior formulas;
- reserve branch condition when (	heta=2ρ/δ) is substituted;
- direct separate statements for (δ=0,1);
- (r>0, v>r) for the strict Proposition-2(a) dominance gap;
- equality/degenerate policy correspondences separately.

No theorem uses “unique equilibrium” without the qualifier “of the fixed-θ reduced affine game.”

## Formal Verification Gate

Formal verification is applicable because the correction rests on polynomial/rational identities, strict sign claims and an exact counterexample.

Lean targets:
- moment identities and (L>0);
- compact derivative decomposition;
- corrected BR satisfies the reduced FOC;
- negative Hessian;
- symmetric FOC;
- signs of (di^*/dr) and (df^*/dr);
- exact (5/96) counterexample;
- exact (-3/4) corrected rate;
- δ=1 endpoint algebra;
- positive welfare gap for (v>r>0);
- boundary welfare normal form.

Economic primitives, market-share regime validity and full equilibrium correspondence are deliberately not represented as Lean theorems.

## Verdict

Pending CI execution of the Lean project. The portability/scope audit itself is **PASS**; Stage 8 is blocked until the Formal Verification Gate is PASS.
