---
title: "Avoiding Circular Reference"
source: "https://community.anaplan.com/discussion/156120/avoiding-circular-reference"
author:
  - "[[saket22]]"
published: 2023-07-04
created: 2026-06-15
description: "I have a list of Manufacturing Plants. The output material of one plant becomes the input for the next plant. The cost at which a material is transferred from one plant to the other is the weighted average of opening stock cost, production cost and cost of materials transferred from other plants. Since the cost of one…"
tags:
  - "clippings"
---
[Modeling](https://community.anaplan.com/search?domain=discussions&tags%5B0%5D=Modeling)

Its not super clear to me but based on my understanding I can say you can use lookup to achieve this.  
Create a SYSTEM Module for the Plants with the Base Plant where it should pick up inputs from

![image.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/uploads/GCGAE76B312N/image.png)

And in your calculation Module you can use this mapping to in Lookup to pick-up the values from the base plant

Hope this helps!

Thanks,

Vamshi

[![User: "saket22"](https://us.v-cdn.net/6037036/uploads/userpics/LWVES84W1ES4/nPMI52MX52OT1.jpg "saket22")](https://community.anaplan.com/profile/99315/saket22)

[saket22](https://community.anaplan.com/profile/99315/saket22)

OP

[@Vamshidhar Reddy](https://community.anaplan.com/profile/Vamshidhar%20Reddy) Thanks for taking the time to answer. The situation is not as simple.

Below is the excel mock up of the desired functionality:

![image.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/uploads/FW8U5Y12GF9Z/image.png)

In the above module, 'Transfer Out' from one plant becomes the 'Transfer In' of another plant. The formula for 'Transfer In' would be derived from 'Transfer Out' of another plant. The Weighted Average formula is dependent upon 'Transfer In' line item which is in turn dependent upon 'Transfer Out' line item. It appears to be a loop, but actually is not. Because the calculations are happening on different list members. Anaplan returns a circular reference error because line items used are the same, it does not check that the list members are different.

The end user decides the quantity to be transferred and the material to be transferred in a module which looks like the following:

The From Plant and To Plant are list formatted line items with Plant list. Material is also a list formatted line item with Material list.

[![User: "CommunityMember131103"](https://us.v-cdn.net/6037036/uploads/userpics/WRQ1PNMCTZQZ/nJFWXRJJX3PP9.jpg "CommunityMember131103")](https://community.anaplan.com/profile/16019/CommunityMember131103)

[CommunityMember131103](https://community.anaplan.com/profile/16019/CommunityMember131103)

Updated by [CommunityMember131103](https://community.anaplan.com/profile/16019/CommunityMember131103)

Thanks for the explanation [@saket22](https://community.anaplan.com/profile/saket22),  
Based on your explanation I have built the modules  
**Module 1  
**

![image.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/uploads/P8QOYDGR1XYM/image.png)

Module 2

Module 3

two things I need clarification on,

1. What is the input for th QTY in Module 3?
2. So the **value** in Module 3 that is 1283 for the plant 1 should feed the **value** in Module 1?

Thanks

[![User: "pyrypeura"](https://us.v-cdn.net/6037036/uploads/userpics/QTL29AQOL3AO/n9J3A3U1AHAFF.jpg "pyrypeura")](https://community.anaplan.com/profile/29855/pyrypeura)

[pyrypeura](https://community.anaplan.com/profile/29855/pyrypeura)

Hi,  
  
Do you need time as dimension in your calculations? If you don't need time you could map Transfer 1 to week 1 of calendar Transfer 2 to Week 2 of calendar on so on. Then when you have everything on time dimension you can use previous in your formula. Then when you have done calculations with time dimension you can lookup numbers back to the real dimension you are using.

[![User: "saket22"](https://us.v-cdn.net/6037036/uploads/userpics/LWVES84W1ES4/nPMI52MX52OT1.jpg "saket22")](https://community.anaplan.com/profile/99315/saket22)

[saket22](https://community.anaplan.com/profile/99315/saket22)

OP

[Jul 5, 2023](https://community.anaplan.com/discussion/comment/159177#Comment_159177)

[@Vamshidhar Reddy](https://community.anaplan.com/profile/Vamshidhar%20Reddy) Thanks for the mock up of the modules.

1. The input for Qty in Module 3 will be entered manually for now
2. The Qty and Rate of Transfer Out from Module 3 would feed the Qty and Rate in Module 1. Lets say 100 units of Material 1 goes from Plant 1 to Plant 2 at the rate of 128.3

[@pyrypeura](https://community.anaplan.com/profile/pyrypeura) Thanks for replying.

Yes, time dimension of Months is also being used.