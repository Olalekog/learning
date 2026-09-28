# TCS AWS Cloud Engineer – FinOps Interview Guide

Prepared for Olalekan Gabriel Ogundare | September 2026

## How to use this guide

These are practice answers, not claims that a particular project happened. Replace the bracketed facts in behavioral answers with your actual account, baseline, actions, dates, and verified result. Keep each spoken answer near 45–60 seconds. For a deep technical follow-up, explain the evidence, decision, implementation, validation, and measured outcome.

## Index

1. [Introduction and role fit](#1-introduction-and-role-fit) — Q1–5
2. [FinOps fundamentals and cost data](#2-finops-fundamentals-and-cost-data) — Q6–13
3. [EC2 rightsizing and scheduling](#3-ec2-rightsizing-and-scheduling) — Q14–21
4. [EKS and ECS optimization](#4-eks-and-ecs-optimization) — Q22–29
5. [Savings Plans and Reserved Instances](#5-savings-plans-and-reserved-instances) — Q30–39
6. [Terraform, automation, and CI/CD](#6-terraform-automation-and-cicd) — Q40–47
7. [Organizations, governance, and security](#7-organizations-governance-and-security) — Q48–55
8. [Well-Architected and architecture](#8-well-architected-and-architecture) — Q56–61
9. [KPI dashboards and financial reporting](#9-kpi-dashboards-and-financial-reporting) — Q62–68
10. [FOCUS and multi-cloud data](#10-focus-and-multi-cloud-data) — Q69–73
11. [Stakeholders and behavioral scenarios](#11-stakeholders-and-behavioral-scenarios) — Q74–84
12. [Rapid-fire definitions and questions to ask](#12-rapid-fire-definitions-and-questions-to-ask) — Q85–91

## 1. Introduction and role fit

**Q1. Tell me about yourself.**  
I have 15-plus years in IT and 12 years working across AWS and Azure. My work combines cloud engineering, Terraform, CI/CD, security guardrails, and production operations. For this role, I would bring an engineering-led FinOps approach: make costs attributable, identify waste and inefficient configurations, implement approved changes safely, and measure the savings. I have reported roughly 20–25% cloud cost savings in my prior work; in the interview I would support that figure with the specific project and measurement period.

**Q2. Why this AWS Cloud Engineer – FinOps role?**  
It sits at the intersection of work I enjoy: building reliable cloud platforms and improving the economics of running them. I can translate a billing finding into a concrete engineering change, such as rightsizing, scheduling, scaling, or a Terraform control, then show the Cloud Business Office whether the change actually saved money.

**Q3. What is your main strength for this role?**  
I understand both infrastructure and the operational consequences of changing it. I can review usage and cost data, work with an application owner on acceptable risk, implement an approved change through IaC, and verify cost, performance, and availability afterward.

**Q4. How is a FinOps engineer different from a cost analyst?**  
A cost analyst identifies and explains spending patterns. A FinOps engineer also turns findings into repeatable changes: right-sized infrastructure, autoscaling, schedules, tagging controls, dashboards, and deployment guardrails. Both roles need to agree on the cost baseline and outcome.

**Q5. What would you do in your first 90 days?**  
In the first month I would learn the account structure, billing ownership, tagging quality, commitments, top cost drivers, and reliability constraints. Next I would rank opportunities by savings, risk, and effort and pilot changes with willing application teams. By day 90 I would have a recurring review, a measured savings register, agreed KPIs, and automated controls for common waste.

## 2. FinOps fundamentals and cost data

**Q6. What is FinOps?**  
FinOps is a collaborative practice for making technology spending visible and improving business value through shared decisions by engineering, finance, and business teams. I apply the iterative Inform, Optimize, and Operate cycle: attribute spending, choose changes, implement them, and measure the result.

**Q7. How do you establish an AWS cost baseline?**  
I choose a defined period and cost basis, then group spending by account, service, application, environment, and owner. I separate recurring usage from one-time purchases, credits, taxes, and unusual events. I record usage volumes and key workload metrics so the post-change comparison reflects demand changes rather than treating every bill reduction as savings.

**Q8. Cost Explorer versus CUR/Data Exports?**  
Cost Explorer is useful for interactive trends, filters, and recommendations. AWS Cost and Usage Report through Data Exports gives granular billing records for custom allocation, reconciliations, and dashboards. I use one agreed definition of cost and document any difference between views.

**Q9. How do you handle untagged spend?**  
First I quantify it by account and service and identify what can be attributed through account ownership, resource IDs, or cost categories. I add required tags to Terraform modules and deployment checks, remediate existing resources with owners, and track the unallocated percentage. Tags used for billing must also be activated as cost allocation tags.

**Q10. What is showback versus chargeback?**  
Showback reports spending to teams without transferring the charge. Chargeback assigns that cost to their budgets or financial accounts. In either case, I document the allocation rules for shared platforms, support, and commitment discounts so the numbers are explainable.

**Q11. How do you detect unexpected spend?**  
I use budgets for known thresholds, anomaly detection for unusual patterns, and dashboards for trends. An alert needs an owner and an investigation path: identify service, account, Region, usage type, deployment, and business event; then decide whether the spend is expected or needs correction.

**Q12. How do you prioritize opportunities?**  
I rank estimated net savings alongside implementation effort, confidence, production risk, owner readiness, and time to realize value. Deleting a known idle development resource may be easy; reducing a production database requires more evidence and a rollback plan. I avoid adding overlapping recommendation estimates as if they were independent.

**Q13. How do you distinguish avoided cost from realized savings?**  
Realized savings are verified after a change against a normalized baseline or a defensible counterfactual. Avoided cost is the expense prevented by a design or control, such as stopping a planned oversized deployment. I report them separately from estimated opportunity, and note any purchase commitments or transition costs.

## 3. EC2 rightsizing and scheduling

**Q14. Walk me through an EC2 rightsizing decision.**  
I review Compute Optimizer recommendations and CloudWatch CPU, memory where instrumented, network, disk, peak periods, and application SLOs. I check family compatibility and licensing, ask the owner to approve a candidate size, test under representative load, and apply it with Terraform or the approved change process. I watch latency, errors, saturation, and cost after the change, with a rollback path.

**Q15. Why is low CPU alone insufficient?**  
The instance may be memory, network, disk, or burst constrained, or may need headroom for monthly peaks. Missing memory telemetry also makes a CPU-only conclusion weak. I correlate multiple metrics and business cycles before recommending a size.

**Q16. When would you schedule EC2 instances off?**  
For nonproduction workloads with predictable hours and an owner-approved schedule. I check dependencies, backup windows, patching, time zones, and whether a restart is safe. I exclude or explicitly approve exceptions for always-on systems and track whether the schedule is followed.

**Q17. How would you implement scheduling?**  
I would store ownership, schedule, and exception metadata as tags or configuration, invoke a controlled automation on a schedule, and log every action. I would test restart behavior, handle holidays and time zones, alert on failures, and leave a clear manual override for application owners.

**Q18. How do you find idle EC2 and EBS resources?**  
I combine utilization history with inventory and ownership. For EC2, I inspect network, CPU, memory if available, and recent operational activity; for EBS I find unattached volumes and old snapshots, verify retention and recovery requirements, then request owner approval before removal. Idle findings are candidates, not automatic deletion orders.

**Q19. How do you optimize Auto Scaling Groups?**  
I evaluate minimum and desired capacity, scaling signals, warm-up time, peak behavior, and instance selection. I test whether a lower baseline or mixed instance policy preserves SLOs; then observe scale-out during representative demand. I distinguish reduced capacity from a purchase discount in the savings report.

**Q20. Would you use Spot Instances?**  
Yes for interruption-tolerant workers, batch jobs, and stateless capacity with retries and diversification. I would assess interruption handling, minimum On-Demand capacity, performance, and the workload's recovery behavior. I would not assume every production workload is suitable.

**Q21. A recommendation says to downsize a critical server, but its owner refuses. What do you do?**  
I ask what failure mode worries them and review peak and memory data together. I propose a safe test, smaller first step, load test, or maintenance-window pilot with explicit rollback criteria. If the risk remains unacceptable, I document the exception and look for less risky savings elsewhere.

## 4. EKS and ECS optimization

**Q22. What are the major EKS cost drivers?**  
Compute on EC2 or Fargate, cluster charges, load balancers, persistent storage, data transfer, logging, and observability are common drivers. I analyze cost alongside pod requests, node utilization, scaling, environment schedules, and availability requirements rather than focusing only on worker-node price.

**Q23. How do you optimize EKS node capacity?**  
I compare pod requests and actual usage against allocatable node resources, identify stranded capacity and placement constraints, then review instance mix and autoscaling behavior. I test changes to requests and limits with application owners, protect critical workloads, and watch evictions, latency, and scaling after rollout.

**Q24. How do you optimize ECS?**  
I examine service CPU and memory reservations, actual usage, task count, deployment minimums, scaling policies, and the EC2 or Fargate launch model. I rightsize tasks and adjust autoscaling only after checking peak demand and deployment behavior. For ECS on EC2 I also measure unused host capacity.

**Q25. How can you allocate shared EKS/ECS costs to teams?**  
I start with account and cluster ownership, then use container-level split cost allocation data where appropriate to connect shared compute costs to ECS tasks and EKS workloads. I agree on rules for idle capacity and shared services with finance and platform owners, and disclose the assumptions in the dashboard.

**Q26. Why might lowering pod requests save no money immediately?**  
The same nodes may still run, so the EC2 bill has not changed. Lower requests create room for consolidation; savings occur when autoscaling can remove nodes, a smaller node mix is adopted, or future growth is absorbed without adding nodes. I verify the actual node and billing change.

**Q27. EKS on EC2 versus Fargate: how would you choose?**  
I compare the workload's resource profile, operational model, placement needs, utilization, scaling, and total cost including idle capacity and supporting services. Fargate removes node management; EC2 can be more economical when efficiently packed. I model representative workloads instead of assuming one is universally cheaper.

**Q28. How do you reduce observability cost for containers?**  
I measure ingestion and retention by log group and workload, remove noisy duplicate logs, set appropriate retention, and sample or filter high-volume telemetry when acceptable. I retain security and incident-response requirements and measure the effect on troubleshooting before broad rollout.

**Q29. How do you validate a container cost optimization?**  
I compare normalized spend and resource usage before and after, including node/task counts, requests, peak throughput, and commitments. I verify latency, errors, availability, and scaling behavior. I do not call a lower allocation estimate a cash saving unless the billed resources or effective rate changed.

## 5. Savings Plans and Reserved Instances

**Q30. Explain Savings Plans in one minute.**  
Savings Plans exchange an hourly spending commitment over a term for discounted eligible usage. Compute Savings Plans are flexible across eligible EC2, Fargate, and Lambda compute; EC2 Instance Savings Plans target a particular EC2 family and Region. I purchase against a conservative stable baseline after planned rightsizing and migration are considered.

**Q31. What is an EC2 Reserved Instance?**  
An RI is a billing discount applied to matching EC2 instance usage under specified attributes and terms; it is not itself a running instance. A zonal RI can also provide a capacity reservation under its terms, while a regional RI is primarily a pricing mechanism. I check matching requirements carefully before purchase.

**Q32. What is coverage versus utilization?**  
Coverage is how much eligible usage receives a commitment benefit; utilization is how much of the purchased commitment is actually used. High coverage with poor utilization can mean overbuying, while high utilization with low coverage suggests some On-Demand baseline may remain. I watch both, by account and organization.

**Q33. How do you size a new commitment?**  
I review hourly usage and seasonality, current RI/Savings Plans inventory, planned migrations, rightsizing, shutdowns, and growth. I model conservative commitment levels and the organization's sharing settings, compare expected savings with downside risk, and obtain finance and workload-owner approval before purchase.

**Q34. When choose Compute Savings Plans versus EC2 Instance Savings Plans?**  
I favor flexibility when workloads may change family, Region, or move among eligible compute services. A narrower EC2 commitment can be considered when a stable family and Region are highly predictable and its economics justify reduced flexibility. I compare actual recommendations and forecast scenarios.

**Q35. Where do RIs fit if we already have Savings Plans?**  
I inventory existing commitments and model how discounts apply before adding any new one. RIs may remain appropriate for stable matching EC2 usage or for certain non-EC2 services with their own RI models. The purchase decision depends on service, eligibility, flexibility, and current effective coverage.

**Q36. What can go wrong with an RI or Savings Plans purchase?**  
Overbuying after a migration or rightsizing effort, misunderstanding eligible usage, ignoring account sharing rules, and relying on an average month instead of hourly demand. I require scenario modeling, approval, and post-purchase coverage and utilization reviews.

**Q37. How do you report savings from a commitment accurately?**  
I compare discounted effective cost with the equivalent On-Demand cost for the *same eligible usage*, include any unused commitment cost, and distinguish the purchase benefit from a separate reduction in consumed resources. I reconcile reports to the agreed amortized-cost view.

**Q38. A team plans to move from EC2 to Fargate in six months. What changes?**  
I avoid a new narrow EC2 family commitment that assumes the old footprint will remain. I model a flexible Compute Savings Plan against the stable eligible baseline, existing commitments, migration schedule, and downside scenarios, then seek financial approval.

**Q39. Should you buy commitments before rightsizing?**  
Usually I first remove obvious waste and account for approved migrations so the commitment reflects the durable baseline. If timing requires an earlier purchase, I use a conservative floor and document the residual risk. A discount on unneeded capacity is still waste.

### Deep dive: Savings Plans vs. Reserved Instances

Savings Plans is the umbrella term for AWS pricing plans that discount
eligible usage in exchange for a one-year or three-year commitment,
usually expressed as a dollar amount per hour. EC2 Instance Savings
Plans and Compute Savings Plans are two types. AWS also offers
Database and SageMaker AI Savings Plans. Payment can be all upfront,
partial upfront, or no upfront.

| Option | What you commit to | What receives the discount | Flexibility |
|---|---|---|---|
| EC2 Reserved Instance (RI) | A matching EC2 configuration for 1 or 3 years | Eligible EC2 instance usage | The most configuration-specific of these options. A regional RI can offer limited instance-size flexibility; a zonal RI reserves capacity in its Availability Zone. |
| EC2 Instance Savings Plan | A dollar-per-hour amount for an EC2 instance family in one Region | EC2 usage in that family and Region | You can change instance size, operating system, or tenancy within that family and Region. |
| Compute Savings Plan | A dollar-per-hour amount of eligible compute usage | EC2, Fargate, and Lambda | The most flexible compute option: coverage can follow changes in EC2 family, size, Region, OS, or tenancy, or a move to Fargate or Lambda. |

AWS describes EC2 Instance Savings Plans as offering up to 72% off
On-Demand rates and Compute Savings Plans as offering up to 66%. Those
are maximums, not a guaranteed saving for a particular workload.

The key RI distinction: an RI is generally a billing discount, not an
instance that AWS launches for you. A regional RI does not reserve
capacity; a zonal RI does in its specified Availability Zone. Savings
Plans do not reserve capacity.

**Example**: If your organization expects steady use of the m5 family
in us-east-1, an EC2 Instance Savings Plan may fit. If it expects to
change families or Regions, or move some work from EC2 to ECS or EKS
on Fargate, a Compute Savings Plan offers more flexibility. Both
compute plan types can discount eligible EC2 worker instances used by
EKS or ECS; they do not discount the EKS cluster charge itself.

**Interview answer**: "I rightsize first, forecast the stable hourly
baseline, and review existing commitment coverage and utilization.
Then I compare an RI for predictable matching EC2 usage, an EC2
Instance Savings Plan for a stable family and Region, and a Compute
Savings Plan when flexibility across compute services or Regions
matters. I measure the effective saving and the risk of unused
commitment before recommending a purchase."

## 6. Terraform, automation, and CI/CD

**Q40. How do you use Terraform for FinOps?**  
I build reusable modules with standard tags, appropriate defaults, autoscaling and retention controls, and cost-conscious environment sizes. I review plans for expensive resources or unexpected replacement, require approvals for significant changes, and use drift detection so the declared configuration matches reality.

**Q41. How would you enforce tags?**  
I require fields such as application, owner, environment, and cost center in Terraform modules and validate them in CI. At the organization level I can use tag policies to standardize values and suitable IAM/SCP conditions to control supported creation paths. I still audit resources because no single control covers every service and workflow.

**Q42. How do you put cost checks in a CI/CD pipeline?**  
I run formatting and validation, security and policy checks, then inspect the plan for resource changes and estimated cost impact where a suitable tool is available. High-cost or destructive changes get owner review; approved exceptions are tracked. After deployment I compare actual spend because predeployment estimates are incomplete.

**Q43. How would you do this in Harness, Jenkins, or GitHub Actions?**  
The pattern is the same: authenticate with short-lived credentials where available, run Terraform checks, create a plan, apply policy and approval gates, and deploy with an audit trail. I can adapt the implementation to the client's pipeline platform; my strongest direct examples are GitHub Actions, Jenkins, and Azure DevOps. I would describe specific Harness hands-on experience only if I can substantiate it.

**Q44. How would you automate idle resource reporting with Python?**  
I would inventory resources across approved accounts and Regions, join configuration and telemetry, calculate candidate savings, and send owner-specific reports or tickets. I would make it read-only initially, exclude protected resources, and use approvals before remediation. The script would log decisions and handle API pagination and rate limits.

**Q45. How do you prevent automated shutdown from affecting production?**  
I use explicit environment and owner scopes, an allowlist or opt-in, protected-resource exceptions, change windows, and dry runs. Automation records what it will change, checks current state before acting, and supports a rapid override. I monitor both the action and the application afterward.

**Q46. How do you manage Terraform state and drift?**  
I use a protected remote backend, encryption, access control, state locking where supported, and separate state by environment and ownership. I review drift before applying a cost change; importing or reconciling a manually altered resource must preserve production behavior. I never edit state casually to manufacture savings.

**Q47. How can PowerShell or Bash help?**  
They are useful for inventory, reports, CI glue, tagging checks, and operational runbooks. For a repeatable cross-account service I often prefer Python with the AWS SDK; regardless of language, I use least privilege, dry-run behavior, structured logs, and error handling.

## 7. Organizations, governance, and security

**Q48. How does AWS Organizations support FinOps?**  
Separate accounts can give clean ownership and guardrails, while consolidated billing provides an organization-wide cost view and potential discount sharing. I align accounts and cost categories with business ownership and review spend at both account and application levels.

**Q49. What is an SCP?**  
A service control policy sets a permissions boundary for principals in applicable AWS Organizations accounts. It does not grant permissions by itself. I use SCPs for carefully tested organization-wide restrictions and pair them with IAM policies and deployment checks.

**Q50. Would you use an SCP to block expensive instance types?**  
Only after examining critical workload needs, exceptions, and service support. A blanket deny can block recovery or legitimate high-performance workloads. I prefer approved patterns and controls with a documented exception route, then validate in a test OU before broad rollout.

**Q51. How do you balance cost and security?**  
I treat required encryption, logging, backup, identity, and network protections as constraints. I optimize within them—for example, tune log retention to policy, select appropriate storage tiers, and remove duplicate telemetry—rather than counting a weakened control as a saving.

**Q52. How do you build tagging governance across teams?**  
I agree on a small tag dictionary and accountable owners, build tags into modules and pipelines, publish compliance by team, and remediate legacy resources in waves. I measure allocated versus unallocated spend and give teams a way to correct ownership disputes.

**Q53. Who should be able to purchase Savings Plans or RIs?**  
I separate recommendation and analysis from purchasing authority. A designated finance or cloud business owner approves commitment amount, term, and payment option; a narrowly authorized role performs the purchase, with an auditable record and post-purchase review.

**Q54. How do you optimize data transfer cost?**  
I inspect the bill by transfer usage type and map traffic among AZs, Regions, NAT gateways, load balancers, on-premises links, and the internet. I assess placement, caching, endpoints, and architecture options, then check resiliency and security impact before changing routing.

**Q55. How do you optimize S3 without jeopardizing recovery?**  
I examine access patterns, lifecycle rules, versioning growth, incomplete multipart uploads, replication, and retention requirements. I model transition and retrieval charges before changing storage class, and obtain data-owner approval for expiration policies.

## 8. Well-Architected and architecture

**Q56. What is the AWS Well-Architected Framework?**  
It provides a structured way to review workloads across operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. For this role I would use the cost pillar to identify waste and trade-offs while keeping the other pillars in view.

**Q57. How have you participated in a Well-Architected review?**  
Use a verified example: “For [workload], I gathered architecture, usage, cost, and owner input. We recorded risks and prioritized [specific changes] by business impact. I implemented or supported [your action], then validated [cost and reliability measures] over [period].” Do not claim formal tool participation if your experience was a design review using the framework principles.

**Q58. What does cost optimization mean in Well-Architected terms?**  
It is a continuing process of matching resources and pricing to business demand, measuring efficiency, and revisiting design choices over the workload life cycle. It is not simply reducing the monthly bill; value, reliability, and performance remain part of the decision.

**Q59. How do you evaluate a managed service migration for cost?**  
I compare total cost: infrastructure, licensing, operations effort, support, data transfer, migration, and resiliency. A service with a higher unit price can still be better value if it reduces maintenance or improves availability. I present assumptions and sensitivity to demand.

**Q60. A cost recommendation conflicts with a reliability requirement. Which wins?**  
I make the trade-off explicit. I quantify the saving and the effect on recovery objectives, availability, or peak performance, then seek the accountable workload owner's decision. Often a different action—such as reducing nonproduction hours—delivers savings without weakening production resilience.

**Q61. How do you incorporate cost in architecture review?**  
I require an owner, traffic and capacity assumptions, estimated monthly cost range, scaling behavior, data transfer and retention estimates, and a plan to measure actual cost after launch. I revisit the estimate once real usage is available.

## 9. KPI dashboards and financial reporting

**Q62. Which KPIs would you put on an executive dashboard?**  
Actual and forecast spend versus budget, spend by value stream, realized savings, open opportunity, unallocated spend, commitment coverage/utilization, and unit cost where a business metric exists. I show trends and the owner of each action, plus reliability context so savings have meaning.

**Q63. What is unit economics in cloud FinOps?**  
It is cost per meaningful business unit—for example, per transaction, customer, order, or completed data job. I align the numerator to attributable workload cost and the denominator to a trusted business metric. It helps distinguish efficient growth from uncontrolled spending.

**Q64. How would you build a dashboard?**  
I define metrics and cost basis with finance first, then ingest billing exports and ownership metadata into a governed dataset. I validate totals against AWS billing views, expose drill-down from executive value stream to application and resource, and automate refresh and data-quality checks.

**Q65. Why might a dashboard not match the monthly invoice?**  
It may use amortized versus billed cost, different treatment of credits, refunds, taxes, support, discounts, time zones, or incomplete late-arriving records. I label the cost basis, reconcile by billing period and account, and explain residual differences rather than silently changing the numbers.

**Q66. How do you forecast AWS spend?**  
I start with historical run rate and seasonality, then include known launches, migrations, growth, shutdowns, and commitment expirations. I give a range with assumptions and compare forecast error to actuals monthly to improve the model.

**Q67. How do you measure savings after rightsizing?**  
I record the old and new effective hourly cost, actual hours used, usage and performance changes, and any upfront or transition costs. I account for shared commitments so I do not double-count a discount and a usage reduction. I show a baseline, measurement period, and calculation to finance.

**Q68. What is a good FinOps operating cadence?**  
Daily or near-real-time alerts for anomalies; weekly triage of opportunities and owner actions; monthly reconciliation of actuals, forecast, commitments, and realized savings; periodic architecture and governance reviews. The cadence should fit the client's spend and release velocity.

## 10. FOCUS and multi-cloud data

**Q69. What does FOCUS stand for?**  
FinOps Open Cost and Usage Specification. It defines a common structure and semantics for technology billing data, helping teams compare and analyze data from different providers. It is a data specification, not a commitment discount or optimization engine.

**Q70. How would you use FOCUS in this role?**  
I would export AWS cost and usage in a supported FOCUS format, map account and application ownership, and build a common reporting layer for multi-cloud or other technology spend. I would validate AWS-specific fields and known conformance differences before using a cross-provider KPI.

**Q71. Does FOCUS replace the AWS Cost and Usage Report?**  
No. It supplies standardized concepts and fields for analysis, while AWS-specific billing data and dimensions still matter for detailed AWS investigations. I select the export that supports the question and reconcile results to the agreed billing basis.

**Q72. How do you compare AWS and Azure costs fairly?**  
I align time periods, currency, cost basis, shared-cost allocation, credits, commitment treatment, and workload scope. FOCUS can simplify normalization, but the services and architectures may differ; a unit-cost comparison with business context is more useful than raw cloud totals.

**Q73. What would you check before trusting a FOCUS dataset?**  
Completeness, source and version, billing period, account coverage, tags and cost categories, treatment of adjustments and commitments, and reconciliation to provider bills. I document any provider-specific extensions or gaps.

## 11. Stakeholders and behavioral scenarios

**Q74. How do you speak to a CXO about FinOps?**  
I lead with business outcomes: spend versus plan, value-stream unit cost, realized savings, forecast risk, and decisions needed. I keep the technical detail available for follow-up but show owners, deadlines, and the effect on reliability or delivery.

**Q75. How do you align the Cloud Business Office, platform, and app teams?**  
I define a shared cost basis, ownership map, review cadence, and decision rights. The Cloud Business Office owns financial targets and reporting; platform teams own common controls; application teams validate workload changes. A tracked backlog links each opportunity to an owner, risk, due date, and measured result.

**Q76. An application owner disputes the cost allocated to their team.**  
I trace the figure from the dashboard to account, tags, cost categories, and billing records, then review shared-cost rules with them. If the mapping is wrong, I correct it and publish the adjustment. If the number is right, I explain its components and agree on optimization actions.

**Q77. Finance asks for a 20% reduction this quarter. What do you say?**  
I would establish the current baseline and identify which portion is controllable in the time frame. I present a portfolio of actions with expected net savings, confidence, owners, timing, and risk, separating one-time reductions from durable savings. If the target is not credible without reliability impact, I say so and offer alternatives.

**Q78. Tell me about a cost optimization you led.**  
Use STAR with evidence: “At [company], [workload or account group] had [baseline and problem]. I analyzed [billing and utilization data], aligned [owners], and implemented [specific IaC or operational change]. Over [period], normalized spend moved from [before] to [after], giving [verified saving], while [SLO/security outcome] remained within target.”

**Q79. Tell me about a recommendation you rejected.**  
“A recommendation suggested [change], but [peak demand, memory, licensing, or recovery requirement] made its estimate incomplete. I collected [evidence], explained the risk to [owner], and selected [safer alternative]. We documented why the original recommendation was deferred and measured the accepted action.” Use an actual example.

**Q80. Tell me about influencing teams without authority.**  
“I showed the app owner their attributable spend and a low-risk opportunity, listened to their reliability concerns, and designed a limited pilot with success and rollback criteria. After they saw both stable performance and measured savings, we agreed on a broader rollout.” Replace with your real stakeholders and result.

**Q81. How do you handle competing value streams?**  
I use common scoring for savings, effort, risk, and business priority, with accountable owners for exceptions. I show the trade-offs in one backlog rather than letting the loudest team set priorities, and escalate resource conflicts with evidence and recommended options.

**Q82. A production rightsizing change causes latency. What do you do?**  
I restore the previous capacity according to the rollback plan, confirm user impact has recovered, and coordinate incident communication. Then I compare telemetry and load patterns, update the sizing hypothesis, and reattempt only after a validated alternative and owner approval. I remove the projected saving from realized results.

**Q83. How do you present a failed savings initiative?**  
I state what was expected, what happened, the performance and cost evidence, and the corrective action. I distinguish a forecast miss from a production incident. Transparent reporting protects trust and improves the next recommendation.

**Q84. What would you ask a client before recommending a commitment purchase?**  
I ask about planned migrations, growth, rightsizing, deployment schedules, ownership and sharing rules, existing purchases, budget, approval authority, and tolerance for unused commitments. I then model conservative scenarios rather than buying to match the latest month's peak.

## 12. Rapid-fire definitions and questions to ask

**Q85. What is amortized cost?**  
A view that spreads upfront and recurring commitment charges across the period they benefit, making workload and period comparisons more meaningful. State which cost basis your dashboard uses.

**Q86. What is an AWS Cost Category?**  
A rule-based grouping of cost and usage into business dimensions such as team, product, or environment. It can combine account, tag, service, and other dimensions for reporting.

**Q87. What is AWS Compute Optimizer?**  
A service that analyzes utilization and offers resource optimization recommendations. Treat the recommendation as an input, then validate application requirements and realized savings.

**Q88. What is Cost Optimization Hub?**  
An AWS view and API that aggregate optimization opportunities across accounts and Regions and deduplicate related recommendations. It helps prioritize estimated opportunity; the savings still require implementation and measurement.

**Q89. What is the difference between a budget alert and anomaly detection?**  
A budget alert compares actual or forecast spend with a defined threshold. Anomaly detection flags unusual spending patterns. Both need an owner and response workflow.

**Q90. What questions should you ask the interviewer?**  
“How is realized savings defined and reconciled today?” “Who approves commitments and production changes?” “What percentage of spend has reliable application ownership?” “What are the largest cost drivers and current EKS/ECS allocation challenges?” “Which dashboard and FOCUS data sources are in use?”

**Q91. What is your closing statement?**  
“My strength is connecting AWS engineering with financial accountability. I can work from granular cost and utilization evidence through Terraform and automation to an approved production change, then explain the measured result to application owners and executives. That is the approach I would bring to your FinOps program.”

## Accuracy notes for interview practice

- Do not present projected AWS recommendation amounts as realized savings. Verify changes against an agreed baseline and cost basis.
- Do not say Savings Plans discount EKS cluster fees; eligible underlying EC2 or Fargate usage is the relevant compute component.
- Do not claim direct Harness administration, formal FinOps certification, or a formal Well-Architected Tool review unless confirmed by your experience.
- Replace every bracketed behavioral placeholder with a real example. Your reported 20–25% savings figure needs a defensible baseline, period, and calculation.

## Primary references

- [FinOps Framework and phases](https://www.finops.org/framework/) and [FOCUS specification](https://focus.finops.org/what-is-focus/)
- [AWS Well-Architected Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost-optimization.html)
- [AWS Savings Plans eligible services](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-services.html), [plan types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html), and [coverage reporting](https://docs.aws.amazon.com/savingsplans/latest/userguide/ce-sp-usingCR.html)
- [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) and [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html)
- [AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html), [EKS cost monitoring](https://docs.aws.amazon.com/eks/latest/userguide/cost-monitoring.html), and [split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html)
- [AWS Data Exports and FOCUS](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create.html)
