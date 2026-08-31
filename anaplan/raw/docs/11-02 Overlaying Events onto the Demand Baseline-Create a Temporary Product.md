# Overlaying Events onto the Demand Baseline-Create a Temporary Product

So first of all, let's take a look at creating the product placeholder.

So within the data hub application there is a area down at the bottom here for managing temporary products.

And we also have a similar concept for temporary customers.

So again the ability to have place holders or dummy customers that we can plan against before they are commercially active.

In this case it's a temporary product that we were interested in.

So first thing I can do is create a staging area for that temporary product.

So I'm going to select where within the hierarchy I want it to sit.

I'm going to enter a display name for that product to give it a name.

And I'm going to flag it with being temporary.

Submitting that then applies that placeholder for me.

So I can now say I've got this staged, product.

A code is being generated for it so that we can then track it through the application.

The step which I now need to take here is just to be able to flag it as something which I want to be visible within demand planning.

So this is forecast subset is the product subset which drives a lot of our demand planning.

Once I've then done that I could commit to the update.

So that's essentially going to now take the product details that were just entered into that staging area and move that through to the product hierarchy itself.

The last step, which I'll just complete here, is then to be able to market as being available for planning against all of our customers.

So managing this valid combination which determines which products in which customers are permissible intersects for planning.

So that’s just done everything I need to do within the data hub.

I now need to progress that through to my demand planning application, and I will still, within the data hub application, run the process for updating my hierarchies.

So page 230DP.

I'm just going to run the update ALL Master hierarchy process, and that will ensure that the product moves through to demand planning.

Okay, so that’s now completed.

So the product should, in theory, be available within demand planning.

So let's just confirm if that's the case.

We’re moving over to the demand planning application.

I'll just pull up one of the main screens for the page 350.

And now within my product hierarchy, I just need to remove this product filter.

Within my product hierarchy, I can see that new temporary product that I just created, Orange juice with extra bits.

Now, of course, I could plan against this through a number of mechanisms.

I could just directly enter its plan, that's going to select it.

Directly, enter its plan as an override.

Or I can use something like the collaborative planning approach that we looked at in a previous exercise to build the plan up based upon a base level, growth rate and a seasonality profile.

