# Emerson — STAR Interview Questions and Answers

**Candidate:** Olalekan G. Ogundare  
**Target role:** Cloud Platform Infrastructure Engineer (DevOps)

These STAR answers are tailored to Emerson’s job description and the supplied resume. Use the documented results, and adjust scenario details to match what you personally did.

STAR means **Situation, Task, Action, Result**.

## 1. Tell me about a time you automated a manual infrastructure process.

**Situation:** At Citibank, teams needed consistent AWS infrastructure across development, UAT, and production, but provisioning involved substantial manual effort.

**Task:** My responsibility was to improve delivery speed and consistency while maintaining security controls.

**Action:** I developed reusable Terraform modules and integrated provisioning with Ansible and CI/CD workflows. I embedded infrastructure security checks and review gates so teams could use approved patterns repeatedly.

**Result:** The work reduced manual provisioning by approximately 45% and made infrastructure changes more consistent and reviewable.

## 2. Describe a time you improved production monitoring and reliability.

**Situation:** At Citibank, supporting distributed cloud workloads required visibility across applications, infrastructure, logs, and deployment changes.

**Task:** I needed to help teams detect problems earlier and investigate incidents faster.

**Action:** I implemented observability using CloudWatch, Prometheus, Grafana, and centralized logging. I also built operational dashboards and integrated alerting with ServiceNow so teams could connect symptoms with the affected services.

**Result:** These improvements reduced incident detection and recovery time by 35% and gave teams better information for root-cause analysis.

## 3. Tell me about a time you embedded security into software delivery.

**Situation:** At Citibank, infrastructure and application changes had to meet security requirements within a regulated financial environment.

**Task:** My goal was to identify security issues before production without making every deployment depend on manual checks.

**Action:** I integrated static analysis, dependency scanning, secret detection, container scanning, and IaC checks into pipelines. I also implemented OPA and Sentinel policies to prevent noncompliant Terraform changes from reaching apply.

**Result:** Security checks became part of the repeatable delivery process, giving engineers earlier feedback and making enforcement more consistent.

## 4. Describe a time you supported Kubernetes workloads for multiple teams.

**Situation:** At Citibank, EKS supported microservices, batch processing, and compute-intensive workloads used by different teams.

**Task:** I needed to support shared platform usage while maintaining appropriate access boundaries and resource governance.

**Action:** I designed multitenant Kubernetes environments using RBAC, namespace isolation, and resource governance. I worked with workload requirements so access and resource allocation reflected each team’s needs.

**Result:** The platform supported multiple teams with clearer access boundaries and more controlled resource consumption.

## 5. Tell me about a time you improved infrastructure performance.

**Situation:** At Citibank, data-intensive workloads depended on efficient access to datasets stored in S3 and served through FSx for Lustre.

**Task:** My responsibility was to improve storage performance for large-scale processing.

**Action:** I focused on FSx for Lustre throughput and S3-backed dataset access, using workload performance information to guide the optimization.

**Result:** The changes improved large-scale data processing performance by more than 30%. It reinforced the importance of identifying the actual bottleneck before increasing compute capacity.

## 6. Describe a time you reduced cloud costs while maintaining resilience.

**Situation:** At Citibank, we needed to control infrastructure spending while continuing to support production workloads reliably.

**Task:** I was responsible for identifying practical savings opportunities without weakening platform resilience.

**Action:** I directed cost optimization through rightsizing, Savings Plans, appropriate Spot usage, and automated FSx lifecycle policies. I evaluated opportunities according to workload requirements rather than applying the same approach everywhere.

**Result:** The work delivered sustained infrastructure cost savings of 20–25% while maintaining platform resilience.

## 7. Tell me about a time you improved CI/CD delivery.

**Situation:** At Citibank, we had legacy Jenkins pipelines that required ongoing maintenance and improvements to release consistency.

**Task:** I helped modernize delivery workflows and reduce pipeline maintenance overhead.

**Action:** I migrated pipelines to GitHub Actions and Harness and developed reusable configurations. My Harness work included approval gates, secrets management, Terraform deployments, Kubernetes releases, and deployment strategies such as canary and blue-green.

**Result:** The migration reduced maintenance overhead and improved deployment reliability and consistency across environments.

## 8. Describe your approach to validating disaster recovery.

**Situation:** In my consulting role, client workloads needed recovery strategies across AWS and Azure.

**Task:** My responsibility was to align recovery capabilities with business recovery time and recovery point objectives.

