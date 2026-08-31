---
title: "How to avoid Circular Reference"
source: "https://community.anaplan.com/discussion/139009/how-to-avoid-circular-reference"
author:
  - "[[ahowe2]]"
published: 2022-06-02
created: 2026-06-15
description: "I am looking for a solution on how to write a formula that takes the value for 1 and Jan 21 and adds that value to the answer to the formula in cell 2 and Jan 21. The formula I have currently is the below. What is in bold is what I need to figure out. IF Financial Projection Time = Financial Projection Time.'1' THEN Sales…"
tags:
  - "clippings"
---
[Modeling](https://community.anaplan.com/search?domain=discussions&tags%5B0%5D=Modeling)

[Calculation Functions](https://community.anaplan.com/search?domain=discussions&tags%5B0%5D=calculation-functions)

[@ahowe2](https://community.anaplan.com/profile/ahowe2)

I got you covered and you are correct now that I see what you are needing, RankCumulate will not work. But, that doesn't mean it can't be done. I am not going to say this is easy, but it does work.

![2022-06-03_15-07-22.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_15-07-22_139129.png "2022-06-03_15-07-22.png")

Now, how did I get there? Buckle in because this is going to be fun...but long-winded. Also, in the link I linked above about the block structure, the block structure is the reason why we have to do this work around. So, at a high level, we are doing the following:

- have to use Time (at the day level) to get the previous value - due to the block structure.
- but we can't have time on both dimensions, so we have to create a "Fake Time" or Custom Time list

so, here we go...

The setup...

Create a list, I called it Fake Months, with all of the months in your time calendar (your model calendar). It is best to name them the exact same as they appear as it will help the Finditem() to be much easier.

![2022-06-03_15-24-38.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_15-24-38_139129.png "2022-06-03_15-24-38.png")

Create a SYS Months Property module, dimensionalized by Time (native time). Create two line items:

- item Txt: NAME(ITEM(Time))
- Link to Fake Months: FINDITEM(Fake Months, Item Txt)

![2022-06-03_15-26-58.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_15-26-58_139129.png "2022-06-03_15-26-58.png")

Now, we need to also do the opposite, map the "fake months" to the real. Create a SYS Fake Months with two line items:

- Item Txt: NAME(ITEM(Fake Months))
- Time List: FINDITEM(Time, Item txt)

![2022-06-03_15-53-24.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_15-53-24_139129.png "2022-06-03_15-53-24.png")

![2022-06-03_15-54-52.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_15-54-52_139129.png "2022-06-03_15-54-52.png")

Create a module SYS Filter Days which is dimensionalzed only by Time. Now, we only need 256 days, so if your model calendar is greater than one year, I suggest creating a Time Range with only one year. And honestly, the beginning year really doesn't matter because we are only using this for calculation purposes.

![2022-06-03_15-32-20.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_15-32-20_139129.png "2022-06-03_15-32-20.png")

Now, the SYS Filter Days module, create a line item called Date (format of Date) with the formula START() and also change the Timescale to Day as well as change the Time Range to what you defined above (the one year time range).

![2022-06-03_15-34-45.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_15-34-45_139129.png "2022-06-03_15-34-45.png")

Create a SYS Index properties module (this is the 1-256 dimension you have). I called my Row Count, but please use yours. Within this, create a line item name Days, formatted as Date. This is where we are going to link the data. Now, in your previous module, SYS Filter Days, copy the data in the Date line item and paste it into the Days column...This will be used for mapping.

![2022-06-03_15-42-34.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_15-42-34_139129.png "2022-06-03_15-42-34.png") ![2022-06-03_15-50-06.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_15-50-06_139129.png "2022-06-03_15-50-06.png")

Now the fun part...

Create a CALC module, I called my CALC Circular dimensionalized by Fake Months and Time (native time). In the blueprint, change the Timescale to Day, change the time range to One Year (the time range you defined above) and add the following line items:

- Sales Premium
- Sales to Info
- Result
- Persistency Result - although I think can be from the original module but not exactly sure what it does. Mine is hardcoded to.9957.

The formulas go back to my original module (the first picture in this post, the module is named Circular) where I am inputting the Sales to Info. Here are my formulas:

- Sales Premium: Circular.Sales Premium\[LOOKUP: SYS Fake Months Circular.Time list, LOOKUP: 'SYS Filter Days - Circular'.Row Count List\]  
	This is getting the Sales Premium data from the first module, but I am having to lookup on the mapping modules that you have already created.
- Sales to Info: Circular.Sales to Info\[LOOKUP: SYS Fake Months Circular.Time list, LOOKUP: 'SYS Filter Days - Circular'.Row Count List\]
- Result: IF 'SYS Filter Days - Circular'.First Member? THEN Sales Premium \* Sales to Info ELSE Sales Premium \* Sales to Info + PREVIOUS(Result) \* Persistency Result

![2022-06-03_16-06-15.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_16-06-15_139129.png "2022-06-03_16-06-15.png")

![2022-06-03_16-07-22.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_16-07-22_139129.png "2022-06-03_16-07-22.png")

The above is working because the time (in the rows) is a separate block of data, therefore you will not get a circular reference when you use the Previous() function.

Now, back to the first module, the "input" if you will. It is dimensionalized by native time (at the month level) and your index (my row count). I have 3 line items:

- Sales Premium: hardcoded to.47, but you can enter what you want
- Sales to Info: data input
- Result: CALC Circular.Result\[LOOKUP: SYS Row Count Circular.Day, LOOKUP: 'SYS Months - Circular'.Link to Fake Months\]

![2022-06-03_16-11-24.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_16-11-24_139129.png "2022-06-03_16-11-24.png")

![2022-06-03_16-12-07.png](https://us.v-cdn.net/cdn-cgi/image/quality=80,format=auto,fit=scale-down,height=2000,width=2000/6037036/img/2022-06-03_16-12-07_139129.png "2022-06-03_16-12-07.png")

Now, the Sales Premium and the Sales to Info can come from a different module, but I was just going off what you had. But you can see, if I change any of the values in Sales Info, it will automatically calculate correctly.

Let me know if you have questions or need further guidance.

Rob