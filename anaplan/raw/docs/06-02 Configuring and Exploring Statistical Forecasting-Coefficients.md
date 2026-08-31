# Configuring and Exploring Statistical Forecasting-Coefficients

So in terms of the coefficients, the alphas and betas, these are involved in various forecasting methods.

Invariably they will range from a value of 0 through to 1.

And the task of the application is to pick or to select the best value for these coefficients.

They can only do this from a discrete list of options.

So rather than trying to pick any number between 0 and 1, we have to provide the application with a small list that we wanted to test.

And then it will use that to identify the one which it wants to use for the forecasting.

The number of options within these lists is a big driver for model size.

So it is important that they are carefully configured during the implementation.

Giving enough options to aid the performance of the calculation, but not too many options to inflate the model size.

As part of this exercise, we won't go through the theory of these alphas and betas.

There's more relating to that within some of the process rec.

and documentation.

So let's take a look at these coefficients, and management of those within the application.

So back within my statistical forecasting application and under this stat optimization area, we can see there's a page where I can manage the alphas and betas.

So as mentioned it’s only a subset of the methods which need the coefficients.

So simple exponential smoothing, has an alpha parameter.

And we can see here that four options are being set up 0.05, .1 .15 and .2.

Crostons Method, as an alpha coefficient and a beta coefficient.

So they both have their own separate lists of options that are available here.

Same with modify Crostons and also with double exponential smoothing.

To add a new option to this list, it's simply the case of adding it.

So let's now have a value of 0.025.

And we'll submit that and it will be included within the list.

So now the calculation of simple exponential smoothing can have five options for what the alpha parameter might be.

It ultimately has to select one option.

And that will be the basis for the true forecast which gets generated.

So the next task within the application is that selection of best value or optimization as it's referred to within the application.

And we can see the result of that here.

So we can see for the selected product and customer up at the top, that in this particular instance, the value of 0.05 has been identified as being the best performing alpha.

The simple exponential smoothing.

But pick a different product and maybe we'll get a different result.

So in this case for this particular product, that newly added 0.025 is actually the best performing alpha for that particular product, customer combination.

And that's essentially all that's involved with configuring those alpha and beta parameters, setting up the list, referring to the process rec.

and documentation to try and understand a bit more about what these do, and being very conscious of the impact that these have on model size.

