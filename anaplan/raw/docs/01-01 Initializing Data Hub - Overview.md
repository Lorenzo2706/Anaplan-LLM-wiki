# Initializing Data Hub - Overview

Exercise one.

Initial configuration of the data hub.

In this first exercise, we going to focus on the data hub and just get it up and running and ready to start to receive data.

We will bring some data in.

We will look at the hierarchies and we will look at some of the structural changes that we need to make, such as time settings.

We’ll also have a conversation and explore whether or not we need to completely clear out an existing data hub in advance of starting data, or whether we can just leave data in there and allow some of the processes themselves to deal with cleaning out redundant hierarchy of items.

By the end of this exercise, we should be in a position where we've got the data hub up and running and we've bought into it the product and customer hierarchies that are going to be needed as we go on into subsequent exercises.

So these are the tasks that we're going to step through.

First of all, we're going to focus on all we're going to run this mass deletion process.

And we'll look at whether or not that is necessary.

But that's what we'll do in this instance.

that will clear out everything all the hierarchy all the data.

And then we will look at setting up the call time setting that we don't need.

Time setting and time ranges are going to be done through the model.

Once they are done we can then start to look at importing product and customer hierarchies via the UX page.

Once the hierarchy they're in, we should be able to confirm that they you look at, we expect before we’ll just finish off with a couple of additional structural loads.

Firstly to import a list of currencies and then to import some product and customer properties associated with the hierarchy items.

As mentioned, the first task we will do is this mass deletion.

All of the applications include processes which will completely clear out all the hierarchies, lists and therefore associated data.

The result will be a model which is completely empty of all of those structural items.

We're going to do that in this instance, but it's not always necessary.

Virtually all of the import processes that we have to bring in things, such as a list of products, actually have parameters to control whether or not we would allow existing items to be deleted if they're not available within the source, but deleting out everything.

And in this instance it will delete out things such as a list of currency codes, transportation modes, units of measures.

It may be that we actually end up deleting more than it's strictly necessary, and for that reason, it's actually not always critical to run this mass deletion.

When it comes to importing the product hierarchy.

Purely just due to an encoding issue with the current data that's being provisioned for the training exercise, it may be necessary just to amend, an import process where we've got a mapping issue.

Second step here calls out, the task that's going to be needed as we do that.

When we're thinking about bringing in the hierarchy and when we load that in, we will look at a parameter which deals with the concept of hierarchy balancing.

This will cater for how the application should build a structure where not every item within that structure has the same number of parents, i.e.

it's what we would normally refer to as a value hierarchy.

So in the example that we see on the left is a simple representation of what a file might look like, where some of our products, which are what we see on the far left hand side, do not have the same number of parent levels.

In the subsequent columns.

The parameter we will look at, has two options.

One is to try and process the file exactly as is.

That will result in, process level products as we referring to them in this instance, appearing at different levels within the hierarchy.

So that's usually something which is undesirable.

Alternatively, we can get the import processes to automatically balance the hierarchy.

What it will do is insert additional items into those levels where the parents are missing, in order to ensure that the lowest level items.

So in this case, the individual products all appear down at the bottom of the hierarchy.

In configuring the hierarchy, imports, there are other parameters that we can explore.

One that we will just touch on here is the idea of parent code generation.

This caters for an instance where the codes are not available for the parent items.

It's mandatory that the least levels of the process, lowest level products in this instance, or customers or locations.

It is essential that they at that lowest level have codes, but there may be instances where the source systems do not give us codes at the level.

In that instance, we can ask the data hub to generate those codes so that we then have a mapping key which we can trace the hierarchy flow on downstream into subsequent models.

Another concept, which is prevalent in the importing of structures into the data hub, is the distinction between the transactional level and the process level, or what we often refer to as the leaf level.

This process, or leaf level, is essentially the lowest level of which planning is going to take place.

So in this instance, shown in purple, on my product hierarchy, it's that full count 750 mil bottle of orange juice smooth.

Now the ultimate customer hierarchy is this entity Tesco supermarket.

Now in many instances, the level of which planning is occurring will be slightly higher than the true lowest level of the transactional data.

So I may have a skew variant.

It could be a, a different language pack or just, you know, promotional packaging of the same product, that type of thing.

Or in the example that we see here with customers at the lowest level, it's actually the ship to entity that all my transactional data is recorded against.

When in reality I want to plan against my sold to entity.

One of the last steps in the this exercise will be to import some product terms and customer properties with the additional attributes and master data points that sit alongside the those hierarchical items.

The point just to call out here is that the files that import this information allow us to and have columns for a large number of potential fields that we may collect from a source ERP.

Typically, though, very few of these are actually commonly used by the applications.

So in this slide we just list out what might arguably be probably the most important ones that we may be looking to capture in those property files.

