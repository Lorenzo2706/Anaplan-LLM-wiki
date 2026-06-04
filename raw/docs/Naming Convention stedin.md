# Naming Convention

## Short Introduction

### Why do we need naming conventions?

- **Model structure and navigation**
Consistent naming makes it easier to navigate large models
- **Efficient development**
Easier to locate components quickly
Helps (new) team members understand the model design
- **Improved maintainability and troubleshooting**
Standardized names reduce time spent identifying errors

> Naming conventions are guidelines, not strict rules
> 

---

## Guiding Principles

- **Alignment upfront**
Agree on a unified naming convention before starting
- **Review and align changes**
Align updates during Model Builders meetings
- **Clear and accessible standards**
Ensure documentation is clear and accessible in sharepoint

---

## How to Apply

- Applicability in existing models
- Benefits & guiding principles
- Structure user stories

---

## Easy guide -- Naming Conventions

### 1. Naming Conventions - Lists

- **List code (identical between models)**
    - *V1 Versions*
    - *PR2 SKU*
    - *D3 Employees#*
    - *#LOAD SAP ACTUALS*
- **Alternative Hierarchies**
    - *P1 -- Programma*
    - *PV2 -- Programma versies*
    - *PT2 -- Taak*
- Codes established in DH -- if levels are not used in model, this has consequences for numbering
- **Properties only used for**
    1. display name
    2. dependent drop-down
    - Loading #list (numbered lists) in module instead of properties
- **Subsets**
    - "SS" & name list
    - Example: SS V01: Versions: Forecast
- **Line item Subset (LIS)**
    - "LIS" & module code
    - Example: *LIS A01: P&L*
- **Categorization**
    - fake lists as headers

---

### 2. Naming Conventions - Modules

- **Module code**
    - *LO01. PAM kenmerken*
- **Functions**
    - DM = demand
    - SP = Supply
    - RP = Report
- **Data flow:** DM01 → DM02 → DM03
- **Parallel calculations:** DM03 | *└* DM03a
- Only one module allowed per dimension set per category
    - Only if segregation of duties are disturbed, allowed to neglect.
- **Saved View code**
    - Example: o*LO 01.1 Update L: PT2 Taak*
    - Logic: Prefix code (module code.X) in order of actions in process, Update L/M.
- **Categorization**:
    - DISCO → D (Data), I (Input), S (System), C (Calculations), O (Output)
    - Order of Calc flow
    - Functional Area

---

### 3. Naming Conventions -- Line Items

- **Categorization (labels)**
    - Load
    - Transformation
    - Calculations
    - Filters / CF
- **Abbreviations**
    - AN: Anaplan list (e.g   *AN PT2 Taak*  )
    - FO: firstoccurence (eg.  *FO Employee code* )
    - DB: filter (user) (eg.  *DB Active Employees w/ keten selection* )
    - CF: color format (eg. *CF delta D/S*)
- Clear if name / code: Taak code
- **Saved view**
    - Filter SV L01.1
- **Subsidiary views**
    - Only allowed for dashboarding publishing purposes
    - Maintain readability

---

### 4. Naming Conventions - Actions

- Coding all actions
- All imports, processes, exports, triggers must be coded
- **Example:**     *01. Update MD* | *01.01. Update L: PT1*, *01.02 Update L: PT2*, ..  ****
- Clean-up and categorize actions every sprint
- **Standardized format →** `XX.YY Update L/M To_List /Module from Model_Code: From_ModuleCode (From_View_Code)`
    - Process nr (01)
    - Action nr (02)
    - Update list / module (Update L:/M:) **or** description of action (e.g. delete, sort, export)
    - View source module (A01) – important to code all saved views (in order).
    - Source module (IM 05)
    - Target list / module (ADL 04)
- **Example**
01.02 Update M: ADL04 from DH: IM05 (01.1)

---

### 5. Naming Conventions - Dashboards

- **Categorization**
Functional, based on user access and DISCO
    - Naming category **:** *01. Master Data Management*
    - Naming Dashboard: *01.02 Exception-based mapping Postcode: Region*
- **Status Dashboard**
    - Draft: user can’t see, should be in *‘uncategorized’ or ‘not released’.*
    - *Published but new draft:* put **(S)** behind the dashboard name: *01.02 Thema’s en Tafels (S)*
    - *For S&OP: Copy dashboard and put the copy in section ‘Updated dashboards’.*

---

## Complete guide

[FINAL - Naming Conventions Agreements Anaplan [STRAT + TACT].docx](https://www.notion.so/FINAL-Naming-Conventions-Agreements-Anaplan-STRAT-TACT-docx-2d9724c1494843658c5a5d09ba49f19e?pvs=21)

---

## HANDS ON: APPLY NAMING CONVENTION IN ANAPLAN

- Apply naming conventions
- Then create user stories for model maintenance