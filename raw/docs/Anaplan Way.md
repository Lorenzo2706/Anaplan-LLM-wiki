# Anaplan Way

Methodology to ensure transparency during anaplan implementation, designed to be agile.

Dirty dozen: implementation risks


Tollgates: checkpoint in between project phases, designed to pause and evaluate the project before moving forward.

**Agile values**:

- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

**Agile Scrum vs Waterfall**:

- Flexibility to adapt to emerging or undiscovered business needs
- Communication and collaboration
- Delivering products in short cycles
- Mechanism for continual improvement and rapid adaptation to change

**Scrum process**:

- Product Backlog (bucket in Anaplan): repository of all User stories
- Sprint Backlog: selected user stories per sprint.
- Sprint cycles: usually 2-4 weeks, with daily scrum meeting. Focus is to develop MVP and incremental features to cover user stories.
- Outcome: potentially usable product increment, sign off of covered user stories

**Do**

- Talk to other successful customers, partners, and Anaplan Business Partners with experience in your use case and get their take on how to tackle your business problem.
- Rethink and optimize current processes; consider how they can be re-envisioned to leverage the power of Anaplan.
- Keep it simple.

**Don't**

- Be tempted to simply replicate a process currently done in another system in Anaplan. It almost never works, and what's the point anyway?
- Try to rebuild a broken process in the middle of trying to build an Anaplan solution. You will fail.
- Try to include everything in the first release. Additional iterations (releases) can quickly follow the first release.


## 4 CORNERSTONES:

The Anaplan Way cornerstones provide the foundation for an implementation of the Anaplan platform. These cornerstones must be planned, executed, and tracked during each phase. They are:

- **Process**: The wider business process that the Anaplan model supports. Must be clarified and documented before the beginning of the project. Base for user stories collection. Key suggestions:
  - It's important to understand the E2E process, with upstream and downstream impacts of the solution on other functions and processes.
  - Rethink and optimize processes
  - Clean data and test data flows
  - Understand inputs and outputs and identify pain points and exceptions
  - Determine the stakeholder perspective over the process (High-level only or also detail oriented)
  - Draw swim lanes between roles
  - Consider any other change that may impact the project (e.g. parallel projects ongoing)
  - Set clear expectations across stakeholders
  - Look beyond current process, use helicopter view over the business processes
- **Data**: All the data components needed for the model: master, meta (describe the context of data, such as: time, version, customer, sku, ect), and transactional data.
  - Key things are master data and hierarchies
  - Critical to identify data sources
  - Start by scoping the dataset
  - Set up all data before UAT
  - Checkout other data migration initiatives
  - Data is the most likely reason for timeline slip
  - Collect data ASAP, involving IT team and considering data requirements
  - Discuss data governance
- **Model**: The design, build, and testing of the Anaplan model.
  - Anaplan recommends that the customer have at least two trained model builders on staff in order to assist the team with the model build and gain valuable experience
- **Deployment**: A plan to ensure that the Anaplan model and new business process are adopted in the organization. Deployment IS change management. It is fundamental to involve users and SME.
  - Users:
    - Ensure the most influential people in the user population are involved early in the process.
    - Encourage the project team to let influential end users own some of the decisions and participate in the design; early buy-in to the design boosts confidence in a successful deployment.
    - Involve end users often in early sneak-peeks at the model.
    - Consider involving a detractor. This person will challenge the team and say out loud what other people might only be thinking. Plus, it's very rewarding to see their perspective change and convert them once the project is successful!
    - Re-engage end users who provided early buy-in later toward the end of the implementation. These people will act as Anaplan champions.
    - Engage end users in testing.
  - SME:
    - Involve them right away - preferably in the requirements gathering process.
    - If they are not constantly involved in the project, re-engage them to evaluate the model when it is around 90% done.


## Methodology:

