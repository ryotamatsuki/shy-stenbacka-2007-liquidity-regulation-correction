#!/usr/bin/env python3
"""Independent Stage-4A evaluator.

No SymPy. Risky-account integral is evaluated by exact rational Simpson quadrature,
which is exact because the primitive integrand is quadratic in lambda.
"""
from fractions import Fraction as F

def q(x): return x if isinstance(x,F) else F(x)

def profit(i,ik,delta,rho,v,r,tau,thj,thk):
    i,ik,delta,rho,v,r,tau,thj,thk=map(q,(i,ik,delta,rho,v,r,tau,thj,thk))
    def g(lam):
        margin=(1-rho)*r-(1-lam)*i
        share=F(1,2)+(lam*v*(thj-thk)+(1-lam)*(i-ik))/(2*tau)
        return margin*share
    risk=F(0) if delta==0 else delta*(g(F(0))+4*g(delta/2)+g(delta))/6
    fee=delta*v*(1-thj)-(1-delta)*i
    xL=F(1,2)+(delta*v*(thj-thk)+(1-delta)*(i-ik))/(2*tau)
    return risk+fee*(1-delta)*xL

def deriv(i,ik,delta,rho,v,r,tau,thj,thk,h=F(1,997)):
    args=(ik,delta,rho,v,r,tau,thj,thk)
    return (profit(i+h,*args)-profit(i-h,*args))/(2*h)

def hessian(i,ik,delta,rho,v,r,tau,thj,thk,h=F(1,997)):
    args=(ik,delta,rho,v,r,tau,thj,thk)
    return (profit(i+h,*args)-2*profit(i,*args)+profit(i-h,*args))/(h*h)

def moments(delta):
    t=q(delta); a=1-t
    I1=t-t*t/2; I2=t*t/2-t*t*t/3; I3=t-t*t+t*t*t/3
    return a,I1,I2,I3,I1+a*a,I3+a*a*a

def corrected_br(ik,delta,rho,v,r,tau,thj,thk):
    ik,delta,rho,v,r,tau,thj,thk=map(q,(ik,delta,rho,v,r,tau,thj,thk))
    a,I1,I2,I3,K,L=moments(delta)
    A=(1-rho)*r; d=thj-thk; E=1-2*thj+thk
    return ik/2+(A*I1-v*d*I2+a*a*delta*v*E-tau*K)/(2*L)

def sym_rate(delta,rho,v,r,tau,theta):
    delta,rho,v,r,tau,theta=map(q,(delta,rho,v,r,tau,theta))
    a,I1,I2,I3,K,L=moments(delta)
    return ((1-rho)*r*I1+a*a*delta*v*(1-theta)-tau*K)/L

def reserve_theta(delta,rho):
    delta,rho=map(q,(delta,rho))
    if delta==0: return F(1)
    return min(F(1),2*rho/delta)

def welfare(delta,rho,v,r,tau=F(1),beta=F(0)):
    delta,rho,v,r,tau,beta=map(q,(delta,rho,v,r,tau,beta))
    if delta==0: return beta+v/2-tau/4
    th=reserve_theta(delta,rho)
    return beta-tau/4+v*(1-delta*delta)/2+v*th*delta*delta/2+delta*(1-rho)*r

# Exact source-candidate regression.
p=dict(delta=F(1,2),rho=F(0),v=F(1),r=F(1,2),tau=F(1),thj=F(0),thk=F(0))
assert deriv(F(-1),F(-1),**p)==F(5,96)
assert sym_rate(F(1,2),F(0),F(1),F(1,2),F(1),F(0))==F(-3,4)
assert profit(F(-99,100),F(-1),**p)-profit(F(-1),F(-1),**p)==F(1,2000)

# Independent derivative-zero/Hessian attacks at rational parameters.
cases=[
 (F(1,2),F(0),F(1),F(1,2),F(1),F(0),F(0),F(-1)),
 (F(1,3),F(1,12),F(3,2),F(2,3),F(5,4),F(1,2),F(1,4),F(1,5)),
 (F(9,10),F(1,5),F(2),F(5,3),F(1,10),F(4,5),F(3,4),F(2,7)),
 (F(1,100),F(0),F(0),F(3),F(2),F(0),F(0),F(1,3)),
 (F(99,100),F(49,100),F(5),F(1),F(3,2),F(1),F(1),F(-2)),
]
for delta,rho,v,r,tau,thj,thk,ik in cases:
    ib=corrected_br(ik,delta,rho,v,r,tau,thj,thk)
    assert deriv(ib,ik,delta,rho,v,r,tau,thj,thk)==0
    H=hessian(ib,ik,delta,rho,v,r,tau,thj,thk)
    a,I1,I2,I3,K,L=moments(delta)
    assert H<0 and H==-L/tau

# delta=0 liquid-only fee game.
for tau0 in (F(1,5),F(1),F(7,3)):
    f=tau0
    def lp(ff): return ff*(F(1,2)+(f-ff)/(2*tau0))
    h=F(1,101)
    assert (lp(f+h)-lp(f-h))/(2*h)==0

# delta=1 risky-only rate game.
for rho0,r0,tau0 in [(F(0),F(1,2),F(1)),(F(1,2),F(2),F(1,3)),(F(3,4),F(4),F(2))]:
    istar=F(3,2)*((1-rho0)*r0-tau0)
    assert deriv(istar,istar,F(1),rho0,F(5),r0,tau0,F(1),F(1))==0

# Planner grid attacks over clipped and unclipped regions.
for vv,rr,expected in [
    (F(2),F(1),(F(1),F(1,2))),
    (F(5),F(2),(F(1),F(1,2))),
    (F(1),F(2),(F(1),F(0))),
]:
    best=None; pts=[]
    for di in range(41):
        dd=F(di,40)
        for ri in range(41):
            rh=F(ri,40); w=welfare(dd,rh,vv,rr)
            if best is None or w>best: best=w; pts=[(dd,rh)]
            elif w==best: pts.append((dd,rh))
    assert pts==[expected]

best=None; pts=[]
for di in range(41):
    dd=F(di,40)
    for ri in range(41):
        rh=F(ri,40); w=welfare(dd,rh,F(1),F(1))
        if best is None or w>best: best=w; pts=[(dd,rh)]
        elif w==best: pts.append((dd,rh))
assert pts==[(F(1),F(ri,40)) for ri in range(21)]

best=max(welfare(F(di,40),F(ri,40),F(1),F(0)) for di in range(41) for ri in range(41))
for di in range(1,41):
    dd=F(di,40)
    for ri in range(41):
        rh=F(ri,40)
        if rh>=dd/2: assert welfare(dd,rh,F(1),F(0))==best

print("PASS: independent Fraction/Simpson evaluator")
print("PASS: exact source-candidate regression and finite deviation")
print("PASS: corrected BR derivative zero and Hessian on adversarial rational cases")
print("PASS: delta=0 and delta=1 endpoint games")
print("PASS: clipped planner grid including v>r, v<r, v=r, r=0")
