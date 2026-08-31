# Configuring and Exploring Statistical Forecasting-method utilization

Okay, to the last bit of the exercise we just want to touch on is to quickly talk through some of the of the parameters that are available for reviewing the application application section 900 into my global parameters.

And there's a few that we will just quickly highlight if we scroll through here.

We've talked about the alpha and beta optimization, some of the additional parameters that to control some of that.

Ultimately, if we want to input a a value of the new that optimize selected from a discrete list, then we can do, we've talked about our best fit parameters, to control that calculation.

We looked in the previous exercise at Disaggregating and how we can use things like variability to take a forecast from a higher level and disaggregated.

We didn't talk about seasonality.

That's an interesting one.

This parameter here controls whether or not we want to apply a seasonal index to those forecast methods, which do not inherently include seasonality themselves.

So if we just go back to our best fit page and take an example, some methods would include seasonality, multiplicative decomposition, is a method which will understand and will will include seasonality within the forecast.

And you can see that in the shape that we see here.

Another method, like a simple moving average will not inherently include seasonality as with some of the trending methods.

They will understand, a growth rate of decline, but not seasonality.

So the parameter that we have available to us is to say, do we want to overlay seasonality on top of the non seasonal methods.

So if we're back into this page, many of the other parameters will control the behavior of individual forecasting methods.

So as an example we've just looked at it on the previous page for the method, which is to forecast based upon a moving average.

Then this control, how many periods do I want to calculate that moving average over and is one example of that.

Or there's a rolling linear regression method which again, as an input of a number of periods over which we want to calculate that linear regression.

Okay.

So just getting back to the slides, just to confirm what we have worked with and what we should configure.

So we talked about alphas and betas.

The configuration task that really is to set up that discrete list.

Being conscious of the impact how the model size we talked about best fit calculation and how it's important to configure the right parameters for the lead time, the period to and the number of tests, and to try to broadly line those up with the dynamics of the customer supply chain.

And then we just finished off with a very quick look at some of the other parameters which are available.

