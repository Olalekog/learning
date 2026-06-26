# AWS Multi-Account Strategy – Features and Characteristics

## What is an AWS Multi-Account Strategy?

An AWS multi-account strategy is an architecture approach where an organization uses multiple AWS accounts to separate workloads, environments, teams, security boundaries, billing, and governance controls.

Instead of placing all workloads in one AWS account, organizations create different accounts for different purposes such as development, testing, production, security, networking, logging, and shared services.

AWS multi-account strategy is commonly managed using:

* AWS Organizations
* AWS Control Tower
* Organizational Units
* Service Control Policies
* IAM Identity Center
* AWS CloudTrail
* AWS Config
* AWS Security Hub
* AWS Billing and Cost Management

---

# Why Use a Multi-Account Strategy?

A multi-account strategy helps enterprises improve:

* Security
* Governance
* Cost management
* Operational isolation
* Compliance
* Scalability
* Environment separation
* Disaster recovery readiness

It is a best practice for medium and large AWS environments.

---

# Key Features

## 1. Account Isolation

Each AWS account acts as a strong isolation boundary.

### Benefits

* Separates workloads by environment or business unit
* Reduces blast radius during incidents
* Prevents one application from affecting another
* Improves security and access control

### Example

```text
Development Account
Testing Account
Production Account
Security Account
Logging Account
Network Account
```

If a developer makes a mistake in the development account, it does not directly affect the production account.

---

## 2. Environment Separation

Different environments can be placed in separate AWS accounts.

### Common Environment Accounts

* Dev account
* Test account
* QA account
* Staging account
* Production account

### Benefits

* Clear separation between non-production and production
* Better change control
* Easier access management
* Safer testing and experimentation

---

## 3. Security Boundary

AWS accounts provide security boundaries for workloads and users.

### Security Benefits

* Separate IAM roles and permissions
* Separate resource access
* Separate encryption keys
* Separate logs and monitoring
* Separate network boundaries

### Example

Production users may only have read-only access, while DevOps engineers may have deployment access through controlled pipelines.

---

## 4. Reduced Blast Radius

A multi-account design limits the impact of mistakes, failures, or security incidents.

### Example

If one account is compromised, the attacker does not automatically gain access to all AWS resources across the organization.

This improves:

* Incident containment
* Security response
* Risk management
* Compliance posture

---

## 5. Centralized Governance with AWS Organizations

AWS Organizations allows companies to centrally manage multiple AWS accounts.

### Key Capabilities

* Create and manage AWS accounts
* Group accounts into Organizational Units
* Apply Service Control Policies
* Consolidate billing
* Centrally manage governance

---

## 6. Organizational Units

Organizational Units, also called OUs, are logical groups of AWS accounts inside AWS Organizations.

### Example OU Structure

```text
Root
├── Security OU
├── Infrastructure OU
├── Production OU
├── Non-Production OU
├── Sandbox OU
└── Suspended OU
```

### Benefits

* Organizes accounts by purpose
* Makes policy management easier
* Supports consistent governance
* Allows different controls for different account types

---

## 7. Service Control Policies

Service Control Policies, also called SCPs, are guardrails used to control the maximum permissions available in AWS accounts.

SCPs do not grant permissions. They only limit what users and roles can do.

### Example SCP Use Cases

* Prevent disabling CloudTrail
* Prevent deleting AWS Config
* Block public S3 bucket creation
* Restrict access to specific AWS Regions
* Prevent removal of security tools
* Require encryption for certain resources

---

## 8. Centralized Logging

A multi-account strategy usually includes a dedicated logging account.

### Centralized Logs May Include

* AWS CloudTrail logs
* VPC Flow Logs
* AWS Config logs
* Elastic Load Balancer logs
* GuardDuty findings
* Security Hub findings

### Benefits

* Protects logs from deletion by workload teams
* Supports audit requirements
* Improves investigation and incident response
* Creates a single location for security visibility

---

## 9. Centralized Security Account

A dedicated security account is used to manage security services and monitoring.

### Common Security Services

* Amazon GuardDuty
* AWS Security Hub
* Amazon Inspector
* AWS Config
* IAM Access Analyzer
* AWS Detective
* AWS Firewall Manager

### Benefits

* Centralized security visibility
* Better incident response
* Stronger compliance monitoring
* Separation of security operations from application teams

---

## 10. Shared Services Account

A shared services account hosts common services used by multiple accounts.

### Common Shared Services

