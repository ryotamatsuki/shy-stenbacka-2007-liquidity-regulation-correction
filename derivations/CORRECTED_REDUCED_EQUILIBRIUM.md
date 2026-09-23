# Stage 4 — Corrected Reduced Banking Problem

Let (t=delta), (a=1-delta), (A=(1-ho)r), (d=	heta_j-	heta_k), and define
[
I_1=t-t^2/2,quad I_2=t^2/2-t^3/3,quad I_3=t-t^2+t^3/3,
]
[
K=I_1+a^2=1-t+t^2/2,qquad
L=I_3+a^3=rac{1+2a^3}{3}.
]

## Theorem R1 — corrected derivative and concavity

For the source's reduced Eq. (7), holding (	heta_j,	heta_k) fixed:
[
rac{partialpi_j}{partial i_j}
=-rac K2+
rac{A I_1-vdI_2+a^2tv(1-2	heta_j+	heta_k)-(2i_j-i_k)L}{2	au}.
]

For (	au>0):
[
rac{partial^2pi_j}{partial i_j^2}=-rac L	au<0.
]

Because (L=[1+2(1-delta)^3]/3>0) on (deltain[0,1]), the reduced quadratic objective is globally strictly concave in (i_j).

## Theorem R2 — corrected reduced best response

The unique maximizer of the one-dimensional reduced objective is
[
oxed{
i_j(i_k)=rac{i_k}{2}
+rac{A I_1-vdI_2+a^2tv(1-2	heta_j+	heta_k)-	au K}{2L}.
}
]

The best-response slope is (1/2). This establishes uniqueness of the fixed-(	heta) affine reduced-game intersection, not uniqueness of the unrestricted banking game.

## Theorem R3 — symmetric fixed-theta solution

For (	heta_A=	heta_B=	heta):
[
oxed{
i^*=rac{(1-ho)rI_1+a^2tv(1-	heta)-	au K}{L}.
}
]
The cutoff identity gives
[
oxed{
f^*=tv(1-	heta)-a i^*.
}
]

On the useful reserve branch (0<t<1), (0lehole t/2), (	heta=2ho/t):
[
oxed{
i^*=rac{(1-ho)rI_1+a^2v(t-2ho)-	au K}{L},
}
]
[
oxed{
f^*=v(t-2ho)-a i^*.
}
]

These differ from source Eqs. (11)–(12).

## Comparative statics on the useful reserve branch

For (0<t<1), (	au>0), (r,vge0):
[
rac{partial i^*}{partial	au}=-rac KL<0,
]
[
rac{partial i^*}{partial r}=rac{(1-ho)I_1}{L}>0,
]
[
rac{partial i^*}{partialho}
=-rac{rI_1+2a^2v}{L}le0,
]
with strict inequality except the degenerate (r=v=0) case,
[
rac{partial f^*}{partial	au}=rac{aK}{L}>0,
qquad
rac{partial f^*}{partial r}
=-rac{a(1-ho)I_1}{L}<0,
]
and
[
rac{partial i^*}{partial v}=rac{a^2(t-2ho)}{L}ge0,qquad
rac{partial f^*}{partial v}=rac{(t-2ho)I_3}{L}ge0.
]

Thus Proposition 1(a)'s directions in (	au) survive, but magnitudes change; Proposition 1(b)'s rate sign in (ho) survives; Proposition 1(c)'s (r)-invariance is false.

No universal sign is asserted here for the total derivative with respect to the policy cutoff (delta); it changes multiple moments and the reserve mapping simultaneously.

## Clipped reserve branch

For (hoge t/2), (	heta=1):
[
i^*_{m clip}=rac{(1-ho)rI_1-	au K}{L},qquad
f^*_{m clip}=-(1-t)i^*_{m clip}.
]
This branch is mathematically distinct from simply continuing (	heta=2ho/t) above one.
