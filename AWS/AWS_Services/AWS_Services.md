# AWS Services — Exam & Interview Ready Guide

## Overview

AWS provides cloud services used to design, deploy, secure, monitor, and scale modern applications. These services are grouped into categories such as compute, storage, database, networking, security, monitoring, DevOps, analytics, AI/ML, migration, and cost management.

A strong AWS engineer should understand what each service does, its defining characteristics, when to use it, and — critically for interviews — *why* it would be chosen over a similar service with respect to cost, scalability, efficiency, and security.


---

## AWS Services Architecture Diagram

```mermaid
flowchart TB
    Users[Users / Clients] --> R53[Amazon Route 53
DNS]
    R53 --> CF[Amazon CloudFront
CDN]
    CF --> WAF[AWS WAF
Web protection]
    WAF --> ALB[Application Load Balancer]

    ALB --> APP[Compute Layer
EC2 / ECS / EKS / Lambda]
    APP --> DB[Database Layer
RDS / Aurora / DynamoDB]
    APP --> S3[Storage Layer
S3 / EBS / EFS / FSx]

    IAM[IAM / IAM Identity Center
Access control] --> APP
    KMS[AWS KMS
Encryption keys] --> DB
    KMS --> S3
    SM[Secrets Manager
Secrets and credentials] --> APP

    CW[CloudWatch
Metrics, logs, alarms] --> APP
    CT[CloudTrail
API audit logs] --> IAM
    CFG[AWS Config
Compliance tracking] --> DB
    SH[Security Hub / GuardDuty
Security findings] --> IAM
```

---

## Secure 3-Tier AWS Application Flow

```mermaid
sequenceDiagram
    participant User
    participant DNS as Route 53
    participant CDN as CloudFront + WAF
    participant ALB as Application Load Balancer
    participant App as App Tier: EC2/ECS/EKS/Lambda
    participant DB as Data Tier: RDS/DynamoDB
    participant Logs as CloudWatch/CloudTrail

    User->>DNS: Request application URL
    DNS->>CDN: Resolve domain and route traffic
    CDN->>ALB: Forward allowed HTTPS request
    ALB->>App: Route request to healthy target
    App->>DB: Read/write application data
    DB-->>App: Return response
    App-->>ALB: Return application response
    ALB-->>User: Return HTTPS response
    App->>Logs: Send metrics and logs
    ALB->>Logs: Send access logs
```

---

## AWS DevOps Deployment Flow

```mermaid
flowchart LR
    Dev[Developer] --> Git[GitHub / CodeCommit]
    Git --> CI[CI Pipeline
GitHub Actions / CodeBuild]
    CI --> Scan[Security Checks
SAST, IaC scan, dependency scan]
    Scan --> Build[Build Artifact
Container image or package]
    Build --> ECR[Amazon ECR / S3 Artifact Bucket]
    ECR --> Deploy[Deploy
ECS / EKS / Lambda / EC2]
    Deploy --> Monitor[CloudWatch + X-Ray
Monitoring and tracing]
    Monitor --> Feedback[Feedback to team]
```

---

## AWS Security and Governance Flow

```mermaid
flowchart TB
    ORG[AWS Organizations] --> SCP[Service Control Policies
Prevent risky actions]
    ORG --> CTOWER[AWS Control Tower
Landing zone]
    CTOWER --> ACCOUNTS[Workload Accounts
Dev / Test / Prod / Security / Logging]
    SCP --> ACCOUNTS

    IAM[IAM Identity Center
Centralized access] --> ACCOUNTS
    CLOUDTRAIL[CloudTrail
API audit logs] --> LOGGING[Logging Account]
    CONFIG[AWS Config
Resource compliance] --> SECURITY[Security Account]
    GUARDDUTY[GuardDuty
Threat detection] --> SECURITY
    SECURITYHUB[Security Hub
Central findings] --> SECURITY

    SECURITY --> SNOW[Ticketing / Alerting
ServiceNow, SNS, EventBridge]
```


---

