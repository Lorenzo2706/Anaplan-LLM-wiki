# Inventory reporting-alerting report

So the first one which I wanted to touch on is the concept of alerting.

within all the applications, there's a reasonably standardized alert and exception report.

If we see a screenshot here.

We'll look at it live in the application at the moment.

But it's one which is really, presenting a number of KPIs and allowing the planner to use those KPIs to focus which part of the plan they might want to drill down into.

There's then the corresponding configuration of that, which is really all about setting the thresholds for those KPIs.

So now what we want to count is good bad or neutral.

And also how we, essentially wait and use the combination of different KPIs to give us a final single prioritization metric for the planner.

Moving over to the application.

So looking at my inventory planning application, this is not the one that the previous exercises have been based upon, because that doesn't have sufficient data in it to make all of this work.

That's just a different copy of the application.

If I step into page 052 and let's just select all some more locations and products.

This shows us just what we have explained.

Let's look at our community scenario.

For each my product and customer combination, I've got some contextual metrics which show me the relative magnitude.

So in this case is how much inventory and additional receipts.

But the KPIs are really the ones that we see here.

So in this case, I'm looking at, how long until we stock out for this product in that location?

Where does the current inventory sit compared to the target?

So is it significantly above or below target?

And how old is that inventory?

What's aging profile of that?

the performance of all three of those metrics gets combined into this one single prioritization area.

So this is one which then allows the planner to focus, if they have a limited amount of time to focus on those product, location combinations where they wanted to drill down into a little more detail.

The idea would be that ultimately they can, take this one.

So we go to high priority.

There's a lot of inventory smartphones in New York DC.

Let's go and actually take a look at what's going on there and we'll start to get the representation, which is in this instance.

Another great one is just a place where we have too much inventory compared to the corresponding demand.

So what's involved with configuring that?

Let's step over to, our set of configuration pages.

And there’s the manage KPIs page 950.

There we go.

So the first thing we're going to do is, some simple definitions for the KPI unless new KPIs are being added.

Some of these things are probably not going to need to be touched as part of the project.

But something like this, weighting approach might need to be.

This is how we're combining multiple KPIs into one conclusion.

And we're doing that by placing some emphasis on, different KPIs.

So we may say this is a 30.

And therefore the performance of this particular KPI is much more likely to drive that overall prioritization score.

Alongside that, weighting approach.

The other main input is to determine the, the thresholds.

So what's the start and end point of that?

Good, bad, neutral, status reporting against the KPIs.

Clearly, this is a an important configuration as part of any implementation because, different businesses will have, a different perspective on, for instance, what is a good, bad or different timeline for stock out.

Particularly in this case, if, for instance, the model is being changed between weeks and monthly periods, then we may need to revisit this.

So that's how we configure the alerts and the, corresponding exceptions and prioritization report.

The next one which we just wanted to look at was inventory aging.

Again, we will look at the output page where we can see what the report is doing.

And we will look at a couple of places where we will configure that particular report.

So the report itself is page 522 as an example.

So what does this show me?

This is giving me, let’s select totals as a starting point.

This is showing me all of my inventory across the network and the inventory quantities are grouped into, different buckets based upon the age of that inventory.

So, if we remove this one.

Let’s start things off simply.

Let's go here.

So, here we can see within the California DC we have 60,000 units of inventory, which are greater than 61 days old.

So when measured against a essentially a birth date, then we can see that that is the age of this inventory.

On top of that we have a bit more inventory, which is 46 to 60 days old, and so on.

Most of our network inventory is sat within this 16 to 30 day age range.

So that's essentially the purpose of the report with the corresponding drill down to see exactly what products that is, etc., etc..

Again, the key area of configuration is two things really.

First of all is the definition of these buckets.

these analysis boundaries that we want to put in place, will need to vary based upon the particular organization that we're implementing for.

Where do we do that?

It's within the application configuration area.

And the page is if I can find it, manage age categories.

And then simply just in case of provide a name and input the upper and lower threshold for each of those groupings.

And again, clearly, the right age buckets will vary based upon the organization itself.

The other piece of configuration which is in our overall global parameter page, if we scroll down, is this estimated production date.

In order to identify the age of the inventory, clearly, we need to know a start point.

And this parameter determines how we define that start point.

So in this case it's production date.

this is operating on a basis where the inventory that we load in to the application, it includes the production date of each batch.

So each lot of inventory, we know its original production date.

And clearly based upon the model current date, we could accurately calculate how old that inventory is versus its original production date.

In some instances, that date might not be available.

So additional parameters allow us to define that report on a different basis.

So maybe we have the date that it was received into the distribution center.

