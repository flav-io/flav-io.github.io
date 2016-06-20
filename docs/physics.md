---
layout: default
title: Physics implementation notes
---

# Notes on physics implementations

This document collects some details about the implementation of the physical
observables. It should be seen as a work in progress -- when in doubt, better
look at the source code.


## $\Delta F=1$ Wilson coefficients

- NNLO QCD corrections and NLO electroweak corrections to the running and
initial conditions of [all Wilson coefficients](operators.html) are taken
into account, see [arXiv:1102.5650](http://www.arxiv.org/abs/1102.5650) for references.
The exception is $C_9$, where NLO electroweak corrections are not fully known
yet (and the resulting uncertainty is currently not accounted for).

## $B\to K^\ast\ell^+\ell^-$

- By default, the $B\to K^\ast$ form factors from the combined fit to lattice
and light-cone sum rules in
[arXiv:1503.05534v2](http://www.arxiv.org/abs/1503.05534v2)
are used.
- NNLL corrections to the matrix elements of $O_{1,2}$ are taken numerically from
[arXiv:0810.4077](http://www.arxiv.org/abs/0810.4077)
taking into account the full $m_c$ dependence at low and high $q^2$
- Hard spectator scattering and weak annihilation at low $q^2$ is taken from
QCD factorization (Beneke, Feldmann, Seidel) including Cabibbo-suppressed terms
but not uncluding power corrections (in the central value)
- Power corrections to QCDF as well as additional hadronic uncertainties -- e.g.
from charm loops -- are parametrized by helicity- and $q^2$-dependent shifts in
the Wilson coefficients, adopting the ranges in
[arXiv:1411.3161](http://arxiv.org/abs/1411.3161)

Note the following important limitations.

- The default implementation does not give reliable predictions for any
observables when $q^2$ is between roughly 6 and 14 GeV$^2$
- The differential branching ratio does not reproduce local, narrow resonances
such as the $\phi$, or $c\bar c$ states above the open charm threshold.
Direct comparisons to experiment should thus only be made for sufficiently wide
bins.

## $B\to K\ell^+\ell^-$

- By default, The $B\to K$ form factors are taken from the lattice calculation
in
 [arXiv:1509.06235v1](http://arxiv.org/abs/1509.06235v1)
- For hadronic uncertainties beyond the form factors, the same approach as for
$B\to K^\ast\ell^+\ell^-$ is used, again adopting the ranges in
[arXiv:1411.3161](http://arxiv.org/abs/1411.3161)

The same limitations as in $B\to K^\ast\ell^+\ell^-$ apply.

## $B_s\to \phi\ell^+\ell^-$

- By default, the $B_s\to \phi$ form factors from the combined fit to lattice
and light-cone sum rules in
[arXiv:1503.05534v2](http://www.arxiv.org/abs/1503.05534v2)
are used.
- The effect of the finite $B_s$ lifetime difference is taken into account and
all observables correspond to time-integrated ones.
- The other comments and limitations of $B\to K^\ast\ell^+\ell^-$ apply.

## $B\to D\ell\nu$

- By default, $B\to  D$ form factors are taken from the lattice calculation in
[arXiv:1505.03925](http://arxiv.org/abs/1505.03925)

## $B\to D^\ast\ell\nu$

- By default, $B\to  D^\ast$ form factors are based on HQET (see
  [arXiv:1203.2654](http://arxiv.org/abs/1203.2654)), with shape parameters
  taken from HFAG and the normalization from the lattice
  ([arXiv:1403.0635](http://arxiv.org/abs/1403.0635))

## $B\to \pi\ell\nu$

- By default, $B\to \pi$ form factors are taken from the lattice
calculation in [arXiv:1503.07839](http://arxiv.org/abs/1503.07839).
Note that these have huge uncertainties at low $q^2$ and
should be improved by adding LCSR information in the future (see e.g.
[arXiv:1409.7816](http://arxiv.org/abs/1409.7816)).