### Pre release
  - **Rough cut**: estimate of time to have the system up and running. Based on project estimated duration and resource plan
  - **Scoping**: high-level understanding of the requirements, done before the SoW. It includes:
    - _Scope of work_ (process flows and business requirements): a scoping workshop will focus on white boarding the entire process work-flow Anaplan will address, start to finish, and identify areas/processes covered by Anaplan. Roles involved are:
      - Business process owners who understand the end-to-end process
      - End users who are responsible for their individual in-scope process components
      - Data specialists who understand the data inputs, calculations, and data outputs
      - Core project team
    - _Data readiness and data integration_: never make assumptions about customer's data. Assess data readiness - best practices:
      - Start the data discussion with key customer stakeholders before the project begins.
      - Clearly identify data sources and data components (lists, properties, hierarchies, subsets, and transactional data) in the statement of work.
      - Assign your customer homework: have the customer's team ensure production-quality data is ready and available at the start of the project. Gain early insight into data completeness, quality, and integrity. Build contingencies and identify critical risks and dependencies during the planning phase.
    - Level of effort to design and build the model
    - Environment size
  - **SOW**: if rough cut is ok, formalize project details. The sow is a letter of intent (starting point, not rigid), which is used as a starting point where customer expectations are established and defines:
    - Project-specific activities
    - Project deliverables
    - Project timeline
    - Business requirements
    - Pricing
### Foundation (all activities done before sprints)
  - **Project planning**: 4 to 5 days to draft the timeline of project
    - _L1 MB training to users_
    - _Project kick-off meeting_ (introduce the objectives and the Anaplan way methodology). Agenda:
      - Executive sponsor introduction to explain why they chose Anaplan
      - Team introduction and time expectations (full team should participate)
      - Assess and state the current status
      - Methodology (agile)
      - Customer E2E process
    - _Create a manifesto_ -> clear and concise statement of what the team intends to build, focused on the overall project goal. Written by the customer, consultant should help them.
      - Helps to steer project back on track -> help to deliver the MVP (pay attention to not nominate that word, it could undermine client confidence over Anaplan)
      - Creates a sense of purpose on the project, leaving people inspired
      - That should be a tool for communicating with executives
      - Focused on foundations first, keep it easy
      - Important to define what is success and how to measure it
      - All stakeholders should be involved
    - _Establish the scrum team_
      - **Project sponsor** (business owner): responsible for ROI, vision and reprioritize the product backlog. He has final decision over timeline, scope, user stories, product releases and represents stakeholders' interests all the times. Client should provide this role
      - **Scrum Master**: leader without management authority. He has the role of facilitator, creates the environment for team self-organization, makes the forecast, tracks updates and shields team from external interferences. Ideally client side, but not necessary
      - **Scrum team**: cross-functional team of 5/10 people. Includes model builder, developer, tester, analysts, designers. They should provide full time involvement, be able to self-organize and include also client people
    - _Create deployment plan_: project team must convince the rest of the business of the value of the Anaplan model in order for the business to adopt both the Anaplan model and resulting process changes.
      - Over-communicate that a process change and new tool are being implemented.
      - Evaluate how many end users need to be trained; determine how many/what resources are needed to reach them all effectively.
      - Create a training plan for end users. Include why the change is important to the end user, what the change includes, how their work may change due to Anaplan, and where they can go for more information or assistance.
      - Use documentation to create job aids on process flows or changes.
      - Identify two or three key success measures: how will you know end users are adopting the model and process?
    - _Establish a COE_: All projects should be set up for a future Center of Excellence, not just large projects. It is a team that provides leadership, best practices, research, support, and training for Anaplan within an organization. Preparing for a CoE includes:
      - Setting up a data hub as part of the model design. This will make it much easier to add another model for a future use case.
      - Documenting the business processes. When a new use case is being considered, you'll be able to determine how it fits into the overall business process.
      - Documenting the model logic and business rules:
        - Technical ecosystem topology
        - Model blueprint
        - Module blueprints
        - Model flow (model map)/schema
