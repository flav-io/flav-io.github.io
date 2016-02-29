---
layout: default
title: Development installation
---

# Development installation

If you plan to modify flavio, an installation method slightly different from
the [simplest one](installation.html) is advisable.

This assumes you already have all dependencies (in particular `scipy`,
`numpy` and `pip`) as well as `git` installed.

## Step 1: clone the repository

To get the most recent version of the code and be able to keep it up-to-date,
clone the repository with `git` using

{% highlight bash %}
git clone https://github.com/flav-io/flavio.git
{% endhighlight %}


## Step 2: install flavio

Enter the directory created by `git`

{% highlight bash %}
cd flavio
{% endhighlight %}

and install the package with this command

{% highlight bash %}
pip3 install -e . --user
{% endhighlight %}

(depending on your system, `pip3` might have to be replaced by `pip`).
The `-e` switch means that the package is installed in "development mode", so
you can make modifications to the downloaded code and don't have to reinstall.

## Step 3: run unit tests

To check whether the package has been installed correctly, you can run the unit
tests using `nose` (install it with `pip3 install nose` if necessary).
Just go to the root directory of the package and run

{% highlight bash %}
nosetests3
{% endhighlight %}

(or just `nosetests`, depending on your system).
The output should look something like this:
{% highlight bash %}
.........................................
----------------------------------------------------------------------
Ran 41 tests in 5.135s

OK
{% endhighlight %}
