# Stage 4A — Independent Mathematical Adversarial Certification

Date: 2026-09-23
Input SHA: `42d73db8abea76f48e354222e8ba0ab10d8739ff`

## Independence design

The Stage-4 production path uses SymPy differentiation of the source integral. Stage 4A deliberately does not import SymPy or the Stage-4 derivative expression.

The independent evaluator:
1. implements the primitive reduced profit directly;
2. evaluates the risky-account integral using exact rational Simpson quadrature (exact because the integrand is quadratic in λ);
3. obtains first and second derivatives by exact central differences of the quadratic profit;
4. evaluates finite deviations directly;
5. attacks the planner problem by exact rational grids across both reserve branches.

## Adversarial cases

Covered:
- exact source regression point, derivative (5/96);
- exact finite gain (1/2000) at (i_A=-99/100);
- random/diverse rational parameters;
- δ=1/100 and δ=99/100;
- ρ=0 and near-clipping values;
- small τ;
- r=0;
- positive and negative rate candidates;
- δ=0 direct fee game;
- δ=1 direct risky-rate game;
- v>r, v<r, v=r and r=0 planner cases;
- reserve clipping.

## Results

Command:
`python code/stage04a_independent.py`

Clean local run: PASS.

Every corrected best response tested has exact zero derivative in the independent evaluator; the exact Hessian equals (-L/	au<0). The source counterexample and same-regime finite gain reproduce exactly.

The clipped planner grid independently selects:
- ((δ,ρ)=(1,1/2)) for representative v>r>0 cases;
- ((1,0)) for v<r;
- (δ=1, ρ∈[0,1/2]) for v=r>0;
- the full-liquidity/clipped continuum for r=0<v.

## Scope audit

PASS applies to the reduced Eq. (7) game, its symmetric fixed-θ implementation, the explicitly reconstructed endpoints, and the regulator welfare problem. It does **not** promote those results into a global theorem about the source's incompletely specified asymmetric/clipped off-path two-instrument game.

## Verdict

**PASS.**

No rollback trigger was found. The new Proposition-2(a) boundary issue survives an implementation independent of Stage 4.