### Design and Process Planning
    sometimes referred to as "requirements gathering". 3 types of activities:
    - _Wireframing_: process of building mock-ups of the end user experience in Anaplan. This **front-to-back model design** approach focuses on the data and functionality that each end user role needs to complete their activities in the planning process. Useful questions:
      - What's the process performed in Anaplan?
      - Who are the users?
      - How are the end users interacting with this model?
      - What is the end user's process?

_UX -> module needed -> data needed -> calculations -> dimensions -> lists_

Wireframes help people to focus on the outcome and facilitate the work of solution architects in creating the model.

- _Writing User Stories_: lowest level of detail used to build the functionality of the customer's Anaplan model. It succinctly describes how an end user wants to interact with the model to complete a specific task.
  - SME describe the business process to the scrum team
  - Scrum team helps build the user story
  - User story owners are assigned
  - User stories must be "INVEST":
    - _Independent_: as much as possible
    - _Negotiable_: starting point for conversation
    - _Valuable_: relevant to customers
    - _Estimable_: developers must be able to determine the priority of the story
    - _Small_: the longer, the more likely to make errors in scoping and estimation
    - _Testable_: fundamental for acceptance

EPICS: cluster of user stories -> good to have an high level view over the goals

US are owned by business stakeholders.

- Acceptance criteria:
  - Define when a feature is working correctly
  - From user pov
  - Include description of how it needs to be tested

The workspace "Agile Implementation - the Anaplan Way" can be used to track user stories.

Best practice is to capture the 95% of the cases with the US, do not focus too much on exceptions.

- _Model Design_: Develop the basic design of the model, including its data flow, lists, user inputs, calculations, and output. Follow best practices by employing the DISCO framework for module design. Great model designs begin with:
  - Understanding the high-level business requirements for the model (in the SOW)
  - Identifying who will use the model (defined in the SOW)
  - Documenting how users will interact with the model (defined by wireframes and user stories)
  - Establishing how data flows through the model (defined in Rough Cut or SOW)

Best practice is to create a **model schema** to capture design. Anaplan recommends lucidchart.

- Determine output modules based on wireframes
- Determine how to transform input into outputs (use of the data hub?)
- Determine dimensions and data flows required
- A schema is a flexible roadmap to build models

Guidelines - **preparing the data for integration** into the model:

- Assign overall accountability of the data work-stream to a member of the customer team; ensure the customer holds the data work-stream owner accountable throughout the implementation.
- Start small and focus on data quality.
- If the data needs cleaning, suggest that the customer bring in expert help if that makes sense. Many organizations rely on external expertise to supplement the core team, and many also bring in special data cleansing tools that help reconcile differences between systems.
- Automate later. It is best to begin with manual uploads. The fact that data and metadata loads are not automated will not stop the project. Poor data can.
- If you haven't already, add data tasks as user stories. You can track them in the Agile Implementation - The Anaplan Way app.
- Pay as much attention to data as you do to building the model.

**Model design review** - best practices:

- Schedule a check-in with your Business Partner or a model builder with more experience than you. Provide a link to your model schema in the meeting invitation.
- Prepare for the check-in by completing the Model Design Check-in Checklist document. During the check-in, you are expected to describe the customer perspective, show your model schema, and describe how the model solves the customer problem.
- During the model design check-in meeting, listen to the changes the model reviewer proposes.
- Document the meeting by placing a copy of the checklist in the project files.
- **Sprint planning**: focus is on turning the customer's requirements into a plan for executing the model build during the Implementation phase. 2 main activities:
  - _Estimating effort_: **Planning poker** is the standard approach to estimating effort in the Agile methodology. Benefits of planning poker:
    - _Builds team engagement_: This collaborative activity serves to enhance team dynamics and define roles. It is a collaborative undertaking that incorporates insights from across the team. It can also be fun!
    - _Diverse perspectives_: Two heads are better than one; more are even better. The approach encourages independent thinking.
    - _Consistency_: Planning poker provides a consensus estimate and an agreed-upon unit of measurement. This allows for easier recalculation of sprints if original estimates are inaccurate.
    - _Tests user story quality_: Wide ranging effort estimates for a single user story often indicate that the story is unclear, missing essential information, or too large to estimate. It's better to find that out now than when you start to build it.

