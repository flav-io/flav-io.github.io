---
layout: default
title: Observables
---

# List of all observables

The table below is an automatically generated list of all observables currently
implemented in flavio. The first column is the string name that must  be used
when calling functions such as `flavio.sm_prediction`. The last column lists
the arguments the observable depends on (which can also be empty in case of
a scalar observable).

Some general notes on conventions:

- Unless noted explicitly, branching ratios and angular observables always
imply a *CP-average*. For instance, charged $B$ decay modes are always written as
$B^+ \to \ldots$, but what is meant is the average of the $B^+$ and the $B^-$
decay.
- *"Binned branching ratio"* refers to the $q^2$-integral of the differential branching
ratio, which is a dimensionless number and which coincides with the total branching
ratio if the bin spans the whole kinematic domain. *"Binned differential branching ratio"*
refers instead to the binned branching ratio divided by the bin width, which
has units of GeV$^{-2}$. This definition is frequently used by LHCb and has the
advantage that it is easier  to  compare results in the same kinematic region
but with different bin sizes.
- The conventions for $B\to V\ell^+\ell^-$ angular observables follow the ones
used by LHCb, which differ from the ones used in many theory papers,
e.g. for $A_\text{FB}$, $S_4$, $P_4^\prime$, $A_7$, $A_9$
(see e.g. [arXiv:1506.03970](http://www.arxiv.org/abs/1506.03970)).
- Lepton flavour $\ell$ always refers to an average of electron and muon modes.


{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<A3>(B+->K*ee)` | $\langle A_3\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `A3(B+->K*ee)` | $A_3(B^+\to K^{\ast +}e^+e^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<A4>(B+->K*ee)` | $\langle A_4\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `A4(B+->K*ee)` | $A_4(B^+\to K^{\ast +}e^+e^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<A5>(B+->K*ee)` | $\langle A_5\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `A5(B+->K*ee)` | $A_5(B^+\to K^{\ast +}e^+e^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<A6s>(B+->K*ee)` | $\langle A_6^s\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `A6s(B+->K*ee)` | $A_6^s(B^+\to K^{\ast +}e^+e^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<A7>(B+->K*ee)` | $\langle A_7\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `A7(B+->K*ee)` | $A_7(B^+\to K^{\ast +}e^+e^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<A8>(B+->K*ee)` | $\langle A_8\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `A8(B+->K*ee)` | $A_8(B^+\to K^{\ast +}e^+e^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<A9>(B+->K*ee)` | $\langle A_9\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `A9(B+->K*ee)` | $A_9(B^+\to K^{\ast +}e^+e^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<AFB>(B+->K*ee)` | $\langle A_\text{FB}\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned forward-backward asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `AFB(B+->K*ee)` | $A_\text{FB}(B^+\to K^{\ast +}e^+e^-)$ | Forward-backward asymmetry in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<FL>(B+->K*ee)` | $\langle F_L\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned longitudinal polarization fraction in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `FL(B+->K*ee)` | $F_L(B^+\to K^{\ast +}e^+e^-)$ | Longitudinal polarization fraction in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<S3>(B+->K*ee)` | $\langle S_3\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `S3(B+->K*ee)` | $S_3(B^+\to K^{\ast +}e^+e^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<S4>(B+->K*ee)` | $\langle S_4\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `S4(B+->K*ee)` | $S_4(B^+\to K^{\ast +}e^+e^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<S5>(B+->K*ee)` | $\langle S_5\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `S5(B+->K*ee)` | $S_5(B^+\to K^{\ast +}e^+e^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<S7>(B+->K*ee)` | $\langle S_7\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `S7(B+->K*ee)` | $S_7(B^+\to K^{\ast +}e^+e^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<S8>(B+->K*ee)` | $\langle S_8\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `S8(B+->K*ee)` | $S_8(B^+\to K^{\ast +}e^+e^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<S9>(B+->K*ee)` | $\langle S_9\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `S9(B+->K*ee)` | $S_9(B^+\to K^{\ast +}e^+e^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<P4p>(B+->K*ee)` | $\langle P_4^\prime\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `P4p(B+->K*ee)` | $P_4^\prime(B^+\to K^{\ast +}e^+e^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<P5p>(B+->K*ee)` | $\langle P_5^\prime\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `P5p(B+->K*ee)` | $P_5^\prime(B^+\to K^{\ast +}e^+e^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<P6p>(B+->K*ee)` | $\langle P_6^\prime\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `P6p(B+->K*ee)` | $P_6^\prime(B^+\to K^{\ast +}e^+e^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<P8p>(B+->K*ee)` | $\langle P_8^\prime\rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `P8p(B+->K*ee)` | $P_8^\prime(B^+\to K^{\ast +}e^+e^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<dBR/dq2>(B+->K*ee)` | $\langle \text{BR} \rangle(B^+\to K^{\ast +}e^+e^-)$ | Binned differential branching ratio of $B^+\to K^{\ast +}e^+e^-$ | `q2min`, `q2max` |
| `dBR/dq2(B+->K*ee)` | $\frac{d\text{BR}}{dq^2}(B^+\to K^{\ast +}e^+e^-)$ | Differntial branching ratio of $B^+\to K^{\ast +}e^+e^-$ | `q2` |
| `<A3>(B0->K*ee)` | $\langle A_3\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `A3(B0->K*ee)` | $A_3(B^0\to K^{\ast 0}e^+e^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<A4>(B0->K*ee)` | $\langle A_4\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `A4(B0->K*ee)` | $A_4(B^0\to K^{\ast 0}e^+e^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<A5>(B0->K*ee)` | $\langle A_5\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `A5(B0->K*ee)` | $A_5(B^0\to K^{\ast 0}e^+e^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<A6s>(B0->K*ee)` | $\langle A_6^s\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `A6s(B0->K*ee)` | $A_6^s(B^0\to K^{\ast 0}e^+e^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<A7>(B0->K*ee)` | $\langle A_7\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `A7(B0->K*ee)` | $A_7(B^0\to K^{\ast 0}e^+e^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<A8>(B0->K*ee)` | $\langle A_8\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `A8(B0->K*ee)` | $A_8(B^0\to K^{\ast 0}e^+e^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<A9>(B0->K*ee)` | $\langle A_9\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `A9(B0->K*ee)` | $A_9(B^0\to K^{\ast 0}e^+e^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<AFB>(B0->K*ee)` | $\langle A_\text{FB}\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned forward-backward asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `AFB(B0->K*ee)` | $A_\text{FB}(B^0\to K^{\ast 0}e^+e^-)$ | Forward-backward asymmetry in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<FL>(B0->K*ee)` | $\langle F_L\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned longitudinal polarization fraction in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `FL(B0->K*ee)` | $F_L(B^0\to K^{\ast 0}e^+e^-)$ | Longitudinal polarization fraction in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<S3>(B0->K*ee)` | $\langle S_3\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `S3(B0->K*ee)` | $S_3(B^0\to K^{\ast 0}e^+e^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<S4>(B0->K*ee)` | $\langle S_4\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `S4(B0->K*ee)` | $S_4(B^0\to K^{\ast 0}e^+e^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<S5>(B0->K*ee)` | $\langle S_5\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `S5(B0->K*ee)` | $S_5(B^0\to K^{\ast 0}e^+e^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<S7>(B0->K*ee)` | $\langle S_7\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `S7(B0->K*ee)` | $S_7(B^0\to K^{\ast 0}e^+e^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<S8>(B0->K*ee)` | $\langle S_8\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `S8(B0->K*ee)` | $S_8(B^0\to K^{\ast 0}e^+e^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<S9>(B0->K*ee)` | $\langle S_9\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `S9(B0->K*ee)` | $S_9(B^0\to K^{\ast 0}e^+e^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<P4p>(B0->K*ee)` | $\langle P_4^\prime\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `P4p(B0->K*ee)` | $P_4^\prime(B^0\to K^{\ast 0}e^+e^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<P5p>(B0->K*ee)` | $\langle P_5^\prime\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `P5p(B0->K*ee)` | $P_5^\prime(B^0\to K^{\ast 0}e^+e^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<P6p>(B0->K*ee)` | $\langle P_6^\prime\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `P6p(B0->K*ee)` | $P_6^\prime(B^0\to K^{\ast 0}e^+e^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<P8p>(B0->K*ee)` | $\langle P_8^\prime\rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `P8p(B0->K*ee)` | $P_8^\prime(B^0\to K^{\ast 0}e^+e^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<dBR/dq2>(B0->K*ee)` | $\langle \text{BR} \rangle(B^0\to K^{\ast 0}e^+e^-)$ | Binned differential branching ratio of $B^0\to K^{\ast 0}e^+e^-$ | `q2min`, `q2max` |
| `dBR/dq2(B0->K*ee)` | $\frac{d\text{BR}}{dq^2}(B^0\to K^{\ast 0}e^+e^-)$ | Differntial branching ratio of $B^0\to K^{\ast 0}e^+e^-$ | `q2` |
| `<A3>(B+->K*mumu)` | $\langle A_3\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A3(B+->K*mumu)` | $A_3(B^+\to K^{\ast +}\mu^+\mu^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<A4>(B+->K*mumu)` | $\langle A_4\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A4(B+->K*mumu)` | $A_4(B^+\to K^{\ast +}\mu^+\mu^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<A5>(B+->K*mumu)` | $\langle A_5\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A5(B+->K*mumu)` | $A_5(B^+\to K^{\ast +}\mu^+\mu^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<A6s>(B+->K*mumu)` | $\langle A_6^s\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A6s(B+->K*mumu)` | $A_6^s(B^+\to K^{\ast +}\mu^+\mu^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<A7>(B+->K*mumu)` | $\langle A_7\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A7(B+->K*mumu)` | $A_7(B^+\to K^{\ast +}\mu^+\mu^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<A8>(B+->K*mumu)` | $\langle A_8\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A8(B+->K*mumu)` | $A_8(B^+\to K^{\ast +}\mu^+\mu^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<A9>(B+->K*mumu)` | $\langle A_9\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A9(B+->K*mumu)` | $A_9(B^+\to K^{\ast +}\mu^+\mu^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<AFB>(B+->K*mumu)` | $\langle A_\text{FB}\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned forward-backward asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `AFB(B+->K*mumu)` | $A_\text{FB}(B^+\to K^{\ast +}\mu^+\mu^-)$ | Forward-backward asymmetry in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<FL>(B+->K*mumu)` | $\langle F_L\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned longitudinal polarization fraction in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `FL(B+->K*mumu)` | $F_L(B^+\to K^{\ast +}\mu^+\mu^-)$ | Longitudinal polarization fraction in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<S3>(B+->K*mumu)` | $\langle S_3\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S3(B+->K*mumu)` | $S_3(B^+\to K^{\ast +}\mu^+\mu^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<S4>(B+->K*mumu)` | $\langle S_4\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S4(B+->K*mumu)` | $S_4(B^+\to K^{\ast +}\mu^+\mu^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<S5>(B+->K*mumu)` | $\langle S_5\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S5(B+->K*mumu)` | $S_5(B^+\to K^{\ast +}\mu^+\mu^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<S7>(B+->K*mumu)` | $\langle S_7\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S7(B+->K*mumu)` | $S_7(B^+\to K^{\ast +}\mu^+\mu^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<S8>(B+->K*mumu)` | $\langle S_8\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S8(B+->K*mumu)` | $S_8(B^+\to K^{\ast +}\mu^+\mu^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<S9>(B+->K*mumu)` | $\langle S_9\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S9(B+->K*mumu)` | $S_9(B^+\to K^{\ast +}\mu^+\mu^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<P4p>(B+->K*mumu)` | $\langle P_4^\prime\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `P4p(B+->K*mumu)` | $P_4^\prime(B^+\to K^{\ast +}\mu^+\mu^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<P5p>(B+->K*mumu)` | $\langle P_5^\prime\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `P5p(B+->K*mumu)` | $P_5^\prime(B^+\to K^{\ast +}\mu^+\mu^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<P6p>(B+->K*mumu)` | $\langle P_6^\prime\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `P6p(B+->K*mumu)` | $P_6^\prime(B^+\to K^{\ast +}\mu^+\mu^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<P8p>(B+->K*mumu)` | $\langle P_8^\prime\rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `P8p(B+->K*mumu)` | $P_8^\prime(B^+\to K^{\ast +}\mu^+\mu^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<dBR/dq2>(B+->K*mumu)` | $\langle \text{BR} \rangle(B^+\to K^{\ast +}\mu^+\mu^-)$ | Binned differential branching ratio of $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2min`, `q2max` |
| `dBR/dq2(B+->K*mumu)` | $\frac{d\text{BR}}{dq^2}(B^+\to K^{\ast +}\mu^+\mu^-)$ | Differntial branching ratio of $B^+\to K^{\ast +}\mu^+\mu^-$ | `q2` |
| `<A3>(B0->K*mumu)` | $\langle A_3\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A3(B0->K*mumu)` | $A_3(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<A4>(B0->K*mumu)` | $\langle A_4\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A4(B0->K*mumu)` | $A_4(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<A5>(B0->K*mumu)` | $\langle A_5\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A5(B0->K*mumu)` | $A_5(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<A6s>(B0->K*mumu)` | $\langle A_6^s\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A6s(B0->K*mumu)` | $A_6^s(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<A7>(B0->K*mumu)` | $\langle A_7\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A7(B0->K*mumu)` | $A_7(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<A8>(B0->K*mumu)` | $\langle A_8\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A8(B0->K*mumu)` | $A_8(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<A9>(B0->K*mumu)` | $\langle A_9\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `A9(B0->K*mumu)` | $A_9(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<AFB>(B0->K*mumu)` | $\langle A_\text{FB}\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned forward-backward asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `AFB(B0->K*mumu)` | $A_\text{FB}(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Forward-backward asymmetry in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<FL>(B0->K*mumu)` | $\langle F_L\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned longitudinal polarization fraction in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `FL(B0->K*mumu)` | $F_L(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Longitudinal polarization fraction in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<S3>(B0->K*mumu)` | $\langle S_3\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S3(B0->K*mumu)` | $S_3(B^0\to K^{\ast 0}\mu^+\mu^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<S4>(B0->K*mumu)` | $\langle S_4\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S4(B0->K*mumu)` | $S_4(B^0\to K^{\ast 0}\mu^+\mu^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<S5>(B0->K*mumu)` | $\langle S_5\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S5(B0->K*mumu)` | $S_5(B^0\to K^{\ast 0}\mu^+\mu^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<S7>(B0->K*mumu)` | $\langle S_7\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S7(B0->K*mumu)` | $S_7(B^0\to K^{\ast 0}\mu^+\mu^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<S8>(B0->K*mumu)` | $\langle S_8\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S8(B0->K*mumu)` | $S_8(B^0\to K^{\ast 0}\mu^+\mu^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<S9>(B0->K*mumu)` | $\langle S_9\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `S9(B0->K*mumu)` | $S_9(B^0\to K^{\ast 0}\mu^+\mu^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<P4p>(B0->K*mumu)` | $\langle P_4^\prime\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `P4p(B0->K*mumu)` | $P_4^\prime(B^0\to K^{\ast 0}\mu^+\mu^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<P5p>(B0->K*mumu)` | $\langle P_5^\prime\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `P5p(B0->K*mumu)` | $P_5^\prime(B^0\to K^{\ast 0}\mu^+\mu^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<P6p>(B0->K*mumu)` | $\langle P_6^\prime\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `P6p(B0->K*mumu)` | $P_6^\prime(B^0\to K^{\ast 0}\mu^+\mu^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<P8p>(B0->K*mumu)` | $\langle P_8^\prime\rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `P8p(B0->K*mumu)` | $P_8^\prime(B^0\to K^{\ast 0}\mu^+\mu^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<dBR/dq2>(B0->K*mumu)` | $\langle \text{BR} \rangle(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Binned differential branching ratio of $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2min`, `q2max` |
| `dBR/dq2(B0->K*mumu)` | $\frac{d\text{BR}}{dq^2}(B^0\to K^{\ast 0}\mu^+\mu^-)$ | Differntial branching ratio of $B^0\to K^{\ast 0}\mu^+\mu^-$ | `q2` |
| `<A3>(B+->K*tautau)` | $\langle A_3\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A3(B+->K*tautau)` | $A_3(B^+\to K^{\ast +}\tau^+\tau^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<A4>(B+->K*tautau)` | $\langle A_4\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A4(B+->K*tautau)` | $A_4(B^+\to K^{\ast +}\tau^+\tau^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<A5>(B+->K*tautau)` | $\langle A_5\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A5(B+->K*tautau)` | $A_5(B^+\to K^{\ast +}\tau^+\tau^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<A6s>(B+->K*tautau)` | $\langle A_6^s\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A6s(B+->K*tautau)` | $A_6^s(B^+\to K^{\ast +}\tau^+\tau^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<A7>(B+->K*tautau)` | $\langle A_7\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A7(B+->K*tautau)` | $A_7(B^+\to K^{\ast +}\tau^+\tau^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<A8>(B+->K*tautau)` | $\langle A_8\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A8(B+->K*tautau)` | $A_8(B^+\to K^{\ast +}\tau^+\tau^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<A9>(B+->K*tautau)` | $\langle A_9\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A9(B+->K*tautau)` | $A_9(B^+\to K^{\ast +}\tau^+\tau^-)$ | Angular CP asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<AFB>(B+->K*tautau)` | $\langle A_\text{FB}\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned forward-backward asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `AFB(B+->K*tautau)` | $A_\text{FB}(B^+\to K^{\ast +}\tau^+\tau^-)$ | Forward-backward asymmetry in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<FL>(B+->K*tautau)` | $\langle F_L\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned longitudinal polarization fraction in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `FL(B+->K*tautau)` | $F_L(B^+\to K^{\ast +}\tau^+\tau^-)$ | Longitudinal polarization fraction in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<S3>(B+->K*tautau)` | $\langle S_3\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S3(B+->K*tautau)` | $S_3(B^+\to K^{\ast +}\tau^+\tau^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<S4>(B+->K*tautau)` | $\langle S_4\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S4(B+->K*tautau)` | $S_4(B^+\to K^{\ast +}\tau^+\tau^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<S5>(B+->K*tautau)` | $\langle S_5\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S5(B+->K*tautau)` | $S_5(B^+\to K^{\ast +}\tau^+\tau^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<S7>(B+->K*tautau)` | $\langle S_7\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S7(B+->K*tautau)` | $S_7(B^+\to K^{\ast +}\tau^+\tau^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<S8>(B+->K*tautau)` | $\langle S_8\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S8(B+->K*tautau)` | $S_8(B^+\to K^{\ast +}\tau^+\tau^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<S9>(B+->K*tautau)` | $\langle S_9\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S9(B+->K*tautau)` | $S_9(B^+\to K^{\ast +}\tau^+\tau^-)$ | CP-averaged angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<P4p>(B+->K*tautau)` | $\langle P_4^\prime\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `P4p(B+->K*tautau)` | $P_4^\prime(B^+\to K^{\ast +}\tau^+\tau^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<P5p>(B+->K*tautau)` | $\langle P_5^\prime\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `P5p(B+->K*tautau)` | $P_5^\prime(B^+\to K^{\ast +}\tau^+\tau^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<P6p>(B+->K*tautau)` | $\langle P_6^\prime\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `P6p(B+->K*tautau)` | $P_6^\prime(B^+\to K^{\ast +}\tau^+\tau^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<P8p>(B+->K*tautau)` | $\langle P_8^\prime\rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `P8p(B+->K*tautau)` | $P_8^\prime(B^+\to K^{\ast +}\tau^+\tau^-)$ | CP-averaged "optimized" angular observable in $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<dBR/dq2>(B+->K*tautau)` | $\langle \text{BR} \rangle(B^+\to K^{\ast +}\tau^+\tau^-)$ | Binned differential branching ratio of $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2min`, `q2max` |
| `dBR/dq2(B+->K*tautau)` | $\frac{d\text{BR}}{dq^2}(B^+\to K^{\ast +}\tau^+\tau^-)$ | Differntial branching ratio of $B^+\to K^{\ast +}\tau^+\tau^-$ | `q2` |
| `<A3>(B0->K*tautau)` | $\langle A_3\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A3(B0->K*tautau)` | $A_3(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<A4>(B0->K*tautau)` | $\langle A_4\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A4(B0->K*tautau)` | $A_4(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<A5>(B0->K*tautau)` | $\langle A_5\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A5(B0->K*tautau)` | $A_5(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<A6s>(B0->K*tautau)` | $\langle A_6^s\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A6s(B0->K*tautau)` | $A_6^s(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<A7>(B0->K*tautau)` | $\langle A_7\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A7(B0->K*tautau)` | $A_7(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<A8>(B0->K*tautau)` | $\langle A_8\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A8(B0->K*tautau)` | $A_8(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<A9>(B0->K*tautau)` | $\langle A_9\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `A9(B0->K*tautau)` | $A_9(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Angular CP asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<AFB>(B0->K*tautau)` | $\langle A_\text{FB}\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned forward-backward asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `AFB(B0->K*tautau)` | $A_\text{FB}(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Forward-backward asymmetry in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<FL>(B0->K*tautau)` | $\langle F_L\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned longitudinal polarization fraction in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `FL(B0->K*tautau)` | $F_L(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Longitudinal polarization fraction in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<S3>(B0->K*tautau)` | $\langle S_3\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S3(B0->K*tautau)` | $S_3(B^0\to K^{\ast 0}\tau^+\tau^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<S4>(B0->K*tautau)` | $\langle S_4\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S4(B0->K*tautau)` | $S_4(B^0\to K^{\ast 0}\tau^+\tau^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<S5>(B0->K*tautau)` | $\langle S_5\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S5(B0->K*tautau)` | $S_5(B^0\to K^{\ast 0}\tau^+\tau^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<S7>(B0->K*tautau)` | $\langle S_7\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S7(B0->K*tautau)` | $S_7(B^0\to K^{\ast 0}\tau^+\tau^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<S8>(B0->K*tautau)` | $\langle S_8\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S8(B0->K*tautau)` | $S_8(B^0\to K^{\ast 0}\tau^+\tau^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<S9>(B0->K*tautau)` | $\langle S_9\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `S9(B0->K*tautau)` | $S_9(B^0\to K^{\ast 0}\tau^+\tau^-)$ | CP-averaged angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<P4p>(B0->K*tautau)` | $\langle P_4^\prime\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `P4p(B0->K*tautau)` | $P_4^\prime(B^0\to K^{\ast 0}\tau^+\tau^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<P5p>(B0->K*tautau)` | $\langle P_5^\prime\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `P5p(B0->K*tautau)` | $P_5^\prime(B^0\to K^{\ast 0}\tau^+\tau^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<P6p>(B0->K*tautau)` | $\langle P_6^\prime\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `P6p(B0->K*tautau)` | $P_6^\prime(B^0\to K^{\ast 0}\tau^+\tau^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<P8p>(B0->K*tautau)` | $\langle P_8^\prime\rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `P8p(B0->K*tautau)` | $P_8^\prime(B^0\to K^{\ast 0}\tau^+\tau^-)$ | CP-averaged "optimized" angular observable in $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<dBR/dq2>(B0->K*tautau)` | $\langle \text{BR} \rangle(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Binned differential branching ratio of $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2min`, `q2max` |
| `dBR/dq2(B0->K*tautau)` | $\frac{d\text{BR}}{dq^2}(B^0\to K^{\ast 0}\tau^+\tau^-)$ | Differntial branching ratio of $B^0\to K^{\ast 0}\tau^+\tau^-$ | `q2` |
| `<Rmue>(B+->K*ll)` | $\langle R_{\mu e} \rangle(B^+\to K^{\ast +}\ell^+\ell^-)$ | Ratio of partial branching ratios of $B^+\to K^{\ast +}\mu^+ \mu^-$ and $B^+\to K^{\ast +}e^+ e^-$ | `q2min`, `q2max` |
| `<Rmue>(B0->K*ll)` | $\langle R_{\mu e} \rangle(B^0\to K^{\ast 0}\ell^+\ell^-)$ | Ratio of partial branching ratios of $B^0\to K^{\ast 0}\mu^+ \mu^-$ and $B^0\to K^{\ast 0}e^+ e^-$ | `q2min`, `q2max` |
| `<Rtaumu>(B+->K*ll)` | $\langle R_{\tau \mu} \rangle(B^+\to K^{\ast +}\ell^+\ell^-)$ | Ratio of partial branching ratios of $B^+\to K^{\ast +}\tau^+ \tau^-$ and $B^+\to K^{\ast +}\mu^+ \mu^-$ | `q2min`, `q2max` |
| `<Rtaumu>(B0->K*ll)` | $\langle R_{\tau \mu} \rangle(B^0\to K^{\ast 0}\ell^+\ell^-)$ | Ratio of partial branching ratios of $B^0\to K^{\ast 0}\tau^+ \tau^-$ and $B^0\to K^{\ast 0}\mu^+ \mu^-$ | `q2min`, `q2max` |
| `BR(B+->K*emu)` | $\text{BR}(B^+\to K^{*+} e^+\mu^-)$ | Total branching ratio of $B^+\to K^{*+} e^+\mu^-$ |  |
| `BR(B0->K*emu)` | $\text{BR}(B^0\to K^{*0} e^+\mu^-)$ | Total branching ratio of $B^0\to K^{*0} e^+\mu^-$ |  |
| `BR(B0->rhoemu)` | $\text{BR}(B^0\to \rho^{0} e^+\mu^-)$ | Total branching ratio of $B^0\to \rho^{0} e^+\mu^-$ |  |
| `BR(Bs->phiemu)` | $\text{BR}(B_s\to \phi e^+\mu^-)$ | Total branching ratio of $B_s\to \phi e^+\mu^-$ |  |
| `BR(B+->rhoemu)` | $\text{BR}(B^+\to \rho^{+} e^+\mu^-)$ | Total branching ratio of $B^+\to \rho^{+} e^+\mu^-$ |  |
| `BR(B+->K*mue)` | $\text{BR}(B^+\to K^{*+} \mu^+e^-)$ | Total branching ratio of $B^+\to K^{*+} \mu^+e^-$ |  |
| `BR(B0->K*mue)` | $\text{BR}(B^0\to K^{*0} \mu^+e^-)$ | Total branching ratio of $B^0\to K^{*0} \mu^+e^-$ |  |
| `BR(B0->rhomue)` | $\text{BR}(B^0\to \rho^{0} \mu^+e^-)$ | Total branching ratio of $B^0\to \rho^{0} \mu^+e^-$ |  |
| `BR(Bs->phimue)` | $\text{BR}(B_s\to \phi \mu^+e^-)$ | Total branching ratio of $B_s\to \phi \mu^+e^-$ |  |
| `BR(B+->rhomue)` | $\text{BR}(B^+\to \rho^{+} \mu^+e^-)$ | Total branching ratio of $B^+\to \rho^{+} \mu^+e^-$ |  |
| `BR(B+->K*etau)` | $\text{BR}(B^+\to K^{*+} e^+\tau^-)$ | Total branching ratio of $B^+\to K^{*+} e^+\tau^-$ |  |
| `BR(B0->K*etau)` | $\text{BR}(B^0\to K^{*0} e^+\tau^-)$ | Total branching ratio of $B^0\to K^{*0} e^+\tau^-$ |  |
| `BR(B0->rhoetau)` | $\text{BR}(B^0\to \rho^{0} e^+\tau^-)$ | Total branching ratio of $B^0\to \rho^{0} e^+\tau^-$ |  |
| `BR(Bs->phietau)` | $\text{BR}(B_s\to \phi e^+\tau^-)$ | Total branching ratio of $B_s\to \phi e^+\tau^-$ |  |
| `BR(B+->rhoetau)` | $\text{BR}(B^+\to \rho^{+} e^+\tau^-)$ | Total branching ratio of $B^+\to \rho^{+} e^+\tau^-$ |  |
| `BR(B+->K*taue)` | $\text{BR}(B^+\to K^{*+} \tau^+e^-)$ | Total branching ratio of $B^+\to K^{*+} \tau^+e^-$ |  |
| `BR(B0->K*taue)` | $\text{BR}(B^0\to K^{*0} \tau^+e^-)$ | Total branching ratio of $B^0\to K^{*0} \tau^+e^-$ |  |
| `BR(B0->rhotaue)` | $\text{BR}(B^0\to \rho^{0} \tau^+e^-)$ | Total branching ratio of $B^0\to \rho^{0} \tau^+e^-$ |  |
| `BR(Bs->phitaue)` | $\text{BR}(B_s\to \phi \tau^+e^-)$ | Total branching ratio of $B_s\to \phi \tau^+e^-$ |  |
| `BR(B+->rhotaue)` | $\text{BR}(B^+\to \rho^{+} \tau^+e^-)$ | Total branching ratio of $B^+\to \rho^{+} \tau^+e^-$ |  |
| `BR(B+->K*mutau)` | $\text{BR}(B^+\to K^{*+} \mu^+\tau^-)$ | Total branching ratio of $B^+\to K^{*+} \mu^+\tau^-$ |  |
| `BR(B0->K*mutau)` | $\text{BR}(B^0\to K^{*0} \mu^+\tau^-)$ | Total branching ratio of $B^0\to K^{*0} \mu^+\tau^-$ |  |
| `BR(B0->rhomutau)` | $\text{BR}(B^0\to \rho^{0} \mu^+\tau^-)$ | Total branching ratio of $B^0\to \rho^{0} \mu^+\tau^-$ |  |
| `BR(Bs->phimutau)` | $\text{BR}(B_s\to \phi \mu^+\tau^-)$ | Total branching ratio of $B_s\to \phi \mu^+\tau^-$ |  |
| `BR(B+->rhomutau)` | $\text{BR}(B^+\to \rho^{+} \mu^+\tau^-)$ | Total branching ratio of $B^+\to \rho^{+} \mu^+\tau^-$ |  |
| `BR(B+->K*taumu)` | $\text{BR}(B^+\to K^{*+} \tau^+\mu^-)$ | Total branching ratio of $B^+\to K^{*+} \tau^+\mu^-$ |  |
| `BR(B0->K*taumu)` | $\text{BR}(B^0\to K^{*0} \tau^+\mu^-)$ | Total branching ratio of $B^0\to K^{*0} \tau^+\mu^-$ |  |
| `BR(B0->rhotaumu)` | $\text{BR}(B^0\to \rho^{0} \tau^+\mu^-)$ | Total branching ratio of $B^0\to \rho^{0} \tau^+\mu^-$ |  |
| `BR(Bs->phitaumu)` | $\text{BR}(B_s\to \phi \tau^+\mu^-)$ | Total branching ratio of $B_s\to \phi \tau^+\mu^-$ |  |
| `BR(B+->rhotaumu)` | $\text{BR}(B^+\to \rho^{+} \tau^+\mu^-)$ | Total branching ratio of $B^+\to \rho^{+} \tau^+\mu^-$ |  |
| `dBR/dq2(B+->D*enu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{*0}e^+\nu_e)$ | Differential branching ratio of $B^+\to D^{*0}e^+\nu_e$ | `q2` |
| `dBR/dq2(B0->D*enu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{*-}e^+\nu_e)$ | Differential branching ratio of $B^0\to D^{*-}e^+\nu_e$ | `q2` |
| `dBR/dq2(Bs->K*enu)` | $\frac{d\text{BR}}{dq^2}(B_s\to K^{*-}e^+\nu_e)$ | Differential branching ratio of $B_s\to K^{*-}e^+\nu_e$ | `q2` |
| `dBR/dq2(B+->rhoenu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \rho^0e^+\nu_e)$ | Differential branching ratio of $B^+\to \rho^0e^+\nu_e$ | `q2` |
| `dBR/dq2(B0->rhoenu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \rho^-e^+\nu_e)$ | Differential branching ratio of $B^0\to \rho^-e^+\nu_e$ | `q2` |
| `BR(B+->D*enu)` | $\text{BR}(B^+\to D^{*0}e^+\nu_e)$ | Total branching ratio of $B^+\to D^{*0}e^+\nu_e$ |  |
| `BR(B0->D*enu)` | $\text{BR}(B^0\to D^{*-}e^+\nu_e)$ | Total branching ratio of $B^0\to D^{*-}e^+\nu_e$ |  |
| `BR(Bs->K*enu)` | $\text{BR}(B_s\to K^{*-}e^+\nu_e)$ | Total branching ratio of $B_s\to K^{*-}e^+\nu_e$ |  |
| `BR(B+->rhoenu)` | $\text{BR}(B^+\to \rho^0e^+\nu_e)$ | Total branching ratio of $B^+\to \rho^0e^+\nu_e$ |  |
| `BR(B0->rhoenu)` | $\text{BR}(B^0\to \rho^-e^+\nu_e)$ | Total branching ratio of $B^0\to \rho^-e^+\nu_e$ |  |
| `<BR>(B+->D*enu)` | $\langle\text{BR}\rangle(B^+\to D^{*0}e^+\nu_e)$ | Binned branching ratio of $B^+\to D^{*0}e^+\nu_e$ | `q2min`, `q2max` |
| `<BR>(B0->D*enu)` | $\langle\text{BR}\rangle(B^0\to D^{*-}e^+\nu_e)$ | Binned branching ratio of $B^0\to D^{*-}e^+\nu_e$ | `q2min`, `q2max` |
| `<BR>(Bs->K*enu)` | $\langle\text{BR}\rangle(B_s\to K^{*-}e^+\nu_e)$ | Binned branching ratio of $B_s\to K^{*-}e^+\nu_e$ | `q2min`, `q2max` |
| `<BR>(B+->rhoenu)` | $\langle\text{BR}\rangle(B^+\to \rho^0e^+\nu_e)$ | Binned branching ratio of $B^+\to \rho^0e^+\nu_e$ | `q2min`, `q2max` |
| `<BR>(B0->rhoenu)` | $\langle\text{BR}\rangle(B^0\to \rho^-e^+\nu_e)$ | Binned branching ratio of $B^0\to \rho^-e^+\nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B+->D*munu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{*0}\mu^+\nu_\mu)$ | Differential branching ratio of $B^+\to D^{*0}\mu^+\nu_\mu$ | `q2` |
| `dBR/dq2(B0->D*munu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{*-}\mu^+\nu_\mu)$ | Differential branching ratio of $B^0\to D^{*-}\mu^+\nu_\mu$ | `q2` |
| `dBR/dq2(Bs->K*munu)` | $\frac{d\text{BR}}{dq^2}(B_s\to K^{*-}\mu^+\nu_\mu)$ | Differential branching ratio of $B_s\to K^{*-}\mu^+\nu_\mu$ | `q2` |
| `dBR/dq2(B+->rhomunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \rho^0\mu^+\nu_\mu)$ | Differential branching ratio of $B^+\to \rho^0\mu^+\nu_\mu$ | `q2` |
| `dBR/dq2(B0->rhomunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \rho^-\mu^+\nu_\mu)$ | Differential branching ratio of $B^0\to \rho^-\mu^+\nu_\mu$ | `q2` |
| `BR(B+->D*munu)` | $\text{BR}(B^+\to D^{*0}\mu^+\nu_\mu)$ | Total branching ratio of $B^+\to D^{*0}\mu^+\nu_\mu$ |  |
| `BR(B0->D*munu)` | $\text{BR}(B^0\to D^{*-}\mu^+\nu_\mu)$ | Total branching ratio of $B^0\to D^{*-}\mu^+\nu_\mu$ |  |
| `BR(Bs->K*munu)` | $\text{BR}(B_s\to K^{*-}\mu^+\nu_\mu)$ | Total branching ratio of $B_s\to K^{*-}\mu^+\nu_\mu$ |  |
| `BR(B+->rhomunu)` | $\text{BR}(B^+\to \rho^0\mu^+\nu_\mu)$ | Total branching ratio of $B^+\to \rho^0\mu^+\nu_\mu$ |  |
| `BR(B0->rhomunu)` | $\text{BR}(B^0\to \rho^-\mu^+\nu_\mu)$ | Total branching ratio of $B^0\to \rho^-\mu^+\nu_\mu$ |  |
| `<BR>(B+->D*munu)` | $\langle\text{BR}\rangle(B^+\to D^{*0}\mu^+\nu_\mu)$ | Binned branching ratio of $B^+\to D^{*0}\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<BR>(B0->D*munu)` | $\langle\text{BR}\rangle(B^0\to D^{*-}\mu^+\nu_\mu)$ | Binned branching ratio of $B^0\to D^{*-}\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<BR>(Bs->K*munu)` | $\langle\text{BR}\rangle(B_s\to K^{*-}\mu^+\nu_\mu)$ | Binned branching ratio of $B_s\to K^{*-}\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<BR>(B+->rhomunu)` | $\langle\text{BR}\rangle(B^+\to \rho^0\mu^+\nu_\mu)$ | Binned branching ratio of $B^+\to \rho^0\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<BR>(B0->rhomunu)` | $\langle\text{BR}\rangle(B^0\to \rho^-\mu^+\nu_\mu)$ | Binned branching ratio of $B^0\to \rho^-\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->D*taunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{*0}\tau^+\nu_\tau)$ | Differential branching ratio of $B^+\to D^{*0}\tau^+\nu_\tau$ | `q2` |
| `dBR/dq2(B0->D*taunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{*-}\tau^+\nu_\tau)$ | Differential branching ratio of $B^0\to D^{*-}\tau^+\nu_\tau$ | `q2` |
| `dBR/dq2(Bs->K*taunu)` | $\frac{d\text{BR}}{dq^2}(B_s\to K^{*-}\tau^+\nu_\tau)$ | Differential branching ratio of $B_s\to K^{*-}\tau^+\nu_\tau$ | `q2` |
| `dBR/dq2(B+->rhotaunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \rho^0\tau^+\nu_\tau)$ | Differential branching ratio of $B^+\to \rho^0\tau^+\nu_\tau$ | `q2` |
| `dBR/dq2(B0->rhotaunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \rho^-\tau^+\nu_\tau)$ | Differential branching ratio of $B^0\to \rho^-\tau^+\nu_\tau$ | `q2` |
| `BR(B+->D*taunu)` | $\text{BR}(B^+\to D^{*0}\tau^+\nu_\tau)$ | Total branching ratio of $B^+\to D^{*0}\tau^+\nu_\tau$ |  |
| `BR(B0->D*taunu)` | $\text{BR}(B^0\to D^{*-}\tau^+\nu_\tau)$ | Total branching ratio of $B^0\to D^{*-}\tau^+\nu_\tau$ |  |
| `BR(Bs->K*taunu)` | $\text{BR}(B_s\to K^{*-}\tau^+\nu_\tau)$ | Total branching ratio of $B_s\to K^{*-}\tau^+\nu_\tau$ |  |
| `BR(B+->rhotaunu)` | $\text{BR}(B^+\to \rho^0\tau^+\nu_\tau)$ | Total branching ratio of $B^+\to \rho^0\tau^+\nu_\tau$ |  |
| `BR(B0->rhotaunu)` | $\text{BR}(B^0\to \rho^-\tau^+\nu_\tau)$ | Total branching ratio of $B^0\to \rho^-\tau^+\nu_\tau$ |  |
| `<BR>(B+->D*taunu)` | $\langle\text{BR}\rangle(B^+\to D^{*0}\tau^+\nu_\tau)$ | Binned branching ratio of $B^+\to D^{*0}\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<BR>(B0->D*taunu)` | $\langle\text{BR}\rangle(B^0\to D^{*-}\tau^+\nu_\tau)$ | Binned branching ratio of $B^0\to D^{*-}\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<BR>(Bs->K*taunu)` | $\langle\text{BR}\rangle(B_s\to K^{*-}\tau^+\nu_\tau)$ | Binned branching ratio of $B_s\to K^{*-}\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<BR>(B+->rhotaunu)` | $\langle\text{BR}\rangle(B^+\to \rho^0\tau^+\nu_\tau)$ | Binned branching ratio of $B^+\to \rho^0\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<BR>(B0->rhotaunu)` | $\langle\text{BR}\rangle(B^0\to \rho^-\tau^+\nu_\tau)$ | Binned branching ratio of $B^0\to \rho^-\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `dBR/dq2(B+->D*lnu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{*0}\ell^+\nu_\ell)$ | Differential branching ratio of $B^+\to D^{*0}\ell^+\nu_\ell$ | `q2` |
| `dBR/dq2(B0->D*lnu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{*-}\ell^+\nu_\ell)$ | Differential branching ratio of $B^0\to D^{*-}\ell^+\nu_\ell$ | `q2` |
| `dBR/dq2(Bs->K*lnu)` | $\frac{d\text{BR}}{dq^2}(B_s\to K^{*-}\ell^+\nu_\ell)$ | Differential branching ratio of $B_s\to K^{*-}\ell^+\nu_\ell$ | `q2` |
| `dBR/dq2(B+->rholnu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \rho^0\ell^+\nu_\ell)$ | Differential branching ratio of $B^+\to \rho^0\ell^+\nu_\ell$ | `q2` |
| `dBR/dq2(B0->rholnu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \rho^-\ell^+\nu_\ell)$ | Differential branching ratio of $B^0\to \rho^-\ell^+\nu_\ell$ | `q2` |
| `BR(B+->D*lnu)` | $\text{BR}(B^+\to D^{*0}\ell^+\nu_\ell)$ | Total branching ratio of $B^+\to D^{*0}\ell^+\nu_\ell$ |  |
| `BR(B0->D*lnu)` | $\text{BR}(B^0\to D^{*-}\ell^+\nu_\ell)$ | Total branching ratio of $B^0\to D^{*-}\ell^+\nu_\ell$ |  |
| `BR(Bs->K*lnu)` | $\text{BR}(B_s\to K^{*-}\ell^+\nu_\ell)$ | Total branching ratio of $B_s\to K^{*-}\ell^+\nu_\ell$ |  |
| `BR(B+->rholnu)` | $\text{BR}(B^+\to \rho^0\ell^+\nu_\ell)$ | Total branching ratio of $B^+\to \rho^0\ell^+\nu_\ell$ |  |
| `BR(B0->rholnu)` | $\text{BR}(B^0\to \rho^-\ell^+\nu_\ell)$ | Total branching ratio of $B^0\to \rho^-\ell^+\nu_\ell$ |  |
| `<BR>(B+->D*lnu)` | $\langle\text{BR}\rangle(B^+\to D^{*0}\ell^+\nu_\ell)$ | Binned branching ratio of $B^+\to D^{*0}\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<BR>(B0->D*lnu)` | $\langle\text{BR}\rangle(B^0\to D^{*-}\ell^+\nu_\ell)$ | Binned branching ratio of $B^0\to D^{*-}\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<BR>(Bs->K*lnu)` | $\langle\text{BR}\rangle(B_s\to K^{*-}\ell^+\nu_\ell)$ | Binned branching ratio of $B_s\to K^{*-}\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<BR>(B+->rholnu)` | $\langle\text{BR}\rangle(B^+\to \rho^0\ell^+\nu_\ell)$ | Binned branching ratio of $B^+\to \rho^0\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<BR>(B0->rholnu)` | $\langle\text{BR}\rangle(B^0\to \rho^-\ell^+\nu_\ell)$ | Binned branching ratio of $B^0\to \rho^-\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `BR(Bs->ee)` | $\overline{\text{BR}}(B_s\to e^+e^-)$. | Time-integrated branching ratio of $B_s\to e^+e^-$. |  |
| `BR(Bd->ee)` | $\text{BR}(B^0\to e^+e^-)$. | Branching ratio of $B^0\to e^+e^-$. |  |
| `BR(Bs->mumu)` | $\overline{\text{BR}}(B_s\to \mu^+\mu^-)$. | Time-integrated branching ratio of $B_s\to \mu^+\mu^-$. |  |
| `BR(Bd->mumu)` | $\text{BR}(B^0\to \mu^+\mu^-)$. | Branching ratio of $B^0\to \mu^+\mu^-$. |  |
| `BR(Bs->tautau)` | $\overline{\text{BR}}(B_s\to \tau^+\tau^-)$. | Time-integrated branching ratio of $B_s\to \tau^+\tau^-$. |  |
| `BR(Bd->tautau)` | $\text{BR}(B^0\to \tau^+\tau^-)$. | Branching ratio of $B^0\to \tau^+\tau^-$. |  |
| `<AFB>(B+->Kee)` | $\langle A_\text{FB}\rangle(B^+\to K^+e^+e^-)$ | Binned forward-backward asymmetry in $B^+\to K^+e^+e^-$ | `q2min`, `q2max` |
| `AFB(B+->Kee)` | $A_\text{FB}(B^+\to K^+e^+e^-)$ | Forward-backward asymmetry in $B^+\to K^+e^+e^-$ | `q2` |
| `<FH>(B+->Kee)` | $\langle F_H\rangle(B^+\to K^+e^+e^-)$ | Binned flat term in $B^+\to K^+e^+e^-$ | `q2min`, `q2max` |
| `FH(B+->Kee)` | $F_H(B^+\to K^+e^+e^-)$ | Flat term in $B^+\to K^+e^+e^-$ | `q2` |
| `<dBR/dq2>(B+->Kee)` | $\langle \text{BR} \rangle(B^+\to K^+e^+e^-)$ | Binned differential branching ratio of $B^+\to K^+e^+e^-$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Kee)` | $\frac{d\text{BR}}{dq^2}(B^+\to K^+e^+e^-)$ | Differntial branching ratio of $B^+\to K^+e^+e^-$ | `q2` |
| `<AFB>(B0->Kee)` | $\langle A_\text{FB}\rangle(B^0\to K^0e^+e^-)$ | Binned forward-backward asymmetry in $B^0\to K^0e^+e^-$ | `q2min`, `q2max` |
| `AFB(B0->Kee)` | $A_\text{FB}(B^0\to K^0e^+e^-)$ | Forward-backward asymmetry in $B^0\to K^0e^+e^-$ | `q2` |
| `<FH>(B0->Kee)` | $\langle F_H\rangle(B^0\to K^0e^+e^-)$ | Binned flat term in $B^0\to K^0e^+e^-$ | `q2min`, `q2max` |
| `FH(B0->Kee)` | $F_H(B^0\to K^0e^+e^-)$ | Flat term in $B^0\to K^0e^+e^-$ | `q2` |
| `<dBR/dq2>(B0->Kee)` | $\langle \text{BR} \rangle(B^0\to K^0e^+e^-)$ | Binned differential branching ratio of $B^0\to K^0e^+e^-$ | `q2min`, `q2max` |
| `dBR/dq2(B0->Kee)` | $\frac{d\text{BR}}{dq^2}(B^0\to K^0e^+e^-)$ | Differntial branching ratio of $B^0\to K^0e^+e^-$ | `q2` |
| `<AFB>(B+->Kmumu)` | $\langle A_\text{FB}\rangle(B^+\to K^+\mu^+\mu^-)$ | Binned forward-backward asymmetry in $B^+\to K^+\mu^+\mu^-$ | `q2min`, `q2max` |
| `AFB(B+->Kmumu)` | $A_\text{FB}(B^+\to K^+\mu^+\mu^-)$ | Forward-backward asymmetry in $B^+\to K^+\mu^+\mu^-$ | `q2` |
| `<FH>(B+->Kmumu)` | $\langle F_H\rangle(B^+\to K^+\mu^+\mu^-)$ | Binned flat term in $B^+\to K^+\mu^+\mu^-$ | `q2min`, `q2max` |
| `FH(B+->Kmumu)` | $F_H(B^+\to K^+\mu^+\mu^-)$ | Flat term in $B^+\to K^+\mu^+\mu^-$ | `q2` |
| `<dBR/dq2>(B+->Kmumu)` | $\langle \text{BR} \rangle(B^+\to K^+\mu^+\mu^-)$ | Binned differential branching ratio of $B^+\to K^+\mu^+\mu^-$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Kmumu)` | $\frac{d\text{BR}}{dq^2}(B^+\to K^+\mu^+\mu^-)$ | Differntial branching ratio of $B^+\to K^+\mu^+\mu^-$ | `q2` |
| `<AFB>(B0->Kmumu)` | $\langle A_\text{FB}\rangle(B^0\to K^0\mu^+\mu^-)$ | Binned forward-backward asymmetry in $B^0\to K^0\mu^+\mu^-$ | `q2min`, `q2max` |
| `AFB(B0->Kmumu)` | $A_\text{FB}(B^0\to K^0\mu^+\mu^-)$ | Forward-backward asymmetry in $B^0\to K^0\mu^+\mu^-$ | `q2` |
| `<FH>(B0->Kmumu)` | $\langle F_H\rangle(B^0\to K^0\mu^+\mu^-)$ | Binned flat term in $B^0\to K^0\mu^+\mu^-$ | `q2min`, `q2max` |
| `FH(B0->Kmumu)` | $F_H(B^0\to K^0\mu^+\mu^-)$ | Flat term in $B^0\to K^0\mu^+\mu^-$ | `q2` |
| `<dBR/dq2>(B0->Kmumu)` | $\langle \text{BR} \rangle(B^0\to K^0\mu^+\mu^-)$ | Binned differential branching ratio of $B^0\to K^0\mu^+\mu^-$ | `q2min`, `q2max` |
| `dBR/dq2(B0->Kmumu)` | $\frac{d\text{BR}}{dq^2}(B^0\to K^0\mu^+\mu^-)$ | Differntial branching ratio of $B^0\to K^0\mu^+\mu^-$ | `q2` |
| `<AFB>(B+->Ktautau)` | $\langle A_\text{FB}\rangle(B^+\to K^+\tau^+\tau^-)$ | Binned forward-backward asymmetry in $B^+\to K^+\tau^+\tau^-$ | `q2min`, `q2max` |
| `AFB(B+->Ktautau)` | $A_\text{FB}(B^+\to K^+\tau^+\tau^-)$ | Forward-backward asymmetry in $B^+\to K^+\tau^+\tau^-$ | `q2` |
| `<FH>(B+->Ktautau)` | $\langle F_H\rangle(B^+\to K^+\tau^+\tau^-)$ | Binned flat term in $B^+\to K^+\tau^+\tau^-$ | `q2min`, `q2max` |
| `FH(B+->Ktautau)` | $F_H(B^+\to K^+\tau^+\tau^-)$ | Flat term in $B^+\to K^+\tau^+\tau^-$ | `q2` |
| `<dBR/dq2>(B+->Ktautau)` | $\langle \text{BR} \rangle(B^+\to K^+\tau^+\tau^-)$ | Binned differential branching ratio of $B^+\to K^+\tau^+\tau^-$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Ktautau)` | $\frac{d\text{BR}}{dq^2}(B^+\to K^+\tau^+\tau^-)$ | Differntial branching ratio of $B^+\to K^+\tau^+\tau^-$ | `q2` |
| `<AFB>(B0->Ktautau)` | $\langle A_\text{FB}\rangle(B^0\to K^0\tau^+\tau^-)$ | Binned forward-backward asymmetry in $B^0\to K^0\tau^+\tau^-$ | `q2min`, `q2max` |
| `AFB(B0->Ktautau)` | $A_\text{FB}(B^0\to K^0\tau^+\tau^-)$ | Forward-backward asymmetry in $B^0\to K^0\tau^+\tau^-$ | `q2` |
| `<FH>(B0->Ktautau)` | $\langle F_H\rangle(B^0\to K^0\tau^+\tau^-)$ | Binned flat term in $B^0\to K^0\tau^+\tau^-$ | `q2min`, `q2max` |
| `FH(B0->Ktautau)` | $F_H(B^0\to K^0\tau^+\tau^-)$ | Flat term in $B^0\to K^0\tau^+\tau^-$ | `q2` |
| `<dBR/dq2>(B0->Ktautau)` | $\langle \text{BR} \rangle(B^0\to K^0\tau^+\tau^-)$ | Binned differential branching ratio of $B^0\to K^0\tau^+\tau^-$ | `q2min`, `q2max` |
| `dBR/dq2(B0->Ktautau)` | $\frac{d\text{BR}}{dq^2}(B^0\to K^0\tau^+\tau^-)$ | Differntial branching ratio of $B^0\to K^0\tau^+\tau^-$ | `q2` |
| `<Rmue>(B+->Kll)` | $\langle R_{\mu e} \rangle(B^+\to K^+\ell^+\ell^-)$ | Ratio of partial branching ratios of $B^+\to K^+\mu^+ \mu^-$ and $B^+\to K^+e^+ e^-$ | `q2min`, `q2max` |
| `<Rmue>(B0->Kll)` | $\langle R_{\mu e} \rangle(B^0\to K^0\ell^+\ell^-)$ | Ratio of partial branching ratios of $B^0\to K^0\mu^+ \mu^-$ and $B^0\to K^0e^+ e^-$ | `q2min`, `q2max` |
| `<Rtaumu>(B+->Kll)` | $\langle R_{\tau \mu} \rangle(B^+\to K^+\ell^+\ell^-)$ | Ratio of partial branching ratios of $B^+\to K^+\tau^+ \tau^-$ and $B^+\to K^+\mu^+ \mu^-$ | `q2min`, `q2max` |
| `<Rtaumu>(B0->Kll)` | $\langle R_{\tau \mu} \rangle(B^0\to K^0\ell^+\ell^-)$ | Ratio of partial branching ratios of $B^0\to K^0\tau^+ \tau^-$ and $B^0\to K^0\mu^+ \mu^-$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Denu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{0}e^+\nu_e)$ | Differential branching ratio of $B^+\to D^{0}e^+\nu_e$ | `q2` |
| `dBR/dq2(B0->Denu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{-}e^+\nu_e)$ | Differential branching ratio of $B^0\to D^{-}e^+\nu_e$ | `q2` |
| `dBR/dq2(B+->pienu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \pi^0e^+\nu_e)$ | Differential branching ratio of $B^+\to \pi^0e^+\nu_e$ | `q2` |
| `dBR/dq2(B0->pienu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \pi^-e^+\nu_e)$ | Differential branching ratio of $B^0\to \pi^-e^+\nu_e$ | `q2` |
| `BR(B+->Denu)` | $\text{BR}(B^+\to D^{0}e^+\nu_e)$ | Total branching ratio of $B^+\to D^{0}e^+\nu_e$ |  |
| `BR(B0->Denu)` | $\text{BR}(B^0\to D^{-}e^+\nu_e)$ | Total branching ratio of $B^0\to D^{-}e^+\nu_e$ |  |
| `BR(B+->pienu)` | $\text{BR}(B^+\to \pi^0e^+\nu_e)$ | Total branching ratio of $B^+\to \pi^0e^+\nu_e$ |  |
| `BR(B0->pienu)` | $\text{BR}(B^0\to \pi^-e^+\nu_e)$ | Total branching ratio of $B^0\to \pi^-e^+\nu_e$ |  |
| `<BR>(B+->Denu)` | $\langle\text{BR}\rangle(B^+\to D^{0}e^+\nu_e)$ | Binned branching ratio of $B^+\to D^{0}e^+\nu_e$ | `q2min`, `q2max` |
| `<BR>(B0->Denu)` | $\langle\text{BR}\rangle(B^0\to D^{-}e^+\nu_e)$ | Binned branching ratio of $B^0\to D^{-}e^+\nu_e$ | `q2min`, `q2max` |
| `<BR>(B+->pienu)` | $\langle\text{BR}\rangle(B^+\to \pi^0e^+\nu_e)$ | Binned branching ratio of $B^+\to \pi^0e^+\nu_e$ | `q2min`, `q2max` |
| `<BR>(B0->pienu)` | $\langle\text{BR}\rangle(B^0\to \pi^-e^+\nu_e)$ | Binned branching ratio of $B^0\to \pi^-e^+\nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Dmunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{0}\mu^+\nu_\mu)$ | Differential branching ratio of $B^+\to D^{0}\mu^+\nu_\mu$ | `q2` |
| `dBR/dq2(B0->Dmunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{-}\mu^+\nu_\mu)$ | Differential branching ratio of $B^0\to D^{-}\mu^+\nu_\mu$ | `q2` |
| `dBR/dq2(B+->pimunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \pi^0\mu^+\nu_\mu)$ | Differential branching ratio of $B^+\to \pi^0\mu^+\nu_\mu$ | `q2` |
| `dBR/dq2(B0->pimunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \pi^-\mu^+\nu_\mu)$ | Differential branching ratio of $B^0\to \pi^-\mu^+\nu_\mu$ | `q2` |
| `BR(B+->Dmunu)` | $\text{BR}(B^+\to D^{0}\mu^+\nu_\mu)$ | Total branching ratio of $B^+\to D^{0}\mu^+\nu_\mu$ |  |
| `BR(B0->Dmunu)` | $\text{BR}(B^0\to D^{-}\mu^+\nu_\mu)$ | Total branching ratio of $B^0\to D^{-}\mu^+\nu_\mu$ |  |
| `BR(B+->pimunu)` | $\text{BR}(B^+\to \pi^0\mu^+\nu_\mu)$ | Total branching ratio of $B^+\to \pi^0\mu^+\nu_\mu$ |  |
| `BR(B0->pimunu)` | $\text{BR}(B^0\to \pi^-\mu^+\nu_\mu)$ | Total branching ratio of $B^0\to \pi^-\mu^+\nu_\mu$ |  |
| `<BR>(B+->Dmunu)` | $\langle\text{BR}\rangle(B^+\to D^{0}\mu^+\nu_\mu)$ | Binned branching ratio of $B^+\to D^{0}\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<BR>(B0->Dmunu)` | $\langle\text{BR}\rangle(B^0\to D^{-}\mu^+\nu_\mu)$ | Binned branching ratio of $B^0\to D^{-}\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<BR>(B+->pimunu)` | $\langle\text{BR}\rangle(B^+\to \pi^0\mu^+\nu_\mu)$ | Binned branching ratio of $B^+\to \pi^0\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<BR>(B0->pimunu)` | $\langle\text{BR}\rangle(B^0\to \pi^-\mu^+\nu_\mu)$ | Binned branching ratio of $B^0\to \pi^-\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Dtaunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{0}\tau^+\nu_\tau)$ | Differential branching ratio of $B^+\to D^{0}\tau^+\nu_\tau$ | `q2` |
| `dBR/dq2(B0->Dtaunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{-}\tau^+\nu_\tau)$ | Differential branching ratio of $B^0\to D^{-}\tau^+\nu_\tau$ | `q2` |
| `dBR/dq2(B+->pitaunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \pi^0\tau^+\nu_\tau)$ | Differential branching ratio of $B^+\to \pi^0\tau^+\nu_\tau$ | `q2` |
| `dBR/dq2(B0->pitaunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \pi^-\tau^+\nu_\tau)$ | Differential branching ratio of $B^0\to \pi^-\tau^+\nu_\tau$ | `q2` |
| `BR(B+->Dtaunu)` | $\text{BR}(B^+\to D^{0}\tau^+\nu_\tau)$ | Total branching ratio of $B^+\to D^{0}\tau^+\nu_\tau$ |  |
| `BR(B0->Dtaunu)` | $\text{BR}(B^0\to D^{-}\tau^+\nu_\tau)$ | Total branching ratio of $B^0\to D^{-}\tau^+\nu_\tau$ |  |
| `BR(B+->pitaunu)` | $\text{BR}(B^+\to \pi^0\tau^+\nu_\tau)$ | Total branching ratio of $B^+\to \pi^0\tau^+\nu_\tau$ |  |
| `BR(B0->pitaunu)` | $\text{BR}(B^0\to \pi^-\tau^+\nu_\tau)$ | Total branching ratio of $B^0\to \pi^-\tau^+\nu_\tau$ |  |
| `<BR>(B+->Dtaunu)` | $\langle\text{BR}\rangle(B^+\to D^{0}\tau^+\nu_\tau)$ | Binned branching ratio of $B^+\to D^{0}\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<BR>(B0->Dtaunu)` | $\langle\text{BR}\rangle(B^0\to D^{-}\tau^+\nu_\tau)$ | Binned branching ratio of $B^0\to D^{-}\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<BR>(B+->pitaunu)` | $\langle\text{BR}\rangle(B^+\to \pi^0\tau^+\nu_\tau)$ | Binned branching ratio of $B^+\to \pi^0\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<BR>(B0->pitaunu)` | $\langle\text{BR}\rangle(B^0\to \pi^-\tau^+\nu_\tau)$ | Binned branching ratio of $B^0\to \pi^-\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Dlnu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{0}\ell^+\nu_\ell)$ | Differential branching ratio of $B^+\to D^{0}\ell^+\nu_\ell$ | `q2` |
| `dBR/dq2(B0->Dlnu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{-}\ell^+\nu_\ell)$ | Differential branching ratio of $B^0\to D^{-}\ell^+\nu_\ell$ | `q2` |
| `dBR/dq2(B+->pilnu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \pi^0\ell^+\nu_\ell)$ | Differential branching ratio of $B^+\to \pi^0\ell^+\nu_\ell$ | `q2` |
| `dBR/dq2(B0->pilnu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \pi^-\ell^+\nu_\ell)$ | Differential branching ratio of $B^0\to \pi^-\ell^+\nu_\ell$ | `q2` |
| `BR(B+->Dlnu)` | $\text{BR}(B^+\to D^{0}\ell^+\nu_\ell)$ | Total branching ratio of $B^+\to D^{0}\ell^+\nu_\ell$ |  |
| `BR(B0->Dlnu)` | $\text{BR}(B^0\to D^{-}\ell^+\nu_\ell)$ | Total branching ratio of $B^0\to D^{-}\ell^+\nu_\ell$ |  |
| `BR(B+->pilnu)` | $\text{BR}(B^+\to \pi^0\ell^+\nu_\ell)$ | Total branching ratio of $B^+\to \pi^0\ell^+\nu_\ell$ |  |
| `BR(B0->pilnu)` | $\text{BR}(B^0\to \pi^-\ell^+\nu_\ell)$ | Total branching ratio of $B^0\to \pi^-\ell^+\nu_\ell$ |  |
| `<BR>(B+->Dlnu)` | $\langle\text{BR}\rangle(B^+\to D^{0}\ell^+\nu_\ell)$ | Binned branching ratio of $B^+\to D^{0}\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<BR>(B0->Dlnu)` | $\langle\text{BR}\rangle(B^0\to D^{-}\ell^+\nu_\ell)$ | Binned branching ratio of $B^0\to D^{-}\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<BR>(B+->pilnu)` | $\langle\text{BR}\rangle(B^+\to \pi^0\ell^+\nu_\ell)$ | Binned branching ratio of $B^+\to \pi^0\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<BR>(B0->pilnu)` | $\langle\text{BR}\rangle(B^0\to \pi^-\ell^+\nu_\ell)$ | Binned branching ratio of $B^0\to \pi^-\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<dBR/dq2>(B+->K*nunu)` | $\langle \text{BR} \rangle(B^+\to K^{*+}\nu\bar\nu)$ | Binned differential branching ratio of $B^+\to K^{*+}\nu\bar\nu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->K*nunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to K^{*+}\nu\bar\nu)$ | Differential branching ratio of $B^+\to K^{*+}\nu\bar\nu$ | `q2` |
| `BR(B+->K*nunu)` | $\text{BR}(B^+\to K^{*+}\nu\bar\nu)$ | Branching ratio of $B^+\to K^{*+}\nu\bar\nu$ |  |
| `<dBR/dq2>(B0->K*nunu)` | $\langle \text{BR} \rangle(B^0\to K^{*0}\nu\bar\nu)$ | Binned differential branching ratio of $B^0\to K^{*0}\nu\bar\nu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->K*nunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to K^{*0}\nu\bar\nu)$ | Differential branching ratio of $B^0\to K^{*0}\nu\bar\nu$ | `q2` |
| `BR(B0->K*nunu)` | $\text{BR}(B^0\to K^{*0}\nu\bar\nu)$ | Branching ratio of $B^0\to K^{*0}\nu\bar\nu$ |  |
| `<dBR/dq2>(B0->rhonunu)` | $\langle \text{BR} \rangle(B^0\to \rho^{0}\nu\bar\nu)$ | Binned differential branching ratio of $B^0\to \rho^{0}\nu\bar\nu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->rhonunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \rho^{0}\nu\bar\nu)$ | Differential branching ratio of $B^0\to \rho^{0}\nu\bar\nu$ | `q2` |
| `BR(B0->rhonunu)` | $\text{BR}(B^0\to \rho^{0}\nu\bar\nu)$ | Branching ratio of $B^0\to \rho^{0}\nu\bar\nu$ |  |
| `<dBR/dq2>(B+->rhonunu)` | $\langle \text{BR} \rangle(B^+\to \rho^{+}\nu\bar\nu)$ | Binned differential branching ratio of $B^+\to \rho^{+}\nu\bar\nu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->rhonunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \rho^{+}\nu\bar\nu)$ | Differential branching ratio of $B^+\to \rho^{+}\nu\bar\nu$ | `q2` |
| `BR(B+->rhonunu)` | $\text{BR}(B^+\to \rho^{+}\nu\bar\nu)$ | Branching ratio of $B^+\to \rho^{+}\nu\bar\nu$ |  |
| `<dBR/dq2>(B+->pinunu)` | $\langle \text{BR} \rangle(B^+\to \pi^+\nu\bar\nu)$ | Binned differential branching ratio of $B^+\to \pi^+\nu\bar\nu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->pinunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \pi^+\nu\bar\nu)$ | Differential branching ratio of $B^+\to \pi^+\nu\bar\nu$ | `q2` |
| `BR(B+->pinunu)` | $\text{BR}(B^+\to \pi^+\nu\bar\nu)$ | Branching ratio of $B^+\to \pi^+\nu\bar\nu$ |  |
| `<dBR/dq2>(B+->Knunu)` | $\langle \text{BR} \rangle(B^+\to K^+\nu\bar\nu)$ | Binned differential branching ratio of $B^+\to K^+\nu\bar\nu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Knunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to K^+\nu\bar\nu)$ | Differential branching ratio of $B^+\to K^+\nu\bar\nu$ | `q2` |
| `BR(B+->Knunu)` | $\text{BR}(B^+\to K^+\nu\bar\nu)$ | Branching ratio of $B^+\to K^+\nu\bar\nu$ |  |
| `<dBR/dq2>(B0->Knunu)` | $\langle \text{BR} \rangle(B^0\to K^0\nu\bar\nu)$ | Binned differential branching ratio of $B^0\to K^0\nu\bar\nu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->Knunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to K^0\nu\bar\nu)$ | Differential branching ratio of $B^0\to K^0\nu\bar\nu$ | `q2` |
| `BR(B0->Knunu)` | $\text{BR}(B^0\to K^0\nu\bar\nu)$ | Branching ratio of $B^0\to K^0\nu\bar\nu$ |  |
| `<dBR/dq2>(B0->pinunu)` | $\langle \text{BR} \rangle(B^0\to \pi^0\nu\bar\nu)$ | Binned differential branching ratio of $B^0\to \pi^0\nu\bar\nu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->pinunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \pi^0\nu\bar\nu)$ | Differential branching ratio of $B^0\to \pi^0\nu\bar\nu$ | `q2` |
| `BR(B0->pinunu)` | $\text{BR}(B^0\to \pi^0\nu\bar\nu)$ | Branching ratio of $B^0\to \pi^0\nu\bar\nu$ |  |
| `DeltaM_s` | $\Delta M_s$ | Mass difference in the $B_s$-$\bar B_s$ system |  |
| `DeltaM_d` | $\Delta M_d$ | Mass difference in the $B^0$-$\bar B^0$ system |  |
| `a_fs_s` | $a_\text{fs}^s$ | CP asymmetry in flavour-specific $B_s$ decays |  |
| `a_fs_d` | $a_\text{fs}^d$ | CP asymmetry in flavour-specific $B^0$ decays |  |
| `DeltaGamma_s` | $\Delta\Gamma_s$ | Decay width difference in the $B_s$-$\bar B_s$ system |  |
| `DeltaGamma_d` | $\Delta\Gamma_d$ | Decay width difference in the $B^0$-$\bar B^0$ system |  |
| `eps_K` | $\vert\epsilon_K\vert$ | Direct CP violation parameter in the $K^0$-$\bar K^0$ system |  |
| `S_psiK` | $S_{\psi K_S}$ | Mixing induced CP asymmetry in $B^0\to J/\psi K_S$ |  |
| `S_psiphi` | $S_{\psi\phi}$ | Mixing induced CP asymmetry in $B_s\to J/\psi \phi$ |  |
| `ACP(B+->K*gamma)` | $A_{CP}(B^+\to K^{*+}\gamma)$ | Direct CP asymmetry of $B^+\to K^{*+}\gamma$ |  |
| `ACP(B0->K*gamma)` | $A_{CP}(B^0\to K^{*0}\gamma)$ | Direct CP asymmetry of $B^0\to K^{*0}\gamma$ |  |
| `BR(B+->K*gamma)` | $\text{BR}(B^+\to K^{*+}\gamma)$ | Branching ratio of $B^+\to K^{*+}\gamma$ |  |
| `BR(B0->K*gamma)` | $\text{BR}(B^0\to K^{*0}\gamma)$ | Branching ratio of $B^0\to K^{*0}\gamma$ |  |
| `S_K*gamma` | $S_{K^{*}\gamma}$ | Mixing-induced CP asymmetry in $B^0\to K^{*0}\gamma$ |  |
