---
layout: default
title: Observables - $b$ hadron decays - Semi-leptonic tree-level decays
---

# Observables / $b$ hadron decays / Semi-leptonic tree-level decays



The tables below have been generated automatically from the observables currently
implemented in flavio. The first column is the string name that must  be used
when calling functions such as `flavio.sm_prediction`. The last column lists
the arguments the observable depends on (which can also be empty in case of
a scalar observable).



{::options toc_levels="2" /}

* TOC
{:toc}

## $B\to P\ell\nu$

### $B^+\to D^0\ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->Dlnu)` | $\langle\text{BR}\rangle(B^+\to D^0\ell^+\nu_\ell)$ | Binned branching ratio of $B^+\to D^0\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<Rtaul>(B->Dlnu)` | $\langle R_{\tau \ell} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `BR(B+->Dlnu)` | $\text{BR}(B^+\to D^0\ell^+\nu_\ell)$ | Total branching ratio of $B^+\to D^0\ell^+\nu_\ell$ |  |
| `Rtaul(B->Dlnu)` | $R_{\tau \ell}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Dlnu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^0\ell^+\nu_\ell)$ | Differential branching ratio of $B^+\to D^0\ell^+\nu_\ell$ | `q2` |


### $B^+\to D^0\mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->Dmunu)` | $\langle\text{BR}\rangle(B^+\to D^0\mu^+\nu_\mu)$ | Binned branching ratio of $B^+\to D^0\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<Rmue>(B->Dlnu)` | $\langle R_{\mu e} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\mu^+ \nu_\mu$ and $B\to De^+ \nu_e$ | `q2min`, `q2max` |
| `<Rtaumu>(B->Dlnu)` | $\langle R_{\tau \mu} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B+->Dmunu)` | $\text{BR}(B^+\to D^0\mu^+\nu_\mu)$ | Total branching ratio of $B^+\to D^0\mu^+\nu_\mu$ |  |
| `Rmue(B->Dlnu)` | $R_{\mu e}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\mu^+ \nu_\mu$ and $B\to De^+ \nu_e$ | `q2min`, `q2max` |
| `Rtaumu(B->Dlnu)` | $R_{\tau \mu}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Dmunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^0\mu^+\nu_\mu)$ | Differential branching ratio of $B^+\to D^0\mu^+\nu_\mu$ | `q2` |


### $B^+\to D^0\tau^+\nu_\tau$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->Dtaunu)` | $\langle\text{BR}\rangle(B^+\to D^0\tau^+\nu_\tau)$ | Binned branching ratio of $B^+\to D^0\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<Rtaul>(B->Dlnu)` | $\langle R_{\tau \ell} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `<Rtaumu>(B->Dlnu)` | $\langle R_{\tau \mu} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B+->Dtaunu)` | $\text{BR}(B^+\to D^0\tau^+\nu_\tau)$ | Total branching ratio of $B^+\to D^0\tau^+\nu_\tau$ |  |
| `Rtaul(B->Dlnu)` | $R_{\tau \ell}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `Rtaumu(B->Dlnu)` | $R_{\tau \mu}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Dtaunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^0\tau^+\nu_\tau)$ | Differential branching ratio of $B^+\to D^0\tau^+\nu_\tau$ | `q2` |


### $B^+\to D^0e^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->Denu)` | $\langle\text{BR}\rangle(B^+\to D^0e^+\nu_e)$ | Binned branching ratio of $B^+\to D^0e^+\nu_e$ | `q2min`, `q2max` |
| `<Rmue>(B->Dlnu)` | $\langle R_{\mu e} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\mu^+ \nu_\mu$ and $B\to De^+ \nu_e$ | `q2min`, `q2max` |
| `BR(B+->Denu)` | $\text{BR}(B^+\to D^0e^+\nu_e)$ | Total branching ratio of $B^+\to D^0e^+\nu_e$ |  |
| `Rmue(B->Dlnu)` | $R_{\mu e}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\mu^+ \nu_\mu$ and $B\to De^+ \nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B+->Denu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^0e^+\nu_e)$ | Differential branching ratio of $B^+\to D^0e^+\nu_e$ | `q2` |


### $B^+\to \pi^0\ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->pilnu)` | $\langle\text{BR}\rangle(B^+\to \pi^0\ell^+\nu_\ell)$ | Binned branching ratio of $B^+\to \pi^0\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<Rtaul>(B->pilnu)` | $\langle R_{\tau \ell} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `BR(B+->pilnu)` | $\text{BR}(B^+\to \pi^0\ell^+\nu_\ell)$ | Total branching ratio of $B^+\to \pi^0\ell^+\nu_\ell$ |  |
| `Rtaul(B->pilnu)` | $R_{\tau \ell}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `dBR/dq2(B+->pilnu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \pi^0\ell^+\nu_\ell)$ | Differential branching ratio of $B^+\to \pi^0\ell^+\nu_\ell$ | `q2` |


### $B^+\to \pi^0\mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->pimunu)` | $\langle\text{BR}\rangle(B^+\to \pi^0\mu^+\nu_\mu)$ | Binned branching ratio of $B^+\to \pi^0\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<Rmue>(B->pilnu)` | $\langle R_{\mu e} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \mu^+ \nu_\mu$ and $B\to \pi e^+ \nu_e$ | `q2min`, `q2max` |
| `<Rtaumu>(B->pilnu)` | $\langle R_{\tau \mu} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B+->pimunu)` | $\text{BR}(B^+\to \pi^0\mu^+\nu_\mu)$ | Total branching ratio of $B^+\to \pi^0\mu^+\nu_\mu$ |  |
| `Rmue(B->pilnu)` | $R_{\mu e}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \mu^+ \nu_\mu$ and $B\to \pi e^+ \nu_e$ | `q2min`, `q2max` |
| `Rtaumu(B->pilnu)` | $R_{\tau \mu}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->pimunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \pi^0\mu^+\nu_\mu)$ | Differential branching ratio of $B^+\to \pi^0\mu^+\nu_\mu$ | `q2` |


