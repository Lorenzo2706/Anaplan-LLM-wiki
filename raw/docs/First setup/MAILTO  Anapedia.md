---
title: "MAILTO | Anapedia"
source: "https://help.anaplan.com/mailto-880af3a5-45c5-4f80-ba27-a55fc8b411d0"
author:
published:
created: 2026-05-02
description: "Use the MAILTO function to generate clickable links that send an email. You can specify recipients, subjects, and body text."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

Use the MAILTO function to generate clickable links that send an email. You can specify recipients, subjects, and body text.

You could use the MAILTO function to automatically create links that notify model users of a change to data or a required action.

`MAILTO(Display text, To [, CC] [, BCC] [, Subject] [, Body text])`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Display text* (required) | Text | The text to use as a clickable link to send an email. Displays in the result line item. |
| *To* (required) | Text | The recipients within the **To** field of the email that the function sends.  For multiple recipients, email addresses should be separated by commas. |
| *Cc* | Text | The recipients within the **Cc** field of the email that the function sends.  For multiple recipients, email addresses should be separated by commas. |
| *Bcc* | Text | The recipients within the **Bcc** field of the email the function sends.  For multiple recipients, email addresses should be separated by commas. |
| *Subject* | Text | The subject of the email that the function sends. |
| *Body text* | Text | The body text of the email that the function sends. |

The MAILTO function returns a text result that you can click to send an email.

You cannot currently use the MAILTO function in Polaris.

In the Classic Engine, you can.

`MAILTO("Click to send email", "", "", Mail list, Email subject, Content)`

This example uses line items named *Mail list*, *Email subject*, and *Content*. This means that the recipient, subject, and content of the email are easy to change by clicking different links.

The arguments for the MAILTO function work with all text-formatted line items regardless of whether they have the **General**, **Email**, or **Link** text type.

The only required arguments for the MAILTO function are *Display text* and *To*. To omit any of the other arguments, such as *Cc* or *Bcc*, use two double quotation marks for the argument. This provides a blank text entry for them, which enables you to provide later arguments.

You can add line breaks or paragraphs to the *Body text* argument if it refers to a line item (you cannot add line breaks directly into a formula). These also display in the email that the MAILTO function generates. To add a line break when you edit a text-formatted line item, press:

- Ctrl + Alt + Enter on Windows
- Ctrl + Option + Enter on Mac OS

When you use the MAILTO function to send an email, it opens a new email window in the default email application selected for your operating system. The email pre-populates with the information provided in the arguments of the MAILTO function. To ensure the MAILTO function works properly, select the correct email application for your operating system and browser.

The MAILTO function sends the details of an email to your default email application via a URL string.

Different browsers support different maximum lengths for URL strings. Internet Explorer supports 2,048 characters, and other browsers such as Google Chrome, Firefox, Safari, and Microsoft Edge support about 80,000. However, the MAILTO function is limited by a combination of the operating system, browser, and email application. For example, a combination of Windows operating system, Google Chrome browser, and Outlook email application limits characters to about 2,000.

If the combined character count of the recipient's email addresses, the email subject, and the body text cause the URL to exceed the maximum length for your browser, the MAILTO function does not work.

If your email contains [non-ASCII characters](https://en.wikipedia.org/wiki/ASCII) such as Japanese or Cyrillic, each character displays in URLs as multiple symbols and numbers, usually about 3 to 6. This is based on [percent-encoding](https://en.wikipedia.org/wiki/Percent-encoding). Additionally, in percent-encoding, a whitespace character and various punctuation display as three characters. This means that the maximum length of MAILTO emails composed of non-ASCII characters is can be about one sixth to one third as long as standard ASCII characters. Additionally, the maximum length of MAILTO emails that contain a lot of punctuation is also shorter.

[HYPERLINK](https://support.office.com/en-gb/article/HYPERLINK-function-333c7ce6-c5ae-4164-9c47-7de9b76f577f)

In this example, the module has a *User roles* list on columns, which contains the different categories of users to send emails to. The module also has text-formatted line items on rows. The line items contain the email addresses to send the emails to, the content of the emails, and a formula that uses the MAILTO function.

You can publish the links generated by the MAILTO function to a [dashboard](https://help.anaplan.com/f95d9d39-5ece-46a2-9cc3-2e76563b8fb2) or [page](https://help.anaplan.com/17b0ba75-c9dc-4b68-840f-6f846632a42b). Use this to enable users to send emails more easily.

|  | **Model Builders** | **Reviewers** |
| --- | --- | --- |
| Email link | Send email to model builder | Send email to reviewers |
| To | Brianna.builder@anaplan.com | Renata.reviewer@anaplan.com |
| Cc |  | Sawyer.security@anaplan.com, Patrice.planner@anaplan.com |
| Bcc |  | Alex.admin@anaplan.com |
| Subject | New update to the Reporting Model | Review the latest update to the Reporting Model |
| Body text | Hello Brianna,  There's been an update to the Reporting Model. Please check it and update the model with your required actions. | Hello All,  Please review the changes that have been made to the Reporting Model. Provide any feedback via the agreed channels. |
| Link to send email  `MAILTO(Email link, To, Cc, Bcc, Subject, Body text)` | Send email to model builder | Send email to reviewers |

When a user clicks the text *Send email to model builder* within the *Link to send email* line item, the MAILTO function generates an email where:

- *Brianna.builder@anaplan.com* is the recipient in the **To** field of the email.
- The **Subject** line reads *New update to the Reporting Model*.
- The body text of the email reads: *Hello Brianna, there's been an update to the reporting model. Please check it and update the model with your required actions.*

When a user clicks the text *Send email to reviewers* within the *Link to send email* line item, the MAILTO function generates an email where:

- *Renata.reviewer@anaplan.com* is the recipient in the **To** field of the email.
- *Sawyer.security@anaplan.com* and *Patrice.planner@anaplan.com* are the recipients in the **Cc** field of the email.
- *Alex.admin@anaplan.com* is the recipient in the **Bcc** field of the email.
- The **Subject** line of the email reads *Review the latest update to the Reporting Model*.
- The body text of the email reads: *Hello All, Please review the changes that have been made to the Reporting Model. Provide any feedback via the agreed channels.*

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmailto-880af3a5-45c5-4f80-ba27-a55fc8b411d0&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>