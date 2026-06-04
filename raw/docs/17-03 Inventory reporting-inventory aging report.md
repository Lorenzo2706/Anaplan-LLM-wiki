# Inventory reporting-inventory aging report

The next one which we just wanted to look at was inventory aging.

Again, we will look at the output page where we can see what the report is doing.

And we will look at a couple of places where we will configure that particular report.

So the report itself is page 522 as an example.

So what does this show me?

This is giving me, let’s select totals as a starting point.

This is showing me all of my inventory across the network and the inventory quantities are grouped into, different buckets based upon the age of that inventory.

So, if we remove this one.

Let’s start things off simply.

Let's go here.

So, here we can see within the California DC we have 60,000 units of inventory, which are greater than 61 days old.

So when measured against a essentially a birth date, then we can see that that is the age of this inventory.

On top of that we have a bit more inventory, which is 46 to 60 days old, and so on.

Most of our network inventory is sat within this 16 to 30 day age range.

So that's essentially the purpose of the report with the corresponding drill down to see exactly what products that is, etc., etc..

Again, the key area of configuration is two things really.

First of all is the definition of these buckets.

these analysis boundaries that we want to put in place, will need to vary based upon the particular organization that we're implementing for.

Where do we do that?

It's within the application configuration area.

And the page is if I can find it, manage age categories.

And then simply just in case of provide a name and input the upper and lower threshold for each of those groupings.

And again, clearly, the right age buckets will vary based upon the organization itself.

The other piece of configuration which is in our overall global parameter page, if we scroll down, is this estimated production date.

In order to identify the age of the inventory, clearly, we need to know a start point.

And this parameter determines how we define that start point.

So in this case it's production date.

this is operating on a basis where the inventory that we load in to the application, it includes the production date of each batch.

So each lot of inventory, we know its original production date.

And clearly based upon the model current date, we could accurately calculate how old that inventory is versus its original production date.

In some instances, that date might not be available.

So additional parameters allow us to define that report on a different basis.

So maybe we have the date that it was received into the distribution center.

So if we have the receipt date then at least we can measure the inventory age relative to that receipt date.

Or finally we may say well actually we want to approximate production date based upon the receipt date, less the lead time.

So then we broadly sort of having an approximation, a guess at the production date by offsetting.

We know when it's received that's offset by the that by the lead time.

So that's the inventory aging report.

