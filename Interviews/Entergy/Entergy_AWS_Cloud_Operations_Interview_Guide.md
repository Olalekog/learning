<a id="top"></a>

# Entergy — AWS Cloud Operations Engineer Interview Guide

Prepared for Olalekan Gabriel Ogundare
Updated: October 13, 2026

## How to use this guide

This guide combines 61 interview questions and answers, practical troubleshooting commands, AWS console walkthroughs, automation examples, security preparation, and production-support procedures.

Aim for approximately 45–60 seconds for an initial answer, then use the commands and console steps when asked for details. Use this sequence: **impact → evidence → diagnosis → safe correction → verification**.

The introduction reflects your stated background. Sample automation and incident stories must be adapted to work you actually performed. Do not claim invented employers, outage durations, savings, or project results. Console labels can vary by resource type and account configuration. Commands containing `<placeholders>` need actual values; operating-system tools and service names vary.

## Index

- [Entergy — AWS Cloud Operations Engineer Interview Guide](#entergy--aws-cloud-operations-engineer-interview-guide)
  - [How to use this guide](#how-to-use-this-guide)
  - [Index](#index)
  - [Questions 1–20: Core interview questions](#questions-120-core-interview-questions)
    - [1. Can you briefly introduce yourself and explain your AWS Cloud Operations experience?](#1-can-you-briefly-introduce-yourself-and-explain-your-aws-cloud-operations-experience)
    - [2. How do you troubleshoot an EC2 instance that is running but inaccessible?](#2-how-do-you-troubleshoot-an-ec2-instance-that-is-running-but-inaccessible)
    - [3. What is the difference between a Security Group and a Network ACL?](#3-what-is-the-difference-between-a-security-group-and-a-network-acl)
    - [4. How do you troubleshoot connectivity between EC2 and RDS?](#4-how-do-you-troubleshoot-connectivity-between-ec2-and-rds)
    - [5. How do you use CloudWatch for monitoring and troubleshooting?](#5-how-do-you-use-cloudwatch-for-monitoring-and-troubleshooting)
    - [6. What would you do if an application on EC2 became slow or unresponsive?](#6-what-would-you-do-if-an-application-on-ec2-became-slow-or-unresponsive)
    - [7. How do VPCs, subnets, route tables, and Internet Gateways work together?](#7-how-do-vpcs-subnets-route-tables-and-internet-gateways-work-together)
    - [8. How do you manage IAM using least privilege?](#8-how-do-you-manage-iam-using-least-privilege)
    - [9. What is the difference between an ALB and an NLB?](#9-what-is-the-difference-between-an-alb-and-an-nlb)
    - [10. How do you troubleshoot a target failing load-balancer health checks?](#10-how-do-you-troubleshoot-a-target-failing-load-balancer-health-checks)
    - [11. How do you use Terraform or CloudFormation?](#11-how-do-you-use-terraform-or-cloudformation)
    - [12. Can you give a scripting example for AWS operational tasks?](#12-can-you-give-a-scripting-example-for-aws-operational-tasks)
    - [13. How do you use AWS Systems Manager?](#13-how-do-you-use-aws-systems-manager)
    - [14. How do you troubleshoot Route 53 DNS issues?](#14-how-do-you-troubleshoot-route-53-dns-issues)
    - [15. What steps do you follow during a production incident?](#15-what-steps-do-you-follow-during-a-production-incident)
    - [16. How do you patch EC2 while minimizing downtime?](#16-how-do-you-patch-ec2-while-minimizing-downtime)
    - [17. How do you configure backups and disaster recovery?](#17-how-do-you-configure-backups-and-disaster-recovery)
    - [18. How do you investigate CPU, memory, or disk pressure?](#18-how-do-you-investigate-cpu-memory-or-disk-pressure)
    - [19. How do you reduce AWS costs without affecting availability?](#19-how-do-you-reduce-aws-costs-without-affecting-availability)
    - [20. Tell me about a major AWS production issue you resolved.](#20-tell-me-about-a-major-aws-production-issue-you-resolved)
  - [Questions 21–45: Additional responsibility-based questions](#questions-2145-additional-responsibility-based-questions)
    - [21. What does your daily AWS operations routine look like?](#21-what-does-your-daily-aws-operations-routine-look-like)
    - [22. How do you manage EC2 throughout its lifecycle?](#22-how-do-you-manage-ec2-throughout-its-lifecycle)
    - [23. How would you secure an application's S3 bucket?](#23-how-would-you-secure-an-applications-s3-bucket)
    - [24. How do you troubleshoot S3 AccessDenied?](#24-how-do-you-troubleshoot-s3-accessdenied)
    - [25. How do you expand EBS safely?](#25-how-do-you-expand-ebs-safely)
    - [26. Auto Scaling is not adding instances. What do you check?](#26-auto-scaling-is-not-adding-instances-what-do-you-check)
    - [27. How do you design reliable Auto Scaling?](#27-how-do-you-design-reliable-auto-scaling)
    - [28. How do you support RDS operationally?](#28-how-do-you-support-rds-operationally)
    - [29. How do you troubleshoot VPN or hybrid connectivity?](#29-how-do-you-troubleshoot-vpn-or-hybrid-connectivity)
    - [30. What happens when a client connects to an HTTPS application?](#30-what-happens-when-a-client-connects-to-an-https-application)
    - [31. How do you troubleshoot Windows EC2?](#31-how-do-you-troubleshoot-windows-ec2)
    - [32. What if EC2 does not appear in Systems Manager?](#32-what-if-ec2-does-not-appear-in-systems-manager)
    - [33. How do you maintain consistent fleet configuration?](#33-how-do-you-maintain-consistent-fleet-configuration)
    - [34. How do you handle patch failures?](#34-how-do-you-handle-patch-failures)
    - [35. How do you handle infrastructure drift?](#35-how-do-you-handle-infrastructure-drift)
    - [36. How do you make scripts safe for production?](#36-how-do-you-make-scripts-safe-for-production)
    - [37. How do you verify backups are usable?](#37-how-do-you-verify-backups-are-usable)
    - [38. How do you conduct a DR exercise?](#38-how-do-you-conduct-a-dr-exercise)
    - [39. How do you improve availability without unnecessary cost?](#39-how-do-you-improve-availability-without-unnecessary-cost)
    - [40. What should a runbook contain?](#40-what-should-a-runbook-contain)
    - [41. How do you work with application, infrastructure, security, and development teams?](#41-how-do-you-work-with-application-infrastructure-security-and-development-teams)
    - [42. What if teams disagree about whether the fault is application or infrastructure?](#42-what-if-teams-disagree-about-whether-the-fault-is-application-or-infrastructure)
    - [43. How do you handle urgent requests for broader production access?](#43-how-do-you-handle-urgent-requests-for-broader-production-access)
    - [44. How do you communicate incidents to business stakeholders?](#44-how-do-you-communicate-incidents-to-business-stakeholders)
    - [45. What would you focus on in your first 30 days?](#45-what-would-you-focus-on-in-your-first-30-days)
  - [Questions 46–61: Backup and disaster recovery](#questions-4661-backup-and-disaster-recovery)
    - [46. Tell me about your experience with backup and disaster recovery.](#46-tell-me-about-your-experience-with-backup-and-disaster-recovery)
    - [47. What is the difference between backup, high availability, and disaster recovery?](#47-what-is-the-difference-between-backup-high-availability-and-disaster-recovery)
    - [48. How do you define RTO and RPO?](#48-how-do-you-define-rto-and-rpo)
    - [49. How do you choose a disaster-recovery strategy?](#49-how-do-you-choose-a-disaster-recovery-strategy)
    - [50. How would you configure an AWS Backup plan?](#50-how-would-you-configure-an-aws-backup-plan)
    - [51. Walk me through a recovery drill for an EC2 application.](#51-walk-me-through-a-recovery-drill-for-an-ec2-application)
    - [52. How do you validate an EBS backup?](#52-how-do-you-validate-an-ebs-backup)
    - [53. How do you recover RDS after accidental data deletion?](#53-how-do-you-recover-rds-after-accidental-data-deletion)
    - [54. What exactly do you test during a recovery drill?](#54-what-exactly-do-you-test-during-a-recovery-drill)
    - [55. How do you prove the drill met RTO and RPO?](#55-how-do-you-prove-the-drill-met-rto-and-rpo)
    - [56. What evidence do you retain for audit and sign-off?](#56-what-evidence-do-you-retain-for-audit-and-sign-off)
    - [57. What if the application owner signs off without providing test evidence?](#57-what-if-the-application-owner-signs-off-without-providing-test-evidence)
    - [58. Tell me about a recovery drill that exposed a problem.](#58-tell-me-about-a-recovery-drill-that-exposed-a-problem)
    - [59. How do you automate recovery testing?](#59-how-do-you-automate-recovery-testing)
    - [60. How do you conduct a regional failover and failback?](#60-how-do-you-conduct-a-regional-failover-and-failback)
    - [61. How often should recovery drills run?](#61-how-often-should-recovery-drills-run)
  - [Hands-on commands and interpretation](#hands-on-commands-and-interpretation)
    - [Command set A — EC2 access and SSH](#command-set-a--ec2-access-and-ssh)
    - [Command set B — CPU, memory, disk, and application health](#command-set-b--cpu-memory-disk-and-application-health)
    - [Command set C — RDS connectivity](#command-set-c--rds-connectivity)
    - [Command set D — Load-balancer targets](#command-set-d--load-balancer-targets)
    - [Command set E — DNS, routes, and TLS](#command-set-e--dns-routes-and-tls)
    - [Command set F — Windows administration](#command-set-f--windows-administration)
    - [Command set G — AWS identity, SSM, and Auto Scaling](#command-set-g--aws-identity-ssm-and-auto-scaling)
  - [AWS console step-by-step walkthroughs](#aws-console-step-by-step-walkthroughs)
    - [Walkthrough 1 — EC2 inaccessible (Questions 2, 22, 31)](#walkthrough-1--ec2-inaccessible-questions-2-22-31)
    - [Walkthrough 2 — CloudWatch alarms and slowness (Questions 5, 6, 18)](#walkthrough-2--cloudwatch-alarms-and-slowness-questions-5-6-18)
    - [Walkthrough 3 — EC2 to RDS (Question 4)](#walkthrough-3--ec2-to-rds-question-4)
    - [Walkthrough 4 — RDS performance and availability (Question 28)](#walkthrough-4--rds-performance-and-availability-question-28)
    - [Walkthrough 5 — Unhealthy load-balancer target (Question 10)](#walkthrough-5--unhealthy-load-balancer-target-question-10)
    - [Walkthrough 6 — Auto Scaling launch failures (Questions 26, 27)](#walkthrough-6--auto-scaling-launch-failures-questions-26-27)
    - [Walkthrough 7 — S3 security and AccessDenied (Questions 23, 24)](#walkthrough-7--s3-security-and-accessdenied-questions-23-24)
    - [Walkthrough 8 — EBS expansion (Question 25)](#walkthrough-8--ebs-expansion-question-25)
    - [Walkthrough 9 — IAM least privilege and temporary access (Questions 8, 43)](#walkthrough-9--iam-least-privilege-and-temporary-access-questions-8-43)
    - [Walkthrough 10 — Secure remote administration (Questions 13, 32, 43)](#walkthrough-10--secure-remote-administration-questions-13-32-43)
    - [Walkthrough 11 — Patch Manager (Questions 16, 34)](#walkthrough-11--patch-manager-questions-16-34)
    - [Walkthrough 12 — Inventory and State Manager (Question 33)](#walkthrough-12--inventory-and-state-manager-question-33)
    - [Walkthrough 13 — Route 53 (Question 14)](#walkthrough-13--route-53-question-14)
    - [Walkthrough 14 — Restore and DR validation (Questions 17, 37, 38)](#walkthrough-14--restore-and-dr-validation-questions-17-37-38)
    - [Walkthrough 15 — CloudFormation changes and drift (Questions 11, 35)](#walkthrough-15--cloudformation-changes-and-drift-questions-11-35)
    - [Walkthrough 16 — Cost and performance (Questions 19, 39)](#walkthrough-16--cost-and-performance-questions-19-39)
  - [Automation examples](#automation-examples)
    - [Terraform — Three-tier AWS project](#terraform--three-tier-aws-project)
    - [Python — EC2/EBS operational report](#python--ec2ebs-operational-report)
    - [Bash and PowerShell operational examples](#bash-and-powershell-operational-examples)
  - [Production support and communication](#production-support-and-communication)
    - [Prioritization and escalation](#prioritization-and-escalation)
    - [Change and rollback preparation](#change-and-rollback-preparation)
    - [Incident update example](#incident-update-example)
    - [Root-cause analysis](#root-cause-analysis)
    - [Runbook outline](#runbook-outline)
  - [Security review](#security-review)
  - [Teams-call preparation](#teams-call-preparation)
    - [Work arrangement and authorization](#work-arrangement-and-authorization)
    - [Questions to ask the interviewer](#questions-to-ask-the-interviewer)
  - [Official AWS references](#official-aws-references)

## Questions 1–20: Core interview questions

### 1. Can you briefly introduce yourself and explain your AWS Cloud Operations experience?

**Answer:**

I’m Olalekan Gabriel Ogundare, a cloud infrastructure and DevOps engineer with over 10 years of experience designing, automating, securing, and supporting AWS and Azure environments.

Currently at Tech Consulting, I build and operate client cloud platforms, including EC2, S3, EBS, and container services. I use Terraform and automated pipelines for controlled infrastructure changes, implement least-privilege IAM and encryption, and monitor availability, performance, and cost through CloudWatch and Cost Explorer. I also support backup and disaster-recovery strategies validated through recovery drills.

Previously at Citibank, I standardized AWS deployments across dev, UAT, and production using reusable Terraform modules covering VPC, EC2, load balancers, Auto Scaling, RDS, and IAM. My work also included hardened Linux AMIs, patch management, and CloudWatch dashboards integrated with ServiceNow. Our observability improvements reduced incident detection and recovery time by 35%.

That experience aligns closely with Entergy’s need for hands-on AWS operations, troubleshooting, security, automation, and production support. I’m comfortable working across application, infrastructure, security, and development teams to resolve issues and improve reliability.

[⬆ Go to top](#top)

### 2. How do you troubleshoot an EC2 instance that is running but inaccessible?

**Answer:**

“I first determine whether the failure is a network timeout, connection refusal, or authentication error. In the EC2 console, I check status checks, the correct IP address, security groups, routes, and network ACLs. For a private instance, I verify the approved access path, such as VPN or Session Manager.

I use `ssh -vvv` to identify where SSH fails. If an alternative approved connection is available, I inspect the SSH service, host firewall, disk capacity, and authentication logs. After correcting the cause, I reconnect from the original source and verify application health. I avoid opening administrative ports broadly.”

**Console:** [Walkthrough 1 — EC2 inaccessible](#walkthrough-1--ec2-inaccessible-questions-2-22-31). **Commands:** Command set A.

[⬆ Go to top](#top)

### 3. What is the difference between a Security Group and a Network ACL?

| Feature | Security Group | Network ACL |
|---|---|---|
| Scope | Associated network interfaces | Subnet |
| Rules | Allow | Allow and deny |
| Connection handling | Stateful | Stateless |
| Return traffic | Automatically allowed for permitted connections | Requires explicit rules |
| Evaluation | Applicable allow rules considered together | Numbered rules evaluated in order |

**Answer:**

“I use security groups to control communication between workloads. For example, the database security group allows the database port from the application security group. Network ACLs provide subnet-level filtering. Because they are stateless, I check both request and return traffic, including the relevant ephemeral ports, during troubleshooting.”

[⬆ Go to top](#top)

### 4. How do you troubleshoot connectivity between EC2 and RDS?

**Answer:**

“I troubleshoot DNS, network connectivity, and database authentication separately. I confirm RDS availability and the correct endpoint and port, then resolve the endpoint and test TCP connectivity from the application instance.

I inspect database inbound rules, application outbound rules, routes, and network ACLs. For separate VPCs, I check the connecting network and return path. If TCP connects but login fails, I investigate credentials, database permissions, TLS, and connection limits. I verify recovery through an application database transaction.”

**Console:** [Walkthrough 3 — EC2 to RDS](#walkthrough-3--ec2-to-rds-question-4). **Commands:** Command set C.

[⬆ Go to top](#top)

### 5. How do you use CloudWatch for monitoring and troubleshooting?

**Answer:**

“I monitor availability, performance, and capacity: EC2 CPU and status checks, load-balancer latency and errors, RDS connections and storage, and application metrics. I configure the CloudWatch agent for operating-system memory and filesystem utilization because standard EC2 monitoring does not provide them.

I create alarms with suitable thresholds, evaluation periods, missing-data treatment, and operational notifications. During incidents, I correlate metric timestamps with logs and recent changes. I verify recovery through monitoring and a user-facing transaction, then improve the alarm if the incident revealed a gap.”

**Console:** [Walkthrough 2 — CloudWatch alarms and slowness](#walkthrough-2--cloudwatch-alarms-and-slowness-questions-5-6-18). **Commands:** Command set B.

[⬆ Go to top](#top)

### 6. What would you do if an application on EC2 became slow or unresponsive?

**Answer:**

“I determine the business impact, when the issue started, and whether a deployment or infrastructure change occurred. I check load-balancer errors, latency, healthy targets, and instance metrics. Through approved access, I inspect CPU, memory, disk, service status, and logs, then check dependencies such as RDS.

I restore service through a controlled rollback, traffic shift, instance replacement, or capacity change supported by the evidence. Finally, I run business smoke tests, confirm normal error rates and latency, and investigate the root cause.”

**Console:** [Walkthrough 2 — CloudWatch alarms and slowness](#walkthrough-2--cloudwatch-alarms-and-slowness-questions-5-6-18) · [Walkthrough 4 — RDS performance and availability](#walkthrough-4--rds-performance-and-availability-question-28) · [Walkthrough 5 — Unhealthy load-balancer target](#walkthrough-5--unhealthy-load-balancer-target-question-10). **Commands:** Command set B.

[⬆ Go to top](#top)

### 7. How do VPCs, subnets, route tables, and Internet Gateways work together?

**Answer:**

“A VPC provides an isolated network, and subnets divide its address space across Availability Zones. Route tables determine where subnet traffic goes. A public subnet has a route to an Internet Gateway; direct IPv4 internet communication also requires an appropriate public address and security rules.

Private subnets have no direct Internet Gateway route. They can use a NAT Gateway for outbound IPv4 internet access or VPC endpoints for supported AWS services. I typically place internet-facing load balancers in public subnets and application servers and databases in private subnets.”

[⬆ Go to top](#top)

### 8. How do you manage IAM using least privilege?

**Answer:**

“I start with the actions and resources required for a task. I prefer federation and temporary credentials for people, and IAM roles for workloads rather than embedded keys. I separate operational and administrative access, require MFA for privileged human access, and use conditions where appropriate.

I review unused permissions and use IAM Access Analyzer to validate policies and assess unintended access. For AccessDenied, I check identity and resource policies, boundaries, organizational controls, and explicit denies. I verify both permitted tasks and actions that should remain blocked.”

**Console:** [Walkthrough 9 — IAM least privilege and temporary access](#walkthrough-9--iam-least-privilege-and-temporary-access-questions-8-43).

[⬆ Go to top](#top)

### 9. What is the difference between an ALB and an NLB?

| Load balancer | Main use | Typical capabilities |
|---|---|---|
| Application Load Balancer | HTTP/HTTPS applications | Host/path routing and HTTP-aware rules |
| Network Load Balancer | TCP, UDP, and TLS workloads | Transport-level balancing and static IP addresses |

**Answer:**

“I choose an ALB for HTTP-aware routing, such as sending `/api` and `/web` requests to different target groups. I choose an NLB for transport-level protocols or static IP requirements. I base the decision on application protocols, routing behavior, connectivity requirements, and operational needs.”

[⬆ Go to top](#top)

### 10. How do you troubleshoot a target failing load-balancer health checks?

**Answer:**

“I inspect the target-health reason, then verify the health-check protocol, port, path, expected response, timeout, and startup requirements. On the instance, I check the process and listening interface, then test the endpoint locally and over the private network.

I review security groups, network ACLs, host firewalls, and application logs. If failures followed a release, I assess rollback. I confirm recovery through healthy targets, successful requests through the load balancer, and normal latency and errors.”

**Console:** [Walkthrough 5 — Unhealthy load-balancer target](#walkthrough-5--unhealthy-load-balancer-target-question-10). **Commands:** Command set D.

[⬆ Go to top](#top)

### 11. How do you use Terraform or CloudFormation?

**Answer:**

“I use infrastructure as code for repeatable, reviewable deployments. With Terraform, I organize reusable modules, separate environment inputs, and protect remote state with restricted access, encryption, and supported locking.

The workflow includes formatting, validation, security checks, and review of the proposed plan. Production changes include approval and a recovery strategy. With CloudFormation, I review change sets before execution. After either deployment, I verify the resources and application behavior rather than relying only on deployment success.”

**Console:** [Walkthrough 15 — CloudFormation changes and drift](#walkthrough-15--cloudformation-changes-and-drift-questions-11-35). **Example:** Automation section.

[⬆ Go to top](#top)

### 12. Can you give a scripting example for AWS operational tasks?

**Sample answer — use only if it matches implemented work:**

“One example is a Python and Boto3 operational report for potentially idle EC2 instances and unattached EBS volumes. It collects resource metadata, ownership tags, and monitoring evidence, handles pagination and API errors, and generates a reviewable report.

I separate identification from cleanup because low CPU does not prove a server is unused. Owners validate candidates, and destructive actions follow approved changes with retention and recovery considerations. This reduces manual effort while protecting production resources.”

[⬆ Go to top](#top)

### 13. How do you use AWS Systems Manager?

**Answer:**

“I use Session Manager for remote administration, Run Command for controlled operations, Inventory for visibility, Patch Manager for compliance, and State Manager for recurring configuration. Automation supports repeatable operational workflows.

I verify the agent, instance permissions, and connectivity before relying on these capabilities. I target operations using tags, control concurrency and error thresholds, and retain execution results. After an operation, I validate application health as well as the execution status.”

**Console:** [Walkthrough 10 — Secure remote administration](#walkthrough-10--secure-remote-administration-questions-13-32-43) · [Walkthrough 11 — Patch Manager](#walkthrough-11--patch-manager-questions-16-34) · [Walkthrough 12 — Inventory and State Manager](#walkthrough-12--inventory-and-state-manager-question-33).

[⬆ Go to top](#top)

### 14. How do you troubleshoot Route 53 DNS issues?

**Answer:**

“I distinguish a DNS failure from a connection failure and query the hostname from the affected network. For public DNS, I check records and registrar delegation. For private DNS, I verify VPC associations, DNS settings, and resolver behavior.

For hybrid DNS, I check Resolver endpoints, forwarding rules, and network connectivity. I consider TTLs and caching. After correction, I verify resolution and the application connection from the original client network.”

**Console:** [Walkthrough 13 — Route 53](#walkthrough-13--route-53-question-14). **Commands:** Command set E.

[⬆ Go to top](#top)

### 15. What steps do you follow during a production incident?

**Answer:**

“I confirm impact, assign severity under the organization's model, establish ownership, and engage the required teams. I communicate known facts and the next update time. I review metrics, logs, and recent changes to form a focused hypothesis.

Restoration takes priority through an approved rollback, failover, or mitigation with clear validation criteria. I document actions and avoid unrelated changes. Before resolution, I verify business transactions and stable monitoring. Follow-up includes root-cause analysis, corrective actions, owners, deadlines, and runbook updates.”

[⬆ Go to top](#top)

### 16. How do you patch EC2 while minimizing downtime?

**Answer:**

“I test patches in a lower environment, review reboot requirements, and arrange an approved window and recovery plan. For redundant servers, I patch a canary batch, drain traffic, patch and reboot, validate, and return instances to service before proceeding.

Where practical, I replace instances using a tested patched AMI. For a single-instance workload, I communicate the expected outage. Systems Manager controls targeting and execution, but application-aware draining needs separate coordination. I verify patch compliance and business transactions afterward.”

**Console:** [Walkthrough 11 — Patch Manager](#walkthrough-11--patch-manager-questions-16-34).

[⬆ Go to top](#top)

### 17. How do you configure backups and disaster recovery?

**Answer:**

“I start with the recovery point objective—acceptable data loss—and recovery time objective—acceptable recovery duration. I configure EC2/EBS backups with retention, encryption, and appropriate consistency procedures, and retain infrastructure definitions needed for rebuilding.

For RDS, I configure automated backups and point-in-time recovery where supported. Multi-AZ supports availability; backups address recovery from data loss and corruption. For regional recovery, I assess cross-Region copies or replication and the required architecture. I validate the design through restore drills and application-owner testing.”

**Console:** [Walkthrough 14 — Restore and DR validation](#walkthrough-14--restore-and-dr-validation-questions-17-37-38).

[⬆ Go to top](#top)

### 18. How do you investigate CPU, memory, or disk pressure?

**Answer:**

“I identify the constrained resource first. For CPU, I inspect busy processes and distinguish application work from jobs or runaway activity. For memory, I check available memory, swapping, and out-of-memory events. For disk, I check space, inodes, large files, and I/O pressure.

I correlate findings with traffic and recent changes. The correction may involve application tuning, log rotation, storage expansion, or capacity adjustment. I verify sustained recovery and improve monitoring.”

**Commands:** Command set B.

**Console:** [Walkthrough 2 — CloudWatch alarms and slowness](#walkthrough-2--cloudwatch-alarms-and-slowness-questions-5-6-18).

[⬆ Go to top](#top)

### 19. How do you reduce AWS costs without affecting availability?

**Answer:**

“I review cost allocation, ownership, usage trends, and workload requirements. I investigate idle nonproduction resources, unattached volumes, unnecessary snapshots, excessive retention, and oversized instances.

Rightsizing considers peak demand, memory, network throughput, and resilience requirements—not average CPU alone. I evaluate scheduling, Auto Scaling, and commitment discounts after understanding the baseline. Owners validate changes, which follow change control. I compare savings with performance and availability after implementation.”

**Console:** [Walkthrough 16 — Cost and performance](#walkthrough-16--cost-and-performance-questions-19-39).

[⬆ Go to top](#top)

### 20. Tell me about a major AWS production issue you resolved.

**Sample STAR story — adapt to a real incident:**

- **Situation:** After a release, users experienced intermittent errors and the load balancer reported unhealthy targets.
- **Task:** Restore service and determine whether the fault was infrastructure or application behavior.
- **Action:** Review target-health reasons, metrics, and deployment timing. Verify network connectivity, then test the endpoint. Identify an unexpected response from the new version, coordinate rollback, and confirm healthy targets and user transactions.
- **Result:** Service recovered. Add endpoint tests, deployment smoke tests, and a documented rollback procedure to reduce recurrence.

**Spoken answer:**

“After a deployment, an application experienced intermittent errors and unhealthy targets. I reviewed the target-health reasons and correlated failures with the release. Network connectivity was working, but the new version returned an unexpected health response. I coordinated rollback and verified recovery through target health and application transactions. We then added health-endpoint tests and post-deployment validation. For my actual example, I would explain my personal actions and use only recovery times I can substantiate.”

[⬆ Go to top](#top)

## Questions 21–45: Additional responsibility-based questions

### 21. What does your daily AWS operations routine look like?

“I review active incidents, overnight alerts, service health, and handover notes. I check critical dashboards, failed backups, patch compliance, and capacity warnings. I then review scheduled changes and prioritize business impact, security exposure, and availability risks. During the day, I investigate issues and support approved changes. Before handover, I document unresolved issues, actions, risks, and next owners. I also identify repeatable work suitable for automation.”

[⬆ Go to top](#top)

### 22. How do you manage EC2 throughout its lifecycle?

“I use standardized provisioning, configuration, monitoring, patching, and retirement. At provisioning, I check the approved AMI, instance size, subnet, security groups, role, encrypted storage, and ownership tags. During operation, I monitor health and compliance. Before retirement, I confirm dependencies, owner approval, retention, and recovery needs. I review associated volumes and Elastic IPs so decommissioning does not leave unnecessary costs or remove required data.”

**Console:** [Walkthrough 1 — EC2 inaccessible](#walkthrough-1--ec2-inaccessible-questions-2-22-31).

[⬆ Go to top](#top)

### 23. How would you secure an application's S3 bucket?

“I block public access unless explicitly approved and use an application role scoped to required actions and prefixes. I enforce HTTPS, configure encryption appropriate to the data, and verify KMS access if using a customer-managed key. I review versioning, lifecycle, recovery, and audit requirements. I test permitted actions and confirm unauthorized actions remain denied.”

**Console:** [Walkthrough 7 — S3 security and AccessDenied](#walkthrough-7--s3-security-and-accessdenied-questions-23-24).

[⬆ Go to top](#top)

### 24. How do you troubleshoot S3 AccessDenied?

“I identify the actual caller and failed operation, then inspect identity and bucket policies and resource scope. I check explicit denies, boundaries, organizational controls, and endpoint policies. For KMS-encrypted data, I check key access. I distinguish bucket actions from object actions and repeat the exact failed request using the same role and network path after correcting permissions.”

**Console:** [Walkthrough 7 — S3 security and AccessDenied](#walkthrough-7--s3-security-and-accessdenied-questions-23-24).

[⬆ Go to top](#top)

### 25. How do you expand EBS safely?

“I confirm whether the issue is capacity or performance, identify the volume and filesystem, and arrange appropriate backup and change approval. I modify the EBS volume, monitor progress, and extend the partition if necessary and filesystem with OS-specific tools. Increasing the AWS volume alone does not expand usable filesystem space. I verify capacity and application writes afterward.”

**Console:** [Walkthrough 8 — EBS expansion](#walkthrough-8--ebs-expansion-question-25).

[⬆ Go to top](#top)

### 26. Auto Scaling is not adding instances. What do you check?

“I inspect desired and maximum capacity, scaling policies, triggering metrics, and Activity history. I review the launch template, AMI, instance type, subnet addresses, quotas, roles, KMS access, lifecycle hooks, and bootstrap logs. After correction, I verify instances launch, initialize, become healthy targets, and serve traffic.”

**Console:** [Walkthrough 6 — Auto Scaling launch failures](#walkthrough-6--auto-scaling-launch-failures-questions-26-27).

[⬆ Go to top](#top)

### 27. How do you design reliable Auto Scaling?

“I choose a metric aligned with workload demand and maintain minimum capacity across Availability Zones. I configure startup and warmup behavior around the application and verify automated bootstrap. Scale-in accounts for draining and shutdown requirements. I test scaling under load and check that additional application instances do not overload shared dependencies such as RDS.”

**Console:** [Walkthrough 6 — Auto Scaling launch failures](#walkthrough-6--auto-scaling-launch-failures-questions-26-27).

[⬆ Go to top](#top)

### 28. How do you support RDS operationally?

“I monitor availability, CPU, memory, storage, connections, and latency, and review events, backups, and maintenance. I separate connectivity, authentication, and query-performance issues. I collaborate with DBAs or developers on slow queries, locks, and connection pools. Changes use approved procedures, and validation includes application transactions and database metrics. I also test recovery.”

**Console:** [Walkthrough 4 — RDS performance and availability](#walkthrough-4--rds-performance-and-availability-question-28).

[⬆ Go to top](#top)

### 29. How do you troubleshoot VPN or hybrid connectivity?

“I identify the scope and check tunnel status, routing, and BGP where applicable. I trace both directions across the on-premises network, VPN, gateway or Transit Gateway, and VPC. I inspect filtering and DNS separately and use port-specific tests because ping is not sufficient. I coordinate with networking and verify the affected application transaction.”

[⬆ Go to top](#top)

### 30. What happens when a client connects to an HTTPS application?

“The client resolves DNS, establishes TCP connectivity, negotiates TLS, and sends an HTTP request. An AWS load balancer may forward that request to a healthy target. I troubleshoot in that order: DNS, network, TLS, HTTP, then dependencies. I test from the client's actual network because internal tests may follow a different path.”

[⬆ Go to top](#top)

### 31. How do you troubleshoot Windows EC2?

“I start with EC2 status checks and monitoring, then use approved administrative access. I inspect services, Event Viewer, resource usage, disk capacity, and listening ports. I correlate events with changes and test DNS and destination ports. I make a targeted correction and verify service status and an application transaction rather than rebooting immediately.”

**Console:** [Walkthrough 1 — EC2 inaccessible](#walkthrough-1--ec2-inaccessible-questions-2-22-31).

[⬆ Go to top](#top)

### 32. What if EC2 does not appear in Systems Manager?

“I confirm account, Region, instance state, agent installation and service status, instance-profile permissions, and HTTPS connectivity to the required endpoints. I inspect DNS, proxies, endpoint policies, and agent logs. After correcting the cause, I confirm managed-node visibility and test a permitted session or command.”

**Console:** [Walkthrough 10 — Secure remote administration](#walkthrough-10--secure-remote-administration-questions-13-32-43).

[⬆ Go to top](#top)

### 33. How do you maintain consistent fleet configuration?

“I define baselines for agents, services, and security settings. I apply them with State Manager or configuration-management tooling using tags and environment-specific settings. I test changes, review compliance and failures, and remediate drift through the managed source. I update the AMI or bootstrap so newly launched instances start with the right configuration.”

**Console:** [Walkthrough 12 — Inventory and State Manager](#walkthrough-12--inventory-and-state-manager-question-33).

[⬆ Go to top](#top)

### 34. How do you handle patch failures?

“I inspect execution output and package-manager logs for repository access, space, dependencies, permissions, or reboot problems. I assess impact and pause the wider rollout if the canary fails. I correct the cause, rerun the affected batch, and validate OS and application health. Exceptions have owners and remediation dates rather than being reported as compliant.”

**Console:** [Walkthrough 11 — Patch Manager](#walkthrough-11--patch-manager-questions-16-34).

[⬆ Go to top](#top)

### 35. How do you handle infrastructure drift?

“I compare deployment state with code using Terraform plans or supported CloudFormation drift detection. I determine whether the change was approved, unauthorized, or external. Approved changes are incorporated into code after review; unintended changes are corrected after impact assessment. I do not automatically apply a plan that could replace production resources. I then address the access or process gap.”

**Console:** [Walkthrough 15 — CloudFormation changes and drift](#walkthrough-15--cloudformation-changes-and-drift-questions-11-35).

[⬆ Go to top](#top)

### 36. How do you make scripts safe for production?

“I use explicit account, Region, and resource selection, structured logging, pagination, error handling, bounded retries, and dry-run support. Destructive operations need clear criteria, exclusions, and approval. I use roles, avoid logging secrets, design idempotent behavior where possible, and start with a controlled batch. I validate actual resource state and partial failures.”

[⬆ Go to top](#top)

### 37. How do you verify backups are usable?

“I check coverage, job status, retention, and encryption, then perform isolated restore tests. I validate restored volumes or databases with the relevant owner. I record recovery time, recovery point, dependencies, and problems. A completed backup confirms creation; a tested restore provides evidence that recovery works.”

**Console:** [Walkthrough 14 — Restore and DR validation](#walkthrough-14--restore-and-dr-validation-questions-17-37-38).

[⬆ Go to top](#top)

### 38. How do you conduct a DR exercise?

“I agree on scenario, scope, objectives, owners, and success criteria. I follow the runbook, restore or activate infrastructure and data, validate dependencies and access, and test business transactions. I compare actual recovery time and data loss with objectives and test return to normal where applicable. Gaps become owned corrective actions, and application owners confirm functionality.”

**Console:** [Walkthrough 14 — Restore and DR validation](#walkthrough-14--restore-and-dr-validation-questions-17-37-38).

[⬆ Go to top](#top)

### 39. How do you improve availability without unnecessary cost?

“I identify failure points and business requirements, then evaluate multi-AZ application capacity, load balancing, automated replacement, database availability, and recovery procedures. I compare costs with outage risk and check application support for redundancy, including session and file storage. I validate failure behavior through controlled tests.”

**Console:** [Walkthrough 16 — Cost and performance](#walkthrough-16--cost-and-performance-questions-19-39).

[⬆ Go to top](#top)

### 40. What should a runbook contain?

“A runbook includes symptoms, scope, prerequisites, access, diagnostics, expected results, recovery actions, rollback criteria, validation, and escalation. Commands have clear placeholders and decision points. It has an owner and review date. I test it with an engineer who did not write it and update it after incidents and platform changes.”

[⬆ Go to top](#top)

### 41. How do you work with application, infrastructure, security, and development teams?

“I establish a shared problem and assign investigation based on evidence. Application and development teams inspect behavior and releases; infrastructure teams investigate hosts, storage, and networks; security assesses access or security events. I maintain a common timeline, owners, and next steps. We jointly verify recovery and assign prevention actions to the appropriate owners.”

[⬆ Go to top](#top)

### 42. What if teams disagree about whether the fault is application or infrastructure?

“I replace assumptions with tests. I compare local application responses, private-network responses, and requests through the load balancer, then correlate them with metrics, logs, dependencies, and changes. Local failures with healthy host resources guide application investigation; successful local tests with remote failures guide network-path investigation. We document evidence and validate the correction together.”

[⬆ Go to top](#top)

### 43. How do you handle urgent requests for broader production access?

“I clarify the task, scope, and urgency and seek a narrowly scoped role or approved procedure. If elevation is necessary, I follow approval requirements, limit duration where supported, and retain audit evidence. I remove temporary access afterward and consider whether a permanent operational capability is needed. I understand logging limitations, including the lack of session-content logging for Session Manager SSH and port forwarding.”

**Console:** [Walkthrough 9 — IAM least privilege and temporary access](#walkthrough-9--iam-least-privilege-and-temporary-access-questions-8-43) · [Walkthrough 10 — Secure remote administration](#walkthrough-10--secure-remote-administration-questions-13-32-43).

[⬆ Go to top](#top)

### 44. How do you communicate incidents to business stakeholders?

“I lead with the affected service, user impact, and scope, then explain current actions, workarounds, and the next update time. I separate facts from hypotheses and do not promise unsupported recovery times. After recovery, I summarize the cause, validation, and preventive actions in plain language. Technical teams receive detailed evidence separately.”

[⬆ Go to top](#top)

### 45. What would you focus on in your first 30 days?

“I learn account structure, critical applications, procedures, access, and escalation. I review dashboards, alerts, backups, patch compliance, maintenance, and runbooks, and shadow incidents. I then agree on a few practical improvements, such as a missing alarm, untested recovery step, or manual task. My priority is understanding the environment enough to support it safely and independently.”

[⬆ Go to top](#top)

## Questions 46–61: Backup and disaster recovery

This section goes deeper on backup, restore validation, and disaster recovery. Related material elsewhere in the guide: [Question 17](#17-how-do-you-configure-backups-and-disaster-recovery), [Question 37](#37-how-do-you-verify-backups-are-usable), [Question 38](#38-how-do-you-conduct-a-dr-exercise), and [Walkthrough 14 — Restore and DR validation](#walkthrough-14--restore-and-dr-validation-questions-17-37-38).

### 46. Tell me about your experience with backup and disaster recovery.

“At Tech Consulting, I designed backup and disaster-recovery strategies for client environments using AWS Backup and cross-Region replication, alongside Azure recovery services.

I started with business requirements: how much data loss was acceptable and how quickly each service needed to recover. Those requirements guided backup frequency, retention, recovery location, and infrastructure readiness.

I validated the strategy through recovery drills rather than assuming a successful backup meant successful recovery. That involved restoring resources, checking networking and access, and working with application owners to validate functionality. Findings were used to improve the recovery procedure.”

[⬆ Go to top](#top)

### 47. What is the difference between backup, high availability, and disaster recovery?

| Concept | Purpose | Example |
|---|---|---|
| Backup | Recover historical data after loss or corruption | Restore an EBS snapshot or RDS recovery point |
| High availability | Maintain service through component failures | Application instances across AZs; RDS Multi-AZ |
| Disaster recovery | Restore the business service after a major disruption | Recover an application in another Region |

“Replication can copy accidental deletion or corruption, so it does not replace historical backups. Similarly, RDS Multi-AZ supports availability within a Region; a regional recovery strategy requires additional planning.”

[⬆ Go to top](#top)

### 48. How do you define RTO and RPO?

“RTO is the target maximum time to restore the service. RPO is the target maximum acceptable data loss measured in time.

For example, an application might require a two-hour RTO and a fifteen-minute RPO. I would design recovery capabilities around those requirements and test whether the complete application can meet them.

I agree on measurement points with the business before testing. Database availability alone does not mean the service has recovered; users must be able to complete the required business transactions.”

[⬆ Go to top](#top)

### 49. How do you choose a disaster-recovery strategy?

“I consider business criticality, recovery objectives, cost, application architecture, and operational complexity.

Backup and restore can suit workloads that tolerate longer recovery. Pilot light maintains core recovery components but requires additional activation. Warm standby keeps a functioning environment at reduced capacity. Active-active serves traffic from multiple locations but introduces greater complexity.

I select the least costly approach that can demonstrably meet the requirements. I validate the choice through drills rather than promising recovery times from the architecture alone.”

**Note:** AWS describes these four recovery strategies in the Well-Architected Framework.

[⬆ Go to top](#top)

### 50. How would you configure an AWS Backup plan?

“I define resource coverage, schedule, retention, encryption, and any cross-account or cross-Region copies. I use tags or explicit resource selection and verify that critical resources are actually included.

I also monitor failed jobs and copy operations and schedule restore tests. A backup policy is only effective if its coverage and recovery capabilities are verified.”

**Console steps:**

1. Open **AWS Backup → Backup plans → Create backup plan**.
2. Choose a template or build a plan.
3. Configure the backup rule, schedule, backup window, and retention.
4. Select the backup vault.
5. Configure copy rules where supported and required.
6. Create the plan and assign resources using tags or resource IDs.
7. Select the appropriate backup role.
8. Review **Jobs → Backup jobs** and **Copy jobs**.

**Verify:** Confirm expected resources have successful, usable recovery points—not simply that the plan exists.

[⬆ Go to top](#top)

### 51. Walk me through a recovery drill for an EC2 application.

“I define the outage scenario and success criteria first, then restore into an isolated environment.

I recover the instance and data, check security groups, IAM roles, networking, configuration, and dependencies, and validate application functionality. I measure recovery against the agreed objectives.

The application owner runs representative transactions. I retain the results and record any gaps before cleanup and sign-off.”

**Console steps:**

1. Open **AWS Backup → Backup vaults**.
2. Select the EC2 recovery point and choose **Restore**.
3. Review the recovery networking, instance settings, and restore role.
4. Start the restore and monitor **Restore jobs**.
5. Open the restored instance in **EC2 → Instances**.
6. Check status, storage, networking, and access.
7. Connect through the approved administrative method.
8. Validate services and application dependencies.
9. Run business tests and record elapsed recovery time.

**Note:** An AWS Backup EC2 restore creates infrastructure resources; application validation remains a separate responsibility.

[⬆ Go to top](#top)

### 52. How do you validate an EBS backup?

“I restore the snapshot into a new volume in the test instance’s Availability Zone and attach it to an isolated instance.

I identify the filesystem before mounting it and follow the appropriate procedures for its type. I validate required files, permissions, and application data. Where available, I compare checksums against a known reference.

I also consider consistency: a filesystem that mounts successfully may still contain an inconsistent application dataset. Stateful workloads may require application-aware backup procedures.”

**Console steps:**

1. Open **EC2 → Snapshots**.
2. Select the snapshot → **Actions → Create volume from snapshot**.
3. Choose the test instance’s Availability Zone.
4. Open **Volumes**, select the new volume, and attach it to the test instance.
5. Inspect and validate the restored data through approved access.

**Verify:** Required data is readable and usable by the application—not just that the volume attached.

[⬆ Go to top](#top)

### 53. How do you recover RDS after accidental data deletion?

“I identify when the deletion occurred and confirm the available recovery window. I restore to a point before the incident into a new database.

I validate the missing data with the database and application owners and assess valid transactions that occurred after the chosen recovery point. We decide whether to recover selected data or switch the application to the restored database.

I do not redirect production automatically because that could lose newer valid transactions.”

**Console steps:**

1. Open **RDS → Automated backups**.
2. Select the database → **Restore to point in time**.
3. Choose a time before the deletion.
4. Configure the new database, networking, and security.
5. Monitor restoration and validate data.
6. Perform an approved data recovery or application cutover.

**Note:** RDS point-in-time recovery creates a new database; it does not rewind the existing one in place.

[⬆ Go to top](#top)

### 54. What exactly do you test during a recovery drill?

“I test the complete dependency chain, not only the restored resource.”

| Layer | Validation |
|---|---|
| Infrastructure | Instances, storage, required capacity |
| Networking | Routes, DNS, load balancing, private connectivity |
| Security | IAM, KMS, secrets, certificates, access controls |
| Data | Expected records, consistency, actual recovery point |
| Application | Startup, login, read/write transactions, dependencies |
| Operations | Monitoring, alerts, runbook accuracy, escalation |
| Business | Application-owner acceptance |

“I also prevent the test environment from sending real customer notifications or triggering production integrations.”

[⬆ Go to top](#top)

### 55. How do you prove the drill met RTO and RPO?

“I record the agreed start time, recovery actions, and the time the service passed business validation. That gives the actual recovery duration.

For RPO, I examine the latest valid data recovered—using transaction timestamps, sequence numbers, or another application-specific measure—and compare it with the disruption time.

For example, if the latest valid recovered transaction predates the disruption by twelve minutes, the observed data-loss window is twelve minutes. I compare that result with the target and retain the evidence. Backup-job timestamps alone are not sufficient.”

[⬆ Go to top](#top)

### 56. What evidence do you retain for audit and sign-off?

“I retain the drill scope, approved objectives, recovery-point identifiers, execution timestamps, restore results, test output, and application-owner validation.

Each test records who executed it, what was expected, what happened, and whether it passed. Failed tests create corrective actions with owners and deadlines.

The application owner signs off on functionality and data. Infrastructure confirms technical recovery, and the designated risk or compliance owner provides any required control acceptance. I close the ticket according to the organization’s approval process.”

[⬆ Go to top](#top)

### 57. What if the application owner signs off without providing test evidence?

“I would request the evidence before accepting the drill as validated. That includes the tested transactions, execution time, expected result, actual result, and tester identity.

If evidence is missing, the test remains incomplete and the owner repeats the required validation.

I would improve the sign-off template so approval requires linked test results. That makes it clear whether the application was actually exercised rather than simply confirmed as running.”

[⬆ Go to top](#top)

### 58. Tell me about a recovery drill that exposed a problem.

Sample STAR answer—adapt to an actual drill:

“During a recovery drill, the database restored successfully, but the application could not connect.

My responsibility was to identify the dependency preventing business recovery. I checked DNS, network rules, credentials, and encryption access. We found that the recovery environment’s application role lacked the required access to a dependency.

I coordinated the approved correction, repeated the business tests, and recorded the additional recovery time.

We then added dependency and permission checks to the runbook and infrastructure validation. The drill demonstrated why a successful resource restore is not enough to declare the application recovered.”

[⬆ Go to top](#top)

### 59. How do you automate recovery testing?

“I use AWS Backup restore testing for supported resources and automate validation around the restored environment.

For example, a restore-completion event can trigger an EventBridge workflow that invokes Lambda to check the resource or initiate application tests. I collect results, report validation status, and alert on failures.

I keep resource restoration separate from business acceptance. Automated checks help detect failures regularly, while application owners validate the business scenarios the automation does not cover.”

**Note:** AWS supports restore-testing validation workflows using EventBridge targets such as Lambda.

[⬆ Go to top](#top)

### 60. How do you conduct a regional failover and failback?

“I confirm disaster declaration and approval, then follow the runbook to activate recovery capacity, recover data, validate dependencies, and switch traffic.

I prevent conflicting writes where the application requires a single writer. Before traffic moves, I check security, certificates, DNS, and application readiness.

Failback is a separate planned operation. I establish the authoritative data source, synchronize changes, validate the primary environment, and perform an approved cutover.

I do not assume reversing a DNS record safely returns everything to normal.”

[⬆ Go to top](#top)

### 61. How often should recovery drills run?

“I set frequency according to criticality, policy, and the rate of change. Critical workloads need more frequent validation than low-impact systems.

I also retest after significant changes to infrastructure, databases, IAM, encryption, networking, or application dependencies. Scheduled automated restore tests can complement broader business recovery exercises.

The key is that the evidence remains representative of the current environment. An old successful drill may no longer prove recoverability after major changes.”

**Closing line for this topic:** “I consider recovery validated when the business transaction works, the measured recovery meets the agreed objectives, and the responsible owners have signed off on the evidence.”

[⬆ Go to top](#top)

## Hands-on commands and interpretation

### Command set A — EC2 access and SSH

Run client commands from the approved source:

```bash
ssh -vvv -i key.pem ec2-user@<host>
nc -vz -w 5 <host> 22
```

Run host commands through an available approved connection:

```bash
sudo systemctl status sshd   # Common on RHEL/Amazon Linux
sudo systemctl status ssh    # Common on Ubuntu
sudo ss -lntp
df -h
sudo journalctl -u sshd --since "30 minutes ago"
```

| Symptom | Investigation |
|---|---|
| Timeout | Routes, filtering, reachability, unresponsive host |
| Connection refused | Listener, service, active firewall rejection |
| Permission denied | Username, key, account and authentication logs |

Authentication logs may be in `/var/log/secure`, `/var/log/auth.log`, or the journal depending on OS configuration.

[⬆ Go to top](#top)

### Command set B — CPU, memory, disk, and application health

```bash
uptime
top
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head
free -m
vmstat 1 5
df -h
df -i
sudo journalctl -k --since "1 hour ago"
sudo systemctl status <application-service>
sudo journalctl -u <application-service> --since "30 minutes ago"
curl --max-time 10 -sS -o /dev/null \
  -w 'HTTP=%{http_code} Total=%{time_total}s\n' \
  http://localhost:8080/health
```

| Evidence | Next investigation |
|---|---|
| High CPU | Busy process, traffic, jobs, loops |
| Low available memory and swapping | Leak, process size, increased demand |
| Full filesystem or exhausted inodes | Logs, temporary files, small-file accumulation |
| Normal host metrics but slow requests | Database, pool limits, downstream APIs |
| Failure immediately after release | Release behavior and rollback readiness |

CloudWatch Logs Insights example:

```text
fields @timestamp, @logStream, @message
| filter @message like /ERROR|Exception|timeout/
| sort @timestamp desc
| limit 100
```

[⬆ Go to top](#top)

### Command set C — RDS connectivity

```bash
dig +short <rds-endpoint>
nc -vz -w 5 <rds-endpoint> 3306   # MySQL example
```

A successful TCP test proves a connection can be established, not that database authentication or queries succeed. Use the appropriate database client or application transaction for final validation.

[⬆ Go to top](#top)

### Command set D — Load-balancer targets

```bash
sudo systemctl status <application-service>
sudo ss -lntp
curl -v --max-time 5 http://localhost:8080/health
# Run the following from an approved host with access to the target:
curl -v --max-time 5 http://<target-private-ip>:8080/health
```

A listener bound only to `127.0.0.1` can pass local checks while being unreachable to the load balancer. Verify that the health endpoint does not unexpectedly require authentication or redirect.

[⬆ Go to top](#top)

### Command set E — DNS, routes, and TLS

```bash
dig <application-hostname>
nslookup <application-hostname>
cat /etc/resolv.conf
ip route
nc -vz -w 5 <destination> <port>
curl -v --max-time 10 https://<hostname>/health
openssl s_client -connect <hostname>:443 -servername <hostname>
```

[⬆ Go to top](#top)

### Command set F — Windows administration

```powershell
Get-Service -Name <service-name>
Get-Volume
Get-WinEvent -FilterHashtable @{
    LogName = 'System'
    StartTime = (Get-Date).AddMinutes(-30)
} -MaxEvents 30
Resolve-DnsName <hostname>
Test-NetConnection <hostname> -Port 443
```

Also inspect Application events and the application's own logs as appropriate.

[⬆ Go to top](#top)

### Command set G — AWS identity, SSM, and Auto Scaling

```bash
aws sts get-caller-identity
aws s3api head-object --bucket <bucket> --key <object-key>
aws ssm describe-instance-information
aws ssm start-session --target <instance-id>
aws autoscaling describe-scaling-activities \
  --auto-scaling-group-name <group-name>
sudo systemctl status amazon-ssm-agent
sudo tail -n 100 /var/log/amazon/ssm/amazon-ssm-agent.log
```

Agent service and log locations can vary by installation method. CLI use requires appropriate credentials, Region configuration, and tools; CLI Session Manager sessions also require the Session Manager plugin.

[⬆ Go to top](#top)

## AWS console step-by-step walkthroughs

### Walkthrough 1 — EC2 inaccessible (Questions 2, 22, 31)

1. Open **EC2 → Instances** and select the instance.
2. Review **Status and alarms** for failed checks.
3. Open **Networking** and confirm IP, subnet, VPC, and interface.
4. Open **Security** and select the attached security group.
5. Check the required port from the approved source.
6. Open **VPC → Route tables** and locate the subnet's associated table.
7. Verify the intended VPN, Transit Gateway, or internet route.
8. Open **VPC → Network ACLs** and inspect request and return rules.
9. Return to **EC2 → instance → Connect → Session Manager**, if available.
10. Inspect service status, firewall, authentication logs, and disk capacity.

**Verify:** Reconnect using the original approved method and test application health. Use approved Windows access and Event Viewer where applicable.

[⬆ Go to top](#top)

### Walkthrough 2 — CloudWatch alarms and slowness (Questions 5, 6, 18)

1. Open **CloudWatch → Alarms → All alarms**.
2. Select the alarm and inspect its metric, dimensions, threshold, and history.
3. Set the time range around the incident, including the period before it.
4. Open **Metrics → All metrics** and compare the relevant metrics below.
5. Open **Logs → Logs Insights**, select log groups and the same period.
6. Search for errors, exceptions, and timeouts.
7. Compare evidence with deployment and change timestamps.

| Component | Metrics |
|---|---|
| EC2 | `CPUUtilization`, `StatusCheckFailed`, `NetworkIn`, `NetworkOut` |
| CloudWatch agent | `mem_used_percent`, `disk_used_percent` |
| ALB | `TargetResponseTime`, `HealthyHostCount`, `HTTPCode_Target_5XX_Count`, `HTTPCode_ELB_5XX_Count` |
| RDS | `CPUUtilization`, `DatabaseConnections`, `FreeableMemory`, `FreeStorageSpace` |

**Verify:** Run a business transaction and observe stable latency, errors, and resource usage. An alarm clearing alone does not prove recovery.

**Create an alarm:**

1. Choose **Alarms → Create alarm → Select metric**.
2. Select the correct resource metric.
3. Set statistic, period, threshold, and evaluation criteria.
4. Configure missing-data treatment.
5. Select the SNS notification destination.
6. Name and create the alarm.
7. Test notifications and the operational response process.

[⬆ Go to top](#top)

### Walkthrough 3 — EC2 to RDS (Question 4)

1. Open **RDS → Databases → select database**.
2. Confirm **Available** status.
3. Open **Connectivity & security**.
4. Confirm endpoint, port, VPC, and security groups.
5. Inspect database inbound access from the application's approved source.
6. Inspect application outbound rules.
7. Check routes and network ACLs; verify connecting networks for separate VPCs.
8. Connect to EC2 through an approved method and test DNS and TCP.
9. If TCP works, investigate credentials, TLS, permissions, and connection limits.

**Verify:** Complete a real application database transaction.

[⬆ Go to top](#top)

### Walkthrough 4 — RDS performance and availability (Question 28)

1. Open **RDS → Databases → select database**.
2. Review **Monitoring** for CPU, connections, memory, storage, and latency.
3. Review **Logs & events** for maintenance, restart, failover, and errors.
4. Inspect available database logs at the relevant timestamps.
5. Use **CloudWatch Database Insights**, where configured, to investigate load.
6. Work with DBAs or developers on queries, locks, and pools.
7. Review capacity or parameter changes through the change process.

**Verify:** Business transactions, response times, and connection counts recover.

[⬆ Go to top](#top)

### Walkthrough 5 — Unhealthy load-balancer target (Question 10)

1. Open **EC2 → Target Groups → select group**.
2. Open **Targets** and read unhealthy-target reasons.
3. Open **Health checks**.
4. Check protocol, port, path, matcher, timeout, and thresholds.
5. Open **EC2 → Load Balancers → select load balancer**.
6. Review **Listeners and rules** and target-group selection.
7. Check load-balancer and target security groups where applicable.
8. Access the target and test its endpoint locally and over the private network.
9. Investigate logs and release changes; use approved correction or rollback.

**Verify:** Healthy targets, successful requests through the load balancer, and normal errors/latency.

[⬆ Go to top](#top)

### Walkthrough 6 — Auto Scaling launch failures (Questions 26, 27)

1. Open **EC2 → Auto Scaling Groups → select group**.
2. Inspect minimum, desired, and maximum capacity.
3. Open **Activity** and read failure details.
4. Open **Automatic scaling** and inspect policies and alarms.
5. Review the launch template and selected version.
6. Verify AMI, instance type, role, security groups, and storage.
7. Check subnet addresses and applicable quotas.
8. Inspect lifecycle hooks and initialization failures.
9. For encrypted storage, check service-linked role access to KMS.

**Verify:** Instances launch, reach **InService**, pass target checks, and serve requests.

[⬆ Go to top](#top)

### Walkthrough 7 — S3 security and AccessDenied (Questions 23, 24)

1. Open **S3 → Buckets → select bucket → Permissions**.
2. Review Block public access, bucket policy, and Object Ownership.
3. Open **Properties** and inspect encryption and versioning.
4. Open **IAM → Roles → application role → Permissions**.
5. Distinguish bucket-level and object-level actions and ARN scope.
6. For SSE-KMS, open **KMS → Customer managed keys → select key** and inspect key status and access.
7. If using an endpoint, open **VPC → Endpoints** and inspect its policy.
8. Review organizational controls and explicit denies.

**Verify:** Repeat the failed action with the real application role and original network path, and test that disallowed actions remain denied.

[⬆ Go to top](#top)

### Walkthrough 8 — EBS expansion (Question 25)

1. Open **EC2 → Volumes** and identify the attachment.
2. Review size, type, encryption, and device.
3. Confirm backup, consistency, and approved change requirements.
4. Choose **Actions → Modify volume**.
5. Enter the approved size or performance settings.
6. Monitor modification progress.
7. Access the host, inspect partition/filesystem layout, and extend appropriately.

```bash
lsblk -f
df -hT
```

**Verify:** Increased filesystem capacity and successful application writes. Do not assume that modifying the AWS volume grows the filesystem.

[⬆ Go to top](#top)

### Walkthrough 9 — IAM least privilege and temporary access (Questions 8, 43)

1. Open **IAM → Roles → select role**.
2. Review permissions and resource scope.
3. Review any permissions boundary.
4. Review **Trust relationships** and allowed principals.
5. Check relevant resource policies and organizational controls.
6. Use **IAM Access Analyzer** for supported findings and validation.
7. Record approved temporary elevation and its removal or expiry.
8. Review relevant management actions in **CloudTrail → Event history**.

**Verify:** Required work succeeds and unrelated access remains denied. Event history is not a complete data-access audit; configure data events where needed.

[⬆ Go to top](#top)

### Walkthrough 10 — Secure remote administration (Questions 13, 32, 43)

1. Open **Systems Manager → Session Manager → Start session**.
2. Select the managed node and start the session.
3. Perform approved diagnostics and end the session.
4. Review **Session Manager → Preferences** for configured logging and encryption.
5. If unavailable, inspect agent, role, DNS, and endpoint connectivity.

**Verify:** Approved access works and configured audit records are retained. Standard session-content logging does not capture SSH or port-forwarding sessions.

[⬆ Go to top](#top)

### Walkthrough 11 — Patch Manager (Questions 16, 34)

1. Open **Systems Manager → Patch Manager**.
2. Review baselines and compliance.
3. Choose **Patch now → Scan** and target intended instances or tags.
4. Review missing patches and failures.
5. During the approved window, use **Install** with agreed reboot behavior.
6. Inspect execution status and per-node output.
7. Validate canaries before wider rollout.
8. Review post-patching compliance.

**Verify:** Patch status, reboots, services, target health, and business transactions. Coordinate traffic draining separately; Patch now does not automatically implement application-aware draining. A no-reboot choice does not guarantee patches are fully effective without a later reboot.

[⬆ Go to top](#top)

### Walkthrough 12 — Inventory and State Manager (Question 33)

**Inventory:**

1. Open **Systems Manager → Inventory**.
2. Configure collection if not already enabled.
3. Select targets, data collection, and schedule.
4. Review collected information and timestamps.
5. Investigate failed collection.

**State Manager:**

1. Open **Systems Manager → State Manager → Create association**.
2. Select an approved document and parameters.
3. Select targets using environment and ownership tags.
4. Configure schedule, concurrency, and error controls.
5. Create the association and review execution history and compliance.

**Verify:** Inspect actual configuration on representative nodes, not only association status.

[⬆ Go to top](#top)

### Walkthrough 13 — Route 53 (Question 14)

1. Open **Route 53 → Hosted zones → select zone**.
2. Confirm public or private zone type.
3. Inspect record name, type, value/alias, and routing policy.
4. For public DNS, verify registrar delegation matches zone name servers.
5. For private DNS, verify VPC associations.
6. Open **VPC → Your VPCs** and review DNS settings.
7. For hybrid DNS, inspect Resolver endpoints and forwarding rules.
8. Test resolution from the affected network and consider TTL/cache behavior.

**Verify:** Correct resolution and successful application access from the original client.

[⬆ Go to top](#top)

### Walkthrough 14 — Restore and DR validation (Questions 17, 37, 38)

1. Open **AWS Backup → Backup vaults → select vault**.
2. Select the relevant recovery point.
3. Check source resource, timestamp, status, and encryption.
4. Choose **Restore**.
5. Enter resource-specific settings, networking, location, and restore role.
6. Restore into the approved isolated test or recovery environment.
7. Open **Jobs → Restore jobs** and monitor progress.
8. Validate resource health, data integrity, and business transactions.
9. Record actual recovery time and recovery point.

**RDS native point-in-time recovery:** Open **RDS → Automated backups**, select the database, and choose **Restore to point in time**. Validate the restored database before changing application connectivity. Exact supported recovery operations depend on database deployment type.

**Verify:** Application/database owners confirm functionality and data; record gaps and corrective actions.

[⬆ Go to top](#top)

### Walkthrough 15 — CloudFormation changes and drift (Questions 11, 35)

1. Open **CloudFormation → Stacks → select stack**.
2. Review Resources, Parameters, Outputs, and Events.
3. Create a change set for the proposed update.
4. Inspect additions, modifications, deletions, and replacement indicators.
5. Obtain required approval and execute the change set.
6. Monitor events and investigate failures or rollback.
7. Use **Detect drift** where supported.

**Verify:** Resource state and application behavior. Terraform normally runs through CLI/CI; use AWS consoles to inspect the resulting resources.

[⬆ Go to top](#top)

### Walkthrough 16 — Cost and performance (Questions 19, 39)

1. Open **Billing and Cost Management → Cost Explorer**.
2. Select the relevant period and group by service, account, or activated allocation tag.
3. Identify growth and unexpected charges.
4. Review **Compute Optimizer** recommendations where available.
5. Validate against workload requirements and monitoring.
6. Inspect candidates in EC2, EBS, RDS, and S3.
7. Agree with application owners and implement an approved change.

**Verify:** Compare costs over a suitable period while checking performance and availability. Include peak and seasonal demand in rightsizing decisions.

[⬆ Go to top](#top)

## Automation examples

### Terraform — Three-tier AWS project

Use your three-tier project as the concrete example, choosing the actual version you implemented rather than mixing the original and simplified architectures.

**Interview answer:**

“I used Terraform to provision environment-specific infrastructure for a three-tier application. I separated reusable configuration from dev, UAT, and production inputs and integrated deployments with GitHub Actions using OIDC. I reviewed plans and infrastructure security checks before deployment, then verified networking, compute, database connectivity, and application behavior. Production changes required approval and an appropriate recovery plan.”

```bash
terraform fmt -check -recursive
terraform init
terraform validate
terraform plan -var-file=dev.tfvars -out=tfplan
terraform show tfplan
terraform apply tfplan
```

**Discuss:** Module consumers, environment inputs, state protection and locking, OIDC permissions, plan review, security checks, deployment gates, and post-deployment verification. Describe only tools actually used in that project's pipeline.

**Rollback:** Reverting Git does not automatically undo an infrastructure change. Review a new plan against current state. Resource replacement or data changes may require restoration and application coordination. Do not assume reverting state is a rollback method.

[⬆ Go to top](#top)

### Python — EC2/EBS operational report

**Sample or proposed design, unless already implemented:**

1. Confirm account and Region.
2. Paginate through EC2 instances and EBS volumes.
3. Gather ownership/environment tags and resource state.
4. Query monitoring over an agreed observation period.
5. Mark missing metrics as unknown, not zero usage.
6. Generate candidate findings with reasons and evidence.
7. Exclude protected workloads and obtain owner validation.
8. Execute any approved cleanup separately with safeguards.
9. Log per-resource outcomes and partial failures.

**Discuss:** Boto3 clients, pagination, retries, least-privilege role, dry run, logging, nonproduction testing, and why low CPU alone is insufficient evidence for termination.

[⬆ Go to top](#top)

### Bash and PowerShell operational examples

- Bash: collect service, disk, and memory diagnostics into a timestamped report.
- PowerShell: collect Windows service status, event logs, and disk capacity.
- Use controlled targets, avoid secrets in output, preserve exit/error information, and validate results.

[⬆ Go to top](#top)

## Production support and communication

### Prioritization and escalation

Use the organization's severity model. Critical service outage, widespread business disruption, data-integrity risk, and security incidents require appropriate urgency. Engage application, networking, database, infrastructure, security, and AWS Support based on evidence.

[⬆ Go to top](#top)

### Change and rollback preparation

Before a production change, document:

- Scope and affected resources.
- Business impact and maintenance window.
- Approval and responsible engineer.
- Prerequisites and backup/recovery needs.
- Execution steps and monitoring.
- Rollback trigger, steps, and owner.
- Success criteria and application-owner validation.

Emergency work follows the established emergency-change process; urgency does not remove the need for traceability.

[⬆ Go to top](#top)

### Incident update example

“Users are experiencing elevated errors on the application. We have isolated the issue to two unhealthy targets following the latest release. The application team is validating rollback, and we will provide the next update in 15 minutes.”

[⬆ Go to top](#top)

### Root-cause analysis

Record impact, timeline, detection, trigger, root cause, contributing factors, restoration actions, and validation evidence. Corrective actions need owners and deadlines. Include monitoring, automation, testing, and documentation improvements. Avoid assigning blame in place of identifying system and process weaknesses.

[⬆ Go to top](#top)

### Runbook outline

1. Purpose and symptom.
2. Scope, prerequisites, and required access.
3. Diagnostic steps and expected outputs.
4. Decision points and escalation conditions.
5. Approved recovery actions.
6. Rollback criteria and procedure.
7. Business and technical validation.
8. Evidence and ticket closure requirements.
9. Owner, review date, and revision history.

[⬆ Go to top](#top)

## Security review

| Area | Practical interview response |
|---|---|
| IAM | Temporary credentials, workload roles, scoped actions/resources, periodic reviews |
| Encryption | EBS/RDS encryption, appropriate KMS key access, TLS in transit |
| Security groups | Required ports from approved sources; workload group references where appropriate |
| Production access | Session Manager where supported, restricted permissions, privileged-access MFA |
| Secrets | Secrets Manager instead of credentials embedded in code |
| Auditability | CloudTrail API activity plus configured operational execution records |
| S3 | Block unintended public access, scoped policies, encryption, versioning/retention as required |
| EC2 | Approved AMIs, patch compliance, IMDSv2 where required, managed agents |

Distinguish IAM permissions from network access and database authentication. They protect different layers. Standard Session Manager content logging does not capture SSH or port-forwarding content. CloudTrail Event history is not a substitute for configured data-access logging.

## Teams-call preparation

Have these three examples ready:

1. **Production incident:** Personal actions, logs/metrics, root cause, restoration, and validation.
2. **IaC change:** Infrastructure, environment inputs, review/security checks, approvals, and recovery plan.
3. **Script:** Inputs, selection criteria, error handling, output, and safeguards.

Practice Questions 2, 5, 6, 10, and 15 aloud. Explain what evidence would lead you to the next step rather than only listing services.

### Work arrangement and authorization

Use current facts; do not assume location or status:

“My current location is **[city, state]**, and my availability for the Spring, TX hybrid schedule is **[availability]**. My current work authorization is **[actual status]**.”

The recruiter lists USC/GC as a requirement. If your authorization differs, clarify eligibility with the recruiter rather than representing it as citizenship or permanent residency.

[⬆ Go to top](#top)

### Questions to ask the interviewer

- Which applications are most critical, and what are their recovery objectives?
- How are on-call responsibilities and incident escalation organized?
- What is the current patching and backup-validation process?
- How much infrastructure is managed through Terraform or CloudFormation?
- Which operational improvements would you want this engineer to deliver first?

**Closing interview sentence:** “I document the evidence, make the approved correction, and verify the business service before closing the incident.”

[⬆ Go to top](#top)

## Official AWS references

The guide is based on the provided role and official AWS documentation checked during this preparation. Console labels and supported features can change.

- [EC2 connection troubleshooting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html)
- [VPC security groups and network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/infrastructure-security.html)
- [CloudWatch agent metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.html)
- [Standard EC2 CloudWatch metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)
- [Application Load Balancer troubleshooting](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-troubleshooting.html)
- [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [RDS automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
- [RDS database logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html)
- [Route 53 private hosted-zone considerations](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-considerations.html)
- [S3 AccessDenied troubleshooting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/troubleshoot-403-errors.html)
- [Extend an EBS filesystem](https://docs.aws.amazon.com/ebs/latest/userguide/recognize-expanded-volume-linux.html)
- [Auto Scaling troubleshooting](https://docs.aws.amazon.com/autoscaling/ec2/userguide/CHAP_Troubleshooting.html)
- [Auto Scaling launch failures](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ts-as-instancelaunchfailure.html)
- [Session Manager prerequisites](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-prerequisites.html)
- [Session Manager logging](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging.html)
- [Systems Manager tools](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-tools.html)
- [Patch now operations](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-patch-now-on-demand.html)
- [AWS Backup restoration](https://docs.aws.amazon.com/aws-backup/latest/devguide/restoring-a-backup.html)
