---
layout: default
title: Installation
---

# Installation

Since flavio is a Python package that does not need compilation, installation
is fairly simple. The following will assume that you already have
Python version 3.5 or above and the Python package manager `pip` installed on your system.

**Note:** If you plan to modify the code and potentially contribute your changes back to
the community, you might follow the steps described in [development install](dev-install.html)
instead.

## Install flavio

The latest released version is available via [PyPI](https://pypi.python.org/), so
you can install it simply by executing

{% highlight bash %}
pip3 install flavio
{% endhighlight %}

(depending on your system, the Python 3 version of `pip` could also be called
`pip-3.3` or just `pip`). You might want to add the `--user` switch to
install it in your home directory rather than system-wide.

## Install optional dependencies

While you are now all set to compute predictions in the SM and beyond,
if you want to use all the features of the package, you might want to install
some additional Python packages. The command

{% highlight bash %}
pip3 install flavio[plotting,sampling]
{% endhighlight %}

will install `matplotlib`, that is required for plotting, as well as some
packages useful for Bayesian analyses.


## Upgrading flavio

If you have installed flavio using `pip`, it is trivial to upgrade it to
a new version. Simply execute

{% highlight bash %}
pip3 install flavio --upgrade
{% endhighlight %}
