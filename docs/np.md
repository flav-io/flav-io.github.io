---
layout: default
title: New Physics
---

# Predictions in the presence of new physics

flavio does not implement any specific new physics (NP) models. Rather, it allows
you to specify NP contributions in the form of Wilson coefficients of dimension-6
operators in an effective field theory below the $W$ mass.

A new "parameter point" in the space of the EFT maps to an instance
of `flavio.WilsonCoefficients`. You can get started with your NP scenario by
calling

{% highlight python %}
wc = flavio.WilsonCoefficients()
{% endhighlight %}

By default, all Wilson coefficients vanish. Note that these Wilson coefficients
are defined to be *the new physics contributions only*, so if they vanish
it means we are in the Standard Model.

If you want to go beyond the SM, you need to specify the values of the Wilson
coefficients at some scale. For instance, to get a universal NP contribution to
$B^0$ and $B_s$ mixing
via the operators $(\bar q_R\gamma^\mu b_R)^2$ with $q=d,s$, you can use

{% highlight python %}
wc.set_initial({ 'CVRR_bdbd': 1e-10, 'CVRR_bsbs': 1e-10 }, scale=160 )
{% endhighlight %}

where `wc` is the object created above.
The Wilson coefficients are referred to by their names. You can have a look
at [the complete list of operators and Wilson coefficients](operators.html).

You can call the `set_initial` method
several times, e.g. if you want to add NP contributions to Wilson coefficients
in other sectors. The only constraint is that the scales of the initial values
for Wilson coefficients of operators that mix under RGE must coincide.

Having defined your NP scenario in this way, you can now get the central
value of your favourite observable by calling the function `np_prediction`,
e.g.

{% highlight python %}
flavio.np_prediction('DeltaM_s', wc)
{% endhighlight %}

Where the observable is referred to by its [name](observables.html) as usual.