## 1. Compute Services

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **Amazon EC2** | Full OS-level control; wide instance family choice (T/M/C/R/I/G/P, plus Graviton ARM for better price/performance); On-Demand/Reserved/Spot/Savings Plans pricing; billed per second. | Hosting apps, web servers, databases, custom/legacy workloads. | You need OS-level access, specialized licensing, or GPU hardware — vs Lambda/Fargate, steady-state usage priced with a Reserved Instance/Savings Plan is cheaper than per-invocation billing at sustained scale. |
| **AWS Lambda** | Serverless, event-driven; auto-scales per invocation with zero idle cost; max 15-minute runtime; billed per ms + request; built-in multi-AZ HA. | Event-driven automation, APIs, file processing, scheduled jobs. | Traffic is spiky/unpredictable and you want zero idle-capacity cost and no servers to manage — less cost-efficient than EC2 for constant high-throughput workloads where per-invocation pricing exceeds a flat reserved rate. |
| **Amazon ECS** | AWS-proprietary container orchestration; simpler API than Kubernetes; EC2 or Fargate launch type; deep native AWS integration. | Running Docker containers on AWS without Kubernetes complexity. | The team wants lower operational overhead and faster onboarding and doesn't need Kubernetes portability or its ecosystem. |
| **Amazon EKS** | Managed Kubernetes control plane; standard k8s API; portable across clouds; large ecosystem (Helm, operators, GitOps). | Kubernetes-based container workloads, multi-cloud strategies. | Portability/multi-cloud requirements or existing Kubernetes expertise/tooling outweigh the added operational complexity and per-cluster control-plane fee. |
| **AWS Fargate** | Serverless compute launch type for ECS/EKS; no EC2 instances to patch or size; billed per vCPU/memory per task. | Running ECS/EKS containers without managing EC2 instances. | Minimizing operational burden matters more than raw cost — Fargate typically costs more per vCPU-hour than a well-utilized EC2 fleet, so it's most efficient at variable/bursty container load, less so at large constant scale. |
| **Amazon Lightsail** | Simplified VPS bundling compute + storage + networking at flat monthly pricing; simplified console; less flexible than full EC2. | Small websites, blogs, simple dev/test applications. | Simplicity and predictable flat pricing matter more than fine-grained control or scalability — not built for high-scale production workloads. |
| **AWS Batch** | Managed batch job scheduling/queuing across EC2, Spot, or Fargate; automatic dynamic provisioning; built-in retries. | Large-scale processing, rendering, scientific/parallel workloads. | The job runs longer than Lambda's 15-minute cap or needs large/specialized compute across many parallel jobs — pairing with Spot makes it the most cost-efficient option for large batch workloads vs manually managing an EC2 fleet. |

### Interview Keyword
Use **EC2** when you need control over servers, **Lambda** for event-driven serverless workloads, **Fargate** for serverless containers, and **EKS** when Kubernetes is required.

---

## 2. Storage Services

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **Amazon S3** | Object storage; 11 nines durability, 99.99% availability; virtually unlimited scale; storage-class tiering (Standard/IA/Glacier); pay per GB + requests. | Backups, logs, data lakes, static websites. | You need internet-accessible, massively scalable object storage rather than a mountable filesystem — cheapest option for large, infrequently accessed datasets when paired with lifecycle policies. |
| **Amazon EBS** | Block storage attached to a single EC2 instance in one AZ; gp3/io2/st1/sc1 volume types; provisioned IOPS available. | Boot volumes, databases, application disks. | You need low-latency block-level access from exactly one instance — most cost-efficient/performant choice for that pattern, but it doesn't share across instances and isn't durable beyond its AZ without snapshots. |
| **Amazon EFS** | Managed NFS file system; elastic capacity, no pre-provisioning; shared concurrently across many instances/AZs/Lambda; pay per GB used. | Shared Linux storage across EC2/EKS fleets. | Multiple instances need concurrent read/write access to the same files — EBS can't do this; costs more per GB than EBS/S3, but shared access isn't available any other way. |
| **Amazon FSx** (Windows / Lustre / NetApp ONTAP / OpenZFS) | Managed third-party file systems — SMB + AD integration (Windows), sub-millisecond HPC throughput (Lustre), enterprise NAS features like snapshots/dedup/cloning (ONTAP/OpenZFS). | Windows File Server migration, ML/HPC training data, enterprise NAS workloads. | You need native Windows SMB/AD integration, extreme HPC throughput, or NetApp-specific enterprise NAS features EFS doesn't offer. |
| **AWS Backup** | Centralized, policy-based backup across EBS/RDS/DynamoDB/EFS/S3; cross-region/cross-account copy; retention/lifecycle rules. | Backup EC2, EBS, RDS, DynamoDB, and EFS from one place. | You need one policy/schedule/audit trail across many resource types instead of managing backup schedules separately per service — reduces both operational overhead and the compliance risk of a missed service. |
| **Amazon S3 Glacier** (Instant / Flexible / Deep Archive) | Lowest-cost archive tiers; retrieval time ranges from milliseconds (Instant) to ~12 hours (Deep Archive). | Long-term compliance retention (7–10 years), rarely accessed backups. | Data is rarely accessed and a retrieval delay of minutes-to-hours is acceptable — dramatically lower storage cost is the driver, at the expense of retrieval speed. |
| **AWS Storage Gateway** | Hybrid bridge — File/Volume/Tape gateway backing on-prem NFS/SMB/iSCSI/virtual-tape interfaces with S3/EBS. | Connect on-premises storage/backup systems to AWS. | On-prem systems must keep their existing file/block/tape interfaces while data is actually stored durably and cost-effectively in AWS. |

### Interview Keyword
Use **S3** for object storage, **EBS** for EC2 block storage, **EFS** for shared Linux file storage, and **FSx** for managed high-performance file systems.

---

