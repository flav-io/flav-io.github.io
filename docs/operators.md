---
layout: default
title: Operators
---

# Operator basis

New physics contributions are always defined as contributions to dimension-6
operators in an effective field theory (EFT) below the $W$ mass in the
$\overline{\text{MS}}$ renormalization scheme with naive dimensional regularization.
The operators
are grouped into "sectors" relevant for a particular class of processes.
Operators in one sector close under renormalization, but individual operators
can appear in several "sectors".

## Meson-antimeson mixing (`bsbs`, `bdbd`, `sdsd`)

$$\mathcal H_\text{eff} = - \sum_i C_i O_i$$

The following lists the operators for the case of $B_s$ mixing.

{: class="table"}
Operator                                                                   | Wilson coefficient
---------------------------------------------------------------------------|------------
$O_V^{LL} = (\bar s_L \gamma^\mu b_L)(\bar s_L \gamma_\mu b_L)$            | `CVLL_bsbs`
$O_V^{RR} = (\bar s_R \gamma^\mu b_R)(\bar s_R \gamma_\mu b_R)$            | `CVRR_bsbs`
$O_S^{LL} = (\bar s_R \gamma^\mu b_L)(\bar s_R \gamma_\mu b_L)$            | `CSLL_bsbs`
$O_S^{RR} = (\bar s_L \gamma^\mu b_R)(\bar s_L \gamma_\mu b_R)$            | `CSRR_bsbs`
$O_T^{LL} = (\bar s_R \sigma^{\mu\nu} b_L)(\bar s_R \sigma_{\mu\nu} b_L)$  | `CTLL_bsbs`
$O_T^{RR} = (\bar s_L \sigma^{\mu\nu} b_R)(\bar s_L \sigma_{\mu\nu} b_R)$  | `CTRR_bsbs`
$O_V^{LR} = (\bar s_L \gamma^\mu b_L)(\bar s_R \gamma_\mu b_R)$            | `CVRR_bsbs`
$O_S^{LR} = (\bar s_R \gamma^\mu b_L)(\bar s_L \gamma_\mu b_R)$            | `CSLL_bsbs`


## Semi-leptonic FCNCs (`bsee`, `bdee`, `sdee`, `bsmumu`, ..., `bstautau`, ...)

The following lists the operators for the case of $b\to se^+e^-$.

$$\mathcal H_\text{eff} = - \frac{4 G_F}{\sqrt{2}} V_{tb} V_{ts}^* \sum_i C_i O_i$$

