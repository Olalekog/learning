<a id="top"></a>

# Platform Architect Resume Connections and STAR Guide

Prepared for Olalekan Gabriel Ogundare

This companion explains how the experience in Gabriel_O_Resume 5(1).docx connects to the Platform Architect Cloud and Kubernetes job description. Each section includes a question, STAR details, a spoken answer, and follow-up preparation.

[Return to the main interview guide](Platform_Architect_Cloud_Kubernetes_Interview_Guide.md#resume-experience-matched-to-the-role)

Keep both Markdown files in the same folder when downloading them so the relative links work. You can also [open the saved main guide](https://chatgpt.com/api/library/files/libfile_a1041c553a38819183ef88323b048bc9/download).

**How to use this guide:** Resume-based stories summarize documented work, without inventing project names, team counts, incident causes, or measured recovery figures. Confirm the detailed implementation and your personal contribution. GCP is presented as moderate experience. The service-mesh and self-managed Kubernetes section is explicitly hypothetical. Spoken answers target approximately 45–60 seconds; use the supporting details for follow-ups.

## Index

1. [Target-state architecture and reusable patterns](#1-target-state-architecture-and-reusable-patterns)
2. [Enterprise Kubernetes](#2-enterprise-kubernetes)
3. [Cloud networking and identity](#3-cloud-networking-and-identity)
4. [Security and governance](#4-security-and-governance)
5. [Infrastructure automation](#5-infrastructure-automation)
6. [CI/CD and auditability](#6-cicd-and-auditability)
7. [Observability and incident response](#7-observability-and-incident-response)
8. [Recovery and availability](#8-recovery-and-availability)
9. [Modernization and specialist workloads](#9-modernization-and-specialist-workloads)
10. [Cross-team platform adoption](#10-cross-team-platform-adoption)
11. [GCP](#11-gcp)
12. [Service mesh and internally managed Kubernetes](#12-service-mesh-and-internally-managed-kubernetes)
13. [Evidence to prepare before the interview](#evidence-to-prepare-before-the-interview)

## 1 Target-state architecture and reusable patterns

**Question:** Tell me about a time you defined reusable platform architecture for multiple teams.

**Experience:** Truist — AWS–Azure platform patterns.

- **Situation:** Application teams needed consistent foundations for projects across AWS and Azure.
- **Task:** Define reusable designs for networking, identity, security, and delivery.
- **Action:** Created standard multi-cloud designs and patterns other teams followed for new projects; aligned these with governance and deployment workflows.
- **Result:** Teams across the bank could use common platform foundations. The resume does not state an adoption count or quantified onboarding improvement.

**Spoken answer:**

“At Truist, I developed standard designs for how teams use AWS and Azure together. My responsibility was to make networking, identity, security, and CI/CD patterns repeatable across projects. I created reusable architecture foundations that other teams followed, rather than having every project make those decisions independently. That experience relates directly to this role’s reference-architecture and governance responsibilities. The result was a common foundation teams could build on. In a deeper discussion, I would explain one specific pattern, the requirement behind it, and how a consuming team used it.”

**Follow-up:** What was standardized, and what could teams change?

**Answer approach:** Explain an actual pattern’s mandatory controls and configurable inputs. Identify the consuming team, interface, versioning, and exception process you actually used.

[⬆ Go to top](#top)

## 2 Enterprise Kubernetes

**Question:** Describe your role in building and evolving enterprise Kubernetes platforms.

**Experience:** Truist — EKS and companion AKS platforms; Southern Company — EKS data processing.

- **Situation:** Containerized workloads required scalable and secure platforms with reliable operations.
- **Task:** Manage Kubernetes capabilities and lifecycle activities supporting those workloads.
- **Action:** Worked on EKS scaling, upgrades, security hardening, and monitoring; supported companion AKS platforms at Truist and EKS data-processing workloads at Southern Company.
- **Result:** Supported the operating foundations for cloud-hosted container workloads; specific upgrade outcomes or availability figures need your confirmation.

**Spoken answer:**

“At Truist, my Kubernetes work included EKS scaling, upgrades, security hardening, and monitoring, alongside AKS platforms. At Southern Company, I also worked with EKS supporting scalable data processing. My responsibility connected platform lifecycle decisions with application requirements. I focused on the capabilities needed to operate those environments consistently, including capacity, security, and visibility. This fits the role’s responsibility for evolving enterprise Kubernetes platforms. I would support the answer with one upgrade or scaling example and explain which parts I owned versus those managed by other teams.”

**Follow-up:** What was the most difficult upgrade issue?

**Prepare:** Actual cluster version transition, compatibility concern, testing, maintenance approach, and observed result. Do not substitute a hypothetical issue for your real experience.

[⬆ Go to top](#top)

## 3 Cloud networking and identity

**Question:** Tell me about designing secure connectivity for sensitive workloads.

**Experience:** Regeneron — clinical and genomic research across AWS and Azure.

- **Situation:** Research platforms needed secure data movement and access across clouds under GxP requirements.
- **Task:** Design shared identity, private networking, and consistent delivery foundations.
- **Action:** Designed the cross-cloud architecture and aligned access and deployment patterns with research and governance needs.
- **Result:** Supported secure cloud integration for research workloads while preserving required controls.

**Spoken answer:**

“At Regeneron, I designed how research workloads would use AWS and Azure together. Clinical and genomic data required secure access and connectivity under GxP requirements. My responsibility covered shared identity, private networking, and consistent CI/CD. I designed those foundations so research teams could work across clouds without creating separate, inconsistent access and deployment models. This maps directly to enterprise networking and identity architecture. My strongest implementation experience is AWS and Azure; for GCP, I would apply those principles while validating its provider-specific networking and IAM mechanisms.”

**Follow-up:** Which private connectivity and identity mechanisms did you implement?

**Prepare:** Actual services, trust relationships, DNS ownership, routing, access scope, and data boundaries. The resume does not specify every implementation component.

[⬆ Go to top](#top)

## 4 Security and governance

**Question:** Give an example of establishing cloud guardrails at enterprise scale.

**Experience:** Truist — AWS and Azure governance.

- **Situation:** A multi-cloud environment required consistent security standards and risk visibility.
- **Task:** Establish controls and operational mechanisms across both clouds.
- **Action:** Used AWS Organizations/SCPs, Security Hub, GuardDuty, and automated checks and fixes; applied Azure Policy, Sentinel, and Defender for Cloud to align governance.
- **Result:** Improved the security posture and supported consistent standards across clouds; specific finding reductions are not supplied.

**Spoken answer:**

“At Truist, I worked on AWS security at scale using Organizations and SCPs, Security Hub, GuardDuty, and automated checks and remediation. I also applied Azure Policy, Sentinel, and Defender for Cloud to align governance across the environment. My responsibility was to connect controls with operational visibility and corrective action. This relates directly to defining secure platform standards. I would explain an actual guardrail by separating what prevented an action, what detected a problem, and who owned remediation. The outcome was a more consistent security foundation across clouds.”

**Follow-up:** How did you prevent guardrails from disrupting applications?

**Answer approach:** Describe your actual testing, rollout, exception handling, and review process. Do not claim that every control automatically remediated every finding.

[⬆ Go to top](#top)

## 5 Infrastructure automation

**Question:** Describe reusable infrastructure automation you developed.

**Experience:** Truist — Bicep modules and landing-zone templates; Regeneron — Terraform and Bicep integration.

- **Situation:** Infrastructure needed consistent provisioning and maintainable deployment code.
- **Task:** Develop reusable infrastructure definitions and integrate them with delivery workflows.
- **Action:** Authored modular Bicep templates at Truist, replaced complex ARM templates, and combined Bicep with Terraform at Regeneron.
- **Result:** Standardized Azure infrastructure deployment and supported repeatable cloud provisioning.

**Spoken answer:**

“At Truist, I authored reusable Bicep modules and templates to standardize Azure landing zones, naming, governance, and security baselines. I also improved infrastructure code by replacing complex ARM templates with modular Bicep integrated into delivery pipelines. At Regeneron, I used Bicep alongside Terraform for cloud provisioning. This connects to the role’s emphasis on repeatable platform automation. I would explain a module I personally owned, its inputs and outputs, how it was validated, and how changes reached consuming teams.”

**Follow-up:** How did you manage ownership between Terraform and Bicep?

**Prepare:** Actual resource boundaries, repositories, deployment sequence, state ownership, validation, and release practices. The resume does not establish a particular testing tool or module registry.

[⬆ Go to top](#top)

## 6 CICD and auditability

**Question:** Tell me about improving delivery speed while preserving governance.

**Experience:** Truist — Azure DevOps and GitHub Actions.

- **Situation:** Application and infrastructure delivery needed faster release cycles with retained regulatory auditability.
- **Task:** Improve release workflows while maintaining approvals and environment controls.
- **Action:** Used Azure DevOps and GitHub Actions to manage releases, approvals, and environments.
- **Result:** Approximately 40% shorter release cycle time is recorded in your resume, with audit trails retained.

**Spoken answer:**

“At Truist, I worked on improving application and infrastructure release workflows using Azure DevOps and GitHub Actions. We needed faster delivery while retaining approvals and auditability. My work involved managing release workflows, environments, and controls so deployments were more repeatable. My resume records approximately a 40% reduction in release cycle time while retaining audit trails. This is directly relevant to improving release velocity without sacrificing stability. I would explain the actual stages that changed, the measurement baseline, and my personal contribution.”

**Follow-up:** How was the 40% calculated?

**Prepare:** Before-and-after cycle times, measurement period, workflow scope, and data source. Confirm these details before presenting the percentage as measured evidence.

[⬆ Go to top](#top)

## 7 Observability and incident response

**Question:** Describe how you improved platform reliability through incident response.

**Experience:** Truist and Southern Company.

- **Situation:** Major outages and pipeline/connectivity incidents required coordinated recovery and operational improvement.
- **Task:** Lead response and improve detection, runbooks, and recovery mechanisms.
- **Action:** Coordinated cross-team recovery, improved alerts/runbooks/automation, and tracked reliability goals at Truist; used CloudWatch and Prometheus in Southern Company’s EKS environment.
- **Result:** Improved recovery capability and reduced recovery time as described in the resume; no exact MTTR figure is supplied.

**Spoken answer:**

“At Truist, I led responses to major outages and coordinated recovery across teams. I also improved alerts, runbooks, and automation and tracked reliability goals such as uptime and response time. At Southern Company, I worked with CloudWatch and Prometheus and responded to data-pipeline and connectivity incidents. This experience connects observability to operational decisions rather than dashboards alone. For the interview, I would walk through an actual incident, the evidence we used, the recovery decision, and the improvement that followed.”

**Follow-up:** What was the root cause and how did you verify recovery?

**Prepare:** One real incident timeline, customer impact, signals, diagnosis, action, and verification. The readiness-probe outage in the main guide is illustrative and must not be attributed to these employers without evidence.

[⬆ Go to top](#top)

## 8 Recovery and availability

**Question:** Tell me about improving recovery for a critical platform.

**Experience:** Regeneron research pipelines.

- **Situation:** Research pipelines needed clear recovery behavior during high-impact failures.
- **Task:** Improve recovery planning and operational repeatability.
- **Action:** Defined recovery objectives, wrote runbooks, and automated common recovery paths.
- **Result:** Shortened downtime during high-impact incidents, as described in the resume.

**Spoken answer:**

“At Regeneron, I improved reliability for critical research pipelines by defining recovery objectives, developing runbooks, and automating common failure-recovery paths. My responsibility was to make restoration more predictable for the teams supporting those workflows. The improvements shortened downtime during high-impact incidents. This relates directly to platform availability and disaster-recovery planning. I would explain the dependencies involved and the recovery checks I actually performed, using measured RTO or RPO only where I have supporting evidence.”

**Follow-up:** Did you conduct recovery drills?

**Answer approach:** State the exercises or tests you actually performed. Recovery drills, Velero usage, and specific measured RTO/RPO results are not established in this resume.

[⬆ Go to top](#top)

## 9 Modernization and specialist workloads

**Question:** Describe adapting platform architecture to data or AI workloads.

**Experience:** Regeneron research analytics and Truist operational workflows.

- **Situation:** Specialist workloads needed secure data preparation, model deployment, and operational integration.
- **Task:** Build cloud foundations and pipelines that met those workload needs.
- **Action:** Used SageMaker, Azure Databricks, and end-to-end ML pipelines at Regeneron; built cost/capacity forecasting pipelines and internal Azure OpenAI workflows at Truist.
- **Result:** Supported research analytics and internal operational use cases with access controls.

**Spoken answer:**

“At Regeneron, I worked on research workloads using SageMaker for model training, deployment, and monitoring, with Azure Databricks supporting data preparation. I also built end-to-end ML pipelines. At Truist, I worked on cost and capacity forecasting and internal Azure OpenAI workflows. These experiences show how platform architecture must support workload-specific requirements while retaining shared controls. For this role, I would bring that judgment to modernization, particularly around data access, deployment, monitoring, and operational ownership.”

**Follow-up:** What was your role versus the data-science team’s role?

**Prepare:** Your exact platform/pipeline responsibilities, access controls, deployment workflow, and operational checks. Avoid claiming model accuracy or cost savings that are not documented.

[⬆ Go to top](#top)

## 10 Cross-team platform adoption

**Question:** Tell me about getting other teams to use common architecture standards.

**Experience:** Truist reusable patterns and Regeneron company-wide templates.

- **Situation:** Multiple teams needed common cloud foundations for new projects.
- **Task:** Establish reusable designs and standards that could be consumed beyond an individual project.
- **Action:** Defined patterns used by other teams at Truist and company-wide cloud rules/templates at Regeneron.
- **Result:** Supported consistent starting points and standards across projects; adoption counts and a particular pilot process are not documented.

**Spoken answer:**

“At Truist, I developed reusable AWS and Azure patterns that other teams across the bank followed for new projects. At Regeneron, I established company-wide cloud rules and templates. My responsibility was to make platform standards reusable beyond an individual deployment. This matches the role’s emphasis on collaboration and adoption. In the interview, I would explain one consuming team, its requirements, how we aligned the design, and the actual feedback or outcome. I would avoid inventing team counts or describing an adoption process I did not use.”

**Follow-up:** How did you handle resistance?

**Prepare:** A real objection, your response, and the decision. If discussing a proposed approach, say you would clarify requirements, validate the standard, and agree on improvements or a documented exception.

[⬆ Go to top](#top)

## 11 GCP

**Question:** Give an example of your GCP experience and explain how it prepares you for this role.

**Experience:** Alteryx pilot; moderate GCP skills.

- **Situation:** Your resume describes early cloud experiments and a small GCP application pilot.
- **Task:** Build and monitor a small application using GCP capabilities.
- **Action:** Used Compute Engine and Cloud Storage for the pilot.
- **Result:** Established foundational GCP exposure; this does not establish enterprise GKE or production fleet ownership.

**Spoken answer:**

“My GCP experience is moderate. My resume includes an Alteryx pilot where I built and monitored a small application using Compute Engine and Cloud Storage. That gave me foundational exposure, while my deeper production experience developed in AWS and Azure. For this role, I bring transferable architecture knowledge in networking, identity, Kubernetes, automation, and reliability. I would be clear about the GCP tasks I personally performed and validate provider-specific implementation details rather than present AWS experience as equivalent GCP ownership.”

**Follow-up:** Have you operated enterprise GKE clusters?

**Answer approach:** Answer based on actual experience. A GKE skill listing or general Kubernetes knowledge is not evidence of enterprise production ownership.

[⬆ Go to top](#top)

## 12 Service mesh and internally managed Kubernetes

**Question:** How would you lead a service-mesh initiative on internally managed Kubernetes?

**Hypothetical STAR design exercise:** Istio appears in your skills, but this resume does not establish a specific production mesh rollout or self-managed control-plane ownership.

- **Situation:** An internally managed platform needs consistent service communication security and traffic visibility.
- **Task:** Assess whether a mesh addresses those requirements and establish an operable adoption approach.
- **Action:** Propose a limited pilot, define workload identity and authorization requirements, evaluate overhead and compatibility, and agree on certificate, upgrade, and incident ownership.
- **Result:** The intended result is a tested architecture and rollout decision supported by evidence. This is an acceptance goal, not a delivered personal achievement.

**Spoken answer:**

“My strongest documented Kubernetes experience is EKS and AKS, and Istio is included in my skills. I would distinguish that from ownership of a production service mesh or self-managed control plane. For this initiative, I would establish the requirements, assess the existing platform and operational ownership, and pilot a limited set of services. I would evaluate security, traffic behavior, performance, and recovery before recommending wider adoption. Success would be a tested design with clear ownership and measurable acceptance criteria.”

**Follow-up:** Which responsibilities change with self-managed Kubernetes?

**Answer approach:** Discuss control-plane availability, etcd protection, certificates, operating systems, and lifecycle responsibilities as design knowledge unless you personally owned those components.

[⬆ Go to top](#top)

## Evidence to prepare before the interview

For each resume-based answer, prepare the actual project context, your responsibility, one design decision, one implementation detail, and the observed result. For metrics, identify the baseline and measurement source. Replace hypothetical scenarios with actual events before presenting them as past achievements.

[Return to the main interview guide](Platform_Architect_Cloud_Kubernetes_Interview_Guide.md#resume-experience-matched-to-the-role)

[⬆ Go to top](#top)
