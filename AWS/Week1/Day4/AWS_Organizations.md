# AWS Organizations – Features and Characteristics

## What is AWS Organizations?

AWS Organizations is an AWS service that helps you centrally manage and govern multiple AWS accounts.

It allows an organization to:

* Create AWS accounts
* Invite existing AWS accounts
* Group accounts into Organizational Units
* Apply policies across accounts
* Use consolidated billing
* Manage governance at scale
* Integrate with other AWS services

AWS Organizations is commonly used as the foundation for:

* Multi-account strategy
* AWS Landing Zone
* AWS Control Tower
* Governance and guardrails
* Centralized billing
* Security and compliance management

---

# Why AWS Organizations is Important

AWS Organizations helps enterprises manage cloud environments at scale. Instead of managing each AWS account separately, teams can manage accounts centrally using organizational structure, policies, and shared billing.

## Main Benefits

* Centralized account management
* Better security governance
* Improved cost visibility
* Easier compliance control
* Account isolation
* Reduced blast radius
* Standardized cloud operations
* Easier multi-account management

---

# Key Features of AWS Organizations

## 1. Centralized Account Management

AWS Organizations allows you to manage multiple AWS accounts from one place.

### Capabilities

* Create new AWS accounts
* Invite existing AWS accounts
* Remove accounts from the organization
* Move accounts between Organizational Units
* Apply policies to accounts or OUs
* View all accounts in one organization

### Benefit

This makes it easier to manage AWS environments across departments, teams, projects, and applications.

---

## 2. Management Account

The management account is the main account used to create and manage the AWS Organization.

### Responsibilities

* Create and manage the organization
* Create and invite member accounts
* Manage consolidated billing
* Apply organization-level policies
* Manage trusted access for AWS services

### Best Practice

Do not run application workloads in the management account.

The management account should be protected because it has high-level administrative control over the organization.

---

## 3. Member Accounts

Member accounts are AWS accounts that belong to the AWS Organization.

### Examples

* Production account
* Development account
* Test account
* Security account
* Logging account
* Network account
* Shared services account
* Sandbox account

### Benefits

* Workload isolation
* Separate billing visibility
* Separate IAM boundaries
* Reduced blast radius
* Easier ownership tracking

---

## 4. Organizational Units

Organizational Units, also called OUs, are logical groups of AWS accounts.

### Example OU Structure

```text
AWS Organization
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
│   └── App1 Test Account
│
└── Sandbox OU
    └── Developer Sandbox Account
```

### Benefits

* Groups accounts by function
* Simplifies policy management
* Allows different controls for different environments
* Supports enterprise governance

---

## 5. Service Control Policies

Service Control Policies, also called SCPs, are policies used to define the maximum permissions available in AWS accounts.

SCPs do not grant permissions. They only limit what users and roles can do.

### Common SCP Use Cases

* Deny disabling CloudTrail
* Deny deleting AWS Config
* Deny creating public S3 buckets
* Deny use of unapproved AWS Regions
* Deny deleting security services
* Restrict root user actions
* Require use of approved services

### Example

An SCP can deny users from launching resources outside approved AWS Regions.

---

## 6. Consolidated Billing

AWS Organizations provides consolidated billing for all accounts in the organization.

### Benefits

* One bill for multiple AWS accounts
* Central payment management
* Account-level cost visibility
* Easier budgeting
* Possible volume pricing benefits
* Easier chargeback and showback reporting

### Example

```text
Management Account Billing
│
├── Production Account Cost
├── Development Account Cost
├── Security Account Cost
├── Network Account Cost
└── Sandbox Account Cost
```

---

## 7. Policy-Based Governance

AWS Organizations supports organization policies that help centrally govern AWS accounts.

### Common Policy Types

* Service Control Policies
* Tag Policies
* Backup Policies
* AI Services Opt-Out Policies
* Resource Control Policies

### Benefits

* Centralized governance
* Consistent controls
* Better compliance
* Reduced manual enforcement
* Standardized account behavior

---

## 8. Integration with AWS Services

AWS Organizations integrates with many AWS services to support centralized governance and management.

### Common Integrations

* AWS Control Tower
* IAM Identity Center
* AWS CloudTrail
* AWS Config
* Amazon GuardDuty
* AWS Security Hub
* Amazon Inspector
* AWS Backup
* AWS Firewall Manager
* AWS Resource Access Manager
* AWS Service Catalog
* AWS Cost Explorer

