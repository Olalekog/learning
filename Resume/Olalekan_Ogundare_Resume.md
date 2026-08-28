# OLALEKAN G. OGUNDARE

+1-214-564-5701 | ogogundare@gmail.com | [linkedin.com/in/olalekan-o-08276144](https://www.linkedin.com/in/olalekan-o-08276144/)

**Senior Infrastructure | DevOps and Platform Engineer**

---

## Summary

Senior Infrastructure, DevOps, and Platform Engineer with 10+ years designing, automating, and securing large-scale AWS and Azure environments — building the reusable platforms, pipelines, and guardrails other engineering teams build on, not just point solutions. Deep expertise in Infrastructure as Code (Terraform), Kubernetes (EKS), CI/CD pipeline engineering (Jenkins, GitHub Actions, Harness), and embedding security controls (SAST, IaC scanning, policy-as-code) directly into the software delivery lifecycle — the DevSecOps discipline of making the secure path the default path. Modernized multi-account, multi-billion-dollar cloud platforms to 99.99% availability and 40% faster deployments, while operating in regulated financial and healthcare environments (SOC 2, HIPAA).

---

## Core Technical Skills

| Category | Skills |
|---|---|
| **Cloud Platforms** | AWS (EC2, VPC, S3, EBS, EFS, FSx, RDS, DynamoDB, EKS, Fargate, ECS, Lambda, IAM, KMS, CloudFront, Route 53, ELB, SNS/SQS, EventBridge, Organizations, Control Tower), Microsoft Azure (VMs, VM Scale Sets, AKS, Container Apps, VNet, Storage, Entra ID, Azure Policy, hybrid connectivity) |
| **Infrastructure as Code** | Terraform (modules, remote state, Sentinel/OPA policy gates), Terragrunt, Bicep, AWS CloudFormation, Ansible |
| **Containers & Orchestration** | Kubernetes (EKS), Docker, Helm, multi-tenant RBAC & namespace isolation |
| **CI/CD & DevOps Tooling** | Azure DevOps (Pipelines, Boards, Repos, Artifacts), Jenkins, GitHub Actions, Harness, GitLab CI, Bitbucket Pipelines |
| **DevSecOps & Security** | SAST, dependency/secret/container scanning, IaC security gates (OPA, Sentinel), IAM/SCP/NACL enforcement, GuardDuty, Security Hub, Inspector, CloudTrail, IAM Access Analyzer, CrowdStrike, Qualys, Tanium, Microsoft Entra ID (Conditional Access, Privileged Identity Management, App Registrations, Identity Governance) |
| **Observability** | CloudWatch, Prometheus, Grafana, ELK/OpenSearch, Fluentd/Fluent Bit, Kafka/MSK monitoring, ServiceNow incident automation |
| **FinOps & Cost Optimization** | Rightsizing, Savings Plans, Spot instances, lifecycle automation, cost governance/reporting |
| **Storage & Data Protection** | SAN/NAS (Hitachi, EMC VMAX/VSP, NetApp), backup/DR (Avamar, SRDF, TrueCopy, Azure Backup, Azure Site Recovery, AWS Backup), FSx Lustre |
| **Big Data & Analytics** | Hadoop, Apache Spark, AWS EMR, ETL pipeline development |
| **MLOps & AI/ML Platforms** | AWS SageMaker (Pipelines, Model Registry, endpoints), Azure Machine Learning (pipelines, model registry), Amazon Bedrock, model CI/CD, automated retraining/monitoring |
| **Programming & Scripting** | Python (PySpark, pandas), Bash |

---

## Professional Experience

### Cloud and DevOps Engineering
**Tech Consulting** | May 2026 – Present

- Led AWS and Azure platform engineering for client engagements — building reusable landing zone patterns, self-service infrastructure modules, and golden-path Terraform/ARM templates that client engineering teams adopted directly instead of provisioning environments by hand.
- Built and operated cloud compute, storage, and serverless platforms across Azure (Virtual Machines, VM Scale Sets, Azure Batch, Storage Accounts, Azure Functions, App Services, Container Apps) and AWS (EC2, S3, Lambda, EBS, Fargate, ECS) for client workloads.
- Deployed and managed containerized platforms on Azure Kubernetes Service (AKS) and Amazon EKS — node pool/Cluster Autoscaler and Karpenter-based scaling, Helm-packaged workloads, and multi-tenant namespace isolation — using Terraform, ARM/Bicep templates, and Pulumi for consistent infrastructure-as-code across both providers.
- Built and maintained CI/CD pipelines in Azure DevOps (YAML pipelines, environment approvals), AWS CodePipeline/CodeBuild, and GitHub Actions for automated build/test/deploy, and automated configuration management with Ansible.
- Implemented cloud security controls across both platforms — Azure RBAC/NSGs/Key Vault/Defender for Cloud/Azure Policy, and AWS IAM/SCPs/Security Groups/KMS/GuardDuty/Security Hub — for continuous posture monitoring and encryption at rest/in transit.
- Administered Microsoft Entra ID identity and access management for client tenants — Conditional Access policies (MFA and device-registration enforcement), Privileged Identity Management for just-in-time role elevation, and App Registrations/Enterprise Applications governance.
- Designed backup, disaster recovery, and resilience strategies using Azure Backup and Azure Site Recovery (cross-region failover, RTO/RPO-driven recovery tiers) alongside AWS Backup and cross-region replication, validated through regular recovery drills rather than assuming failover would work untested.
- Configured hybrid and multi-cloud network connectivity (Azure VNet/Hub-and-Spoke/ExpressRoute, AWS VPC/Transit Gateway/Direct Connect, site-to-site VPN) and set up Azure Front Door and AWS CloudFront for low-latency application delivery.
- Monitored performance, availability, and cost using Azure Monitor + Cost Management and AWS CloudWatch + Cost Explorer; implemented auto-scaling and caching to optimize workload efficiency and spend across both clouds.
- Built MLOps pipelines for model training, versioning, and deployment across cloud-native ML platforms — AWS SageMaker and Azure Machine Learning — integrating CI/CD, model registries, and automated retraining/monitoring workflows for production ML services.

### AVP, Public Cloud Service — Cloud Engineering & DevOps
**Citibank** | Irving, Texas | Feb 2023 – Apr 2026

**Infrastructure as Code & Automation**
- Designed and built reusable Terraform modules and golden templates standardizing AWS deployments (VPC, EC2, ALB, ASG, RDS, S3, IAM, KMS, CloudWatch, SNS, SQS, EventBridge, FSx) across dev, UAT, and production accounts.
- Managed Terraform remote state via S3 backend with DynamoDB locking to eliminate state conflicts across teams.
- Automated infrastructure and ML platform deployments using Terraform, Ansible, Jenkins, and Bitbucket CI/CD, cutting manual provisioning ~45% and improving deployment speed up to 65% (CloudFormation/Ansible workflows).
- Migrated legacy Jenkins pipelines to GitHub Actions and Harness, reducing pipeline maintenance overhead and improving deployment reliability and release consistency across environments.

**Kubernetes & Containers**
- Managed EKS clusters running distributed, compute-intensive workloads at scale, including containerized batch processing, inference services, and microservices.
- Designed multi-tenant Kubernetes environments with RBAC, namespace isolation, and resource governance for secure multi-team usage.

**DevSecOps**
- Embedded security scanning directly into CI/CD pipelines — SAST, dependency scanning, secret scanning, container scanning, and IaC security checks — shifting vulnerability detection left of production.
- Enforced Terraform security gates using OPA and Sentinel to block non-compliant infrastructure changes before apply.
- Supported enterprise security monitoring and response using GuardDuty, Security Hub, Inspector, AWS Config, CloudTrail, KMS, and IAM Access Analyzer.
- Built and hardened golden AMIs (RHEL, Amazon Linux 2023) via EC2 Image Builder, integrating CrowdStrike Falcon, Qualys, and Tanium for endpoint protection, CVE remediation, and compliance validation; administered Qualys patch management (agents, asset groups, deployment jobs, post-patch compliance reporting).
- Enforced least-privilege access and network controls using IAM, Service Control Policies, security groups, and NACLs.

**Observability & Reliability**
- Implemented full-stack observability across CloudWatch, Prometheus, Grafana, and the ELK/OpenSearch stack, including Fluentd/Fluent Bit log forwarding and Kafka/MSK pipeline monitoring — reducing incident detection and recovery time 35%.
- Built real-time operational dashboards and alerting integrated with ServiceNow for proactive incident response and root-cause analysis.

**Cost Governance**
- Directed FinOps cost governance — rightsizing, Savings Plans, Spot usage, and automated FSx lifecycle policies — delivering sustained 20–25% infrastructure cost savings while maintaining platform resilience.

**AI/ML & HPC Infrastructure (highlights)**
- Architected AWS-based HPC/AI-ML platform infrastructure (EKS, FSx for Lustre, SageMaker, Bedrock) supporting distributed training, inference, and RAG pipelines integrating Bedrock and OpenSearch.
- Optimized FSx for Lustre throughput and S3-backed dataset access, improving large-scale data processing performance 30%+.

**Big Data & Analytics**
- Provisioned and automated Hadoop/Spark cluster lifecycle on AWS EMR using Terraform, supporting distributed batch processing for analytics and ML training pipelines.
- Built Python-based ETL pipelines (PySpark, pandas) processing large-scale datasets between S3-backed data lakes and downstream analytics/ML workloads.
- Developed Python automation and tooling for infrastructure orchestration, data validation, and operational reporting across the platform.

### Infrastructure Cloud Engineer
**Cynet Systems** (Client: State Farm) | Dec 2022 – Feb 2023

- Administered cloud infrastructure across OS, database, and network layers, primarily in Microsoft Azure.
- Evaluated existing data center environments and designed cost-efficient solutions addressing business requirements.
- Planned and implemented server upgrades, maintenance fixes, and vendor patches; performed capacity planning.
- Supported new Azure cloud implementations alongside existing on-premises virtualization, compute, and storage platforms.
- Managed Docker/Helm CI/CD pipelines, enabling consistent global releases and faster developer delivery.

### Cloud Infrastructure Engineer
**Dell EMC / VirtualTechGuru** (Client: Texas A&M University) | College Station, TX | Nov 2022 – Dec 2022

- Led hybrid and multi-cloud infrastructure design and deployment, improving system scalability and resilience.
- Directed cloud migration and modernization initiatives, achieving $1.2M in cost savings.
- Configured hybrid connectivity via VPN/ExpressRoute, securing data transfer between on-prem VMware and Azure.
- Executed large-scale VM migrations — replication setup, test failovers, and production cutovers — with minimal disruption.
- Implemented monitoring and reliability strategies that reduced incidents 25% across enterprise systems.

### Infrastructure Cloud Engineer
**Luminous Logistic** (Client: CloudWave Healthcare Solutions) | MA, USA | Jan 2019 – Jun 2022

- Architected and scaled hybrid/multi-cloud AWS infrastructure (VPC, EC2, ELB, RDS, Transit Gateway) across multiple regions.
- Designed a multi-account landing zone using AWS Organizations and Control Tower, with accounts structured into Dev, Non-Prod, Prod, Security, and Shared Services OUs for isolation and governance.
- Developed Service Control Policies enforcing encryption, region restrictions, and public-access blocks; implemented preventive and detective Control Tower guardrails for continuous compliance.
- Secured hybrid connectivity between AWS VPCs and the corporate network using VPC Peering, VPN, and Transit Gateway.
- Centralized audit logging via CloudTrail, AWS Config, and S3 Object Lock for immutable long-term retention.
- Integrated organization-wide GuardDuty and Security Hub with centralized monitoring and alerting.
- Automated account provisioning and governance controls using Terraform and CI/CD pipelines.
- Partnered with security and compliance teams to maintain HIPAA and SOC 2 controls, supporting secure healthcare data interoperability (HL7, FHIR) across regulated platforms.

### Senior Enterprise Server and Storage Specialist
**Computer Warehouse Ltd.** (Client: MTN Nigeria) | Lagos, Nigeria | Apr 2011 – Mar 2018

- Led enterprise SAN/NAS infrastructure (Hitachi, EMC VMAX/VSP, NetApp) for hybrid/multi-cloud environments, improving storage efficiency 30%.
- Architected replication and disaster recovery solutions (SRDF, TrueCopy, Shadow-Image), cutting recovery time 40%.
- Directed Kubernetes and Terraform platform integration, accelerating deployment speed and reliability for distributed teams.
- Developed documentation and operational templates that reduced project delivery time and incident resolution by 25%.

---

## Certifications

| | |
|---|---|
| AWS Certified Solutions Architect – Professional | AWS Certified Solutions Architect – Associate |
| AWS Certified Security – Specialty | AWS Certified SysOps Administrator – Associate |
| HashiCorp Certified: Terraform Associate | AWS Certified Developer – Associate |
| Certified Kubernetes Administrator (CKA) | AWS Certified Cloud Practitioner |
| Kubernetes and Cloud Native Associate (KCNA) | FinOps Certified Practitioner |
| Microsoft Certified: Azure Fundamentals | |

---

## Education

**Postgraduate Diploma, Information System Management** — University of Liverpool, UK (2015)
**BSc Equivalent, Electrical and Electronics Engineering** — The Polytechnic, Ibadan, Nigeria (2002)

---

## Leadership & Recognition

- Defined cloud platform standards and automation practices, boosting operational efficiency 35%.
- Directed hybrid/multi-cloud governance initiatives, improving reliability and developer velocity org-wide.
- Mentored engineering teams on IaC, observability, and platform automation best practices.
- **CITIBank Cloud Innovation Award** — delivering high-throughput, resilient cloud platforms.
- Recognized for $1.2M in infrastructure savings via hybrid/multi-cloud modernization (Texas A&M engagement).
- Honored for achieving 99.99% uptime and excellence in multi-region cloud reliability.