## 3. Database Services

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **Amazon RDS** | Managed relational database (MySQL, PostgreSQL, SQL Server, Oracle, MariaDB); automated patching/backup; Multi-AZ for HA; read replicas for read scaling. | Traditional relational workloads needing a specific engine. | You need an engine Aurora doesn't support (Oracle/SQL Server), or want the lower baseline cost of a standard engine for a smaller workload. |
| **Amazon Aurora** | AWS-built MySQL/PostgreSQL-compatible engine; storage auto-scales to 128TB, decoupled from compute; ~30s failover; up to 15 read replicas; Aurora Serverless v2 auto-scales capacity. | Enterprise relational workloads needing higher throughput/availability than RDS. | Performance, availability, or read-scale requirements justify the higher baseline cost — better price/performance at scale despite the higher entry cost. |
| **Amazon DynamoDB** | Serverless NoSQL key-value/document store; single-digit-ms latency at virtually unlimited scale; On-Demand or Provisioned capacity; DAX for microsecond caching; Global Tables for multi-region. | High-scale key-value/document workloads (session stores, gaming, IoT). | The access pattern is key-based (not complex joins) and needs massive horizontal scale with minimal ops — pay-per-request pricing is more cost-efficient than a provisioned relational DB at spiky/unpredictable load, and it scales further than any relational option. |
| **Amazon Redshift** | Provisioned or serverless columnar data warehouse; petabyte-scale; optimized for complex analytical (OLAP) queries. | Analytics and reporting, BI workloads. | Queries are frequent/complex and consistent low-latency performance matters enough to justify a continuously running warehouse — vs Athena's pay-per-query-scanned model, which is cheaper for occasional ad-hoc queries. |
| **Amazon ElastiCache** (Redis / Memcached) | Managed in-memory cache; Redis adds persistence, replication, pub/sub, rich data structures; Memcached is simpler, pure cache, horizontally shardable. | Redis/Memcached caching, session stores, reducing DB read load. | Caching needs to sit in front of any data source (not just DynamoDB), or you need Redis's durability/replication/complex data types — vs DAX, which only fronts DynamoDB. |
| **Amazon DocumentDB** | MongoDB-compatible managed document database. | Document-based applications, MongoDB workloads. | An application already uses MongoDB's document query API/aggregation framework, and rewriting to DynamoDB's access patterns isn't worth the migration cost. |
| **Amazon Neptune** | Managed graph database (property graph + RDF); optimized for deep relationship traversal. | Fraud detection, social graphs, recommendation engines. | The core query pattern is relationship traversal (e.g., "friends of friends") that would require expensive recursive joins in a relational database. |
| **Amazon Timestream** | Purpose-built serverless time-series database; automatic tiering of recent (memory) vs historical (magnetic) data; built-in time-series analytics functions. | IoT telemetry, application/infrastructure monitoring metrics at high ingestion scale. | Data is inherently time-ordered at very high ingestion rates — storage tiering and time-series-specific query functions are far cheaper and faster than modeling the same workload in a general-purpose database. |

### Interview Keyword
Use **RDS/Aurora** for relational workloads, **DynamoDB** for NoSQL scale, **Redshift** for analytics, and **ElastiCache** for low-latency caching.

---

## 4. Networking and Content Delivery

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **Amazon VPC** | Logically isolated virtual network — subnets, route tables, gateways. | Network segmentation and workload isolation. | Foundational — every AWS network design starts here; no real alternative. |
| **Subnets** | Divide a VPC's CIDR range into AZ-scoped segments; public (routes to an IGW) vs private (routes to NAT or nowhere). | Public/private workload placement, tiering (web/app/data). | You need to control which resources are internet-reachable per tier — separating public and private subnets is the baseline pattern for any secure design. |
| **Route Tables** | Per-subnet routing rules; most-specific route wins; defines whether a subnet behaves as public or private. | Route traffic to internet gateways, NAT gateways, or transit gateways. | Any VPC — this is how subnet-level traffic behavior is actually controlled, not an optional add-on. |
| **Internet Gateway** | Horizontally scaled, redundant AWS-managed gateway for VPC-to-internet traffic; one per VPC, no bandwidth cost of its own. | Public-facing resources needing direct internet access. | A subnet needs bidirectional internet reachability — the only way to make a subnet genuinely "public." |
| **NAT Gateway** | Managed, AZ-scoped, outbound-only internet access for private subnets; hourly + per-GB data processing charge. | Private EC2 patching and outbound updates without inbound exposure. | You want a managed, highly available NAT path without patching a self-managed NAT instance — trade-off is the per-GB processing cost, which a VPC endpoint avoids for AWS-service traffic specifically. |
| **Elastic Load Balancing** (ALB / NLB / GWLB) | ALB = L7, content-based routing, WebSocket support; NLB = L4, extreme throughput, static IP; GWLB = L3, transparent appliance insertion. | High-availability applications, microservices routing, appliance insertion. | ALB when routing depends on path/host; NLB when raw throughput/static IP/non-HTTP protocols matter more than content routing; GWLB when transparently inserting third-party firewalls/IDS into the traffic path. |
| **Amazon Route 53** | Managed authoritative DNS; health-check-driven routing policies (weighted, latency, failover, geolocation); domain registration. | Domain registration, DNS routing, health checks, DR failover. | You need deep AWS integration — alias records to AWS resources at no extra query cost — and health-check-driven failover a third-party DNS provider won't natively give you. |
| **Amazon CloudFront** | CDN caching content at edge locations; integrates with WAF/Shield/ACM; reduces origin load and latency. | Faster global content delivery, static asset offload. | Content is cacheable HTTP(S) — dramatically cuts both latency and origin compute/bandwidth cost for repeat requests, vs Global Accelerator, which doesn't cache. |
| **AWS Transit Gateway** | Hub-and-spoke connectivity for many VPCs/VPNs with transitive routing; centralized management; scales to thousands of attachments. | Connect multiple VPCs and on-premises networks. | Connecting more than a handful of VPCs — VPC Peering has no transitive routing and becomes an unmanageable mesh past a few connections; TGW adds hourly + per-GB cost but is far more operationally efficient at scale. |
| **AWS Direct Connect** | Dedicated private physical link to AWS; consistent low latency/high throughput; can reduce data-transfer cost vs internet egress at high volume. | Hybrid cloud connectivity requiring predictable performance. | You need predictable performance and high sustained throughput and can accept a longer provisioning lead time (weeks) and higher fixed cost — vs VPN's fast setup but internet-dependent variability. |
| **AWS VPN** (Site-to-Site / Client) | Encrypted IPsec tunnel over the public internet. | Site-to-site VPN and client remote-access VPN. | You need to connect quickly and cheaply and can tolerate variable, internet-dependent latency — no long lead time, pay-as-you-go, vs Direct Connect's predictability and cost. |

