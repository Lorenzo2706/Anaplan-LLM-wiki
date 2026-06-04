# Managing inventory policies-Create a test inventory policy

So first of all, let's head over to Anaplan.

Back within my inventory planning application and down within my main configuration area is the page where I can manage my inventory policies.

So here are the list of policies which are already in my copy of the application.

What does a policy do?

It's ultimately trying to achieve or define two concepts.

Firstly, a reorder point strategy.

So what is the basis for when and how we trigger the reorder of new inventory.

So placing inventory purchase orders for instance.

And then secondly the target level strategy.

So what is the target level of inventory that we want to hold in the distribution center.

So those two things then control the replenishment calculation of when do we replenish and to what level do we replenish.

So to create a new policy, we will just step through a set of inputs.

So first of all let's create a policy and give it a name. So I will have a policy here which is called “Every 4 periods: 8 periods supply”.

So it's just the free text name I have chosen to give this.

I then choose my reorder point strategy.

So different ways of defining that trigger.

So the point at which we trigger an order and in this instance I'll say is periodic review.

So we're saying that's essentially the inventory planners have a routine cadence of when they review inventory and place orders.

And in this instance, I'm going to say it's on a full weekly cycle.

So that's the basis for triggering when we order.

Next is going to be the basis for how we set the target level that we order up to.

So in this instance I'm going to say it's calculated.

So we're going to calculate that target.

I'm going to calculate it based upon a periods of supply.

And that's going to be eight.

So what this is saying is essentially my target inventory level is always going to be sufficient to represent eight forward periods of supply.

That the inventory should be out to cover eight periods of future demand.

So having defined that policy that if we now just move over to the main inventory planning page, page 240.

We can start to see that policy come into effect if we select it.

So here we're just selecting it for the specific DC and product combination.

So I will select, I'll override my default.

And I'll select that new policy that we see here.

And we can see the impact of that coming through.

So we still got these open supply purchase orders.

So this incoming inventory that's what's being transacted within the ERP.

It's only once we get to this point in the future, do we then start to see new simulated receipts.

The frequency of those receipts, should be in line with the full week, The reorder point that we defined and the level of inventory that those receipts are managing us to should represent eight weeks of demand.

So that's essentially that policy kicking into action and controlling the behavior of those receipts.

We see that.

So if we just step back to the policies themselves, let's go back to the page where we manage those, that we won't, as part of this exercise, explore all the different alternatives for specifying those things that documented in the process reference guide.

Just worth calling out, in particular, on the target level, there are a range of different ways of articulating that target.

It could be a fixed target.

So for a given product location combination, I will input my target level of inventory as being a defined quantity.

More likely it will be calculated.

And if it's calculated, there's then a range of different ways of calculating that.

We've just done periods of supply to set the target to be sufficient to cover an number of future periods of demand, or we could move through to a more of a service level approach, where we then set a target, which is going to be aligned to some sort of service level.

So let's say that we want to hit a 99% service level.

like anything, you know, like any service level that is there to protect us from some uncertainty.

So what is the uncertainty that we want to protect against?

Is it the variability in the future demand?

Is it the, quality of the forecast itself?

And then also we can include whether or not to, represent lead time variability as another uncertainty within the equation.

So the fact that that we have a default known lead time, but in reality we can get variability a standard deviation about that.

So that's how we set up the policies clearly as part of a project and the configuration.

The key thing is that first of all, the an appropriate catalog and appropriate set of policies are defined during the project, and made available for use.

And then also that the sort of administrators, the super users within the customer are trained so that they are then able to manage these and add and remove these on into the future as the business changes and needs different service level options.

For instance.

All we've done there is this very first step where we just created an inventory policy and explored a little bit how that policy is going to impact on the calculations.

