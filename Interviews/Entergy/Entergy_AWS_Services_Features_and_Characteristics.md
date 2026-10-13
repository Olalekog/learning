<a id="top"></a>

# Entergy — AWS Services: Features and Characteristics

AWS Cloud Operations Engineer interview reference  
Updated: October 13, 2026

## Index

- [Service overview](#service-overview)
- [1. Amazon EC2 — Elastic Compute Cloud](#1-amazon-ec2--elastic-compute-cloud)
- [2. Amazon S3 — Simple Storage Service](#2-amazon-s3--simple-storage-service)
- [3. Amazon EBS — Elastic Block Store](#3-amazon-ebs--elastic-block-store)
- [4. Amazon VPC — Virtual Private Cloud](#4-amazon-vpc--virtual-private-cloud)
  - [Networking components to distinguish](#networking-components-to-distinguish)
- [5. AWS IAM — Identity and Access Management](#5-aws-iam--identity-and-access-management)
- [6. Amazon RDS — Relational Database Service](#6-amazon-rds--relational-database-service)
- [7. Amazon Route 53](#7-amazon-route-53)
- [8. Elastic Load Balancing — ELB](#8-elastic-load-balancing--elb)
- [9. Amazon EC2 Auto Scaling](#9-amazon-ec2-auto-scaling)
- [10. Amazon CloudWatch](#10-amazon-cloudwatch)
  - [Useful operations metrics](#useful-operations-metrics)
- [11. AWS Systems Manager — SSM](#11-aws-systems-manager--ssm)
- [12. AWS CloudFormation](#12-aws-cloudformation)
- [Supporting Services and Tools](#supporting-services-and-tools)
- [Key Comparisons to Rehearse](#key-comparisons-to-rehearse)
- [Interview Practice Framework](#interview-practice-framework)
- [Official References](#official-references)

## Service overview

The job description names 12 AWS services. Know each service's purpose, major features, operating responsibilities, and common failure points.

| Service | Primary purpose |
|---|---|
| EC2 | Virtual servers |
| S3 | Object storage |
| EBS | Persistent block storage for EC2 |
| VPC | Isolated cloud networking |
| IAM | Identity and permissions |
| RDS | Managed relational databases |
| Route 53 | DNS and DNS-based routing |
| Elastic Load Balancing | Distribute application traffic |
| EC2 Auto Scaling | Maintain and adjust instance capacity |
| CloudWatch | Metrics, logs, alarms, and dashboards |
| Systems Manager | Fleet administration and operational automation |
| CloudFormation | AWS infrastructure as code |

Console labels and feature availability can vary. Confirm account and Region before inspecting resources. The console paths below are navigation starting points.

[⬆ Go to top](#top)

## 1. Amazon EC2 — Elastic Compute Cloud

**Definition:** Provides virtual servers called instances.

**Features and characteristics:**

- Instance families optimized for general purpose, compute, memory, storage, and accelerated workloads.
- Supports Linux and Windows.
- Amazon Machine Images (AMIs) provide operating-system and software templates.
- Launch templates standardize instance configuration.
- Integrates with EBS, IAM roles, security groups, load balancing, and Auto Scaling.
- Offers On-Demand, Spot, and commitment-based purchasing options.
- Instances run in a particular Availability Zone; application resilience requires deliberate deployment across AZs.

**Operations focus:** Status checks, CPU, memory, disk, connectivity, patching, application services, and instance sizing.

**Console:** EC2 → Instances → select instance → Status and alarms / Monitoring / Networking / Security.

**Interview distinction:** AWS manages the underlying infrastructure; you normally manage the guest OS, installed software, configuration, and application.

[⬆ Go to top](#top)

## 2. Amazon S3 — Simple Storage Service

**Definition:** Stores objects in buckets, accessed through APIs rather than as an attached disk.

**Features and characteristics:**

- Objects consist of data and metadata, identified by object keys.
- Storage classes address access frequency, availability, and retention requirements.
- Versioning preserves multiple object versions.
- Lifecycle rules transition or expire objects.
- Replication supports eligible cross-Region and same-Region use cases.
- Supports encryption, IAM and bucket policies, and Block Public Access.
- Object Lock provides retention controls for supported configurations.
- Provides strong consistency for object reads and writes; versioning remains important for recovery.

**Operations focus:** AccessDenied errors, ownership, encryption permissions, lifecycle rules, replication, and storage costs.

**Console:** S3 → Buckets → select bucket → Objects / Properties / Permissions / Management.

**Interview distinction:** A private EC2 instance can reach S3 through NAT or an S3 gateway endpoint. The bucket does not need public access.

[⬆ Go to top](#top)

## 3. Amazon EBS — Elastic Block Store

**Definition:** Persistent block storage attached to EC2, typically used for operating systems and application data.

**Features and characteristics:**

- SSD options support general-purpose and IOPS-intensive workloads.
- HDD options support suitable throughput-oriented workloads.
- Volumes are Availability Zone scoped.
- Data persists independently of instance execution, subject to deletion settings.
- Supports snapshots, encryption through KMS, and volume modification.
- Snapshot copies support recovery in other Regions.
- Increasing volume capacity requires extending the filesystem to use additional space; partition expansion may also be required.

**Operations focus:** Capacity, IOPS, throughput, latency, attachment, snapshots, and filesystem health.

**Console:** EC2 → Volumes / Snapshots.

**Interview distinction:** EBS is block storage; S3 is object storage. They serve different access patterns.

[⬆ Go to top](#top)

## 4. Amazon VPC — Virtual Private Cloud

**Definition:** Provides a logically isolated network for AWS resources.

**Features and characteristics:**

- Uses IP address ranges defined through CIDR blocks.
- A VPC spans a Region; each subnet belongs to one Availability Zone.
- Route tables determine where traffic goes.
- Public subnets have a route to an Internet Gateway.
- Private subnets can use NAT for outbound connectivity.
- Security groups and network ACLs control traffic.
- Supports connectivity through peering, VPN, Transit Gateway, and endpoints.
- VPC Flow Logs provide network-flow evidence for troubleshooting.

**Operations focus:** Routes in both directions, subnet capacity, DNS, NAT, endpoints, and filtering.

**Console:** VPC → Your VPCs / Subnets / Route tables / Security groups / Network ACLs.

**Interview distinction:** A private subnet provides network isolation; it does not automatically grant or deny AWS API permissions.

### Networking components to distinguish

| Component | Characteristic |
|---|---|
| Security group | Stateful allow rules associated with network interfaces |
| Network ACL | Stateless allow/deny rules at subnet level, evaluated in order |
| Internet Gateway | Enables internet connectivity when addressing, routes, and security rules permit it |
| Public NAT Gateway | Enables outbound IPv4 access from private resources through its public-subnet route to an Internet Gateway |
| S3 gateway endpoint | Routes matching regional S3 traffic through an endpoint without NAT or an Internet Gateway |

[⬆ Go to top](#top)

## 5. AWS IAM — Identity and Access Management

**Definition:** Controls who can perform which actions on AWS resources.

**Features and characteristics:**

- Users, groups, roles, and policies represent identities and permissions.
- Roles provide temporary credentials when assumed.
- Trust policies determine who can assume a role.
- Permissions policies define allowed actions and resources.
- Conditions further restrict access.
- Permissions boundaries limit an identity's maximum permissions; they do not grant access.
- Organizational service control policies provide additional permission limits; they do not grant access.
- Explicit denies override allows.

**Operations focus:** Least privilege, role assumption, policy scope, unused access, and AccessDenied diagnosis.

**Console:** IAM → Roles → select role → Permissions / Trust relationships.

**Interview distinction:** Trust and permissions policies answer different questions: who can assume the role, and what the role can do.

[⬆ Go to top](#top)

## 6. Amazon RDS — Relational Database Service

**Definition:** Simplifies provisioning and operation of relational databases.

**Features and characteristics:**

- Supports multiple database engines and deployment options.
- Provides managed infrastructure and maintenance capabilities.
- Supports automated backups, snapshots, and point-in-time recovery.
- Multi-AZ options improve availability.
- Read replicas support eligible read-scaling and recovery use cases.
- Supports encryption, private networking, monitoring, and maintenance windows.
- Features vary by engine, version, Region, and deployment type.

**Operations focus:** Connections, CPU, free memory, storage, latency, events, backups, and maintenance.

**Console:** RDS → Databases → select database → Connectivity & security / Monitoring / Logs & events.

**Interview distinction:** Multi-AZ does not replace historical backups. Query tuning and application connection behavior still require customer attention. Do not assume every Multi-AZ standby is readable: Multi-AZ DB instances and Multi-AZ DB clusters differ.

[⬆ Go to top](#top)

## 7. Amazon Route 53

**Definition:** Provides DNS, domain-registration capabilities, health checks, and DNS-based routing.

**Features and characteristics:**

- Public hosted zones resolve public domain records.
- Private hosted zones provide DNS for associated VPCs.
- Alias records point to supported AWS resources.
- Routing policies include simple, weighted, latency, failover, and geographic options.
- Health checks can influence supported failover configurations.
- Route 53 Resolver supports hybrid DNS.
- TTL and caching influence how quickly clients observe DNS changes.

**Operations focus:** Record correctness, delegation, VPC associations, forwarding rules, health checks, and cached responses.

**Console:** Route 53 → Hosted zones / Health checks / Resolver.

**Interview distinction:** Route 53 answers DNS queries; it does not proxy each application request like a load balancer.

[⬆ Go to top](#top)

## 8. Elastic Load Balancing — ELB

**Definition:** Distributes traffic among registered targets.

| Type | Main characteristics | Typical use |
|---|---|---|
| Application Load Balancer | HTTP/HTTPS, host and path routing | Web applications and APIs |
| Network Load Balancer | Transport-level balancing, static IP capability | TCP, UDP, and TLS workloads |
| Gateway Load Balancer | Traffic distribution to network appliances | Firewall and inspection fleets |
| Classic Load Balancer | Earlier generation | Existing legacy deployments |

**Common features and characteristics:**

- Health checks identify target availability.
- Supports appropriate internal or internet-facing configurations, depending on type.
- Integrates with monitoring and Auto Scaling where applicable.
- Target deregistration settings help manage connection draining.
- Protocol, routing, security, and logging capabilities differ by type.

**Operations focus:** Healthy targets, listener rules, health-check paths, latency, errors, and security rules.

**Console:** EC2 → Load Balancers / Target Groups.

**Interview distinction:** Choose based on protocols, routing, and connectivity requirements rather than describing one type as universally faster.

[⬆ Go to top](#top)

## 9. Amazon EC2 Auto Scaling

**Definition:** Maintains an EC2 fleet and adjusts capacity.

**Features and characteristics:**

- Groups define minimum, desired, and maximum capacity.
- Launch templates define instance configuration.
- Replaces instances identified as unhealthy under configured health checks.
- Target tracking scales toward a selected metric target.
- Step scaling responds to alarm-based thresholds.
- Scheduled scaling anticipates known demand.
- Predictive scaling supports eligible recurring demand patterns.
- Lifecycle hooks allow custom launch and termination processing.

**Operations focus:** Scaling activity failures, quotas, subnet addresses, bootstrap, warmup, and dependency capacity.

**Console:** EC2 → Auto Scaling Groups → Activity / Automatic scaling / Instance management.

**Interview distinction:** Auto Scaling adjusts capacity; load balancing distributes traffic. They commonly work together. Configure the intended health-check integration rather than assuming application health is checked automatically.

[⬆ Go to top](#top)

## 10. Amazon CloudWatch

**Definition:** Provides operational observability through metrics, logs, alarms, and dashboards.

**Features and characteristics:**

- Collects AWS service metrics and custom metrics.
- Stores logs in log groups and streams.
- Logs Insights queries operational logs.
- Alarms evaluate metrics and trigger configured actions.
- Dashboards combine operational views.
- Supports application and infrastructure monitoring capabilities.
- The CloudWatch agent collects guest OS metrics and logs.
- Log retention and metric selection affect cost.

**Operations focus:** Thresholds, missing data, dimensions, timestamp correlation, and notification delivery.

**Console:** CloudWatch → Metrics / Alarms / Dashboards / Logs Insights.

**Interview distinction:** Standard EC2 metrics do not include guest memory or filesystem utilization; configure an agent or custom publisher.

### Useful operations metrics

| Component | Examples |
|---|---|
| EC2 | CPUUtilization, StatusCheckFailed, NetworkIn, NetworkOut |
| CloudWatch agent | mem_used_percent, disk_used_percent |
| ALB | TargetResponseTime, HealthyHostCount, HTTPCode_Target_5XX_Count |
| RDS | DatabaseConnections, FreeableMemory, FreeStorageSpace, CPUUtilization |

[⬆ Go to top](#top)

## 11. AWS Systems Manager — SSM

**Definition:** Provides administration and automation for managed nodes and operational workflows.

| Capability | Purpose |
|---|---|
| Session Manager | Controlled remote sessions |
| Run Command | Execute commands across selected nodes |
| Patch Manager | Scan and install patches |
| Inventory | Collect software and configuration information |
| State Manager | Maintain recurring configuration |
| Automation | Execute operational runbooks |
| Maintenance Windows | Schedule controlled operations |
| Parameter Store | Store configuration values and supported encrypted parameters |

**Features and characteristics:**

- Supports eligible AWS and hybrid managed nodes.
- Uses documents to define commands, configuration, and workflows.
- Tag-based targeting helps manage fleets.
- Supports concurrency and error controls for appropriate operations.
- Requires suitable permissions and network connectivity; node-management functions generally require SSM Agent.

**Operations focus:** Agent health, instance permissions, endpoints, targeting, concurrency, and execution results.

**Console:** Systems Manager → select the relevant capability.

**Interview distinction:** Session Manager does not require inbound SSH, but it needs its agent, permissions, and connectivity prerequisites. Standard session-content logging does not capture SSH or port-forwarding content.

[⬆ Go to top](#top)

## 12. AWS CloudFormation

**Definition:** Provisions and manages AWS resources from declarative templates.

**Features and characteristics:**

- Templates use YAML or JSON.
- Stacks manage related resources as a unit.
- Parameters customize deployments.
- Outputs expose resource information.
- Change sets preview proposed changes.
- Handles resource dependencies.
- Supports rollback behavior and supported drift detection.
- StackSets deploy across accounts and Regions.

**Operations focus:** Failed events, replacements, permissions, drift, and data-protection settings.

**Console:** CloudFormation → Stacks → Events / Resources / Parameters / Outputs.

**Interview distinction:** Template validation does not prove deployment will succeed. Check permissions, quotas, dependencies, replacements, and retention policies. Rollback is not a substitute for a database backup.

[⬆ Go to top](#top)

## Supporting Services and Tools

The role also refers to encryption, backups, costs, and automation. These supporting capabilities are relevant, although they are not all explicitly named services.

| Service or tool | Features and characteristics | Operations focus |
|---|---|---|
| AWS KMS | Managed cryptographic keys; key policies and grants control key use | Key state, permissions, encryption dependencies |
| AWS Backup | Central plans, vaults, retention, copies, and supported restore testing | Coverage, failed jobs, usable recovery points, restore evidence |
| Cost Explorer | Cost and usage analysis | Trends, allocation tags, unexpected spend |
| Terraform | IaC using providers, modules, plans, and state | Reviewed plans, state protection, drift, safe deployment |
| Python | General-purpose scripting; Boto3 supports AWS API automation | Pagination, retries, logging, safe resource selection |
| Bash | Linux shell and command automation | Diagnostics, exit codes, quoting, idempotency |
| PowerShell | Object-oriented shell and automation, especially for Windows | Services, event logs, disk, error handling |

AWS Backup copy and restore features vary by resource type and configuration. A successful backup job does not prove successful application recovery; perform restore and business-validation tests.

[⬆ Go to top](#top)

## Key Comparisons to Rehearse

| Comparison | Main distinction |
|---|---|
| EC2 vs RDS | General-purpose server administration vs managed relational database platform |
| S3 vs EBS | Object API storage vs attached block storage |
| Security group vs NACL | Stateful interface controls vs stateless subnet controls |
| IAM vs security group | API authorization vs network filtering |
| ALB vs NLB | HTTP-aware routing vs transport-level balancing |
| Auto Scaling vs ELB | Adjust capacity vs distribute traffic |
| CloudWatch vs Systems Manager | Observe and alert vs administer and automate |
| Terraform vs CloudFormation | Provider-based IaC with explicit state vs AWS-managed stacks |
| Multi-AZ vs backup | Availability through infrastructure failures vs historical recovery |
| NAT vs S3 gateway endpoint | General outbound connectivity vs matching regional S3 routing without NAT |

[⬆ Go to top](#top)

## Interview Practice Framework

For each service, answer:

1. What does it do?
2. Which features matter to this workload?
3. What can fail?
4. Which console views, metrics, logs, or commands do I inspect?
5. What correction is safe and approved?
6. How do I verify technical and business recovery?

[⬆ Go to top](#top)

## Official References

- [EC2 features](https://aws.amazon.com/ec2/features/)
- [S3 overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
- [EBS features](https://docs.aws.amazon.com/ebs/latest/userguide/EBSFeatures.html)
- [EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes.html)
- [VPC subnet route tables](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-route-tables.html)
- [VPC subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
- [IAM policies and access management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html)
- [RDS concepts](https://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/concepts.html)
- [RDS overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/)
- [Route 53 concepts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html)
- [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)
- [Elastic Load Balancing features](https://aws.amazon.com/elasticloadbalancing/features/)
- [EC2 Auto Scaling dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)
- [EC2 Auto Scaling methods](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scaling-overview.html)
- [CloudWatch overview](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/)
- [Systems Manager features](https://aws.amazon.com/systems-manager/features/)
- [Session Manager logging](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-logging.html)
- [CloudFormation stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html)
- [CloudFormation documentation](https://aws.amazon.com/documentation-overview/cloudformation/)
- [AWS Backup overview](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)

[⬆ Go to top](#top)