### $B^+\to \pi^0\tau^+\nu_\tau$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->pitaunu)` | $\langle\text{BR}\rangle(B^+\to \pi^0\tau^+\nu_\tau)$ | Binned branching ratio of $B^+\to \pi^0\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<Rtaul>(B->pilnu)` | $\langle R_{\tau \ell} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `<Rtaumu>(B->pilnu)` | $\langle R_{\tau \mu} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B+->pitaunu)` | $\text{BR}(B^+\to \pi^0\tau^+\nu_\tau)$ | Total branching ratio of $B^+\to \pi^0\tau^+\nu_\tau$ |  |
| `Rtaul(B->pilnu)` | $R_{\tau \ell}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `Rtaumu(B->pilnu)` | $R_{\tau \mu}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->pitaunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \pi^0\tau^+\nu_\tau)$ | Differential branching ratio of $B^+\to \pi^0\tau^+\nu_\tau$ | `q2` |


### $B^+\to \pi^0e^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->pienu)` | $\langle\text{BR}\rangle(B^+\to \pi^0e^+\nu_e)$ | Binned branching ratio of $B^+\to \pi^0e^+\nu_e$ | `q2min`, `q2max` |
| `<Rmue>(B->pilnu)` | $\langle R_{\mu e} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \mu^+ \nu_\mu$ and $B\to \pi e^+ \nu_e$ | `q2min`, `q2max` |
| `BR(B+->pienu)` | $\text{BR}(B^+\to \pi^0e^+\nu_e)$ | Total branching ratio of $B^+\to \pi^0e^+\nu_e$ |  |
| `Rmue(B->pilnu)` | $R_{\mu e}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \mu^+ \nu_\mu$ and $B\to \pi e^+ \nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B+->pienu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \pi^0e^+\nu_e)$ | Differential branching ratio of $B^+\to \pi^0e^+\nu_e$ | `q2` |


### $B^0\to D^- \ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->Dlnu)` | $\langle\text{BR}\rangle(B^0\to D^- \ell^+\nu_\ell)$ | Binned branching ratio of $B^0\to D^- \ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<Rtaul>(B->Dlnu)` | $\langle R_{\tau \ell} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `BR(B0->Dlnu)` | $\text{BR}(B^0\to D^- \ell^+\nu_\ell)$ | Total branching ratio of $B^0\to D^- \ell^+\nu_\ell$ |  |
| `Rtaul(B->Dlnu)` | $R_{\tau \ell}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `dBR/dq2(B0->Dlnu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^- \ell^+\nu_\ell)$ | Differential branching ratio of $B^0\to D^- \ell^+\nu_\ell$ | `q2` |


### $B^0\to D^- \mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->Dmunu)` | $\langle\text{BR}\rangle(B^0\to D^- \mu^+\nu_\mu)$ | Binned branching ratio of $B^0\to D^- \mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<Rmue>(B->Dlnu)` | $\langle R_{\mu e} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\mu^+ \nu_\mu$ and $B\to De^+ \nu_e$ | `q2min`, `q2max` |
| `<Rtaumu>(B->Dlnu)` | $\langle R_{\tau \mu} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B0->Dmunu)` | $\text{BR}(B^0\to D^- \mu^+\nu_\mu)$ | Total branching ratio of $B^0\to D^- \mu^+\nu_\mu$ |  |
| `Rmue(B->Dlnu)` | $R_{\mu e}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\mu^+ \nu_\mu$ and $B\to De^+ \nu_e$ | `q2min`, `q2max` |
| `Rtaumu(B->Dlnu)` | $R_{\tau \mu}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->Dmunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^- \mu^+\nu_\mu)$ | Differential branching ratio of $B^0\to D^- \mu^+\nu_\mu$ | `q2` |


### $B^0\to D^- \tau^+\nu_\tau$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->Dtaunu)` | $\langle\text{BR}\rangle(B^0\to D^- \tau^+\nu_\tau)$ | Binned branching ratio of $B^0\to D^- \tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<Rtaul>(B->Dlnu)` | $\langle R_{\tau \ell} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `<Rtaumu>(B->Dlnu)` | $\langle R_{\tau \mu} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B0->Dtaunu)` | $\text{BR}(B^0\to D^- \tau^+\nu_\tau)$ | Total branching ratio of $B^0\to D^- \tau^+\nu_\tau$ |  |
| `Rtaul(B->Dlnu)` | $R_{\tau \ell}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `Rtaumu(B->Dlnu)` | $R_{\tau \mu}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\tau^+ \nu_\tau$ and $B\to D\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->Dtaunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^- \tau^+\nu_\tau)$ | Differential branching ratio of $B^0\to D^- \tau^+\nu_\tau$ | `q2` |


### $B^0\to D^- e^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->Denu)` | $\langle\text{BR}\rangle(B^0\to D^- e^+\nu_e)$ | Binned branching ratio of $B^0\to D^- e^+\nu_e$ | `q2min`, `q2max` |
| `<Rmue>(B->Dlnu)` | $\langle R_{\mu e} \rangle(B\to D\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D\mu^+ \nu_\mu$ and $B\to De^+ \nu_e$ | `q2min`, `q2max` |
| `BR(B0->Denu)` | $\text{BR}(B^0\to D^- e^+\nu_e)$ | Total branching ratio of $B^0\to D^- e^+\nu_e$ |  |
| `Rmue(B->Dlnu)` | $R_{\mu e}(B\to D\ell^+\nu)$ | Ratio of total branching ratios of $B\to D\mu^+ \nu_\mu$ and $B\to De^+ \nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B0->Denu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^- e^+\nu_e)$ | Differential branching ratio of $B^0\to D^- e^+\nu_e$ | `q2` |


