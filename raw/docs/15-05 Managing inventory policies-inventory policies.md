# Managing inventory policies-inventory policies

So, having done that, you know as part of the exercise, of course we can.

And I would suggest it's a good idea to start to, set up some additional inventory policies and, specify them in different ways for the reorder point strategy and the reorder quantity and just explore how those different policies work.

The bit which isn't represented on this slide, is we'll also use this exercise to quickly explore some of the other key parameters in operation here.

So what are they?

So as things currently stand, the policy is determining exactly this replenishment requirement that we see out in the future.

There are likely to be let's see if we can get something slightly different this year.

It's got a shorter term replenishment.

There are other factors in play when it comes to the replenishment that we see here.

First of all, will be the related concepts of minimum order quantity and order multiple.

We can see here that, currently, the calculation identifies the exact value of inventory it wants to bring in, in order to perfectly meet the inventory target.

Reality that ordering 2655 might not be possible.

We could well be constrained by some form of minimum order quantity.

So let's say we got an MOQ of 5000.

So applying that MOQ we can immediately see everything now gets adjusted to honor that MOQ.

And actually in this instance, it also means that sometimes when we replenish, we have significantly more inventory than the target requires us to have.

And therefore we can actually miss a replenishment cycle because we've got enough that MOQ is driven us to have enough inventory to last us through to four weeks later, rather than the two weeks that we would have expected.

As I say, related to the MOQ would be the corresponding concept of an order multiple.

So quite simply, in here we can see why we've got a MOQ of a thousand.

Once we're above that thousand, we're currently running at whatever the precise number needs to be.

But maybe we've got an order multiple to be ordering in 5000.

And again, that will influence that replenishment calculation that we see here.

So they’re two of the important factors or parameters within this calculation.

Another related one or another similar one is probably the concept of frozen horizon, which essentially it's a little bit like lead time, but it's more what does the business planning process allow us to do in terms of how much of the future is locked?

So in this instance, if we had a frozen horizon of, let's say 12, then we can see that the next 12 weeks are frozen.

As you know, we've committed that.

We've communicated that to production or suppliers when in whatever it might be.

There's no opportunity to change that plan within that horizon.

And then only after those 12 weeks can we start to see some new replenishment coming through here.

In this instance, you'll see that what's just happened through that frozen horizon is that it put me into a position where the DC is now stocking out.

So we can see we've got this shortfall coming through.

We do not have any inventory in order to be able to meet the customer demand in those weeks.

And in this case, that shortfall building up.

So it's accumulating as a backlog.

And actually when I can finally bring in some new inventory, I can use that to clear the backlog.

So I've essentially got a back order strategy in place, which allows me to meet my customer demand later than they ideally wanted it, because they will accept better orders.

That, again, is controlled by a parameter.

So there's a back order strategy here.

And in this instance it's set to back order.

So I'm allowed to build up that backlog and fulfill it later on.

But that could be set to a “Fill or Kill”, which essentially means that, if I do not have the inventory to meet the customer demand in the week in which they want it, then that is lost demand.

I cannot subsequently ship product to them later.

So you can now say, I've still got my shortfall, still recognizing that.

I'm not building up a backlog.

And actually, the replenishment that I see coming in here is lower, because all that replenishment needs to do is to bring me in line with my inventory policy.

It cannot bring in more product to clear the backlog, because that's not an opportunity we have here.

So they’re probably some of the main parameters in place for controlling that calculation.

So it's the policies, MOQs, order multiples, frozen horizons, and the few others which may be explored at some other time.

But they’re predominantly the main ones.

Just to finish this exercise off.

You'll notice that, everything is being controlled against, a number of scenarios.

So it's possibly important to look at how we define some of those scenarios.

So let's just review the configuration of those.

So this is where I can manage the inventory planning scenarios, providing it a name, and through a set of controls determining the behavior of those scenarios.

So for instance this one titled committed has this Boolean ticked to mark it as a committed plan.

And what that means is it will prevent it from calculating any or simulating any future replenishment requirements.

It is a scenario which we’ll purely look at, what can my current on hand inventory and committed transactional additions, get me to.

And then there's other parameters which deal with things such as how we interface with a constrained production plan, and also allow us to run quick scenarios, for instance, where we may have MOQs in place, but we quickly wanted to, override those MOQs and look at what my time inventory do if we weren't constrained to meet an MOQ.

So, what inefficiency or what additional inventory are we holding purely due to the impact of an MOQ--a minimum order quantity.

That brings us to the end of this exercise.

So we've created a policy.

We've looked at how we can use ABC XYZ to apply those policies.

And then we just had a quick tour of some of those additional parameters.

As I say, I think the best way to conclude this exercise is to explore the creation and the application of a few additional policies and maybe the impact of some of those parameters that we've just taken a look at.

