# Configuring a Network

Exercise 16.

Configuring a network In this exercise, we will now look at how we can set up the distribution center network that we have here.

We have a multi-tiered network where one location can actually provide inventory to other locations.

So we need to see how we can set up those relationships and how we can use them for modeling the additional demand that some distribution centers will see in order to fulfill their responsibility of replenishing other locations.

We will also briefly talk about a related concept of ad hoc network transfers, which is more of a sort of, you know, an occasional rebalancing approach rather than a routine flow of of goods through the network.

So what is it we're trying to achieve here?

So, so far, we have essentially set up an inventory plan to look like this.

We've taken our customer demand.

We put it through that DC disaggregation process, and that identified the demand that each of our three DCs needs to serve in order to directly service their customers.

That triggered a replenishment requirement.

So a need to source additional inventory into those DCs.

But at that point, we haven't then done anything to identify what the supply of that additional inventory would, would come from or where it would come from.

What we want to move through to is something like this, where we know that as part of this network, there is a relationship whereby once the North and South DCs have a replenishment requirement, once we need to get additional inventory into those DCs, that actually comes from our central DC.

So as part of this, the central DC will then ultimately see two sources of demand.

It's still directly servicing some customers.

And it's also replenishing the north and south.

And then ultimately it is the central DC replenishment, which is the the signal to production in order to get new inventory into the overall network.

So how are we going to do that?

So the steps that we will walk through is to, first of all create some transfer lanes.

So the these relationships between the different DC used to be able to move product between them.

Once we have set those lanes up, we will input some data points which will allow us to use that as the flow.

So that sort of routine logic of center always replenishes north and south.

We will set that up and we will put some corresponding lead times to represent the offset that we get to see.

Once we've done that, we should be able to confirm that we have inventory flows moving through those transfer lanes and then ultimately see the resulting impact on the inventory plan.

We should be an impact whereby the central DC is now receiving or seeing additional demand back to the application.

The first place we're going to go to is page 904.

This is the page where we need to create some empty list placeholders.

So as we explored in an earlier exercise, a number of places within the applications where we want to use this to capture planning inputs against list items.

Wrong page we have a process where we will pre create those empty placeholders for them.

So they don't need to add new items to a list, but they can just populate existing ones.

So if I scroll down here I think where I do that here is in this section here.

So I want to create some new placeholders for transfer lanes.

So we'll run the process, create location related lists and allow that to capture those placeholders.

We want.

That's completed.

So where do we go next.

So now that we've created a placeholder that we want to start to populate them.

So there is a page within the application 910 where I can manage my transfer lanes.

Let's move over to that page 910.

And then quite simply all I need to do is select the “From DC”.

So each lane is a child of the DC that it is putting inventory into.

So I just need to select the the source for that inventory.

So in this case is my central DC.

So now we can see we have a transfer lane which allows us to move product from the center to the north and the center to the south.

The next step is to input this routine desegregation.

So on a sort of routine business as usual basis, how much of the replenishment requirement of the northern DC is met through this lane?

So in this case, it's everything all the product that we want to get into.

The northern DC comes out of the center.

And then similarly, all the product that we want into the southern comes out of the center.

So I've defined the lane.

I've specified this routine logic.

The final bit which I just want to do on this page is then just select the normal transit mode.

So I'm just select road.

Which will ultimately govern the lead time in this instance.

It's not showing a lead time.

So we'll just update that through page 912.

Edit ead times. In that instance.

Then it's just a case of let's let's input a lead time. So a conservative planning assumption that it takes one period.

So one week to get product through this transfer lane out of the center and into the north and south.

So having set up those bits and pieces, we should now start to see the impact of that. So let's move over to the inventory transfers page 222.

Routine network replenishment.

Nothing quite showing through.

First let me just create make a selection or two and actually I think sometimes this page doesn't show the scenario that we have selected.

So let's just make sure we are on the correct scenario.

Force ourselves to be looking at scenario one, and then we'll head back down to that page or up to that page.

And let's make sure we select all DCs.

So there we go.

This is what we're now seeing.

So we take this transfer lane sent it to the north.

So this is how much product is flowing through that lane on a weekly basis.

The volumes represent the point to which they are received into the the destination location.

But we could also see that is when they get shipped out of the source, which is essentially just offsetting us by the lead time.

And there’s the same for the additional lane of the center to the south.

So how do we then represent that within the main inventory planning calculation.

Let's have a look at that in page 240.

So now if I start off by looking at the central DC and I will - well let's leave on tier one at the moment.

So what do we see here for the central DC.

We can see essentially committed demand.

That's the open sales orders. Forecasted demand.

And the two of those are the total demand that we're currently planning around for the central DC.

If I were to move this selector up at the top here to tier one and two, that's when we would also layer in the additional demand coming from its need to replenish those other two DCs.

And that's what we now see coming through here on this simulated network replenishment lane.

So as additional demand witnessed by the central DC in its role of serving the other two DCs, as a result it's own replenishment calculation.

So the simulated requirements that we see here and then we're going to reflect the total demand both serving customers and serving the other DCs.

If we were to look at those other DCs, it’s a slightly simpler story.

Now if we look at our northern DC we can see it's simulated requirement.

This is the additional inventory that it wants.

Looking at this based upon tier one that it comes through in this simulated requirement, which is essentially a an inventory requirement still to be sourced open ended as to where we're going to get that from.

If we move this over to tier 1 or 2, then we see that requirement coming up here into the top where we now recognize or we acknowledge it as being inventory, which is received through the network.

So that's the the essence of the calculation, the behavior and the configuration.

I think, a couple of points to make there.

Firstly, invariably actually, you know, once this logic is set up, then the planner only need to worry about looking at the the last tier in the selection, because that's the one which gives them the full picture of demand for the DC.

There is a little merit in reviewing the inventory when we're only looking at a partial picture for a particular DC.

So we would always say, let's select the last one.

This approach is also extensible to more tiers.

So we can see we've got tier one. And two is our final step here.

If we had a more complicated network with further tiers within that network, then the configuration of that is through versions actually.

So if we open up the underlying model, we can see it's actually the use of versions which is how we achieve this theory.

So to have another loop back around an additional tier we would add another version. Okay.

Now for the old recalculate the model, but we'll add another version.

The last one in the left market is the current version.

And that would allow us to define this broader network that we would see that.

Okay.

So that brings us to the end of that exercise.

As I say, that the, this point where we should be able to get to in order to confirm the successful calculation would be one whereby if we're looking at the central DC, we should see that additional simulated network replenishment when looking at tier one and two.

And if we're looking at the north and south, we would see their replenishment requirement coming through in this plan to receive from network replenishment lane that would essentially identify we've successfully configured the network in that instance.

