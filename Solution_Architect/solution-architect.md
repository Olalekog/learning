<a id="top"></a>

# AWS Solutions Architect — Interview Prep Notes

A single reference covering AWS architecture from core services through
scenario-based interview questions, with comparison tables, example
configurations, and a troubleshooting guide organized by topic.

## Table of Contents

1. [How to Approach the Interview](#1-how-to-approach-the-interview)
2. [AWS Well-Architected Framework](#2-aws-well-architected-framework)
3. [Compute](#3-compute)
4. [Storage](#4-storage)
5. [Databases](#5-databases)
6. [Networking (VPC)](#6-networking-vpc)
7. [Load Balancing and DNS](#7-load-balancing-and-dns)
8. [Security and IAM](#8-security-and-iam)
9. [High Availability, Fault Tolerance, and Disaster Recovery](#9-high-availability-fault-tolerance-and-disaster-recovery)
10. [Serverless Architecture](#10-serverless-architecture)
11. [Containers](#11-containers)
12. [Messaging and Integration](#12-messaging-and-integration)
13. [Content Delivery and Edge](#13-content-delivery-and-edge)
14. [Monitoring and Observability](#14-monitoring-and-observability)
15. [Cost Optimization](#15-cost-optimization)
16. [Migration and Hybrid Cloud](#16-migration-and-hybrid-cloud)
17. [Common Architecture Patterns](#17-common-architecture-patterns)
18. [Scenario-Based Interview Questions](#18-scenario-based-interview-questions)
19. [Service Comparison Cheat Sheet](#19-service-comparison-cheat-sheet)
20. [Common Pitfalls and Trick Questions](#20-common-pitfalls-and-trick-questions)
21. [AWS Services by Category](#21-aws-services-by-category)
22. [Troubleshooting Guide by Topic](#22-troubleshooting-guide-by-topic)
23. [CLI / IaC Cheat Sheet](#23-cli--iac-cheat-sheet)
24. [Study Checklist](#24-study-checklist)

---

# 1. How to Approach the Interview

SA interviews (especially loop/panel rounds) rarely ask "define EC2" —
they hand you an ambiguous scenario and evaluate how you narrow it down.

## The Framework for Any "Design X" Question

```text
1. Clarify requirements before designing anything:
   - Functional: what does the system actually do?
   - Scale: requests/sec, data volume, growth rate?
   - Non-functional: latency target, availability target (99.9% vs 99.99%)?
   - Constraints: budget, existing tech, compliance (HIPAA/PCI/GDPR)?
   - RTO/RPO if resilience is in scope?

2. Start broad, then narrow:
   - Draw the high-level flow (client → edge → compute → data) before
     naming specific services.
   - Name services only once the shape of the architecture is agreed.

3. Justify every choice against a requirement, not "because it's popular":
   - "DynamoDB because access pattern is key-based lookups at high scale
     with single-digit-ms latency" beats "DynamoDB because NoSQL is fast."

4. Address the cross-cutting concerns explicitly:
   - Security (who can access what, encryption at rest/in transit)
   - Scalability (what scales automatically, what's the bottleneck)
   - Resilience (what happens when an AZ/region fails)
   - Cost (rough shape: pay-per-use vs provisioned)
   - Observability (how would you know it broke)

5. State trade-offs out loud — this is what separates a senior answer:
   "We could use Aurora for stronger consistency, but given the read-heavy
   pattern at this scale, DynamoDB with DAX gets us lower latency at lower
   ops overhead; the trade-off is eventual consistency on cross-item reads."
```

## What Interviewers Are Actually Scoring

- Do you ask clarifying questions instead of guessing requirements?
- Do you reason from first principles (CAP theorem, shared responsibility,
  blast radius) rather than reciting a memorized architecture?
- Can you defend a choice when the interviewer pushes back ("what if
  traffic is 100x that")?
- Do you mention security and cost without being prompted?

[⬆ Back to top](#top)

---

# 2. AWS Well-Architected Framework

The six pillars are the vocabulary interviewers expect you to structure
answers around, especially in Professional-level and behavioral rounds.

| Pillar | Core Question | Key AWS Tools |
|---|---|---|
| **Operational Excellence** | Can you run and monitor systems to deliver business value, and continually improve? | CloudFormation/CDK, Systems Manager, CloudWatch, X-Ray |
| **Security** | Are data and systems protected through risk assessment and mitigation? | IAM, KMS, GuardDuty, Security Hub, WAF, Shield |
| **Reliability** | Can the system recover from failure and meet demand? | Multi-AZ, Auto Scaling, Route 53 health checks, Backup |
| **Performance Efficiency** | Are resources used efficiently as demand and technology change? | Compute Optimizer, caching (CloudFront/ElastiCache/DAX), right-sizing |
| **Cost Optimization** | Is the lowest cost achieved to meet business needs? | Cost Explorer, Trusted Advisor, Savings Plans, S3 lifecycle |
| **Sustainability** | Is environmental impact minimized? | Managed/serverless services (shared infra efficiency), right-sizing, region selection |

## Design Principles Worth Quoting in an Interview

- **Reliability**: stop guessing capacity, test recovery procedures,
  automate recovery from failure, scale horizontally, manage change
  through automation.
- **Security**: implement a strong identity foundation, enable
  traceability, apply security at every layer (defense in depth), automate
  security best practices, protect data in transit and at rest, keep
  people away from data (least access), prepare for security events.
- **Cost**: adopt a consumption model, measure overall efficiency, stop
  spending on undifferentiated heavy lifting, analyze and attribute spend.

[⬆ Back to top](#top)

---

# 3. Compute

## EC2 Instance Family Cheat Sheet

| Family | Optimized For | Example Use Case |
|---|---|---|
| **T** (T3/T4g) | Burstable, low baseline CPU with credits | Dev/test, low-traffic web servers |
| **M** (M6i/M7g) | General purpose, balanced CPU:RAM | Typical application servers |
| **C** (C7g) | Compute-optimized (high CPU:RAM ratio) | Batch processing, video encoding, gaming servers |
| **R** (R7g) | Memory-optimized | In-memory caches, real-time big data analytics |
| **X** | Extreme memory | SAP HANA, large in-memory databases |
| **I** (I4i) | Storage-optimized, high IOPS local NVMe | NoSQL databases, data warehousing |
| **G/P** | GPU-accelerated | ML training/inference, graphics rendering |
| **Graviton (g suffix)** | ARM-based, better price/performance | Any workload compiled for ARM — usually first choice for cost optimization |

## Purchasing Options

| Option | Discount vs On-Demand | Commitment | Best For |
|---|---|---|---|
| **On-Demand** | None (baseline) | None | Unpredictable, short-term, spiky workloads |
| **Reserved Instances (RI)** | Up to ~72% | 1 or 3 years | Steady-state, predictable baseline load |
| **Savings Plans** | Up to ~72% | 1 or 3 years, $/hour commitment | Same as RI but flexible across instance family/region/compute type (EC2, Fargate, Lambda) |
| **Spot Instances** | Up to ~90% | None (can be reclaimed with 2-min warning) | Fault-tolerant, stateless, batch/CI workloads |
| **Dedicated Hosts/Instances** | Premium | Varies | Compliance requiring physical isolation, licensing tied to sockets/cores |

## Auto Scaling

```text
Auto Scaling Group (ASG) components:
  - Launch Template (AMI, instance type, security groups, user data)
  - Min / Desired / Max capacity
  - Scaling policies:
      Target tracking   → "keep average CPU at 50%" (most common, simplest)
      Step scaling      → different scale amounts per CloudWatch alarm breach
      Scheduled scaling → known traffic patterns (e.g., business hours)
  - Health checks: EC2 status checks, or ELB health checks (catches app-level failure)
```

**Interview point**: target tracking is almost always the right default
answer unless the question specifically calls for scaling ahead of a known
event (scheduled) or fine-grained control over scale-out increments (step).

## Lambda (see also [§10 Serverless](#10-serverless-architecture))

- Max execution time: 15 minutes — anything longer needs Step Functions,
  ECS/Fargate, or Batch.
- Cold starts matter for latency-sensitive sync APIs — mitigate with
  provisioned concurrency, smaller deployment packages, or a
  lighter-weight runtime.
- Concurrency is throttled per-account/region by default; reserved
  concurrency protects critical functions from being starved by others.

[⬆ Back to top](#top)

---

# 4. Storage

## S3 Storage Classes

| Class | Availability | Retrieval | Use Case |
|---|---|---|---|
| **Standard** | 99.99% | Instant | Frequently accessed data |
| **Intelligent-Tiering** | 99.9% | Instant | Unknown/changing access patterns — moves objects automatically, no retrieval fee |
| **Standard-IA** | 99.9% | Instant | Infrequent access, needs millisecond access when it happens |
| **One Zone-IA** | 99.5% (single AZ) | Instant | Infrequent, re-creatable data (no AZ redundancy needed) |
| **Glacier Instant Retrieval** | 99.9% | Instant (ms) | Archive accessed roughly once a quarter |
| **Glacier Flexible Retrieval** | 99.99% | Minutes–hours | Archive, backup |
| **Glacier Deep Archive** | 99.99% | Hours (~12h) | Long-term compliance retention (7–10 years), lowest cost |

**Lifecycle policies** automate the transition between these tiers
(e.g., Standard → IA after 30 days → Glacier after 90 days → Deep Archive
after 365 days) — a near-universal cost-optimization answer for any
"how would you reduce storage cost" question.

## S3 Core Concepts Interviewers Probe

- **Consistency**: S3 has been strongly consistent for all operations
  (reads-after-writes, overwrites, deletes) since Dec 2020 — no longer a
  "eventual consistency" gotcha.
- **Durability vs Availability**: 11 nines durability (data loss) is not
  the same as 99.99% availability (can you reach it right now) — a
  common interview distinction.
- **Versioning + MFA Delete**: protects against accidental/malicious
  deletion; pairs with Object Lock for WORM compliance requirements.
- **Encryption**: SSE-S3 (AWS-managed keys), SSE-KMS (auditable via
  CloudTrail, supports key rotation/policies), SSE-C (customer-supplied
  key, AWS doesn't store it).
- **Access control layering**: bucket policy (resource-based) + IAM policy
  (identity-based) + ACL (legacy, avoid) + Block Public Access (account/
  bucket-level guardrail) — default recommendation is Block Public Access
  on + bucket policy for access, ACLs disabled.

## Block and File Storage

| Service | Type | Attach Point | Notes |
|---|---|---|---|
| **EBS** | Block | Single EC2 instance (one AZ) | gp3 (general purpose baseline), io2 Block Express (high IOPS, databases), st1/sc1 (throughput-optimized HDD for big sequential workloads) |
| **Instance Store** | Block (ephemeral) | Physically attached, lost on stop/terminate | Only for data that can be regenerated/replicated elsewhere |
| **EFS** | File (NFS) | Many EC2/Lambda/ECS across multiple AZs concurrently | Shared POSIX file system, scales automatically |
| **FSx for Windows** | File (SMB) | Windows workloads needing AD integration | Lift-and-shift Windows file shares |
| **FSx for Lustre** | File (high-performance) | HPC, ML training | Sub-millisecond latency, integrates with S3 as the data repository |

**Interview point**: "EBS vs EFS" is one of the most common questions —
EBS is single-instance block storage (like a hard drive), EFS is a
shared, multi-attach network file system. If the question mentions
"multiple EC2 instances need to read/write the same files," the answer
is EFS, not EBS.

## AWS Storage Gateway (Hybrid)

| Type | Function |
|---|---|
| **File Gateway** | On-prem NFS/SMB access backed by S3 |
| **Volume Gateway** | iSCSI block volumes, cached or stored mode, backed by EBS snapshots |
| **Tape Gateway** | Virtual tape library backed by Glacier, replaces physical tape backup |

[⬆ Back to top](#top)

---

# 5. Databases

## Relational (RDS / Aurora)

```text
Multi-AZ (RDS)        → synchronous standby replica in another AZ,
                         automatic failover, DISASTER RECOVERY (not scaling)
Read Replicas          → asynchronous copies, SCALE READ traffic,
                         can be cross-region, can be promoted to standalone
Aurora                 → storage layer replicated across 3 AZs (6 copies)
                         automatically; up to 15 read replicas with
                         <10ms replica lag typical; Aurora Global Database
                         for cross-region DR with <1s typical lag
```

| | RDS (standard engines) | Aurora |
|---|---|---|
| Engines | MySQL, PostgreSQL, MariaDB, Oracle, SQL Server | MySQL/PostgreSQL-compatible only |
| Storage | Provisioned, scales in fixed increments | Auto-scales up to 128TB, decoupled from compute |
| Replicas | Up to 5 | Up to 15 |
| Failover time | ~60–120s (Multi-AZ) | ~30s or less |
| Cost | Lower baseline | Higher baseline, better price/performance at scale |
| Serverless option | No | Aurora Serverless v2 (auto-scales capacity with load) |

## NoSQL — DynamoDB

- **Access pattern first**: DynamoDB requires designing the table around
  known query patterns (partition key + sort key) up front — unlike SQL,
  you can't easily "just add a WHERE clause" later without a new
  Global Secondary Index (GSI).
- **Partition key choice** drives scalability — a low-cardinality key
  (e.g., `status: active/inactive`) causes a "hot partition"; prefer high
  cardinality (e.g., `userId`).
- **Capacity modes**: On-Demand (pay per request, unpredictable traffic)
  vs Provisioned (cheaper at steady, predictable throughput, supports
  Auto Scaling on top).
- **DAX** — in-memory cache in front of DynamoDB, microsecond reads,
  used when read-heavy and read-after-write consistency isn't critical
  for the cached path.
- **Global Tables** — multi-region, multi-active replication for global
  low-latency reads/writes.
- **Streams** — ordered, time-stamped record of item-level changes;
  commonly triggers a Lambda for event-driven processing (e.g.,
  audit log, cross-region sync, materialized view update).

## Caching — ElastiCache

| | Redis | Memcached |
|---|---|---|
| Persistence | Yes (snapshots, AOF) | No |
| Replication/HA | Yes (Multi-AZ, read replicas) | No (pure cache, node failure loses data) |
| Data structures | Rich (lists, sets, sorted sets, pub/sub) | Simple key-value only |
| Use case | Session store, leaderboard, pub/sub, needs durability | Simple, horizontally scalable object cache |

## Analytics / Warehousing

| Service | Purpose |
|---|---|
| **Redshift** | Petabyte-scale SQL data warehouse, columnar storage, used for BI/OLAP |
| **Athena** | Serverless SQL directly over S3 data (via Glue Data Catalog), pay per query scanned |
| **EMR** | Managed Hadoop/Spark for big data processing |
| **OpenSearch Service** | Search and log analytics (successor to Elasticsearch Service) |

**Interview point**: "OLTP vs OLAP" — RDS/Aurora/DynamoDB for
transactional (OLTP) workloads; Redshift/Athena for analytical (OLAP)
workloads. A common wrong answer is trying to run heavy analytics
queries directly against a production OLTP database.

[⬆ Back to top](#top)

---

# 6. Networking (VPC)

## Core VPC Building Blocks

```text
VPC (e.g., 10.0.0.0/16)
 ├─ Public Subnet   (10.0.1.0/24) → Route Table → Internet Gateway (IGW)
 ├─ Private Subnet  (10.0.2.0/24) → Route Table → NAT Gateway (in public subnet)
 └─ Isolated Subnet (10.0.3.0/24) → Route Table → no route out (e.g., DB tier)

Availability Zones: always design subnets across 2+ AZs for resilience.
```

| Component | Purpose |
|---|---|
| **Internet Gateway (IGW)** | Allows a VPC to reach/be reached from the internet; one per VPC |
| **NAT Gateway** | Lets private-subnet resources initiate outbound internet traffic without being reachable inbound; managed, AZ-scoped (deploy one per AZ for HA) |
| **Route Table** | Per-subnet routing rules; determines public vs private subnet |
| **Security Group** | Stateful, instance-level firewall — allow rules only |
| **Network ACL (NACL)** | Stateless, subnet-level firewall — allow AND deny rules, evaluated in rule-number order |
| **VPC Endpoint (Gateway)** | Private route to S3/DynamoDB without traversing the internet, no cost |
| **VPC Endpoint (Interface/PrivateLink)** | ENI-based private connection to most other AWS services or a partner/private service, hourly + data cost |

## Security Group vs NACL (frequent interview question)

| | Security Group | NACL |
|---|---|---|
| Level | Instance (ENI) | Subnet |
| State | Stateful (return traffic auto-allowed) | Stateless (must explicitly allow both directions) |
| Rules | Allow only | Allow and deny |
| Evaluation | All rules evaluated | Rules evaluated in order, first match wins |
| Default | Deny all inbound, allow all outbound | Allow all in/out (default NACL) |

## Connecting VPCs and On-Prem

| Method | Use Case | Notes |
|---|---|---|
| **VPC Peering** | Direct connection between two VPCs | No transitive routing — each pair needs its own peering connection |
| **Transit Gateway** | Hub-and-spoke connectivity for many VPCs/VPNs | Transitive routing, scales far better than mesh peering |
| **Site-to-Site VPN** | Encrypted connection over the internet to on-prem | Quick to set up, variable latency (internet-dependent) |
| **Direct Connect** | Dedicated private network link to AWS | Consistent low latency/high throughput, longer lead time to provision; pair with VPN over DX for encryption |
| **PrivateLink** | Private, one-way service exposure (provider → consumer) without peering/routing complexity | Used heavily for SaaS-to-VPC or internal service-to-service without exposing full VPC |

**Interview point**: "How do you connect 20 VPCs together without a
routing mess?" → Transit Gateway, not a full mesh of VPC peering
connections (peering doesn't support transitive routing and doesn't
scale past a handful of VPCs).

[⬆ Back to top](#top)

---

# 7. Load Balancing and DNS

## Elastic Load Balancer Types

| Type | Layer | Use Case |
|---|---|---|
| **Application Load Balancer (ALB)** | L7 (HTTP/HTTPS) | Content-based routing (path/host-based), microservices, WebSocket support |
| **Network Load Balancer (NLB)** | L4 (TCP/UDP) | Extreme performance, static IP/Elastic IP, millions of requests/sec, low latency |
| **Gateway Load Balancer (GWLB)** | L3 | Deploying/scaling third-party virtual appliances (firewalls, IDS/IPS) transparently |
| Classic Load Balancer | Legacy | Avoid for new designs — retained knowledge only |

## Route 53 Routing Policies

| Policy | Behavior |
|---|---|
| **Simple** | Single resource, no health checks |
| **Weighted** | Distribute traffic by assigned percentage — canary/blue-green rollouts, A/B testing |
| **Latency-based** | Route to the region with the lowest latency for the user |
| **Failover** | Active-passive DR — route to secondary only if primary health check fails |
| **Geolocation** | Route based on the user's geographic location (compliance/content restrictions) |
| **Geoproximity** | Route based on geographic distance, with a "bias" to shift traffic |
| **Multi-value answer** | Return multiple healthy records, basic client-side load distribution |

**Interview point**: "How do you fail over to a DR region if the primary
region goes down?" → Route 53 failover routing policy with health checks
against the primary endpoint, combined with a warm/hot standby in the DR
region (see [§9](#9-high-availability-fault-tolerance-and-disaster-recovery)).

[⬆ Back to top](#top)

---

# 8. Security and IAM

## IAM Core Concepts

- **Users** — long-term identity for a person; avoid long-lived access
  keys where possible.
- **Groups** — collection of users, attach policies once to the group.
- **Roles** — temporary credentials (via STS), assumed by users, services,
  or federated identities — the preferred way to grant AWS service-to-
  service or human-to-AWS access without static keys.
- **Policies** — JSON documents; evaluation logic: **explicit deny always
  wins**, otherwise at least one explicit allow is required, default is
  implicit deny.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::app-data/reports/*",
      "Condition": {
        "StringEquals": { "aws:PrincipalTag/team": "analytics" }
      }
    }
  ]
}
```

## Policy Types

| Type | Attached To | Notes |
|---|---|---|
| **Identity-based** | User, group, role | Most common — "what can this identity do" |
| **Resource-based** | The resource itself (S3 bucket policy, KMS key policy) | Enables cross-account access without assuming a role |
| **Permission boundary** | User or role | Caps the *maximum* permissions that identity-based policies can grant — used to let teams create their own roles safely |
| **SCP (Service Control Policy)** | AWS Organizations OU/account | Guardrail across an entire account/OU, does not itself grant permissions, only restricts the maximum |

## Encryption and Key Management

- **KMS**: envelope encryption, customer-managed keys (CMKs) vs
  AWS-managed keys; key policies control who can use/manage a key
  (separate from IAM policies — both must allow).
- **Encryption in transit**: TLS everywhere — ALB/CloudFront listener
  certs via ACM, enforce via bucket/policy conditions
  (`aws:SecureTransport`).
- **Secrets Manager vs Parameter Store**: Secrets Manager supports
  automatic rotation (via Lambda) and is priced per secret; Parameter
  Store (SSM) is free for standard tier, no built-in rotation, fine for
  config values and manually-rotated secrets.

## Perimeter and Threat Detection

| Service | Purpose |
|---|---|
| **WAF** | L7 filtering — SQLi/XSS rules, rate-based rules, geo-blocking; attaches to ALB/CloudFront/API Gateway |
| **Shield Standard** | Automatic, free DDoS protection for all customers (L3/L4) |
| **Shield Advanced** | Paid — L7 DDoS protection, cost protection, 24/7 DRT access |
| **GuardDuty** | ML-based threat detection over CloudTrail/VPC Flow Logs/DNS logs |
| **Security Hub** | Aggregates findings from GuardDuty, Inspector, Config, and partner tools into one view |
| **Inspector** | Automated vulnerability scanning for EC2/ECR images/Lambda |
| **Macie** | ML-based discovery/classification of sensitive data (PII) in S3 |

**Interview point (shared responsibility model)**: AWS is responsible
*for* the security *of* the cloud (physical infra, hypervisor, managed
service internals); the customer is responsible for security *in* the
cloud (data, IAM configuration, network controls, patching for
unmanaged compute, application code). Nearly every real-world AWS
breach traces back to a *customer-side* misconfiguration (public S3
bucket, over-permissive IAM, exposed credentials) — good to state this
explicitly.

[⬆ Back to top](#top)

---

# 9. High Availability, Fault Tolerance, and Disaster Recovery

## Key Definitions (interviewers check these are not confused)

- **High Availability** — minimizing downtime through redundancy (e.g.,
  Multi-AZ) — normal operation, not a "disaster."
- **Fault Tolerance** — the system keeps operating correctly *even during*
  a component failure, with no perceptible impact (higher bar than HA).
- **RTO (Recovery Time Objective)** — how long you can be down before
  it's unacceptable.
- **RPO (Recovery Point Objective)** — how much data loss (measured in
  time) is acceptable.

## DR Strategy Spectrum

| Strategy | RTO | RPO | Cost | Description |
|---|---|---|---|---|
| **Backup & Restore** | Hours | Hours | $ | Regular backups/snapshots to another region, restore on disaster |
| **Pilot Light** | ~10s of minutes | Minutes | $$ | Core services (e.g., DB) always running minimally in DR region, rest scaled up on failover |
| **Warm Standby** | Minutes | Seconds–minutes | $$$ | Scaled-down but fully functional copy running in DR region, scaled up on failover |
| **Multi-Site Active-Active** | Near zero | Near zero | $$$$ | Full production capacity live in two+ regions simultaneously |

**Interview point**: this is the single most-tested DR question — be
ready to map a stated RTO/RPO ("we can tolerate 15 minutes of downtime
and 5 minutes of data loss") to the cheapest strategy that satisfies it
(here, warm standby, not full active-active — over-engineering for the
stated requirement is a red flag in a cost-aware interview).

## Backup Tooling

- **AWS Backup** — centralized, policy-based backup across EBS, RDS,
  DynamoDB, EFS, and more; supports cross-region and cross-account copy.
- **RDS/Aurora snapshots** — automated (within retention window) and
  manual (retained indefinitely); cross-region snapshot copy for DR.
- **S3 Cross-Region Replication (CRR)** — asynchronous, near-real-time
  object replication to a bucket in another region.

[⬆ Back to top](#top)

---

# 10. Serverless Architecture

## Core Services

```text
API Gateway → Lambda → DynamoDB
     │            │
     │            └─ Step Functions (multi-step orchestration, retries,
     │                                human approval steps, visual workflow)
     └─ Auth via Cognito or a Lambda authorizer
```

| Service | Role |
|---|---|
| **API Gateway** | Managed REST/HTTP/WebSocket API front door — throttling, auth, request validation, caching |
| **Lambda** | Event-driven compute, scales automatically, pay per invocation/duration |
| **Step Functions** | Orchestrates multi-step workflows with built-in retry/error handling — replaces fragile Lambda-calling-Lambda chains |
| **EventBridge** | Event bus for decoupled, event-driven architectures; supports schema registry and third-party SaaS event sources |
| **Cognito** | User authentication (User Pools) and federated/temporary AWS credentials (Identity Pools) |
| **DynamoDB** | Near-universal default database pairing for serverless due to scaling model |

## When Serverless Is (and Isn't) the Right Answer

**Favors serverless**: spiky/unpredictable traffic, event-driven
processing, want zero infrastructure management, workload fits within
Lambda's execution/memory limits.

**Favors traditional compute (EC2/ECS/EKS)**: constant high-throughput
traffic (cost crosses over vs Fargate/EC2 at sustained volume), execution
time >15 minutes, need for specialized hardware (GPU) or persistent
in-memory state, very strict cold-start latency requirements without
budget for provisioned concurrency.

[⬆ Back to top](#top)

---

# 11. Containers

## ECS vs EKS vs Fargate

| | ECS | EKS | Fargate |
|---|---|---|---|
| Orchestrator | AWS-proprietary | Managed Kubernetes | Not an orchestrator — a compute *launch type* |
| Learning curve | Lower | Higher (full k8s API) | N/A |
| Portability | AWS-only | Portable (k8s is an open standard) | N/A |
| Best for | Teams standardized on AWS, want simplicity | Teams needing k8s ecosystem/portability, multi-cloud | Removing server management from either ECS or EKS |

**Interview point**: Fargate is not a competitor to ECS/EKS — it's a
*launch type* (serverless compute) that can back either one, as an
alternative to the EC2 launch type where you manage the underlying
instances yourself.

## Container Registry and Image Flow

```text
docker build → ECR (private registry, image scanning on push) →
  ECS Task Definition / EKS Pod spec references the ECR image URI →
  Service (ECS) / Deployment (EKS) maintains desired replica count →
  ALB/NLB target group registers tasks/pods dynamically
```

[⬆ Back to top](#top)

---

# 12. Messaging and Integration

## Decoupling Pattern

```text
Producer → SQS (buffer/queue) → Consumer (polls, processes, deletes)

Producer → SNS (fan-out topic) → SQS Queue A → Consumer A
                               → SQS Queue B → Consumer B
                               → Lambda       → Consumer C
```

| Service | Model | Use Case |
|---|---|---|
| **SQS Standard** | Queue, at-least-once, best-effort ordering | Decoupling producer/consumer, absorbing traffic spikes, buffering |
| **SQS FIFO** | Queue, exactly-once processing, strict ordering | Order-sensitive workloads (e.g., financial transactions), lower throughput than Standard |
| **SNS** | Pub/sub, push-based fan-out | One event needs to reach multiple independent subscribers |
| **EventBridge** | Event bus, content-based routing rules | Complex routing logic, SaaS integrations, schema registry, more sophisticated than SNS fan-out |
| **Kinesis Data Streams** | Ordered, replayable stream, custom consumers | Real-time analytics, clickstream processing, need to replay/reprocess |
| **Kinesis Firehose** | Managed delivery stream to S3/Redshift/OpenSearch | Near-real-time ETL/loading, no custom consumer code needed |
| **MQ (Amazon MQ)** | Managed ActiveMQ/RabbitMQ | Lift-and-shift of existing app using JMS/AMQP protocols |

**Interview point**: "SQS vs SNS vs EventBridge" is asked constantly.
Shorthand: SQS = queue (pull, one consumer processes each message), SNS =
simple fan-out (push to many subscribers, no routing logic), EventBridge
= fan-out *with* content-based routing rules and third-party/SaaS
integration.

## Dead-Letter Queues and Resilience

- Attach a DLQ to SQS/SNS/Lambda so messages that repeatedly fail
  processing don't get silently dropped or block the queue —
  investigate DLQ contents rather than deleting them blind.
- Use exponential backoff + jitter on consumer retry logic to avoid
  a thundering-herd retry storm against a struggling downstream service.

[⬆ Back to top](#top)

---

# 13. Content Delivery and Edge

| Service | Purpose |
|---|---|
| **CloudFront** | CDN — caches content at edge locations, reduces latency and origin load, integrates with WAF/Shield |
| **Global Accelerator** | Anycast static IPs routing over the AWS global network backbone — improves performance for non-cacheable/TCP-UDP traffic (not HTTP caching) |
| **Lambda@Edge / CloudFront Functions** | Run logic at edge locations (auth checks, header manipulation, A/B testing) closer to the user |

**Interview point**: "CloudFront vs Global Accelerator" — CloudFront
caches *content* at the edge (best for static/cacheable HTTP content);
Global Accelerator improves *network path* performance for any TCP/UDP
traffic including non-cacheable dynamic content, and gives static
anycast IPs useful for allow-listing.

## Common CloudFront + S3 Pattern (Static Site / SPA)

```text
Route 53 → CloudFront (ACM cert, caching, WAF attached)
              → Origin: S3 bucket (Origin Access Control, bucket NOT public)
              → Origin: ALB (for dynamic API paths, path-based behavior)
```

[⬆ Back to top](#top)

---

# 14. Monitoring and Observability

| Service | Role |
|---|---|
| **CloudWatch Metrics** | Time-series metrics (CPU, custom app metrics via `PutMetricData`) |
| **CloudWatch Logs** | Centralized log aggregation, log groups/streams, subscription filters for real-time processing |
| **CloudWatch Alarms** | Trigger actions (SNS notification, Auto Scaling action) on metric threshold breach |
| **CloudWatch Dashboards** | Visualize metrics across services in one view |
| **X-Ray** | Distributed tracing — follow a single request across Lambda/API Gateway/ECS/downstream calls, find the slow hop |
| **CloudTrail** | Audit log of every API call made in the account — who did what, when, from where; foundational for security investigations |
| **Config** | Tracks resource configuration changes over time, evaluates against compliance rules |

**Interview point**: "CloudWatch vs CloudTrail" — CloudWatch answers "how
is my system performing" (metrics/logs/health); CloudTrail answers "who
did what" (API-level audit trail). Both are usually needed together for
a complete incident investigation.

[⬆ Back to top](#top)

---

# 15. Cost Optimization

## Levers, Roughly in Order of Impact

```text
1. Right-size            — match instance/DB size to actual utilization
                            (Compute Optimizer recommendations)
2. Elasticity             — scale down/off when not needed (dev/test
                            environments off nights & weekends)
3. Pricing model          — Savings Plans/RIs for steady-state,
                            Spot for fault-tolerant workloads
4. Storage tiering        — S3 lifecycle policies, delete unused
                            snapshots/AMIs/EBS volumes
5. Architecture            — serverless/managed services remove
                            idle-capacity cost; caching reduces
                            redundant compute/DB load
6. Data transfer           — minimize cross-AZ/cross-region transfer,
                            use VPC endpoints to avoid NAT Gateway
                            data processing charges for AWS-service traffic
```

## Tools

| Tool | Purpose |
|---|---|
| **Cost Explorer** | Visualize and analyze spend/usage trends over time |
| **Budgets** | Alert when spend/usage exceeds a defined threshold |
| **Trusted Advisor** | Automated checks across cost, performance, security, fault tolerance |
| **Compute Optimizer** | ML-based right-sizing recommendations for EC2/EBS/Lambda |
| **Cost and Usage Report (CUR)** | Most granular billing data, for custom analysis/chargeback |

**Interview point**: a cost question almost always has a "cheapest
correct answer" — e.g., "logs need to be searchable for 30 days, then
kept for 7 years for compliance" → CloudWatch Logs (or OpenSearch) for
the hot 30 days, exported to S3 with a lifecycle policy into Glacier
Deep Archive for the long tail, not one expensive system doing both.

[⬆ Back to top](#top)

---

# 16. Migration and Hybrid Cloud

## The 7 R's of Migration

| Strategy | Description |
|---|---|
| **Rehost** ("lift and shift") | Move as-is, minimal changes — fastest, least optimized |
| **Replatform** ("lift, tinker, and shift") | Small optimizations during move (e.g., move DB to RDS) |
| **Repurchase** | Move to a SaaS/different product (e.g., CRM → Salesforce) |
| **Refactor/Re-architect** | Redesign for cloud-native (e.g., monolith → microservices) — most effort, most long-term benefit |
| **Retire** | Decommission — it's no longer needed |
| **Retain** | Keep on-prem for now (compliance, not yet ready) |
| **Relocate** | Move VMs at hypervisor level (e.g., VMware Cloud on AWS) without re-provisioning |

## Migration Tooling

| Tool | Purpose |
|---|---|
| **DMS (Database Migration Service)** | Migrate databases with minimal downtime, supports homogeneous and heterogeneous (via Schema Conversion Tool) migrations |
| **Application Migration Service (MGN)** | Lift-and-shift server migration (successor to CloudEndure) |
| **DataSync** | Automated, accelerated transfer of large datasets between on-prem and AWS storage |
| **Snowball/Snowball Edge/Snowmobile** | Physical data transfer devices for very large datasets where network transfer is impractically slow |
| **Migration Hub** | Central tracking dashboard across multiple migration tools/waves |

**Interview point**: "We need to move 500TB and our link is 100Mbps" —
do the math out loud (500TB over 100Mbps is roughly weeks) and conclude
Snowball is faster than network transfer; this kind of quick
back-of-envelope math is exactly what interviewers want to see.

[⬆ Back to top](#top)

---

# 17. Common Architecture Patterns

## Pattern: Highly Available 3-Tier Web Application

```text
Route 53
   │
CloudFront (static assets, WAF attached)
   │
ALB (public subnets, 2+ AZs)
   │
Auto Scaling Group of app servers (private subnets, 2+ AZs)
   │
Aurora Multi-AZ (private/isolated subnets) + ElastiCache for session/cache
   │
S3 (uploads, backups) + CloudWatch/X-Ray (observability)
```

## Pattern: Serverless Event-Driven API

```text
API Gateway → Lambda → DynamoDB
                 │
                 └─ EventBridge → downstream async processors
                                   (analytics, notifications via SNS)
Cognito for auth; X-Ray for tracing; DLQ on the Lambda for failed events.
```

## Pattern: Data Lake / Analytics Pipeline

```text
Sources → Kinesis Data Streams/Firehose → S3 (raw zone)
                                              │
                                     Glue (ETL, Data Catalog)
                                              │
                                   S3 (curated zone) → Athena (ad-hoc SQL)
                                              │                or
                                        Redshift (BI/dashboards via QuickSight)
```

## Pattern: Multi-Region Active-Passive DR (Warm Standby)

```text
Primary Region (us-east-1)          DR Region (us-west-2)
  ALB + ASG (full capacity)           ALB + ASG (scaled down, min=1)
  Aurora Global DB (writer)  ──────►  Aurora Global DB (reader, <1s lag)
  S3 (CRR target) ◄──────────────────  S3 (CRR source)

Route 53 failover routing policy, health check against primary ALB.
On failover: promote Aurora Global DB secondary to standalone writer,
scale DR ASG up via automation (runbook or Lambda-triggered).
```

## Pattern: Microservices on Containers

```text
API Gateway / ALB → ECS/EKS services (each microservice = own service +
                     task definition + ECR image)
                        │
                     Service discovery (Cloud Map) or internal ALB
                        │
                     Each service owns its data store (DynamoDB/RDS per
                     service — avoid a shared database across services)
                        │
                     EventBridge/SQS for async inter-service communication
```

[⬆ Back to top](#top)

---

# 18. Scenario-Based Interview Questions

Sample questions with the shape of a strong answer — practice stating
the requirement-gathering questions *first*, before jumping to services.

## "Design a globally distributed application with low latency for users worldwide."

- Clarify: read-heavy or write-heavy? Consistency requirements?
- Answer shape: CloudFront for static content at the edge; Global
  Accelerator or Route 53 latency-based routing for dynamic API traffic
  to the nearest regional deployment; DynamoDB Global Tables or Aurora
  Global Database for multi-region data; discuss the consistency
  trade-off explicitly (eventual consistency across regions).

## "A retail site needs to survive a 50x traffic spike on Black Friday."

- Clarify: is the spike predictable (scheduled scaling) or could it be
  unpredictable?
- Answer shape: ALB + ASG with target tracking (and pre-warming/scheduled
  scaling ahead of the known event), offload static assets to
  CloudFront/S3, cache hot reads in ElastiCache, decouple
  order-processing via SQS so a backend slowdown doesn't drop customer
  requests, load test beforehand (not "hope it scales").

## "How would you migrate a legacy on-prem monolith with a 500GB Oracle database to AWS with minimal downtime?"

- Answer shape: DMS with the Schema Conversion Tool if changing engine
  (e.g., to Aurora PostgreSQL), continuous replication during the
  migration window, cut over during a low-traffic window, keep the
  source as rollback for a defined period; mention Application
  Migration Service for the app-tier lift-and-shift if not refactoring
  yet.

## "Our S3 bucket got exposed publicly — walk me through your incident response."

- Answer shape: (1) immediately re-enable Block Public Access / fix the
  policy, (2) check CloudTrail for access during the exposure window to
  scope what was actually accessed, (3) rotate any credentials/secrets
  that may have been in the exposed objects, (4) use Macie to confirm
  whether PII was present, (5) root-cause how it happened (manual
  change? IaC drift?) and add a Config rule/SCP guardrail to prevent
  recurrence, (6) blameless postmortem.

## "How do you design for a service that must never lose a message, ever?"

- Answer shape: SQS with a DLQ, visibility timeout tuned to consumer
  processing time, idempotent consumer logic (since at-least-once
  delivery means possible duplicates), and if strict ordering/exactly-
  once matters, SQS FIFO; for cross-region durability, consider
  replicating critical events via EventBridge to a second region.

## "How would you reduce this account's AWS bill by 30% without hurting reliability?"

- Answer shape: start from Cost Explorer/Trusted Advisor data, not
  guesses — identify idle/oversized resources (Compute Optimizer),
  move steady-state workloads to Savings Plans, move fault-tolerant
  batch workloads to Spot, apply S3 lifecycle policies, shut down
  non-prod outside business hours, check for orphaned EBS
  volumes/snapshots/unattached Elastic IPs. Emphasize measuring before
  and after, not a one-time cut.

## "What single point of failure do you see in this diagram?" (whiteboard/live-review style)

- Practice spotting: a NAT Gateway in only one AZ, an RDS instance
  without Multi-AZ, an ALB with targets in only one AZ, a Lambda with no
  DLQ processing a critical queue, a hardcoded IP instead of a DNS name,
  a security group allowing `0.0.0.0/0` on a database port.

[⬆ Back to top](#top)

---

# 19. Service Comparison Cheat Sheet

Rapid-fire comparisons that come up constantly — know the one-line
distinguishing factor for each.

| Comparison | Distinguishing Factor |
|---|---|
| **S3 vs EBS vs EFS** | S3 = object store, internet-accessible, unlimited scale; EBS = block storage, single instance, one AZ; EFS = file storage, shared across many instances/AZs |
| **RDS vs Aurora vs DynamoDB** | RDS = managed traditional relational engines; Aurora = AWS-built MySQL/PostgreSQL-compatible, better scale/HA; DynamoDB = NoSQL, key-based access, near-infinite horizontal scale |
| **SQS vs SNS vs EventBridge** | SQS = pull queue, one consumer per message; SNS = push fan-out, no routing logic; EventBridge = push fan-out with content-based routing + SaaS integrations |
| **ALB vs NLB vs GWLB** | ALB = L7 content routing; NLB = L4 extreme performance/static IP; GWLB = L3 transparent appliance insertion |
| **Security Group vs NACL** | SG = stateful, instance-level, allow-only; NACL = stateless, subnet-level, allow+deny |
| **IAM Role vs IAM User** | Role = temporary credentials, assumed, no long-term secret; User = long-term identity, can have long-lived access keys (avoid where possible) |
| **KMS vs Secrets Manager vs Parameter Store** | KMS = manages encryption keys; Secrets Manager = stores/rotates secrets (uses KMS underneath); Parameter Store = general config/secrets storage, no built-in rotation |
| **CloudFront vs Global Accelerator** | CloudFront = HTTP content caching at the edge; Global Accelerator = network path optimization for any TCP/UDP traffic, static anycast IPs |
| **CloudWatch vs CloudTrail** | CloudWatch = performance metrics/logs ("how's it running"); CloudTrail = API audit log ("who did what") |
| **ECS vs EKS** | ECS = simpler, AWS-proprietary orchestration; EKS = managed Kubernetes, portable, steeper learning curve |
| **Multi-AZ vs Read Replica (RDS)** | Multi-AZ = synchronous standby for failover/DR, not readable directly (in older engines); Read Replica = asynchronous, for scaling read traffic, can be cross-region |
| **Spot vs On-Demand vs Reserved/Savings Plans** | Spot = cheapest, can be reclaimed; On-Demand = no commitment, full price; Reserved/Savings Plans = discount for committing to steady usage |
| **Athena vs Redshift** | Athena = serverless, ad-hoc SQL directly on S3, pay per query; Redshift = provisioned data warehouse, better for frequent/complex BI workloads |
| **Step Functions vs SQS/Lambda chaining** | Step Functions = explicit state machine, built-in retry/error handling/visibility; manual chaining = more fragile, harder to observe/debug |
| **VPC Peering vs Transit Gateway** | Peering = point-to-point, no transitive routing; Transit Gateway = hub-and-spoke, transitive, scales to many VPCs |
| **Direct Connect vs Site-to-Site VPN** | Direct Connect = dedicated private line, consistent low latency, slower to provision; VPN = over the internet, fast to set up, variable latency |

[⬆ Back to top](#top)

---

# 20. Common Pitfalls and Trick Questions

- **"Just use the biggest instance"** — interviewers will push back;
  always justify size against a stated metric (CPU/memory utilization
  target), not intuition.
- **Forgetting Multi-AZ is not a scaling mechanism** — candidates often
  say "Multi-AZ handles the read traffic," but the standby in RDS
  Multi-AZ (classic, non-Aurora) is not readable — that's what read
  replicas are for.
- **Treating NAT Gateway as free** — it has both an hourly charge and a
  per-GB data processing charge; a very common cost-question answer is
  "route AWS-service traffic through a VPC endpoint instead of NAT."
- **Assuming Security Groups are stateless** — they're stateful; only
  NACLs require explicit inbound *and* outbound rules.
- **Over-engineering for the stated RTO/RPO** — proposing active-active
  multi-region when the requirement tolerates hours of downtime signals
  you don't think about cost trade-offs.
- **Ignoring idempotency with at-least-once delivery** — SQS/SNS/Lambda
  retries can deliver a message more than once; a design that assumes
  exactly-once processing without idempotent handling is a common gap
  interviewers probe.
- **Confusing durability and availability** — S3's "11 nines" is
  durability (won't lose the object), not availability (can reach it
  right now); these answer different questions.
- **Forgetting encryption is opt-in for some services** — e.g., EBS
  encryption by default can (and should) be enabled account-wide, but
  it's a setting, not automatic everywhere.
- **Proposing a single NAT Gateway across all AZs** — a common
  reliability gap; one NAT Gateway is itself a single point of failure
  for every private subnet routing through it — deploy one per AZ for
  production.

[⬆ Back to top](#top)

---

# 21. AWS Services by Category

Every service covered above, grouped by category, with a brief
definition, its defining characteristics, and — the part interviewers
actually probe — why you'd pick it over the nearest alternative.

## Compute

| Service | Definition & Characteristics | Chosen Over the Alternative When |
|---|---|---|
| **EC2** | Resizable virtual machines (IaaS); full OS-level control; billed per second; wide instance family choice; On-Demand/Reserved/Spot pricing. | You need OS-level access, long-running processes, specialized licensing, or a steady-state workload where a Reserved Instance/Savings Plan beats Lambda/Fargate on cost. |
| **Lambda** | Event-driven, serverless function execution; no server management; max 15-minute runtime; scales automatically per invocation; billed per ms. | The workload is short-lived and event-driven/spiky — vs EC2/Fargate, avoid it for jobs >15 min, GPU workloads, or workloads needing persistent local state. |
| **Auto Scaling (ASG)** | Automatically adds/removes EC2 instances to match demand or replace unhealthy ones; target-tracking, step, or scheduled policies. | Any EC2 fleet with variable load — it's the standard scaling mechanism for EC2, as opposed to Fargate/Lambda which scale the underlying compute for you natively. |
| **AWS Batch** | Managed batch job scheduling/queuing across EC2, Spot, or Fargate; handles retries and dynamic provisioning. | The job runs longer than Lambda's 15-minute cap, needs a custom AMI/large compute, or is a massively parallel array job. |
| **Elastic Beanstalk** | PaaS that provisions and wires together EC2, ASG, and an ELB from an uploaded app bundle. | You want a fast, standard deployment without hand-configuring each piece — vs raw CloudFormation, trades granular control for speed; vs Lambda, fits apps that aren't naturally function-shaped. |

## Containers

| Service | Definition & Characteristics | Chosen Over the Alternative When |
|---|---|---|
| **ECS** | AWS-proprietary container orchestrator; simpler API than Kubernetes; task definitions and services. | The team wants simplicity and deep AWS integration without needing Kubernetes portability or its ecosystem. |
| **EKS** | Managed Kubernetes control plane; standard k8s API; portable across clouds. | You need multi-cloud portability, already have k8s expertise/tooling (Helm, operators), or need k8s-specific ecosystem features. |
| **Fargate** | Serverless compute *launch type* for ECS/EKS — no EC2 instances to patch or size. | You don't want to manage underlying instances at all; trade-off is less control and typically higher cost than EC2 launch type at sustained high utilization. |
| **ECR** | Fully managed private container registry; IAM-integrated; image scanning on push. | You need private images tied to IAM auth and native AWS scanning/lifecycle policies, vs a public registry like Docker Hub. |

## Storage

| Service | Definition & Characteristics | Chosen Over the Alternative When |
|---|---|---|
| **S3** | Object storage; 11 nines durability; HTTP(S) access; virtually unlimited scale; storage-class tiering. | You need internet-accessible object storage, static site hosting, a data lake, or a backup/archive target — not a mountable filesystem. |
| **EBS** | Block storage volume attached to a single EC2 instance within one AZ. | You need a traditional filesystem/boot volume or low-latency block access from exactly one instance (e.g., a database's data volume). |
| **EFS** | Managed NFS file system; shared concurrently across many instances/AZs; capacity scales elastically. | Multiple instances need concurrent read/write access to the same files — EBS can't do this (single-attach), only newer io2/gp3 multi-attach in narrow cases. |
| **FSx (Windows/Lustre)** | Managed third-party file systems — SMB with AD integration (Windows) or sub-millisecond HPC throughput (Lustre). | You need native Windows SMB/Active Directory file shares, or extreme HPC/ML training throughput that EFS doesn't provide. |
| **Storage Gateway** | Hybrid storage bridge — File/Volume/Tape gateway backing on-prem NFS/SMB/iSCSI/tape interfaces with S3/EBS. | On-prem systems must keep using familiar file/block/tape interfaces while data is actually stored in AWS. |

## Database

| Service | Definition & Characteristics | Chosen Over the Alternative When |
|---|---|---|
| **RDS** | Managed relational database (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server); AWS handles patching/backup. | You need a specific engine Aurora doesn't support (Oracle, SQL Server), or want the lower baseline cost of a standard engine — vs self-managed EC2, you avoid all engine/OS ops. |
| **Aurora** | AWS-built MySQL/PostgreSQL-compatible engine; storage auto-scales to 128TB; faster failover (~30s); up to 15 read replicas. | You need higher performance, availability, or read-scaling than standard RDS at the same wire-compatible engine. |
| **DynamoDB** | Managed NoSQL key-value/document store; single-digit-millisecond latency at any scale; access via partition/sort key. | The access pattern is key-based lookups needing massive horizontal scale and minimal ops — vs RDS/Aurora, trades relational query flexibility for scale and latency. |
| **ElastiCache (Redis/Memcached)** | Managed in-memory cache; Redis adds persistence, replication, and rich data structures/pub-sub; Memcached is simpler and pure cache. | You need a general-purpose cache in front of any data source, or (Redis specifically) durability/replication/pub-sub — vs DAX, which only fronts DynamoDB. |
| **DAX** | In-memory cache purpose-built in front of DynamoDB. | You need microsecond DynamoDB read caching without writing app-level cache logic yourself. |

## Networking & Content Delivery

| Service | Definition & Characteristics | Chosen Over the Alternative When |
|---|---|---|
| **VPC** | Logically isolated virtual network — subnets, route tables, gateways. | Foundational — every AWS network design starts here; no real alternative. |
| **Route 53** | Managed DNS with health checks and multiple routing policy types (weighted, latency, failover, geolocation). | You need deep AWS integration — alias records to AWS resources, health-check-driven failover — beyond what a third-party DNS provider offers. |
| **ALB** | Layer 7 (HTTP/HTTPS) load balancer; content-based routing by path/host; supports WebSocket. | Routing decisions depend on request content (path/host), or the workload is HTTP-based microservices — vs NLB, trades raw throughput for L7 intelligence. |
| **NLB** | Layer 4 (TCP/UDP) load balancer; extreme throughput; static/Elastic IP support. | You need a static IP, non-HTTP protocols, or the highest possible throughput/lowest latency — vs ALB, trades content-based routing for raw performance. |
| **GWLB** | Layer 3 transparent traffic inspection/load balancing. | You're inserting a third-party virtual appliance (firewall, IDS/IPS) transparently into the traffic path — not a fit for ALB/NLB's use cases. |
| **CloudFront** | CDN — caches content at edge locations close to users. | The content is cacheable HTTP(S) traffic (static assets, API responses with TTLs) — vs Global Accelerator, which doesn't cache. |
| **Global Accelerator** | Anycast static IPs routed over AWS's global network backbone. | Traffic is non-cacheable/non-HTTP (TCP/UDP), or you need a fixed IP to allow-list — vs CloudFront, optimizes network path rather than caching content. |
| **Direct Connect** | Dedicated private physical network link to AWS. | You need consistent low latency and high throughput and can accept a longer provisioning lead time — vs VPN, which rides the public internet. |
| **Site-to-Site VPN** | Encrypted IPsec tunnel over the public internet to on-prem. | You need to connect quickly and cheaply and can tolerate variable, internet-dependent latency — vs Direct Connect's predictability. |
| **Transit Gateway** | Hub-and-spoke connectivity hub for many VPCs/VPNs with transitive routing. | You're connecting more than a handful of VPCs and need transitive routing and centralized management — vs VPC Peering, which doesn't scale past a few connections. |
| **VPC Peering** | Direct point-to-point connection between exactly two VPCs; no transitive routing. | You only need to connect two VPCs and want to avoid Transit Gateway's hourly cost and added complexity. |
| **PrivateLink** | Private, one-directional service exposure via an ENI — no peering or route table changes needed. | You're exposing one specific service (not a whole VPC) to consumers, e.g. a SaaS provider pattern — vs Peering, avoids exposing the entire network. |

## Security, Identity & Compliance

| Service | Definition & Characteristics | Chosen Over the Alternative When |
|---|---|---|
| **IAM** | Identity and access management — users, groups, roles, policies; foundation for all AWS authorization. | Always — the baseline for every access-control decision in AWS. |
| **KMS** | Managed encryption key creation, rotation, and auditable usage (via CloudTrail); envelope encryption. | You need AWS-integrated encryption key management with policy-based access control and rotation. |
| **Secrets Manager** | Stores and automatically rotates secrets (DB credentials, API keys) via Lambda rotation functions. | The secret needs automatic rotation or fine-grained, secret-specific access policies — vs Parameter Store, costs more per secret but adds rotation. |
| **Systems Manager Parameter Store** | Stores config values and secrets (SecureString via KMS); standard tier is free. | The value is general config, or a secret that's rotated manually/infrequently, and cost is a concern — vs Secrets Manager, no built-in rotation. |
| **Cognito** | Managed user authentication (User Pools) plus federated temporary AWS credentials (Identity Pools). | You need managed sign-up/sign-in/MFA/social login without building and hardening auth yourself. |
| **WAF** | Layer 7 web filtering — SQLi/XSS rules, rate-based rules, geo-blocking; attaches to ALB/CloudFront/API Gateway. | You need to block specific malicious request *patterns*, not just absorb volumetric traffic — vs Shield, which handles the DDoS volume itself. |
| **Shield (Standard/Advanced)** | DDoS protection; Standard is automatic and free (L3/L4); Advanced adds L7 protection, cost protection, and DRT access. | Standard is always on by default; upgrade to Advanced when the business needs an SLA-backed response team and cost protection against a large attack. |
| **GuardDuty** | ML-based threat detection over CloudTrail, VPC Flow Logs, and DNS logs. | You need continuous, automated anomaly/threat detection instead of manually reviewing logs. |
| **Security Hub** | Aggregates findings from GuardDuty, Inspector, Config, and partner tools into one dashboard with compliance scoring. | You need a single pane of glass across many security tools instead of checking each dashboard separately. |
| **Inspector** | Automated vulnerability scanning for EC2, ECR images, and Lambda functions. | You need continuous automated CVE scanning of running workloads rather than manual patch tracking. |
| **Macie** | ML-based discovery and classification of sensitive data (PII) in S3. | You need to know where PII/sensitive data lives across S3 for a compliance requirement. |
| **Organizations (SCPs)** | Account/OU-level guardrails across a multi-account organization; caps maximum permissions, doesn't grant any. | You need an org-wide guardrail that holds regardless of what IAM policies an individual account defines — IAM alone can't enforce that across accounts. |

## Application Integration

| Service | Definition & Characteristics | Chosen Over the Alternative When |
|---|---|---|
| **API Gateway** | Managed API front door (REST/HTTP/WebSocket); request throttling, auth, validation, caching. | You need per-client throttling, request validation, native Lambda integration, or API key management — vs a bare ALB, adds an API-management layer. |
| **SQS** | Message queue; pull-based; decouples producer from consumer. Standard = at-least-once/best-effort order; FIFO = exactly-once/strict order at lower throughput. | Exactly one consumer should process each message and you need a durable buffer — vs SNS, which pushes to many subscribers instead. |
| **SNS** | Pub/sub messaging; push-based fan-out to many subscribers at once. | The same message must reach multiple independent subscribers immediately — vs SQS, which is single-consumer-per-message. |
| **EventBridge** | Event bus with content-based routing rules, a schema registry, and built-in SaaS/third-party event sources. | Routing depends on event *content*, not just fan-out, or you're integrating third-party/SaaS events — vs SNS's simpler, routing-free fan-out. |
| **Step Functions** | Visual state-machine orchestration with built-in retries, error handling, and long-running (up to 1 year) workflows. | A multi-step workflow needs visibility, retry logic, or human-approval steps — vs manually chaining Lambda calls, which is fragile and hard to observe. |
| **Amazon MQ** | Managed ActiveMQ/RabbitMQ. | You're migrating an existing app that already speaks JMS/AMQP and don't want to rewrite its messaging code for SQS/SNS. |

## Analytics & Big Data

| Service | Definition & Characteristics | Chosen Over the Alternative When |
|---|---|---|
| **Kinesis Data Streams** | Ordered, replayable real-time data stream with custom consumer applications. | You need custom processing logic, multiple independent consumers, or the ability to replay/reprocess data — vs Firehose, which has no custom consumer code. |
| **Kinesis Firehose** | Managed delivery stream straight to S3/Redshift/OpenSearch; no consumer code to write. | You need simple near-real-time loading/ETL with no custom processing — vs Data Streams, trades flexibility for zero ops. |
| **Redshift** | Provisioned, petabyte-scale columnar data warehouse for OLAP/BI. | Queries are frequent and complex and you need consistent performance — vs Athena, you're willing to provision and pay for a cluster continuously. |
| **Athena** | Serverless SQL directly over S3 (via the Glue Data Catalog); pay per query scanned. | Queries are ad-hoc or infrequent and you don't want to provision/manage a warehouse — vs Redshift, no cluster to size or keep running. |
| **EMR** | Managed Hadoop/Spark clusters for large-scale big-data processing. | You need full control over the cluster or a custom big-data framework at very large scale — vs Glue, which is serverless but less flexible. |
| **Glue** | Serverless ETL jobs plus a shared Data Catalog (schema registry for S3/Athena/Redshift). | You want managed, serverless ETL and a shared catalog without cluster management — vs EMR, less control but zero infrastructure. |
| **OpenSearch Service** | Managed search and log-analytics engine (Elasticsearch/Kibana-compatible). | You need full-text search or log-analytics dashboards — a query shape Athena/Redshift aren't built for. |
| **QuickSight** | Managed, serverless BI/dashboarding tool; pay-per-session pricing. | You want AWS-native dashboards directly over Redshift/Athena/S3 without standing up a third-party BI platform. |

## Management & Governance

| Service | Definition & Characteristics | Chosen Over the Alternative When |
|---|---|---|
| **CloudWatch** | Metrics, logs, alarms, and dashboards — answers "how is the system performing." | Always, for operational visibility — pairs with CloudTrail, which answers a different question (see below). |
| **CloudTrail** | Audit log of every API call made in the account — answers "who did what, when." | You're investigating an access/change event, not runtime performance — CloudWatch won't tell you *who* made an API call. |
| **Config** | Tracks resource configuration state/changes over time and evaluates them against compliance rules. | You need the current or historical *configuration state* of a resource, not just the API call that changed it — complements CloudTrail rather than replacing it. |
| **CloudFormation** | Declarative Infrastructure-as-Code using JSON/YAML templates. | You need repeatable, version-controlled infrastructure — vs manual console changes, gives auditability and repeatability; vs CDK, you prefer declarative templates over imperative code. |
| **Systems Manager** | Operational hub — Session Manager (no SSH keys/open ports), Patch Manager, Run Command, Parameter Store. | You need centralized, auditable fleet management without opening SSH/RDP ports to instances. |
| **Trusted Advisor** | Automated best-practice checks across cost, performance, security, and fault tolerance. | You want a quick automated health check across many dimensions without building custom checks yourself. |
| **Cost Explorer** | Visualizes and analyzes historical spend/usage trends. | You're investigating *why* a bill changed — the go-to first stop before Budgets or CUR. |
| **Budgets** | Proactive alerts when spend or usage crosses a defined threshold. | You need forward-looking alerts, not just historical analysis — vs Cost Explorer, which only looks backward. |
| **Compute Optimizer** | ML-based right-sizing recommendations for EC2, EBS, and Lambda. | You want data-driven right-sizing recommendations instead of guessing at instance sizes. |
| **AWS Backup** | Centralized, policy-based backup across EBS, RDS, DynamoDB, EFS, and more. | You need one policy/schedule managing backups across many services, plus cross-region/cross-account copy — vs per-service native snapshots managed separately. |

## Migration & Transfer

| Service | Definition & Characteristics | Chosen Over the Alternative When |
|---|---|---|
| **DMS** | Database migration with minimal downtime; homogeneous or heterogeneous (via the Schema Conversion Tool). | You need continuous replication during a live cutover window — vs a manual export/import, avoids an extended downtime window. |
| **Application Migration Service (MGN)** | Agent-based, continuous-replication lift-and-shift for whole servers/apps. | You're migrating entire servers/applications, not just a database — vs DMS, which is database-only. |
| **DataSync** | Automated, accelerated transfer of large datasets between on-prem and AWS storage, with scheduling and validation. | The transfer is large and recurring and needs scheduling/bandwidth throttling — vs manual `aws s3 cp`/rsync, adds validation and automation. |
| **Snowball family** | Physical data transfer devices shipped to you. | The dataset is so large that network transfer would take weeks/months, or no reliable network link exists — do the bandwidth math to justify this. |
| **Migration Hub** | Central dashboard tracking multiple migration tools/waves. | You're running many migrations across several tools and need one consolidated tracking view. |

## Category-to-Section Map

If a question centers on one of these categories, the deep-dive section
is:

- Compute → [§3](#3-compute) · Containers → [§11](#11-containers)
- Storage → [§4](#4-storage) · Database → [§5](#5-databases)
- Networking → [§6](#6-networking-vpc) and [§7](#7-load-balancing-and-dns)
- Security → [§8](#8-security-and-iam)
- Application Integration → [§12](#12-messaging-and-integration) and [§10](#10-serverless-architecture)
- Analytics → [§5](#5-databases) (warehousing subsection)
- Management & Governance → [§14](#14-monitoring-and-observability) and [§15](#15-cost-optimization)
- Migration → [§16](#16-migration-and-hybrid-cloud)

[⬆ Back to top](#top)

---

# 22. Troubleshooting Guide by Topic

## Connectivity ("EC2 instance can't reach the internet / can't be reached")

- Confirm the subnet's route table: public subnet needs a route to an
  IGW; private subnet needs a route to a NAT Gateway for *outbound*
  internet only.
- Check the Security Group (stateful, but the *initial* direction of
  traffic still needs an explicit allow rule) and the NACL (stateless —
  confirm both inbound and outbound rules exist).
- Confirm the instance actually has a public IP (or is behind something
  that does) if the expectation is direct internet reachability.
- For "can't reach an AWS service" from a private subnet, check for a
  missing VPC endpoint or a NAT Gateway that isn't provisioned in that AZ.

## Latency / Performance

- Check CloudWatch metrics first (CPU, memory via custom metric,
  network) before assuming it's a code problem.
- Use X-Ray to find which specific hop in a distributed request is slow,
  rather than guessing.
- For a database bottleneck: check for missing indexes, connection pool
  exhaustion, or whether a read replica/DAX/ElastiCache would offload
  read pressure.
- For Lambda cold-start latency on a sync-facing API: check package
  size, consider provisioned concurrency, or a lighter runtime.

## IAM "Access Denied" Debugging

```text
1. Identity-based policy — does the user/role have an explicit Allow
   for this action on this resource?
2. Resource-based policy — if calling a resource with its own policy
   (S3 bucket, KMS key), does IT allow this principal?
3. Permission boundary — is the role/user's boundary capping this action
   even if the identity policy allows it?
4. SCP — is an Organizations SCP denying this at the OU/account level,
   overriding everything below it?
5. Explicit Deny anywhere in the above — always wins, stop looking
   for an Allow once found.
Use IAM Access Analyzer / the policy simulator to test before guessing.
```

## Auto Scaling Not Behaving as Expected

- Confirm the scaling policy's target metric is actually reflecting
  load (a CPU-based policy won't react to a memory-bound or I/O-bound
  bottleneck — may need a custom CloudWatch metric).
- Check cooldown periods — a policy immediately reversing a scale-out
  can indicate cooldown is too short relative to how long new instances
  take to become healthy in the target group.
- Confirm health check type — EC2 status checks won't catch an
  application that's up but broken; switch to ELB health checks so the
  ASG replaces instances failing at the application layer.

## S3 Access Issues

- "403 Forbidden" despite a bucket policy allowing it → check Block
  Public Access settings (account and bucket level) aren't overriding
  the policy, and check for an explicit Deny in either the bucket
  policy or an attached IAM policy.
- Cross-account access failing → both the bucket policy (granting the
  other account) and an identity policy in the *requesting* account
  (allowing the action) are required — one without the other fails.

## Database Failover / Replication Lag

- Multi-AZ failover slower than expected → check whether DNS caching on
  the client side is delaying the switch to the new endpoint (RDS
  Multi-AZ failover changes what the same endpoint resolves to; clients
  with long DNS TTL caching can be slow to pick it up).
- Read replica lag growing → check for a single large write burst
  overwhelming replica apply, or an undersized replica instance class
  relative to the primary.

## Cost Spikes

- Check Cost Explorer grouped by service, then by linked account/tag —
  identify what changed, don't guess.
- Common surprise sources: NAT Gateway data processing charges, cross-AZ
  data transfer, unattached EBS volumes/old snapshots, a Lambda function
  in a retry loop, forgotten dev/test resources left running.

[⬆ Back to top](#top)

---

# 23. CLI / IaC Cheat Sheet

```bash
# EC2 / Auto Scaling
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"
aws autoscaling update-auto-scaling-group --auto-scaling-group-name my-asg \
  --desired-capacity 4 --min-size 2 --max-size 10

# S3
aws s3 cp ./file.txt s3://my-bucket/path/ --sse aws:kms
aws s3api put-bucket-lifecycle-configuration --bucket my-bucket \
  --lifecycle-configuration file://lifecycle.json
aws s3api put-public-access-block --bucket my-bucket \
  --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true

# IAM
aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::123456789012:role/app-role \
  --action-names s3:GetObject --resource-arns arn:aws:s3:::my-bucket/*
aws iam get-role --role-name app-role

# RDS
aws rds create-db-instance --db-instance-identifier mydb \
  --multi-az --engine postgres --db-instance-class db.r6g.large
aws rds describe-db-instances --db-instance-identifier mydb \
  --query 'DBInstances[0].MultiAZ'

# CloudWatch
aws cloudwatch put-metric-alarm --alarm-name high-cpu \
  --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average \
  --period 300 --threshold 80 --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 --alarm-actions arn:aws:sns:us-east-1:123456789012:alerts

# CloudTrail (incident investigation)
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=PutBucketPolicy

# CloudFormation
aws cloudformation deploy --template-file template.yaml --stack-name my-stack \
  --capabilities CAPABILITY_NAMED_IAM
```

```yaml
# Minimal CloudFormation — HA web tier skeleton
Resources:
  AppASG:
    Type: AWS::AutoScaling::AutoScalingGroup
    Properties:
      MinSize: 2
      MaxSize: 6
      DesiredCapacity: 2
      VPCZoneIdentifier: [!Ref PrivateSubnetA, !Ref PrivateSubnetB]
      TargetGroupARNs: [!Ref AppTargetGroup]
      LaunchTemplate:
        LaunchTemplateId: !Ref AppLaunchTemplate
        Version: !GetAtt AppLaunchTemplate.LatestVersionNumber

  AppALB:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Subnets: [!Ref PublicSubnetA, !Ref PublicSubnetB]
      SecurityGroups: [!Ref ALBSecurityGroup]
      Scheme: internet-facing
```

[⬆ Back to top](#top)

---

# 24. Study Checklist

- [ ] Explain the shared responsibility model with a concrete example
      of a customer-side failure.
- [ ] Walk through the Well-Architected six pillars from memory with one
      example service per pillar.
- [ ] Design a 3-tier HA web app on a whiteboard in under 5 minutes.
- [ ] Explain EBS vs EFS vs S3 without hesitation.
- [ ] Explain RDS Multi-AZ vs Read Replica vs Aurora Global Database.
- [ ] Design a DynamoDB table for a stated access pattern (partition/sort
      key choice, GSI if needed).
- [ ] Explain Security Group vs NACL with the stateful/stateless
      distinction.
- [ ] Draw a VPC with public/private subnets, IGW, NAT Gateway, and
      explain the route tables.
- [ ] Map a stated RTO/RPO to the correct DR strategy (backup/restore,
      pilot light, warm standby, active-active).
- [ ] Explain SQS vs SNS vs EventBridge with a one-line distinguishing
      factor for each.
- [ ] Explain ALB vs NLB vs GWLB and when each is the right choice.
- [ ] Walk through an IAM "Access Denied" debugging path (identity
      policy → resource policy → permission boundary → SCP → explicit
      deny).
- [ ] Explain the cost trade-off between On-Demand, Reserved/Savings
      Plans, and Spot, with a workload example for each.
- [ ] Answer at least 3 scenario questions from [§18](#18-scenario-based-interview-questions)
      out loud, including the clarifying questions you'd ask first.
- [ ] Practice spotting single points of failure in a given architecture
      diagram.
- [ ] Explain ECS vs EKS vs Fargate distinctly.
- [ ] State the 7 R's of migration from memory with one example each.

[⬆ Back to top](#top)
