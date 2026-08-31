---
title: "Managing changes during development"
source: "https://support.anaplan.com/managing-changes-during-development-02434cc7-fd08-4dd0-9191-53905bea38fe"
author:
published:
created: 2026-05-04
description: "Planual rules regarding managing changes during development."
tags:
  - "clippings"
---
DEV>Test and DEV>Prod is more flexible as this allows multiple Test models to be created and deleted without compromising Prod. By always syncing from the development mode to the target, segregation of duties is observed where the administrator can control who has access to the target models.

Compatible models (DEV, TEST or PROD) can be archived without breaking the link between them.

[ALM Explained - Part 2: Testing](https://community.anaplan.com/t5/Best-Practices/ALM-Explained-Part-2-Testing/ta-p/85148)

When restoring Archived models, restore the model to Deployed mode if this is a Production or Test model.

Keep the Development model as small as possible. Try and only use a selection of items in the production lists to minimize the model size. Use the “create from revision” functionality as part of the creation of the Development model.

Note: Don't create a Dev model using the "create from revision" functionality from a Production model as this will create a new revision in the Production model that will ‌now be out of sync with Dev.

Use saved views within the Data Hub to populate the development model. This allows defined data and structures to be imported to support initial development and component testing.

Back to top