### Interview Keyword
A secure AWS network usually includes **VPC, public/private subnets, route tables, security groups, NACLs, NAT Gateway, ALB, and Route 53**.

---

## 5. Security, Identity, and Compliance

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **AWS IAM** | Foundation identity/access service — users, groups, roles, policies; free; least-privilege is the default control for everything else in AWS. | Access control and least privilege. | Always — the baseline for every access-control decision; no alternative within AWS. |
| **IAM Identity Center** | Centralized workforce SSO across multiple AWS accounts/Organizations; integrates with external IdPs (Okta, Azure AD). | Single sign-on across AWS accounts. | Managing access across many AWS accounts — avoids credential sprawl and centralizes MFA/lifecycle management vs per-account IAM users. |
| **AWS Organizations** | Multi-account management; consolidated billing; Service Control Policies (SCPs) as org-wide guardrails. | Account governance and consolidated billing. | You need centralized governance/billing and guardrails that hold regardless of what IAM policies an individual account defines — IAM alone can't enforce that org-wide. |
| **AWS Control Tower** | Automated landing zone on top of Organizations — pre-built account factory, guardrails, compliance dashboards. | Secure multi-account setup. | You want an AWS-recommended best-practice account structure provisioned automatically rather than hand-rolling a multi-account setup. |
| **AWS KMS** | Managed encryption key creation/rotation/audit (via CloudTrail); envelope encryption; customer-managed vs AWS-managed keys. | Encrypt S3, EBS, RDS, Lambda, and Secrets Manager. | Any workload needing encryption at rest with auditable, policy-controlled key access — the foundational encryption service nearly every other service builds on. |
| **AWS Secrets Manager** | Stores and automatically rotates secrets via Lambda rotation functions; fine-grained resource policies. | Database passwords, API keys, credentials. | The secret needs automatic rotation or tighter secret-specific access auditing — costs more per secret than Parameter Store but removes manual rotation risk. |
| **AWS Certificate Manager** | Free public/private TLS certificate issuance with automatic renewal; native integration with ALB/CloudFront/API Gateway. | HTTPS for ALB, CloudFront, and API Gateway. | You want zero-cost, zero-maintenance TLS with no renewal risk — ACM auto-renews, avoiding the classic "certificate expired in production" incident. |
| **Amazon GuardDuty** | ML-based continuous threat detection over CloudTrail/VPC Flow Logs/DNS logs; no infrastructure to deploy. | Detect suspicious AWS activity. | You need automated, continuously updated threat intelligence at low operational cost, vs manual log review that doesn't scale. |
| **AWS Security Hub** | Aggregates findings from GuardDuty/Inspector/Config/partner tools into one dashboard with compliance scoring (CIS, PCI-DSS, etc.). | Centralized security findings, security posture management. | You need a single pane of glass and automated compliance scoring across many security tools instead of checking each dashboard separately. |
| **Amazon Inspector** | Automated, continuous vulnerability (CVE) scanning for EC2, ECR images, and Lambda. | EC2, ECR, and Lambda vulnerability scanning. | You need continuous, automatic re-scanning as new CVEs are disclosed, not just a point-in-time scan at deploy. |
| **AWS WAF** | L7 filtering (SQLi/XSS/rate-limiting rules) attached to ALB/CloudFront/API Gateway; pay per rule + request. | Protect applications from web attacks. | You need to block specific malicious request patterns, not just absorb DDoS volume — vs Shield, which handles the volumetric attack itself. |
| **AWS Shield** (Standard / Advanced) | DDoS protection; Standard = automatic, free L3/L4 for everyone; Advanced = adds L7 protection, cost protection, 24/7 DRT access. | Protect internet-facing applications from DDoS. | Standard is always on by default at no cost; upgrade to Advanced when the business impact of a large-scale attack justifies an SLA-backed response team and billing protection. |
| **AWS Config** | Tracks resource configuration state/history; evaluates against compliance rules; detects drift. | Compliance and audit checks, drift detection. | You need to know a resource's actual configuration state over time, not just the API calls that changed it — complements CloudTrail rather than replacing it. |
| **AWS CloudTrail** | Records every API call made in the account — who did what, when, from where. | Governance, auditing, and investigations. | Any investigation into an access/change event — CloudWatch tells you *how* the system is performing, CloudTrail tells you *who* did what. |

