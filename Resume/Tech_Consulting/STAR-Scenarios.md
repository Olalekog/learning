<a id="top"></a>

# Gabriel O — STAR Scenarios

One Situation/Task/Action/Result scenario per role, built directly from
the resume's own bullets — ready to use for behavioral interview
questions ("tell me about a time you..."). Companion to
[Elevator-Pitch.md](Elevator-Pitch.md) and
[Project-Deep-Dive-and-Interview-Prep.md](Project-Deep-Dive-and-Interview-Prep.md)
in this folder.

## Table of Contents

1. [Truist Bank — Slow, Inconsistent Multi-Cloud Releases](#truist-bank)
2. [Regeneron — Moving Regulated Data Across Clouds Without Breaking GxP](#regeneron)
3. [Southern Company — Recurring Data-Pipeline & Connectivity Outages](#southern-company)
4. [Rivian — De-Risking Vehicle Software Rollouts](#rivian)
5. [TJ Maxx — Surviving Peak Holiday Traffic](#tj-maxx)
6. [Liberty Mutual — No Company-Wide Cloud Security Standard](#liberty-mutual)
7. [Alteryx — Manual, Error-Prone Internal Administration](#alteryx)
8. [Cross-Cutting — Unifying AWS and Azure Security Posture](#unified-security-posture)

---

## Truist Bank — Slow, Inconsistent Multi-Cloud Releases {#truist-bank}

**Situation**: Truist ran both AWS and Azure, but teams across the bank
had no shared pattern for networking, identity, security, or CI/CD —
every team solved multi-cloud its own way, and releases were slow while
still needing to satisfy banking regulators' audit requirements.

**Task**: Design a reusable multi-cloud pattern the whole bank could
adopt, and speed up releases without weakening the audit trail
regulators required.

**Action**: Defined reusable AWS+Azure landing zone patterns
(networking/security/identity/CI-CD) that other teams pulled directly
for new projects; ran companion EKS and AKS clusters so teams could
pick the right platform per workload; unified AWS security (Organizations
+ SCPs, Security Hub, GuardDuty, automatic checks and fixes) with Azure
security (Sentinel, Defender for Cloud, Azure Policy) into one risk
view; used Azure DevOps and GitHub Actions to manage releases, approvals,
and environments with built-in audit trails.

**Result**: ~40% reduction in release cycle time, a single unified view
of risk across both clouds, and a pattern other teams actually adopted
bank-wide rather than one that stayed a document nobody used.

[⬆ Back to top](#top)

---

## Regeneron — Moving Regulated Data Across Clouds Without Breaking GxP {#regeneron}

**Situation**: Regeneron's research platform needed to move clinical and
genomic data between AWS and Azure, but the environment was constrained
by GxP — the regulatory framework governing data integrity and
traceability in pharma research — meaning any cross-cloud data movement
risked breaking compliance if not designed carefully.

**Task**: Architect an AWS-Azure approach that let data move securely
between clouds while keeping every environment provably GxP-compliant
from the start, not audited into compliance after the fact.

**Action**: Designed shared identity, private networking, and
consistent CI/CD across both clouds specifically for compliant data
movement; split the ML pipeline so SageMaker handled production
train/deploy/monitor while Azure Databricks handled large-scale data
prep and feature engineering; set company-wide Landing Zones/Azure
Policy plus equivalent AWS Organizations guardrails so every new
research project started from the same secure, validated baseline;
unified Sentinel/Defender/Azure Policy with AWS Security Hub for one
coherent risk picture.

**Result**: Secure, compliant data movement between clouds that never
broke GxP controls, plus defined recovery objectives and automated
failure recovery that shortened downtime during several high-impact
incidents.

[⬆ Back to top](#top)

---

## Southern Company — Recurring Data-Pipeline & Connectivity Outages {#southern-company}

**Situation**: Southern Company's OT-related analytics environment
experienced several major data-pipeline and connectivity outages,
disrupting operations that depended on reliable data flow between AWS
and Azure.

**Task**: Restore service quickly during each outage, then reduce how
often — and how badly — it happened again.

**Action**: Led incident response for the outages, coordinating on-call
teams to restore service; afterward, built organization-wide AWS
security policies with automated remediation so misconfigurations were
caught and fixed without manual effort; improved alerts, wrote clearer
runbooks, and automated recovery steps for the specific failure modes
that had caused the outages; used Azure DevOps to make every
infrastructure and data-pipeline change reviewable and auditable going
forward, closing off a common source of unreviewed changes causing
drift.

**Result**: Measurably reduced recovery time on subsequent incidents,
and fewer manual interventions required as automated remediation caught
issues before they became outages.

[⬆ Back to top](#top)

---

## Rivian — De-Risking Vehicle Software Rollouts {#rivian}

**Situation**: Rivian's vehicle telemetry and OTA (over-the-air) update
services meant that a bad software rollout wouldn't just cause a
service outage — it could reach real, physical vehicles already on the
road.

**Task**: Build a delivery process that let the team ship frequently
without risking a bad release reaching the full vehicle fleet at once.

**Action**: Used Azure DevOps and GitHub Actions to implement
blue-green and canary progressive delivery for vehicle software
services, with clear approval gates and environment promotion paths;
backed this with dual EKS/AKS clusters and full observability
(CloudWatch, Azure Monitor, Prometheus, Grafana) so a bad canary was
visible immediately; used SageMaker to build predictive-maintenance
models from vehicle and factory data, catching quality issues earlier
in the pipeline as well.

**Result**: Vehicle software releases could be validated against a
small slice of real traffic before full rollout, with a fast rollback
path if something was wrong; predictive maintenance improved quality
insights, and better alerting/automated remediation reduced overall
recovery time.

[⬆ Back to top](#top)

---

## TJ Maxx — Surviving Peak Holiday Traffic {#tj-maxx}

For the full architecture behind this (VNet/VPC network diagram,
autoscaling, release-freeze windows), see
[TJ-Maxx-Architecture-Design.md](TJ-Maxx-Architecture-Design.md).

**Situation**: TJ Maxx's store and digital applications faced a hard,
narrow, revenue-critical peak every year — holiday shopping traffic —
where a platform failure had immediate, outsized business impact.

**Task**: Keep releases flowing right up to and through peak retail
events without disruption, and make each subsequent peak event less
risky than the last.

**Action**: Used Azure DevOps to manage frequent, controlled releases
for store and digital applications; applied early Security Center/
Defender-era governance to keep customer data protected during
high-traffic periods; participated directly in incident response during
major peak retail events, then fed what was learned back into improved
alerts and runbooks before the next event.

**Result**: Releases survived peak holiday traffic, and each subsequent
peak event caused measurably less disruption than the one before it —
a direct result of treating peak readiness as a recurring, iterative
problem rather than a one-time fix.

[⬆ Back to top](#top)

---

## Liberty Mutual — No Company-Wide Cloud Security Standard {#liberty-mutual}

**Situation**: Liberty Mutual's claims and policy applications were
moving to Azure before any company-wide Landing Zone or security
pattern existed — each new application risked being built with its own,
inconsistent approach to protecting sensitive insurance data.

**Task**: Establish a first, repeatable security and networking
standard that future claims/policy applications could build on, while
still letting development and operations teams work efficiently.

**Action**: Helped establish some of the first company-wide Azure
Landing Zone concepts and policy at the organization; applied identity,
Key Vault, and network isolation controls to protect sensitive insurance
data; used the era's Azure DevOps tooling to bring structure to release,
approval, and environment management; supported reliability through
improved monitoring and documented recovery steps.

**Result**: A repeatable, secure baseline that every new claims/policy
application could start from, instead of each team inventing its own
approach to protecting sensitive data.

[⬆ Back to top](#top)

---

## Alteryx — Manual, Error-Prone Internal Administration {#alteryx}

**Situation**: Internal systems administration relied heavily on manual,
repetitive work, and the team's incident response lacked the clear
runbooks needed for fast, consistent recovery.

**Task**: Reduce manual toil in routine administration and build the
early habits of documented, fast incident recovery — while getting
hands-on with cloud platforms still new to the organization.

**Action**: Automated routine administration tasks with PowerShell and
Bash; participated directly in incident response for internal services,
learning first-hand why clear runbooks and fast recovery mattered; built
and monitored a small pilot application on Google Cloud (Compute Engine/
Cloud Storage) alongside early AWS and Azure experimentation.

**Result**: Established the foundational identity, networking,
automation, and monitoring skills that every later multi-cloud
architecture role — Liberty Mutual through Truist Bank — scaled up
from, plus the moderate GCP experience carried into the skills section
today.

[⬆ Back to top](#top)

---

## Cross-Cutting — Unifying AWS and Azure Security Posture {#unified-security-posture}

Not tied to one role — this pattern recurs at Truist Bank, Southern
Company, and Regeneron, all of which needed a single security picture
across two clouds running side by side.

**Situation**: Each cloud's security tooling operated in its own
silo — AWS Organizations/SCPs, Security Hub, and GuardDuty on one side,
Microsoft Sentinel, Defender for Cloud, and Azure Policy on the
other — leaving security and compliance teams switching between two
consoles and reconciling findings by hand instead of seeing one picture
of risk.

**Task**: Build a single, coherent view of security posture across
both clouds, without ripping out either cloud's native tooling or
standing up a whole separate platform just to reconcile the two.

**Options Considered**:
- **Keep the two consoles separate and reconcile manually.** Rejected —
  doesn't scale past a handful of accounts/subscriptions, and cross-cloud
  incidents (the kind that actually matter) get missed or correlated too
  slowly when nobody's looking at both consoles at once.
- **Adopt a third-party CNAPP (Wiz or Prisma Cloud) as a single pane of
  glass across every cloud.** Genuinely viable — both appear in the
  skills section — but means standing up and governing an entirely new
  vendor relationship and tool, on top of security tooling already
  built into both clouds natively.
- **Use each cloud's native security stack, and connect AWS into the
  Azure-native tools already in place (Defender for Cloud, Sentinel).**
  Chosen — reuses tooling and skills already in place on the Azure side,
  avoids a net-new vendor relationship, and both Defender for Cloud and
  Sentinel ship purpose-built AWS connectors for exactly this.

**Action**: Connected AWS to **Microsoft Defender for Cloud** via its
native AWS connector — Defender for Cloud discovers AWS resources
directly through a federated-trust connection (no long-lived AWS keys
stored) and folds them into the same Secure Score, recommendations, and
regulatory compliance dashboard Azure resources already show up in.
Connected AWS to **Microsoft Sentinel** separately via its own AWS
connector (CloudTrail/S3-based log ingestion) so AWS alerts and logs
flow into the same SIEM workspace and get correlated against Azure
signals. Paired this with AWS-side automation (Organizations + SCPs for
preventive guardrails, Security Hub for posture, GuardDuty for threat
detection, automated remediation) so drift gets fixed on the AWS side
without waiting on the unified view to catch it after the fact.

**Result**: One Secure Score/compliance view and one SIEM workspace
spanning both clouds instead of two disconnected tool sets — the
pattern underlying Truist Bank's ~40% faster release cycle time
(security wasn't a bottleneck because posture was already consistent)
and Regeneron's ability to move GxP-regulated data across clouds
without breaking compliance controls.

[⬆ Back to top](#top)