### $B^0\to \pi^- \ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->pilnu)` | $\langle\text{BR}\rangle(B^0\to \pi^- \ell^+\nu_\ell)$ | Binned branching ratio of $B^0\to \pi^- \ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<Rtaul>(B->pilnu)` | $\langle R_{\tau \ell} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `BR(B0->pilnu)` | $\text{BR}(B^0\to \pi^- \ell^+\nu_\ell)$ | Total branching ratio of $B^0\to \pi^- \ell^+\nu_\ell$ |  |
| `Rtaul(B->pilnu)` | $R_{\tau \ell}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `dBR/dq2(B0->pilnu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \pi^- \ell^+\nu_\ell)$ | Differential branching ratio of $B^0\to \pi^- \ell^+\nu_\ell$ | `q2` |


### $B^0\to \pi^- \mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->pimunu)` | $\langle\text{BR}\rangle(B^0\to \pi^- \mu^+\nu_\mu)$ | Binned branching ratio of $B^0\to \pi^- \mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<Rmue>(B->pilnu)` | $\langle R_{\mu e} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \mu^+ \nu_\mu$ and $B\to \pi e^+ \nu_e$ | `q2min`, `q2max` |
| `<Rtaumu>(B->pilnu)` | $\langle R_{\tau \mu} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B0->pimunu)` | $\text{BR}(B^0\to \pi^- \mu^+\nu_\mu)$ | Total branching ratio of $B^0\to \pi^- \mu^+\nu_\mu$ |  |
| `Rmue(B->pilnu)` | $R_{\mu e}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \mu^+ \nu_\mu$ and $B\to \pi e^+ \nu_e$ | `q2min`, `q2max` |
| `Rtaumu(B->pilnu)` | $R_{\tau \mu}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->pimunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \pi^- \mu^+\nu_\mu)$ | Differential branching ratio of $B^0\to \pi^- \mu^+\nu_\mu$ | `q2` |


### $B^0\to \pi^- \tau^+\nu_\tau$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->pitaunu)` | $\langle\text{BR}\rangle(B^0\to \pi^- \tau^+\nu_\tau)$ | Binned branching ratio of $B^0\to \pi^- \tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<Rtaul>(B->pilnu)` | $\langle R_{\tau \ell} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `<Rtaumu>(B->pilnu)` | $\langle R_{\tau \mu} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B0->pitaunu)` | $\text{BR}(B^0\to \pi^- \tau^+\nu_\tau)$ | Total branching ratio of $B^0\to \pi^- \tau^+\nu_\tau$ |  |
| `Rtaul(B->pilnu)` | $R_{\tau \ell}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `Rtaumu(B->pilnu)` | $R_{\tau \mu}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \tau^+ \nu_\tau$ and $B\to \pi \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->pitaunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \pi^- \tau^+\nu_\tau)$ | Differential branching ratio of $B^0\to \pi^- \tau^+\nu_\tau$ | `q2` |


### $B^0\to \pi^- e^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->pienu)` | $\langle\text{BR}\rangle(B^0\to \pi^- e^+\nu_e)$ | Binned branching ratio of $B^0\to \pi^- e^+\nu_e$ | `q2min`, `q2max` |
| `<Rmue>(B->pilnu)` | $\langle R_{\mu e} \rangle(B\to \pi \ell^+\nu)$ | Ratio of partial branching ratios of $B\to \pi \mu^+ \nu_\mu$ and $B\to \pi e^+ \nu_e$ | `q2min`, `q2max` |
| `BR(B0->pienu)` | $\text{BR}(B^0\to \pi^- e^+\nu_e)$ | Total branching ratio of $B^0\to \pi^- e^+\nu_e$ |  |
| `Rmue(B->pilnu)` | $R_{\mu e}(B\to \pi \ell^+\nu)$ | Ratio of total branching ratios of $B\to \pi \mu^+ \nu_\mu$ and $B\to \pi e^+ \nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B0->pienu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \pi^- e^+\nu_e)$ | Differential branching ratio of $B^0\to \pi^- e^+\nu_e$ | `q2` |


## $B\to V\ell\nu$

### $B^+\to D^{\ast 0}\ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->D*lnu)` | $\langle\text{BR}\rangle(B^+\to D^{\ast 0}\ell^+\nu_\ell)$ | Binned branching ratio of $B^+\to D^{\ast 0}\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<Rtaul>(B->D*lnu)` | $\langle R_{\tau \ell} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `BR(B+->D*lnu)` | $\text{BR}(B^+\to D^{\ast 0}\ell^+\nu_\ell)$ | Total branching ratio of $B^+\to D^{\ast 0}\ell^+\nu_\ell$ |  |
| `Rtaul(B->D*lnu)` | $R_{\tau \ell}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `dBR/dq2(B+->D*lnu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{\ast 0}\ell^+\nu_\ell)$ | Differential branching ratio of $B^+\to D^{\ast 0}\ell^+\nu_\ell$ | `q2` |


### $B^+\to D^{\ast 0}\mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->D*munu)` | $\langle\text{BR}\rangle(B^+\to D^{\ast 0}\mu^+\nu_\mu)$ | Binned branching ratio of $B^+\to D^{\ast 0}\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<Rmue>(B->D*lnu)` | $\langle R_{\mu e} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\mu^+ \nu_\mu$ and $B\to D^{\ast}e^+ \nu_e$ | `q2min`, `q2max` |
| `<Rtaumu>(B->D*lnu)` | $\langle R_{\tau \mu} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B+->D*munu)` | $\text{BR}(B^+\to D^{\ast 0}\mu^+\nu_\mu)$ | Total branching ratio of $B^+\to D^{\ast 0}\mu^+\nu_\mu$ |  |
| `Rmue(B->D*lnu)` | $R_{\mu e}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\mu^+ \nu_\mu$ and $B\to D^{\ast}e^+ \nu_e$ | `q2min`, `q2max` |
| `Rtaumu(B->D*lnu)` | $R_{\tau \mu}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->D*munu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{\ast 0}\mu^+\nu_\mu)$ | Differential branching ratio of $B^+\to D^{\ast 0}\mu^+\nu_\mu$ | `q2` |