### Interview Keyword
Security in AWS starts with **IAM least privilege, MFA, encryption with KMS, CloudTrail logging, Config compliance, GuardDuty, and Security Hub**.

---

## 6. Monitoring, Management, and Governance

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **Amazon CloudWatch** | Metrics, logs, alarms, dashboards; natively integrated with every AWS service with zero extra setup for basic metrics. | Monitoring EC2, Lambda, RDS, and applications. | The default operational monitoring tool for "how is it performing" — pairs with CloudTrail (below), which answers a different question. |
| **AWS CloudTrail** | Records API activity across the account. | Audit and incident investigation. | You're investigating an access/change event, not runtime performance. |
| **AWS Config** | Tracks configuration history; evaluates compliance rules. | Compliance and drift detection. | You need the *state* of a resource's configuration over time, not the API call log itself. |
| **AWS Systems Manager** | Operational hub — Session Manager (no SSH keys/open ports), Patch Manager, Run Command, Parameter Store, Automation documents. | Patch Manager, Session Manager, Run Command. | You need centralized, auditable fleet management without opening inbound SSH/RDP ports — improves both security posture and operational efficiency at scale, vs direct SSH access. |
| **AWS Trusted Advisor** | Automated best-practice checks across cost, security, performance, fault tolerance, and service limits. | Cost, security, performance, fault-tolerance checks. | You want a quick, low-effort automated health check without building custom checks yourself — full check set requires a Business/Enterprise support plan. |
| **AWS Health Dashboard** | Account-specific visibility into AWS service events/maintenance affecting your resources (vs the public, account-agnostic status page). | Account-specific service events. | You need proactive, personalized alerts about issues actually affecting your account's resources, not generic AWS-wide status. |
| **AWS Service Catalog** | Curated, approved self-service IaC templates for end users/teams. | Enterprise provisioning governance. | You want teams to self-serve infrastructure within guardrails (approved templates) rather than either blocking them entirely or granting unrestricted console/IaC access. |
| **AWS License Manager** | Tracks and enforces BYOL software license usage across accounts. | License compliance management. | You run licensed software (Windows Server, Oracle, SQL Server) and need to avoid license compliance violations or overage penalties. |
| **AWS Compute Optimizer** | ML-based right-sizing recommendations for EC2/EBS/Lambda/ECS based on actual utilization data. | Cost and performance optimization. | You want data-driven right-sizing recommendations instead of guessing at instance sizes or over-provisioning "just in case." |

### Interview Keyword
For cloud operations, combine **CloudWatch for monitoring, CloudTrail for auditing, Config for compliance, and Systems Manager for patching and automation**.

---

