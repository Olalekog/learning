# AWS Landing Zone – Features, Characteristics, and Design

## What is an AWS Landing Zone?

An AWS Landing Zone is a secure, scalable, and well-architected multi-account AWS environment that provides a foundation for deploying cloud workloads.

It includes baseline configurations for:

* Account structure
* Security
* Networking
* Identity and access management
* Logging
* Monitoring
* Governance
* Compliance
* Cost management
* Automation

A landing zone helps organizations start using AWS in a controlled, standardized, and enterprise-ready way.

---

# Why Landing Zone is Important

A landing zone provides a foundation for cloud adoption. Instead of creating AWS accounts manually without standards, a landing zone ensures every account follows approved security, networking, logging, and governance rules.

## Main Benefits

* Standardized AWS account setup
* Improved security and compliance
* Centralized logging and monitoring
* Controlled access management
* Faster workload onboarding
* Reduced manual configuration errors
* Better cost visibility
* Stronger governance across the AWS environment

---

# Key Features of AWS Landing Zone

## 1. Multi-Account Architecture

A landing zone is built using multiple AWS accounts.

### Common Accounts

* Management account
* Security account
* Log archive account
* Network account
* Shared services account
* Dev account
* Test account
* Production account
* Sandbox account

### Benefits

* Strong isolation
* Reduced blast radius
* Better workload separation
* Easier cost tracking
* Improved security boundaries

---

## 2. AWS Organizations Integration

AWS Organizations is used to centrally manage multiple AWS accounts.

### Features

* Create and manage AWS accounts
* Group accounts into Organizational Units
* Apply Service Control Policies
* Consolidate billing
* Centralized governance

---

## 3. Organizational Units

Organizational Units, also called OUs, are used to group accounts by purpose.

### Example OU Structure

```text
AWS Organization
│
├── Security OU
├── Infrastructure OU
├── Production OU
├── Non-Production OU
├── Sandbox OU
└── Suspended OU
```

### Benefits

* Easier account organization
* Better policy management
* Clear separation of environments
* Supports enterprise governance

---

## 4. Identity and Access Management

A landing zone includes centralized identity access.

### Common Services

* IAM Identity Center
* AWS IAM
* Role-based access control
* Federation with corporate identity provider
* Multi-factor authentication

### Benefits

* Centralized user access
* Least privilege permissions
* Easier onboarding and offboarding
* Stronger access control
* Better audit visibility

---

## 5. Security Baseline

A landing zone applies a security baseline across all accounts.

### Common Security Controls

* CloudTrail enabled
* AWS Config enabled
* GuardDuty enabled
* Security Hub enabled
* IAM Access Analyzer enabled
* S3 Block Public Access enabled
* Encryption standards applied
* MFA required
* Root account usage restricted

### Benefits

* Consistent security posture
* Better threat detection
* Easier compliance monitoring
* Reduced misconfiguration risk

---

## 6. Centralized Logging

A landing zone normally includes a dedicated log archive account.

### Logs Collected

* AWS CloudTrail logs
* AWS Config logs
* VPC Flow Logs
* ELB access logs
* Route 53 Resolver logs
* Security Hub findings
* GuardDuty findings

### Benefits

* Central log storage
* Tamper-resistant audit trail
* Easier investigation
* Compliance evidence
* Better operational visibility

---

## 7. Network Foundation

A landing zone defines the network architecture for workloads.

### Common Network Components

* VPCs
* Subnets
* Route tables
* NAT Gateways
* Internet Gateways
* Transit Gateway
* Direct Connect
* Site-to-Site VPN
* Route 53 Resolver
* AWS Network Firewall
* VPC Endpoints

### Benefits

* Standardized network design
* Secure connectivity
* Hybrid cloud integration
* Centralized traffic inspection
* Better segmentation between environments

---

## 8. Governance Guardrails

Guardrails are rules that help enforce security, compliance, and operational standards.

### Types of Guardrails

* Preventive guardrails
* Detective guardrails

### Preventive Guardrails

Preventive guardrails stop users from performing risky actions.

Examples:

* Deny disabling CloudTrail
* Deny deleting AWS Config
* Deny public S3 buckets
* Deny use of unapproved AWS Regions
* Deny changes to security accounts

### Detective Guardrails

Detective guardrails detect policy violations after they happen.

Examples:

* Detect unencrypted S3 buckets
* Detect public security groups
* Detect unused IAM users
* Detect untagged resources
* Detect non-compliant resources

---

## 9. Account Factory

Account Factory is used to provision new AWS accounts using a standard baseline.

### Benefits

* Faster account creation
* Standard security configuration
* Consistent network setup
* Reduced manual errors
* Automatic guardrail application

### Example

When a new application team needs an account, Account Factory can create the account with:

* Required CloudTrail logging
* AWS Config enabled
* Guardrails applied
* IAM Identity Center access
* Standard network configuration
* Required tags

---

## 10. Cost Management

A landing zone includes cost visibility and control.

### Common Cost Controls

* Consolidated billing
* AWS Budgets
* Cost Explorer
* Cost and Usage Reports
* Cost allocation tags
* Tag policies
* Chargeback and showback reports