* CI/CD tools
* Directory services
* DNS services
* Patch management tools
* Monitoring tools
* Artifact repositories
* License servers
* Golden AMI pipelines

### Benefits

* Avoids duplication
* Improves standardization
* Reduces operational overhead
* Provides reusable enterprise services

---

## 11. Network Account

A network account is used to centrally manage networking services.

### Common Network Components

* AWS Transit Gateway
* AWS Direct Connect
* Site-to-Site VPN
* Centralized inspection VPC
* Network Firewall
* Route 53 Resolver
* Shared VPC patterns

### Benefits

* Centralized network control
* Consistent routing
* Easier hybrid cloud connectivity
* Better inspection and monitoring
* Stronger network security

---

## 12. Consolidated Billing

AWS Organizations supports consolidated billing across all AWS accounts.

### Benefits

* Single billing view
* Easier cost tracking
* Volume discounts
* Reserved Instance and Savings Plans sharing
* Centralized budget monitoring

---

## 13. Cost Allocation and Chargeback

A multi-account strategy improves cost visibility.

### Common Cost Management Methods

* Account-level cost tracking
* Tags
* Cost allocation tags
* AWS Cost Explorer
* AWS Budgets
* Cost and Usage Reports
* Chargeback and showback reporting

### Example

```text
Production Account = Business-critical application cost
Development Account = Engineering cost
Security Account = Security operations cost
Network Account = Shared infrastructure cost
```

---

## 14. Compliance and Audit Support

Multi-account design helps meet compliance requirements by separating workloads and centralizing controls.

### Supports Compliance Needs Such As

* Audit logging
* Access control
* Data segregation
* Encryption enforcement
* Least privilege
* Change control
* Evidence collection

### Common Frameworks

* CIS Benchmarks
* NIST
* ISO 27001
* SOC 2
* PCI DSS
* HIPAA

---

## 15. Automated Account Provisioning

AWS Control Tower and Account Factory can automate account creation.

### Benefits

* Standardized account setup
* Preconfigured guardrails
* Baseline security controls
* Faster onboarding
* Reduced manual errors

### Example Baseline Controls

* CloudTrail enabled
* AWS Config enabled
* Guardrails applied
* Logging configured
* IAM Identity Center integrated

---

# Common AWS Account Types

## Management Account

The management account is the root account for AWS Organizations.

### Purpose

* Manages the AWS Organization
* Creates and manages member accounts
* Controls consolidated billing
* Applies organization-wide policies

### Best Practice

Do not run workloads in the management account.

---

## Security Account

Used for centralized security operations.

### Purpose

* Security monitoring
* Threat detection
* Incident response
* Security tooling administration

---

## Log Archive Account

Used to store logs from all AWS accounts.

### Purpose

* Centralized log storage
* Audit trail protection
* Long-term retention
* Compliance evidence

---

## Network Account

Used for shared networking.

### Purpose

* Transit Gateway
* VPN
* Direct Connect
* Network inspection
* DNS forwarding

---

## Shared Services Account

Used for common enterprise services.

### Purpose

* CI/CD tooling
* Directory services
* Monitoring
* Patch management
* Artifact storage

---

## Workload Accounts

Used to run applications and services.

### Examples

* App1 Dev
* App1 Test
* App1 Prod
* App2 Dev
* App2 Prod

---

## Sandbox Account

Used for learning, experimentation, and proof of concept work.

### Purpose

* Testing new AWS services
* Developer experimentation
* Training
* Temporary workloads

---

# Example Multi-Account Structure

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

# Characteristics Summary

| Characteristic         | Description                                                   |
| ---------------------- | ------------------------------------------------------------- |
| Isolation              | Each AWS account provides a strong boundary                   |
| Security               | Separates access, resources, logs, and permissions            |
| Governance             | Central policies can be applied using AWS Organizations       |
| Cost Visibility        | Costs can be tracked by account, workload, or environment     |
| Scalability            | Supports growth across teams, workloads, and business units   |
| Compliance             | Helps support audit, logging, and access control requirements |
| Blast Radius Reduction | Limits the impact of failures or security incidents           |
| Centralized Logging    | Logs are stored in a dedicated log archive account            |
| Shared Services        | Common services can be reused across accounts                 |
| Environment Separation | Dev, test, staging, and production can be separated           |
| Automation             | Account creation can be standardized using Control Tower      |

---

# Benefits of AWS Multi-Account Strategy

## Security Benefits

* Limits access between workloads
* Reduces blast radius
* Supports least privilege
* Enables stronger audit control
* Protects security logs from workload teams

## Operational Benefits

