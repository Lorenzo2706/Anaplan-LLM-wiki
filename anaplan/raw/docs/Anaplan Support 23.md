---
title: "Anaplan Support"
source: "https://support.anaplan.com/convert-416a5a25-c0c7-43ff-8d52-ce36560c618c"
author:
published:
created: 2026-05-04
description: "Planual rules for transforming data in Anaplan Data Orchestrator."
tags:
  - "clippings"
---
Reducing the volume of data that is processed through a sequence of transforms as soon as possible reduces the processing burden. Use filters and aggregation and only carry across those columns of data that are needed.

The HASH function returns a deterministic unique key that's 56 characters in length based on a parameter value.

You can safely shorten this from 56 characters to n characters (by, for example taking the left n characters) with an insignificant chance of collision based on the expected populated size of the target domain. Shortening the result provides a more readable unique code.

For less than 0.0001% chance of collision, use:

- 10 characters for domains of up to 1,000 items
- 15 characters for domains of up to 1 million items
- 20 characters for domains of up to 1 billion items

This provides the ability to define the format that the date is in, whereas the general CAST function assumes a date in the U.S. date format: mm/dd/yyyy.

This prevents users from mistakenly creating a cartesian product between two large datasets. If you need to do this — for example, to join in a parameter value to be used in a transform — then add a calculated column to both datasets with the same constant value.

For example, a detail filter is applied to the results of a transform after any column calculations have been applied. So, if you need to filter on the original values, apply the calculation in one transformation view and then base a subsequent transformation view with the detail filter on that.

When joining two datasets, we can only join on equal values since it's not possible to join on the result of an expression or filter on an expression.

For example:

TransactionsDataSet.Productcode = ProductMaster.ProductCode AND TransactionsDataSet.TransactionDate >= ProductMaster.StartDate.

To achieve this, join the datasets for all relevant combinations and apply a filter to the relevant rows.

TransactionsDataSet.Productcode = ProductMaster.ProductCode

Calculate a column for the comparison:

InRelevantDateRange = TransactionsDataSet.TransactionDate >= ProductMaster.StartDate

Add a filter for InRelevantDateRange = TRUE

Use these functions to convert string values to the appropriate type:

- TO\_NUMBER
- TO\_DATE
- TO\_TIMESTAMP

Use the TO\_CHAR function to convert NUMERIC (floats / integers), DATE, and TIMESTAMP type columns into strings in a specified format.

To convert between types, use CAST:

![](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/2d73e271-6fc1-4c1b-b3c1-bcee831216bb/CAST%20table.gif)

You can use the functions IS\_FLOAT, IS\_INTEGER, and IS\_BOOLEAN to check if a string value is suitable for CASTing into the required data type.

Note: IS\_FLOAT and IS\_INTEGER don't consider strings that represent numbers with a thousand separators as numbers. Use a formula such as the one below to address the issue:

`IF     IS_FLOAT ( SUBSTITUTE ( 'CC Test'.'New column1' , "," , "" ) )    THEN     CAST(SUBSTITUTE ( 'CC Test'.'New column1' , "," , "" ),"FLOAT")   ELSE      0`

Back to top