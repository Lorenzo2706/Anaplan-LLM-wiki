# Inventory reporting-auto expiry

So the next concept, which is actually more of a, planning, modeling calculation rather than true reporting, is how we might also want to use that expiry information to impact our available inventory.

So if I just move over to, back to the application and let's try and focus on what we see here.

So we see a lot of inventory due to expire shortly for to 256 gig tablets in California.

So let's see if that gives us an interesting story.

A little bit, let's see if can find a slightly better one.

Actually, Okay, so I'm now looking at 128.

Let's just confirm that the report tells us we have something interesting happening here. 128.

We have 40,000 units due to expire within the next 5 to 6 days.

So, looking at this now, we can see there's our opening position at 40,000 units.

And, our demand comes through and we start to consume all of that inventory through that demand.

So actually, this is not recognizing that some of that inventory is going to expire before we get to use it.

The application essentially applies a first in, first out, type of method that we're always trying to consume the oldest inventory, to meet the demand.

But in this case, we're not recognizing that some of that inventory is actually about to expire.

there's not enough demand to consume it before it expires.

So the parameter which controls that we see down here.

So at the moment we can see we have auto expiry turned off.

So it's ignoring the expiry risk.

If we were to turn that back on then at the moment it's based upon true expiry.

We can say 17,000 units would expire in week 35 and they cease to be available inventory, which is possible to use to meet the demand.

Same parameter controls.

Just toggle between.

Is it actually the true expiry date or the stop sell date that we're more interested in.

If we think about it in terms of stop sell date, then actually it’s a greater amount of inventory which ceases to be available.

earlier in the time horizon.

Okay, so that's the end of the reports that we wanted to look at.

Just to round off the conversation here, again, the key point/takeaway from this exercise is that there is some configuration involved with making sure that the reports are best, tailored to the organization.

And also that in some instances, the available data will drive what the report can show.

Clearly, things like the aging report needs us to know at least the receipt date in the DC, or preferably the production data inventory.

And similarly, things like remaining shelf life, needs us to know the expiry date of that inventory.

So there's clear interplay dynamic between the data which can be brought into the application and the reporting capabilities, which then get unlocked.

