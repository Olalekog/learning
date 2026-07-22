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

---

# AWS Services and Tools Glossary

Quick one-line reference for every service, tool, and language mentioned in this guide.

## AWS Services

| Service | Description |
|---|---|
| **Amazon EC2** | Virtual servers ("instances") for running applications in the cloud. |
| **AWS Systems Manager (SSM)** | Centralized service for managing, patching, and automating EC2 and hybrid servers without SSH/RDP. |
| **— Session Manager** | SSM feature giving shell/PowerShell access to instances with no open inbound ports or SSH keys. |
| **— Run Command** | SSM feature that executes ad-hoc commands/scripts across one or more managed instances. |
| **— Automation (Runbooks)** | SSM feature that runs multi-step YAML/JSON operational workflows (e.g., patch, validate, rollback). |
| **— Patch Manager** | SSM feature that automates OS and application patching. |
| **— Maintenance Windows** | SSM feature defining scheduled time windows for disruptive operations. |
| **— State Manager** | SSM feature that continuously enforces a defined configuration state on instances. |
| **— Parameter Store** | SSM feature storing configuration values and encrypted secrets (SecureString). |
| **— Inventory** | SSM feature that collects installed software, OS, and configuration metadata. |
| **Amazon EFS** | Managed, scalable NFS file system mountable by multiple Linux EC2 instances or ECS tasks. |
| **Application Load Balancer (ALB)** | Layer-7 load balancer that routes HTTP/HTTPS traffic using host/path rules and health checks. |
| **Amazon Route 53** | Managed DNS service supporting hosted zones, health checks, and traffic-routing policies. |
| **AWS IAM** | Identity and Access Management — controls who/what can authenticate and what they're authorized to do. |
| **AWS KMS** | Key Management Service — creates and manages encryption keys used by S3, EBS, RDS, EFS, and more. |
| **Amazon Machine Image (AMI)** | A template (OS, patches, agents, software) used to launch EC2 instances. |
| **Security Groups** | Stateful, instance-level virtual firewalls controlling inbound/outbound traffic. |
| **Amazon VPC** | Virtual Private Cloud — an isolated, software-defined network for AWS resources. |
| **Internet Gateway** | VPC component that lets public-subnet resources reach the internet. |
| **NAT Gateway** | Lets private-subnet resources initiate outbound internet traffic without being publicly reachable. |
| **Network ACLs** | Stateless, subnet-level firewall rules (complement to security groups). |
| **VPC Endpoints** | Private, non-internet connectivity from a VPC to AWS services like S3, ECR, or SSM. |
| **VPC Flow Logs** | Captures network traffic metadata for a VPC, used for troubleshooting and security auditing. |
| **Amazon CloudWatch** | Monitoring service for metrics, logs, alarms, dashboards, and Logs Insights queries. |
| **— CloudWatch Agent** | Optional agent collecting OS-level metrics (memory, disk) and application/Windows Event Logs. |
| **AWS CloudTrail** | Records AWS API activity — who made a change, when, from where, and with which role. |
| **AWS Secrets Manager** | Securely stores, encrypts, versions, and automatically rotates sensitive credentials. |
| **Amazon ECR** | Elastic Container Registry — managed Docker image repository with scanning. |
| **Amazon ECS** | Elastic Container Service — runs containers via clusters, task definitions, and services on EC2 or Fargate. |
| **AWS Lambda** | Serverless compute that runs event-triggered code without managing servers. |
| **AWS Step Functions** | Orchestrates multi-step workflows (sequential, parallel, retries, branching) across Lambda and other services. |
| **Amazon S3** | Simple Storage Service — scalable, durable object storage with versioning and lifecycle policies. |
| **Amazon RDS (PostgreSQL)** | Managed relational database service handling backups, patching, and Multi-AZ failover. |
| **Amazon DynamoDB** | Managed NoSQL key-value/document database with single-digit-millisecond latency at scale. |
| **AWS CodePipeline** | Orchestrates CI/CD release stages (source, build, test, deploy, approval). |
| **AWS CodeBuild** | Managed build service that compiles, tests, and packages code in a temporary environment. |
| **AWS Security Hub** | Aggregates and prioritizes security findings across AWS accounts and services. |
| **Amazon GuardDuty** | Continuous threat-detection service that monitors for malicious or unauthorized activity. |
| **Amazon Inspector** | Automated vulnerability scanning for EC2 instances and container images. |
| **AWS Config** | Tracks AWS resource configuration changes and evaluates them against compliance rules. |
| **AWS AppStream 2.0** | Streams desktop applications to end users through a web browser. |
| **Amazon SNS** | Pub/sub messaging service used for notifications and alert routing. |
| **Amazon SQS** | Managed message queuing service for decoupling application components. |
| **Amazon EventBridge** | Event bus that routes AWS/application events to targets like Lambda or SNS for automated remediation. |

