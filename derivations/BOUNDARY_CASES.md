# Boundary and Endpoint Cases

## Reserve clipping

In a symmetric allocation:
[
w_A^R=w_B^R=int_0^delta lambda/2,dlambda=delta^2/4,
qquad
q_A^R=q_B^R=delta/2.
]

For (delta>0):
[
	heta(ho,delta)=min\{2ho/delta,1\}.
]

Cases:
- (2ho<delta): interior reserve response;
- (2ho=delta): clipping boundary, (	heta=1);
- (2ho>delta): (	heta=1), additional reserves have no depositor-liquidity benefit in the source mechanism.

## δ=0 — narrow-banking endpoint

There are no risky accounts. The risky rate (i_j) is economically irrelevant and should not be assigned the generic interior value.

The remaining liquid-fee game is
[
pi_j=f_jleft[rac12+rac{f_k-f_j}{2	au}ight].
]
It is strictly concave in (f_j), with best response
[
f_j=(	au+f_k)/2,
]
and unique symmetric affine-demand solution
[
f^*=	au.
]

The reserve ratio is irrelevant because there are no risky deposits.

## δ=1 — risky-banking endpoint

There are no liquid accounts, so the fee instrument and the λ=δ liquid/risky cutoff identity are absent. The source Eq. (11) is undefined.

Solving the no-liquid rate problem directly at symmetric fixed (	heta) gives
[
oxed{
i^*_{delta=1}=rac32[(1-ho)r-	au].
}
]

The corrected reduced formula has the same finite limit, but the endpoint is certified separately from its own instrument set.

## v=r equality

For (r=v>0), the welfare optimum is
[
delta^*=1,qquad ho^*in[0,1/2].
]
For (r=v=0), aggregate welfare is flat over the policy domain.

## max/min display

In the source's (v<r) line, displaying (max\{r/v,1\}=1) is algebraically inconsistent when (r/v>1). A constrained endpoint representation would use (min\{r/v,1\}=1). This is a local display issue, not the headline contribution.
