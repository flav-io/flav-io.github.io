---
layout: default
title: Fitting parameters or Wilson coefficients
---

# Fitting parameters or Wilson coefficients

Fitting Standard Model parameters or the allowed values of new physics
contributions to the Wilson coefficicents to existing experimental data
is one of the main purposes of flavio. Making this possible requires two
ingredients:

- experimental measurements of the observables,
- statistical fitting routines.

Please note that this functionality is still in the early stages of
development, so interfaces may change in the future.

## Experimental data

All experimental measurements are included in the YAML file `measurements.yml`
([view on Github](https://github.com/flav-io/flavio/blob/master/flavio/data/measurements.yml)).

A "measurement" (represented internally as an instance of `flavio.Measurement`)
is defined as one or more observables with a central value and uncertainties
attached to it, with uncertainties between the observables possibly correlated.

To add additional measurements not included in the above file, created your
own file in the same format and add any measurements you like. You can then
load the file by

{% highlight python %}
flavio.measurements.load('my_measurements.yml')
{% endhighlight %}

Needless to say, you are welcome to add any missing measurements via a
pull request on Github.

## Fitting routines

Fitting parameters to data requires fixing a statistical approach (Bayesian
vs. frequentist). While flavio is designed to accomodate different approaches,
at present only two possibilities are implemented:

- a Bayesian fit,
- a "fast" version of the Bayesian fit not requiring marginalization.

### Bayesian fits

#### Fitting parameters

To define a Bayesian fit of SM parameters (e.g. the CKM parameters) to
experimental data, the following inputs have to be specified:

- a unique name for the fit
- input parameters with uncertainties in the form of a `flavio.ParameterConstraints`
instance (you can simply use `flavio.default_parameters`)
- a list of parameters of interest (see the [full list of parameters](parameters.html)),
- a list of nuisance parameters (that are varied in the fit as well).

For instance, a CKM fit could look like

{% highlight python %}
import flavio.statistics.fits

ckmfit = flavio.statistics.fits.BayesianFit(
  name = 'SM CKM fit',
  par_obj = flavio.default_parameters,
  fit_parameters = ['Vus', 'Vub', 'Vcb', 'gamma'],
  nuisance_parameters = ['bag_B0_1', ...]
  )
{% endhighlight %}

(not showing the full list  of nuisance parameters). Once defined, you can
access the logarithm of the target distribution (likelihood times prior
probability) via

{% highlight python %}
ckmfit.log_target(x)
{% endhighlight %}

where x is a list (or NumPy array) of real numbers, with the first four
being the values of the fit parameters and the remaining ones the values of
the nuisance parameters.

To obtain the posterior probability distribution, Markov Chain Monte Carlo  (MCMC)
techniques can be used. At present, simple interfaces to the
[pypmc](https://github.com/fredRos/pypmc)
and
[emcee](http://dan.iel.fm/emcee)
packages are implemented, acessible via
`flavio.statistics.fits.fitters.pypmc`
and
`flavio.statistics.fits.fitters.emcee`.

#### Fitting Wilson coefficients

To fit Wilson coefficients in addition to (or instead of) parameters,
the following four additional inputs have to be passed when defining the fit instance:

- a list of names of coefficients (or functions of coefficients) to be fitted,
- a function relating these coefficients to actual Wilson coefficients
defined in the [flavio basis](operators.html),
- an input scale where the Wilson coefficients are defined (defaults to 160 GeV),
- optionally, a function returning the prior probability in the space of the
coefficients (defaults to flat).

The first two items are necessary as the quantities to be fitted need to be real
numbers, while the Wilson coefficients are in general complex objects, so real
and imaginary parts have to be treated as independent fit parameters.
In addition, this allows to fit constrained scenarios such as MFV or models
with lepton flavour universality.

For details please consult the [API docs](http://flav-io.github.io/apidoc/flavio/statistics/fits.m.html).

### "Fast" fits

Bayesian fits with a large number of nuisance parameters are computationally
intensive and thus time consuming. Sometimes, it can be useful to be able to
directly evaluate the probability in the space of, say, two Wilson coefficients.
This can be achieved by precomputing the uncertainties (and their correlations)
of all observables
within the SM and treating them like an experimental uncertainty (to be added
in quadrature with the actual experimental uncertainty). This approach was
used in [arXiv:1411.3161](http://arxiv.org/pdf/1411.3161.pdf)
for a global analysis of $b\to s$ transitions -- see section 3.1 for a discussion.

Another use case would be to plot the constraints from a single CKM observable
in the $\bar\rho$-$\bar\eta$ plane as a band.

Defining a FastFit is very similar to a BayesianFit, using the class
`flavio.statistics.fits.FastFit`. The main differences are

- when fitting SM parameters, the number of fit parameters should usually just be
1 or 2 (for one- or two-dimensional plots),
as the fit parameters are not marginalized over
- the number of nuisance parameters does *not* impact on computation time and
can be large.

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
take less time.

Once this is completed, the logarithm of the likelihood can be accessed via
{% highlight python %}
my_fastfit.log_likelihood(x)
{% endhighlight %}
where `x` is a  list (or NumPy array) *only* containing the values of the
fit parameters (or Wilson coefficients). Note that there is no prior probability
for the nuisance parameters (and non-flat priors for the fit parameters are
currently not supported by `FastFit`).