## 7. DevOps and Developer Tools

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **AWS CodeCommit** | Managed private Git hosting. *(AWS stopped onboarding new customers in July 2024 — GitHub/GitLab is now the more common real-world choice; still worth knowing the name for interviews.)* | Source code hosting. | Legacy accounts already using it, or a strict requirement to keep source control fully inside AWS's IAM/network boundary. |
| **AWS CodeBuild** | Managed, serverless build service; pay per build minute; no build servers to maintain. | Compile, test, and package code. | You want to avoid managing build infrastructure/capacity — scales automatically with concurrent builds, vs self-hosted Jenkins agents needing their own patching/scaling. |
| **AWS CodeDeploy** | Automates deployment to EC2/ECS/Lambda/on-prem; supports blue/green and canary strategies with automatic rollback on failed health checks. | Deploy applications to EC2, ECS, Lambda, or on-premises. | You need built-in blue/green or canary rollout with automatic rollback safety, vs a manual/scripted deploy with no native rollback. |
| **AWS CodePipeline** | Managed CI/CD orchestration connecting source → build → test → deploy stages. | Automate release pipelines. | You want native AWS service integration (CodeBuild/CodeDeploy/manual approval gates) without managing pipeline infrastructure yourself. |
| **AWS CloudFormation** | Declarative IaC; native AWS integration; no external state backend to manage (AWS manages it); stack-based automatic rollback on failure. | Provision AWS resources using templates. | You want zero additional tooling/state backend and native rollback semantics — at the cost of being AWS-only, vs Terraform's multi-cloud reach. |
| **AWS CDK** | IaC using real programming languages (TypeScript, Python, Java); synthesizes to CloudFormation. | Define infrastructure with Python, TypeScript, Java, etc. | You want loops/abstractions/type-checking and reusable constructs instead of verbose YAML/JSON — still inherits CloudFormation's deployment engine and rollback behavior. |
| **Amazon ECR** | Private, IAM-integrated container registry; image scanning on push; lifecycle policies. | Store Docker images. | You need private images tied to IAM auth and native AWS scanning, vs a public registry like Docker Hub. |
| **AWS X-Ray** | Distributed tracing across Lambda/ECS/API Gateway/downstream calls; visualizes the full request path and per-hop latency. | Troubleshoot microservices and APIs. | You need to pinpoint which specific service/hop in a distributed request is slow or failing — log-based debugging alone can't show the full request path. |

### Interview Keyword
A common CI/CD pipeline uses **GitHub or CodeCommit → CodeBuild → ECR → ECS/EKS/Lambda deployment**, with security scanning and approval gates.

---

