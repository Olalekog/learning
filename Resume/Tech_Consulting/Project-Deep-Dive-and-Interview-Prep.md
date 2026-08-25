<a id="top"></a>

# Gabriel O — Project Deep Dives & Interview Prep

Detailed explanations for every project on the resume, plus dedicated
troubleshooting, performance, scaling, and high-availability sections
tied directly back to that work, and interview questions built to probe
it. Companion to [Elevator-Pitch.md](Elevator-Pitch.md) in this folder.

## Table of Contents

1. [Overview](#overview)
2. [Project Deep Dives](#project-deep-dives)
3. [Troubleshooting](#troubleshooting)
4. [Performance](#performance)
5. [Scaling](#scaling)
6. [High Availability](#high-availability)
7. [Interview Questions](#interview-questions)
8. [Most Important Concepts to Know First](#most-important-concepts-to-know-first)

---

## Overview

Every project on this resume shares one architectural thread: **AWS and
Azure operated together, deliberately, not as a fallback for either
one** — shared identity, shared network patterns, dual EKS/AKS
platforms, and a unified security posture across both clouds' native
tooling. The seven roles below span six industries (banking,
pharmaceuticals, energy, automotive, retail, insurance) plus a
foundational IT role, each adding a layer: **Alteryx** built the base
skills, **Liberty Mutual** and **TJ Maxx** established the first
repeatable Azure patterns, **Rivian** and **Southern Company** extended
that into dual-cloud Kubernetes and OT/IoT-scale data, **Regeneron**
added regulated-data (GxP) rigor, and **Truist Bank** is the current
synthesis of all of it in a banking-regulated environment.

[⬆ Back to top](#top)

---

## Project Deep Dives

### Truist Bank — Senior Multi-Cloud DevOps & Security Engineer (Jan 2024–Present, Banking)

**Context**: A regulated bank running both AWS and Azure needed
consistent, bank-wide patterns instead of every team inventing its own
networking/security/CI-CD approach per cloud.

**What was built**: Reusable AWS+Azure landing zone patterns
(networking, identity, security, CI/CD) that other teams adopted for
new projects bank-wide; EKS clusters (scaling, upgrades, hardening,
monitoring) running alongside companion AKS clusters so teams could
choose the right platform per workload; organization-wide AWS security
(Organizations + SCPs, Security Hub, GuardDuty) with automated
checks/remediation; Azure security and governance (Sentinel, Defender
for Cloud, Azure Policy) unified with the AWS side into a single risk
view; Azure DevOps + GitHub Actions release management cutting cycle
time ~40% while preserving audit trails for regulators; AI/ML pipelines
for cost/capacity forecasting, plus Azure OpenAI integrated so teams
could query logs and get recommendations in natural language.

**Key technical decisions**: Running EKS *and* AKS side by side (not
picking one) avoids single-cloud lock-in and gives workload placement
flexibility; pairing AWS SCPs with Azure Policy is defense-in-depth
across both clouds rather than securing one and hoping the other stays
consistent; automated remediation is what makes org-wide policy
actually hold at a bank's account/subscription sprawl scale, where
manual review can't keep up.

**Impact**: ~40% faster release cycles, unified risk visibility across
both clouds, quarter-over-quarter reliability improvement from
systematic incident response.

### Regeneron Pharmaceuticals — Cloud Data & DevOps Architect (Jul 2022–Dec 2023, Pharma)

**Context**: A research platform moving clinical and genomic data
between AWS and Azure, constrained by **GxP** — shorthand for the
family of regulatory frameworks (Good Clinical Practice, Good
Laboratory Practice, Good Manufacturing Practice) governing data
integrity, traceability, and validated environments in pharma/clinical
research.

**What was built**: Shared identity and private networking so data
moved securely between clouds without breaking GxP controls; AWS
SageMaker for training/deploying/monitoring production ML models on
research analytics; Azure Databricks for large-scale data preparation
and feature engineering; end-to-end AI/ML pipelines (prep → train →
deploy → monitor); Azure OpenAI integrated into internal tools so
scientists could explore results conversationally under strict access
controls; company-wide Landing Zones/Azure Policy plus AWS Organizations
guardrails so every new research project started from the same secure
baseline; defined recovery objectives, runbooks, and automated failure
recovery for critical research pipelines.

**Key technical decisions**: GxP compliance is what actually drives the
architecture here — every design choice (shared identity, private
networking, validated baselines) exists to prove data integrity and
traceability to an auditor, not just to make the system work. Splitting
SageMaker (train/deploy/monitor) from Databricks (large-scale prep/
feature engineering) matches each tool to the pipeline stage it's
actually built for, rather than forcing one platform to do both.
Conversational access to research results needed strict access controls
specifically because the underlying data is both regulated *and*
commercially sensitive (unpublished research IP).

**Impact**: shortened downtime during several high-impact incidents;
secure cross-cloud data movement that never broke compliance controls.

### Southern Company — Multi-Cloud DevOps & Data Specialist (May 2020–Jun 2022, Energy)

**Context**: An energy utility running OT (operational technology)
analytics — the kind of environment where connectivity and data-pipeline
reliability have real operational consequences, not just user-facing
downtime.

**What was built**: Azure for OT-related analytics with selected
workloads kept on AWS, with reusable networking/identity/security/CI-CD
patterns other teams followed; EKS clusters for scalable data
processing (node scaling, upgrades, hardening, monitoring via CloudWatch
and Prometheus); org-wide AWS security with automated remediation;
Azure DevOps for reviewable, auditable infrastructure and data-pipeline
changes; unified Azure+AWS security controls; incident response for
data-pipeline and connectivity outages, with recovery time reduced
through better alerts, runbooks, and automated recovery steps.

**Key technical decisions**: Splitting OT analytics onto Azure while
keeping specific workloads on AWS is a deliberate best-tool-per-workload
choice rather than a full migration in either direction — a pattern worth
being able to justify specifically (which workload characteristics drove
which cloud). Utility/energy environments carry real audit-trail and
change-control weight (adjacent to frameworks like NERC CIP even where
not explicitly named), which is why reviewable/auditable pipeline
changes are called out specifically here.

**Impact**: reduced recovery time for major data-pipeline/connectivity
outages through systematically improved alerting and automation.

### Rivian Automotive — Cloud DevOps Engineer, Multi-Cloud Platform (Mar 2018–Apr 2020, Automotive)

**Context**: An EV manufacturer needing reusable patterns for vehicle
telemetry, over-the-air (OTA) update services, and factory systems —
workloads where a bad software rollout doesn't just cause an outage, it
reaches physical vehicles.

**What was built**: Reusable AWS+Azure patterns for vehicle telemetry/
OTA/factory systems so new product teams launched already
security-and-reliability-compliant; EKS and AKS clusters side by side
with full observability (CloudWatch, Azure Monitor, Prometheus,
Grafana); SageMaker for predictive-maintenance and quality-insight
models from vehicle and factory data; Azure Landing Zones + AWS
Organizations templates for a consistent new-service baseline; Azure
DevOps/GitHub Actions managing **blue-green and canary** progressive
delivery for vehicle software with clear approval/promotion paths;
reliability driven by explicit uptime/latency goals, incident bridges,
and automated remediation.

**Key technical decisions**: Blue-green/canary specifically (not a
simple rolling update) for vehicle software is a direct response to the
stakes of OTA updates reaching real vehicles — you need to validate a
release against real traffic on a small slice before it reaches every
car, with a fast, safe rollback path if something's wrong. Running the
*same* observability stack (Prometheus/Grafana) across both clouds'
native tooling (CloudWatch/Azure Monitor) gives one unified dashboard
view instead of two disconnected ones per cloud.

**Impact**: predictive maintenance improved quality insights from
vehicle/factory data; reduced recovery time through better alerting and
automated remediation.

### TJ Maxx — Azure / Multi-Cloud DevOps Engineer (Jan 2016–Feb 2018, Retail)

**Context**: Retail and e-commerce with a hard, narrow, revenue-critical
peak — holiday shopping traffic — where the system either survives the
spike or it doesn't.

**What was built**: Early multi-cloud patterns (Azure as primary, select
AWS services alongside) with shared identity/networking/deployment
standards; Azure DevOps release management for store and digital
applications enabling frequent, controlled releases that survived peak
holiday traffic; early Security Center/Defender-era governance and
policy; AI/ML pipelines for inventory and demand-signal forecasting,
plus early experimentation with Azure cognitive services; incident
response during major peak retail events, with each subsequent event
causing less disruption as alerts/runbooks improved iteratively.

**Key technical decisions**: Azure-primary reflects a common retail
pattern of that era (existing Windows/on-prem estate migrating to
Azure first); the real engineering discipline here is treating peak
readiness as a *recurring, measured* problem — each holiday event's
incidents directly fed the next event's alert/runbook improvements,
rather than treating each peak as a one-off fire drill.

**Impact**: releases survived peak holiday traffic; measurably less
disruption at each subsequent peak event.

### Liberty Mutual — Cloud Infrastructure & DevOps Engineer (Jan 2014–Dec 2015, Insurance)

**Context**: Early-stage Azure adoption for claims and policy
applications handling sensitive insurance data, before "Landing Zone" was
even a formalized industry pattern.

**What was built**: Some of the first company-wide Azure patterns (early
Landing Zone concepts and policy) so new claims/policy applications
followed the same security and networking standards from the start;
release/approval/environment management using the era's Azure DevOps
tooling; identity, Key Vault, and network isolation protecting sensitive
insurance data while still enabling secure dev/ops access; monitoring
and documented recovery steps supporting reliability goals for critical
platforms.

**Key technical decisions**: Being early to a pattern (before it had a
name) meant establishing conventions from first principles rather than
following an existing playbook — a genuinely different skill than
applying an already-standardized Landing Zone template today, worth
distinguishing in an interview if asked to compare this era of work to
the later, more mature Landing Zone rollouts at Rivian/Regeneron/Truist.

**Impact**: established a repeatable, secure baseline that every new
claims/policy application could start from.

### Alteryx — IT Systems Administrator (2012–2014, IT Services)

**Context**: The foundational role — internal systems support alongside
early, exploratory cloud work on both AWS and Azure.

**What was built**: Support for internal systems plus early cloud
experiments across AWS and Azure, building the foundational identity,
networking, automation, and monitoring skills everything since has
scaled from; routine administration automated with PowerShell and Bash;
incident response participation, learning the value of clear runbooks
and fast recovery early; a small pilot application on Google Cloud
(Compute Engine/Cloud Storage), the source of the "moderate" GCP
experience noted in the skills section.

**Impact**: the base every later multi-cloud architecture role compounds
on. It's the least glamorous role on the resume, but the one an
interviewer asking "how did you get started" should hear about
specifically, since it grounds the "12+ years of AWS+Azure" claim in an
actual beginning rather than implying it started fully formed.

[⬆ Back to top](#top)

---

## Troubleshooting

| Domain | Where It Shows Up | Approach |
|---|---|---|
| **EKS/AKS cluster issues** | Every role from Rivian onward runs dual EKS+AKS | Start with `kubectl describe` on the failing Pod/node — Events almost always name the exact cause (insufficient capacity, failed image pull, node NotReady). Cross-cloud, the *symptoms* look identical even though the underlying node-provisioning mechanism differs (EKS managed node groups/Karpenter vs. AKS node pools) — diagnose at the Kubernetes API level first, drop to the cloud-specific node layer only once the Pod-level cause is ruled out. |
| **Multi-cloud connectivity/networking outages** | Explicitly named at Southern Company ("data-pipeline and connectivity outages") | Isolate which side of the cross-cloud link failed first — check the AWS side (Transit Gateway/VPN/Direct Connect route tables, security groups) and the Azure side (VNet peering/ExpressRoute, NSGs) independently before assuming the failure is symmetric; a one-sided route table or NSG change is a far more common root cause than a genuine cross-cloud link outage. |
| **CI/CD pipeline/release failures** | Azure DevOps + GitHub Actions used consistently across every role | Check the specific stage that failed (build vs. approval gate vs. deploy) — a release that fails at an approval gate is a process/authorization issue, not a technical one; a deploy-stage failure needs the actual target-environment logs, not just the pipeline's own output. |
| **Security policy drift / automated remediation false positives** | Organizations SCPs + Azure Policy with "automatic checks and fixes" at Truist, Southern Company, Regeneron | Automated remediation that fires on a legitimate, intentional configuration looks identical in the audit log to one that caught a real drift — always check *why* the policy triggered (what changed, and was that change authorized) before assuming either "the policy is wrong" or "this was definitely a real incident." |
| **AI/ML pipeline issues** | SageMaker + Azure Databricks + Azure OpenAI end-to-end pipelines at Regeneron, Rivian, Truist | Split the diagnosis by pipeline stage: a data-prep failure (Databricks) looks completely different from a training failure (SageMaker job logs, resource errors) or an inference-time issue (endpoint latency/errors) — don't debug the whole pipeline as one unit; isolate which stage actually failed first. |

[⬆ Back to top](#top)

---

## Performance

| Area | What to Tune | How to Check | How to Improve |
|---|---|---|---|
| **EKS/AKS workload performance** | Pod resource requests/limits, node instance sizing | `kubectl top pods/nodes`; CloudWatch Container Insights / Azure Monitor Container Insights for sustained CPU/memory pressure | Right-size requests based on actual observed usage, not guesses; separate node pools by workload profile (e.g., ML training vs. general services) so one workload type doesn't starve another. |
| **CI/CD pipeline throughput** | Build/test stage duration, parallelization | Azure DevOps/GitHub Actions run-time analytics per stage | Parallelize independent test suites, cache dependencies between runs, and move genuinely slow integration tests to a separate, less-frequently-triggered stage rather than blocking every commit. |
| **Cross-cloud network latency** | Transit Gateway/VPN/Direct Connect (AWS) and VNet peering/ExpressRoute (Azure) path | Network Watcher (Azure) / VPC Flow Logs + Reachability Analyzer (AWS) for hop-by-hop latency | Prefer a dedicated link (Direct Connect + ExpressRoute) over public-internet VPN for any latency-sensitive cross-cloud traffic; co-locate frequently-communicating services in the same region on both clouds rather than spreading them arbitrarily. |
| **ML pipeline performance** | SageMaker training instance type/count, Databricks cluster sizing | SageMaker training job metrics (GPU/CPU utilization); Databricks cluster utilization dashboards | Low GPU utilization during training usually means a data-loading bottleneck, not a compute one — fix the pipeline feeding the model before reaching for a bigger instance. |

[⬆ Back to top](#top)

---

## Scaling

| Area | How It Scales | Notes From This Resume's Work |
|---|---|---|
| **EKS/AKS node scaling** | Cluster Autoscaler / Karpenter (AWS), cluster autoscaler / node pool scaling (Azure); HPA for pod-level scaling on both | Running dual clusters (Rivian, Truist) means scaling policy has to be defined and tuned *twice*, once per cloud — a common interview trap is describing scaling as if it's one unified mechanism across both. |
| **CI/CD scaling for a growing org** | Reusable pipeline templates and Landing Zone patterns adopted org-wide (Truist, Regeneron, Rivian) | The actual scaling lever here isn't infrastructure capacity, it's *process reuse* — a standardized pattern that every new team adopts scales far better than each team building its own pipeline from scratch. |
| **Multi-region/multi-cloud scaling** | Workload placement decisions per region/cloud based on data residency, latency, and cost | Regeneron's GxP-constrained data movement and Southern Company's OT-vs-general-workload split are both examples of *deliberate* placement decisions, not "scale everywhere identically." |
| **Database scaling** | Managed relational/NoSQL scaling (RDS/Aurora, Azure SQL Database) — read replicas, vertical scaling | Not the primary focus of this resume's roles, but relevant wherever the AI/ML pipelines' feature stores or application backends sit — know the standard read-replica/vertical-scaling levers if asked directly. |

[⬆ Back to top](#top)

---

## High Availability

| Concept | Definition | Where It Applies Here |
|---|---|---|
| **Multi-AZ (within one cloud)** | Redundancy across physically separate datacenters in one region, protecting against a single-datacenter failure | The baseline HA layer under every EKS/AKS cluster on this resume — node groups/pools spread across AZs. |
| **Cross-Cloud Disaster Recovery** | Explicitly listed in the skills section — using AWS *and* Azure as failover targets for each other, not just multi-region within one cloud | The most advanced HA pattern on this resume; be ready to describe a concrete scenario (e.g., a critical service's control plane failing over from EKS to AKS, or vice versa) rather than only naming it abstractly. |
| **Progressive delivery as an HA safety mechanism** | Blue-green/canary rollouts (Rivian) limit the blast radius of a bad release *before* it becomes an availability incident | Distinguish this from traditional HA (which protects against infrastructure failure) — progressive delivery protects against a *bad deployment* becoming an outage, a different failure mode with a different mitigation. |
| **RTO / RPO** | Recovery Time Objective (how long can it be down) / Recovery Point Objective (how much data loss is acceptable) | Explicitly referenced at Regeneron ("defined recovery objectives") — know these as the two numbers that actually drive which DR strategy (backup/restore vs. pilot light vs. warm standby vs. active-active) is appropriate, rather than defaulting to the most expensive option everywhere. |
| **Automated recovery / self-healing** | Runbooks and automation that remediate a known failure mode without waiting on a human | The consistent thread across every role's reliability work — from Alteryx's early "clear runbooks and fast recovery" lesson through Truist's current automated remediation. |

[⬆ Back to top](#top)

---

## Interview Questions

### Project-Specific

**1. Walk me through how you designed the multi-cloud landing zone pattern at Truist Bank.**
Answer shape: start from the requirement (consistent networking/identity/security/CI-CD across AWS and Azure for a regulated bank), describe the reusable pattern itself (Organizations/SCPs paired with Azure Policy, EKS alongside AKS), and close with how you made it *adopted* org-wide, not just designed — templates other teams could actually pull and use, not a document nobody followed.

**2. How did you keep GxP compliance intact while moving clinical/genomic data between AWS and Azure at Regeneron?**
Answer shape: shared identity and private networking so data never touched a public path, validated baselines from Landing Zones/Azure Policy and AWS Organizations guardrails so every environment started compliant rather than being audited into compliance after the fact, and unified Sentinel/Defender/Security Hub visibility so a compliance gap on either cloud would actually surface.

**3. Why blue-green and canary specifically for Rivian's vehicle software, instead of a standard rolling update?**
A bad rollout reaches physical vehicles, not just a web server — canary lets you validate a release against a small slice of real traffic first, and blue-green gives an instant, complete rollback path if something's wrong, both of which a rolling update can't offer at the same safety margin.

**4. How did TJ Maxx's platform actually survive peak holiday traffic — what changed year over year?**
Answer shape: frame it as an iterative process, not a one-time fix — each peak event's incidents fed directly into the next event's alerting and runbook improvements, so the measurable claim is "less disruption each subsequent event," not "zero incidents ever."

### Technical / Cross-Cutting

**5. What's the actual difference in how EKS and AKS handle node scaling, and why run both instead of standardizing on one?**
They use different underlying mechanisms (Karpenter/Cluster Autoscaler on EKS vs. AKS's own node pool autoscaling) and need separately tuned policies — running both isn't about hedging, it's giving each workload the platform best suited to it while keeping a consistent Kubernetes API surface for the teams building on top.

**6. How do AWS SCPs and Azure Policy actually complement each other rather than duplicate effort?**
SCPs set hard boundaries at the AWS Organization level (what's *possible*, even for an account admin); Azure Policy audits/enforces configuration compliance within Azure. Used together across a multi-cloud estate, they close the same class of gap (unauthorized or non-compliant configuration) on each cloud's own terms, feeding into one unified risk view rather than each cloud being secured in isolation.

**7. When would you use SageMaker versus Azure Databricks in the same pipeline?**
Databricks for large-scale data preparation and feature engineering (its Spark-native strength); SageMaker for the actual model training, deployment, and production monitoring — matching each tool to the pipeline stage it's built for rather than forcing one platform to cover the whole lifecycle.

**8. Describe a specific incident you led the response for, and what changed afterward.**
Prepare one concrete example from any of these roles — the pattern across all of them is: detect (alerts), stabilize, root-cause, and then *close the gap* with a specific runbook/automation change, not just a retrospective document. Interviewers weight the "what changed afterward" part most heavily.

**9. What's the difference between RTO and RPO, and how did that show up in your work at Regeneron?**
RTO is how long a system can be down before it's unacceptable; RPO is how much data loss (in time) is tolerable. At Regeneron, "defined recovery objectives" for critical research pipelines means those two numbers were set deliberately per pipeline's actual criticality, driving which specific recovery mechanism (not necessarily the most expensive one) was appropriate.

**10. How do you decide what belongs on AWS versus Azure for a given workload, rather than just picking one cloud?**
Answer shape: data residency/compliance constraints, existing team expertise, specific managed-service fit (e.g., SageMaker vs. Databricks), and cost — the Southern Company OT-analytics-on-Azure-with-AWS-for-select-workloads split is a concrete example of this being a deliberate per-workload decision, not an arbitrary one.

[⬆ Back to top](#top)

---

## Most Important Concepts to Know First

1. Why AWS + Azure together, not either alone (the thread through every role)
2. Dual EKS/AKS operation — same Kubernetes API, different underlying scaling mechanisms
3. SCPs (AWS) + Azure Policy — complementary, not redundant
4. GxP compliance driving architecture decisions (Regeneron)
5. Blue-green/canary as a deployment-risk mitigation, distinct from infrastructure HA (Rivian)
6. SageMaker vs. Azure Databricks — model lifecycle vs. large-scale data prep
7. RTO/RPO as the two numbers that actually drive DR strategy choice
8. Cross-Cloud Disaster Recovery as the most advanced HA pattern on this resume
9. Incident response discipline: detect → stabilize → root-cause → close the gap with automation
10. The career arc itself: Alteryx (foundational) → Liberty Mutual/TJ Maxx (first patterns) → Rivian/Southern Company (dual-cloud K8s at scale) → Regeneron (regulated-data rigor) → Truist (current synthesis)

[⬆ Back to top](#top)