So if we have the receipt date then at least we can measure the inventory age relative to that receipt date.

Or finally we may say well actually we want to approximate production date based upon the receipt date, less the lead time.

So then we broadly sort of having an approximation, a guess at the production date by offsetting.

We know when it's received that's offset by the that by the lead time.

So that's the inventory aging report.

A very closely related concept of reports which allow us to, report on remaining shelf life.

So again, we'll look at the reporting action and then drill into a couple of areas of configuration.

So the report itself, if we look at page 526 inventory shelf life, remaining shelf life.

Gives me a view which, let’s start off simply.

This is reporting on how many days to go, until this particular piece of inventory expires.

So again, we are grouping all of our inventory into different buckets.

So in this instance, we can see we have 60,000 units within California which will expire within the next 14 to 27 days.

So that's the point at which that inventory, reaches its shelf life and will be deemed to have expired.

On top of that, we've got some additional inventory which has longer to go, so up to 100 days until it expires.

And then most of our inventory actually has more than 100 days of remaining shelf life.

So more than 100 days until it's going to be deemed to have expired.

So in terms of the configuration of that, two main concepts very similar to the previous report.

So first of all, we need to define those shelf life buckets.

So remaining shelf life.

So in this case we've got 1 to 2 days, 3 to 4, 5 to 6, and so on.

Those the correct groupings will be just another example of where that clearly needs to be configured based upon the nature of the particular implementation or the organization that we're implementing for.

And again, it's just a case of end to the name input to the upper and lower boundaries for that, that grouping.

And that's sufficient to define it.

The other important parameter which we can actually see on the report itself.

It’s RSL 526.

It's probably this one here, which is the basis for remaining shelf life.

So this is saying actually what is the expiry date that we're really interested in at the moment.

This report is measuring our shelf life, remaining shelf life against true expiry.

The data which, based upon production and, core master data on inventory life, product life, we know the exact expiry date.

That can be useful.

Actually, an alternative might be, and more relevant might be the idea of stop sell.

Which is one where we recognize the fact that our customers will only take the product from us if it has a minimum remaining shelf life.

So in this instance, we're essentially offsetting the expiry date by that minimum remaining shelf life.

So our, customer who will mandate that, 28 days minimum, the shelf life needs to be on the product when we supply it to them.

For instance.

Either way, that brings us to a view where we can, can see all of this.

So again, if we focus here, let's just find out a little bit of what's going on.

So in the California DC, in that instance, we started to get, some product with a short shelf life.

So it's not long until this is going to expire where expiry is, essentially when we can no longer provide it to our customers based upon the stop sell point.

So the next concept, which is actually more of a, planning, modeling calculation rather than true reporting, is how we might also want to use that expiry information to impact our available inventory.

So if I just move over to, back to the application and let's try and focus on what we see here.

So we see a lot of inventory due to expire shortly for to 256 gig tablets in California.

So let's see if that gives us an interesting story.

A little bit, let's see if can find a slightly better one.

Actually, Okay, so I'm now looking at 128.

Let's just confirm that the report tells us we have something interesting happening here. 128.

We have 40,000 units due to expire within the next 5 to 6 days.

So, looking at this now, we can see there's our opening position at 40,000 units.

And, our demand comes through and we start to consume all of that inventory through that demand.

So actually, this is not recognizing that some of that inventory is going to expire before we get to use it.

The application essentially applies a first in, first out, type of method that we're always trying to consume the oldest inventory, to meet the demand.

But in this case, we're not recognizing that some of that inventory is actually about to expire.

there's not enough demand to consume it before it expires.

So the parameter which controls that we see down here.

So at the moment we can see we have auto expiry turned off.

So it's ignoring the expiry risk.

If we were to turn that back on then at the moment it's based upon true expiry.

We can say 17,000 units would expire in week 35 and they cease to be available inventory, which is possible to use to meet the demand.

Same parameter controls.

Just toggle between.

Is it actually the true expiry date or the stop sell date that we're more interested in.

If we think about it in terms of stop sell date, then actually it’s a greater amount of inventory which ceases to be available.

earlier in the time horizon.

Okay, so that's the end of the reports that we wanted to look at.

Just to round off the conversation here, again, the key point/takeaway from this exercise is that there is some configuration involved with making sure that the reports are best, tailored to the organization.

And also that in some instances, the available data will drive what the report can show.

Clearly, things like the aging report needs us to know at least the receipt date in the DC, or preferably the production data inventory.

And similarly, things like remaining shelf life, needs us to know the expiry date of that inventory.

So there's clear interplay dynamic between the data which can be brought into the application and the reporting capabilities, which then get unlocked.

