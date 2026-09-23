#!/usr/bin/env python3
"""Stage-4 symbolic certification from the printed reduced objective.

This file reconstructs Eq. (7) directly from Eqs. (2)-(6) and differentiates
that objective. It does not import the upstream audit.
"""
import sympy as sp

t,rho,v,r,tau,thj,thk,i,ik,lam=sp.symbols(
    "t rho v r tau thj thk i ik lam", real=True
)
a=1-t
A=(1-rho)*r
d=thj-thk
xR=sp.Rational(1,2)+(lam*v*d+(1-lam)*(i-ik))/(2*tau)
fee=t*v*(1-thj)-a*i
xL=sp.Rational(1,2)+(t*v*d+a*(i-ik))/(2*tau)
pi=sp.integrate((A-(1-lam)*i)*xR,(lam,0,t))+fee*a*xL

I1=t-t**2/2
I2=t**2/2-t**3/3
I3=t-t**2+t**3/3
K=sp.simplify(I1+a**2)
L=sp.simplify(I3+a**3)
E=1-2*thj+thk

D=sp.simplify(sp.diff(pi,i))
Dtarget=-K/2+(A*I1-v*d*I2+a**2*t*v*E-(2*i-ik)*L)/(2*tau)
H=sp.factor(sp.diff(pi,i,2))
BR=sp.solve(sp.Eq(D,0),i)[0]
BRtarget=ik/2+(A*I1-v*d*I2+a**2*t*v*E-tau*K)/(2*L)

assert sp.simplify(D-Dtarget)==0
assert sp.simplify(H+L/tau)==0
assert sp.simplify(L-(1+2*a**3)/3)==0
assert sp.simplify(BR-BRtarget)==0

th,z=sp.symbols("th z", real=True)
isol=sp.solve(sp.Eq(z,BRtarget.subs({ik:z,thj:th,thk:th})),z)[0]
isol_target=((1-rho)*r*I1+a**2*t*v*(1-th)-tau*K)/L
assert sp.simplify(isol-isol_target)==0
fsym=sp.simplify(t*v*(1-th)-a*isol_target)

itheta=sp.factor(isol_target.subs(th,2*rho/t))
ftheta=sp.factor(fsym.subs(th,2*rho/t))
assert sp.simplify(itheta-((1-rho)*r*I1+a**2*v*(t-2*rho)-tau*K)/L)==0
assert sp.simplify(ftheta-(v*(t-2*rho)-a*itheta))==0

# Comparative statics in the useful reserve region 0<delta<1, rho<=delta/2.
assert sp.simplify(sp.diff(itheta,tau)+K/L)==0
assert sp.simplify(sp.diff(itheta,r)-(1-rho)*I1/L)==0
assert sp.simplify(sp.diff(itheta,rho)+(r*I1+2*a**2*v)/L)==0
assert sp.simplify(sp.diff(ftheta,tau)-a*K/L)==0
assert sp.simplify(sp.diff(ftheta,r)+a*(1-rho)*I1/L)==0
assert sp.simplify(sp.diff(itheta,v)-a**2*(t-2*rho)/L)==0
assert sp.simplify(sp.diff(ftheta,v)-(t-2*rho)*I3/L)==0

# Welfare block and constrained-boundary correction.
beta=sp.symbols("beta", real=True)
Wint=beta+v*(1-t**2+2*t*rho)/2-tau/4+t*(1-rho)*r
Wbound=sp.simplify(Wint.subs(rho,t/2))
assert sp.simplify(sp.diff(Wint,rho)-t*(v-r))==0
assert sp.simplify(sp.diff(Wbound,t)-r*(1-t))==0

source_t=2*r/(r+v)
source_rho=r/(r+v)
Wsource=sp.simplify(Wint.subs({t:source_t,rho:source_rho}))
Wend=sp.simplify(Wint.subs({t:1,rho:sp.Rational(1,2)}))
assert sp.factor(Wend-Wsource)==r*(r-v)**2/(2*(r+v)**2)

# Exact regression point.
subs={t:sp.Rational(1,2),rho:0,v:1,r:sp.Rational(1,2),
      tau:1,thj:0,thk:0,i:-1,ik:-1}
assert sp.simplify(D.subs(subs))==sp.Rational(5,96)
assert sp.simplify(isol_target.subs({
    t:sp.Rational(1,2),rho:0,v:1,r:sp.Rational(1,2),tau:1,th:0
}))==sp.Rational(-3,4)

pi0=sp.simplify(pi.subs(subs))
pi_eps=sp.simplify(pi.subs({**subs,i:sp.Rational(-99,100)}))
assert sp.simplify(pi_eps-pi0)==sp.Rational(1,2000)

xR_eps=sp.factor(xR.subs({
    t:sp.Rational(1,2),rho:0,v:1,r:sp.Rational(1,2),tau:1,
    thj:0,thk:0,i:sp.Rational(-99,100),ik:-1
}))
xL_eps=sp.factor(xL.subs({
    t:sp.Rational(1,2),rho:0,v:1,r:sp.Rational(1,2),tau:1,
    thj:0,thk:0,i:sp.Rational(-99,100),ik:-1
}))
assert sp.simplify(xR_eps-(sp.Rational(101,200)-lam/sp.Integer(200)))==0
assert xL_eps==sp.Rational(201,400)

print("PASS: Eq7 symbolic derivative identity")
print("PASS: Hessian = -L/tau and L positive polynomial identity")
print("PASS: corrected best response and symmetric rate/fee")
print("PASS: comparative-static identities")
print("PASS: exact counterexample derivative=5/96; epsilon gain=1/2000")
print("PASS: planner boundary derivative and welfare-dominance identity")