Estimation process using planning poker:

- Establish complexity levels for user stories
- Chose user story with a medium level of complexity and estimate effort
- Assign a unit value representing the effort (e.g. a numeric scale 1-5)
- Once that is determined, use that value as baseline for determining the effort of the remaining stories
- This is a group process: estimation is done independently by each team member and then they compare results and agree on consensus before passing to the next one. The discussion itself can be source of interesting insights. Clients must be onboard as they know their data and their processes.
- In the Anaplan way app there is an ad hoc dashboard to support the process
- It is a good practice to high-medium-low sizing levels of effort when client is not aware of that.

| **Time Intensive \\ Build Complexity** | **Low** | **Medium** | **High** |
| -------------------------------------- | ------- | ---------- | -------- |
| **Low**                                | 1/2     | 1          | 3        |
| **Medium**                             | 2       | 8          | 13       |
| **High**                               | 5       | 20         | 40       |

- Baseline IS NOT a straight estimate of time, it is an estimate of complexity and effort that equates to time. The difference is subtle but important. In the example above, a story with medium complexity and medium time equals eight points, while one with medium complexity but low time is two points, and medium/high is 20 points. Alternatively can use high medium low.
- Develop a consensus estimate of the amount of time it will take to build the functionality described in the baseline user story, and translate the user story points into development hours using a multiplier.
- _Sprint calculations_:
  - _Total development capacity available_: is the volume of model building resources x the length of the Implementation phase. For example, five model builders working 40 hours per week for eight weeks equates to 1600 hours of development time. This development capacity must be divided into sprints. Remember to account for review and testing time as you determine development capacity. The Project Sponsor assigns each story its priority rating. Any user stories that do not fall under Priorities 1, 2, or 3 are initially put in the backlog as Priority 4. Priority 1 items should be completed no later than the first two sprints. Consider dependencies between user stories as well. You won't be able to complete a Priority 1 story if it depends on something you've designated as a Priority 3.
  - _Master Bucket_: initial repository of all User Stories. Then US are sized (planning poker) and prioritized and then put into **Sprint Buckets**.
  - _Managing the buckets_: process of allocating US into sprints based on priority and Tot dev capacity available, to create a feasible sprint plan. Factors to consider to balance the buckets are:
    - Timeline: length of the sprint session.
    - Resources: people allocated to the sprint
    - Scope (User Stories): possibility to move US across sprints

The Managing the Buckets conversation can serve to control scope creep and to revisit priorities when re-planning sprints. As long as you ensure that the user stories priorities are correct and that you create what everyone agrees is a good minimum viable product/Release 1 (not necessarily perfect, but good enough), then you have effectively managed the buckets.

### Implementation
  - **Sprint execution**:
    - Sprint cycles: team made by model builders, scrum team and 1 scrum master. Size user stories
    - P1 usually is for more complex features, that could take more time.
    - Can I actually get those user stories executed with the resources I have? If it doesn't work out that you can do it, you have to **re-balance the buckets** and that means either putting user stories into after sprints or it means actually deprioritizing it for another release
    - Sprint retrospective
  - **Project tracking**: using Anaplan Way Agile App. Includes:
    - Product backlog
    - Sprint backlog
    - Burndown Chart
  - **Sprint meetings**: The sprint cycle includes:
    - _Sprint Planning meeting_
      - Define a realistic sprint backlog
      - Comes after gathering requirements
      - First time estimation against US
      - Then US allocation into sprint -> consider Priority, Dependency and Capacity. Project sponsor has the last word on priority
      - End result: all US allocated
    - _Daily stand-up meetings_ for the Scrum team -> 15 minutes to track progresses and make commitments by sharing:
      - What did you do yesterday
      - What are you going to do today
      - What are the obstacles
    - _Sprint reviews_ at the end of each sprint + mini sprint planning meeting
      - Meeting for external stakeholders to communicate the product, should be informal and less than 2 hours
      - Stakeholder could give valuable feedback over the prototype
    - _All Sprint Retrospective_:
      - Project sponsor declare what's done
      - What's not done goes to the product backlog and ranked
      - Scrum team, project sponsor and stakeholder convert feedback
      - Review of new scopes by PS
  - **Unit testing**: Test each product increment during the build to ensure that it meets the acceptance criteria specified in the user story. It is important that any sample or mock data used for unit testing be realistic. It should reflect the structure and quality of the production data that will eventually be used in the model. The data should also allow the builder to easily verify that formulas are calculating correctly.
  - **Model performance analysis**: Review model performance during the build, and make adjustments to improve organization, response time, and visual appeal. Discuss service levels with the customer and agree on the service levels for the completed model:
    - _Determine core processes/actions_. Expect an average of five to seven core processes in a model.