### Benefits

* Centralized security monitoring
* Centralized logging
* Centralized backup governance
* Cross-account resource sharing
* Better compliance visibility

---

## 9. Delegated Administration

Delegated administration allows selected member accounts to manage specific AWS services for the organization.

### Example

A security tooling account can be delegated to manage:

* GuardDuty
* Security Hub
* AWS Config
* IAM Access Analyzer
* Amazon Inspector

### Benefits

* Reduces use of the management account
* Improves separation of duties
* Supports security operations
* Allows teams to manage specific services centrally

---

## 10. Account Isolation

Each AWS account provides an isolation boundary.

### Benefits

* Separates environments
* Limits blast radius
* Supports least privilege
* Improves security
* Prevents development issues from affecting production

### Example

A misconfiguration in a sandbox account should not impact the production account.

---

## 11. Support for Landing Zones

AWS Organizations is a core building block for AWS landing zones.

### Used For

* Multi-account structure
* Organizational Units
* Account governance
* SCP guardrails
* Consolidated billing
* AWS Control Tower setup

### Benefit

It provides the account foundation needed for secure, scalable AWS cloud adoption.

---

# AWS Organizations Feature Modes

AWS Organizations supports two main feature modes.

## 1. Consolidated Billing Mode

This mode provides shared billing functionality only.

### Includes

* Centralized billing
* Account cost visibility
* One payer account

### Limitation

It does not include advanced governance features such as SCPs and service integrations.

---

## 2. All Features Mode

All Features mode includes consolidated billing plus advanced governance capabilities.

### Includes

* Consolidated billing
* Service Control Policies
* AWS service integrations
* Organization policies
* Advanced account management

### Best Practice

Use All Features mode for enterprise governance and multi-account management.

---

# Characteristics Summary

| Characteristic   | Description                                                                             |
| ---------------- | --------------------------------------------------------------------------------------- |
| Centralized      | Manages multiple AWS accounts from one place                                            |
| Hierarchical     | Uses root, OUs, and accounts                                                            |
| Scalable         | Supports growth across teams, workloads, and environments                               |
| Governed         | Applies policies across accounts and OUs                                                |
| Cost-Aware       | Provides consolidated billing and account-level cost visibility                         |
| Secure           | Supports account isolation and preventive controls                                      |
| Integrated       | Works with services like Control Tower, CloudTrail, Config, GuardDuty, and Security Hub |
| Flexible         | Accounts can be moved between OUs                                                       |
| Auditable        | Supports centralized logging and compliance monitoring through integrations             |
| Enterprise-Ready | Supports landing zones, multi-account strategy, and cloud governance                    |

---

# Common AWS Organizations Structure

```text
AWS Organizations
│
├── Root
│
├── Security OU
│   ├── Security Tooling Account
│   └── Log Archive Account
│
├── Infrastructure OU
│   ├── Network Account
│   └── Shared Services Account
│
├── Workloads OU
│   ├── Production OU
│   │   ├── App1 Prod Account
│   │   └── App2 Prod Account
│   │
│   └── Non-Production OU
│       ├── App1 Dev Account
│       └── App1 Test Account
│
└── Sandbox OU
    └── Developer Sandbox Account
```

---

# Common AWS Organizations Services and Concepts

| Item                    | Purpose                                                     |
| ----------------------- | ----------------------------------------------------------- |
| Organization            | Collection of AWS accounts managed centrally                |
| Root                    | Top-level container in the organization                     |
| Organizational Unit     | Logical group of accounts                                   |
| Management Account      | Main account that manages the organization                  |
| Member Account          | AWS account inside the organization                         |
| SCP                     | Defines maximum allowed permissions                         |
| Consolidated Billing    | Combines bills for all accounts                             |
| Delegated Administrator | Member account allowed to manage organization-wide services |
| Tag Policy              | Helps standardize tags across accounts                      |
| Backup Policy           | Helps standardize backup plans across accounts              |

---

# Example Service Control Policy Use Cases

## Deny Unapproved Regions

```text
Purpose:
Prevent workloads from being deployed outside approved AWS Regions.

Example:
Allow only us-east-1 and us-east-2 for company workloads.
```

## Protect CloudTrail

```text
Purpose:
Prevent users from disabling or deleting CloudTrail.

Example:
Deny cloudtrail:StopLogging and cloudtrail:DeleteTrail.
```

