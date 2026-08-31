---
title: "MAKELINK | Anapedia"
source: "https://help.anaplan.com/makelink-0dbc28e2-da61-4b82-95c7-11fe707a06ab"
author:
published:
created: 2026-05-02
description: "The MAKELINK function generates clickable links in a module."
tags:
  - "clippings"
---
[All functions](https://help.anaplan.com/all-functions-160769b0-de37-4f08-87a0-cc3aa55525a3 "All functions")

For example, if a module contains information about products you sell, you can create links to the online store page for those products.

`MAKELINK(Display text, URL)`

| **Argument** | **Data type** | **Description** |
| --- | --- | --- |
| *Display text* | Text | The text that displays for the link. When a user clicks this text, they're taken to the link specified in the *URL* argument. |
| *URL* | Text | The URL for the link. |

The result of the MAKELINK function must be a text format line item with a text **Type** of **Link**, otherwise the link is not clickable

You cannot currently use the MAKELINK function in Polaris.

In the Classic Engine, you can.

`MAKELINK("Click here to view the expenses board", "https://us2a.app.anaplan.com/a/apps/app/2b12f4a4-aba0-4033-9be6-bbc77d86812d/boards/8b30567a-7edd-4c69-aeee-1b6b4ae8dc24")`

In this example, the text *Click here to view the expenses board* is a clickable link. The link goes to an Anaplan board specified in the *URL* argument.

- The MAKELINK function only works with valid HTTP (http://) or HTTPS (https://) URLs.

[ENCODEURL](https://support.office.com/en-gb/article/ENCODEURL-function-07c7fb90-7c60-4bff-8687-fac50fe33d0e)

This example contains a *Languages* list on columns, and three line items on rows. Two of the line items contain the data for the *Display text* and *URL* arguments and one contains a formula that uses this information.

|  | **English** | **French** | **German** | **Japanese** | **Spanish** |
| --- | --- | --- | --- | --- | --- |
| Link title | English landing page | French landing page | German landing page | Japanese landing page | Spanish landing page |
| Landing page URL | https://www.anaplan.com/ | https://www.anaplan.com/fr/ | https://www.anaplan.com/de/ | https://www.anaplan.com/jp/ | https://www.anaplan.com/es/ |
| Link to landing pages  `MAKELINK(Link title, Landing page URL)` | [English landing page](https://www.anaplan.com/) | [French landing page](https://www.anaplan.com/fr/) | [German landing page](https://www.anaplan.com/de/) | [Japanese landing page](https://www.anaplan.com/jp/) | [Spanish landing page](https://www.anaplan.com/es/) |

The result of the formula in the *Link to landing pages* line item is a clickable link that goes to the respective landing page. You can publish a line item that uses the MAKELINK formula to a dashboard or worksheet to help users access links.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fmakelink-0dbc28e2-da61-4b82-95c7-11fe707a06ab&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>