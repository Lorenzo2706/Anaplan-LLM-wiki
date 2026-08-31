# Inventory reporting-remaining shelflife report

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

