# Independent Reconstruction of Eq. (7)

This derivation begins from the source utilities and Eq. (2), not from the upstream audit.

For risky accounts, bank-j demand at type λ is
[
x_R(\lambda)=\frac12+\frac{\lambda v(\theta_j-\theta_k)+(1-\lambda)(i_j-i_k)}{2\tau}.
]

The λ=δ risky/liquid indifference condition implies
[
f_j=\delta v(1-\theta_j)-(1-\delta)i_j.
]

Liquid-account share is therefore
[
x_L=\frac12+\frac{\delta v(\theta_j-\theta_k)+(1-\delta)(i_j-i_k)}{2\tau}.
]

Substituting into Eq. (2) yields the reduced objective recorded in Stage 1.

Let (t=\delta), (a=1-t), (A=(1-\rho)r), (d=\theta_j-\theta_k). Direct integration uses
[
I_1=\int_0^t(1-\lambda)d\lambda=t-t^2/2,
]
[
I_2=\int_0^t\lambda(1-\lambda)d\lambda=t^2/2-t^3/3,
]
[
I_3=\int_0^t(1-\lambda)^2d\lambda=t-t^2+t^3/3.
]

The rate-dependent risky block differentiates to
[
-\frac{I_1}{2}
+\frac{A I_1-vdI_2-(2i_j-i_k)I_3}{2\tau},
]
while the liquid block differentiates to
[
-\frac{a^2}{2}
+\frac{a^2tv(1-2\theta_j+\theta_k)-(2i_j-i_k)a^3}{2\tau}.
]

Adding yields
[
\pi_{j,i_j}=-\frac{I_1+a^2}{2}
+\frac{A I_1-vdI_2+a^2tv(1-2\theta_j+\theta_k)-(2i_j-i_k)(I_3+a^3)}{2\tau}.
]

Hence with (K=I_1+a^2) and (L=I_3+a^3):
[
\pi_{j,i_ji_j}=-L/\tau.
]

Since
[
L=t-t^2+t^3/3+(1-t)^3=\{1+2(1-t)^3\}/3>0
]
on (t\in[0,1]), the reduced quadratic objective is strictly concave for (	au>0).

This establishes globality only **inside the reduced affine-share objective**. It does not certify the unrestricted original game after clipping or endogenous asymmetric reserve feedback.
