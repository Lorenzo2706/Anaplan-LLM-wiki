---
title: "Versions | Anapedia"
source: "https://help.anaplan.com/versions-19b4391f-5257-40ee-8dfb-36f0ab426c8f"
author:
published:
created: 2026-05-13
description: "You can use versions to compare different scenarios in a model."
tags:
  - "clippings"
---
[Dimensions](https://help.anaplan.com/dimensions-e020c93d-9f3e-4cce-8294-2d34073b302a "Dimensions")

Workspace administrators can access the **Versions** pane from Model settings, to create, delete, and manage versions. You can also [import](https://help.anaplan.com/f61e31b6-6e66-4d72-822e-bb8ebf1e99d7) and [export versions](https://help.anaplan.com/62e64f25-a3b4-44ec-bee6-72b8b7b5f839) from there.

When a workspace administrator creates a model, it includes versions called Actual and Forecast by default. You can change the names for these versions, but the version created with the name **Actual** is always selected as **Actual** in the **Versions** pane.

Workspace administrators can [create additional versions](https://help.anaplan.com/78fa342e-9c6d-4dff-95e4-e34d725e6eb7) to explore further scenarios, and set up [variance reports](https://help.anaplan.com/bd3ad610-2ea4-4bb2-aa87-d0fb0b73a475) to compare the variance between model versions.

Bulk Copy enables workspace administrators to copy data from one version to another in bulk. You can also use this to copy data from one item to another item within any list.

**Note:** You cannot delete the Actual version.

For any version except Actual, workspace administrators can select a switchover date from the **Switchover** column of the Versions pane. The dates you can select are the model's [time periods](https://help.anaplan.com/f5263813-9086-4554-a8ec-5197a2ddc10f), and are independent of the current period.

Up to the date you select, the data for that version is the same as for Actual and is read-only. After the switchover date, data for the version that's not actual defaults to zero (or other default value for the data type) and you can enter different data.

The Forecast version automatically includes a switchover date, but you can change this. You can also select a new switchover date at the end of each period to create a rolling forecast.

Suppose you set a switchover date of Apr 23. Then create a *Sales forecast* module, with Time on columns, Versions on rows, and *Sales* as a line item on pages. You can edit the Actual data for the first quarter (*Jan 23*, *Feb 23*, and *Mar 23*), but not the Forecast data. For Q2 (Apr 23 onwards), the values for both versions are editable. Editable values display in blue.

![A module with Versions on rows, Time on columns, and a line item called Sales on pages. For Jan 23, Feb 23, Mar 23, data for the Actual version is blue and editable, but data for the Forecast version is black and not editable. The data for both versions is the same for these time periods. From Apr 23 onwards, cell data for both Actual and Forecast is blue. Data has been entered for the Forecast, but Actual data is 0 as no actual data has been entered yet.](https://assets-us-01.kc-usercontent.com/cddce937-cf5a-003a-bfad-78b8fc29ea3f/6fc956e7-5d18-483c-8d56-78b43f4f12a4/versions-switchover.png)

The current version determines which version is selected in a page selector by default when you open a module or subsidiary view. If there’s no current version, or you do not have access to the current version, the version at the top of the Versions list is selected.

You must select a current version to use calculation functions that deliver results based on the current version. For example, CURRENTVERSION returns the value of a line item for the current version.

Workspace administrators can optionally select the **Current** checkbox next to a version to mark the version as current. You can only set one version as the current version.

<iframe title="Feedback Survey" src="https://nebula-cdn.kampyle.com/us/md-form/website/1.23.1/index.html?formId=32270&amp;type=live&amp;isMobile=false&amp;referrer=https%3A%2F%2Fhelp.anaplan.com%2Fversions-19b4391f-5257-40ee-8dfb-36f0ab426c8f&amp;region=digital-cloud-us-main&amp;displayType=embedded&amp;isSeparateFormTemplateFromData=true&amp;domainsListRelativePath=..%7C..%7C..%7C..%7Cus%2Fwu%2F568549%2Fonsite"></iframe>