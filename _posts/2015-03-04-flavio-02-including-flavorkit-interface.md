---
layout: blog
title: New version including FlavorKit interface
date: 2015-03-04 12:00
---

flavio 0.2 is now available through `pip`.

<!-- more -->

The main new feature is an interface to
[SARAH](https://sarah.hepforge.org/)/[FlavorKit](http://arxiv.org/abs/1405.1434).
With these tools, you can compute new physics contributions to $\Delta F=1$
Wilson coefficients in a large number of new physics models. Interfacing
them with flavio, you can compute all the observables the code offers.
For details, check the [the documentation](/docs/interface.html).

To read the output files in SLHA format, code from the
[Rosetta](http://arxiv.org/abs/1508.05895) package was
adapted.

This version also corrects a critical bug in the SM contribution to the
$\Delta F=2$ Wilson coefficient.

Special thanks to:

- Florian Staub and Avelino Vicente for modifying SARAH/FlavorKit
- Ken Mimasu for kind permission to adapt the Rosetta SLHA parser
