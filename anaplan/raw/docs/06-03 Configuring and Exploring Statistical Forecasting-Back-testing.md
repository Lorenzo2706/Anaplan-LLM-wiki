# Configuring and Exploring Statistical Forecasting-Back-testing

Just reverting back to the PowerPoint presentation.

So the next thing we want to look at and configure within the application is the approach for back-testing.

So this is the technique that we're going to apply to measure how past performing forecast would have been or how well they would have predicted the actuals.

And using that to drive an accuracy calculation.

And then ultimately using that accuracy to identify which of the 20 or so methods is the right one, the best fit for any given product and customer combination.

In terms of the calculation or the accuracy measurement that's going to be applied, like any forecast accuracy, it's going to have to operate on a lead time offset.

Essentially referring to, in order to predict actuals in a given period, which forecast, which previous forecast we want to use for that prediction.

And it also includes a period to some parameter, the ability to group together actuals, we may say, for instance, that we're not so concerned about how well the forecast predicts a single week.

We're more interested in its ability to predict a block of four weeks.

So in summary or a simple representation is, in an example such as this where we have actuals up through to September.

So that's yellow line that we see here.

I want to, with a lead time offset of four and a periods to sum of two, to measure a forecast which would have predicted August and September, which is that periods to sum lead time to offset steps me backwards to say, well, therefore it needs to be the April actuals.

So a forecast produced in April that I'm going to use to measure its ability to predict August and September.

That's it in essence.

So we will add together the August and September actuals, add together the August and September forecasted values, and then calculate the accuracy of the forecast versus those actuals.

The other third parameter, influencing the back-testing, is then how many tests we want to perform.

In this example, performing just one test, we're looking at a forecast produced in April and its ability to predict August and September.

We may want to perform that over multiple forecasts.

If I move on, this is when we can then see, where we have a parameter dictating the number of tests we want to perform.

So that is four, and we can see therefore we are going to look at a forecast produced in January and how that would have predicted May in June and a forecast produced in February, and how that would have predicted June and July, and so on.

And that's going to be the basis for measuring forecast accuracy and deriving the best fit.

So let's just take a look at that in action within the application.

If I step into my “Best Fit Analysis” page, page 360.

Okay.

So in this first instance I am measuring forecast accuracy based upon lead time offset of 4.

Here is the sum of 4.

So I got a weekly timescale, so I'm adding 4 weeks up into a 4 weekly block.

And I'm performing 4 tests.

That's the basis of the calculation.

The yellow area represents that testing window.

So if you see the period from which I'm going to derive forecast and assess their ability to predict the actuals.

So the parameters then will affect a number of things.

So if I increase for example my offset let's take that to ten.

That's essentially going to shift that yellow window backwards.

I'd have to take forecasts from, ten weeks in advance of the actuals in order to measure the accuracy.

So that lead time offset essentially determines, how close my forecasts are to the actuals in terms of the period that Number of tests then will ultimately drive the width of that window.

So if I ask for eight tests, then it's going to be eight separate forecasts, which I'm using to measure that, best fit calculation.

So the window widens, because I'm now asking for eight forecasts to be assessed rather than four forecasts.

So the key thing here really as part of the project configuration and implementation, is to ensure that these best fit settings, are most appropriately defined for the given customer that we're implementing Invariably, the rule of thumb is that they should match as best as possible, or be a simple proxy for some of the dynamics within the supply chain.

So, for instance, lead time offset.

Let's have that being close to the true lead time that the organization experiences.

At no point, measuring a statistical forecast and its ability to predict four weeks into the future, if actually the supply chain means that products needs to be sourced 12 weeks And in that instance, it's like a 12 week lag, which is most important to us.

Similarly appears to some may just represent some of the ordering dynamics.

So if the business is placing orders on a monthly basis on to a contract manufacturer.

Then really it's probably a block of four weeks, that's most important to be correctly predicting rather than performance of any individual week.

Number of test is more just down to how many tests we want to perform.

The more we perform, the more confident we can be in the fact that the selected method is the best fit, but it will have an impact on how much history is needed.

The more tests we perform, the more history we will need in order to be able to feed those tests.

So that is the essence of the best fit analysis.

Setting these parameters, those parameters determine the calculation of the root mean square error.

So this metric that we see here.

That gets ranked to identify the lowest error.

And that then gets identified as being the best fit method.

The important bit just to touch on here is that for all of this sort of traditional statistical forecasting techniques, we are able to dynamically calculate within the application, the past forecast, which are needed to be measured.

So as we change these parameters, then we can calculate what would a forecast be.

if we produce one in week 45, when it comes to applying the same testing methodology to, Plan IQ.

We actually need to have snapshot stored archived copies of the forecast from the appropriate point in time, which in this instance is what's driving the reason that they cannot be included in that test approach here, I clearly don't have any archives to be able to drive that assessment.

If this was something different, then maybe I might be able to do that.