### Benefits

* Better financial governance
* Account-level cost tracking
* Budget alerts
* Improved forecasting
* Easier chargeback to teams

---

# Characteristics of a Good Landing Zone

| Characteristic | Description                                                         |
| -------------- | ------------------------------------------------------------------- |
| Secure         | Includes security baseline, logging, encryption, and access control |
| Scalable       | Supports many accounts, teams, workloads, and environments          |
| Automated      | Uses automation for account creation and baseline deployment        |
| Governed       | Uses policies, guardrails, and compliance monitoring                |
| Standardized   | Applies consistent configuration across accounts                    |
| Auditable      | Centralizes logs and security findings                              |
| Flexible       | Supports different workload types and business units                |
| Resilient      | Supports high availability and disaster recovery patterns           |
| Cost-Aware     | Provides cost visibility and budget controls                        |
| Compliant      | Supports regulatory and internal policy requirements                |

---

# Landing Zone Design Components

## 1. Account Design

A landing zone should include dedicated accounts for different responsibilities.

### Example Account Structure

```text
AWS Organization
│
├── Management Account
│
├── Security OU
│   ├── Security Tooling Account
│   └── Log Archive Account
│
├── Infrastructure OU
│   ├── Network Account
│   └── Shared Services Account
│
├── Production OU
│   ├── App1 Prod Account
│   └── App2 Prod Account
│
├── Non-Production OU
│   ├── App1 Dev Account
│   ├── App1 Test Account
│   └── App2 Dev Account
│
└── Sandbox OU
    └── Developer Sandbox Account
```

---

## 2. Network Design

The network design should support secure connectivity between AWS accounts, on-premises data centers, and the internet.

### Common Network Patterns

* Centralized network account
* Hub-and-spoke VPC design
* Transit Gateway for routing
* Shared services VPC
* Inspection VPC
* Private subnets for applications
* Public subnets for load balancers
* VPC endpoints for private AWS service access

### Example

```text
On-Premises Data Center
        |
 Direct Connect / VPN
        |
 Transit Gateway
        |
 --------------------------------
 |              |               |
Prod VPC     Dev VPC      Shared Services VPC
```

---

## 3. Security Design

Security should be built into the landing zone from the beginning.

### Security Design Areas

* Identity and access control
* Logging and monitoring
* Encryption
* Network segmentation
* Threat detection
* Vulnerability management
* Compliance monitoring
* Incident response

### Common Services

* IAM Identity Center
* AWS CloudTrail
* AWS Config
* Security Hub
* GuardDuty
* Inspector
* KMS
* AWS WAF
* AWS Shield
* Network Firewall

---

## 4. Logging and Monitoring Design

Logging should be centralized and protected.

### Design Principles

* Send logs to a log archive account
* Enable CloudTrail for all accounts and Regions
* Enable AWS Config in all accounts
* Store logs in encrypted S3 buckets
* Restrict access to log archive buckets
* Use retention policies
* Monitor security findings centrally

---

## 5. Governance Design

Governance ensures that accounts follow organizational standards.

### Governance Tools

* Service Control Policies
* Tag policies
* AWS Config rules
* Control Tower guardrails
* IAM permission boundaries
* CloudFormation StackSets
* Terraform modules
* CI/CD approval gates

### Example Governance Rules

* Only approved AWS Regions can be used
* S3 buckets must not be public
* CloudTrail must not be disabled
* EBS volumes must be encrypted
* Required tags must be applied
* Root user must not be used

---

## 6. Automation Design

Automation is important for consistency and speed.

### Common Automation Tools

* AWS Control Tower
* Account Factory
* CloudFormation StackSets
* Terraform
* GitHub Actions
* Jenkins
* AWS CodePipeline
* AWS Lambda
* AWS Service Catalog

### Automation Use Cases

* Account creation
* Baseline security setup
* Network deployment
* IAM role creation
* Guardrail enforcement
* Tagging validation
* Compliance reporting

---

# AWS Landing Zone Implementation Options

## 1. AWS Control Tower

AWS Control Tower is the AWS-managed service for setting up and governing a multi-account landing zone.

### Features

* Landing zone setup
* Account Factory
* Guardrails
* Centralized logging
* AWS Organizations integration
* IAM Identity Center integration
* Account governance

### Best For

* Organizations that want a managed AWS landing zone
* Fast multi-account setup
* Standardized governance

---

## 2. Custom Landing Zone

A custom landing zone is built using tools such as Terraform, CloudFormation, or AWS CDK.

### Features

* Flexible design
* Custom account structure
* Custom networking
* Custom security controls
* Custom automation pipelines

### Best For

* Large enterprises with specific governance requirements
* Organizations with existing automation frameworks
* Highly customized AWS environments

---

## 3. AWS Landing Zone Accelerator

AWS Landing Zone Accelerator helps deploy a secure, compliant, and scalable AWS environment using configuration-driven automation.

### Features

* Security baseline
* Network baseline
* Logging
* Compliance controls
* Multi-account architecture
* Global configuration management