### $B^+\to D^{\ast 0}\tau^+\nu_\tau$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->D*taunu)` | $\langle\text{BR}\rangle(B^+\to D^{\ast 0}\tau^+\nu_\tau)$ | Binned branching ratio of $B^+\to D^{\ast 0}\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<Rtaul>(B->D*lnu)` | $\langle R_{\tau \ell} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `<Rtaumu>(B->D*lnu)` | $\langle R_{\tau \mu} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B+->D*taunu)` | $\text{BR}(B^+\to D^{\ast 0}\tau^+\nu_\tau)$ | Total branching ratio of $B^+\to D^{\ast 0}\tau^+\nu_\tau$ |  |
| `Rtaul(B->D*lnu)` | $R_{\tau \ell}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `Rtaumu(B->D*lnu)` | $R_{\tau \mu}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->D*taunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{\ast 0}\tau^+\nu_\tau)$ | Differential branching ratio of $B^+\to D^{\ast 0}\tau^+\nu_\tau$ | `q2` |


### $B^+\to D^{\ast 0}e^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->D*enu)` | $\langle\text{BR}\rangle(B^+\to D^{\ast 0}e^+\nu_e)$ | Binned branching ratio of $B^+\to D^{\ast 0}e^+\nu_e$ | `q2min`, `q2max` |
| `<Rmue>(B->D*lnu)` | $\langle R_{\mu e} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\mu^+ \nu_\mu$ and $B\to D^{\ast}e^+ \nu_e$ | `q2min`, `q2max` |
| `BR(B+->D*enu)` | $\text{BR}(B^+\to D^{\ast 0}e^+\nu_e)$ | Total branching ratio of $B^+\to D^{\ast 0}e^+\nu_e$ |  |
| `Rmue(B->D*lnu)` | $R_{\mu e}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\mu^+ \nu_\mu$ and $B\to D^{\ast}e^+ \nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B+->D*enu)` | $\frac{d\text{BR}}{dq^2}(B^+\to D^{\ast 0}e^+\nu_e)$ | Differential branching ratio of $B^+\to D^{\ast 0}e^+\nu_e$ | `q2` |


### $B^+\to \omega \ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->omegalnu)` | $\langle\text{BR}\rangle(B^+\to \omega \ell^+\nu_\ell)$ | Binned branching ratio of $B^+\to \omega \ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<Rtaul>(B+->omegalnu)` | $\langle R_{\tau \ell} \rangle(B^+\to \omega \ell^+\nu)$ | Ratio of partial branching ratios of $B^+\to \omega \tau^+ \nu_\tau$ and $B^+\to \omega \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `BR(B+->omegalnu)` | $\text{BR}(B^+\to \omega \ell^+\nu_\ell)$ | Total branching ratio of $B^+\to \omega \ell^+\nu_\ell$ |  |
| `Rtaul(B+->omegalnu)` | $R_{\tau \ell}(B^+\to \omega \ell^+\nu)$ | Ratio of total branching ratios of $B^+\to \omega \tau^+ \nu_\tau$ and $B^+\to \omega \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `dBR/dq2(B+->omegalnu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \omega \ell^+\nu_\ell)$ | Differential branching ratio of $B^+\to \omega \ell^+\nu_\ell$ | `q2` |


### $B^+\to \omega \mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->omegamunu)` | $\langle\text{BR}\rangle(B^+\to \omega \mu^+\nu_\mu)$ | Binned branching ratio of $B^+\to \omega \mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<Rmue>(B+->omegalnu)` | $\langle R_{\mu e} \rangle(B^+\to \omega \ell^+\nu)$ | Ratio of partial branching ratios of $B^+\to \omega \mu^+ \nu_\mu$ and $B^+\to \omega e^+ \nu_e$ | `q2min`, `q2max` |
| `<Rtaumu>(B+->omegalnu)` | $\langle R_{\tau \mu} \rangle(B^+\to \omega \ell^+\nu)$ | Ratio of partial branching ratios of $B^+\to \omega \tau^+ \nu_\tau$ and $B^+\to \omega \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B+->omegamunu)` | $\text{BR}(B^+\to \omega \mu^+\nu_\mu)$ | Total branching ratio of $B^+\to \omega \mu^+\nu_\mu$ |  |
| `Rmue(B+->omegalnu)` | $R_{\mu e}(B^+\to \omega \ell^+\nu)$ | Ratio of total branching ratios of $B^+\to \omega \mu^+ \nu_\mu$ and $B^+\to \omega e^+ \nu_e$ | `q2min`, `q2max` |
| `Rtaumu(B+->omegalnu)` | $R_{\tau \mu}(B^+\to \omega \ell^+\nu)$ | Ratio of total branching ratios of $B^+\to \omega \tau^+ \nu_\tau$ and $B^+\to \omega \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->omegamunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \omega \mu^+\nu_\mu)$ | Differential branching ratio of $B^+\to \omega \mu^+\nu_\mu$ | `q2` |


### $B^+\to \omega \tau^+\nu_\tau$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->omegataunu)` | $\langle\text{BR}\rangle(B^+\to \omega \tau^+\nu_\tau)$ | Binned branching ratio of $B^+\to \omega \tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<Rtaul>(B+->omegalnu)` | $\langle R_{\tau \ell} \rangle(B^+\to \omega \ell^+\nu)$ | Ratio of partial branching ratios of $B^+\to \omega \tau^+ \nu_\tau$ and $B^+\to \omega \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `<Rtaumu>(B+->omegalnu)` | $\langle R_{\tau \mu} \rangle(B^+\to \omega \ell^+\nu)$ | Ratio of partial branching ratios of $B^+\to \omega \tau^+ \nu_\tau$ and $B^+\to \omega \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B+->omegataunu)` | $\text{BR}(B^+\to \omega \tau^+\nu_\tau)$ | Total branching ratio of $B^+\to \omega \tau^+\nu_\tau$ |  |
| `Rtaul(B+->omegalnu)` | $R_{\tau \ell}(B^+\to \omega \ell^+\nu)$ | Ratio of total branching ratios of $B^+\to \omega \tau^+ \nu_\tau$ and $B^+\to \omega \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `Rtaumu(B+->omegalnu)` | $R_{\tau \mu}(B^+\to \omega \ell^+\nu)$ | Ratio of total branching ratios of $B^+\to \omega \tau^+ \nu_\tau$ and $B^+\to \omega \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->omegataunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \omega \tau^+\nu_\tau)$ | Differential branching ratio of $B^+\to \omega \tau^+\nu_\tau$ | `q2` |


