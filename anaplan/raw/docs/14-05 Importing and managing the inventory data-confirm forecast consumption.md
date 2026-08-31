# Importing and managing the inventory data-confirm forecast consumption

The last piece of this exercise is then just to look at the configuration of forecast consumption.

So let's have a look at that.

So first of all we'll go to a parameter page.

So the global parameter page within inventory planning which is page 900.

Application configuration, 900 global parameters.

And then if I scroll down through these parameters somewhere down here I can see my consumption method.

And the important bit just here is to make sure that we have some consumption method defined.

So it's not left out but we're consuming on some basis.

I will leave it as same period only for now.

We should then be able to see that consumption calculation taking place.

So what's this doing?

So let's just, move this over.

This is giving me a view of my initial demand plan.

Along the side that, what is my committed customer demand?

So this is the open purchase, open sales orders that have been placed by our customers.

So this is actual demand that we need to meet.

And then finally, the consumption process deals with how do we reconcile, a forecasted planned view versus an actual transacted view with those open orders.

So that's our consumption approach here.

Make time shorter.

Yeah.

So as an example, you know, what we're saying here is we had a demand plan of 2,200.

We know that we're actually set on 1,960 of open orders.

Therefore, if I just remove this so it's easier, our unconsumed is the difference.

So, it's 277.

So that means the inventory planner, when looking at their projection, will have clear visibility in terms of the demand—how much is transacted customer orders versus just the result of a planning process.

Where the consumption method approach really matters, I guess, is what we do where that open amount exceeds the plan.

So if I were to bump this up to, 5000, then we have a large spike in our committed customer demand massively exceeds the plan for that week.

With the consumption method as, it is currently set to same period, only then, that basically just gives us a view where there is no under-consumed forecast.

And we got this big spike here.

It may be that in the dynamics of the particular business, that large spike here not only represents the demand for that week, but also for future weeks.

So that, for instance, might be where we would set the consumption method to forwards.

And now that spike not only consumes week 20, but it's consumed week 21 and some of week 22.

So that 5000 or that 6900, that's been equivalent to two and a half weeks worth of demand.

If we remember just back to the start of a previous exercise, there was one small step where we turned consumption off within demand planning.

That is so that we don't end up in a situation where we could double consume.

I think we previously discussed that forecast consumption is one of those activities which can happen at the end of demand planning.

So within the demand planning model or at the start of inventory planning.

So within the supply planning model.

To ensure that it doesn't happen twice, then inventory planning will receive a signal from demand planning as to whether or not forecast consumption has taken place there.

And if it has, then, so if this is set to something other than off, then we would not be able to apply forecast consumption on the supply side.

So that completes this exercise.

Where it's got us to is we have imported some of the main inventory data that we could use.

Not all of it.

And there were other transactional data sets, but the main bits, and we have, essentially got ourselves to a position where we can see that, inventory plan or that inventory calculation starting to kick in, and our inventory plan is now ready to use.

