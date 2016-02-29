#!/usr/bin/env python3

import flavio
import os
from collections import OrderedDict

os.chdir('docs')

with open('observables.md', 'w') as f:
    f.write("""---
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
$B^+ \\to \ldots$, but what is meant is the average of the $B^+$ and the $B^-$
decay.
- *"Binned branching ratio"* refers to the $q^2$-integral of the differential branching
ratio, which is a dimensionless number and which coincides with the total branching
ratio if the bin spans the whole kinematic domain. *"Binned differential branching ratio"*
refers instead to the binned branching ratio divided by the bin width, which
has units of GeV$^{-2}$. This definition is frequently used by LHCb and has the
advantage that it is easier  to  compare results in the same kinematic region
but with different bin sizes.
- The conventions for $B\\to V\ell^+\ell^-$ angular observables follow the ones
used by LHCb, which differ from the ones used in many theory papers,
e.g. for $A_\\text{FB}$, $S_4$, $P_4^\prime$, $A_7$, $A_9$
(see e.g. [arXiv:1506.03970](http://www.arxiv.org/abs/1506.03970)).
- Lepton flavour $\ell$ always refers to an average of electron and muon modes.


{: class="table"}
| Name | Symbol | Description | Arguments |
|------|--------|-------------|-----------|\n""")
    for name, instance in flavio.Observable.instances.items():
        f.write('| `' + name + '` | ')
        f.write(instance.tex  + ' | ' + instance.description  + ' | ' )
        if instance.arguments is not None:
            f.write('`' + '`, `'.join(instance.arguments) + '`')
        f.write(' |\n')


with open('parameters.md', 'w') as f:
    f.write("""---
layout: default
title: Parameters
---

# List of all parameters

This is an automatically generated list  of all parameters defined in the
default configuration of flavio. The first coolumn contains the string name
of the parameter.

Note that the LaTeX symbol and description has not yet been defined for
all parametewrs.

{: class="table"}
| Name | Symbol |  Description |
|------|--------|--------------|\n""")
    parameters_sorted = OrderedDict(sorted(flavio.Parameter.instances.items(), key=lambda t: t[0]))
    for name, instance in parameters_sorted.items():
        f.write('| `' + name + '` | ')
        f.write(instance.tex  + ' | ')
        # f.write(flavio.default_parameters.get_constraint_string(name)  + ' | ')
        f.write(instance.description)
        f.write(' |\n')


# with open('implementations.md', 'w') as f:
#     f.write("""---
# layout: default
# title: Implementations
# ---
#
# # List of all auxiliary quantities and their implementations
#
# """)
#     auxf_sorted = OrderedDict(sorted(flavio.AuxiliaryQuantity.instances.items(), key=lambda t: t[0]))
#     impl_sorted = OrderedDict(sorted(flavio.Implementation.instances.items(), key=lambda t: t[0]))
#     for name, instance in auxf_sorted.items():
#         f.write('\n### ')
#         f.write('`' + name + '`\n')
#         f.write(instance.description)
#
#         f.write("""
#
# {: class="table"}
# | Implementation | Description |
# |------|-------------|\n""")
#
#         for i_name, i_instance in impl_sorted.items():
#             if i_instance.quantity != name:
#                 continue
#             f.write('| `' + i_name + '` | ')
#             f.write(i_instance.description)
#             f.write(' |\n')
