# Stage 4A Attack Matrix

| Attack | Expected | Result |
|---|---|---|
| source candidate at δ=1/2 | derivative 5/96 > 0 | PASS |
| finite source-candidate deviation | positive gain, same regime | PASS |
| corrected BR, rational interior cases | exact derivative 0 | PASS |
| Hessian | exact -L/τ < 0 | PASS |
| δ→0 probe | stable; endpoint separated | PASS |
| δ→1 probe | stable; endpoint separated | PASS |
| δ=0 fee-only game | f*=τ | PASS |
| δ=1 risky-only game | i*=3[(1-ρ)r-τ]/2 | PASS |
| reserve clipping | θ=min(2ρ/δ,1) | PASS |
| v>r planner | (1,1/2) for r>0 | PASS |
| v<r planner | (1,0) | PASS |
| v=r>0 | δ=1, ρ∈[0,1/2] | PASS |
| r=0<v | full-liquidity/clipped continuum | PASS |
| τ small positive | strict concavity retained | PASS |
| negative/positive rate candidates | no artificial sign restriction | PASS |

No source-unprovided price bound, participation constraint, market-capture rule, or asymmetric reserve continuation was added.
