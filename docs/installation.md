---
layout: default
title: Installation
---

# Installation

Since flavio is a Python package that does not need compilation, installation
is fairly simple. The following tutorial will assume that you already have
Python 3 and the Python package manager `pip` installed on your system.

**Note:** If you plan to modify the code and potentially contribute your changes back to
the community, you might follow the steps described in [development install](dev-install.html)
instead.

## Step 1: install dependencies

flavio depends on the `numpy` and `scipy` packages. If you already have them
installed, you can skip to step 2. Otherwise, on Ubuntu, you can install them
via

{% highlight bash %}
sudo apt-get install python3-numpy python3-scipy
{% endhighlight %}

For more detailed install instructions, including other operating systems,
see the [SciPy documentation](http://www.scipy.org/install.html).

To also use the plotting features of flavio, you have to install `matplotlib`
as well.

## Step 2: install flavio

The latest released version is available via [PyPI](https://pypi.python.org/), so
you can install it simply by executing

{% highlight bash %}
pip install flavio
{% endhighlight %}

(or `pip3` instead of `pip` depending on your system).

## (Step 3: install optional dependencies)

While you are now all set to compute predictions in the SM and beyond,
if you want to use all the features of the package, you might want to install
some additional Python packages:

- `matplotlib` for plotting
- `nose` for testing
- `pypmc` and `emcee` for sampling


## Upgrading flavio

If you have installed flavio using `pip`, it is trivial to upgrade it to
a new version. Simply execute

{% highlight bash %}
pip install flavio --upgrade
{% endhighlight %}