### Best For

* Regulated industries
* Enterprises requiring stronger compliance alignment
* Organizations needing repeatable landing zone deployment

---

# Landing Zone Design Best Practices

* Use a multi-account strategy.
* Do not run workloads in the management account.
* Use separate accounts for security and logging.
* Use separate accounts for production and non-production.
* Use Organizational Units to group accounts.
* Apply Service Control Policies as guardrails.
* Enable CloudTrail across all accounts and Regions.
* Enable AWS Config for compliance tracking.
* Use centralized logging in a log archive account.
* Use IAM Identity Center for centralized access.
* Use MFA for privileged access.
* Use least privilege permissions.
* Use encryption by default.
* Use approved Regions only.
* Use standard naming and tagging policies.
* Use automation for account provisioning.
* Use centralized networking where appropriate.
* Use monitoring and alerting for security events.
* Review guardrails regularly.
* Design for scalability from the beginning.

---

# Landing Zone vs Multi-Account Strategy

| Area    | Multi-Account Strategy                           | Landing Zone                                                                                 |
| ------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| Purpose | Defines how accounts are separated and organized | Provides the full operating foundation                                                       |
| Scope   | Focuses mainly on account separation             | Includes accounts, identity, network, security, logging, governance, and automation          |
| Tools   | AWS Organizations, OUs, SCPs                     | AWS Control Tower, Account Factory, Security Hub, CloudTrail, Config, networking, automation |
| Outcome | Account isolation and governance                 | Enterprise-ready AWS environment                                                             |
| Example | Dev, Test, Prod, Security accounts               | Secure baseline with logging, guardrails, IAM, networking, and monitoring                    |

---

# Sample Landing Zone Architecture

```text
                        Users / Admins
                              |
                              v
                    IAM Identity Center
                              |
                              v
                    AWS Organizations
                              |
        ------------------------------------------------
        |                    |                         |
   Security OU        Infrastructure OU          Workload OUs
        |                    |                         |
  ---------------      -----------------       -----------------
  |             |      |               |       |       |       |
Security     Log    Network       Shared     Dev     Test    Prod
Tooling    Archive  Account       Services   Acct    Acct    Acct
Account    Account  Account       Account

        Centralized Logging | Guardrails | Monitoring | Billing
```

---

# Interview Questions and Sample Answers

## Q1: What is an AWS Landing Zone?

An AWS Landing Zone is a secure and scalable multi-account AWS environment that provides the foundation for deploying workloads. It includes account structure, networking, identity, logging, monitoring, security, governance, and compliance controls.

---

## Q2: What is the difference between AWS Control Tower and a Landing Zone?

A landing zone is the overall cloud foundation design. AWS Control Tower is a managed AWS service that helps create and govern that landing zone using AWS Organizations, Account Factory, guardrails, centralized logging, and IAM Identity Center.

---

## Q3: What are the core components of a landing zone?

The core components are multi-account structure, AWS Organizations, IAM Identity Center, centralized logging, security tooling, network foundation, Service Control Policies, monitoring, governance, and account provisioning automation.

---

## Q4: Why is centralized logging important in a landing zone?

Centralized logging stores logs from all accounts in a dedicated log archive account. This protects logs from deletion or tampering and supports auditing, compliance, troubleshooting, and incident response.

---

## Q5: Why should workloads not run in the management account?

Workloads should not run in the management account because it is used to manage AWS Organizations and billing. Keeping it free of workloads reduces security risk, limits blast radius, and protects critical administrative functions.

---

## Q6: What are landing zone guardrails?

Guardrails are rules used to enforce security, compliance, and operational standards. Preventive guardrails block risky actions, while detective guardrails identify policy violations.

---

## Q7: How would you design a landing zone for an enterprise?

I would start with a multi-account architecture using AWS Organizations. I would create separate accounts for security, log archive, networking, shared services, production, non-production, and sandbox workloads. I would enable centralized logging, IAM Identity Center, CloudTrail, AWS Config, GuardDuty, Security Hub, Service Control Policies, and standardized networking through Transit Gateway or shared network patterns. I would also automate account creation using Control Tower Account Factory or Terraform.

---

# Solution Architect Tips

For AWS Solutions Architect interviews and exams, remember:

* A landing zone is the cloud foundation.
* AWS Control Tower helps automate and govern a landing zone.
* Multi-account design is a core landing zone principle.
* Use a log archive account for centralized logs.
* Use a security account for security tooling.
* Use a network account for shared network services.
* Use SCPs for preventive guardrails.
* Use AWS Config and Security Hub for detective controls.
* Use IAM Identity Center for centralized access.
* Automate account creation and baseline configuration.
* Design the landing zone before deploying production workloads.

---

# Key Takeaways

* A landing zone provides a secure foundation for AWS workloads.
* It includes accounts, networking, security, identity, logging, governance, and automation.
* AWS Control Tower is commonly used to create and manage landing zones.
* Landing zones support enterprise security, compliance, and scalability.
* A good landing zone reduces risk, improves consistency, and speeds up cloud adoption.
