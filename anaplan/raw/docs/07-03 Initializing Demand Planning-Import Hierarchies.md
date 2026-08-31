# Initializing Demand Planning-Import Hierarchies

So the next set of tasks which I want to talk us through, at one point I want us to step through, are the concept of, all associated with managing the hierarchy.

So we'll set the hierarchy reconciliation parameter to update and insert.

We will then run the product and customer hierarchy imports, and we will just use either the underlying model or page selected in the application to confirm that the hierarchies have come across okay.

But before we just look at these within the application, let's just touch on the concept of hierarchy reconciliation.

There's a parameter within the application which deals with how we keep hierarchies in sync between the data hub and the downstream model.

Taking the example a position where our demand planning model starts off with its hierarchy looking like this.

We have then updated the data up.

We've pulled a new hierarchy income source system into the data hub, and some things have changed.

Product 1.3 is no longer in that source list.

Product 2.2 has been added.

Product 1.1 has been renamed.

The hierarchy reconciliation parameter really does deals with one particular situation here, and that's what we want to do about the disappearance of product. 1.3.

In all instances we will update.

So changes to names such as what we see here with 1.1 will happen.

And in all instances, we will add new products and we will insert new.

The only difference between the options we have is to what to do about the deletion.

We could specify, or we can select the parameter to update, insert and delete, in which case my downstream demand planning model will remove Product 1.3.

And we'll look exactly like the resource hierarchy within the data hub.

Or we could just set the parameter to update and insert, in which case point at 1.3 would be retained within demand planning.

In the majority of implementations, update, insert and delete is typically the way in which we select that parameter.

We’re relying on the source system to be and the update from the source system to be a full refresh of the product hierarchy.

In some instances, that may not be the case, and it may be appropriate to use the update and insert only option.

So let's just do the various bits we want to do for our hierarchy.

So going back to Anaplan, refreshing the hierarchies in the data within the demand planning model is something which is determined or is run by processes that sit within our data hub, just as it was when we updated demand analysis and the stat forecast.

So going to the update data page, this is where we have all the processes that are going to bring in to demand planning data from other models.

So in the first instance it's the hierarchies I'm interested in.

There we can see the update, insert, and delete parameter has been set.

That hasn't been set, we can change it within the global parameters page.

I can run the individual product and customer hierarchy imports separately.

Or I can have one process which will do the two and actually also locations, although we don't have locations yet.

And that's what I will do.

I will update all my hierarchies.

Right.

That appears to have completed.

Let's just check the hierarchies have indeed come over.

And in this instance, I'll do that through the underlying model just by looking at the lists.

So, with any luck, one look at my product linked list, I should see my juices and my smoothies.

And I don't see any of the demo products which were previously in the model.

Similarly, hopefully, if I look at my customer leaf, and I should see my retail and other channel customers that we have within the data hub.