{: class="table"}
Operator                                                                  | Wilson coefficient
--------------------------------------------------------------------------|-------
$O_1 = (\bar s_L \gamma^\mu T^a c_L)(\bar c_L \gamma_\mu T^a b_L)$        | `C1_bsee`
$O_1^\prime = (\bar s_R \gamma^\mu T^a c_R)(\bar c_L \gamma_\mu T^a b_L)$ | `C1p_bsee`
$O_2 = (\bar s_L \gamma^\mu c_L)(\bar c_L \gamma_\mu b_L)$                | `C2_bsee`
$O_2^\prime = (\bar s_R \gamma^\mu c_R)(\bar c_L \gamma_\mu b_L)$         | `C2p_bsee`
$O_3 = (\bar s_L \gamma^\mu b_L)\sum_q(\bar q \gamma_\mu q)$                | `C3_bsee`
$O_3^\prime = (\bar s_R \gamma^\mu b_R)\sum_q(\bar q \gamma_\mu q)$         | `C3p_bsee`
$O_4 = (\bar s_L \gamma^\mu T^a b_L)\sum_q(\bar q \gamma_\mu T^a q)$        | `C4_bsee`
$O_4^\prime = (\bar s_R \gamma^\mu T^a b_R)\sum_q(\bar q \gamma_\mu T^a q)$ | `C4p_bsee`
$O_5 = (\bar s_L \gamma^{\mu_1}\gamma^{\mu_2}\gamma^{\mu_3} b_L)\sum_q(\bar q \gamma_{\mu_1}\gamma_{\mu_2}\gamma_{\mu_3} T^a q)$ | `C5_bsee`
$O_5^\prime  = (\bar s_R \gamma^{\mu_1}\gamma^{\mu_2}\gamma^{\mu_3} b_R)\sum_q(\bar q \gamma_{\mu_1}\gamma_{\mu_2}\gamma_{\mu_3} T^a q)$ | `C5p_bsee`
$O_6 = (\bar s_L \gamma^{\mu_1}\gamma^{\mu_2}\gamma^{\mu_3} T^a b_L)\sum_q(\bar q \gamma_{\mu_1}\gamma_{\mu_2}\gamma_{\mu_3} T^a q)$ | `C6_bsee`
$O_6^\prime  = (\bar s_R \gamma^{\mu_1}\gamma^{\mu_2}\gamma^{\mu_3} T^a b_R)\sum_q(\bar q \gamma_{\mu_1}\gamma_{\mu_2}\gamma_{\mu_3} T^a q)$ | `C6p_bsee`
$O_{3Q} = (\bar s_L \gamma^\mu b_L)\sum_q Q_q (\bar q \gamma_\mu q)$                | `C3Q_bsee`
$O_{3Q}^\prime = (\bar s_R \gamma^\mu b_R)\sum_q Q_q (\bar q \gamma_\mu q)$         | `C3Qp_bsee`
$O_{4Q} = (\bar s_L \gamma^\mu T^a b_L)\sum_q Q_q (\bar q \gamma_\mu T^a q)$        | `C4Q_bsee`
$O_{4Q}^\prime = (\bar s_R \gamma^\mu T^a b_R)\sum_q Q_q (\bar q \gamma_\mu T^a q)$ | `C4Qp_bsee`
$O_{5Q} = (\bar s_L \gamma^{\mu_1}\gamma^{\mu_2}\gamma^{\mu_3} b_L)\sum_q Q_q (\bar q \gamma_{\mu_1}\gamma_{\mu_2}\gamma_{\mu_3} T^a q)$ | `C5Q_bsee`
$O_{5Q}^\prime  = (\bar s_R \gamma^{\mu_1}\gamma^{\mu_2}\gamma^{\mu_3} b_R)\sum_q Q_q (\bar q \gamma_{\mu_1}\gamma_{\mu_2}\gamma_{\mu_3} T^a q)$ | `C5Qp_bsee`
$O_{6Q} = (\bar s_L \gamma^{\mu_1}\gamma^{\mu_2}\gamma^{\mu_3} T^a b_L)\sum_q Q_q (\bar q \gamma_{\mu_1}\gamma_{\mu_2}\gamma_{\mu_3} T^a q)$ | `C6Q_bsee`
$O_{6Q}^\prime  = (\bar s_R \gamma^{\mu_1}\gamma^{\mu_2}\gamma^{\mu_3} T^a b_R)\sum_q Q_q (\bar q \gamma_{\mu_1}\gamma_{\mu_2}\gamma_{\mu_3} T^a q)$ | `C6Qp_bsee`
$O_9 = \frac{e^2}{16\pi^2}(\bar s_L \gamma^\mu b_L)(\bar e \gamma_\mu e)$                    | `C9_bsee`
$O_9^\prime = \frac{e^2}{16\pi^2}(\bar s_R \gamma^\mu b_R)(\bar e \gamma_\mu e)$             | `C9p_bsee`
$O_{10} = \frac{e^2}{16\pi^2}(\bar s_L \gamma^\mu b_L)(\bar e \gamma_\mu\gamma_5 e)$         | `C10_bsee`
$O_{10}^\prime = \frac{e^2}{16\pi^2}(\bar s_R \gamma^\mu b_R)(\bar e \gamma_\mu\gamma_5 e)$  | `C10p_bsee`
$O_S = \frac{e^2}{16\pi^2}m_b(\bar s_L b_R)(\bar e e)$                                       | `CS_bsee`
$O_S^\prime = \frac{e^2}{16\pi^2}m_b(\bar s_R b_L)(\bar e e)$                                | `CSp_bsee`
$O_P = \frac{e^2}{16\pi^2}m_b(\bar s_L b_R)(\bar e \gamma_5 e)$                              | `CP_bsee`
$O_P^\prime = \frac{e^2}{16\pi^2}m_b(\bar s_R b_L)(\bar e \gamma_5 e)$                       | `CPp_bsee`

$T^a$ is a generator of $SU(3)_c$ in the fundamental representation.

In addition, there are the dipole operators

