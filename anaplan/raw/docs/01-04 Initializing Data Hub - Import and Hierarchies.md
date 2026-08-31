# Initializing Data Hub - Import and Hierarchies

So we've got our deletion.

We've set our time settings.

We’ve dealt with our time ranges.

Now we're just going to start the import of these hierarchies.

So in the first instance this can be a place where we are now interacting with the UX application rather than the underlying model.

So here's my data hub application.

Just to give you a little bit of orientation in terms of how this is structured.

Up at the top of the set of pages which are associated with bringing data and hierarchies into the application.

there are a whole set of sections which are really focused on and enable us to then pass that data into the downstream models of demand planning, production planning, whatever it might be.

Then there are a set of pages which just allow me to review what sat in the data hub.

To apply some validations and then some other particular activities, such as creating and mastering dummy products.

So place holder products for new product planning.

And down at the bottom of every application will be the configuration area.

So the set of pages that allow me to change some of the parameters which are controlling the behavior of the application.

So for this first exercise, the place I want to be is in this Update Master Hierarchy page.

we've got four main hierarchies which this page is allowing me to import locations, customers, suppliers and products.

The one that I'm concerned with in this instance are just the customers and the products there.

What I need for my demand plan, which is the thing we're really trying to focus on right now.

With both of those, importing the hierarchy is actually two steps.

There's a step which will bring that hierarchy or that the contents of the source into a staging area, so that potentially I can review it and look at it before I then allow the actual hierarchy to be built.

And then, the process which will take the contents of that staging area and build the hierarchy itself.

That's consistent across all of these.

But to make a start on this I'm going to focus on my customer hierarchy.

I'm going to run that first process.

Select the file.

Now you should have access to a folder of data templates.

All CSVs populated with all the information we need for this exercise.

In the very first of those subfolders, labeled exercise one, that's where we can find our customer hierarchy CSV I'm going to select that.

And just run that process.

Okay.

So imported that into a staging area.

And actually, if we look at what we've got just down here at the bottom, I'm already being alerted to the fact that I’ve got a problem, with the contents of that file.

It's informing me that there's some missing information in this instance, it's the customer names that are missing.

So fortunately, in this instance, I know what that problem is.

It's the issue that we just mentioned on the slides related to, an import mapping, issue in the, copy, the training data that we have here.

Just revert back to the PowerPoint just so that we can be super clear on that, so that we can help you fix it, should you have the same problem.

The action I need to edit here is P020 002, import customer hierarchy.

There it is okay.

Let's edit that.

So the issue that we've just had here with just this mapping on the level one name.

If I reselect that, you can see I've got some strange characters coming through in my import CSV I just need to select that.

I’m sure it's an import file importing issue.

And just okay, that.

Right, let's see if we have a bit more success this time.

So back to the UX application.

I'm going to import that hierarchy file.

Select it.

And run that process.

You can now see that validation has been cleared out.

So I'm good to go on to the second step of this two stage process.

And that's the one where we will build the hierarchy itself using this process here update customer hierarchy.

And there it is.

Brilliant. so at that point we should have a hierarchy in the application.

How can I tell that?

Well, it would be the normal set of options for reviewing the hierarchy and a couple that we may want to use.

So for instance, we should have the ability to, have a page where we can see hierarchies, the master hierarchies page, 310 customer.

And now if I just start to expand this out, I can see the hierarchy that we've just imported.

Great.

Obviously, you know, the other quick way to validate it, to look at the hierarchy would be to just go to the underlying list itself.

So in the general lists, at the bottom level it's the one labeled leaf.

Open that up.

And now we can see the hierarchy just imported.

Brilliant.

So that's refreshed our list of customers.

Now let's go and do the same for products.

So it's the same UX page.

So data import update master hierarchies.

The section is over here on the right hand side.

I'm just going to import that.

Select the file.

Open.

And run the process.

Same import validation error I knew it was going to come.

Okay, now I need to go to my, data hub model itself.

Before I do that, I will just go over to the PowerPoint just so we can be clear.

On the process that we want to update or the action There it is.

It's the import product hierarchy action P010 002 Then into my actions.

P0010 002.

Import product hierarchy.

And I'm just going to edit that.

Same exact same issue to my level one name.

The mapping has been lost.

I'm just going to remap that.

Set okay.

Now we're good.

So let's just try that again.

Import product hierarchy.

Select multiple data hierarchy CSV.

Open and run the process.

Great.

My validations cleared out.

I'm looking in a lot better place.

So now I can proceed to the next step.

Again, the step where I now go ahead and build the hierarchy itself.

Having just imported into a staging area.

And that's done.

Same options to review that.

I can look at page within the UX application itself.

Or I could just go the quick way and look at the list within the model to see if this appears how I would expect it to and it does indeed.

There's my hierarchy of juices And then a small business of smoothies.

