<a id="top"></a>

# Platform Architect Cloud and Kubernetes Interview Preparation Guide

Prepared for Olalekan Gabriel Ogundare

This guide combines the vendor screening questions, cloud and Kubernetes architecture questions, and three concrete practice scenarios from our preparation. Most primary answers are designed for approximately 45–60 seconds of spoken delivery. Technical details and follow-ups support deeper discussion.

The role emphasizes target-state architecture, reference patterns, governance, platform usability, reliability, and collaboration across application, platform, security, and operations teams.

**Experience grounding:** Your uploaded resume describes strong AWS and Azure experience, EKS and AKS platform work, reusable architecture patterns, automation, security, and incident response. It describes GCP experience as moderate. Proposed designs and illustrative incidents below are not verified personal achievements. Use “I would” for proposed work and “I implemented” only for work you personally delivered. Confirm any metrics and your individual contribution before using them.

## Index

1. [Interview positioning and core themes](#interview-positioning-and-core-themes)
   - [Resume experience matched to the role](#resume-experience-matched-to-the-role)
2. [Vendor screening and platform leadership](#vendor-screening-and-platform-leadership)
   - [Q1 Tell me about yourself and why you fit this role](#q1-tell-me-about-yourself-and-why-you-fit-this-role)
   - [Q2 How much hands-on GCP experience do you have](#q2-how-much-hands-on-gcp-experience-do-you-have)
   - [Q3 What is the difference between a Platform Architect and a DevOps Engineer](#q3-what-is-the-difference-between-a-platform-architect-and-a-devops-engineer)
   - [Q4 How would you define the target-state architecture](#q4-how-would-you-define-the-target-state-architecture)
   - [Q5 Tell me about a platform architecture initiative you led](#q5-tell-me-about-a-platform-architecture-initiative-you-led)
   - [Q6 What would your first 90 days look like](#q6-what-would-your-first-90-days-look-like)
3. [Cloud architecture and governance](#cloud-architecture-and-governance)
   - [Q7 How would you design networking across AWS and GCP](#q7-how-would-you-design-networking-across-aws-and-gcp)
   - [Q8 How would you secure application access to cloud services](#q8-how-would-you-secure-application-access-to-cloud-services)
   - [Q9 What would you standardize across clouds](#q9-what-would-you-standardize-across-clouds)
   - [Q10 How would you choose a modernization strategy](#q10-how-would-you-choose-a-modernization-strategy)
4. [Kubernetes platform engineering](#kubernetes-platform-engineering)
   - [Q11 What would a standard deployment pattern include](#q11-what-would-a-standard-deployment-pattern-include)
   - [Q12 How would you manage multiple clusters](#q12-how-would-you-manage-multiple-clusters)
   - [Q13 What experience do you have with internally managed Kubernetes](#q13-what-experience-do-you-have-with-internally-managed-kubernetes)
   - [Q14 How would you select a multi-cluster management approach](#q14-how-would-you-select-a-multi-cluster-management-approach)
   - [Q15 How would you upgrade Kubernetes safely](#q15-how-would-you-upgrade-kubernetes-safely)
   - [Q16 How would you design capacity and scaling](#q16-how-would-you-design-capacity-and-scaling)
   - [Q17 How would you design a resilient application](#q17-how-would-you-design-a-resilient-application)
   - [Q18 How would you design disaster recovery](#q18-how-would-you-design-disaster-recovery)
5. [Service mesh and observability](#service-mesh-and-observability)
   - [Q19 How would you design a service mesh strategy](#q19-how-would-you-design-a-service-mesh-strategy)
   - [Q20 How would you define observability and reliability standards](#q20-how-would-you-define-observability-and-reliability-standards)
6. [Automation and developer experience](#automation-and-developer-experience)
   - [Q21 How would you improve release velocity while retaining governance](#q21-how-would-you-improve-release-velocity-while-retaining-governance)
   - [Q22 How would you choose between Helm Kustomize and Crossplane](#q22-how-would-you-choose-between-helm-kustomize-and-crossplane)
   - [Q23 How would you design canary deployments](#q23-how-would-you-design-canary-deployments)
   - [Q24 How would you improve developer experience and drive adoption](#q24-how-would-you-improve-developer-experience-and-drive-adoption)
7. [Concrete scenario one Reusable platform pattern](#concrete-scenario-one-reusable-platform-pattern)
   - [Q25 Give me a concrete example of a reusable platform pattern](#q25-give-me-a-concrete-example-of-a-reusable-platform-pattern)
   - [Follow-up How would you handle a breaking change](#follow-up-how-would-you-handle-a-breaking-change)
   - [Follow-up How do you avoid making the pattern too restrictive](#follow-up-how-do-you-avoid-making-the-pattern-too-restrictive)
8. [Concrete scenario two Kubernetes incident](#concrete-scenario-two-kubernetes-incident)
   - [Q26 How would you troubleshoot this production outage](#q26-how-would-you-troubleshoot-this-production-outage)
   - [Concrete troubleshooting commands](#concrete-troubleshooting-commands)
   - [Follow-up Why not just restart pods](#follow-up-why-not-just-restart-pods)
   - [Follow-up How would you roll back with Argo CD](#follow-up-how-would-you-roll-back-with-argo-cd)
   - [Follow-up What would the root-cause analysis include](#follow-up-what-would-the-root-cause-analysis-include)
9. [Concrete scenario three Architecture tradeoff](#concrete-scenario-three-architecture-tradeoff)
   - [Q27 Describe the tradeoff and your decision framework](#q27-describe-the-tradeoff-and-your-decision-framework)
   - [Follow-up Are dedicated node pools equivalent to dedicated clusters](#follow-up-are-dedicated-node-pools-equivalent-to-dedicated-clusters)
   - [Follow-up How would you justify the additional cost](#follow-up-how-would-you-justify-the-additional-cost)
   - [Follow-up What controls belong in a shared cluster](#follow-up-what-controls-belong-in-a-shared-cluster)
10. [Questions to ask the vendor](#questions-to-ask-the-vendor)
11. [Final preparation checklist](#final-preparation-checklist)
12. [Official technical references](#official-technical-references)

## Interview positioning and core themes

Position yourself as an AWS and Azure platform architect with strong Kubernetes, security, automation, and reliability experience, with moderate GCP exposure. Your recent Truist and Regeneron roles provide relevant examples.

For design questions, explain the requirement, your choice, the tradeoff, and how you verify success. For experience questions, explain the situation, your responsibility, your actions, and the actual outcome.

Expect questions about:

- Target-state architecture, standards, reference implementations, and governance.
- Secure, scalable, repeatable deployments across dev, UAT, and production.
- AWS and GCP networking, identity, private access, and cloud guardrails.
- Multi-cluster operations, upgrades, capacity, tenancy, resilience, and recovery.
- Service-to-service security, traffic management, and observability.
- IaC, GitOps, progressive delivery, and self-service platform capabilities.
- Influencing teams, driving adoption, and reducing operational toil.

### Resume experience matched to the role

The following matches come from the Gabriel_O_Resume 5(1).docx supplied for this preparation. They distinguish documented experience from implementation details that still need your confirmation.

| Job requirement | Relevant resume experience | How to explain the connection |
| --- | --- | --- |
| Target-state architecture and reusable patterns | Truist: standard AWS–Azure designs covering networking, security, identity, and CI/CD, reused by teams across the bank | Explain one pattern, the requirement it addressed, and how other teams consumed it |
| Enterprise Kubernetes | Truist: EKS scaling, upgrades, hardening, monitoring, and companion AKS platforms; Southern Company: EKS data-processing workloads | Describe your role in cluster lifecycle, workload onboarding, and operational standards |
| Cloud networking and identity | Regeneron: shared identity, private networking, and consistent CI/CD across AWS and Azure for clinical and genomic data | Connect network and identity decisions to sensitive-data access and GxP requirements |
| Security and governance | Truist: AWS Organizations/SCPs, Security Hub, GuardDuty, automated checks and fixes, Azure Policy, Sentinel, and Defender for Cloud | Explain preventive guardrails, detection, remediation, and ownership |
| Infrastructure automation | Truist: reusable Bicep modules/templates and Azure landing-zone standards; Regeneron: Bicep alongside Terraform | Explain reusable interfaces and deployment standards; confirm the exact Terraform components you owned |
| CI/CD and auditability | Truist: Azure DevOps and GitHub Actions releases, approvals, and environments, with approximately 40% shorter release cycle time | Explain the workflow changes, measurement basis, and retained controls |
| Observability and incident response | Truist: major-outage coordination, improved alerts/runbooks/automation, tracked uptime and response-time goals; Southern Company: CloudWatch and Prometheus | Describe actual signals, incident decisions, and verified recovery outcomes |
| Recovery and availability | Regeneron: recovery objectives, runbooks, and automated common failure recovery for research pipelines | Explain recovery design; do not claim specific drills or measured RTO/RPO unless you performed them |
| Modernization and specialist workloads | Regeneron: SageMaker, Azure Databricks, and end-to-end ML pipelines; Truist: cost/capacity forecasting and internal Azure OpenAI workflows | Show how platform patterns supported distinct workload needs with access controls |
| Cross-team platform adoption | Truist: reusable designs consumed by teams across the bank; Regeneron: company-wide cloud rules and templates | Describe stakeholder alignment, onboarding, and a real adoption example without inventing team counts |
| GCP | Skills list describes moderate GCP capability; Alteryx role describes a Compute Engine/Cloud Storage pilot | Present actual exposure accurately and explain transferable AWS/Kubernetes principles |
| Service mesh and internally managed Kubernetes | Istio appears in skills; detailed production mesh and self-managed control-plane ownership are not established in the resume | Use design answers and identify what you personally operated before making experience claims |

**Best interview sequence:** Lead with Truist for platform standards, EKS/AKS, security, and delivery. Use Regeneron for secure multi-cloud architecture, sensitive workloads, recovery objectives, and Terraform/Bicep integration. Use Southern Company for EKS operations and CloudWatch/Prometheus examples.

[⬆ Go to top](#top)

## Vendor screening and platform leadership

### Q1 Tell me about yourself and why you fit this role

**Sample answer:**

“I’m a multi-cloud DevOps and security engineer and architect with over 14 years in IT and more than 12 years focused on cloud infrastructure.

At Truist, I create reusable AWS–Azure patterns for networking, identity, security, and CI/CD. I manage EKS scaling, upgrades, hardening, and monitoring alongside AKS, and standardize infrastructure through reusable modules and governance controls.

Previously at Regeneron, I designed secure cloud foundations for research workloads, combining shared identity, private networking, Terraform and Bicep automation, and recovery planning under GxP requirements.

That aligns with this role’s focus on reference architectures, enterprise Kubernetes, and reliable deployment standards. My deepest experience is AWS and Azure, with moderate GCP exposure. I bring practical architecture judgment and experience helping teams adopt consistent platform patterns.”

**If asked for the business result:** Explain your documented release-workflow improvement at Truist, including the approximately 40% reduction and how it was measured. Keep this as a follow-up so the introduction stays close to 60 seconds.

**Alternative shorter introduction:**

“I’m a multi-cloud DevOps and security engineer and architect with over 14 years in IT, including more than 12 years focused on cloud infrastructure. My strongest experience is across AWS, Azure, Kubernetes, infrastructure automation, and enterprise security.

At Truist, I developed reusable platform patterns covering networking, identity, security, and CI/CD, and supported EKS and AKS environments. At Regeneron, I worked on secure cloud architecture supporting research and data workloads.

This role aligns with my experience translating enterprise requirements into repeatable deployment patterns application teams can use. My deepest cloud experience is AWS and Azure, while GCP is a secondary area where I bring transferable architecture and Kubernetes knowledge.”

[⬆ Go to top](#top)

### Q2 How much hands-on GCP experience do you have

**Sample answer:**

“My GCP experience is moderate compared with my AWS and Azure background. My resume includes exposure across compute, storage, networking, IAM, monitoring, and Kubernetes.

I would be transparent about that distinction. My strength is understanding the underlying architecture: network isolation, workload identity, access controls, Kubernetes operations, deployment automation, and observability.

For a GCP platform, I would apply those principles while validating Google-specific implementation details, particularly project organization, GKE configuration, IAM, and connectivity. I’m comfortable contributing to the architecture and would work closely with GCP specialists on areas requiring deeper provider-specific expertise.”

**Prepare:** Identify the exact GCP tasks you have performed yourself. Separate production ownership from pilots, labs, and design knowledge.

[⬆ Go to top](#top)

### Q3 What is the difference between a Platform Architect and a DevOps Engineer

**Sample answer:**

“A Platform Architect defines the platform direction: deployment patterns, security boundaries, integration standards, operational responsibilities, and the roadmap. A DevOps Engineer typically implements and operates the automation, pipelines, infrastructure, and deployment workflows supporting that direction. The roles overlap.

My approach is to stay close to implementation. Architecture decisions should be validated through working reference implementations, operational testing, and feedback from application teams. Success means teams can deploy securely and reliably using clear standards, with fewer manual decisions and less repeated engineering.”

[⬆ Go to top](#top)

### Q4 How would you define the target-state architecture

**Relevant resume experience:** Truist is your strongest match: reusable AWS–Azure designs and landing-zone standards. Regeneron supports the same theme through company-wide templates and cloud guardrails. Prepare one actual architectural decision and the stakeholders involved.

**Sample answer:**

“I would begin with application requirements and the current environment: availability, latency, compliance, data location, deployment frequency, and operational capability.

Then I would define the platform layers—cloud foundations, Kubernetes, identity, networking, delivery, security, and observability—and establish ownership for each. I would produce reference architectures for common workload types, document important tradeoffs, and validate them with a pilot application.

The roadmap would prioritize the largest reliability and security gaps. At Truist, my reusable AWS and Azure platform work followed this general principle: provide consistent foundations while allowing workload-specific choices.”

[⬆ Go to top](#top)

### Q5 Tell me about a platform architecture initiative you led

**STAR outline based on your resume:**

“At Truist, the challenge was establishing consistent foundations for teams deploying across AWS and Azure. My responsibility was to develop reusable architecture patterns covering networking, identity, security, and delivery.

I created standard designs other teams could follow, supported EKS and AKS platforms, and aligned cloud governance with release controls. I also worked on reusable infrastructure templates and automated deployment workflows.

The result was a more consistent foundation for new projects. My resume records approximately a 40% reduction in release cycle time from the associated release workflow improvements while retaining auditability. The main lesson was that standards gain adoption when they make application delivery easier.”

**Confirm before speaking:** How the 40% was measured, the workflows included, your individual contribution, stakeholders, and one concrete architecture decision. Do not attribute the metric to unrelated changes.

[⬆ Go to top](#top)

### Q6 What would your first 90 days look like

**Sample answer:**

“In the first 30 days, I would understand the existing architecture, stakeholder needs, incidents, security gaps, and platform ownership. During the next 30 days, I would agree on the highest-priority improvements and develop a reference implementation with a pilot application team.

By day 90, I would aim to have a validated deployment pattern, documented architecture decisions, operational guidance, and an adoption roadmap. I would keep the scope realistic. One working pattern with clear evidence of value provides a strong foundation for expansion.”

[⬆ Go to top](#top)

## Cloud architecture and governance

### Q7 How would you design networking across AWS and GCP

**Relevant resume experience:** Use Regeneron’s shared identity and private networking for clinical/genomic workloads as your actual architecture example. AWS/GCP network implementation in the sample answer remains a proposed design unless you delivered it.

**Sample answer:**

“I would start with address planning, connectivity requirements, security boundaries, and DNS ownership. Avoiding overlapping CIDRs is important for hybrid connectivity.

In GCP, I would evaluate Shared VPC, with a host project managing shared networking and service projects containing application resources. In AWS, I would evaluate account-based VPC separation with Transit Gateway where centralized connectivity is justified.

I would define approved ingress, private service access, and egress patterns, including inspection requirements. I would test routing, name resolution, and failure behavior. The goal is consistent security and connectivity outcomes while using each provider’s networking model appropriately.”

**Follow-up — Would you route every connection through a central hub?**

“Only where requirements justify it. Centralization simplifies inspection but can introduce cost, latency, and shared dependencies. I would document approved paths and evaluate their failure boundaries.”

**Review topics:** Shared VPC host/service projects, hub-and-spoke connectivity, Private Service Connect, PrivateLink, Cloud Armor, AWS WAF, private DNS, NAT, firewall rules, and egress controls. These are related capabilities, not exact one-to-one equivalents.

[⬆ Go to top](#top)

### Q8 How would you secure application access to cloud services

**Relevant resume experience:** Connect to Truist’s AWS Organizations/SCPs, Security Hub, GuardDuty, and aligned Azure governance. The resume does not explicitly establish an IRSA or EKS Pod Identity implementation; confirm your direct involvement before claiming one.

**Sample answer:**

“I would give each workload an identity with narrowly scoped permissions and temporary credentials. Applications should not inherit broad node permissions or depend on long-lived credentials embedded in configuration.

For GKE, I would evaluate Workload Identity Federation for GKE. For EKS, I would choose between EKS Pod Identity and IRSA based on the environment and integration requirements.

I would separate identities by service and environment, review access to sensitive resources, and audit permission changes. Verification includes positive and negative tests: the application can access required resources and cannot access unrelated resources.”

**Follow-up — Is Kubernetes RBAC enough?**

“Kubernetes RBAC controls Kubernetes API access. Cloud IAM controls access to cloud services. Both are needed, with separate permissions for operators and application workloads.”

[⬆ Go to top](#top)

### Q9 What would you standardize across clouds

**Sample answer:**

“I would standardize the developer experience and control requirements: deployment inputs, environment promotion, ownership labels, telemetry, secrets handling, and security expectations.

Provider-specific implementations would sit behind clearly defined modules. Workload identity would use the appropriate AWS or GCP mechanism, while teams follow the same requirement for temporary credentials and least privilege.

I would allow native databases or messaging services when their benefits justify the dependency. The tradeoff is portability versus capability. I would document where workloads are portable and where migration requires application or data changes.”

**Follow-up — Does Kubernetes make an application fully portable?**

“It makes parts of deployment more portable. Storage, identity, networking, databases, and external dependencies can still require significant changes.”

[⬆ Go to top](#top)

### Q10 How would you choose a modernization strategy

**Sample answer:**

“I would assess business urgency, dependencies, supportability, reliability requirements, and the cost of change. Rehosting can meet a deadline when substantial application changes are impractical. Re-platforming can reduce operational effort through managed services or improved infrastructure. Re-architecture is appropriate when the existing design prevents required scaling, resilience, or delivery improvements.

I would avoid turning every migration into a rewrite. I would propose an incremental roadmap with measurable outcomes and recovery options. The decision should reflect business value and delivery risk rather than a technology preference.”

**Governance discussion points:** Least privilege, organization policies and SCPs, encryption, secrets management, security posture visibility, CIS-aligned hardening where applicable, and documented exceptions. Distinguish preventive controls from detection and remediation.

[⬆ Go to top](#top)

## Kubernetes platform engineering

### Q11 What would a standard deployment pattern include

**Relevant resume experience:** Connect to Truist’s reusable architecture patterns and infrastructure modules. The specific Helm/Argo CD template described here is illustrative; the resume lists these tools but does not document this exact implementation.

**Sample answer:**

“I would provide a reusable Helm chart or equivalent template containing resource requests and limits, health probes, service configuration, workload identity, and security settings.

It would include scaling guidance, disruption budgets, topology placement, secrets integration, and standard telemetry. Teams would supply a small set of approved configuration values. CI would build and validate the image, while GitOps reconciles approved configuration into the target cluster.

Responsibilities would be clear: the platform team owns shared capabilities, while application teams own application behavior, dependencies, and service objectives.”

[⬆ Go to top](#top)

### Q12 How would you manage multiple clusters

**Relevant resume experience:** Use Truist’s EKS and companion AKS platforms to explain consistent cross-platform standards. Do not describe GKE fleet ownership as prior production experience without a real example.

**Sample answer:**

“I would organize clusters around environment separation, regional availability, security boundaries, and operational scale. I would avoid creating a cluster for every application without a clear reason.

Each cluster would follow a versioned baseline covering identity, networking, policies, observability, and platform components. GitOps would help distribute configuration consistently. Upgrades would progress through test environments and a limited production group before wider adoption.

I would maintain ownership, inventory, capacity visibility, and compatibility checks. In GCP, I would evaluate fleets for supported multi-cluster management capabilities.”

[⬆ Go to top](#top)

### Q13 What experience do you have with internally managed Kubernetes

**Sample answer:**

“My strongest documented Kubernetes experience is with managed platforms, particularly EKS and AKS. Workload architecture, security, scaling, delivery, and observability principles transfer to internally managed Kubernetes.

An internally managed platform adds responsibility for control-plane availability, etcd protection, certificates, operating-system maintenance, and cluster lifecycle management. I would assess those capabilities, the existing distribution, and the support model before recommending changes. I would distinguish components I personally operated from those owned by another team.”

**Important:** Your uploaded resume establishes managed Kubernetes experience more clearly than self-managed control-plane ownership.

[⬆ Go to top](#top)

### Q14 How would you select a multi-cluster management approach

**Sample answer:**

“I would distinguish cluster lifecycle management from workload delivery and governance. They do not have to use the same product.

My evaluation would cover supported environments, provisioning, upgrades, policy enforcement, identity, observability, support, and cost. For a GCP-centered estate, I would evaluate GKE fleet capabilities. For internally managed platforms, I would assess the existing distribution and tooling before adding another layer.

I would run a proof of concept covering provisioning, onboarding, upgrades, and recovery. The selection should demonstrate operational value through those workflows.”

**Follow-up — What would make you reject a platform?**

“Unclear lifecycle ownership, unsupported integrations, difficult recovery, or complexity beyond the team’s capabilities.”

**Review topics:** Cluster API, GKE enterprise/fleet capabilities, EKS Anywhere, Rancher, and OpenShift. Compare what each actually manages; they are not interchangeable products. Validate current names and support before making a recommendation.

[⬆ Go to top](#top)

### Q15 How would you upgrade Kubernetes safely

**Relevant resume experience:** EKS upgrades are explicitly described at Truist and Southern Company. Add the actual upgrade you handled, compatibility issue, validation process, and division of responsibility.

**Sample answer:**

“I would inventory cluster versions, APIs, operators, networking components, storage drivers, and application dependencies. Before upgrading, I would check compatibility and deprecated APIs, then test representative workloads in a lower environment.

Production upgrades would proceed in stages with validation and stop conditions. Node replacement requires spare capacity, appropriate disruption budgets, and applications that tolerate draining.

Recovery must be defined before execution. It may involve replacing a cluster and moving workloads rather than assuming a control-plane downgrade is available. Success means applications meet their service objectives throughout the change.”

[⬆ Go to top](#top)

### Q16 How would you design capacity and scaling

**Relevant resume experience:** Use Truist’s EKS scaling work and cost/capacity forecasting, or Southern Company’s scalable EKS data processing. Supply the actual demand signal and capacity decision rather than inventing thresholds.

**Sample answer:**

“I would separate application scaling from infrastructure scaling. Application replicas respond to demand, while node capacity must support those replicas and their placement requirements.

I would establish resource requests using measurements, then test autoscaling with representative traffic. I would account for startup time, quotas, scheduling constraints, and capacity needed during deployments or failures.

Scaling policies should protect dependencies such as databases, because adding replicas can increase downstream pressure. I would validate the design through load tests and monitor latency, saturation, pending pods, and cost.”

**Follow-up — Why might pods remain Pending?**

“Capacity shortages, quotas, node selectors, taints, storage constraints, or topology requirements. I would inspect scheduling events before assuming insufficient nodes.”

[⬆ Go to top](#top)

### Q17 How would you design a resilient application

**Sample answer:**

“I would begin with availability requirements and dependency failure modes. For a replicated service, I would spread replicas across suitable nodes and zones, configure health checks, and ensure enough capacity remains during maintenance or failure.

Disruption budgets help control voluntary evictions, while deployment settings govern rollout availability. I would also review timeouts, retry behavior, dependency resilience, and data recovery.

Finally, I would test node loss and dependency failure. Resilience is demonstrated by application behavior during tests, not simply by configuration.”

**Follow-up — Does a PDB guarantee availability?**

“No. It does not prevent unexpected node or zone failure. Availability also depends on placement, spare capacity, application behavior, and dependencies.”

[⬆ Go to top](#top)

### Q18 How would you design disaster recovery

**Relevant resume experience:** Regeneron documents recovery objectives, runbooks, and automated recovery paths. Connect the design answer to that work; identify the actual recovery tests you performed before claiming recovery-drill results.

**Sample answer:**

“I would define RTO and RPO with the application owner, then identify every dependency needed to restore service. IaC and GitOps would recreate infrastructure and deployment configuration. Stateful components require backups or replication and tested restore procedures.

I would evaluate Velero where it fits Kubernetes resource and storage recovery requirements. Recovery also needs identity, secrets, certificates, registry access, networking, and traffic redirection. Self-managed clusters add control-plane and etcd recovery planning.

I would run a recovery exercise and measure results against the objectives. A successful backup is useful evidence, but a successful restore proves recoverability.”

**Definitions:** RTO is the target time to restore service. RPO is the acceptable data-loss window. Multiple clusters alone do not establish DR; storage backup behavior must be validated for the actual CSI driver and provider.

[⬆ Go to top](#top)

## Service mesh and observability

### Q19 How would you design a service mesh strategy

**Relevant resume experience:** Istio is listed in your skills. Prepare a verified implementation if available; otherwise explain your architecture approach and distinguish it from production ownership.

**Sample answer:**

“I would start with requirements that justify a mesh: service identity, encrypted communication, authorization, traffic control, or cross-service visibility.

For Istio, I would evaluate the deployment model, overhead, application compatibility, and ownership, then pilot a limited set of services. Security standards would address mutual TLS and explicit authorization. Traffic standards would cover timeouts, bounded retries, and controlled rollout routing.

I would test failure behavior because poorly configured retries can amplify an outage. Rollout planning would include performance measurements, certificate operations, monitoring, and recovery.”

**Technical distinction:** Mutual TLS encrypts and authenticates communication. Authorization policies determine which access is permitted. Avoid claiming production mesh ownership solely because Istio appears in your skills list.

[⬆ Go to top](#top)

### Q20 How would you define observability and reliability standards

**Relevant resume experience:** Truist documents reliability goals and alert/runbook improvements. Southern Company explicitly names CloudWatch and Prometheus. Explain a real alert or dashboard and the operational decision it supported.

**Sample answer:**

“I would define metrics, logs, and traces as shared platform capabilities with consistent service names, environment labels, and correlation identifiers. Dashboards would cover infrastructure health and application behavior: traffic, errors, latency, and saturation.

Alerts should identify actionable service impact and link to runbooks. I would work with application owners to define SLIs and SLOs around user journeys, then use error budgets to guide reliability work and release decisions.

My experience improving alerts, runbooks, and incident response would help connect those standards to operational outcomes.”

**Definitions:** An SLI measures service behavior; an SLO sets a target over a defined window; an SLA is an agreement, potentially with consequences. An error budget expresses the unreliability allowed by the SLO.

[⬆ Go to top](#top)

## Automation and developer experience

### Q21 How would you improve release velocity while retaining governance

**Relevant resume experience:** This answer directly matches Truist’s Azure DevOps/GitHub Actions experience. Be ready to explain release approvals, environment promotion, audit trails, and the basis for the approximately 40% improvement.

**Sample answer:**

“I would automate the standard path to production. CI would run relevant tests and security checks, build an immutable artifact, and publish it to an approved registry. Configuration would be reviewed and promoted through environments using the same artifact.

GitOps would provide reconciliation and desired-state history. Production controls would reflect risk, with appropriate approvals, health checks, progressive rollout, and recovery procedures.

At Truist, my resume records approximately a 40% reduction in release cycle time using Azure DevOps and GitHub Actions while retaining approvals and audit trails.”

[⬆ Go to top](#top)

### Q22 How would you choose between Helm Kustomize and Crossplane

**Sample answer:**

“Helm is useful for packaging configurable applications and shared deployment templates. Kustomize is useful for maintaining Kubernetes manifests with environment overlays. Crossplane addresses infrastructure provisioning through Kubernetes APIs and can support self-service abstractions.

These tools can coexist, but I would avoid unnecessary overlap. Each resource should have a clear owner, particularly when Terraform and infrastructure controllers are both present. I would prioritize maintainability, debugging, lifecycle ownership, and existing team skills.”

[⬆ Go to top](#top)

### Q23 How would you design canary deployments

**Sample answer:**

“I would define what makes a release safe before selecting the tool: health checks, error rates, latency limits, and enough traffic to evaluate the change. A canary would receive controlled traffic while its behavior is compared with the existing version. Promotion occurs only when agreed checks pass.

I would consider database compatibility, background workers, and external side effects because HTTP traffic shifting does not address every risk. The platform provides rollout mechanisms and guardrails; application teams define meaningful acceptance criteria.”

**Review topics:** Argo Rollouts or Flagger, ingress/mesh integrations, blue-green delivery, analysis windows, failure thresholds, and backward-compatible schema changes.

[⬆ Go to top](#top)

### Q24 How would you improve developer experience and drive adoption

**Relevant resume experience:** Truist’s patterns were reused by teams across the bank. Describe how adoption actually happened. An internal developer portal, specific self-service workflow, or adoption metric is not established in the resume.

**Sample answer:**

“I would treat the platform as an internal product. I would identify repeated tasks, onboarding delays, and common support requests, then build a standard path for frequent workload needs.

It would include self-service provisioning, templates, documentation, dashboards, and clear support ownership. I would pilot it with application teams and improve it using feedback. Security and operations would participate early so controls are built into the workflow.

I would measure onboarding time, deployment success, support demand, and adoption. A standard succeeds when teams can use it effectively and it improves operational outcomes.”

[⬆ Go to top](#top)

## Concrete scenario one Reusable platform pattern

**Illustrative scenario:** Standardize deployment of containerized APIs across dev, UAT, and production. This is a practice design, not a verified project history.

### Q25 Give me a concrete example of a reusable platform pattern

**Relevant resume experience:** Use Truist’s reusable platform standards and Bicep modules as the verified foundation. Present the detailed Terraform/Helm/Argo CD pattern as a proposed reference implementation unless you personally built it.

**Sample answer:**

“A good example is a standardized deployment pattern for containerized APIs. Teams configuring deployments differently can create inconsistent security and operational behavior.

My approach would combine Terraform modules for cloud foundations with a versioned Helm chart. The chart would include health probes, resource settings, workload identity, autoscaling, and monitoring. Developers supply application-specific values, CI builds and scans the image, and Argo CD deploys approved configuration through environments.

I would validate the pattern with one team before expanding adoption. Success means faster onboarding, fewer configuration defects, and consistent operations, measured against the previous process.”

| Component | Example implementation |
| --- | --- |
| Cloud foundation | Terraform modules for networking, Kubernetes, registry, and permissions |
| Application package | Versioned Helm chart with dev, UAT, and production values |
| Health checks | `/livez` for liveness and `/readyz` for readiness |
| Scaling | CPU-based HPA initially, validated through load tests |
| Security | Non-root execution, restricted permissions, workload identity, external secrets |
| Delivery | Build once; promote the same image digest |
| Observability | Common labels, metrics, structured logs, and trace correlation |

[⬆ Go to top](#top)

### Follow-up How would you handle a breaking change

“I would release a new major version, document migration, and test with a pilot application. Teams pin chart and module versions so adoption is deliberate. I would provide a migration window and retire the previous version according to support and security requirements.”

[⬆ Go to top](#top)

### Follow-up How do you avoid making the pattern too restrictive

“Separate mandatory controls from configurable defaults. Security requirements remain enforced, while teams tune resources, scaling, and application settings. Exceptions have an owner and review process.”

**Evidence to prepare:** One actual module/chart interface, release process, consumer team, onboarding example, and measurable improvement. Do not invent team counts or savings.

[⬆ Go to top](#top)

## Concrete scenario two Kubernetes incident

**Illustrative scenario:** An API returns 503 errors after deployment because a readiness probe references an obsolete endpoint.

### Q26 How would you troubleshoot this production outage

**Relevant resume experience:** Truist and Southern Company document incident-response leadership and improved runbooks. The readiness-endpoint outage here is a practice scenario, not a verified incident at either employer. Replace it with your actual incident when speaking in the past tense.

**Sample answer:**

“I would confirm customer impact, establish incident ownership, and check recent changes. I would trace the request from ingress to the Service and backend pods.

In this scenario, pods were Running but not Ready. The release changed the readiness endpoint, while Helm values referenced the old path. The probe returned 404, leaving no ready backends for normal traffic.

I would restore the previous configuration through Git and verify recovery using readiness, successful requests, and error-rate monitoring. After recovery, I would add a deployment test validating health endpoints and update the checklist. Running pods do not necessarily mean an available application.”

[⬆ Go to top](#top)

### Concrete troubleshooting commands

```bash
# Replace prod, orders-api, and pod names with the actual values.
kubectl get deployment,pods -n prod
kubectl describe pod <pod-name> -n prod
kubectl logs <pod-name> -n prod --tail=100
kubectl get service orders-api -n prod -o yaml
kubectl get endpointslices -n prod \
  -l kubernetes.io/service-name=orders-api -o yaml
kubectl rollout status deployment/orders-api -n prod
```

| Evidence | Interpretation in this example |
| --- | --- |
| Error rate increased after release | Recent configuration or application change is a candidate |
| Pods Running but not Ready | Container execution differs from traffic readiness |
| Readiness probe returns 404 | Verify path against the new application contract |
| EndpointSlices show no ready backends | Service lacks eligible normal traffic targets |
| Known-good configuration restores service | Supports the release-related hypothesis |

[⬆ Go to top](#top)

### Follow-up Why not just restart pods

“Restarting reproduces the incorrect configuration. I would correct or revert desired configuration and verify readiness and successful customer requests.”

[⬆ Go to top](#top)

### Follow-up How would you roll back with Argo CD

“I would revert the deployment change in Git and reconcile the known-good configuration. Direct Kubernetes rollback can conflict with GitOps reconciliation. Argo CD’s own rollback operation requires accounting for its restriction when automated sync is enabled.”

[⬆ Go to top](#top)

### Follow-up What would the root-cause analysis include

“The trigger, customer impact, detection and recovery timeline, why release validation missed the mismatch, and corrective actions with owners. Actions would include health-contract testing and post-deployment synthetic checks. I would verify recovery before closing the incident.”

**Important:** HTTP 503 has several possible causes. Do not conclude probe failure without checking routing, service selectors, ports, readiness, and relevant logs. This scenario has no invented recovery-time metric.

[⬆ Go to top](#top)

## Concrete scenario three Architecture tradeoff

**Illustrative scenario:** Decide between shared Kubernetes clusters and dedicated clusters for application teams.

### Q27 Describe the tradeoff and your decision framework

**Relevant resume experience:** Truist’s EKS/AKS platform work provides relevant context. The shared-versus-dedicated cluster decision is illustrative; confirm whether you made this specific decision before presenting it as delivered work.

**Sample answer:**

“Shared clusters improve utilization and reduce duplicated operations, but share a control plane, cluster-wide components, and parts of the failure boundary. Dedicated clusters provide stronger separation and independent upgrades with additional cost and maintenance.

I would evaluate compliance, workload criticality, team trust, resource consumption, and compatibility requirements. My proposed design uses shared clusters for trusted workloads with similar requirements, supported by namespace RBAC, quotas, network policies, and admission controls.

Workloads requiring stronger isolation or independent lifecycle management receive dedicated clusters. I would document the decision and revisit it as requirements change.”

| Requirement | Shared cluster | Dedicated cluster |
| --- | --- | --- |
| Trusted teams with similar requirements | Usually suitable | May add overhead |
| Strong isolation requirements | Requires careful assessment | Stronger cluster separation |
| Different Kubernetes/operator versions | Can create conflicts | Independent lifecycle |
| Cost and utilization | Better pooling potential | More duplicated capacity |
| Failure containment | Shared cluster failure boundary | Separate cluster failure boundary |
| Platform maintenance | Fewer clusters | More lifecycle work |

[⬆ Go to top](#top)

### Follow-up Are dedicated node pools equivalent to dedicated clusters

“Node pools improve placement and capacity separation but share the control plane and cluster-wide resources. I would use them for scheduling or resource needs and assess stronger isolation separately.”

[⬆ Go to top](#top)

### Follow-up How would you justify the additional cost

“Connect cost to a specific requirement such as compliance, outage containment, or independent maintenance. Compare added operating cost with the business impact of sharing that failure boundary and record the assumptions.”

[⬆ Go to top](#top)

### Follow-up What controls belong in a shared cluster

“Namespace-scoped RBAC, quotas, appropriate limits, network policies enforced by the networking implementation, workload security controls, admission policies, and restrictions on cluster-wide changes. Namespace separation alone is insufficient.”

**Decision record:** Document context, options, decision, consequences, operational owner, and conditions that would trigger reconsideration. Dedicated clusters may still share cloud accounts, networks, or external dependencies; evaluate those boundaries too.

[⬆ Go to top](#top)

## Questions to ask the vendor

- How is the platform divided between AWS, GCP, and internally managed Kubernetes?
- Is deep hands-on GCP experience mandatory from day one?
- Which Kubernetes distribution and service mesh are in use?
- Is the priority architecture definition, implementation, or improving an existing platform?
- Who owns control-plane operations, application SLOs, and recovery testing?
- How mature are platform self-service and GitOps today?
- What are the largest current reliability or developer-experience problems?
- What would successful delivery look like in the first 90 days?

[⬆ Go to top](#top)

## Final preparation checklist

- Practice the introduction in under 60 seconds.
- Prepare one real reusable platform pattern with a concrete interface and release example.
- Prepare one real incident with symptoms, evidence, diagnosis, recovery, and prevention.
- Prepare one real architecture tradeoff with alternatives and consequences.
- Identify your personal contribution versus the team’s contribution.
- Confirm the approximately 40% release-cycle metric and its measurement basis.
- Distinguish production experience from pilots, labs, and proposed designs.
- Explain AWS/GCP identity, networking, and private-access differences.
- Explain why namespaces, multiple clusters, and backups alone do not guarantee isolation or recovery.
- Be ready to discuss standards adoption, exceptions, and ownership.
- Select two or three questions for the interviewer.

[⬆ Go to top](#top)

## Official technical references

These sources informed the technical preparation. Check current provider documentation when discussing supported versions or implementing a design.

- [Google Cloud Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc)
- [Google Cloud GKE fleet management](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)
- [Google Cloud workload identity federation with Kubernetes](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-kubernetes)
- [AWS EKS workload access with service accounts](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html)
- [AWS EKS IAM best practices](https://docs.aws.amazon.com/eks/latest/best-practices/identity-and-access-management.html)
- [Kubernetes production environments](https://kubernetes.io/docs/setup/production-environment/)
- [Kubernetes multi-tenancy](https://kubernetes.io/docs/concepts/security/multi-tenancy/)
- [Kubernetes health probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/)
- [Kubernetes Service troubleshooting](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)
- [Kubernetes topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)
- [Kubernetes PodDisruptionBudgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
- [Istio security](https://istio.io/latest/docs/concepts/security/)
- [Istio observability](https://istio.io/latest/docs/concepts/observability/)
- [Argo CD automated sync](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)

Resume basis: Gabriel_O_Resume 5(1).docx, supplied for this interview preparation. No new employment history or personal achievements have been added.

[⬆ Go to top](#top)
