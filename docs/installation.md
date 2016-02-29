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

To download and install the most recent development version of flavio, follow
these steps.

- Download [a ZIP archive with the latest code](https://github.com/flav-io/flavio/archive/master.zip)
- Unzip it and enter the folder called `flavio`
- To install the package for your user only, type
{% highlight bash %}
pip3 install -e . --user
{% endhighlight %}
The `-e` switch means that the package is installed in "development mode", so
you can make modifications to the downloaded code and don't have to reinstall.

## (Step 3: install optional dependencies)

While you are now all set to compute predictions in the SM and beyond,
if you want to use all the features of the package, you might want to install
some additional Python packages:

- `matplotlib` for plotting
- `nose` for testing
- `pypmc` and `emcee` for sampling