## Protect Logging Account

```text
Purpose:
Prevent workload teams from modifying centralized logs.

Example:
Restrict access to the Log Archive account.
```

## Block Public S3 Buckets

```text
Purpose:
Prevent accidental public exposure of S3 data.

Example:
Deny actions that create public bucket policies or public ACLs.
```

---

# AWS Organizations Best Practices

* Use a dedicated management account.
* Do not run workloads in the management account.
* Use Organizational Units to group accounts by function.
* Use separate accounts for production and non-production.
* Use separate accounts for security and logging.
* Enable All Features mode.
* Use SCPs as preventive guardrails.
* Use delegated administrator accounts for security services.
* Use consolidated billing for cost visibility.
* Apply tag policies for cost and ownership tracking.
* Enable CloudTrail and AWS Config across all accounts.
* Use IAM Identity Center for centralized access.
* Review SCPs before applying them broadly.
* Test policies in sandbox or non-production OUs first.
* Keep root account credentials protected with MFA.
* Use automation for account creation and baseline setup.

---

# AWS Organizations vs AWS Control Tower

| Area              | AWS Organizations                                      | AWS Control Tower                                           |
| ----------------- | ------------------------------------------------------ | ----------------------------------------------------------- |
| Purpose           | Central account management and governance              | Managed landing zone setup and governance                   |
| Main Function     | Organize accounts, apply policies, consolidate billing | Automate landing zone, guardrails, and account provisioning |
| Account Structure | Root, OUs, accounts                                    | Uses AWS Organizations underneath                           |
| Guardrails        | SCPs and policies                                      | Preventive and detective controls                           |
| Account Creation  | Can create accounts                                    | Uses Account Factory for standardized account creation      |
| Best For          | Multi-account governance foundation                    | Enterprise landing zone deployment                          |

---

# Interview Questions and Sample Answers

## Q1: What is AWS Organizations?

AWS Organizations is an AWS service used to centrally manage and govern multiple AWS accounts. It supports account grouping with Organizational Units, consolidated billing, Service Control Policies, and integrations with AWS services for security, compliance, and governance.

---

## Q2: What is the difference between a management account and a member account?

The management account creates and manages the AWS Organization, controls billing, and applies organization-level policies. Member accounts are the AWS accounts inside the organization where workloads or shared services are usually deployed.

---

## Q3: What is an Organizational Unit?

An Organizational Unit is a logical group of AWS accounts inside AWS Organizations. OUs are used to organize accounts by environment, team, workload, or function and to apply policies consistently.

---

## Q4: What is a Service Control Policy?

A Service Control Policy defines the maximum permissions available in AWS accounts. SCPs do not grant permissions. They restrict what IAM users and roles can do inside accounts.

---

## Q5: What is consolidated billing?

Consolidated billing allows multiple AWS accounts in an organization to be billed together under the management account. It provides one bill, centralized payment, and account-level cost visibility.

---

## Q6: Why should workloads not run in the management account?

Workloads should not run in the management account because it is used for organization-level administration and billing. Keeping it workload-free reduces risk, limits blast radius, and protects critical administrative functions.

---

## Q7: How does AWS Organizations support governance?

AWS Organizations supports governance by allowing accounts to be grouped into OUs and controlled with policies such as SCPs, tag policies, and backup policies. It also integrates with services such as CloudTrail, Config, GuardDuty, Security Hub, and Control Tower for centralized security and compliance management.

---

# Solution Architect Tips

For AWS Solutions Architect interviews and exams, remember:

* AWS Organizations is the foundation for multi-account AWS environments.
* Use OUs to group accounts logically.
* Use SCPs to set maximum permissions.
* SCPs do not grant access.
* Use consolidated billing for centralized cost management.
* Use All Features mode for advanced governance.
* Use delegated administrator accounts to reduce use of the management account.
* Use AWS Control Tower on top of AWS Organizations for landing zone automation.
* Keep production and non-production workloads in separate accounts.
* Keep the management account free of workloads.

---

# Key Takeaways

* AWS Organizations centrally manages multiple AWS accounts.
* It supports OUs, SCPs, consolidated billing, and service integrations.
* It is a core part of multi-account strategy and landing zone design.
* SCPs provide preventive governance controls.
* Consolidated billing improves cost visibility.
* OUs simplify account organization and policy management.
* AWS Control Tower uses AWS Organizations to build and govern landing zones.