### $B^+\to \omega e^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->omegaenu)` | $\langle\text{BR}\rangle(B^+\to \omega e^+\nu_e)$ | Binned branching ratio of $B^+\to \omega e^+\nu_e$ | `q2min`, `q2max` |
| `<Rmue>(B+->omegalnu)` | $\langle R_{\mu e} \rangle(B^+\to \omega \ell^+\nu)$ | Ratio of partial branching ratios of $B^+\to \omega \mu^+ \nu_\mu$ and $B^+\to \omega e^+ \nu_e$ | `q2min`, `q2max` |
| `BR(B+->omegaenu)` | $\text{BR}(B^+\to \omega e^+\nu_e)$ | Total branching ratio of $B^+\to \omega e^+\nu_e$ |  |
| `Rmue(B+->omegalnu)` | $R_{\mu e}(B^+\to \omega \ell^+\nu)$ | Ratio of total branching ratios of $B^+\to \omega \mu^+ \nu_\mu$ and $B^+\to \omega e^+ \nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B+->omegaenu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \omega e^+\nu_e)$ | Differential branching ratio of $B^+\to \omega e^+\nu_e$ | `q2` |


### $B^+\to \rho^0\ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->rholnu)` | $\langle\text{BR}\rangle(B^+\to \rho^0\ell^+\nu_\ell)$ | Binned branching ratio of $B^+\to \rho^0\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<Rtaul>(B->rholnu)` | $\langle R_{\tau \ell} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `BR(B+->rholnu)` | $\text{BR}(B^+\to \rho^0\ell^+\nu_\ell)$ | Total branching ratio of $B^+\to \rho^0\ell^+\nu_\ell$ |  |
| `Rtaul(B->rholnu)` | $R_{\tau \ell}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `dBR/dq2(B+->rholnu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \rho^0\ell^+\nu_\ell)$ | Differential branching ratio of $B^+\to \rho^0\ell^+\nu_\ell$ | `q2` |


### $B^+\to \rho^0\mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->rhomunu)` | $\langle\text{BR}\rangle(B^+\to \rho^0\mu^+\nu_\mu)$ | Binned branching ratio of $B^+\to \rho^0\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<Rmue>(B->rholnu)` | $\langle R_{\mu e} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\mu^+ \nu_\mu$ and $B\to \rhoe^+ \nu_e$ | `q2min`, `q2max` |
| `<Rtaumu>(B->rholnu)` | $\langle R_{\tau \mu} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B+->rhomunu)` | $\text{BR}(B^+\to \rho^0\mu^+\nu_\mu)$ | Total branching ratio of $B^+\to \rho^0\mu^+\nu_\mu$ |  |
| `Rmue(B->rholnu)` | $R_{\mu e}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\mu^+ \nu_\mu$ and $B\to \rhoe^+ \nu_e$ | `q2min`, `q2max` |
| `Rtaumu(B->rholnu)` | $R_{\tau \mu}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->rhomunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \rho^0\mu^+\nu_\mu)$ | Differential branching ratio of $B^+\to \rho^0\mu^+\nu_\mu$ | `q2` |


### $B^+\to \rho^0\tau^+\nu_\tau$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->rhotaunu)` | $\langle\text{BR}\rangle(B^+\to \rho^0\tau^+\nu_\tau)$ | Binned branching ratio of $B^+\to \rho^0\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<Rtaul>(B->rholnu)` | $\langle R_{\tau \ell} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `<Rtaumu>(B->rholnu)` | $\langle R_{\tau \mu} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B+->rhotaunu)` | $\text{BR}(B^+\to \rho^0\tau^+\nu_\tau)$ | Total branching ratio of $B^+\to \rho^0\tau^+\nu_\tau$ |  |
| `Rtaul(B->rholnu)` | $R_{\tau \ell}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `Rtaumu(B->rholnu)` | $R_{\tau \mu}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B+->rhotaunu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \rho^0\tau^+\nu_\tau)$ | Differential branching ratio of $B^+\to \rho^0\tau^+\nu_\tau$ | `q2` |


