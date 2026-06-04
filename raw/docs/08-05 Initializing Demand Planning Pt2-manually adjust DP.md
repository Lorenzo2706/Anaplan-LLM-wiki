# Initializing Demand Planning Pt2-manually adjust DP

There's one last, task which we wanted to just talk about here, and that's looking at how we may configure the ability for our users to manually adjust the demand plan.

In particular, the key configuration concept here is the idea perpetuation.

And we'll look at that or we'll go into what that means.

Now when we look at the page within the application.

So in this instance let's just make our chart look a little bit simpler.

Let's just focus on the future early.

So now we can see we've got our baseline.

So that's coming through here.

That's our initial baseline.

Based on one of the start forecast of what was selected.

We then have the option to adjust or override that should we want to So we could override it.

So rather than it being 2,070 we can make it 2,500.

Or we could apply a percentage update on top of that.

So we could say put another 20% on top of that.

With both of these inputs we can see that they are perpetuating.

By which I mean that we input in a single week and then that adjustment continues on into the future and probably continue until we make another change.

So now we make it 2,200.

That's the same for both the volume based input and the percentage based uplift.

That is another thing which is controlled by a parameter.

So we can see this perpetuation behavior is set to yes.

If we don't want that to be the case, if we just want it to apply to the individual week in which we have input it, then that's what we can see here now.

So 2,500 input into week 19 only affects week 19.

And then we're back to the baseline 2,200 in week 26, affects that week, and that week only.

Throughout the application this concept of perpetuation is a key configuration parameter that we will see in various places.

Okay.

So that brings us to the end of this exercise.

Now the output really should be that the demand planning application is now ready to use.

And we should be in a position where we can explore various parts of its capability.

And we should look at what it takes to configure various parts of it’s capability.

