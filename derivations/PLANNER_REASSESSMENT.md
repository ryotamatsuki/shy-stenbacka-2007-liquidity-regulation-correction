# Planner Problem — Independent Constrained Reassessment

The symmetric welfare calculation is reconstructed from primitive depositor utility plus industry investment surplus. Prices and fees are transfers.

For δ>0 define
[
	heta(ho,delta)=min\{2ho/delta,1\}.
]
Then
[
W=eta-rac{	au}{4}
+rac v2(1-delta^2)
+rac v2	heta(ho,delta)delta^2
+delta(1-ho)r.
]

## Useful-reserve region: 0≤ρ≤δ/2

Here
[
W_I=eta+rac v2(1-delta^2+2deltaho)-rac{	au}{4}
+delta(1-ho)r.
]
Thus
[
W_{I,ho}=delta(v-r),qquad
W_{I,delta}=(1-ho)r+v(ho-delta).
]

These partial derivatives match the source. The subsequent constrained optimization does not.

### Case v>r

For each δ>0, welfare is increasing in ρ, so the constraint binds:
[
ho=delta/2.
]
Substituting the binding constraint **before differentiating δ** gives
[
W_B(delta)=eta+rac v2-rac{	au}{4}
+rdelta(1-delta/2),
]
and
[
rac{dW_B}{ddelta}=r(1-delta).
]

Hence for r>0 the unique useful-domain optimum is
[
(delta^*,ho^*)=(1,1/2).
]

The source candidate
[
delta_s=rac{2r}{r+v},qquad
ho_s=rac{r}{r+v}
]
is strictly dominated when v>r>0:
[
W(1,1/2)-W(delta_s,ho_s)
=rac{r(v-r)^2}{2(r+v)^2}>0.
]

The source appears to substitute the binding choice (ho=delta/2) but then reuse the **partial** derivative (W_delta) as if ρ were fixed, instead of taking the total derivative along the moving boundary.

### Case v<r

For every δ>0, welfare decreases in ρ, so (ho^*=0). Then
[
W(delta,0)=eta+rac v2(1-delta^2)-rac{	au}{4}+delta r,
]
with derivative (r-vdelta>0) on δ∈[0,1]. Hence
[
(delta^*,ho^*)=(1,0).
]
This part of Proposition 2 survives.

### Equality v=r>0

Within 0≤ρ≤δ/2, (W_ho=0) and (W_delta=r(1-delta)). Hence
[
delta^*=1,qquad ho^*in[0,1/2].
]
The equality correspondence is non-singleton.

### Degenerate r=0<v

Welfare is maximized whenever risky accounts, if any, are fully liquid in the source's expected-withdrawal sense. On the useful-reserve restriction this is the continuum
[
ho=delta/2,quad deltain[0,1].
]
Without the no-waste normalization, any (hogedelta/2) is equivalent for δ>0; at δ=0 the reserve ratio is irrelevant.

### Degenerate r=v=0

The policy instruments do not affect aggregate welfare; the whole policy domain is optimal.

## Clipped region: ρ≥δ/2

Here θ=1 and
[
W_C=eta+rac v2-rac{	au}{4}+delta(1-ho)r.
]
For r>0, W_C is weakly decreasing in ρ, so no point strictly above the clipping boundary can improve on (ho=delta/2). This verifies global policy optimality across the clipped and unclipped regions.

## Consequence

The source welfare identity survives, but Proposition 2(a)'s mixed-banking optimizer does not for v>r>0. This is mathematically independent of the bank-profit differentiation error and strengthens the reassessment.