**Action:** I designed recovery strategies using AWS Backup and cross-region replication, alongside Azure Backup and Azure Site Recovery. I incorporated recovery drills to validate that the planned recovery approach worked.

**Result:** The drills provided evidence of recovery readiness and helped identify gaps that needed remediation before an actual outage.

## 9. Tell me about a time you worked with security and compliance teams.

**Situation:** At Luminous Logistic, supporting CloudWave Healthcare Solutions, the cloud platform operated within healthcare security and compliance requirements.

**Task:** I needed to help establish secure AWS infrastructure and support HIPAA and SOC 2 controls.

**Action:** I implemented multi-account governance, Service Control Policies, centralized CloudTrail and AWS Config logging, and immutable retention using S3 Object Lock. I also integrated organization-wide GuardDuty and Security Hub and partnered with security and compliance teams.

**Result:** The platform had more consistent preventive controls, centralized security visibility, and stronger audit evidence.

## 10. Tell me about a time you created reusable solutions for other engineers.

**Situation:** In my current consulting role, client engineering teams needed consistent ways to provision AWS and Azure environments.

**Task:** My goal was to make approved infrastructure patterns easier to adopt.

**Action:** I built reusable landing-zone patterns, self-service infrastructure modules, and Terraform and ARM templates. I also configured Terraform Enterprise and Cloud workflows with workspace structures, policy enforcement, and reviewed deployment gates.

**Result:** Client teams adopted the reusable patterns directly, reducing reliance on provisioning environments by hand and improving consistency.

## 11. Describe a time you secured a hybrid cloud connection.

**Situation:** During my Dell EMC/VirtualTechGuru engagement with Texas A&M University, infrastructure modernization required connectivity between on-premises VMware environments and Azure.

**Task:** I needed to support secure connectivity and migration readiness.

**Action:** I configured hybrid connectivity using VPN and ExpressRoute and supported migration activities, including replication setup, test failovers, and production cutovers.

**Result:** The work supported large-scale VM migrations with minimal disruption. The broader modernization engagement achieved $1.2 million in cost savings.

## 12. Tell me about a time you improved infrastructure security through standardization.

**Situation:** At Citibank, Linux infrastructure needed consistent security tooling, patching, and compliance validation.

**Task:** My responsibility was to help establish a repeatable, hardened server baseline.

**Action:** I built golden AMIs for RHEL and Amazon Linux 2023 using EC2 Image Builder. I integrated CrowdStrike Falcon, Qualys, and Tanium and supported patch management and post-patch compliance reporting.

**Result:** This created a repeatable security baseline and made endpoint protection and vulnerability validation part of the infrastructure lifecycle.

## 13. Tell me about a time you coordinated architecture and operational requirements.

**Situation:** In my consulting role, client platforms needed to support application delivery while meeting infrastructure, security, and recovery requirements.

**Task:** I needed to translate those requirements into reusable cloud platform patterns.

**Action:** I brought together networking, identity, Terraform workflows, Kubernetes configuration, monitoring, and disaster recovery considerations. I used policy enforcement and reviewed deployment workflows to carry those requirements into implementation.

**Result:** The resulting patterns gave engineering teams a consistent foundation for deploying and operating workloads across AWS and Azure.

## 14. Describe a time you improved documentation and operational processes.

**Situation:** At Computer Warehouse, supporting MTN Nigeria, infrastructure projects and support activities needed repeatable operational guidance.

**Task:** I wanted to improve delivery consistency and reduce the time spent resolving familiar issues.

**Action:** I developed documentation and operational templates that captured implementation procedures and support practices.

**Result:** Those improvements reduced project delivery time and incident resolution by approximately 25%. It taught me to treat documentation as an operational asset that needs to evolve with the platform.

## 15. Tell me about a time you overcame a technical challenge.

**Situation:** At Citibank, I supported compute-intensive environments involving NVIDIA GPUs, containerized workloads, and high-performance storage.

**Task:** I needed to help maintain a compatible platform for GPU-accelerated applications.

**Action:** My troubleshooting covered GPU driver compatibility, CUDA runtime errors, container access to GPUs, scheduling failures, and storage throughput. I examined the relevant layers to isolate whether the issue came from the host, runtime, container, scheduler, or storage.

**Result:** This work supported the operation of GPU-accelerated workloads and strengthened my ability to troubleshoot problems that span multiple infrastructure layers.

## Preparation note

For questions about a specific outage, failed upgrade, conflict, or missed deadline, use an actual event you can explain under follow-up questioning. Your resume establishes the technical responsibilities, but it does not provide enough detail to claim a particular incident or disagreement.
