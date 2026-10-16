<a id="top"></a>

# Senior Azure DevOps Engineer Transformation Interview Guide

Prepared for Olalekan Gabriel Ogundare

This guide combines all 41 interview questions and sample answers prepared for the Senior Azure DevOps Engineer transformation role, including Azure Cloud Adoption Framework questions, a stakeholder discovery questionnaire, delivery expectations, and questions to ask the interviewer. Most spoken answers target approximately 45–60 seconds.

## Index

1. [Role context and experience positioning](#role-context-and-experience-positioning)
2. [Core interview questions 1 to 12](#core-interview-questions-1-to-12)
3. [Additional interview questions 13 to 30](#additional-interview-questions-13-to-30)
4. [Azure CAF questions 31 to 41](#azure-caf-questions-31-to-41)
5. [CAF stakeholder discovery questionnaire](#caf-stakeholder-discovery-questionnaire)
6. [Initial delivery plan](#initial-delivery-plan)
7. [Questions to ask the interviewer](#questions-to-ask-the-interviewer)
8. [Interview preparation checklist](#interview-preparation-checklist)
9. [Official references](#official-references)

[⬆ Back to top](#top)

---

## Role context and experience positioning

The employer describes an existing Azure estate across nine subscriptions, mostly aligned to environments, with some mixed-environment subscriptions. Approximately ten applications are known, including one very large workload; discovery may identify more. Shared services include Entra ID integration, Active Directory, Azure Virtual Desktop, domain controllers, VMs, and supporting infrastructure. Some are operated by other teams.

The immediate objective is assessment, waste identification, a pragmatic target architecture and subscription strategy, reusable Terraform foundations, and deployment and validation of initial components by the end of December. Longer-term objectives are governed subscription provisioning, incremental workload migration, and retirement of the legacy estate.

Position yourself around assessment, platform foundations, governance, automation, and staged migration. Relevant resume examples are Truist’s reusable Azure patterns, landing-zone modules, governance, and GitHub Actions workflows, plus Regeneron’s Terraform/Bicep integration, shared identity, and private networking.

**Experience accuracy:** The resume supplied for this preparation supports more than 12 years of cloud specialization, but does not separately establish 12 years exclusively engineering Azure platforms. Keep that distinction accurate. Proposed designs below are interview approaches, not verified employer facts or personal achievements. Confirm implementation details and metrics before using them.

[⬆ Back to top](#top)

---

## Core interview questions 1 to 12

### Q1 Tell me about yourself and your suitability for this role

“I’m a cloud DevOps engineer and architect with over 14 years in IT and more than 12 years focused on cloud infrastructure, particularly AWS and Azure.

At Truist, I developed reusable platform patterns and Azure landing-zone modules covering networking, identity, security, and delivery. I also used Azure DevOps and GitHub Actions to improve release workflows while retaining governance and auditability.

Previously, at Regeneron, I designed secure cloud foundations with shared identity, private networking, and Terraform and Bicep automation.

This opportunity interests me because it combines assessment, practical architecture, and hands-on implementation. I would focus on understanding existing dependencies, building a governed foundation in parallel, and enabling migration in manageable stages.”

### Q2 How would you assess our existing nine subscriptions

“I would build both a resource inventory and a dependency map. The inventory would cover subscriptions, environments, applications, owners, costs, networking, access, policies, and existing infrastructure code.

The dependency map would focus on shared services: Entra ID integration, Active Directory, DNS, domain controllers, Azure Virtual Desktop, and connectivity. I would validate those dependencies with application and service owners.

My outputs would be a current-state assessment, ownership matrix, risk register, waste opportunities, and an initial migration grouping. Those findings would shape the target architecture rather than assuming current subscription boundaries should be preserved.”

### Q3 What subscription strategy would you recommend

“I would treat the current nine subscriptions as the starting point for discovery. Subscription boundaries should reflect governance, ownership, isolation, lifecycle, and operational requirements.

I would evaluate separation between platform services and application workloads, with appropriate production and nonproduction boundaries. Shared identity, connectivity, and management services would have explicit ownership.

I would avoid creating subscriptions simply to match an organizational chart or forcing every workload into the same model. The recommendation would explain boundaries, management-group placement, inherited policies, access, and migration implications.”

**Technical context:** Azure landing-zone guidance treats subscriptions as units of management and scale, with management groups supporting inherited governance. See the deployment and management-group references.

### Q4 How would you handle identity services operated by other teams

“I would establish responsibility boundaries before changing infrastructure. Entra ID, Active Directory, domain controllers, DNS, and Azure Virtual Desktop have different dependencies and operational owners.

I would document who owns configuration, deployment, access approval, incident response, and recovery for each service. Then I would agree which components belong in our Terraform scope and which remain externally managed dependencies.

I would not place another team’s resources under our Terraform management without an agreed ownership and lifecycle model. The target platform should integrate through clear interfaces and tested dependencies.”

### Q5 How would you identify waste without disrupting services

“I would combine cost information, utilization, configuration, and owner confirmation. Initial candidates could include unattached disks, unused public IPs, oversized resources, duplicate environments, and infrastructure associated with retired applications.

Low utilization alone would not establish that something is unnecessary. It could support disaster recovery, periodic processing, or another team’s dependency.

I would maintain a savings register with evidence, estimated savings, ownership, risk, and proposed action. Decommissioning would follow dependency checks and an appropriate recovery or retention plan. I would track realized savings separately from estimates.”

**Technical context:** Azure Cost Management and Advisor provide optimization recommendations; workload context and owner validation are still needed.

### Q6 Which Terraform modules would you build first

“I would prioritize the smallest set needed to deploy a useful, governed foundation. That would likely include subscription onboarding, policy and RBAC configuration, networking, and management capabilities such as logging and budgets. The exact scope would follow the agreed architecture.

Modules would have clear inputs, outputs, ownership, documentation, and versioning. I would evaluate maintained Azure modules before writing everything ourselves.

I would deploy into a test scope, validate behavior, and demonstrate a second deployment to prove repeatability. The objective is a usable foundation rather than a large module catalog.”

### Q7 How would you structure Terraform state and deployment permissions

“I would separate state according to ownership, lifecycle, and failure boundaries. Platform governance, connectivity, and individual workload landing zones should not automatically share one large state file.

I would use protected remote state with appropriate access controls and locking, and establish a bootstrap process for state infrastructure and deployment identities.

Pipeline permissions would be scoped to what each workflow needs to manage. I would document dependencies between deployment layers and avoid having multiple states or tools manage the same resource.”

**Technical context:** Microsoft’s subscription-vending guidance recommends a dedicated Terraform state file for each workload landing-zone subscription.

### Q8 How would you implement GitHub Actions for Terraform

“Pull requests would run formatting, validation, relevant tests, security checks, and a Terraform plan. Reviewers would assess the proposed changes before an authorized deployment.

I would use workload identity federation for Azure authentication, with trust restricted to approved repositories and deployment contexts. Production changes would have appropriate environment controls.

The workflow would manage concurrency, protect plan and state data, and retain deployment evidence. I would establish drift detection and an emergency-change process so code remains a reliable representation of the platform.”

**Technical context:** Microsoft documents GitHub Actions authentication through OIDC and provides Terraform workflow examples. See the references.

### Q9 Would you import the existing estate into Terraform or rebuild it

“I would decide component by component. The direction is to build the new platform in parallel, so new foundations would normally be provisioned through Terraform.

Existing resources that must remain in place might justify import, but only after reviewing configuration, dependencies, ownership, and the resulting plan.

I would not import the entire estate simply to claim IaC coverage. Some resources should migrate, some should remain temporarily as dependencies, and others should be retired. Each needs an explicit disposition.”

### Q10 How would you migrate the applications

“I would group workloads by dependency, complexity, criticality, and migration method. The first migration should be representative but manageable, with a clear validation and recovery approach.

I would assess identity, DNS, connectivity, data, certificates, monitoring, backup, and deployment dependencies for each workload.

The very large application would receive a separate assessment because its size may conceal multiple dependencies or migration stages. I would not promise every resource can move directly between subscriptions. After each migration, I would verify application behavior and operational readiness before retiring legacy resources.”

### Q11 What would you realistically deliver by the end of December

“I would agree on achievable scope after initial discovery. Essential deliverables would be a current-state assessment, dependency and ownership map, prioritized waste opportunities, target architecture, subscription strategy, and a phased estimate.

On implementation, I would aim to deliver reusable Terraform foundations, an operational GitHub Actions workflow, and an initial deployment validated against agreed criteria.

I would provide a migration backlog and handover documentation. Full migration and legacy retirement are longer-term outcomes; I would make dependencies and estimates visible without treating them as guaranteed initial-engagement deliverables.”

### Q12 Do we need Atlantis Digger or another TACOS platform

“I would first establish collaboration requirements: plan visibility, approvals, locking, drift detection, access control, and auditability.

GitHub Actions may be sufficient initially. If coordination across many states and teams becomes difficult, I would evaluate a Terraform automation platform against those requirements.

I would consider integration, security, operating effort, licensing, and ownership before recommending one. The priority is a reliable engineering workflow; additional tooling should solve a demonstrated problem.”

[⬆ Back to top](#top)

---

## Additional interview questions 13 to 30

### Q13 How would you discover undocumented application dependencies

“I would combine technical discovery with stakeholder interviews. Inventories show what exists, but rarely explain why or which applications depend on it.

I would examine network connections, DNS, identities, deployment configuration, monitoring, and documentation, then validate findings with application owners and shared-service teams.

I would record each dependency, owner, criticality, and migration implication. Unknown dependencies remain visible risks. Before migration, I would validate the map through application testing rather than assume the inventory is complete.”

### Q14 What would your current-state assessment contain

“My assessment would provide a decision-making baseline covering subscription organization, ownership, dependencies, networking, identity, permissions, governance, costs, resilience, and automation.

I would distinguish confirmed findings from assumptions and immediate risks from longer-term improvements.

The outputs would be an inventory, dependency map, ownership matrix, risk register, and prioritized recommendations. Each recommendation would explain the problem, business impact, proposed action, effort, and dependencies so the team could turn it into an achievable delivery plan.”

### Q15 How would you address broad access permissions

“I would first understand current access and operational dependencies. Removing permissions without that context can interrupt deployments or support.

I would review privileged assignments, inherited access, service identities, and ownership. Then I would propose a least-privilege model distinguishing platform administration, workload deployment, and application support.

Changes would be staged, tested, and coordinated with affected teams. I would establish an emergency-access process and a review mechanism so excessive permissions do not gradually return.”

### Q16 How would you decide which governance controls to implement first

“I would prioritize controls according to risk, delivery impact, and readiness. Identity, ownership, logging, and protection of sensitive resources would receive early attention.

I would assess each control’s effect before enforcing it broadly. Some may initially need visibility and remediation planning, while others should prevent unacceptable configurations immediately.

I would document the purpose, scope, owner, exceptions, and validation method. Governance should produce predictable behavior and clear accountability rather than a collection of policies teams cannot explain or operate.”

### Q17 How would you avoid overengineering the landing zone

“I would start with this estate’s requirements: approximately ten known applications, nine existing subscriptions, shared services, and an initial deadline.

I would use landing-zone principles as a reference and select capabilities needed for the first useful deployment.

I would avoid adding components without a clear requirement, owner, and operating model. Decisions would explain what we implement now, what we defer, and what triggers expansion. The initial platform should be secure and extensible while remaining practical to deliver.”

### Q18 How would you manage temporary coexistence of legacy and new platforms

“I would treat coexistence as an explicit architecture phase. Both platforms may need shared identity, DNS resolution, connectivity, monitoring, and support arrangements while applications migrate.

I would define integration points and assess security and availability implications. Each temporary dependency would have an owner and a retirement condition.

Migration waves would check that legacy workloads still function. I would track which shared services remain necessary so the team does not retire a component simply because its primary application has moved.”

### Q19 How would you manage Azure Virtual Desktop dependencies

“I would work with the Azure Virtual Desktop team to understand its architecture and responsibilities. Assessment would cover identity, network access, DNS, supporting storage, application access, and operational processes.

I would identify dependencies that must remain available during platform changes and components in scope for migration or IaC management.

I would agree on validation with the owner, including user access and application behavior. I would avoid treating Azure Virtual Desktop as an isolated collection of VMs.”

### Q20 How would you handle Terraform changes to resources another team owns

“I would establish an ownership agreement before placing those resources under our Terraform management.

It would identify the authoritative repository, deployment identity, approvals, support owner, and emergency-change procedure. We would decide whether our code manages the resource or consumes it as an external dependency.

I would avoid overlapping management because two teams or tools changing the same configuration can create unpredictable results. Where responsibilities are split, I would define a clear interface and document the dependency.”

### Q21 What makes a Terraform module reusable

“A reusable module has a clear purpose, manageable interface, sensible defaults, and documented behavior. It exposes what consumers need without requiring them to understand every implementation detail.

I would include input validation, useful outputs, examples, and versioning. I would test representative use cases and check that changes do not unexpectedly affect consumers.

I would avoid making one module responsible for an entire platform. Boundaries should reflect ownership and lifecycle as well as resource relationships.”

### Q22 How would you handle a failed Terraform deployment

“I would determine what succeeded, what failed, and whether actual resources and recorded state are consistent.

I would review the error, permissions, dependencies, and concurrent changes, then inspect a fresh plan before corrective action.

I would not assume rerunning a workflow or restoring an older state reverses infrastructure. Recovery depends on the failure and its impact. Afterward, I would improve validation or sequencing where appropriate.”

### Q23 How would you manage configuration drift

“I would establish code as intended configuration and use scheduled checks to identify differences.

When drift appears, I would determine whether it is an approved emergency change, an unauthorized modification, or a gap in the code. Resolution could mean updating the code or restoring intended configuration.

I would avoid automatically correcting every difference without considering impact. The process needs ownership, review, and a way to incorporate legitimate emergency changes so the platform does not remain inconsistent.”

### Q24 How would you validate the initial platform foundations

“I would agree on acceptance criteria before implementation. Validation would cover repeatability, access boundaries, connectivity, DNS, logging, policy behavior, and integrations required by the first workload.

I would include negative tests, such as confirming unauthorized identities cannot deploy outside their scope.

I would check operational readiness: who receives alerts, where evidence is retained, and how failures are handled. A successful pipeline is necessary, but readiness requires demonstrating the foundation’s intended behavior.”

### Q25 How would you estimate effort when discovery is incomplete

“I would provide ranges with explicit assumptions rather than a single unsupported date.

I would break work into discovery, architecture, implementation, validation, and migration preparation, identifying access, approvals, and shared-service dependencies.

High-uncertainty items would receive investigation tasks before detailed commitments. I would update estimates as evidence improves and distinguish engineering effort from elapsed time. Stakeholders should understand both the likely delivery window and decisions that could change it.”

### Q26 What if stakeholders expect all applications migrated by December

“I would clarify outcomes and compare them with the stated scope and evidence available.

I would explain application complexity, dependencies, testing, and approval lead times. Then I would present options, such as completing validated foundations and migration planning or including a carefully selected pilot migration.

I would make consequences visible and agree on priorities. My responsibility is to provide a credible plan and communicate risk early rather than accept a commitment the assessment does not support.”

### Q27 How would you approach the very large application

“I would assess it separately because it may contain multiple components, data flows, and dependencies.

I would work with owners to understand architecture, critical business periods, data movement, identity, connectivity, recovery requirements, and acceptable disruption.

Then I would evaluate migration stages and identify what can move independently. It may need a different approach from smaller workloads. I would avoid using it as the first migration unless its risk was manageable and learning value justified the choice.”

### Q28 How would you determine when legacy resources can be retired

“I would define retirement criteria during migration planning: confirmed migration, successful validation, owner acceptance, retention requirements, and evidence that remaining services no longer depend on those resources.

I would check monitoring, backups, DNS, identities, and deployment references before decommissioning.

Retirement would be recorded and followed by verification that costs and dependencies changed as expected. The objective is safe removal with a clear record of what was retired and why.”

### Q29 How would you work within the team’s sprint process

“I would turn the roadmap into reviewable engineering increments. Findings become prioritized backlog items with owners, dependencies, and acceptance criteria.

In stand-ups, I would communicate progress, blockers, and decisions needed from other teams. During planning, I would balance foundation delivery with investigation and avoid committing beyond available evidence.

I would demonstrate completed capabilities, such as a tested module or repeatable deployment, so stakeholders can assess progress through working outcomes.”

### Q30 What would you hand over at the end of the engagement

“I would leave an operable platform foundation and the information needed to continue its development.

That includes repositories, module documentation, workflows, architecture decisions, state and identity ownership, runbooks, and validation evidence. I would provide the inventory, dependency map, waste register, migration backlog, estimates, and unresolved risks.

Handover would include practical walkthroughs. Success means the team can understand, change, deploy, and support the foundation without depending on undocumented knowledge from me.”

[⬆ Back to top](#top)

---

## Azure CAF questions 31 to 41

### Q31 What is Azure CAF and how would you apply it here

“The Cloud Adoption Framework provides guidance for aligning cloud adoption with business goals, organizational responsibilities, architecture, governance, security, and operations.

I would use it to structure discovery and decision-making: clarify transformation objectives, assess the estate, establish landing-zone foundations, and plan incremental migration.

Governance, security, and management would be incorporated throughout. Practical outputs would include decisions, ownership agreements, reusable Terraform modules, and a validated foundation.”

**Technical context:** The CAF methodologies discussed here are Strategy, Plan, Ready, Adopt, Govern, Secure, and Manage.

### Q32 How would you connect CAF methodologies to this engagement

“Strategy establishes business outcomes and success measures. Plan turns assessment into a prioritized roadmap with dependencies and estimates.

Ready covers landing-zone foundations: subscription organization, identity, networking, governance, and automation. Adopt guides workload migration.

Govern, Secure, and Manage establish controls, responsibilities, visibility, and readiness throughout. I would use the framework to organize work while keeping delivery focused on agreed December outcomes.”

### Q33 What is the difference between CAF and Azure landing zones

“CAF addresses the broader adoption journey, including objectives, people, processes, governance, and operations.

Azure landing zones provide architectural guidance for the environment in which workloads run and are an important part of Ready.

CAF helps determine why we are transforming, who owns decisions, and how we deliver change. Landing-zone guidance helps structure the technical foundation implemented through Terraform.”

**Technical distinction:** A platform landing zone establishes shared foundations; application landing zones host workloads within the agreed governance model.

### Q34 Which landing-zone design areas would you assess

“I would assess billing and tenant arrangements, identity and access, resource organization, networking, security, management, governance, and platform automation.

Each produces decisions and actions. Resource organization informs subscription boundaries; identity establishes access and ownership; networking addresses connectivity and DNS; automation establishes Terraform and pipeline practices.

I would review the areas together because decisions in one can affect several others.”

### Q35 How would you assess landing-zone readiness

“I would evaluate whether the platform can safely support the first migration.

That includes subscription placement, working identity and network dependencies, appropriate permissions, controls, logging, deployment automation, and operational ownership.

Gaps would be classified as blockers, acceptable temporary exceptions, or later improvements. Readiness would be demonstrated through acceptance tests and a representative deployment. An architecture diagram alone does not establish that the foundation is ready.”

### Q36 How would CAF influence the management-group hierarchy

“I would use management groups to apply governance consistently to subscriptions with similar requirements.

Before proposing the hierarchy, I would understand workloads, security boundaries, ownership, and operating requirements. I would avoid reproducing every department or application as a management group.

I would document inheritance and test the effect of moving subscriptions. The hierarchy should remain understandable and support the operating model as the estate changes.”

### Q37 How would you distinguish Entra ID from Active Directory requirements

“I would assess them separately and document their integration. Entra ID requirements include cloud identities, application access, administrative roles, and automation identities.

Active Directory dependencies may include domain membership, authentication, DNS, and applications or desktops requiring domain services.

I would work with the identity team to establish which services remain shared dependencies and which infrastructure belongs in our scope. Moving an application does not necessarily remove its domain-service dependencies.”

### Q38 What operating model would you establish

“I would define responsibilities between platform, application, security, identity, networking, and operations teams.

The platform team owns agreed shared foundations and provisioning standards. Application teams own workload requirements and application validation. Shared-service teams retain clearly defined service responsibilities.

I would document deployment authority, incident ownership, access approvals, exceptions, and recovery responsibilities. Automation should not create uncertainty about who supports the resulting platform.”

### Q39 How would you introduce governance into an existing estate

“I would establish the current compliance position before broad enforcement.

I would prioritize controls by risk, assess impact, and distinguish new-platform requirements from remediation of existing resources. Exceptions would have an owner and review date.

I would define compliance monitoring and how corrective work enters the backlog. Governance needs an operating process as well as technical controls.”

### Q40 What would CAF-aligned subscription vending look like

“It would provide a governed process for requesting and provisioning a workload environment.

The request captures ownership, environment, connectivity, security, cost allocation, and operational requirements. Approved automation creates or onboards the subscription and applies the baseline.

I would validate billing permissions, deployment authority, state ownership, and support responsibilities before implementation. Initially, I would favor a simple, reviewable workflow that can evolve into broader self-service.”

### Q41 How would you demonstrate CAF alignment without excessive documentation

“I would maintain concise working artifacts: business objectives, an assessment, architecture decisions, an ownership matrix, risk register, and prioritized roadmap.

Technical decisions would link to Terraform implementation and validation evidence where possible.

Alignment would be assessed through outcomes: clear ownership, controls behaving as intended, repeatable deployments, and understood migration risks. Documentation should help teams make and maintain those decisions.”

[⬆ Back to top](#top)

---

## CAF stakeholder discovery questionnaire

These are proposed assessment responses, not confirmed facts about the employer’s environment.

| Area | Stakeholder question | Proposed answer or assessment approach |
| --- | --- | --- |
| Strategy | What outcomes justify the transformation? | Agree measurable goals for governance, repeatable provisioning, waste reduction, and safer migration. Establish baselines before targets. |
| Scope | What must be complete by December? | Confirm assessment, target architecture, subscription strategy, reusable modules, and validated foundations. Agree separately on any pilot migration. |
| Inventory | Are approximately ten applications the complete estate? | Treat the count as provisional. Reconcile resources, billing, deployment records, and owner interviews. |
| Ownership | Who owns each application and shared service? | Create a matrix covering business, technical, deployment, incident, and recovery responsibilities. |
| Billing and tenant | Who can create subscriptions and under which billing scope? | Validate billing arrangements, permissions, tenant constraints, and approvals before designing automation. |
| Resource organization | Why do subscriptions contain multiple environments? | Establish historical reasons and dependencies before recommending separation or consolidation. |
| Identity | Which workloads depend on Entra ID, AD, or domain controllers? | Record authentication, domain membership, DNS, service-account, and application-registration dependencies. |
| Access | Who has privileged access and why? | Review inherited and direct assignments, validate needs, and plan staged least-privilege changes. |
| Networking | What connectivity must remain during migration? | Map application flows, shared-service access, DNS, external connectivity, and coexistence requirements. |
| Security | What is mandatory for the first foundation? | Agree a minimum baseline, validation criteria, ownership, and exception handling. |
| Governance | Which controls prevent changes versus report issues? | Decide according to risk and impact. Test enforcement before broad application. |
| Management | Who monitors and supports the new foundation? | Define alerts, incident ownership, maintenance, runbooks, and escalation. |
| Cost | Which resources are genuinely unnecessary? | Combine cost and usage evidence with dependencies and owner confirmation before retirement. |
| Automation | What Terraform code and state already exist? | Assess ownership, quality, access, reuse potential, and whether resources are already managed. |
| Delivery | What may GitHub Actions change? | Define deployment scopes, identity trust, approvals, concurrency, and evidence retention. |
| Migration | Which application should move first? | Select a representative workload with understood dependencies, manageable risk, and validation criteria. |
| Large workload | Can the largest application migrate in stages? | Assess component boundaries, data dependencies, constraints, and recovery options. |
| Retirement | When can legacy services be removed? | Require owner acceptance, dependency clearance, retention decisions, and validation. |

**CAF closing answer:**

“I would use CAF to ensure the transformation addresses business outcomes, ownership, architecture, security, and operations together. My immediate focus would be a practical assessment and a validated Terraform foundation. The migration roadmap would then build on that evidence, with clear responsibilities and achievable delivery stages.”

[⬆ Back to top](#top)

---

## Initial delivery plan

| Phase | Concrete output |
| --- | --- |
| Discovery | Inventory, dependencies, ownership, risks, and cost baseline |
| Architecture | Subscription strategy, network and identity decisions, migration principles |
| Implementation | Terraform modules, state bootstrap, deployment identity, and pipelines |
| Validation | Initial foundation deployed, controls tested, repeatability demonstrated |
| Handover | Runbooks, estimates, prioritized migration backlog, and outstanding decisions |

The schedule depends on the actual start date, access, stakeholder availability, and approval lead times. Agree initial-engagement acceptance criteria explicitly. Full migration and legacy retirement remain longer-term objectives unless separately scoped.

[⬆ Back to top](#top)

---

## Questions to ask the interviewer

- What access and documentation will be available at the start?
- Who can approve subscription, networking, and identity changes?
- Is subscription creation supported by the current billing arrangement?
- Which shared-service teams must participate in discovery?
- What constitutes a successfully validated foundation by December?
- Is an initial workload migration expected, or is initial scope limited to foundations?
- What Terraform code, state, and GitHub workflows already exist?

[⬆ Back to top](#top)

---

## Interview preparation checklist

- Practice the introduction in approximately 60 seconds.
- Lead with Azure platform assessment, Terraform, governance, and incremental migration.
- Prepare a real reusable module example, including ownership, validation, and release practices.
- Explain actual Truist and Regeneron contributions accurately; distinguish Bicep from Terraform ownership.
- Avoid claiming 12 years exclusively in Azure unless your employment history supports it.
- Explain shared-service dependencies and ownership before proposing resource changes.
- Separate initial December deliverables from long-term migration completion.
- Distinguish confirmed findings, assumptions, risks, and proposed decisions.
- Describe how foundations are tested, operated, and handed over.
- Prepare measurable evidence for any delivery improvement or cost savings you cite.

[⬆ Back to top](#top)

---

## Official references

These references informed the technical discussion. Confirm current service capabilities and permissions when implementing a design.

- [Cloud Adoption Framework overview](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/overview)
- [Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/)
- [Azure landing-zone design areas](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-areas)
- [Landing-zone identity and access](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/identity-access-landing-zones)
- [Management groups](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/resource-org-management-groups)
- [Deploy Azure landing zones](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/landing-zone-deploy)
- [Subscription vending](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/subscription-vending)
- [Cost optimization recommendations](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-opt-recommendations)
- [GitHub Actions authentication to Azure with OIDC](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect)
- [Terraform and GitHub Actions OIDC example](https://learn.microsoft.com/en-us/samples/azure-samples/github-terraform-oidc-ci-cd/github-terraform-oidc-ci-cd/)
- [Infrastructure as Code with GitHub Actions](https://learn.microsoft.com/en-us/devops/deliver/iac-github-actions)

Resume basis for personal experience examples: Gabriel_O_Resume 5(1).docx, supplied earlier in this interview-preparation conversation. Employer context is based on the Senior Azure DevOps Engineer job description supplied in this conversation.

[⬆ Back to top](#top)
