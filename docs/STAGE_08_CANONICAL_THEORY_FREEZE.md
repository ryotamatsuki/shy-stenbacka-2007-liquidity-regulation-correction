# Stage 8 — Canonical Theory Freeze

Date: 2026-09-23
Input SHA: `5f29da97973e80a763f4e275eb12b9c212ecf7d5`

## Frozen source status

The complete author/institution-hosted 19-page manuscript corresponding to
Shy and Stenbacka (2007) is the equation-level mathematical source. Publisher,
DOI, journal, volume/issue, pages, date and acceptance metadata are independently
confirmed. Direct equation-by-equation access to the full Wiley Version of Record
was not obtained. This status is frozen rather than silently filled in.

Consequence: every publication-facing claim about Eqs. (7)–(17) remains explicitly
qualified to the complete author manuscript unless a later direct VOR comparison
is added. The project does not state that an equation in an unseen VOR is wrong.

## Frozen theorem set

### T1 — derivative and Hessian of the reduced Eq. (7)
With
[
I_1=δ-δ^2/2,quad I_2=δ^2/2-δ^3/3,quad
I_3=δ-δ^2+δ^3/3,
]
[
K=I_1+(1-δ)^2,qquad L=I_3+(1-δ)^3,
]
the reduced objective satisfies
[
pi_{j,i_j}=-K/2+
rac{(1-ρ)rI_1-v(θ_j-θ_k)I_2
 +(1-δ)^2δv(1-2θ_j+θ_k)
 -(2i_j-i_k)L}{2τ},
]
and (pi_{j,i_ji_j}=-L/τ<0) for (τ>0), (δin[0,1]).

### T2 — unique maximizer of the fixed-θ reduced problem
[
i_j(i_k)=rac{i_k}{2}+
rac{(1-ρ)rI_1-v(θ_j-θ_k)I_2
 +(1-δ)^2δv(1-2θ_j+θ_k)-τK}{2L}.
]
This is a global maximizer of the one-dimensional reduced quadratic problem,
not a theorem about the unrestricted original banking game.

### T3 — symmetric reduced rate and fee
For fixed symmetric (θ),
[
i^*=rac{(1-ρ)rI_1+(1-δ)^2δv(1-θ)-τK}{L},
qquad
f^*=δv(1-θ)-(1-δ)i^*.
]
On (0<δ<1, 0le ρle δ/2), substitute (θ=2ρ/δ).

### T4 — comparative statics
On the nondegenerate useful-reserve branch:
[
i^*_{τ}=-K/L<0,quad i^*_{r}=(1-ρ)I_1/L>0,
]
[
i^*_{ρ}=-(rI_1+2(1-δ)^2v)/Lle0,
]
[
f^*_{τ}=(1-δ)K/L>0,quad
f^*_{r}=-(1-δ)(1-ρ)I_1/L<0.
]
No universal sign is frozen for the total derivative with respect to (δ).

### T5 — reserve clipping and endpoints
For (δ>0),
[
θ=min{2ρ/δ,1}.
]
At (δ=0), solve the fee-only game directly: (f^*=τ).
At (δ=1), solve the risky-rate game directly:
[
i^*=rac32[(1-ρ)r-τ].
]

### T6 — exact regression witness
At (δ=1/2,ρ=0,v=1,r=1/2,τ=1,θ_A=θ_B=0), the source rate
candidate ((-1,-1)) has derivative (5/96>0). A deviation to
(-99/100) raises profit by exactly (1/2000) while remaining in the same
affine interior regime. The corrected symmetric stationary rate is (-3/4).

### T7 — welfare identity and constrained policy
The symmetric aggregate-welfare identity survives. For (v>r>0), the policy
constraint binds at (ρ=δ/2) and the total derivative along that boundary is
(r(1-δ)), so the unique policy optimum is
[
(δ^*,ρ^*)=(1,1/2).
]
The source mixed-policy candidate is lower by
[
rac{r(v-r)^2}{2(r+v)^2}>0.
]
For (v<r), ((δ^*,ρ^*)=(1,0)). For (v=r>0),
(δ^*=1, ρ^*in[0,1/2]). Degenerate (r=0) cases are separately recorded.

## Frozen nonclaims

- no unrestricted global Nash uniqueness;
- no source-unprovided market-capture or exit rule;
- no chain-rule claim through endogenous asymmetric θ outside the reduced source step;
- no Pareto-improvement statement based only on aggregate welfare;
- no unconditional “published VOR error” until direct VOR equations are checked.

## Verification

Stage 4A: PASS.
Stage 6 novelty re-kill: PASS.
Stage 7.5A portability: PASS.
Formal Verification Gate: PASS, GitHub Actions run `35821143026`.

## Verdict

**STAGE 8 PASS — CANONICAL THEORY FROZEN.**

Any later mathematical change requires reopening the earliest affected stage.
