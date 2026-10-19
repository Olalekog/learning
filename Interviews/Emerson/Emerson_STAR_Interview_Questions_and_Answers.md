<a id="top"></a>

# Emerson — STAR Interview Questions and Answers

**Candidate:** Olalekan G. Ogundare  
**Target role:** Cloud Platform Infrastructure Engineer (DevOps)

These STAR answers are tailored to Emerson’s job description and the supplied resume. Use the documented results, and adjust scenario details to match what you personally did.

STAR means **Situation, Task, Action, Result**.

## Index

- [1. Tell me about a time you automated a manual infrastructure process.](#1-tell-me-about-a-time-you-automated-a-manual-infrastructure-process)
- [2. Describe a time you improved production monitoring and reliability.](#2-describe-a-time-you-improved-production-monitoring-and-reliability)
- [3. Tell me about a time you embedded security into software delivery.](#3-tell-me-about-a-time-you-embedded-security-into-software-delivery)
- [4. Describe a time you supported Kubernetes workloads for multiple teams.](#4-describe-a-time-you-supported-kubernetes-workloads-for-multiple-teams)
- [5. Tell me about a time you improved infrastructure performance.](#5-tell-me-about-a-time-you-improved-infrastructure-performance)
- [6. Describe a time you reduced cloud costs while maintaining resilience.](#6-describe-a-time-you-reduced-cloud-costs-while-maintaining-resilience)
- [7. Tell me about a time you improved CI/CD delivery.](#7-tell-me-about-a-time-you-improved-cicd-delivery)
- [8. Describe your approach to validating disaster recovery.](#8-describe-your-approach-to-validating-disaster-recovery)
- [9. Tell me about a time you worked with security and compliance teams.](#9-tell-me-about-a-time-you-worked-with-security-and-compliance-teams)
- [10. Tell me about a time you created reusable solutions for other engineers.](#10-tell-me-about-a-time-you-created-reusable-solutions-for-other-engineers)
- [11. Describe a time you secured a hybrid cloud connection.](#11-describe-a-time-you-secured-a-hybrid-cloud-connection)
- [12. Tell me about a time you improved infrastructure security through standardization.](#12-tell-me-about-a-time-you-improved-infrastructure-security-through-standardization)
- [13. Tell me about a time you coordinated architecture and operational requirements.](#13-tell-me-about-a-time-you-coordinated-architecture-and-operational-requirements)
- [14. Describe a time you improved documentation and operational processes.](#14-describe-a-time-you-improved-documentation-and-operational-processes)
- [15. Tell me about a time you overcame a technical challenge.](#15-tell-me-about-a-time-you-overcame-a-technical-challenge)
- [16. Tell me about a time you restored a corrupted Terraform state file.](#16-tell-me-about-a-time-you-restored-a-corrupted-terraform-state-file)
- [17. How did you standardize infrastructure provisioning at Citi?](#17-how-did-you-standardize-infrastructure-provisioning-at-citi)
- [18. How did you embed security controls into deployment pipelines?](#18-how-did-you-embed-security-controls-into-deployment-pipelines)
- [Preparation note](#preparation-note)

## 1. Tell me about a time you automated a manual infrastructure process.

**Situation:** At Citibank, teams needed consistent AWS infrastructure across development, UAT, and production, but provisioning involved substantial manual effort.

**Task:** My responsibility was to improve delivery speed and consistency while maintaining security controls.

**Action:** I developed reusable Terraform modules and integrated provisioning with Ansible and CI/CD workflows. I embedded infrastructure security checks and review gates so teams could use approved patterns repeatedly.

**Result:** The work reduced manual provisioning by approximately 45% and made infrastructure changes more consistent and reviewable.

[⬆ Go to top](#top)

## 2. Describe a time you improved production monitoring and reliability.

**Situation:** At Citibank, supporting distributed cloud workloads required visibility across applications, infrastructure, logs, and deployment changes.

**Task:** I needed to help teams detect problems earlier and investigate incidents faster.

**Action:** I implemented observability using CloudWatch, Prometheus, Grafana, and centralized logging. I also built operational dashboards and integrated alerting with ServiceNow so teams could connect symptoms with the affected services.

**Result:** These improvements reduced incident detection and recovery time by 35% and gave teams better information for root-cause analysis.

[⬆ Go to top](#top)

## 3. Tell me about a time you embedded security into software delivery.

**Situation:** At Citibank, infrastructure and application changes had to meet security requirements within a regulated financial environment.

**Task:** My goal was to identify security issues before production without making every deployment depend on manual checks.

**Action:** I integrated static analysis, dependency scanning, secret detection, container scanning, and IaC checks into pipelines. I also implemented OPA and Sentinel policies to prevent noncompliant Terraform changes from reaching apply.

**Result:** Security checks became part of the repeatable delivery process, giving engineers earlier feedback and making enforcement more consistent.

[⬆ Go to top](#top)

## 4. Describe a time you supported Kubernetes workloads for multiple teams.

**Situation:** At Citibank, EKS supported microservices, batch processing, and compute-intensive workloads used by different teams.

**Task:** I needed to support shared platform usage while maintaining appropriate access boundaries and resource governance.

**Action:** I designed multitenant Kubernetes environments using RBAC, namespace isolation, and resource governance. I worked with workload requirements so access and resource allocation reflected each team’s needs.

**Result:** The platform supported multiple teams with clearer access boundaries and more controlled resource consumption.

[⬆ Go to top](#top)

## 5. Tell me about a time you improved infrastructure performance.

**Situation:** At Citibank, data-intensive workloads depended on efficient access to datasets stored in S3 and served through FSx for Lustre.

**Task:** My responsibility was to improve storage performance for large-scale processing.

**Action:** I focused on FSx for Lustre throughput and S3-backed dataset access, using workload performance information to guide the optimization.

**Result:** The changes improved large-scale data processing performance by more than 30%. It reinforced the importance of identifying the actual bottleneck before increasing compute capacity.

[⬆ Go to top](#top)

## 6. Describe a time you reduced cloud costs while maintaining resilience.

**Situation:** At Citibank, we needed to control infrastructure spending while continuing to support production workloads reliably.

**Task:** I was responsible for identifying practical savings opportunities without weakening platform resilience.

**Action:** I directed cost optimization through rightsizing, Savings Plans, appropriate Spot usage, and automated FSx lifecycle policies. I evaluated opportunities according to workload requirements rather than applying the same approach everywhere.

**Result:** The work delivered sustained infrastructure cost savings of 20–25% while maintaining platform resilience.

[⬆ Go to top](#top)

## 7. Tell me about a time you improved CI/CD delivery.

**Situation:** At Citibank, we had legacy Jenkins pipelines that required ongoing maintenance and improvements to release consistency.

**Task:** I helped modernize delivery workflows and reduce pipeline maintenance overhead.

**Action:** I migrated pipelines to GitHub Actions and Harness and developed reusable configurations. My Harness work included approval gates, secrets management, Terraform deployments, Kubernetes releases, and deployment strategies such as canary and blue-green.

**Result:** The migration reduced maintenance overhead and improved deployment reliability and consistency across environments.

[⬆ Go to top](#top)

## 8. Describe your approach to validating disaster recovery.

**Situation:** In my consulting role, client workloads needed recovery strategies across AWS and Azure.

**Task:** My responsibility was to align recovery capabilities with business recovery time and recovery point objectives.

**Action:** I designed recovery strategies using AWS Backup and cross-region replication, alongside Azure Backup and Azure Site Recovery. I incorporated recovery drills to validate that the planned recovery approach worked.

**Result:** The drills provided evidence of recovery readiness and helped identify gaps that needed remediation before an actual outage.

[⬆ Go to top](#top)

## 9. Tell me about a time you worked with security and compliance teams.

**Situation:** At Luminous Logistic, supporting CloudWave Healthcare Solutions, the cloud platform operated within healthcare security and compliance requirements.

**Task:** I needed to help establish secure AWS infrastructure and support HIPAA and SOC 2 controls.

**Action:** I implemented multi-account governance, Service Control Policies, centralized CloudTrail and AWS Config logging, and immutable retention using S3 Object Lock. I also integrated organization-wide GuardDuty and Security Hub and partnered with security and compliance teams.

**Result:** The platform had more consistent preventive controls, centralized security visibility, and stronger audit evidence.

[⬆ Go to top](#top)

## 10. Tell me about a time you created reusable solutions for other engineers.

**Situation:** In my current consulting role, client engineering teams needed consistent ways to provision AWS and Azure environments.

**Task:** My goal was to make approved infrastructure patterns easier to adopt.

**Action:** I built reusable landing-zone patterns, self-service infrastructure modules, and Terraform and ARM templates. I also configured Terraform Enterprise and Cloud workflows with workspace structures, policy enforcement, and reviewed deployment gates.

**Result:** Client teams adopted the reusable patterns directly, reducing reliance on provisioning environments by hand and improving consistency.

[⬆ Go to top](#top)

## 11. Describe a time you secured a hybrid cloud connection.

**Situation:** During my Dell EMC/VirtualTechGuru engagement with Texas A&M University, infrastructure modernization required connectivity between on-premises VMware environments and Azure.

**Task:** I needed to support secure connectivity and migration readiness.

**Action:** I configured hybrid connectivity using VPN and ExpressRoute and supported migration activities, including replication setup, test failovers, and production cutovers.

**Result:** The work supported large-scale VM migrations with minimal disruption. The broader modernization engagement achieved $1.2 million in cost savings.

[⬆ Go to top](#top)

## 12. Tell me about a time you improved infrastructure security through standardization.

**Situation:** At Citibank, Linux infrastructure needed consistent security tooling, patching, and compliance validation.

**Task:** My responsibility was to help establish a repeatable, hardened server baseline.

**Action:** I built golden AMIs for RHEL and Amazon Linux 2023 using EC2 Image Builder. I integrated CrowdStrike Falcon, Qualys, and Tanium and supported patch management and post-patch compliance reporting.

**Result:** This created a repeatable security baseline and made endpoint protection and vulnerability validation part of the infrastructure lifecycle.

[⬆ Go to top](#top)

## 13. Tell me about a time you coordinated architecture and operational requirements.

**Situation:** In my consulting role, client platforms needed to support application delivery while meeting infrastructure, security, and recovery requirements.

**Task:** I needed to translate those requirements into reusable cloud platform patterns.

**Action:** I brought together networking, identity, Terraform workflows, Kubernetes configuration, monitoring, and disaster recovery considerations. I used policy enforcement and reviewed deployment workflows to carry those requirements into implementation.

**Result:** The resulting patterns gave engineering teams a consistent foundation for deploying and operating workloads across AWS and Azure.

[⬆ Go to top](#top)

## 14. Describe a time you improved documentation and operational processes.

**Situation:** At Computer Warehouse, supporting MTN Nigeria, infrastructure projects and support activities needed repeatable operational guidance.

**Task:** I wanted to improve delivery consistency and reduce the time spent resolving familiar issues.

**Action:** I developed documentation and operational templates that captured implementation procedures and support practices.

**Result:** Those improvements reduced project delivery time and incident resolution by approximately 25%. It taught me to treat documentation as an operational asset that needs to evolve with the platform.

[⬆ Go to top](#top)

## 15. Tell me about a time you overcame a technical challenge.

**Situation:** At Citibank, I supported compute-intensive environments involving NVIDIA GPUs, containerized workloads, and high-performance storage.

**Task:** I needed to help maintain a compatible platform for GPU-accelerated applications.

**Action:** My troubleshooting covered GPU driver compatibility, CUDA runtime errors, container access to GPUs, scheduling failures, and storage throughput. I examined the relevant layers to isolate whether the issue came from the host, runtime, container, scheduler, or storage.

**Result:** This work supported the operation of GPU-accelerated workloads and strengthened my ability to troubleshoot problems that span multiple infrastructure layers.

[⬆ Go to top](#top)

## 16. Tell me about a time you restored a corrupted Terraform state file.

**Situation:** At Citibank, a Terraform apply was interrupted partway through, leaving the state file out of sync with the actual AWS resources for a shared infrastructure stack.

**Task:** I needed to restore a reliable state before any team could safely run Terraform against that environment again.

**Action:** I stopped all pipeline runs against the affected state and confirmed the lock so no other operation could run concurrently. Our state was stored in a versioned, encrypted S3 backend, so I pulled the last known-good object version and ran a plan to compare it against the live infrastructure. Where the plan still showed unexpected drift, I reconciled it by importing resources that existed in AWS but were missing from state, rather than applying blindly and risking deletion of resources that were still in use.

**Result:** We recovered a state file that accurately reflected the environment without any production impact, and I documented the recovery steps as a runbook. Afterward, I tightened state-backend permissions and alerting so a partial apply would be caught and contained faster next time.

[⬆ Go to top](#top)

## 17. How did you standardize infrastructure provisioning at Citi?

**Situation:** At Citibank, every team needed consistent access to the same core AWS services, but without a common pattern, provisioning was repeated and inconsistent across projects.

**Task:** I needed to give teams a standardized, reviewed way to provision infrastructure instead of each team building it from scratch.

**Action:** I built reusable Terraform modules and golden templates for VPC, EC2, ALB/Auto Scaling, RDS, S3, IAM, KMS, EKS, CloudWatch, EventBridge, and FSx, each with a single responsibility, validated inputs, and secure defaults. I integrated them into CI/CD pipelines — Jenkins, GitHub Actions, and Harness — with formatting, validation, security scanning, and a reviewed plan before an approved apply, and used Ansible for configuration management on top of the provisioned infrastructure.

**Result:** Manual provisioning dropped by about 45%, and some deployments accelerated by up to 65%, while every environment followed the same reviewed, auditable path to production.

[⬆ Go to top](#top)

## 18. How did you embed security controls into deployment pipelines?

**Situation:** At Citibank, security reviews were largely manual and happened late, after infrastructure and application changes were already built.

**Task:** I needed security checks to be a standard, automatic part of every pipeline run instead of a separate manual gate at the end.

**Action:** I added Checkov for Terraform misconfigurations, Trivy for container and dependency vulnerabilities, and SonarQube for static code analysis to every pull request. For infrastructure changes specifically, I added OPA and Sentinel policy-as-code checks against the Terraform plan output to catch issues like public S3 buckets, unencrypted volumes, overly broad IAM, or missing tags before deployment. Pipelines authenticated through OIDC with short-lived, role-scoped credentials instead of long-lived AWS keys, and production required a reviewed, saved plan plus an approval gate.

**Result:** A noncompliant change could not merge or deploy, and every approved change left a complete, auditable trail of what was scanned, who approved it, and what was actually applied — security became the default path instead of an optional step.

[⬆ Go to top](#top)

## Preparation note

For questions about a specific outage, failed upgrade, conflict, or missed deadline, use an actual event you can explain under follow-up questioning. Your resume establishes the technical responsibilities, but it does not provide enough detail to claim a particular incident or disagreement.

[⬆ Go to top](#top)