### $B^+\to \rho^0e^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B+->rhoenu)` | $\langle\text{BR}\rangle(B^+\to \rho^0e^+\nu_e)$ | Binned branching ratio of $B^+\to \rho^0e^+\nu_e$ | `q2min`, `q2max` |
| `<Rmue>(B->rholnu)` | $\langle R_{\mu e} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\mu^+ \nu_\mu$ and $B\to \rhoe^+ \nu_e$ | `q2min`, `q2max` |
| `BR(B+->rhoenu)` | $\text{BR}(B^+\to \rho^0e^+\nu_e)$ | Total branching ratio of $B^+\to \rho^0e^+\nu_e$ |  |
| `Rmue(B->rholnu)` | $R_{\mu e}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\mu^+ \nu_\mu$ and $B\to \rhoe^+ \nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B+->rhoenu)` | $\frac{d\text{BR}}{dq^2}(B^+\to \rho^0e^+\nu_e)$ | Differential branching ratio of $B^+\to \rho^0e^+\nu_e$ | `q2` |


### $B^0\to D^{\ast -}\ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->D*lnu)` | $\langle\text{BR}\rangle(B^0\to D^{\ast -}\ell^+\nu_\ell)$ | Binned branching ratio of $B^0\to D^{\ast -}\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<Rtaul>(B->D*lnu)` | $\langle R_{\tau \ell} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `BR(B0->D*lnu)` | $\text{BR}(B^0\to D^{\ast -}\ell^+\nu_\ell)$ | Total branching ratio of $B^0\to D^{\ast -}\ell^+\nu_\ell$ |  |
| `Rtaul(B->D*lnu)` | $R_{\tau \ell}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `dBR/dq2(B0->D*lnu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{\ast -}\ell^+\nu_\ell)$ | Differential branching ratio of $B^0\to D^{\ast -}\ell^+\nu_\ell$ | `q2` |


### $B^0\to D^{\ast -}\mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->D*munu)` | $\langle\text{BR}\rangle(B^0\to D^{\ast -}\mu^+\nu_\mu)$ | Binned branching ratio of $B^0\to D^{\ast -}\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<Rmue>(B->D*lnu)` | $\langle R_{\mu e} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\mu^+ \nu_\mu$ and $B\to D^{\ast}e^+ \nu_e$ | `q2min`, `q2max` |
| `<Rtaumu>(B->D*lnu)` | $\langle R_{\tau \mu} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B0->D*munu)` | $\text{BR}(B^0\to D^{\ast -}\mu^+\nu_\mu)$ | Total branching ratio of $B^0\to D^{\ast -}\mu^+\nu_\mu$ |  |
| `Rmue(B->D*lnu)` | $R_{\mu e}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\mu^+ \nu_\mu$ and $B\to D^{\ast}e^+ \nu_e$ | `q2min`, `q2max` |
| `Rtaumu(B->D*lnu)` | $R_{\tau \mu}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->D*munu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{\ast -}\mu^+\nu_\mu)$ | Differential branching ratio of $B^0\to D^{\ast -}\mu^+\nu_\mu$ | `q2` |


### $B^0\to D^{\ast -}\tau^+\nu_\tau$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->D*taunu)` | $\langle\text{BR}\rangle(B^0\to D^{\ast -}\tau^+\nu_\tau)$ | Binned branching ratio of $B^0\to D^{\ast -}\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<Rtaul>(B->D*lnu)` | $\langle R_{\tau \ell} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `<Rtaumu>(B->D*lnu)` | $\langle R_{\tau \mu} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B0->D*taunu)` | $\text{BR}(B^0\to D^{\ast -}\tau^+\nu_\tau)$ | Total branching ratio of $B^0\to D^{\ast -}\tau^+\nu_\tau$ |  |
| `Rtaul(B->D*lnu)` | $R_{\tau \ell}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `Rtaumu(B->D*lnu)` | $R_{\tau \mu}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\tau^+ \nu_\tau$ and $B\to D^{\ast}\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->D*taunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{\ast -}\tau^+\nu_\tau)$ | Differential branching ratio of $B^0\to D^{\ast -}\tau^+\nu_\tau$ | `q2` |


### $B^0\to D^{\ast -}e^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->D*enu)` | $\langle\text{BR}\rangle(B^0\to D^{\ast -}e^+\nu_e)$ | Binned branching ratio of $B^0\to D^{\ast -}e^+\nu_e$ | `q2min`, `q2max` |
| `<Rmue>(B->D*lnu)` | $\langle R_{\mu e} \rangle(B\to D^{\ast}\ell^+\nu)$ | Ratio of partial branching ratios of $B\to D^{\ast}\mu^+ \nu_\mu$ and $B\to D^{\ast}e^+ \nu_e$ | `q2min`, `q2max` |
| `BR(B0->D*enu)` | $\text{BR}(B^0\to D^{\ast -}e^+\nu_e)$ | Total branching ratio of $B^0\to D^{\ast -}e^+\nu_e$ |  |
| `Rmue(B->D*lnu)` | $R_{\mu e}(B\to D^{\ast}\ell^+\nu)$ | Ratio of total branching ratios of $B\to D^{\ast}\mu^+ \nu_\mu$ and $B\to D^{\ast}e^+ \nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B0->D*enu)` | $\frac{d\text{BR}}{dq^2}(B^0\to D^{\ast -}e^+\nu_e)$ | Differential branching ratio of $B^0\to D^{\ast -}e^+\nu_e$ | `q2` |


### $B^0\to \rho^-\ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->rholnu)` | $\langle\text{BR}\rangle(B^0\to \rho^-\ell^+\nu_\ell)$ | Binned branching ratio of $B^0\to \rho^-\ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<Rtaul>(B->rholnu)` | $\langle R_{\tau \ell} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `BR(B0->rholnu)` | $\text{BR}(B^0\to \rho^-\ell^+\nu_\ell)$ | Total branching ratio of $B^0\to \rho^-\ell^+\nu_\ell$ |  |
| `Rtaul(B->rholnu)` | $R_{\tau \ell}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `dBR/dq2(B0->rholnu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \rho^-\ell^+\nu_\ell)$ | Differential branching ratio of $B^0\to \rho^-\ell^+\nu_\ell$ | `q2` |