Establish the current performance baseline time in the model for each of these five to seven processes.

- _Discuss with the customer any difference between the current performance and the desired performance_. Some processes take time. Work to understand the project team's reasons and requirements while doing all you can to manage expectations.
- _As needed, determine if the performance can be improved to the level the customer desires_ (see ways to improve model performance below). You may need to have another discussion with the customer to decide what service levels should be. **Performance self-assessment**:
  - Model design
    - Purpose of modules - Did you follow DISCO guidelines?
    - General dimensionality - Do modules use only the dimensions they really need?
    - Subsets and composite lists - Are you using only the relevant dimensionality for the data?
    - Lists - Are hierarchies correct? Are numbered lists used when appropriate?
    - Sparsity - This may not slow performance in all cases, but it adds to the size of the model.
  - Calculations, formulas, blueprint
    - Use functions and intermediate calculations vs. long, complex formulas. Avoid SUM and LOOKUP in the same formula.
    - Use Booleans, especially for filtering.
    - Summary methods and other blueprint settings - Have you turned off settings that are unnecessary for your model?
  - Model behavior, core code
    - Depending on your skill and experience, this may be beyond a self-assessment. In that case, this can be addressed with a request for a Model Optimization test (see below).
    - At this deeper level, look at configuration issues and behavior that affects the model's performance and overall functionality. In addition, look at optimizing the model's code and assessing functioning at the core level.
- _Request a Model Review or a Model Optimization test_: You can request a Model Review or a Model Optimization test via your Anaplan Business Partner. You can request these analyses during the Implementation or Testing phases, but earlier is better. Average turnaround time is 7 to 10 days, but timing depends on how many projects are in the queue.
  - Request testing when you notice that model performance has slowed:
    - When the model is slow to open or you have long rollback times
    - Specific actions or processes in the model have become slow
    - Increased duration of cell inputs
    - Slow loading of user interface screens
  - The results of the analysis include:
    - What is causing the slow performance and recommendations for how to correct it
    - Model design issues that result in poor performance and recommendations for how to correct them
    - Possible workarounds and best practice advice if suitable
  - Benefits include:
    - A model that performs well with a single user baseline (which allows for better user concurrency testing)
    - Information collected during the analysis will be contributed to the community so that all model builders can learn best practices.
    - Some performance issues may be shared directly with the product design team, leading to improvements and fixes.
- _Document the agreed upon performance levels and obtain a sign-off from the project team_. This can be accomplished using email. Keep the agreement with the other project documentation.
- **Test Plan**: Prepare data and the approach for the Testing phase. Develop a plan to establish:
  - How testing is to be done
  - How feedback will be documented
  - The process for making changes based on feedback
  - The process for retesting if necessary
- **Data Readiness** --> it is fundamental for UAT. Can either use sample mock data to perform functional test, use a small amount of production data or import actual production data before UAT (risky).

Best practice is to involve customer COE.

