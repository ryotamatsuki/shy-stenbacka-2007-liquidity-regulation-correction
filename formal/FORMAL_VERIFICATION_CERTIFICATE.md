# Formal Verification Certificate

## Scope

Lean file: `formal/LiquidityRegulationCorrection.lean`.

The formal layer certifies proof-critical algebra after the economic object has been reconstructed independently in Stages 1, 4 and 4A. It does not formalize depositor choice, integration measure theory, equilibrium existence of the unrestricted game, or source interpretation.

| Lean theorem | Manuscript object | Supplied assumptions | Unformalized economic content |
|---|---|---|---|
| derivative_decomposition | compact corrected Eq. (7) derivative | none beyond algebraic definitions | validity of source reduction; actual differentiation is independently certified by Python/manual paths |
| corrected_best_response_foc | corrected reduced BR | τ≠0, L≠0 | feasible active regime |
| corrected_hessian_negative | strict reduced concavity | δ≤1, τ>0 | original-game globality |
| symmetric_rate_foc | symmetric reduced stationary point | τ≠0, L≠0 | rational-expectations fixed point for off-path θ |
| corrected_rate_increases_in_r | (di^*/dr>0) | 0<δ≤1, ρ<1 | institutional interpretation |
| corrected_fee_decreases_in_r | (df^*/dr<0) | 0<δ<1, ρ<1 | institutional interpretation |
| exact_counterexample_derivative | 5/96 witness | exact rational point | source admissibility and regime validity are checked outside Lean |
| exact_corrected_symmetric_rate | -3/4 witness | exact rational point | same |
| delta_one_endpoint_identity | δ=1 algebra | none | endpoint instrument-set derivation outside Lean |
| policy_gap_positive | strict planner dominance | 0<r<v | clipped-policy feasibility outside Lean |
| binding_boundary_normal_form | moving-boundary welfare | none | source policy-domain interpretation |
| source_policy_welfare_gap | exact source-vs-endpoint gap | r+v≠0 | economic optimality across full policy domain, independently checked in Stage 4A |

## Prohibitions audit

- no `sorry`;
- no `admit`;
- no arbitrary axioms;
- no theorem assumes its conclusion;
- no attempt to encode full economic equilibrium as a pure algebra theorem.

CI is required to close this certificate.
