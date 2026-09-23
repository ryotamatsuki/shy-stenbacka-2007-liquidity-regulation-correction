# Stage 7 — Economic Impact Map

Input SHA: `69118e5aa1fba578b2a4650e09799df045958e00`

| Source item | Mathematical dependence | Corrected status | Reason |
|---|---|---|---|
| Eq. (8) | derivative of Eq. (7) | **INVALID AS DISPLAYED** | omits the risky-account investment term and other coefficients |
| Hessian after Eq. (7) | second derivative | **INVALID AS DISPLAYED** | correct value is (-L/τ) |
| Eq. (11) | Eq. (8)+rational expectations | **CORRECTED** | corrected rate depends on (r) |
| Eq. (12) | Eq. (5)+Eq. (11) | **CORRECTED** | fee is not generally (τ) |
| Proposition 1(a) | Eq. (11)–(12) | **QUALITATIVELY SURVIVES** | (di^*/dτ<0, df^*/dτ>0), magnitudes change |
| Proposition 1(b) | Eq. (11) | **QUALITATIVELY SURVIVES** | (di^*/dρle0), strict on nondegenerate positive-return/opportunity domains |
| Proposition 1(c) | source r-invariance | **INVALID** | (di^*/dr>0, df^*/dr<0) on the useful branch |
| Eq. (13) | primitive depositor surplus | **SURVIVES EXACTLY** on symmetric allocation | direct integration reproduces it |
| Eq. (14) | Eq. (13)+industry investment surplus | **SURVIVES EXACTLY** on useful-reserve domain | transfers cancel |
| Eq. (15) | partial derivatives of Eq. (14) | **SURVIVES EXACTLY** | both partial derivatives reproduce |
| Eq. (16) | optimize ρ conditional on δ | **SURVIVES CONDITIONALLY** | (ρ=δ/2) for (v>r), (ρ=0) for (v<r) |
| Eq. (17), v>r | optimize δ after boundary binds | **INVALID** | source reuses a partial derivative instead of boundary total derivative |
| Eq. (17), v<r | optimize δ at ρ=0 | **SURVIVES EXACTLY** | (δ=1,ρ=0) |
| Proposition 2(a) | Eq. (14) constrained planner | **INVALID FOR v>r>0** | correct optimum is (δ=1,ρ=1/2) |
| Proposition 2(b) | Eq. (14) constrained planner | **SURVIVES EXACTLY** for (v<r) | risky banking with (ρ=0) |
| v=r | omitted equality | **CORRECTED CORRESPONDENCE** | (δ=1,ρ∈[0,1/2]) for (r=v>0) |
| Abstract optimal-policy characterization | Proposition 2 | **REQUIRES CORRECTION** | policy characterization changes |
| Conclusion segmentation headline | Proposition 2(a) | **NOT ESTABLISHED AS WELFARE OPTIMUM** | for (v>r>0) planner instead chooses δ=1 with full reserves on risky accounts |
| Full competitive implementation | source Eq. (7) plus off-path game | **NOT ESTABLISHED AS GLOBAL EQUILIBRIUM** | source omits complete off-path/clipping/asymmetric-reserve continuation |

## Planner versus implementation

The welfare arithmetic and bank equilibrium are different logical layers.

1. The aggregate-welfare objective can be evaluated from allocations because rates and fees are transfers.
2. The planner optimum does not by itself prove that the unrestricted banking game implements that allocation.
3. The corrected reduced-rate problem provides the rate/fee formulas for the source's interior reduced representation.
4. A complete global implementation theorem would require off-path rules the source does not fully specify.

No claim in this project equates reduced strict concavity with full-game uniqueness.

## Pareto language

The source's aggregate-welfare comparison is not, by itself, a proof that every depositor type and bank is weakly better off. The manuscript therefore uses “aggregate welfare” unless a type-by-type Pareto statement is separately established.