### $B^0\to \rho^-\mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->rhomunu)` | $\langle\text{BR}\rangle(B^0\to \rho^-\mu^+\nu_\mu)$ | Binned branching ratio of $B^0\to \rho^-\mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<Rmue>(B->rholnu)` | $\langle R_{\mu e} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\mu^+ \nu_\mu$ and $B\to \rhoe^+ \nu_e$ | `q2min`, `q2max` |
| `<Rtaumu>(B->rholnu)` | $\langle R_{\tau \mu} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B0->rhomunu)` | $\text{BR}(B^0\to \rho^-\mu^+\nu_\mu)$ | Total branching ratio of $B^0\to \rho^-\mu^+\nu_\mu$ |  |
| `Rmue(B->rholnu)` | $R_{\mu e}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\mu^+ \nu_\mu$ and $B\to \rhoe^+ \nu_e$ | `q2min`, `q2max` |
| `Rtaumu(B->rholnu)` | $R_{\tau \mu}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->rhomunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \rho^-\mu^+\nu_\mu)$ | Differential branching ratio of $B^0\to \rho^-\mu^+\nu_\mu$ | `q2` |


### $B^0\to \rho^-\tau^+\nu_\tau$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->rhotaunu)` | $\langle\text{BR}\rangle(B^0\to \rho^-\tau^+\nu_\tau)$ | Binned branching ratio of $B^0\to \rho^-\tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<Rtaul>(B->rholnu)` | $\langle R_{\tau \ell} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `<Rtaumu>(B->rholnu)` | $\langle R_{\tau \mu} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(B0->rhotaunu)` | $\text{BR}(B^0\to \rho^-\tau^+\nu_\tau)$ | Total branching ratio of $B^0\to \rho^-\tau^+\nu_\tau$ |  |
| `Rtaul(B->rholnu)` | $R_{\tau \ell}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `Rtaumu(B->rholnu)` | $R_{\tau \mu}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\tau^+ \nu_\tau$ and $B\to \rho\mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(B0->rhotaunu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \rho^-\tau^+\nu_\tau)$ | Differential branching ratio of $B^0\to \rho^-\tau^+\nu_\tau$ | `q2` |


### $B^0\to \rho^-e^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(B0->rhoenu)` | $\langle\text{BR}\rangle(B^0\to \rho^-e^+\nu_e)$ | Binned branching ratio of $B^0\to \rho^-e^+\nu_e$ | `q2min`, `q2max` |
| `<Rmue>(B->rholnu)` | $\langle R_{\mu e} \rangle(B\to \rho\ell^+\nu)$ | Ratio of partial branching ratios of $B\to \rho\mu^+ \nu_\mu$ and $B\to \rhoe^+ \nu_e$ | `q2min`, `q2max` |
| `BR(B0->rhoenu)` | $\text{BR}(B^0\to \rho^-e^+\nu_e)$ | Total branching ratio of $B^0\to \rho^-e^+\nu_e$ |  |
| `Rmue(B->rholnu)` | $R_{\mu e}(B\to \rho\ell^+\nu)$ | Ratio of total branching ratios of $B\to \rho\mu^+ \nu_\mu$ and $B\to \rhoe^+ \nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(B0->rhoenu)` | $\frac{d\text{BR}}{dq^2}(B^0\to \rho^-e^+\nu_e)$ | Differential branching ratio of $B^0\to \rho^-e^+\nu_e$ | `q2` |


### $B_s\to K^{* -} \ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(Bs->K*lnu)` | $\langle\text{BR}\rangle(B_s\to K^{* -} \ell^+\nu_\ell)$ | Binned branching ratio of $B_s\to K^{* -} \ell^+\nu_\ell$ | `q2min`, `q2max` |
| `<Rtaul>(Bs->K*lnu)` | $\langle R_{\tau \ell} \rangle(B_s\to K^{* -} \ell^+\nu)$ | Ratio of partial branching ratios of $B_s\to K^{* -} \tau^+ \nu_\tau$ and $B_s\to K^{* -} \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `BR(Bs->K*lnu)` | $\text{BR}(B_s\to K^{* -} \ell^+\nu_\ell)$ | Total branching ratio of $B_s\to K^{* -} \ell^+\nu_\ell$ |  |
| `Rtaul(Bs->K*lnu)` | $R_{\tau \ell}(B_s\to K^{* -} \ell^+\nu)$ | Ratio of total branching ratios of $B_s\to K^{* -} \tau^+ \nu_\tau$ and $B_s\to K^{* -} \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `dBR/dq2(Bs->K*lnu)` | $\frac{d\text{BR}}{dq^2}(B_s\to K^{* -} \ell^+\nu_\ell)$ | Differential branching ratio of $B_s\to K^{* -} \ell^+\nu_\ell$ | `q2` |


