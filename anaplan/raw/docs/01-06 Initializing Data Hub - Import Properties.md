# Initializing Data Hub - Import Properties

One final activity that we need to look at here.

So this is the importing of the custom properties and the product properties.

So they're back in the same place as where we imported the hierarchy themselves.

Page 106.

And they are the third step of the customer and product hierarchy and item management set of processes.

I'm just going to take the first of the and bring in my customer properties.

There’s the file.

Customer Properties.

Normal steps to open up the file to run the process.

And this is probably what you should get.

This is just another example of that unfortunate, error on the import action mapping due to the fine encoding.

That's why we've had this complete failure.

I'll just triggered the same thing for the product so that we can then fix them together.

Once we're in the underlying model.

So I'll just try my products that set that process, import and update product properties.

Go and select the file.

Open it up.

Run the process and probably get, Ah!

Okay.

So this is okay for me.

Hopefully it'll be okay for you as well.

Well, I was good.

So now let's just.

Well, let's get back to PowerPoint.

So to fix this is where we need to look at that process P022 001 for customers.

And if you've had a problem with the products it’s P012 001 let me just go back and dive into the model.

And find the action to P022 001.

I should now be able to edit that having tried to import the file.

That should allow me to now proceed.

And again, we can see it’s just that funny unfortunate mapping issue that we've got here.

So I just need to map that first column, column one, onto my list of customers.

And then I’m okay.

So finally, just to deal with that, let's go back into the import step through the processes of go and find the customer property file.

Open up that property file and run the process.

And hopefully we won't get many red triangles that we get.

Excellent.

So that's essentially everything completed with this first exercise.

When I walked through the PowerPoint, I did call out a couple of parameters which may be relevant.

One of them was this concept of hierarchy balancing.

And you can see that in play up at the top here.

So you can see where we've got this ability to control how we deal with the situation when we're presenting a ragged hierarchy to the data hub.

Do we want to take the As-is approach where the individual items appear at different levels?

Or do we want the data hub, to automatically balance it?

And we've got the automatic balance option, the sort of global default for that parameter and many other parameters is set down within this application configuration area.

Page 900.

So I'm going to scroll through here to kind of find those bits.

we talked also I think a little bit about whether or not we want the application to create and generate codes at the aggregate levels if the source system is not giving them to us.

So that's another example of where those come to sit there.

And here's our hierarchy balancing.

Here's where we can set the global default for that option.

Okay.

Just finally reverting back to the slides just to finalize where we're at.

We're now in a situation where we've initialized our data hub.

We have cleaned it out of all of the existing demo data that may have been provisioned within that data hub.

We have loaded in, product and customer hierarchies and associated properties, and we have set the time settings for the data hub, to reflect what we want it to be.

So at that point, we've completed this first exercise.

Look forward to the next one.