- **Phase Activity Summary** ([Implementation Phase](onenote:#Implementation%20Phase&section-id={FB8B438C-51AA-4DD8-803F-CD9A80ECBDD5}&page-id={70718F33-2BF5-4765-B920-08718E695E2A}&end&base-path=https://finextnl-my.sharepoint.com/personal/logi_finext_nl/Documents/Lorenzo%20@%20Work/Anaplan%20Model%20Builder.one)):
  - Model build and optimization
  - Project Tracking
  - Sprint review and Retrospectives
  - Deployment Readiness
  - Data Readiness
  - Change management
  - All Sprint Retrospective
  - Tollgate Meeting
- **Go-no go decision**
- **Testing** ([Testing Summary](onenote:#Testing%20Summary&section-id={FB8B438C-51AA-4DD8-803F-CD9A80ECBDD5}&page-id={7EEAF852-4354-4FC9-8ABA-8F4B17C8BC4A}&end&base-path=https://finextnl-my.sharepoint.com/personal/logi_finext_nl/Documents/Lorenzo%20@%20Work/Anaplan%20Model%20Builder.one)):
  - **Set up testing bench**: define scripts, look for SLA, clarify acceptance criteria, perform performance testing. Best practices:
    - Overestimate time for test preparation: writing scripts and prepare data can take a while
    - Send meeting invitation in advance
    - Communicate properly and in time project scope to all levels (to end user)
    - Allow for enough time to run the testing and make model adjustments.
    - Identify the testable criteria up front, as early as user story writing during the Foundation phase.
    - Identify individuals for live testing (UAT).
    - Identify potential hurdles to testing (technical limitations, global audience, and localization).
  - **Test scripts are required for both automated and human testing**
    - For automated testing, the project team will complete a Model Interaction Specification document that captures detailed information describing how each type of user will interact with the model as part of their regular duties. This information will enable the model concurrency team to create test scripts that accurately simulate how the user population will concurrently interact with the model and the frequency of the various interactions.
    - For UAT, the project team will write step-by-step instructions for users to follow ("UAT test scripts") in order to assess whether or not the acceptance criteria have been met as specified in each user story. Broader end-to-end process flow testing should also be captured in the test scripts for UAT.
  - **Automated concurrency testing**: This includes automated testing of peak load, stress, and concurrency on model performance. The purpose is to simulate a scenario that mirrors the expected real-world concurrent user interaction with the model. This testing may not be necessary for some projects.
    - Note that some projects may not require automated concurrency testing. Requests for model concurrency testing should be made at the very start of the implementation project so that the milestones can be understood/agreed upon and the model concurrency information/inputs planned into the project schedule. Every project has many variables that impact testing duration. The range is from a week and a half to four weeks.
    - Contact the Customer Success Business Partner to engage the model concurrency team. Model functionality and performance for a single user, or at very low concurrency (2-3 users), must have already been verified/optimized prior to model concurrency testing. Performance issues that can be observed for a single user or at very low concurrency will be significantly amplified as the concurrent usage increases.
    - Targets and Customer Requirements -> metrics:
      - 90th or 95th percentile target response times for each transaction (A typical goal is a two second or less response time on popular requests when the system is running at normal concurrency levels.)
      - Expected load volumes of the model by end users (pacing)
      - Concurrency level of the user base (typically 15% to 20%)
    - Model Sanitization: manipulation of data in a model to values that do not identify any company, persons, precise locations, company plans, or sensitive financial data.
  - **UAT**: Live testing is important because human users may notice usability issues that machines will not, such as confusing charts, unclear on-screen text, or unexpected results if they engage in "off-script" behavior.

In addition to testing concurrency, capture other critical information from human testers:

- Use of the model with different bandwidths
- Use of different operating systems
- Location differences
- Browser compatibility

One of the keys to a successful UAT is the creation of a test plan with thorough UAT test scripts and clear acceptance criteria.

- _Best practices for UAT_:
  - Test every User Story
  - Test E2E flow
  - Test also for Admin
  - If possible, test real-world scenario
  - Incorporate training into testing
  - Limit users involve to those that can provide the best inputs
  - Formal go/no-go meeting at the end of UAT
  - Set up daily UAT Q&A meetings for testers -> end of day review
  - Set expectations before testing begins
  - At least 1 week for UAT
  - No more than 20 steps (keep it simple)
- _Preparation for UAT_:
  - Agree with the customer which actions are included in each test script and the steps that testers will follow.
  - Write the scripts from the previous sprint as part of the current sprint process (for example, in sprint two write the scripts that apply to the user stories from sprint one).
  - Have testable data loaded in advance of UAT. The data needs to be production-quality and production-quantity.
  - Determine the role and selective access levels needed for testing, and assign appropriate testers to each role.
  - Create a presentation to guide the users on the day of the test.
  - Be sure all participants are online, including the testers, the project team, and the Anaplan consultants.
  - Provide basic Anaplan end user training prior to testing to reduce the amount of "bugs" reported because testers don't understand how the system works.
  - Make sure consultants are looking at Splunk reports and that the server log files are evaluated throughout the testing process.
- _Writing Scripts_:
  - The **user story** being tested.
  - Clear **success criteria** - A broad description of what the test should achieve and how that fits into the overall business need or process flow.
  - **Pre-requisites** - Steps or procedures that the user must have completed before executing the test (i.e., any standard log-in functions or anything they have to do to prepare the test environment).
  - Any known behaviors which may affect the user's ability to complete the script (i.e., any intermittent bugs or undefined behavior).
  - A **step-by-step script**, in tabulated form, with instructions on how to execute the test. Include the following columns:
    - **Step number**
    - **Step description**
    - Requirements mapping, if applicable - Put the actual Requirement that maps to this step; not all steps will map to a Requirement
    - **Comments** - Location for UAT tester to mark any pertinent comments (i.e., "I could not find that option/could not click that button)
    - **Pass / Fail** - The result that the user got when trying to carry out that line of the test script
- _User Survey_: questions are based on conditions related to the performance throughout the testing - internet conductivity, variations of speed, and the performance over the testing period.The only time you will not send out a survey is when you already know the performance or the testing results were poor.As a general rule, only conduct human testing when you expect the results to be somewhat acceptable. Major system issues should be eliminated during the automated testing phase, not during UAT.
- **Triage: bugs vs. change requests**: Feedback from testing may result in both bugs (defects) to correct or change requests (enhancements) to add to the Product Backlog.
  - _Triage committee_:
    - It should include an Anaplan Business Partner, the Solution Architect (partner or Anaplan), a customer subject matter expert, and the Project Sponsor.
    - Classifies feedback as either a _bug_ or a _change request_
    - Assigns a level of severity to each bug or change request
  - _Levels of severity_:
    - L1
      - Bugs: must fix in next UAT
      - CR: Show-stopper functionality - must have in current release
    - L2
      - Bugs: Must fix and include in current release
      - CR: Desirable to have; include in current release if possible
    - L3
      - Bugs: Desirable to have fixed but may be deferred to a future release
      - CR: Likely in a future release
  - _Fixing bugs_: Determine time and resources needed to fix bugs so the customer can successfully complete UAT. If you have a number of L1 bugs to fix and the time and resources needed to fix bugs are extensive, all lower-level bugs will be assigned to the next release. The UAT exit criteria should be referenced as a guide to follow for fixing bugs.
  - _Adding Change Requests_:
    - The Statement of Work (SOW) every customer receives as part of the implementation process contains the requirements for the model and the procedures to follow for incorporating changes in the model. When the testing results include feedback that is reasonably determined to be out of the scope of the SOW, Anaplan or the implementation partner notifies the customer with an impact analysis of the request, a quote for the additional work, and an action plan for handling the request. All change requests must be mutually approved in writing before the work involved in the scope change will be performed.
    - As with fixing bugs, prioritize change requests by level of severity. Any change request considered a "show-stopper" gets top priority; other requests with less severe impact may become part of the next release.
  - _UAT Exit Criteria_ -> often a decision of the team to set a percentage of the L1 bugs and a percentage of the L1 change requests that must be completed.
- **Go/No-Go Decision for Go-Live:** Place the Go/No-Go meeting for go-live on the calendar well in advance. This will help mitigate everyone's busy schedules as you get closer to the go-live date. It also provides the team with a goal date to drive to completion.
- **Deployment/Go-live** -> warranty (hypercare). Deployment is both a cornerstone and a phase. It must be top of mind during every phase - it is critical to plan for internal PR and marketing of Anaplan. If you wait until it is time to deploy to begin these efforts, you'll find it is too late.
  - Deployment plan should be developed early on with the customer, the **objectives** are:
    - _Get buy-in from users_:
      - _Engage the end users_:
        - Ensure the most influential people in the user population are involved early in the process.
        - Let influential end users own some of the decisions and participate in the design; early buy-in to the design boosts confidence in a successful deployment.
        - Involve end users often in early sneak-peeks at the model (e.g., during Sprint Reviews).
        - Re-engage end users who provided early buy-in again toward the end of the implementation - make them Anaplan champions.
      - _Involve respected subject matter experts (SMEs)_
        - Involve them right away - preferably as you gather requirements in the Foundation phase.
        - If they are not constantly involved in the project, re-engage them to evaluate the model when it is around 90% done.
        - By involving them, you'll gain early buy-in to the project and reinforce joint ownership of the solution.
    - _Make the Anaplan process stick in the organization_
    - _Secure the return on investment (ROI) for the customer_

Change management activities:

- **Communication**: Work with the Project Sponsor to create a communication plan early in the project Sample Communication Plan. The communication plan should address the following:
  - Overall communication goal
  - Audience
  - Communication objective
  - Message
  - Communication channel
  - Timing

Best practices for communication plan:

- Good communication can eliminate end user excuses for not adopting the solution
- Keep the audience in mind --> Communication to end user is different from communication to manager and the latter is different from communication with C-Levels
- Over-communication is a good approach
- Status reporting: Status reporting to executives or a Steering Committee is a critical part of project communication. Typically on big projects/organizations, client has their own template, if not you need to provide.
- **Training**: critical change management activity for ensuring user adoption and ROI.
  - Best practices:
    - Train the trainer approach: solution architect trains the super users and the super users train the end user
    - Using video and/or documentation covering step by step e2e process is effective.
    - Hold meeting with demo.
    - Customer building their own training material (never happened to me).
    - Visit end users, especially if geographically dispersed.
    - User L1 model builder early on
    - End user training close to the go-live, to avoid user forgetting how to use the system
    - Super user involved in UAT must be trained early on
- **Documentation**: it provides a lasting record for the project that can be leveraged for future releases or new use cases. It should be kept in a collaborative and secured folder.

Anaplan and/or the Partner Project Manager and the respective customer Project Managers take responsibility to create, maintain, and distribute appropriate documentation, including, but not limited to:

- Overall model schema
- Regional and business unit model schemas
- Data and metadata schemas and processes documentation
- Model maintenance
- Model data flow
- Base model blueprints
- FAQs
- **Monitor performance**: After go-live, monitor performance to ensure goals are met for adoption, a strong customer experience, and service levels. Performance is monitored to ensure adoption, meet SLA and maintain level of experience. An app must be monitored when it has 1 or more of these:
  - High volume
  - High complexity
  - High concurrency

Create an **Anaplan performance app** to monitor performance. Determine the frequency of monitoring, the audience, and also create clear translations of the data for the project team. The app will include Minimum, Maximum, Average, and Median values for:

- Model load time
- Model save time
- Toaster time
- Response time by object, measured in milliseconds
  - Dashboards
  - Modules
  - Large calculations
  - List loads
  - Actions
  - Processes
  - User

Before sharing performance information, make sure that you have already established Service Level Agreements (SLAs) for model performance. In addition, be selective about who receives information regarding performance, as some statistics will need translation.

&nbsp;

![](Clippings\raw\assets\Anaplan Way.png) 