### $B_s\to K^{* -} \mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(Bs->K*munu)` | $\langle\text{BR}\rangle(B_s\to K^{* -} \mu^+\nu_\mu)$ | Binned branching ratio of $B_s\to K^{* -} \mu^+\nu_\mu$ | `q2min`, `q2max` |
| `<Rmue>(Bs->K*lnu)` | $\langle R_{\mu e} \rangle(B_s\to K^{* -} \ell^+\nu)$ | Ratio of partial branching ratios of $B_s\to K^{* -} \mu^+ \nu_\mu$ and $B_s\to K^{* -} e^+ \nu_e$ | `q2min`, `q2max` |
| `<Rtaumu>(Bs->K*lnu)` | $\langle R_{\tau \mu} \rangle(B_s\to K^{* -} \ell^+\nu)$ | Ratio of partial branching ratios of $B_s\to K^{* -} \tau^+ \nu_\tau$ and $B_s\to K^{* -} \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(Bs->K*munu)` | $\text{BR}(B_s\to K^{* -} \mu^+\nu_\mu)$ | Total branching ratio of $B_s\to K^{* -} \mu^+\nu_\mu$ |  |
| `Rmue(Bs->K*lnu)` | $R_{\mu e}(B_s\to K^{* -} \ell^+\nu)$ | Ratio of total branching ratios of $B_s\to K^{* -} \mu^+ \nu_\mu$ and $B_s\to K^{* -} e^+ \nu_e$ | `q2min`, `q2max` |
| `Rtaumu(Bs->K*lnu)` | $R_{\tau \mu}(B_s\to K^{* -} \ell^+\nu)$ | Ratio of total branching ratios of $B_s\to K^{* -} \tau^+ \nu_\tau$ and $B_s\to K^{* -} \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(Bs->K*munu)` | $\frac{d\text{BR}}{dq^2}(B_s\to K^{* -} \mu^+\nu_\mu)$ | Differential branching ratio of $B_s\to K^{* -} \mu^+\nu_\mu$ | `q2` |


### $B_s\to K^{* -} \tau^+\nu_\tau$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(Bs->K*taunu)` | $\langle\text{BR}\rangle(B_s\to K^{* -} \tau^+\nu_\tau)$ | Binned branching ratio of $B_s\to K^{* -} \tau^+\nu_\tau$ | `q2min`, `q2max` |
| `<Rtaul>(Bs->K*lnu)` | $\langle R_{\tau \ell} \rangle(B_s\to K^{* -} \ell^+\nu)$ | Ratio of partial branching ratios of $B_s\to K^{* -} \tau^+ \nu_\tau$ and $B_s\to K^{* -} \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `<Rtaumu>(Bs->K*lnu)` | $\langle R_{\tau \mu} \rangle(B_s\to K^{* -} \ell^+\nu)$ | Ratio of partial branching ratios of $B_s\to K^{* -} \tau^+ \nu_\tau$ and $B_s\to K^{* -} \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `BR(Bs->K*taunu)` | $\text{BR}(B_s\to K^{* -} \tau^+\nu_\tau)$ | Total branching ratio of $B_s\to K^{* -} \tau^+\nu_\tau$ |  |
| `Rtaul(Bs->K*lnu)` | $R_{\tau \ell}(B_s\to K^{* -} \ell^+\nu)$ | Ratio of total branching ratios of $B_s\to K^{* -} \tau^+ \nu_\tau$ and $B_s\to K^{* -} \ell^+ \nu_\ell$ | `q2min`, `q2max` |
| `Rtaumu(Bs->K*lnu)` | $R_{\tau \mu}(B_s\to K^{* -} \ell^+\nu)$ | Ratio of total branching ratios of $B_s\to K^{* -} \tau^+ \nu_\tau$ and $B_s\to K^{* -} \mu^+ \nu_\mu$ | `q2min`, `q2max` |
| `dBR/dq2(Bs->K*taunu)` | $\frac{d\text{BR}}{dq^2}(B_s\to K^{* -} \tau^+\nu_\tau)$ | Differential branching ratio of $B_s\to K^{* -} \tau^+\nu_\tau$ | `q2` |


### $B_s\to K^{* -} e^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `<BR>(Bs->K*enu)` | $\langle\text{BR}\rangle(B_s\to K^{* -} e^+\nu_e)$ | Binned branching ratio of $B_s\to K^{* -} e^+\nu_e$ | `q2min`, `q2max` |
| `<Rmue>(Bs->K*lnu)` | $\langle R_{\mu e} \rangle(B_s\to K^{* -} \ell^+\nu)$ | Ratio of partial branching ratios of $B_s\to K^{* -} \mu^+ \nu_\mu$ and $B_s\to K^{* -} e^+ \nu_e$ | `q2min`, `q2max` |
| `BR(Bs->K*enu)` | $\text{BR}(B_s\to K^{* -} e^+\nu_e)$ | Total branching ratio of $B_s\to K^{* -} e^+\nu_e$ |  |
| `Rmue(Bs->K*lnu)` | $R_{\mu e}(B_s\to K^{* -} \ell^+\nu)$ | Ratio of total branching ratios of $B_s\to K^{* -} \mu^+ \nu_\mu$ and $B_s\to K^{* -} e^+ \nu_e$ | `q2min`, `q2max` |
| `dBR/dq2(Bs->K*enu)` | $\frac{d\text{BR}}{dq^2}(B_s\to K^{* -} e^+\nu_e)$ | Differential branching ratio of $B_s\to K^{* -} e^+\nu_e$ | `q2` |


## $B\to X\ell\nu$

### $B\to X_c\ell^+\nu_\ell$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `BR(B->Xclnu)` | $\text{BR}(B\to X_c\ell^+\nu_\ell)$ | Total branching ratio of $B\to X_c\ell^+\nu_\ell$ |  |


### $B\to X_c\mu^+\nu_\mu$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `BR(B->Xcmunu)` | $\text{BR}(B\to X_c\mu^+\nu_\mu)$ | Total branching ratio of $B\to X_c\mu^+\nu_\mu$ |  |


### $B\to X_ce^+\nu_e$

{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|
| `BR(B->Xcenu)` | $\text{BR}(B\to X_ce^+\nu_e)$ | Total branching ratio of $B\to X_ce^+\nu_e$ |  |


