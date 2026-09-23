# Stage 1 — Source & Mathematical Audit

Date: 2026-09-23
Workflow: research-paper-workflow v2.4, canonical main `63f11a50a13d9328213498a5a6576d00b9bceef7`
Input SHA: `8cde050fd8c02bceda7153ea791136f5f5c5137c`
Branch: `research/stage-14-submission-qa`

## Source identity

Target: Oz Shy and Rune Stenbacka, “Liquidity Provision and Optimal Bank Regulation,” *International Journal of Economic Theory* 3(3), September 2007, 219–233. DOI: 10.1111/j.1742-7363.2007.00057.x.

Current evidence confirms:
- publisher/VOR metadata and DOI through Wiley-linked RePEc records;
- VOR opening page/indexed text, including acceptance date 18 May 2007;
- complete 19-page author/institution-hosted mathematical manuscript;
- 2004 working-paper lineage (The Yrjö Jahnsson working paper series; a March 16, 2004 draft is separately indexed).

No received or revised date was located in the accessible official/indexed sources. No separate appendix, supplement, or accepted-manuscript file was located.

## VOR gate

The complete Wiley VOR body could not be directly opened equation-by-equation in the available access path. A Deep Blue index exposes a 160.1 KB publisher item, but the item body/bitstream could not be retrieved in this run. vLex exposes the VOR opening page only. The complete author/institution manuscript matches the VOR lineage in title, authors, abstract, acceptance information, journal identity, and publication metadata, but equations (7)–(17) have **not** been direct-VOR verified.

Therefore:
- all mathematical claims in this repository are certified first against the frozen complete author/institution manuscript;
- manuscript language must say “the complete author manuscript corresponding to the 2007 article” unless/until the VOR body is directly checked;
- a statement that the *published VOR equation* is wrong remains source-version-qualified.

This satisfies the Stage-0 rule only through explicit source-version qualification. It does not close the final VOR blocker for an unconditional correction claim.

## Primitive model reconstruction

Players: regulator, two banks A/B, continuum of depositors ((\lambda,x)\in[0,1]^2).

Regulator: (ho\in[0,1]) reserve ratio on risky accounts; (delta\in[0,1]) maximum fraction of risky accounts.

Banks: choose risky-account rates (i_A,i_B) and liquid-account fees (f_A,f_B).

Depositors: private (lambda) is liquidity-need probability; (x) is Hotelling location. The source defines (	heta_j\in[0,1]) as funds available upon a liquidity need and later imposes rational expectations.

The source's two-dimensional bank problem is Eq. (2). Eqs. (3)–(6) impose interior affine market shares and the (lambda=delta) account-indifference identity
[
 f_j=delta v(1-	heta_j)-(1-delta)i_j.
]
After substituting those identities, Eq. (7) is explicitly a **one-dimensional reduced rate problem**, holding (	heta_j,	heta_k) fixed in the differentiation step.

## Eq. (7) transcription

For bank (j) and rival (k):
[
\pi_j=\int_0^\delta \left[(1-\rho)r-(1-\lambda)i_j\right]
\left[\frac12+\frac{\lambda v(\theta_j-\theta_k)+(1-\lambda)(i_j-i_k)}{2\tau}\right]d\lambda
]
[
+\left[\delta v(1-\theta_j)-(1-\delta)i_j\right](1-\delta)
\left[\frac12+\frac{\delta v(\theta_j-\theta_k)+(1-\delta)(i_j-i_k)}{2\tau}\right].
]

This transcription was independently reconstructed from Eqs. (2)–(6), not copied from the upstream audit.

## Direct differentiation result

Define (t=\delta), (a=1-\delta), (A=(1-\rho)r), (d=\theta_j-\theta_k),
[
I_1=t-t^2/2,quad I_2=t^2/2-t^3/3,quad I_3=t-t^2+t^3/3,
]
[
K=I_1+a^2=1-t+t^2/2,qquad
L=I_3+a^3=\frac{1+2a^3}{3}.
]

Independent symbolic differentiation gives
[
\frac{\partial\pi_j}{\partial i_j}
=-\frac K2+
\frac{A I_1-vdI_2+a^2tv(1-2\theta_j+\theta_k)-(2i_j-i_k)L}{2\tau}.
]

A second differentiation gives
[
\frac{\partial^2\pi_j}{\partial i_j^2}
=-\frac{L}{\tau}
=-\frac{1+2(1-\delta)^3}{3\tau}<0
]
for (	au>0), (delta\in[0,1]).

The source manuscript instead displays ((\delta-1)^3/\tau) and a best response with no (r)-term. Thus the displayed Eq. (8) does not solve the frozen Eq. (7).

## Scope classification

Level 1 — printed reduced problem: fully specified and auditable.

Level 2 — symmetric rational-expectations implementation: auditable subject to reserve clipping and endpoints.

Level 3 — unrestricted original two-instrument game: not fully specified off equilibrium. The source does not provide a complete rule for clipped market shares, market capture/exit, asymmetric reserve feedback, or tie breaking after large unilateral deviations. No full-game uniqueness claim is allowed.

## Stage 1 verdict

**PASS WITH SOURCE-VERSION QUALIFICATION.**

The reduced-objective discrepancy is independently reproducible. The mathematical object and scope are frozen. Direct equation-level VOR comparison remains an explicit blocker for an unconditional “published VOR error” statement.
