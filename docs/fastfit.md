---
layout: default
title: Fast Fits
---


# "Fast" fits

[As discussed above](fits.html#fast-fit-approach), the "fast" fits defined in flavio are a convenient tool to quickly obtain the likelihood in the space of,
say, two fit parameters (or Wilson coefficients) without having to marginalize
or profile over any nuisance parameter. This can be achieved by precomputing the uncertainties (and their correlations) of all observables within the SM and treating them like an experimental uncertainty (to be added in quadrature with the actual experimental uncertainty). This approach was first used in [arXiv:1411.3161](http://arxiv.org/pdf/1411.3161.pdf) for a global analysis of $b\to s$ transitions -- see section 3.1 for a discussion.

Defining a FastFit is very similar to a Bayesian or frequentist fit, using the class `flavio.statistics.fits.FastFit`. Compared to Bayesian fits, a major difference is that *no prior for fit parameters* is taken into account. Consequently, when fitting SM parameters (rather than Wilson coefficients), the number of fit parameters should usually just be 1 or 2 (for one- or two-dimensional plots), as the fit parameters are not marginalized over.
Compared to both Bayesian and frequentist fits, a major advantage is that the number of nuisance parameters *does not impact on computing time* and
can be large. In fact, one can pass the option `nuisance_parameters='all'` to indicate that all existing parameters (except the fit parameters) will be treated as nuisance parameters.

Having defined the fit instance (let's call it `my_fastfit`), the first step
is to compute the uncertainties of all observables within the SM (varying
all nuisance parameters). Since these theory uncertainties are combined with
the existing experimental uncertainties, the command is called

{% highlight python %}
my_fastfit.make_measurement()
{% endhighlight %}

This part can be very time consuming! The function `make_measurement`
has an optional argument `N` specifying the number of random parameter sets
(default: $N=100$). Larger numbers lead to more accurate results, smaller numbers
take less time. The argument `threads` can be used to enable parallel computation.

Once this is completed, the logarithm of the likelihood can be accessed via
{% highlight python %}
my_fastfit.log_likelihood(x)
{% endhighlight %}
where `x` is a  list (or NumPy array) *only* containing the values of the
fit parameters (or Wilson coefficients). Note that there is no prior probability
for the nuisance parameters, because they have effectively been integrated out.

For more usage details and a full list of options, see the [`FastFit` API docs](http://0.0.0.0:4000/apidoc/flavio/statistics/fits.m.html#flavio.statistics.fits.FastFit).

Several examples of fitting and visualization using the `FastFit` class can be found in the [example repository](https://github.com/flav-io/flavio-examples).
