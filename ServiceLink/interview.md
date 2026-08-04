<a id="top"></a>

# ServiceLink — DevOps Engineer Interview Prep

Role: DevOps Engineer, hybrid (Plano, TX — 3 days/week in-office). Azure
primary platform, GitHub + Azure DevOps for delivery, one active AWS
project. Built against the JD pasted 2026-08-04, cross-referenced with
[Olalekan_Ogundare_Resume.md](../Resume/Olalekan_Ogundare_Resume.md).

## Table of Contents

1. [Role Snapshot](#1-role-snapshot)
2. [Strength Mapping — JD vs Your Experience](#2-strength-mapping--jd-vs-your-experience)
3. [Gaps and How to Address Them](#3-gaps-and-how-to-address-them)
4. [Likely Interview Questions by Category](#4-likely-interview-questions-by-category)
5. [First 90 Days — Talking Points](#5-first-90-days--talking-points)
6. [Questions to Ask Them](#6-questions-to-ask-them)
7. [Live Technical / Build Round](#7-live-technical--build-round)

---

# 1. Role Snapshot

| Aspect | Detail |
|---|---|
| Time split | 60% hands-on engineering, 25% technical leadership, 15% enablement/communication |
| Primary platform | Microsoft Azure (IaC-managed, AKS, Entra ID, networking, PaaS) |
| Delivery tooling | GitHub Actions **and** Azure DevOps — both, not one or the other |
| Secondary platform | AWS — one active project, same IaC/pipeline standards applied |
| Core mandate | Be the "connective tissue" between dev teams and the platform — standardization, self-service, security-embedded pipelines, cost governance |
| Location | Plano, TX, hybrid — 3 days/week in-office, no sponsorship |

**Read on the role**: this is a *platform engineering* DevOps role, not a
pure infra-ops role — the outcomes they list (developers self-serve,
deployment frequency improves quarter over quarter, pipelines are
"trusted" across teams) are about reducing friction for other engineers,
not just keeping infrastructure up. Frame answers around *enablement*,
not just *execution*.

[⬆ Back to top](#top)

---

# 2. Strength Mapping — JD vs Your Experience

| JD Requirement | Your Matching Experience |
|---|---|
| CI/CD across GitHub Actions | Migrated legacy Jenkins pipelines to **GitHub Actions and Harness** at Citibank, improving deployment reliability and release consistency. Directly relevant — lead with this. |
| Standardized pipeline patterns / reusable templates | Built **reusable Terraform modules and golden templates** standardizing deployments across dev/UAT/prod at Citibank — same "standardize once, every team inherits it" pattern the JD wants, just apply it to pipeline templates instead of IaC modules. |
| Security/quality gates in pipelines (SAST, secret/dependency/container scanning) | Embedded **SAST, dependency scanning, secret scanning, container scanning, IaC security checks** directly into CI/CD at Citibank — this is close to a word-for-word match to the JD's "CI/CD & Developer Tooling" bullet. |
| IaC ownership: modules, remote state, policy-as-code | Managed **Terraform remote state via S3 + DynamoDB locking**; enforced **OPA and Sentinel** policy gates blocking non-compliant infra before apply. Same concepts the JD wants for Azure (policy-as-code, drift detection), just on AWS backends — the pattern transfers directly. |
| Kubernetes operations (JD: AKS specifically) | Managed **EKS** at scale (multi-tenant RBAC, namespace isolation, resource governance) — CKA + KCNA certified, so the Kubernetes fundamentals transfer cleanly; the AKS-specific surface area (node pools, Azure CNI, ACR integration) is the actual gap — see [§3](#3-gaps-and-how-to-address-them). |
| Identity & access (Entra ID, managed identities, Key Vault, RBAC) | Direct Azure Entra ID exposure at Cynet Systems (State Farm) and hybrid identity/connectivity work at Dell EMC (Texas A&M) — real but shallower than the AWS IAM depth; be honest about depth, lean on the IAM/least-privilege discipline being platform-agnostic. |
| Azure networking (VNet, NSG, Private Endpoints, App Gateway) | Configured **hybrid connectivity via VPN/ExpressRoute** securing on-prem VMware ↔ Azure at Dell EMC/Texas A&M — real hands-on VNet/hybrid-connectivity experience, good anchor story. |
| AWS project support | This is your **strongest** area by far — AWS Certified Solutions Architect Professional + Security Specialty, multi-account landing zone design (Organizations, Control Tower, SCPs), VPC/Transit Gateway, GuardDuty/Security Hub. Position this as "I can own the AWS side with almost no ramp-up." |
| Observability (metrics, logging, alerting, dashboards) | Full-stack observability at Citibank — **CloudWatch, Prometheus, Grafana, ELK/OpenSearch**, reduced incident detection/recovery time 35%. Directly reusable pattern; Azure equivalents (Azure Monitor, Log Analytics) are a tooling swap, not a conceptual gap. |
| Cloud cost visibility / FinOps | **FinOps Certified Practitioner**, delivered **20–25% sustained infrastructure cost savings** via rightsizing, Savings Plans, Spot, lifecycle automation at Citibank. This is a named JD outcome ("cloud spend is visible and governed") — lead with the certification and the number. |
| Developer self-service / reducing DevOps toil | Automated infra/ML platform deployments cutting manual provisioning ~45% and improving deploy speed up to 65% at Citibank — same "remove yourself from the critical path" outcome the JD's "developers self-serve" bullet wants. |
| GitHub org / ADO governance (branch policies, access control, audit logging) | No explicit resume bullet — infer from IAM/SCP/least-privilege enforcement experience and be ready to speak to it conceptually rather than claim direct ADO admin experience you haven't done. |

[⬆ Back to top](#top)

---

# 3. Gaps and How to Address Them

Be upfront about these rather than overstating — the JD's specificity
(AKS, Azure DevOps, App Service/Functions/SQL/Cosmos DB) suggests they
will probe for hands-on depth, and a confident "here's exactly what
transfers and what I'd need to ramp on" lands better than pretending
equivalent depth you don't have.

| Gap | How to Frame It |
|---|---|
| **AKS vs EKS** | "I've run production Kubernetes at scale on EKS — multi-tenant RBAC, namespace isolation, CKA-certified — the control-plane concepts (scheduling, RBAC, networking policy) are identical on AKS; what's new is the Azure-specific integration surface: Azure CNI, ACR image pull via managed identity, AKS-specific upgrade/node-pool patterns. I'd expect to be productive on AKS within the first few weeks, not months." |
| **Azure DevOps Pipelines specifically** | "My CI/CD depth is GitHub Actions, Jenkins, and Harness — the pipeline-as-code mental model (stages, gates, templates, approvals) maps directly onto Azure Pipelines' YAML syntax; the main ramp is ADO-specific concepts like classic vs YAML pipelines, service connections, and variable groups, which I'd expect to pick up quickly given the underlying CI/CD design patterns are the same ones I've already standardized elsewhere." |
| **Azure PaaS (App Service, Functions, Azure SQL, Cosmos DB)** | "My PaaS-equivalent depth is on the AWS side (Lambda, RDS, DynamoDB) — the operational patterns (managed scaling, connection pooling, serverless cold-start tuning) transfer conceptually; the Azure-specific knowledge I'd need to build is the portal/CLI/ARM-template surface for these specific services." |
| **Direct GitHub org / ADO project governance** | Don't claim it directly — say you've enforced equivalent governance (least-privilege IAM, SCPs, branch-protection-equivalent guardrails in your Terraform policy gates) and would apply the same judgment to GitHub org and ADO project settings. |

[⬆ Back to top](#top)

---

# 4. Likely Interview Questions by Category

## CI/CD & Developer Tooling

**"Walk me through a pipeline migration you led — why, and what broke?"**
→ The Jenkins → GitHub Actions/Harness migration at Citibank. Lead with
*why* (maintenance overhead, release consistency across environments),
then be ready for a follow-up on what specifically broke or needed
rework during the migration — have one concrete failure story ready,
not just the clean success narrative.

**"How do you standardize pipelines across teams without slowing anyone down?"**
→ Reusable Terraform modules/golden templates is your proof point for
*this exact pattern*, just applied to infrastructure rather than
pipelines — reusable templates + shared task libraries + documented
branching workflows is the pipeline-world equivalent of what you already
did for infra.

**"Where do you put security scanning in a pipeline so it doesn't create friction?"**
→ SAST/dependency/secret/container scanning embedded directly into
CI/CD at Citibank — talk about *shifting left* without blocking velocity:
fast-failing gates early (secret scanning, SAST) vs. slower gates
(container scanning) placed later, and using policy-as-code (OPA/Sentinel)
rather than manual review, so the gate scales without more headcount.

## Azure Infrastructure & Platform

**"How would you approach an AKS cluster you've inherited but never
operated day-to-day?"**
→ Anchor on the EKS operational muscle (RBAC, namespace isolation,
resource governance, upgrade management) and name the Azure-specific
things you'd verify first: node pool sizing/autoscaler config, Azure CNI
vs kubenet, ACR pull permissions via managed identity.

**"How do you think about least-privilege identity in Azure vs AWS?"**
→ Be honest that AWS IAM/SCP is your deeper well, then map the concepts:
Entra ID roles/managed identities ≈ IAM roles/instance profiles, Key
Vault ≈ KMS/Secrets Manager, Azure Policy ≈ SCP/Config Rules — the
judgment (least privilege, no long-lived credentials, service-to-service
via managed identity not secrets) is identical even where the exact
service names differ.

## AWS (Active Project Support)

**"Tell me about the multi-account landing zone you designed."**
→ AWS Organizations + Control Tower, OUs for Dev/Non-Prod/Prod/Security/
Shared Services, SCPs enforcing encryption/region restriction/public-
access blocks, centralized CloudTrail + Config + S3 Object Lock. This is
your strongest single story for this section — walk through the *why*
per OU, not just the list of services.

## IaC & Automation

**"How do you handle Terraform state and drift at scale?"**
→ S3 backend + DynamoDB locking to eliminate state conflicts across
teams, OPA/Sentinel gates blocking non-compliant plans before apply —
map this directly to the JD's "policy-as-code enforcement" and "drift
detection" asks; if pushed on Azure-specific state backends (Storage
Account + blob lease locking instead of S3+DynamoDB), acknowledge the
mechanism differs but the discipline is the same.

## Observability & Reliability

**"Tell me about an incident where your observability setup made the
difference."**
→ The CloudWatch/Prometheus/Grafana/ELK stack reducing incident
detection/recovery time 35% — have a specific incident in mind (what the
dashboard/alert actually caught) rather than just citing the percentage.

## FinOps / Cost Governance

**"How do you get engineering teams to actually act on a cost report,
not just receive it?"**
→ This is likely probed hard given the JD names "monthly FinOps
reporting" as an explicit ownership item. Your 20–25% savings number is
strong, but be ready to talk about the *mechanism* that got teams to
act — tagging governance/attribution so cost is visible per-team, not
just an aggregate number nobody owns.

## Leadership / Enablement (25% + 15% of the role)

**"Describe a time you had to convince a team to adopt a standard they
didn't ask for."**
→ Draw on the golden-template/module standardization work — this JD
explicitly wants someone who drives adoption, not just builds tooling
and hopes teams pick it up.

[⬆ Back to top](#top)

---

# 5. First 90 Days — Talking Points

The JD spells out concrete 90-day deliverables — treat this section as
a rehearsal for "walk me through your first 90 days," since they've
already told you what "correct" looks like:

1. **Pipeline audit + standardization roadmap** — frame this the same
   way you'd describe the Citibank golden-template rollout: audit first
   (what exists, what's inconsistent), then propose the reusable pattern,
   not the reverse.
2. **Reusable pipeline templates adopted by 2+ teams** — emphasize
   *adoption*, not just delivery — a template nobody uses isn't a win;
   this is where the "convince a team to adopt a standard" story matters.
3. **Azure IaC coverage assessment** — this is a drift-detection /
   unmanaged-resource audit, conceptually identical to auditing an AWS
   account for resources created outside Terraform — you have direct
   experience reasoning about this even if the Azure tooling specifics
   differ.
4. **Baseline security/quality gates across all repos** — same shift-
   left gate work you did at Citibank, just rolled out org-wide on day
   one instead of iteratively.
5. **Cloud cost baseline report, Azure + AWS** — your FinOps
   certification and Citibank savings number are your strongest opening
   line for this specific deliverable.

[⬆ Back to top](#top)

---

# 6. Questions to Ask Them

- "What does 'trusted delivery mechanism' currently *not* look like today —
  what's the specific pain point that made this a priority hire?"
- "How many teams currently deploy through GitHub Actions vs Azure DevOps,
  and is there an intended long-term direction, or will both remain
  permanent?"
- "How mature is the AWS project's IaC/pipeline setup relative to the
  Azure side — is it meant to converge to the same standards, or stay
  independently operated?"
- "Who currently owns cost governance, and what happens today when a
  cost anomaly is found — is there an existing FinOps process or would
  I be building it?"
- "What does the on-call/incident-response rotation actually look like
  day to day?"

[⬆ Back to top](#top)

---

# 7. Live Technical / Build Round

This is a scenario-based build round: analyze → design/diagram → implement
a working artifact (IaC, pipeline YAML, or automation script) → discuss
trade-offs. AI tooling (Claude, Copilot, Cursor) is explicitly encouraged —
"effective use of AI tooling is considered a positive signal," so plan to
narrate your use of it out loud rather than treat it as something to hide.

## Pre-Interview Setup Checklist

- [ ] VS Code (or equivalent) installed and open
- [ ] draw.io (app.diagrams.net) open in a browser tab, confirmed working
- [ ] Claude.ai / GitHub Copilot / Cursor logged in and ready to use
- [ ] Terminal available with `git`, `terraform`, `az`/`aws` CLI, `python`
- [ ] A blank scratch directory ready to `git init` if needed

## Working Process to Rehearse

1. **Clarify before touching a tool.** Restate the problem out loud, ask
   about constraints explicitly (existing platform choices, security
   requirements, scale, which cloud) — the instructions call this out
   directly: "do not begin designing or coding until you have a thorough
   understanding of the problem."
2. **Diagram first, in draw.io.** A pipeline flow or architecture diagram,
   narrated while you draw — they're evaluating communication as much as
   the diagram itself, so a clear box-and-arrow sketch beats a polished
   one that took too long.
3. **Narrate AI-tool use.** "I'm asking Claude to scaffold this Terraform
   module, let me review what it produced before I adapt it" — shows
   judgment and review discipline, not just typing speed.
4. **Build the smallest artifact that demonstrates the design** — not a
   fully productionized version. A working two-stage pipeline or a single
   focused Terraform module beats an incomplete attempt at something bigger.
5. **Close with trade-offs** — what you'd do differently at production
   scale, what you deliberately skipped for time, and one credible
   alternative approach you considered and didn't take.

## Likely Problem Shapes (Given This JD)

Practice one scenario from each bucket so nothing is a first-time-cold
problem in the room:

- **CI/CD pipeline design** — e.g. a GitHub Actions or Azure DevOps YAML
  pipeline for a containerized app: build → security scan (SAST/secret
  scan) → deploy, gated per environment. Directly maps to
  [§4 CI/CD & Developer Tooling](#4-likely-interview-questions-by-category).
- **Infrastructure as Code** — e.g. a Terraform or Bicep module
  provisioning an AKS cluster or App Service with least-privilege identity
  (managed identity + Key Vault reference, not a static secret).
- **Automation scripting** — e.g. a Python/Bash/PowerShell script that
  audits a set of resources for an IaC-coverage or compliance gap and
  reports it. This maps directly to the "Azure infrastructure IaC coverage
  assessment" 90-day deliverable in [§5](#5-first-90-days--talking-points) —
  worth practicing explicitly since it's named in their own JD.
- **Observability/incident response** — e.g. designing an alerting/
  dashboard flow for a failing pipeline or a degraded service.

## Anchor Patterns to Adapt Live

Don't build from a blank cursor — start from patterns you already know
cold and adapt them to whatever scenario is given, narrating the
adaptation explicitly: the golden-template Terraform module pattern from
Citibank, the OPA/Sentinel policy-gate pattern, the Jenkins→GitHub Actions
migration. Saying "this is the same gate pattern I used for Terraform
plans, just applied to a container-scan step here" demonstrates transfer
of judgment, which is exactly what the AKS/Azure-DevOps gaps in
[§3](#3-gaps-and-how-to-address-them) need you to demonstrate live.

## Common Traps

- Jumping to code before restating the problem back — asking 2–3
  clarifying questions first is expected, not a sign of weakness.
- Hiding AI-tool use instead of narrating it — the instructions state
  effective use is a positive signal.
- Over-polishing the draw.io diagram at the expense of time to build.
- Going silent while typing — think out loud through the build and
  especially through the closing trade-off discussion.

[⬆ Back to top](#top)
