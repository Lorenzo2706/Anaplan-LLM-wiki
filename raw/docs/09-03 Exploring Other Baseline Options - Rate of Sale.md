# Exploring Other Baseline Options - Rate of Sale

Okay.

So that's the first step of the exercise is to explore the collaborative planning approach.

The next one that we will look at is rate of sale.

So if I head down to page 120 we can begin to work with this.

So rate of sale planning is a simple driver based planning approach, which is predicated on two independent drivers that we're going to be working with.

One is a store count.

So this really speaks to a consumer goods type of organization that is selling into a retail channel.

And the input becomes a view on how many of the retailer's stores is my product going to be placed within.

Along with the store count.

The other input then is the rate of sale.

So this is the average weekly sales per store that we anticipate seeing.

So in this case I’ll enter 25 as my rate of sale 100 as my stores.

And then the plan simply becomes a multiplication of those two items.

Those inputs will always persist, and can be edited at that point in the future, at any point in the future.

So if I know through conversations with my retail customer that we're going to expand out and be listed in more stores, then I can do that.

Okay.

So having done that, then, similarly, I should be able to head off to page 350.

And now see for a rate of sale plan as another baseline technique that I have.

That's a simple approach to the plan.

In terms of the configuration and implementation perspectives, it's probably one key element which we didn't see there.

And that's how we can actually arrive at a rate of sale without having to necessarily manage it as a pure set of input planning assumptions.

So if I just step back to that rate of sale plan to talk about or to show what I'm referring to Within this, we input the planned rate of sale.

And just as direct data entry.

And that thought was used in the calculation.

And you can also see a line up here at the top where the rate of sale can actually be something which is statistically forecasted.

And in that instance the inputs below it would become more of an override to that statistical forecast for the rate of sale.

So for that average sale per store, in order to determine that statistical forecast, there are two configuration and ongoing user requirements to achieve that.

Firstly, we need to be able to capture the historic store count.

So if I were to look down here within the table, this.

So down here, this is where we can enter the number of stores that we have been placed that the product has been placed in.

Historically.

So potentially let's say we were in 80 stores, from week 17, FY24.

And then maybe we knew that we went into 90 stores several weeks later.

With that historic store count input.

And clearly it's pretty straightforward to calculate the historic rate of sale just by dividing the total demand by the store count.

The key next step, then, is to send the signal to the statistical forecasting model that we actually want to use that data as the input to the stat forecast, rather than the total volumes.

So within the demand analysis, application is the place where we can manage the input to the statistical forecast.

That's the page that we see here.

And we didn't look at this when we talked about statistical forecasting in a previous exercise.

But this is essentially allows us for each product and customer combination.

Select the data set that we want to base its statistical forecast upon.

So we can see everything here is defaulting to collected history.

So the output of the product training and history collection exercises we can select different data.

So maybe we might just want to send the change history.

So we've managed product through possession.

But we don't want to use the result of this list of outlier collection.

And then finally we can see a couple of instances where we can select different types of rate of sale data series.

By selecting that, that then means the data which is sent to statistical forecasting will be this alternative data set.

And we need to know that the answer coming back from statistical forecasting, is also going to be based upon a rate of sale.

And at that point, that's what we would see coming through into our rate of sale system forecast position.

