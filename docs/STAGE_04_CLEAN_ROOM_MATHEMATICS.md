# Stage 4 — Clean-Room Mathematics

Input SHA: 12dac9904cb5163421a5a7ed583e2ec80817e3fd
Output SHA: to be recorded by Stage 4A closure

## Production derivation
- reconstructed Eq. (7) from Eqs. (2)–(6);
- differentiated with SymPy directly from the integral objective;
- independently simplified moments (I_1,I_2,I_3,K,L);
- solved the FOC;
- proved strict concavity of the reduced objective;
- solved the symmetric fixed-θ and useful-reserve branches;
- recovered fees from the cutoff identity;
- rederived endpoints from their own instrument sets;
- recomputed welfare over clipped/unclipped reserve regions.

## Machine check
Command:
`python code/stage04_symbolic.py`

Local clean run on Python 3.13.5 / SymPy 1.14.0: PASS.

## Result
The upstream derivative finding is independently confirmed.

A second, independent material issue is also confirmed: for (v>r>0), Proposition 2(a)'s mixed-banking policy is not the solution of the source's constrained welfare problem. The correct planner solution is ((delta,ho)=(1,1/2)).

## Scope
Theorems certify the printed reduced objective and symmetric policy/welfare problem. They do not certify an unrestricted asymmetric original-game equilibrium correspondence.

Verdict: **PASS**.
