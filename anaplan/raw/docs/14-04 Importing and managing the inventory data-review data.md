# Importing and managing the inventory data-review data

So let's move over to the inventory planning application and see if we can review the data within that application.

So first of all I'm going to look at the the inventory.

So on page 204 manage available inventory.

This is where I can get a simple summarized view of the inventory, which the application now knows about.

The important element of configuration here is one to think about.

Which or how much of the inventory we want to reflect within the inventory planning application.

So essentially of all of the inventory, are we going to regard that as available inventory that can be used to meet demand or their some elements of that inventory which is not available for various reasons.

We can manage that through status codes.

if the inventory data that has been imported into the data hub has some status codes against it, then we can use those to exclude particular groupings of inventory.

For instance, I could say let's exclude the inventory that is tagged as damaged.

It's not reasonable to think of that as being available.

inventory to meet customer demand.

So that's the key configuration element here is to just decide, which of these status codes get represented within the inventory calculation.

If I then move over to my open purchase orders.

So this is my supply of purchase orders in page 202.

Again as we look at this, we can see all the data that's come over from the data hub.

So that is a purchase order header.

We can see the PO date, the location it's due to arrive at, and the number of lines against that PO.

And then drilling down into it.

We can see the individual products.

So the individual lines as part of that PO.

I'm just going to select scenario one up at the top here.

Rather than my committed scenario.

And that so that we can explore some of the other parameters that are used to control the PO data.

Probably the main one is this decision as to, again, how much of that PO data do we want to show within our inventory calculation?

We could set this to no.

Which essentially means let's run a simulation.

Let's run a scenario where we completely exclude all of our open purchase orders.

So a scenario where we don't have to honor the POs which we placed on the supply.

More likely you would say yes to all.

There may also be one where we say yes, we want to include a PO data, but only those where the expected receipt date.

What we see down here is in the future.

So here we can see, we've got some product which was due to be received, in the week of the 18th of April.

That is before the current period.

So this is late.

So based upon this selection, that's going to be excluded.

Or I could say let's include it.

And at that point, the application will make a decision on to show it is arriving within the first forecasted period.

So the current period.

So having done that, we can now potentially see if we have an inventory plan emerging.

We've got our demand.

We've got our on-hand inventory.

And we have some open supply purchase orders arriving within the DC.

So going down to page 240 DC inventory planning.

We should be able to see that type of picture emerging.

And that's what we get here.

And let's just tidy this up.

Let's show the view here.

So and pick an individual location.

There's my central DC.

So I can see that's the demand that the DC needs to meet.

If I include the incoming, then these two spikes here , relate to open supply purchase orders.

I can see that down within the table.

So, there they are.

So, I've got some, transacted supply purchase orders due to arrive.

Out in the future, this is now the application calculating new receipts.

And we'll explore how it does that calculation later on in another exercise.

And then ultimately we can see the inventory balance.

The on-hand opening position.

And then as it depletes, gets consumed by demand, spikes up due to new arrivals, and then continues to be consumed.

So that's the important place to complete this exercise is to view something along these lines where we can see demand, on-hand inventory, and open purchase orders; all coming together to give us an initial inventory projection, inventory calculation.

