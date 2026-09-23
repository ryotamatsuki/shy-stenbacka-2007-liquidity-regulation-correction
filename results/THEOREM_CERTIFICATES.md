# Canonical Theorem Certificates

Freeze date: 2026-09-23

| ID | Claim | Domain / quantifiers | Analytic proof | Independent check | Lean | Status |
|---|---|---|---|---|---|---|
| T1 | corrected derivative | fixed θj,θk; τ>0 for optimization | Eq7 reconstruction | exact evaluator | decomposition | PASS |
| T1b | Hessian -L/τ<0 | δ≤1, τ>0 | polynomial identity | exact Hessian | certified | PASS |
| T2 | corrected BR | L≠0, τ≠0; reduced affine problem | solve FOC + concavity | derivative-zero attacks | FOC certified | PASS |
| T3 | symmetric rate/fee | fixed symmetric θ; fee identity | substitution | rational attacks | symmetric FOC | PASS |
| T4r | di*/dr>0 | 0<δ≤1, ρ<1 | direct derivative | rational attacks | certified | PASS |
| T4f | df*/dr<0 | 0<δ<1, ρ<1 | direct derivative | rational attacks | certified | PASS |
| T5a | δ=0 fee endpoint | fee-only instrument set | direct game | exact evaluator | not needed | PASS |
| T5b | δ=1 rate endpoint | risky-only instrument set | direct game | exact evaluator | algebra identity | PASS |
| T6 | 5/96 witness | exact admissible point | substitution | finite deviation | certified | PASS |
| T7a | welfare identity | symmetric source allocation | primitive integration | grid/evaluator | boundary normal form | PASS |
| T7b | v>r policy correction | v>r>0 | KKT/boundary derivative | full clipped grid | positive gap | PASS |
| T7c | v<r policy | v<r | boundary derivative | grid | not needed | PASS |
| T7d | v=r equality | v=r>0 | correspondence | grid | not needed | PASS |

Economic-source fidelity is documented separately in `sources/THEOREM_LEDGER.md`.