## 8. Migration and Hybrid Cloud

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **AWS Migration Hub** | Central dashboard tracking migration progress across multiple AWS migration tools/waves. | Central migration dashboard. | You're running many migrations across several tools and need one consolidated tracking view. |
| **AWS Application Migration Service** | Agent-based, continuous-replication lift-and-shift for entire servers; minimal-downtime cutover. | Lift-and-shift migration to AWS. | You're migrating whole servers/applications, not just a database — vs DMS, which is database-only. |
| **AWS Database Migration Service** | Migrates databases with minimal downtime via continuous replication; homogeneous or heterogeneous (with Schema Conversion Tool). | Migrate Oracle, SQL Server, MySQL, PostgreSQL. | You need continuous replication during a live cutover window to minimize downtime, vs a manual export/import requiring an extended outage. |
| **AWS DataSync** | Automated, accelerated large dataset transfer between on-prem and AWS storage; built-in scheduling, validation, bandwidth throttling. | Move data between on-premises and AWS. | Transfers are large and recurring and need scheduling/validation/throttling built in, vs manual `rsync`/`aws s3 cp`. |
| **AWS Transfer Family** | Managed SFTP/FTPS/FTP endpoints backed by S3/EFS. | Secure file transfers. | You need a fully managed, highly available file-transfer endpoint without patching/scaling your own FTP servers. |
| **AWS Snow Family** | Physical data transfer devices (Snowball, Snowball Edge, Snowmobile) for offline bulk transfer. | Large-scale data migration. | The dataset is so large that network transfer would take weeks/months, or no reliable link exists — do the bandwidth math to justify it. |
| **AWS Outposts** | AWS-managed infrastructure physically deployed on-premises, running the same APIs as an AWS region. | Hybrid cloud workloads. | The workload has ultra-low-latency or strict data-residency requirements that force processing to stay physically on-site. |
| **AWS Direct Connect** | Dedicated private network connection to AWS (see [§4 Networking](#4-networking-and-content-delivery) for full detail). | Hybrid cloud connectivity. | You need predictable performance and high sustained throughput for hybrid connectivity at scale. |

### Interview Keyword
Use **DMS** for databases, **DataSync** for file/object data, **Application Migration Service** for servers, and **Direct Connect/VPN** for hybrid connectivity.

---

## 9. Analytics and Data Services

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **Amazon Athena** | Serverless SQL directly over S3 (via the Glue Data Catalog); pay per query/data scanned. | Serverless log and data analysis. | Queries are ad-hoc or infrequent and you don't want to provision/pay for a continuously running warehouse — vs Redshift's provisioned cost. |
| **AWS Glue** | Serverless ETL jobs plus a Data Catalog (shared schema registry for S3/Athena/Redshift). | Prepare data for analytics. | You want managed, serverless ETL and a shared catalog without cluster management overhead — vs EMR's need to size and run a cluster. |
| **Amazon EMR** | Managed Hadoop/Spark clusters for large-scale, custom big-data processing. | Spark and Hadoop workloads. | You need full control over the cluster or a custom big-data framework at very large scale — vs Glue's managed but less flexible model. |
| **Amazon Kinesis** (Data Streams / Firehose) | Real-time streaming ingestion; Data Streams = custom consumers + replay; Firehose = managed delivery straight to S3/Redshift/OpenSearch with no consumer code. | Logs, clickstreams, IoT data. | Data Streams over Firehose: you need custom processing logic, multiple independent consumers, or replay capability — Firehose trades that flexibility for zero ops. |
| **Amazon OpenSearch Service** | Managed search/log-analytics engine (Elasticsearch/Kibana-compatible). | Centralized logging and search. | You need full-text search or log-analytics dashboards — a query shape Athena/Redshift aren't built for. |
| **Amazon QuickSight** | Serverless BI/dashboarding; pay-per-session pricing instead of per-seat licensing. | Dashboards and reporting. | You want AWS-native dashboards directly over Redshift/Athena/S3 with usage-based pricing instead of a third-party BI platform's fixed per-seat licenses. |
| **AWS Lake Formation** | Centralized data lake governance — fine-grained (column/row-level) access control on top of a Glue Catalog/S3 data lake. | Secure data lake setup. | You need fine-grained, centrally managed access control across many datasets/consumers, vs hand-managing S3 bucket policies and IAM directly. |
| **Amazon MSK** | Managed Apache Kafka; handles broker provisioning/patching/scaling. | Event streaming platform. | The application already uses the Kafka API/ecosystem (Kafka Connect, Kafka Streams) and rewriting to Kinesis isn't worth the migration cost. |

### Interview Keyword
A common AWS data lake design uses **S3, Glue Data Catalog, Lake Formation, Athena, Redshift, and QuickSight**.

---

## 10. AI, ML, and Generative AI

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **Amazon SageMaker** | Full ML lifecycle platform — managed notebooks, training jobs, tuning, deployment endpoints, pipelines. | Machine learning lifecycle management. | You need a custom model trained on your own data/architecture, not just calling a pre-trained foundation model — vs Bedrock, this is the right tool when off-the-shelf models don't fit. |
| **Amazon Bedrock** | Managed API access to foundation models (Anthropic Claude, Amazon Titan, Meta Llama, etc.); no infrastructure to manage; supports fine-tuning/RAG/agents. | AI assistants, chatbots, content generation. | You want to build generative AI features quickly via API calls rather than training/hosting your own model — far lower time-to-value and no GPU infrastructure to manage vs SageMaker. |
| **Amazon Q** | AI assistant — Q Developer for code generation/AWS console Q&A, Q Business for enterprise data Q&A. | Developer and enterprise productivity. | You want an AWS-integrated assistant for developer productivity or internal enterprise search without building a custom RAG pipeline yourself. |
| **Amazon Rekognition** | Pre-trained image/video analysis API — object/face detection, content moderation. | Object and face detection. | The use case matches Rekognition's pre-built capabilities — far cheaper/faster than training and hosting a custom computer-vision model. |
| **Amazon Comprehend** | Pre-trained NLP API — sentiment, entity extraction, key phrases, PII detection. | Sentiment and text analysis. | The task matches Comprehend's built-in capabilities — no training data or ML expertise required. |
| **Amazon Textract** | OCR plus structured data extraction (forms, tables) from documents. | OCR and forms processing. | You need structured extraction (form fields, table cells), not just raw text — generic OCR won't give you that structure. |
| **Amazon Lex** | Conversational chatbot engine (same tech as Alexa); intent/slot-based dialog management. | Chatbots and voice bots. | You want a managed conversational interface with built-in intent recognition instead of building a custom NLU pipeline. |
| **Amazon Polly** | Text-to-speech across many languages/voices, including neural voices. | Voice applications. | You need natural-sounding synthesized speech without managing a TTS model yourself. |
| **Amazon Transcribe** | Speech-to-text; supports real-time streaming and batch, speaker diarization, custom vocabulary. | Audio transcription. | You need automated transcription (call centers, media captioning) without a custom ASR model. |
| **Amazon Translate** | Neural machine translation API across many language pairs. | Multilingual applications. | You need fast, good-enough translation without building/maintaining a custom translation model. |

### Interview Keyword
Use **Bedrock** for generative AI applications, **SageMaker** for custom ML model lifecycle, and **Lex/Polly/Transcribe** for conversational AI.

---

## 11. Application Integration

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **Amazon SQS** | Pull-based message queue; Standard = at-least-once/best-effort order, high throughput; FIFO = exactly-once/strict order, lower throughput. | Decouple application components. | Exactly one consumer should process each message and you need a durable buffer against traffic spikes — vs SNS, which pushes to many subscribers instead. |
| **Amazon SNS** | Push-based pub/sub fan-out to many subscribers at once (SQS, Lambda, email, SMS, HTTP). | Fan-out messaging and alerts. | The same message must reach multiple independent subscribers immediately — vs SQS's single-consumer-per-message model. |
| **Amazon EventBridge** | Event bus with content-based routing rules, schema registry, native SaaS/third-party integrations. | Event-driven architecture. | Routing depends on event content, not just fan-out, or you're integrating third-party/SaaS event sources — vs SNS's simpler, routing-free fan-out. |
| **AWS Step Functions** | Visual state-machine workflow orchestration; built-in retries/error handling; executions up to 1 year long. | Multi-step business processes. | A multi-step workflow needs visibility, retry logic, or human-approval steps — vs manually chaining Lambda calls, which is fragile and hard to observe. |
| **Amazon API Gateway** | Managed REST/HTTP/WebSocket API front door; throttling, auth, request validation, caching. | REST, HTTP, and WebSocket APIs. | You need per-client throttling, request validation, native Lambda integration, or API key management — vs a bare ALB, which lacks API-management features. |
| **AWS AppSync** | Managed GraphQL API service; real-time subscriptions; built-in resolvers to DynamoDB/Lambda/RDS. | Real-time web and mobile applications. | Clients (especially mobile) need to fetch exactly the fields they want in one round trip, or need real-time subscription updates — a fit REST/API Gateway doesn't natively provide. |
| **Amazon MQ** | Managed ActiveMQ/RabbitMQ. | ActiveMQ and RabbitMQ migration. | You're migrating an existing app that already speaks JMS/AMQP and rewriting its messaging code for SQS/SNS isn't worth it. |

### Interview Keyword
Use **SQS** for queueing, **SNS** for notifications, **EventBridge** for event routing, and **Step Functions** for workflow orchestration.

---

## 12. Cost Management

| Service | Key Features & Characteristics | Use Cases | Preferred Over the Alternative When |
|---|---|---|---|
| **AWS Cost Explorer** | Visualizes and analyzes historical spend/usage trends with custom filtering/grouping. | View and forecast AWS spend. | You're investigating *why* a bill changed — the natural first stop before Budgets (forward-looking) or CUR (most granular). |
| **AWS Budgets** | Proactive alerts when spend/usage crosses a defined threshold; supports forecasted-spend alerts. | Notify when spend exceeds limits. | You need forward-looking alerts, not just historical analysis — vs Cost Explorer, which only looks backward. |
| **AWS Cost and Usage Report** | Most granular, itemized billing data; exportable to S3/Athena/Redshift for custom analysis. | FinOps reporting and analysis. | You need line-item detail for chargeback models or custom BI dashboards that Cost Explorer's UI can't provide. |
| **Savings Plans** | Flexible $/hour compute commitment (1 or 3 year) applying automatically across EC2/Fargate/Lambda regardless of instance family/region. | Reduce EC2, Lambda, and Fargate cost. | Workload composition (instance family, region) may change over the commitment period — Savings Plans flex with usage, unlike Reserved Instances tied to specific instance attributes. |
| **Reserved Instances** | Discount (up to ~72%) for committing to a specific instance type/region for 1–3 years. | Lower EC2 and RDS cost. | The workload is very stable/predictable and exact instance family won't change, or you need a capacity reservation guarantee Savings Plans don't provide. |
| **AWS Pricing Calculator** | Free tool to estimate architecture cost before deployment. | Estimate architecture cost before deployment. | You want an AWS-maintained, service-accurate cost estimate during the design phase, before committing to an architecture — more reliable than a spreadsheet guess. |

### Interview Keyword
FinOps in AWS includes **tagging, budgets, cost allocation tags, Cost Explorer, CUR, Savings Plans, and right-sizing**.

---

## Most Important AWS Services to Know First

1. IAM
2. VPC
3. EC2
4. S3
5. EBS
6. EFS
7. RDS
8. DynamoDB
9. Lambda
10. CloudWatch
11. CloudTrail
12. Route 53
13. Elastic Load Balancing
14. Auto Scaling
15. KMS
16. Secrets Manager
17. ECS
18. EKS
19. CloudFormation
20. Systems Manager
21. AWS Organizations
22. AWS Control Tower

---

## Simple Interview Answer

AWS services are cloud-based building blocks used to design, deploy, secure, monitor, and scale applications. The major service categories include compute, storage, databases, networking, security, monitoring, DevOps, analytics, AI/ML, and cost management.

For example, **EC2** provides virtual servers, **S3** provides object storage, **RDS** provides managed relational databases, **VPC** provides network isolation, **IAM** manages access control, and **CloudWatch** provides monitoring and alarms.

A well-designed AWS solution combines these services to achieve scalability, high availability, security, automation, and cost optimization — and picking between similar-looking services almost always comes down to a specific trade-off: cost model (pay-per-use vs provisioned), scalability ceiling, operational efficiency (managed vs self-run), or a security/compliance requirement that only one option satisfies.

---

## Daily Learning Notes

### What to Practice

- Create an EC2 instance in a public subnet.
- Create an S3 bucket with encryption enabled.
- Create IAM users, groups, roles, and policies.
- Build a VPC with public and private subnets.
- Create a CloudWatch alarm for EC2 CPU utilization.
- Deploy a simple application using ECS or EKS.
- Create an RDS database in a private subnet.
- Use Systems Manager Session Manager instead of SSH.
- Enable CloudTrail and AWS Config for governance.
- Review costs using AWS Cost Explorer and Budgets.

### Key Architecture Principle

A strong AWS architecture should be:

- Secure
- Highly available
- Fault tolerant
- Scalable
- Automated
- Observable
- Cost optimized
