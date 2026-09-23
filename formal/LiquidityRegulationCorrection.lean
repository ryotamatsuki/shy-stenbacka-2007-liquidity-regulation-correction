import Mathlib

namespace LiquidityRegulationCorrection

noncomputable section

def I1 (δ : ℝ) : ℝ := δ - δ^2 / 2
def I2 (δ : ℝ) : ℝ := δ^2 / 2 - δ^3 / 3
def I3 (δ : ℝ) : ℝ := δ - δ^2 + δ^3 / 3
def K (δ : ℝ) : ℝ := I1 δ + (1-δ)^2
def L (δ : ℝ) : ℝ := I3 δ + (1-δ)^3

theorem K_normal_form (δ : ℝ) :
    K δ = 1 - δ + δ^2 / 2 := by
  unfold K I1
  ring

theorem L_normal_form (δ : ℝ) :
    L δ = (1 + 2*(1-δ)^3) / 3 := by
  unfold L I3
  ring

theorem I1_pos (δ : ℝ) (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) :
    0 < I1 δ := by
  unfold I1
  have hh : 0 < 1 - δ/2 := by nlinarith
  calc
    0 < δ * (1 - δ/2) := mul_pos hδ0 hh
    _ = δ - δ^2/2 := by ring

theorem L_pos (δ : ℝ) (hδ1 : δ ≤ 1) :
    0 < L δ := by
  rw [L_normal_form]
  have ha : 0 ≤ 1 - δ := sub_nonneg.mpr hδ1
  have hc : 0 ≤ (1 - δ)^3 := pow_nonneg ha 3
  nlinarith

def derivExpanded
    (δ ρ v r τ θj θk i ik : ℝ) : ℝ :=
  (-I1 δ/2 +
      (((1-ρ)*r)*I1 δ - v*(θj-θk)*I2 δ - (2*i-ik)*I3 δ)/(2*τ))
  + (-(1-δ)^2/2 +
      ((1-δ)^2*δ*v*(1-2*θj+θk) - (2*i-ik)*(1-δ)^3)/(2*τ))

def derivCompact
    (δ ρ v r τ θj θk i ik : ℝ) : ℝ :=
  -K δ/2
  + (((1-ρ)*r)*I1 δ - v*(θj-θk)*I2 δ
      + (1-δ)^2*δ*v*(1-2*θj+θk)
      - (2*i-ik)*L δ)/(2*τ)

theorem derivative_decomposition
    (δ ρ v r τ θj θk i ik : ℝ) :
    derivExpanded δ ρ v r τ θj θk i ik =
      derivCompact δ ρ v r τ θj θk i ik := by
  unfold derivExpanded derivCompact K L I1 I2 I3
  ring

def bestResponse
    (δ ρ v r τ θj θk ik : ℝ) : ℝ :=
  ik/2 +
    (((1-ρ)*r)*I1 δ - v*(θj-θk)*I2 δ
      + (1-δ)^2*δ*v*(1-2*θj+θk) - τ*K δ)
      /(2*L δ)

theorem corrected_best_response_foc
    (δ ρ v r τ θj θk ik : ℝ)
    (hτ : τ ≠ 0) (hL : L δ ≠ 0) :
    derivCompact δ ρ v r τ θj θk
      (bestResponse δ ρ v r τ θj θk ik) ik = 0 := by
  unfold derivCompact bestResponse
  field_simp [hτ, hL]
  ring

def hessian (δ τ : ℝ) : ℝ := -L δ / τ

theorem corrected_hessian_negative
    (δ τ : ℝ) (hδ1 : δ ≤ 1) (hτ : 0 < τ) :
    hessian δ τ < 0 := by
  unfold hessian
  have hL : 0 < L δ := L_pos δ hδ1
  have hneg : -L δ < 0 := neg_lt_zero.mpr hL
  exact div_neg_of_neg_of_pos hneg hτ

def symmetricRate
    (δ ρ v r τ θ : ℝ) : ℝ :=
  (((1-ρ)*r)*I1 δ + (1-δ)^2*δ*v*(1-θ) - τ*K δ) / L δ

def symmetricFee
    (δ ρ v r τ θ : ℝ) : ℝ :=
  δ*v*(1-θ) - (1-δ)*symmetricRate δ ρ v r τ θ