* Separates production from non-production
* Improves troubleshooting
* Supports team ownership
* Reduces resource conflicts
* Makes account-level monitoring easier

## Financial Benefits

* Centralized billing
* Cost visibility by account
* Easier chargeback and showback
* Better budget control
* Supports cost allocation tagging

## Compliance Benefits

* Clear workload separation
* Centralized logging
* Easier audit reporting
* Stronger policy enforcement
* Supports regulatory requirements

---

# Best Practices

* Do not run workloads in the AWS Organizations management account.
* Use separate accounts for production and non-production.
* Use a dedicated log archive account.
* Use a dedicated security account.
* Use Service Control Policies as preventive guardrails.
* Use IAM Identity Center for centralized user access.
* Enable CloudTrail across all accounts and Regions.
* Enable AWS Config for compliance monitoring.
* Use Control Tower for standardized account provisioning.
* Apply tagging standards for cost management.
* Use least privilege access.
* Use automation for account creation and baseline configuration.
* Use centralized networking for hybrid cloud connectivity.
* Monitor all accounts with Security Hub and GuardDuty.

---

# Common Services Used

| Service                     | Purpose                             |
| --------------------------- | ----------------------------------- |
| AWS Organizations           | Central account management          |
| AWS Control Tower           | Landing zone and account governance |
| Account Factory             | Automated account provisioning      |
| Service Control Policies    | Preventive permission guardrails    |
| IAM Identity Center         | Centralized workforce access        |
| AWS CloudTrail              | API activity logging                |
| AWS Config                  | Resource compliance monitoring      |
| AWS Security Hub            | Security posture management         |
| Amazon GuardDuty            | Threat detection                    |
| AWS Cost Explorer           | Cost analysis                       |
| AWS Budgets                 | Budget alerts                       |
| AWS Transit Gateway         | Central network connectivity        |
| AWS Resource Access Manager | Resource sharing across accounts    |

---

# Interview Questions and Sample Answers

## Q1: What is an AWS multi-account strategy?

An AWS multi-account strategy is a cloud architecture approach where an organization uses multiple AWS accounts to separate workloads, environments, security controls, billing, and governance. It improves security, isolation, compliance, and operational control.

---

## Q2: Why should production and development workloads be in separate AWS accounts?

Production and development workloads should be separated to reduce risk and prevent non-production changes from affecting production systems. It also allows different access controls, budgets, monitoring rules, and security policies for each environment.

---

## Q3: What is the purpose of a log archive account?

A log archive account is used to centrally store logs from all AWS accounts. This protects logs from accidental deletion or tampering and supports auditing, compliance, and incident investigation.

---

## Q4: What is the difference between IAM policies and Service Control Policies?

IAM policies grant permissions to users, groups, and roles. Service Control Policies do not grant permissions. SCPs define the maximum permissions allowed in an AWS account or Organizational Unit.

---

## Q5: What is the purpose of AWS Control Tower?

AWS Control Tower helps set up and govern a secure multi-account AWS environment. It provides a landing zone, guardrails, account provisioning through Account Factory, centralized logging, and baseline security controls.

---

## Q6: What is a shared services account?

A shared services account hosts common services used by multiple accounts, such as CI/CD tools, DNS, directory services, monitoring platforms, patch management, and artifact repositories.

---

## Q7: How does a multi-account strategy reduce blast radius?

A multi-account strategy reduces blast radius by isolating workloads into separate accounts. If one account has a security issue, misconfiguration, or operational failure, the impact is limited to that account instead of affecting the entire AWS environment.

---

# Solution Architect Tips

For AWS Solutions Architect interviews and exams, remember:

* Use multiple accounts for isolation and governance.
* Use Organizational Units to group accounts by function.
* Use SCPs to apply guardrails.
* Use IAM Identity Center for centralized access.
* Use a log archive account for centralized logging.
* Use a security account for threat detection and compliance monitoring.
* Use a network account for shared networking.
* Use separate workload accounts for dev, test, staging, and production.
* Use AWS Control Tower to automate account provisioning.
* Do not place workloads in the management account.

---

# Key Takeaways

* A multi-account strategy improves security, governance, compliance, and cost control.
* AWS accounts provide strong isolation boundaries.
* AWS Organizations centrally manages accounts and billing.
* AWS Control Tower helps automate and govern account setup.
* SCPs provide preventive guardrails.
* Centralized logging and security accounts improve audit and incident response.
* Production and non-production workloads should be separated.
* Multi-account design is a best practice for enterprise AWS environments.
