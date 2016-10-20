#!/usr/bin/env python3

# This script autogenerates the observables.md and subpages as well as the
# parameters.md

import flavio
import os
from collections import OrderedDict

os.chdir('docs')

# this is displayed at the top of every observable subpage
observables_header_table = """

The tables below have been generated automatically from the observables currently
implemented in flavio. The first column is the string name that must  be used
when calling functions such as `flavio.sm_prediction`. The last column lists
the arguments the observable depends on (which can also be empty in case of
a scalar observable).

"""

# this is displayed at the top of the observables overview page
observables_header = """---
layout: default
title: Observables
---

# List of all observables

To display automatically generated tables with lists of all observables
currently implemented in flavio, select a category below. See also the
[notes on conventions](#some-general-notes-on-conventions) at the bottom
of this page.

## Categories

"""

# this is displayed at the bottom of the observables overview page
observables_footer = """
## Some general notes on conventions

- Unless noted explicitly, branching ratios and angular observables always
imply a *CP-average*. For instance, charged $B$ decay modes are always written as
$B^+ \\to \ldots$, but what is meant is the average of the $B^+$ and the $B^-$
decay.
- For lepton flavour violating $B$ decays, no CP-average is made; e.g. the
decay $B^-\\to e^+\mu^-$ (`B+->emu`, *sic*) is distinct from
$B^-\\to\mu^+e^-$ (`B+->mue`) but its rate is equal to $B^+\\to \mu^+e^-$
by CPT.
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

"""

# tree-like observable taxonomy as dictionary
process_dict = flavio.Observable.taxonomy_dict()['Process']

# make filename composed of letters only
def make_filename(s):
    return ''.join([x for x in s.lower() if x.isalpha()])

# make table of observables
def write_obs_table(obs_list, f):
    f.write("""{: class="table"}\n""")
    f.write("""| Name | Symbol | Description | Arguments |\n""")
    f.write("""|------|--------|-------------|-----------|\n""")
    for name in obs_list:
        instance = flavio.Observable.get_instance(name)
        f.write('| `' + name + '` | ')
        f.write(instance.tex  + ' | ' + instance.description  + ' | ' )
        if instance.arguments is not None:
            f.write('`' + '`, `'.join(instance.arguments) + '`')
        f.write(' |\n')
    f.write('\n\n')

# walk the tree and write headings and tables recursively
def recurse_categories(d, f, n):
    if not any(d.values()):
        write_obs_table(sorted(d.keys()), f)
    else:
        for k, v in sorted(d.items()):
            if v:
                f.write(n*'#' + ' ' + k + 2*'\n')
                recurse_categories(v, f, n + 1)

# count the leaves of the tree, i.e. nunmber of observables (with double-counting)
def count_leaves(d, l=[]):
    for k, v in d.items():
        if v:
            count_leaves(v, l)
        else:
            l.append(k)
    return len(l)

# add plural-'s' or not
def plural_s(n):
    if n>1:
        return 's'
    else:
        return ''

# write the observables overview page and subpages
with open('observables.md', 'w') as f:
    f.write(observables_header)
    for k1, v1 in sorted(process_dict.items()):
        f.write("\n\n### " + k1 + "\n\n")
        for k2, v2 in sorted(v1.items()):
            filename = 'obs/' + make_filename(k1) + '-' + make_filename(k2)
            n_obs = count_leaves(v2, []) # number of observables per category
            f.write("""\n- [""" + k2 + """]("""+filename+""".html) ("""+ str(n_obs) +""" observable""" + plural_s(n_obs) + """)\n""")
            with open(filename + '.md', 'w') as f2:
                f2.write("""---\nlayout: default\ntitle: Observables - """ + k1 + """ - """ + k2 + """\n---\n\n""")
                f2.write("""# Observables / """ + k1 + " / " + k2 + "\n\n")
                f2.write(observables_header_table)
                # table of contents
                f2.write("""

{::options toc_levels="2" /}

* TOC
{:toc}

""")
                recurse_categories(v2, f2, 2)
    f.write(observables_footer)


# write the parameter list page
with open('parameters.md', 'w') as f:
    f.write("""---
layout: default
title: Parameters
---

# List of all parameters

This is an automatically generated list  of all parameters defined in the
default configuration of flavio. The first column contains the string name
of the parameter.


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
