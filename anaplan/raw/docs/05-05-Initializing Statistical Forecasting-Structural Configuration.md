# Initializing Statistical Forecasting-Structural Configuration

Okay.

So reverting back to the PowerPoint.

Let's just check where we're at.

So we've done the stuff we wanted to do which in the model we've now imported our product and customer hierarchy.

We've got our data in.

And we've used a page or two, to confirm that things are working.

final step that actually is an interesting one.

the tasks that we're now going to embark upon is, one which requires us to make some formula logic change within the underlying model.

There's not many of when it comes to configuring the applications.

Virtually everything we do, we try to control behavior calculation logic through parameters.

But there may be 1 or 2 times when some modeling updates are needed.

So that's why this task is introduced as part of this exercise.

Just to give an example of what that might look like and what the set of instructions, and to support that task may be available to you.

If you don't complete this task as part of the exercise, that doesn't actually matter.

It's not going to prevent us from carrying on with some of the downstream activities.

But what's the context here?

So let me just revert to the application and I'll provide the context.

The statistical forecast is calculating independently calculating a forecast at all levels of the hierarchy.

so when I'm looking at my orange juice grocery forecast, that is the sum of the parts.

That is what is being calculated at that type of level.

And often, you know, forecasting my slightly higher level may be, better quality forecast, but with something at a lower level, if we want to use that forecast, if we want to control the use and the disaggregation of that higher level forecast, that's the task which we now going to set up is the choice over what level we want to target.

So if I revert to the PowerPoint presentation and keep this to hand, just step through to here.

There's some simple instructions on the slide.

Also, these instructions are going to say whenever there's modeling changes to be made, the notes and the instructions will be in the configuration documentation.

First thing I'm going to need to do is just to change, the, the format of a couple of line items in one particular module as the T400.

So I'm going to move over to my model, and I'm going to go find that module file called FCT400.

There it is.

Open up the module.

And there's two line items which are level to disaggregate from, customer and product.

There they are.

So I want to set these to be whatever level I want to derive that aggregate level forecast from.

So in this case maybe let's say I want to take it from level three product.

And level three customer to just one level up within the hierarchy.

Okay.

The next thing I want to do against these line items is to insert the formula, which will allow me to derive that parent item based upon the leaf level child.

I'm just going to edit my formula here and I’m going to enter parent item.

And this is what it is called is the name of the product hierarchy.

hlp080 product leaf apply.

And I'll do the same with the customer level.

Parent item and customer leaf hierarchy that we see here.

There we go.

The next thing I want to do is just to clear out some formulae, which will need to be reworked in a moment, but in the meantime I just need to delete the formulae.

And it's for these three level, line items that we see here.

So the quick and easy thing that I want to do is just to store these for later use, so I'm just going to pop them into my notes field over here.

So this taking that formula and saving it for later.

So that's this one. This one.

Finally this one.

Okay.

So if I just revert back to our notes just so we can check where I'm at.

Alright, so I cleared out this formulae.

The next thing I want to do is just set the applies to for two of the modules at FTC200 and FCT202.

So these now need to be set to the aggregate level that I'm targeting.

So the way I've just defined it is a product level three customer level three.

So that's what we'll do.

Then we will head off I'm going to find those two modules FCT200.

And we will give it the level settings that we want.

Product three.

Customer three is how I define this.

Do that in as well.

Okay.

Returning back to this FCT400 module.

Now this is the place where I can really introduce those formulae.

So I'm just going to get the formula which I have entered into my notes field and pop it back in there.

But as I introduce it I need to include, lookups for those parents that we have so my disaggregation parent.

I get my syntax right.

Correct that there and lookup customer.

And close it out.

Let's hope we've got it right.

That we do.

I'll do the same here.

So I've actually just stored those lookups by copying them.

So I've got my full formula there.

And let's just put it back into here.

Okay.

Just copy that.

I don't have to.

But just makes it things little bit easier for me.

And enter it in here.

Okay.

So that in theory is the set of model changes which need to be made in order to enable to configure this piece of functionality.

Let's check in a moment to see if that worked.

But the two important takeaways here there's very few places where we need to make modeling changes and if we have to then they are documented in the configuration guide.

That's the number one takeaway.

But number two actually is if you don't manage to successfully complete this bit of the exercise, don't worry.

It's not going to impact upon our ability to do later stages.

Let's go see if that is indeed working.

So the page that I'm going to look at now is this edit final forecast.

Let's go find an individual product and customer.

So as I look at this individual product customer.

I can see orange juice smooth in Tesco's.

The the best fit method.

We'll talk about best for later on.

But it's selected the linear regression following.

That's fine.

If I wanted to though, I could choose to use the disaggregated forecast.

I'm just going to enable that.

And now we can see that actually my final forecast is something different.

There is a parameter to control, whether we want to automatically use the disaggregated forecast.

And in particular the way that works, we will go and look at it over here.

Shall we?

Global parameters page and we'll just scroll down.

Scroll down to where we go.

Where We have this option to choose the aggregate level forecast.

If the variability of the leaf level, so the lowest level product, then customer demand is too high because that then triggers a signal to us that maybe we're too granular.

We're not going to get a great forecast at that lowest level.

So we're better off taking a forecast from a higher level and pushing it that down.

So that concludes that piece of the configuration.

But just revert back to the PowerPoint.

There's probably one other note just to focus on here.

And that's this first comment which is made on this slide here.

As you move around some of the models and you look at things like pages within the data hub, you may see reference in some places to what we refer to as stat combination model.

What that essentially deals with is the fact that we have two different versions of this statistical forecasting application.

We have one where customer and product, are retained at independent dimensions.

That's probably the easiest one for users to interact with.

We've got our natural hierarchies.

But the instances where we have large hierarchies or particularly stat data sets.

We have a combination model where the product and customer dimensions are merged into one single list, just for those that are combinations.

So if you see reference to that, then that's what should go into is that alternative model which can be deployed in those instances where you got large sparse data sets.

They're just reverting back to what we wanted to get out of this exercise.

We have set up our stack forecasting model.

We have pulled the data into it that we need in the hierarchies.

We have, looked at 1 or 2 pages to confirm that it's working as expected.

And we explored a little bit this idea of configuration, which needs modeling changes.

The outcome of this task meeting.

is we have a stat forecast so that we now move into downstream demand planning.

We have a baseline forecast that we can exploit.

