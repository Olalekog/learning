<a id="top"></a>

# AWS Cloud/DevOps Job Requirements and Interview Preparation Guide

## Table of Contents

### Job Requirements and Technologies

1. [Overview of the Job Requirements](#overview-of-the-job-requirements)
2. [AWS Infrastructure Using Terraform](#1-aws-infrastructure-using-terraform)
3. [AWS Systems Manager and Runbook Development](#2-aws-systems-manager-and-runbook-development)
4. [CI/CD Using CodePipeline, CodeBuild, Azure DevOps, and GitHub](#3-cicd-using-codepipeline-codebuild-azure-devops-and-github)
5. [Core AWS Services](#4-core-aws-services)
   - [Amazon EC2](#amazon-ec2)
   - [Amazon EFS](#amazon-efs)
   - [Application Load Balancer](#application-load-balancer)
   - [Amazon Route 53](#amazon-route-53)
   - [AWS IAM](#aws-iam)
   - [AWS KMS](#aws-kms)
   - [Amazon Machine Images](#amazon-machine-images)
   - [Security Groups](#security-groups)
6. [AWS Networking](#5-aws-networking)
7. [Monitoring, Logging, and Auditing](#6-monitoring-logging-and-auditing)
8. [Secrets Manager and Parameter Store](#7-secrets-manager-and-parameter-store)
9. [Amazon ECS and ECR](#8-amazon-ecs-and-ecr)
10. [Automation Languages](#9-automation-languages)
11. [Red Hat Linux Administration](#10-red-hat-linux-administration)
12. [Windows Server 2022 Administration](#11-windows-server-2022-administration)
13. [Lambda and Step Functions](#12-lambda-and-step-functions)
14. [Amazon S3](#13-amazon-s3)
15. [RDS PostgreSQL](#14-rds-postgresql)
16. [DynamoDB](#15-dynamodb)
17. [SonarQube and JFrog](#16-sonarqube-and-jfrog)
18. [DevSecOps and Compliance](#17-devsecops-and-compliance)
19. [ArcGIS, Esri, FME, and AppStream](#18-arcgis-esri-fme-and-appstream)

### Interview Preparation

20. [Technical Interview Questions and Answers](#technical-interview-questions-and-answers)
21. [Behavioral Interview Questions](#behavioral-interview-questions)
22. [Topics to Study Before the Interview](#topics-to-study-before-the-interview)
23. [Strong Interview Introduction](#strong-interview-introduction)

### Reference

1. [AWS Services and Tools Glossary](#aws-services-and-tools-glossary)

[⬆ Back to top](#top)

---

# AWS Services and Tools Glossary

Quick one-line reference for every service, tool, and language mentioned in this guide.

## AWS Services

| Service | Description |
|---|---|
| **Amazon EC2** | Elastic Compute Cloud provides resizable virtual servers ("instances") in the cloud — you choose the CPU, memory, storage, and networking a workload needs and pay only for what you use, instead of owning physical hardware. |
| **AWS Systems Manager (SSM)** | A centralized operations hub for managing EC2 and hybrid on-prem/multi-cloud servers at scale — patching, running commands, enforcing configuration, and giving secure shell access — all without opening SSH/RDP ports or maintaining bastion hosts. |
| **— Session Manager** | An SSM capability that opens a browser-based or CLI shell/PowerShell session directly to an instance via the SSM Agent, giving interactive access with no open inbound ports, no SSH keys to manage, and a full session audit trail in CloudTrail. |
| **— Run Command** | An SSM capability that executes a predefined or custom command/script against one or thousands of managed instances at once and returns per-instance output — the ad-hoc, "run this right now" counterpart to a full Automation runbook. |
| **— Automation (Runbooks)** | SSM's workflow engine for multi-step operational procedures (validate → snapshot → patch → reboot → validate → rollback) defined in YAML/JSON, turning an error-prone manual runbook into a repeatable, auditable, self-service action. |
| **— Patch Manager** | Automates scanning and installing OS/application patches across a fleet on a defined schedule and patch baseline, replacing manual per-server patching with a consistent, reportable process. |
| **— Maintenance Windows** | Defines a scheduled time window — and which instances/tasks are allowed to run in it — during which disruptive operations like patching or reboots are permitted, keeping that activity out of business hours. |
| **— State Manager** | Continuously and automatically re-applies a defined configuration (an installed agent, a registry setting, a required package) to managed instances, correcting drift rather than only fixing it after someone notices. |
| **— Parameter Store** | A hierarchical key-value store for configuration data and encrypted secrets (via KMS-backed SecureString parameters) — commonly used for endpoints, AMI IDs, and other values that don't warrant Secrets Manager's rotation features. |
| **— Inventory** | Automatically collects and reports metadata (installed applications, OS version, running services, patch state) from managed instances, giving a queryable fleet-wide picture without logging into each box individually. |
| **Amazon EFS** | A fully managed, elastic NFS file system that many Linux EC2 instances or ECS/Fargate tasks can mount concurrently, growing and shrinking automatically as files are added or removed — unlike a single-instance-attached EBS volume. |
| **Application Load Balancer (ALB)** | A Layer-7 (HTTP/HTTPS) load balancer that routes requests to backend targets based on host, path, or header rules, health-checks those targets to route only to healthy ones, and terminates TLS — the standard front door for modern web traffic on AWS. |
| **Amazon Route 53** | AWS's highly available, scalable DNS service — public and private hosted zones, standard record types plus AWS "alias" records, health-check-based failover, and traffic-routing policies (weighted, latency-based, geolocation) for directing users to the right endpoint. |
| **AWS IAM** | Identity and Access Management is the authentication and authorization backbone of AWS, controlling exactly which users, roles, or services can call which APIs on which resources — the practical implementation of least privilege across an account. |
| **AWS KMS** | The Key Management Service creates, stores, and manages the encryption keys other AWS services (S3, EBS, RDS, EFS, Secrets Manager) use to encrypt data at rest, with fine-grained IAM-based access control over each key and full audit logging via CloudTrail. |
| **Amazon Machine Image (AMI)** | A reusable template capturing an EC2 instance's root volume — OS, patches, agents, pre-installed software — used to launch new instances in a known, consistent state; a "golden AMI" bakes in hardening and required agents so every new instance starts compliant. |
| **Security Groups** | Stateful, instance/ENI-level virtual firewalls that allow-list specific inbound and outbound traffic by protocol/port/source — "stateful" meaning a response to an allowed inbound request is automatically permitted back out without a matching outbound rule. |
| **Amazon VPC** | A Virtual Private Cloud is a logically isolated, software-defined network within AWS where you control the IP address range, subnets, route tables, and gateways — the foundational network boundary every other networked AWS resource lives inside. |
| **Internet Gateway** | A horizontally scaled, redundant VPC component that provides the actual path for traffic between public-subnet resources and the internet — without one attached, nothing in the VPC can reach or be reached from the internet. |
| **NAT Gateway** | A managed service that lets resources in a private subnet initiate outbound internet connections (e.g., downloading updates) while remaining unreachable from the internet, since inbound connections can't be initiated through it. |
| **Network ACLs** | Stateless, subnet-level firewall rules evaluated in numbered order for both inbound and outbound traffic — "stateless" meaning return traffic must be explicitly allowed by its own rule, unlike a security group — used as a coarse-grained complement to security groups. |
| **VPC Endpoints** | Private connectivity from inside a VPC to supported AWS services (S3, ECR, SSM, KMS, etc.) that never traverses the public internet — a Gateway Endpoint for S3/DynamoDB (route-table-based, free) or an Interface Endpoint for most other services (ENI-based, via PrivateLink). |
| **VPC Flow Logs** | Captures metadata about IP traffic to and from network interfaces in a VPC (source/destination, port, protocol, accept/reject) — not packet contents — and is the primary tool for diagnosing "why is this traffic being blocked" and for security/audit investigations. |
| **Amazon CloudWatch** | AWS's native observability service — collects metrics, logs, and events from AWS resources and applications, and provides alarms, dashboards, and Logs Insights queries for monitoring and alerting on system health. |
| **— CloudWatch Agent** | An optional agent installed on EC2/on-prem instances that collects OS-level metrics CloudWatch can't see natively (memory, disk usage, running processes) and forwards application or Windows Event Logs, extending CloudWatch past its default hypervisor-visible metrics. |
| **AWS CloudTrail** | Records every API call made against your AWS account — who (which IAM identity), what action, on which resource, from where, and when — the authoritative source for "who changed this" investigations and compliance audit trails, distinct from CloudWatch's system/application-behavior focus. |
| **AWS Secrets Manager** | Securely stores, encrypts (via KMS), versions, and can automatically rotate sensitive credentials like database passwords and API keys, with fine-grained IAM access control and full CloudTrail auditing — the higher-feature sibling of Parameter Store's SecureString, purpose-built for credentials specifically. |
| **Amazon ECR** | Elastic Container Registry is a fully managed, private Docker/OCI image registry integrated with IAM for access control and built-in vulnerability scanning of pushed images — the standard place to store images that ECS or EKS will later pull. |
| **Amazon ECS** | Elastic Container Service is AWS's native container orchestrator, running containers as "tasks" defined by a task definition, grouped into "services" for scaling/health management, on either self-managed EC2 capacity or the serverless Fargate launch type. |
| **AWS Lambda** | Serverless, event-driven compute that runs your code in response to a trigger (an API call, a file upload, a schedule) without provisioning or managing any servers, billed per invocation and execution time rather than for idle capacity. |
| **AWS Step Functions** | A serverless workflow orchestrator that coordinates multiple steps — Lambda invocations, other AWS API calls, human-approval waits — as a visual state machine, handling sequencing, parallel branches, retries, and error handling that would otherwise be hand-rolled glue code. |
| **Amazon S3** | Simple Storage Service is AWS's core object storage — durable, virtually unlimited-capacity storage for any file type, with versioning, lifecycle rules to transition/expire objects, fine-grained bucket/object policies, and event notifications on object changes. |
| **Amazon RDS (PostgreSQL)** | A fully managed relational database service running the PostgreSQL engine, where AWS handles patching and automated backups, and — with Multi-AZ enabled — synchronous standby replication and automatic failover, removing most of the operational burden of running a database yourself. |
| **Amazon DynamoDB** | A fully managed, serverless NoSQL key-value/document database delivering consistent single-digit-millisecond performance at virtually any scale, built around a partition key (and optional sort key) rather than SQL joins. |
| **AWS CodePipeline** | Orchestrates the end-to-end release process as a series of stages (source, build, test, deploy, manual approval), triggering automatically on a source change and calling out to services like CodeBuild or CodeDeploy to perform each stage's work. |
| **AWS CodeBuild** | A fully managed build service that checks out source code and runs the commands defined in a `buildspec.yml` (install, build, test, package) inside a fresh, temporary, isolated environment on every run — no build servers to provision or maintain. |
| **AWS Security Hub** | Aggregates, normalizes, and prioritizes security findings from GuardDuty, Inspector, Config, and other sources (plus third-party tools) into a single dashboard with a security score, so teams don't have to check each source separately. |
| **Amazon GuardDuty** | A continuous, ML/threat-intelligence-driven detection service that analyzes VPC Flow Logs, DNS logs, and CloudTrail events to flag likely malicious or unauthorized activity (e.g., an instance communicating with a known-bad IP) without requiring any agents to deploy. |
| **Amazon Inspector** | Automated, continuous vulnerability scanning for EC2 instances and container images in ECR, checking for known CVEs and network reachability issues and surfacing a risk score per finding. |
| **AWS Config** | Continuously records the configuration state of AWS resources over time and evaluates them against defined compliance rules (e.g., "no public S3 buckets"), flagging and optionally auto-remediating non-compliant resources — the configuration-compliance counterpart to CloudTrail's activity log. |
| **AWS AppStream 2.0** | A fully managed application-streaming service that runs desktop applications on AWS-hosted instances and streams the rendered output to a user's browser, so specialized or licensed software (like ArcGIS Pro) can be delivered to any device without local installation. |
| **Amazon SNS** | Simple Notification Service is a fully managed pub/sub messaging service that fans a published message out to many subscribers at once (email, SMS, Lambda, SQS queues) — commonly used for alerting and event broadcast. |
| **Amazon SQS** | Simple Queue Service is a fully managed message queue that decouples producers from consumers — a producer drops a message on the queue and moves on, while consumers pull and process at their own pace, smoothing out load spikes and adding resilience if a consumer is temporarily down. |
| **Amazon EventBridge** | A serverless event bus that routes events — from AWS services, SaaS partners, or your own applications — to targets like Lambda, Step Functions, or SNS based on rule-defined event patterns, the backbone of most "when X happens, automatically do Y" automation. |

## CI/CD and Source Control Tools

| Tool | Description |
|---|---|
| **Terraform** | HashiCorp's open-source, provider-agnostic Infrastructure-as-Code tool — you declare the desired end state of your infrastructure in HCL, and Terraform determines and executes the create/update/destroy operations needed to reach it, tracking what it manages in a state file. |
| **Azure DevOps** | Microsoft's application lifecycle platform bundling Git repos, YAML-based CI/CD pipelines, work-item tracking, and artifact feeds — commonly used for CI/CD orchestration, environment-scoped approvals, and variable-group-based secret management even outside pure Azure shops. |
| **GitHub** | A Git-based source control hosting platform providing pull-request-based code review, branch protection rules, required status checks, and GitHub Actions for CI/CD — the de facto standard for open-source and increasingly for enterprise source control as well. |

## Automation Languages and Operating Systems

| Item | Description |
|---|---|
| **Python** | A general-purpose, readable scripting language that's the dominant choice for AWS automation via the Boto3 SDK, Lambda function code, operational tooling, and reporting/remediation scripts. |
| **YAML** | A human-readable, indentation-based data-serialization format used almost everywhere infrastructure/pipeline configuration needs to be both machine-parseable and human-editable — CI/CD pipeline definitions, SSM Automation documents, configuration files. |
| **Bash** | The default Linux/Unix shell scripting language, used for instance user-data scripts, deployment steps, log collection, and general Linux automation glue. |
| **PowerShell** | Microsoft's object-oriented shell and scripting language — the standard tool for Windows Server administration, IIS management, Active Directory tasks, and Windows-side automation in a mixed-OS environment. |
| **Red Hat Linux** | An enterprise-grade Linux distribution administered through `systemd` (services), SELinux (mandatory access control), `firewalld` (host firewall), and `dnf`/`yum` package management — a common default in regulated or enterprise environments for its support lifecycle and hardening tooling. |
| **Windows Server 2022** | Microsoft's server operating system, administered via Services, Event Viewer, IIS (web hosting), Windows Firewall, and PowerShell, often integrated with Active Directory for centralized identity and Group Policy. |

## Code Quality and Security Scanning Tools

| Tool | Description |
|---|---|
| **SonarQube** | A static code analysis platform that scans source code for bugs, security vulnerabilities, "code smells," and duplication, and enforces a configurable Quality Gate that can block a pipeline from proceeding if code quality falls below the bar. |
| **JFrog Artifactory** | A universal binary/artifact repository that stores and manages versioned build outputs across virtually any package format (Docker, npm, Maven/Java, PyPI, Helm), with promotion workflows to move a vetted artifact from a dev repo to a production-ready one. |
| **JFrog Xray** | Security and license-compliance scanning integrated directly into Artifactory, analyzing stored artifacts (and their dependencies) for known vulnerabilities and license policy violations before they're consumed downstream. |
| **Checkov** | An open-source static analysis tool purpose-built for Infrastructure-as-Code (Terraform, CloudFormation, Kubernetes manifests), catching misconfigurations — like an unencrypted S3 bucket or an overly permissive security group — before the infrastructure is ever provisioned. |
| **Trivy** | An open-source, all-in-one scanner covering container images, filesystems, and IaC configurations for known vulnerabilities (CVEs) and misconfigurations, popular for its speed and broad single-tool coverage. |

## GIS Platform Tools

| Tool | Description |
|---|---|
| **ArcGIS Enterprise** | Esri's on-premises/cloud-deployable GIS platform — a suite of components (Portal, Server, Data Store) working together to publish, manage, and share maps, spatial data, and geospatial applications across an organization. |
| **Portal for ArcGIS** | The web-based front end of ArcGIS Enterprise where users discover, view, and share maps, apps, and geospatial content, and where user/group access to that content is managed. |
| **ArcGIS Server** | The component that actually hosts and serves map, feature, geoprocessing, and imagery services consumed by web maps, apps, and desktop GIS clients. |
| **ArcGIS Data Store** | The managed backend data storage layer supporting ArcGIS Server's hosted feature layers and other hosted services, so Server doesn't have to talk directly to a raw database for every request. |
| **ArcGIS Pro** | Esri's desktop GIS application for advanced spatial analysis, cartography, and publishing content up to ArcGIS Enterprise or ArcGIS Online. |
| **FME Core / FME Engine** | Safe Software's spatial ETL (extract-transform-load) engine for converting between GIS data formats, transforming geospatial data structures, and automating integration workflows between disparate systems — the geospatial-data equivalent of a general-purpose ETL tool. |

[⬆ Back to top](#top)

---

# Overview of the Job Requirements

This is a senior-level AWS Cloud Infrastructure, DevOps, and Systems Automation position. The person in this role will be responsible for building AWS infrastructure, automating deployments, administering operating systems, supporting applications, troubleshooting production issues, and maintaining security and operational documentation.

The most important areas are:

1. AWS infrastructure administration
2. Terraform and Infrastructure as Code
3. AWS Systems Manager automation and runbooks
4. CI/CD using CodePipeline, CodeBuild, Azure DevOps, and GitHub
5. Linux and Windows Server administration
6. AWS networking and security
7. Monitoring, logging, and incident response
8. Containers, serverless applications, databases, and storage
9. DevSecOps, documentation, and disaster recovery
10. ArcGIS and GIS platform support

[⬆ Back to top](#top)

---

# 1. AWS Infrastructure Using Terraform

You are expected to create and manage AWS infrastructure using code rather than manually creating resources in the AWS Management Console.

Terraform configuration files should define resources such as:

- VPCs
- Subnets
- Route tables
- Security groups
- EC2 instances
- Application Load Balancers
- EFS file systems
- Route 53 records
- IAM roles and policies
- KMS keys
- S3 buckets
- RDS databases
- DynamoDB tables
- ECS clusters
- ECR repositories

The company wants repeatable and consistent infrastructure deployments across development, testing, staging, and production environments.

## Terraform Concepts

### Providers

```hcl
provider "aws" {
  region = var.aws_region
}
```

### Resources

```hcl
resource "aws_s3_bucket" "application_data" {
  bucket = "company-application-data"
}
```

### Variables

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"
}
```

### Outputs

```hcl
output "load_balancer_dns" {
  value = aws_lb.application.dns_name
}
```

### Modules

Modules package related Terraform resources into reusable components. A VPC module may include the VPC, subnets, route tables, internet gateway, NAT gateway, network ACLs, and VPC endpoints.

### Terraform State

Terraform state records which real resources are associated with the Terraform configuration.

State should be:

- Stored remotely
- Encrypted
- Access controlled
- Versioned
- Protected from simultaneous modification
- Separated by environment

## Terraform Cloud Workspaces

Terraform Cloud Workspaces provide separate environments for Terraform execution and state management.

Examples:

- `application-dev`
- `application-test`
- `application-stage`
- `application-prod`

Each workspace can have its own variables, credentials, state, execution history, access permissions, and approval controls.

## Infrastructure as Code Best Practices

- Use reusable modules
- Store state remotely
- Enable locking
- Pin provider and module versions
- Add variable validation
- Apply consistent tagging
- Run formatting and validation automatically
- Require pull-request review
- Scan Terraform for security issues
- Separate production approvals
- Avoid hard-coded values
- Keep secrets out of Terraform files
- Review `terraform plan` before `terraform apply`

[⬆ Back to top](#top)

---

# 2. AWS Systems Manager and Runbook Development

This is one of the most important requirements in the job description.

AWS Systems Manager provides centralized management and automation for EC2 instances, hybrid servers, applications, operating systems, and AWS resources.

It can be used to:

- Execute commands remotely
- Patch Linux and Windows servers
- Automate operational workflows
- Manage configuration
- Access instances without SSH or RDP
- Store configuration parameters
- Schedule maintenance
- Maintain inventory
- Create golden AMIs
- Automate incident remediation

## Session Manager

Session Manager provides shell or PowerShell access to EC2 without requiring SSH keys, RDP exposure, bastion hosts, or public IP addresses.

## Run Command

Run Command executes commands remotely on one or more managed nodes.

Common examples:

- Restart an application service
- Install software
- Collect logs
- Check disk utilization
- Update configuration files
- Run PowerShell or Bash commands

## Automation Runbooks

An Automation Runbook is a multi-step operational workflow written in YAML or JSON.

A runbook could:

1. Validate input parameters
2. Check EC2 instance status
3. Create an AMI backup
4. Stop an application
5. Apply patches
6. Reboot the instance
7. Restart services
8. Validate a health endpoint
9. Send notifications
10. Roll back if validation fails

## Patch Manager

Patch Manager automates operating-system and application patching for Red Hat Linux and Windows Server.

## Maintenance Windows

Maintenance Windows define when disruptive activities may happen.

## State Manager

State Manager helps ensure instances remain in the required configuration.

## Parameter Store

Parameter Store stores configuration and encrypted values such as database endpoints, AMI IDs, application URLs, deployment versions, and IAM role ARNs.

## Inventory

Inventory collects information about installed software, operating-system details, services, files, and Windows updates.

## SSM Managed-Node Requirements

An EC2 instance generally needs:

- SSM Agent installed and running
- An IAM instance profile
- Systems Manager permissions
- Network access to SSM endpoints
- Correct DNS and route configuration

## Example SSM Automation Document

```yaml
schemaVersion: "0.3"
description: Restart and validate an application service

parameters:
  InstanceId:
    type: String

mainSteps:
  - name: RestartApplication
    action: aws:runCommand
    inputs:
      DocumentName: AWS-RunShellScript
      InstanceIds:
        - "{{ InstanceId }}"
      Parameters:
        commands:
          - sudo systemctl restart application
          - sudo systemctl status application
```

[⬆ Back to top](#top)

---

# 3. CI/CD Using CodePipeline, CodeBuild, Azure DevOps, and GitHub

CI/CD automates source retrieval, validation, testing, security scanning, build, artifact publishing, deployment, promotion, and release approval.

## AWS CodePipeline

CodePipeline orchestrates the release stages.

A typical pipeline:

1. Source from GitHub
2. Terraform formatting and validation
3. Security scanning
4. CodeBuild execution
5. Terraform plan
6. Manual approval
7. Terraform apply
8. Application deployment
9. Health validation
10. Notification

## AWS CodeBuild

CodeBuild executes build and test commands in a temporary environment.

It can:

- Install dependencies
- Run tests
- Build applications
- Run Terraform
- Build Docker images
- Push images to ECR
- Execute security scans
- Publish reports and artifacts

## Example `buildspec.yml`

```yaml
version: 0.2

phases:
  install:
    commands:
      - terraform version

  pre_build:
    commands:
      - terraform fmt -check
      - terraform init
      - terraform validate

  build:
    commands:
      - terraform plan -out=tfplan

artifacts:
  files:
    - tfplan
```

## Azure DevOps

Azure DevOps may be used for source repositories, YAML pipelines, variable groups, approvals, service connections, self-hosted agents, environments, and artifact management.

## GitHub

Important GitHub concepts:

- Branch protection
- Pull requests
- Required reviewers
- Status checks
- Merge controls
- GitHub Actions
- Tags and releases
- Repository secrets
- Environments and production approvals

## Secure Pipeline Controls

- Protected branches
- Pull-request approval
- Automated tests
- Terraform validation
- Infrastructure scanning
- SonarQube quality gates
- Artifact versioning
- Container scanning
- Least-privilege roles
- Secure secret retrieval
- Manual production approvals
- Rollback procedures
- Audit logging

[⬆ Back to top](#top)

---

# 4. Core AWS Services

## Amazon EC2

EC2 provides virtual servers in AWS.

Key areas:

- Instance types
- AMIs
- EBS volumes
- Instance profiles
- Security groups
- User data
- Elastic IP addresses
- Auto Scaling
- IMDSv2
- Monitoring and troubleshooting

## Amazon EFS

EFS is a managed NFS file system that can be mounted by multiple Linux EC2 instances or ECS tasks.

Key areas:

- Mount targets
- NFS port 2049
- Security groups
- Access points
- Encryption
- Throughput modes
- Lifecycle policies
- Backup
- File permissions

## Application Load Balancer

An ALB distributes HTTP and HTTPS traffic.

Key areas:

- Listeners
- Target groups
- Health checks
- Routing rules
- Host- and path-based routing
- TLS certificates
- Sticky sessions
- Access logs

## Amazon Route 53

Route 53 provides DNS services.

It supports:

- Public and private hosted zones
- A, AAAA, CNAME, and alias records
- Health checks
- Failover routing
- Weighted routing
- Latency-based routing

## AWS IAM

IAM controls authentication and authorization.

Important concepts:

- Users
- Groups
- Roles
- Identity policies
- Resource policies
- Trust policies
- Permission boundaries
- Cross-account access
- Least privilege
- Temporary credentials

## AWS KMS

KMS manages encryption keys for EBS, S3, RDS, EFS, Secrets Manager, Parameter Store, CloudWatch Logs, SNS, and SQS.

## Amazon Machine Images

An AMI is a template used to launch EC2 instances. A golden AMI may include operating-system patches, monitoring agents, security software, SSM Agent, and application prerequisites.

## Security Groups

Security groups are stateful firewalls applied to network interfaces.

A secure design may allow:

- HTTPS from users to the ALB
- Application traffic from the ALB to application servers
- PostgreSQL only from application servers
- NFS only from approved systems

[⬆ Back to top](#top)

---

# 5. AWS Networking

A VPC is a logically isolated network in AWS.

A production VPC may include:

- Public subnets
- Private application subnets
- Private database subnets
- Internet Gateway
- NAT Gateway
- Route tables
- Security groups
- Network ACLs
- VPC endpoints
- VPC Flow Logs

## Public Subnet

A public subnet has a route to an Internet Gateway.

## Private Subnet

A private subnet does not have a direct route to the Internet Gateway.

## NAT Gateway

A NAT Gateway allows private resources to access the internet without accepting unsolicited inbound traffic.

## VPC Endpoints

VPC endpoints provide private access to services such as S3, Systems Manager, ECR, CloudWatch Logs, Secrets Manager, and KMS.

## VPC Flow Logs

VPC Flow Logs record network metadata and help troubleshoot rejected traffic, unexpected destinations, and security-control issues.

[⬆ Back to top](#top)

---

# 6. Monitoring, Logging, and Auditing

## Amazon CloudWatch

CloudWatch provides:

- Metrics
- Logs
- Alarms
- Dashboards
- Logs Insights
- Metric filters
- Agent-based operating-system metrics
- Event-driven remediation

## Typical Metrics

### EC2

- CPU utilization
- Status-check failures
- Memory
- Disk
- Network traffic

### ALB

- HTTP 4xx and 5xx
- Target response time
- Unhealthy host count
- Request count

### RDS

- CPU
- Connections
- Free storage
- Read/write latency
- Freeable memory

### ECS

- CPU
- Memory
- Running task count
- Deployment failures

## CloudWatch Agent

Collects memory, disk, process metrics, Linux logs, and Windows Event Logs.

## CloudTrail

CloudTrail records AWS API activity and helps determine who changed a resource, when it happened, from which source, and with which role.

[⬆ Back to top](#top)

---

# 7. Secrets Manager and Parameter Store

## AWS Secrets Manager

Used for:

- Database passwords
- API tokens
- Application credentials
- Third-party credentials

Features:

- KMS encryption
- Versioning
- IAM access control
- Automatic rotation
- CloudTrail auditing

## Systems Manager Parameter Store

Used for:

- Configuration values
- Environment variables
- AMI IDs
- API endpoints
- Resource identifiers
- SecureString parameters

## Best Practices

- Never hard-code credentials
- Use IAM roles instead of access keys
- Encrypt with KMS
- Restrict access by application and environment
- Rotate sensitive credentials
- Audit access using CloudTrail

[⬆ Back to top](#top)

---

# 8. Amazon ECS and ECR

## Amazon ECR

ECR stores Docker container images.

A typical pipeline:

1. Build the image
2. Tag it with a version
3. Scan it
4. Authenticate to ECR
5. Push it
6. Update the ECS task definition

## Amazon ECS

ECS runs containers using clusters, task definitions, services, tasks, and EC2 or Fargate capacity.

## ECS Task Definition

Defines:

- Container image
- CPU and memory
- Ports
- Environment variables
- Secrets
- Logging
- Health checks
- Task role
- Execution role
- Volumes

## Execution Role vs Task Role

The execution role lets ECS pull images, retrieve referenced secrets, and write logs. The task role gives the running application permission to call AWS services.

[⬆ Back to top](#top)

---

# 9. Automation Languages

## Python

Used for Boto3 automation, Lambda functions, APIs, reporting, health checks, and incident remediation.

## YAML

Used for CodeBuild, Azure DevOps, GitHub Actions, SSM documents, and configuration files.

## Bash

Used for Linux configuration, deployment, validation, log collection, and user data.

## PowerShell

Used for Windows Server administration, services, IIS, Event Logs, registry changes, patching, and scheduled tasks.

[⬆ Back to top](#top)

---

# 10. Red Hat Linux Administration

You should understand:

- Users and groups
- Permissions
- Package management
- systemd
- SELinux
- firewalld
- SSH
- Networking
- Filesystems
- LVM
- Logs
- Patching
- Process and performance troubleshooting

Useful commands:

```bash
systemctl status application
journalctl -u application
df -h
du -sh /var/log/*
free -m
top
ps -ef
ss -tulpn
lsblk
ip address
ip route
dnf update
firewall-cmd --list-all
getenforce
```

[⬆ Back to top](#top)

---

# 11. Windows Server 2022 Administration

You should understand:

- Windows services
- Event Viewer
- PowerShell
- Windows Firewall
- Disk Management
- NTFS permissions
- IIS
- Windows Update
- Scheduled Tasks
- Registry management
- Performance Monitor
- Active Directory integration

Useful PowerShell commands:

```powershell
Get-Service
Restart-Service -Name W3SVC
Get-WinEvent -LogName System -MaxEvents 50
Get-Process
Get-NetTCPConnection
Get-Volume
Test-NetConnection server.example.com -Port 443
Get-HotFix
```

[⬆ Back to top](#top)

---

# 12. Lambda and Step Functions

## AWS Lambda

Lambda runs event-driven code without persistent server management.

Common uses:

- Automated remediation
- API backends
- File processing
- Scheduled tasks
- Resource tagging
- Compliance checks

## AWS Step Functions

Step Functions coordinates tasks using sequential steps, parallel processing, retries, branching, waiting, and error handling.

[⬆ Back to top](#top)

---

# 13. Amazon S3

S3 provides object storage.

Important areas:

- Buckets and objects
- Versioning
- Lifecycle policies
- Encryption
- Bucket policies
- Block Public Access
- Replication
- Event notifications
- Object Lock
- Storage classes
- Presigned URLs

[⬆ Back to top](#top)

---

# 14. RDS PostgreSQL

RDS PostgreSQL is a managed relational database.

Important areas:

- Subnet groups
- Security groups
- Parameter groups
- Automated backups
- Snapshots
- Multi-AZ
- Read replicas
- Encryption
- Performance Insights
- CloudWatch monitoring
- Maintenance windows

Common issues:

- Connection failures
- Incorrect security groups
- Wrong endpoint or port
- DNS problems
- Expired credentials
- Connection exhaustion
- Slow queries
- Storage limitations
- Locks and blocking

[⬆ Back to top](#top)

---

# 15. DynamoDB

DynamoDB is a managed NoSQL key-value and document database.

Important concepts:

- Partition keys
- Sort keys
- Secondary indexes
- On-demand capacity
- Provisioned capacity
- Auto Scaling
- Streams
- TTL
- Global tables
- Encryption
- Point-in-time recovery

[⬆ Back to top](#top)

---

# 16. SonarQube and JFrog

## SonarQube

SonarQube checks code for:

- Bugs
- Vulnerabilities
- Security hotspots
- Code smells
- Duplication
- Test coverage
- Maintainability

## JFrog Artifactory

JFrog stores and manages versioned artifacts such as Java, Python, Node.js, .NET, Helm, Docker, and binary packages.

[⬆ Back to top](#top)

---

# 17. DevSecOps and Compliance

Expected controls include:

- Static code analysis
- Dependency scanning
- Container scanning
- Terraform scanning
- Secrets scanning
- Code review
- Least-privilege IAM
- Encryption
- Logging
- Patch management
- Artifact control
- Production approvals
- Backup and recovery testing

Possible tools:

- SonarQube
- Checkov
- Trivy
- JFrog Xray
- Security Hub
- GuardDuty
- Inspector
- AWS Config
- CloudTrail
- CloudWatch

[⬆ Back to top](#top)

---

# 18. ArcGIS, Esri, FME, and AppStream

## ArcGIS Enterprise

A GIS platform for mapping, analysis, data sharing, and geospatial applications.

## Portal for ArcGIS

Provides maps, applications, content, users, and groups.

## ArcGIS Server

Hosts map, feature, geoprocessing, and image services.

## ArcGIS Data Store

Stores data used by hosted GIS services.

## ArcGIS Pro

A desktop GIS application for mapping, spatial analysis, and publishing.

## FME Core and FME Engine

Used for geospatial data transformation, conversion, integration, and automation.

## AWS AppStream 2.0

Streams desktop applications to users through a browser.

[⬆ Back to top](#top)

---

# Technical Interview Questions and Answers

## 1. Tell me about your experience with AWS and Terraform.

I have hands-on experience designing and managing AWS infrastructure using Terraform and reusable modules. I have worked with services including VPC, EC2, IAM, KMS, S3, ALB, Route 53, RDS, DynamoDB, ECS, ECR, CloudWatch, CloudTrail, Secrets Manager, and Systems Manager.

I organize Terraform code into reusable modules and maintain environment-specific configurations for development, testing, and production. I use remote state, version constraints, validation, pull-request reviews, security scanning, and production approval gates.

## 2. How would you structure a reusable Terraform repository?

I would separate reusable modules from environment-specific configurations. The modules directory would contain VPC, EC2, ALB, RDS, IAM, EFS, and monitoring modules. Environment directories or Terraform Cloud Workspaces would provide environment-specific values.

## 3. What is the difference between SSM Run Command and Automation?

Run Command executes commands directly on managed nodes. SSM Automation coordinates a complete multi-step workflow that may call AWS APIs, invoke Lambda, create AMIs, wait for resources, validate results, and perform rollback.

## 4. Describe an SSM Runbook you have developed.

A good example is a patching and validation runbook. It validates the target instance, creates an AMI or snapshot, stops the application, applies patches, reboots the server, restarts services, validates the application, sends notifications, and invokes rollback when necessary.

## 5. How do you troubleshoot an EC2 instance that is not appearing in Systems Manager?

Check the SSM Agent, IAM instance profile, DNS, routes, internet/NAT or VPC endpoint access, security controls, and SSM Agent logs.

## 6. How would you design an automated patching process?

Group instances by tags or patch groups, define patch baselines, schedule Maintenance Windows, patch nonproduction first, create backups, validate applications, notify operations, and require approval before production.

## 7. Explain how CodePipeline and CodeBuild work together.

CodePipeline orchestrates the release stages, while CodeBuild performs validation, testing, scanning, build, and packaging tasks.

## 8. What would you put in a secure CI/CD pipeline?

Branch protection, pull-request approval, tests, code scanning, dependency scanning, Terraform scanning, container scanning, secrets detection, artifact versioning, least-privilege roles, manual production approval, logging, and rollback controls.

## 9. How do you manage Terraform state?

Store state remotely, encrypt it, separate it by environment, enable locking, version it, and restrict access.

## 10. How do you troubleshoot a Terraform failure?

Review the exact error, IAM permissions, variables, provider versions, dependencies, quotas, existing resources, and state consistency. Run `terraform plan` and correct the root cause before applying again.

## 11. How would you design a highly available AWS application?

Use multiple Availability Zones, an ALB, private application subnets, Auto Scaling or ECS services, Multi-AZ RDS, EFS where required, CloudWatch, Route 53, encryption, backups, and tested recovery procedures.

## 12. How do you troubleshoot an unhealthy ALB target?

Review the target-health reason, health-check path and port, application status, security groups, network ACLs, logs, listener rules, and the endpoint directly from inside the VPC.

## 13. What is the difference between a security group and a network ACL?

A security group is stateful and attached to a network interface. A network ACL is stateless and applies at the subnet level.

## 14. How do you securely manage application secrets?

Use Secrets Manager or Parameter Store, KMS encryption, IAM roles, least-privilege access, rotation, and CloudTrail auditing. Never hard-code credentials.

## 15. How do you monitor AWS infrastructure?

Use CloudWatch metrics, logs, alarms, dashboards, and Logs Insights. Use CloudTrail for API auditing and EventBridge or SNS for alert routing.

## 16. What is the difference between CloudWatch and CloudTrail?

CloudWatch monitors system and application behavior. CloudTrail records AWS API activity and identifies who changed resources.

## 17. How would you troubleshoot an ECS task that keeps stopping?

Check ECS events, stopped-task reason, exit code, CloudWatch logs, ECR image, roles, CPU, memory, startup command, ports, secrets, networking, and health checks.

## 18. Explain the difference between an ECS task role and execution role.

The execution role is used by ECS to pull images and publish logs. The task role is used by the application inside the container.

## 19. How do you troubleshoot a Linux application service?

Check `systemctl`, `journalctl`, configuration, permissions, dependencies, ports, CPU, memory, disk, SELinux, firewall, DNS, and routes.

## 20. How do you troubleshoot a Windows service?

Check service status, Event Logs, permissions, dependencies, ports, certificates, Windows Firewall, disk, and recent patches.

## 21. When would you use RDS PostgreSQL instead of DynamoDB?

Use PostgreSQL for relational data, SQL, joins, and transactions. Use DynamoDB for predictable low-latency key-value or document access at scale.

## 22. How would you troubleshoot an RDS PostgreSQL connection problem?

Check endpoint, port, credentials, database name, SSL, security groups, routes, DNS, database status, connection limits, and database permissions.

## 23. What does SonarQube do in a deployment pipeline?

It checks code quality and security and can block the pipeline when the quality gate fails.

## 24. What is JFrog used for?

JFrog Artifactory stores and promotes versioned application artifacts and packages.

## 25. How do Lambda and Step Functions work together?

Lambda performs individual tasks. Step Functions coordinates multiple tasks with retries, conditions, waiting, and error handling.

## 26. How do you approach disaster recovery?

Define RTO and RPO, identify dependencies, configure backups and replication, document failover and restore steps, test regularly, and document failback.

## 27. What should a disaster recovery runbook include?

Scope, owners, contacts, architecture, RTO/RPO, prerequisites, backups, recovery order, restore steps, validation, communication, escalation, and failback.

## 28. How do you handle production incidents?

Assess impact, stabilize the service, review alerts and recent changes, communicate status, preserve evidence, perform root-cause analysis, and create corrective actions.

## 29. What is your DevSecOps approach?

Integrate security throughout the delivery lifecycle using reviews, scans, least privilege, encryption, logging, artifact controls, approvals, and tracked remediation.

## 30. How would you address limited ArcGIS experience?

My strongest experience is AWS infrastructure, Terraform, automation, CI/CD, Linux, Windows, networking, security, and operations. These skills are directly applicable to ArcGIS environments, and I can quickly learn the product-specific architecture and support processes.

[⬆ Back to top](#top)

---

# Behavioral Interview Questions

## 31. Tell me about a time you automated a manual process.

**Situation:** Engineers manually connected to servers and performed repetitive operational tasks.

**Task:** Make the process consistent, secure, and auditable.

**Action:** I developed an SSM Automation workflow with validated parameters, IAM controls, logging, error handling, health checks, and notifications.

**Result:** The process became faster, safer, and less prone to human error.

## 32. Describe a difficult infrastructure problem you solved.

**Situation:** A Terraform deployment failed because the automation role lacked required permissions.

**Task:** Restore deployment without granting broad administrator access.

**Action:** I reviewed pipeline errors and CloudTrail, identified missing actions, updated the IAM policy with limited permissions, and reran validation and plan.

**Result:** The deployment succeeded while preserving least privilege.

## 33. Tell me about a production deployment you supported.

**Situation:** A release required coordinated infrastructure and application changes.

**Task:** Reduce production risk and improve consistency.

**Action:** I implemented validation, testing, scanning, artifact promotion, approvals, health checks, monitoring, and rollback steps.

**Result:** Releases became repeatable, auditable, and less dependent on manual work.

## 34. How do you work with development and infrastructure teams?

I gather application, security, availability, and deployment requirements, translate them into infrastructure and pipeline designs, document decisions, and collaborate during testing, releases, and incident response.

## 35. Why are you a strong fit for this position?

My experience aligns with the role’s main requirements: AWS, Terraform, Systems Manager, CI/CD, Linux, Windows, IAM, KMS, networking, monitoring, containers, databases, scripting, and technical documentation.

[⬆ Back to top](#top)

---

# Topics to Study Before the Interview

1. SSM Automation document structure and actions
2. Run Command, Patch Manager, State Manager, and Maintenance Windows
3. CodePipeline stages and CodeBuild `buildspec.yml`
4. Terraform Cloud Workspaces and reusable modules
5. Terraform state, drift, imports, and recovery
6. EC2, ALB, EFS, Route 53, IAM, and KMS
7. VPC routing, NAT Gateway, endpoints, security groups, and NACLs
8. CloudWatch, CloudTrail, alarms, and remediation
9. ECS task definitions, task roles, execution roles, and ECR
10. Red Hat and Windows Server troubleshooting
11. RDS PostgreSQL and DynamoDB
12. Lambda and Step Functions
13. SonarQube and JFrog
14. DevSecOps controls
15. Disaster recovery runbooks
16. ArcGIS Enterprise architecture

[⬆ Back to top](#top)

---

# Strong Interview Introduction

## For This Role (GIS / Enterprise Application Focus)

I am an AWS Cloud and DevOps Engineer with experience designing, automating, securing, and supporting cloud infrastructure. My background includes Terraform, AWS Systems Manager, CI/CD pipelines, EC2, networking, IAM, KMS, S3, RDS, ECS, ECR, CloudWatch, CloudTrail, Linux, Windows Server, and automation using Python, Bash, PowerShell, and YAML.

I focus on reusable infrastructure, secure deployment processes, operational automation, monitoring, and clear technical documentation. My experience aligns strongly with the cloud and DevOps responsibilities of this role, and I am prepared to apply those skills to the organization’s GIS and enterprise application environment.

## General-Purpose Pitch — Senior Cloud & DevOps Engineer

For roles not specifically GIS-focused, or as a broader opening pitch grounded directly in the resume's actual metrics and certifications:

> "I'm a Senior Cloud Infrastructure Engineer with 10+ years designing, automating, and securing large-scale environments across AWS, Azure, and GCP. My core strength is Infrastructure as Code and Kubernetes — I've built reusable Terraform modules standardizing deployments across dev through production, and run multi-tenant EKS clusters serving compute-intensive and AI/ML workloads. On the DevOps side, I've modernized CI/CD pipelines — migrating legacy Jenkins to GitHub Actions and Harness — and embedded security directly into the pipeline: SAST, IaC scanning, and policy-as-code gates with OPA and Sentinel, which is the DevSecOps half of how I work, not an afterthought. That combination has driven real numbers: 99.99% platform availability, 40% faster deployments, a 35% cut in incident detection and recovery time, and 20-25% in sustained infrastructure cost savings through FinOps practices. I'm AWS Solutions Architect Professional and Security Specialty certified, Terraform Associate, and a Certified Kubernetes Administrator — and I bring that same rigor to regulated environments, having supported HIPAA and SOC 2 compliant platforms in financial services and healthcare."

~135 words, roughly 45-50 seconds spoken — trim the FinOps or compliance sentence for a tighter 30-second version on a phone screen.

[⬆ Back to top](#top)