theorem symmetric_rate_foc
    (δ ρ v r τ θ : ℝ)
    (hτ : τ ≠ 0) (hL : L δ ≠ 0) :
    derivCompact δ ρ v r τ θ θ
      (symmetricRate δ ρ v r τ θ)
      (symmetricRate δ ρ v r τ θ) = 0 := by
  unfold derivCompact symmetricRate
  field_simp [hτ, hL]
  ring

def diDr (δ ρ : ℝ) : ℝ := (1-ρ)*I1 δ / L δ
def dfDr (δ ρ : ℝ) : ℝ := -((1-δ)*(1-ρ)*I1 δ) / L δ

theorem corrected_rate_increases_in_r
    (δ ρ : ℝ)
    (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) (hρ : ρ < 1) :
    0 < diDr δ ρ := by
  unfold diDr
  have hI : 0 < I1 δ := I1_pos δ hδ0 hδ1
  have hL : 0 < L δ := L_pos δ hδ1
  have hrho : 0 < 1-ρ := sub_pos.mpr hρ
  exact div_pos (mul_pos hrho hI) hL

theorem corrected_fee_decreases_in_r
    (δ ρ : ℝ)
    (hδ0 : 0 < δ) (hδ1 : δ < 1) (hρ : ρ < 1) :
    dfDr δ ρ < 0 := by
  unfold dfDr
  have hI : 0 < I1 δ := I1_pos δ hδ0 (le_of_lt hδ1)
  have hL : 0 < L δ := L_pos δ (le_of_lt hδ1)
  have ha : 0 < 1-δ := sub_pos.mpr hδ1
  have hrho : 0 < 1-ρ := sub_pos.mpr hρ
  have hp : 0 < (1-δ)*(1-ρ)*I1 δ := by positivity
  have hn : -((1-δ)*(1-ρ)*I1 δ) < 0 := neg_lt_zero.mpr hp
  exact div_neg_of_neg_of_pos hn hL

theorem exact_counterexample_derivative :
    derivCompact (1/2 : ℝ) 0 1 (1/2) 1 0 0 (-1) (-1) = 5/96 := by
  norm_num [derivCompact, K, L, I1, I2, I3]

theorem exact_corrected_symmetric_rate :
    symmetricRate (1/2 : ℝ) 0 1 (1/2) 1 0 = -3/4 := by
  norm_num [symmetricRate, K, L, I1, I2, I3]

theorem delta_one_endpoint_identity (ρ r τ : ℝ) :
    symmetricRate 1 ρ 0 r τ 1 = (3/2 : ℝ)*((1-ρ)*r-τ) := by
  unfold symmetricRate K L I1 I3
  ring

def policyGap (r v : ℝ) : ℝ :=
  r*(v-r)^2 / (2*(r+v)^2)

theorem policy_gap_positive
    (r v : ℝ) (hr : 0 < r) (hvr : r < v) :
    0 < policyGap r v := by
  unfold policyGap
  have hsum : 0 < r+v := by nlinarith
  have hsq : 0 < (v-r)^2 := sq_pos_of_pos (sub_pos.mpr hvr)
  exact div_pos (mul_pos hr hsq) (by positivity)

def welfareUseful (β τ v r δ ρ : ℝ) : ℝ :=
  β + v/2*(1-δ^2+2*δ*ρ) - τ/4 + δ*(1-ρ)*r

theorem binding_boundary_normal_form
    (β τ v r δ : ℝ) :
    welfareUseful β τ v r δ (δ/2) =
      β + v/2 - τ/4 + r*δ*(1-δ/2) := by
  unfold welfareUseful
  ring

theorem source_policy_welfare_gap
    (β τ v r : ℝ) (hsum : r+v ≠ 0) :
    welfareUseful β τ v r 1 (1/2) -
      welfareUseful β τ v r (2*r/(r+v)) (r/(r+v))
      = policyGap r v := by
  unfold welfareUseful policyGap
  field_simp [hsum]
  ring

#print axioms K_normal_form
#print axioms L_normal_form
#print axioms I1_pos
#print axioms L_pos
#print axioms derivative_decomposition
#print axioms corrected_best_response_foc
#print axioms corrected_hessian_negative
#print axioms symmetric_rate_foc
#print axioms corrected_rate_increases_in_r
#print axioms corrected_fee_decreases_in_r
#print axioms exact_counterexample_derivative
#print axioms exact_corrected_symmetric_rate
#print axioms delta_one_endpoint_identity
#print axioms policy_gap_positive
#print axioms binding_boundary_normal_form
#print axioms source_policy_welfare_gap

end

end LiquidityRegulationCorrection