- $O_7 =  \frac{e}{16\pi^2}(\bar s_L \sigma^{\mu\nu} b_R)  F_{\mu\nu}$,
- $O_7^\prime =  \frac{e}{16\pi^2}(\bar s_R \sigma^{\mu\nu} b_L)  F_{\mu\nu}$,
- $O_7 =  \frac{e}{16\pi^2}(\bar s_L \sigma^{\mu\nu} b_R)  T^a  G^a_{\mu\nu}$,
- $O_8^\prime =  \frac{e}{16\pi^2}(\bar s_R \sigma^{\mu\nu} T^a b_L)  G^a_{\mu\nu}$.

For these operators, the effective Wilson coefficients `C7eff_bsee`, `C7effp_bsee`,
`C8eff_bsee`, `C8effp_bsee`, are  used which are defined as

$$C_7^\text{eff} = C_7  + \sum_{i=3}^6 y_i \left[C_i - \frac{1}{3}C_{iQ} \right] $$

$$C_8^\text{eff} = C_8  + \sum_{i=3}^6 z_i \left[C_i - \frac{1}{3}C_{iQ} \right]$$

where
$y=(0,0,-\frac{1}{3},-\frac{4}{9},-\frac{20}{3},-\frac{80}{9})$,
 $z=(0,0,1,-\frac{1}{6},20,-\frac{10}{3})$,
and analogously for the primed  operators.

## Semi-leptonic LFV FCNCs (`bsemu`, `bsmue`, ..., `sdtaumu`, ...)

The following lists the operators for the case of $b\to se^+\mu^-$. Note that these
Wilson coefficients are distinct from the case $b\to s\mu^+e^-$!

$$\mathcal H_\text{eff} = - \frac{4 G_F}{\sqrt{2}} V_{tb} V_{ts}^* \sum_i C_i O_i$$

{: class="table"}
Operator                                                                  | Wilson coefficient
--------------------------------------------------------------------------|-------
$O_9 = \frac{e^2}{16\pi^2}(\bar s_L \gamma^\mu b_L)(\bar e \gamma_\mu \mu)$                    | `C9_bsemu`
$O_9^\prime = \frac{e^2}{16\pi^2}(\bar s_R \gamma^\mu b_R)(\bar e \gamma_\mu \mu)$             | `C9p_bsemu`
$O_{10} = \frac{e^2}{16\pi^2}(\bar s_L \gamma^\mu b_L)(\bar e \gamma_\mu\gamma_5 \mu)$         | `C10_bsemu`
$O_{10}^\prime = \frac{e^2}{16\pi^2}(\bar s_R \gamma^\mu b_R)(\bar e \gamma_\mu\gamma_5 \mu)$  | `C10p_bsemu`
$O_S = \frac{e^2}{16\pi^2}m_b(\bar s_L b_R)(\bar e \mu)$                                       | `CS_bsemu`
$O_S^\prime = \frac{e^2}{16\pi^2}m_b(\bar s_R b_L)(\bar e \mu)$                                | `CSp_bsemu`
$O_P = \frac{e^2}{16\pi^2}m_b(\bar s_L b_R)(\bar e \gamma_5 \mu)$                              | `CP_bsemu`
$O_P^\prime = \frac{e^2}{16\pi^2}m_b(\bar s_R b_L)(\bar e \gamma_5 \mu)$                       | `CPp_bsemu`

## Charged-current decays (`buenu`, ..., `bctaunu`, ...,)

The following lists the operators for the case of $b\to c\tau^-\bar\nu$.

$$\mathcal H_\text{eff} = - \frac{4 G_F}{\sqrt{2}} V_{cb} \sum_i C_i O_i$$

{: class="table"}
Operator                                                                  | Wilson coefficient
--------------------------------------------------------------------------|-------
$O_V = (\bar c_L \gamma^\mu b_L)(\bar \tau_L \gamma_\mu \nu_L)$           | `CV_bctaunu`
$O_V^\prime = (\bar c_R \gamma^\mu b_R)(\bar \tau_L \gamma_\mu \nu_L)$    | `CVp_bctaunu`
$O_S = m_b(\bar c_L b_R)(\bar \tau \nu)$                                  | `CS_bctaunu`
$O_S^\prime = m_b(\bar c_R b_L)(\bar \tau_R \nu_L)$                       | `CSp_bctaunu`
$O_T = (\bar c_L \sigma^{\mu\nu} b_R)(\bar \tau_R \sigma_{\mu\nu}\nu_L)$  | `CT_bctaunu`
