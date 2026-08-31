# Initializing Statistical Forecasting-Import Hierarchies and Data

So as that completes, we have done the bits which we need to do in the model itself.

So setting the source models and getting all of the time correctly set up.

The next two tasks that we're going to carry out are associated with bringing the contents of the data hub and the demand analysis application over into the stat forecasting application or model that will import the product and customer hierarchies.

And then we'll import the data, that the step forecast is going to need.

as it was when we were importing content into demand analysis, the processes for bringing content into the stat forecasting model sit on the pages for them sit within the data hub application.

So if I expand this out here, we can see, here's a set of pages associated with updating the stat forecast application.

So the first thing I'm going to do is the master data, the importing the product and customer hierarchies.

Just before That's good.

And now it’s just a case of running the product hierarchy update and then the customer hierarchy update.

So we'll kick those off.

Okay, so that's completed.

It So let's do the same with customer hierarchy.

Alright.

So that has now updated the product and the customer hierarchy within our stat forecasting application.

And the last data set that we now need to bring across is the sort of transactional order data itself.

After that we're going to go to page 212 Update Transactional Data.

Here's the process that we need to run.

And in this instance actually this is not going to be bringing data from the data hub.

What we need is that forecasting is what's come out of demand analysis, which may have been subjected to training for super sessions, outlier correction and other things like that.

So we're going to run that process.

And at that point we should have statistical forecasting fully populated with the data that it needs to start to work.

That's done.

So, Now let's just move ourselves back to the application stat forecasting application.

There it is.

So now let's see if we can just look at 1 or 2 pages, maybe just one page to see if we do have a forecast being calculated.

So the page I'm going to target is probably this one title, where I'm going to go to action this.

See if we can, get in front of these pages.

Let’s look at best fit analysis.

What do I see here.

So looking up at the top I can see I have a, selected individual product and customer, I can see the range of forecasting methods that we have.

And I can start to click through those so I can see what each of them looks like.

So that's a forecast based on a linear regression.

Maybe we've got something which is trying to apply seasonality to the data as well.

And so on.

So all of my traditional statistical forecasting time series based forecasts are working.

the ones which won't be because there's extra configuration, which we won't cover now.

Those which are using PlanIQ to get their results.

As you can see with those we're not having anything coming through yet.

And that's because we haven't done that step of configuring planner queues, involvement within that forecasting.