## CI/CD and Source Control Tools

| Tool | Description |
|---|---|
| **Terraform** | Infrastructure-as-Code tool for declaratively provisioning and managing cloud resources. |
| **Azure DevOps** | Microsoft platform for repos, YAML pipelines, variable groups, and release approvals. |
| **GitHub** | Source-control hosting with pull requests, branch protection, and GitHub Actions pipelines. |

## Automation Languages and Operating Systems

| Item | Description |
|---|---|
| **Python** | General-purpose scripting language, commonly paired with Boto3 for AWS automation and Lambda functions. |
| **YAML** | Human-readable data-serialization format used for pipelines, SSM documents, and configuration. |
| **Bash** | Unix/Linux shell scripting language for configuration, deployment, and log collection. |
| **PowerShell** | Windows scripting language/shell used for Windows Server administration and automation. |
| **Red Hat Linux** | Enterprise Linux distribution administered via systemd, SELinux, firewalld, and package managers. |
| **Windows Server 2022** | Microsoft server operating system managed via Services, Event Viewer, IIS, and PowerShell. |

## Code Quality and Security Scanning Tools

| Tool | Description |
|---|---|
| **SonarQube** | Static code analysis tool that flags bugs, vulnerabilities, code smells, and enforces quality gates. |
| **JFrog Artifactory** | Universal artifact repository that stores and promotes versioned build packages (Docker, Java, npm, etc.). |
| **JFrog Xray** | Security and license-compliance scanning for artifacts stored in Artifactory. |
| **Checkov** | Static analysis tool that scans Infrastructure-as-Code (e.g., Terraform) for misconfigurations. |
| **Trivy** | Vulnerability scanner for container images, filesystems, and IaC. |

## GIS Platform Tools

| Tool | Description |
|---|---|
| **ArcGIS Enterprise** | Esri's GIS platform for mapping, spatial analysis, and geospatial application hosting. |
| **Portal for ArcGIS** | Web front end for sharing ArcGIS maps, apps, and content among users and groups. |
| **ArcGIS Server** | Hosts map, feature, geoprocessing, and image services for GIS applications. |
| **ArcGIS Data Store** | Backend data storage supporting ArcGIS Server's hosted services. |
| **ArcGIS Pro** | Esri's desktop GIS application for mapping, spatial analysis, and publishing. |
| **FME Core / FME Engine** | Tooling for geospatial data transformation, format conversion, and integration automation. |

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

---

# Strong Interview Introduction

I am an AWS Cloud and DevOps Engineer with experience designing, automating, securing, and supporting cloud infrastructure. My background includes Terraform, AWS Systems Manager, CI/CD pipelines, EC2, networking, IAM, KMS, S3, RDS, ECS, ECR, CloudWatch, CloudTrail, Linux, Windows Server, and automation using Python, Bash, PowerShell, and YAML.

I focus on reusable infrastructure, secure deployment processes, operational automation, monitoring, and clear technical documentation. My experience aligns strongly with the cloud and DevOps responsibilities of this role, and I am prepared to apply those skills to the organization’s GIS and enterprise application environment.
