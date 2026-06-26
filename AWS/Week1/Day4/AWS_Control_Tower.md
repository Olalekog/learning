# AWS Control Tower – Features and Characteristics

## What is AWS Control Tower?

AWS Control Tower is an AWS managed service that helps organizations set up, govern, and manage a secure multi-account AWS environment.

It provides a ready-made landing zone with built-in security, governance, logging, identity, and account management features.

AWS Control Tower is commonly used for:

* Multi-account strategy
* Landing zone setup
* Governance and guardrails
* Account provisioning
* Centralized logging
* Security baseline configuration
* Compliance monitoring
* Enterprise AWS environment management

---

# Why AWS Control Tower is Important

AWS Control Tower helps organizations create a secure AWS foundation faster than building everything manually.

Instead of manually configuring AWS Organizations, OUs, accounts, logging, identity access, and guardrails, AWS Control Tower automates much of the landing zone setup.

## Main Benefits

* Faster landing zone deployment
* Standardized account setup
* Centralized governance
* Built-in security controls
* Reduced manual configuration errors
* Easier account provisioning
* Improved compliance visibility
* Better multi-account management
* Stronger operational consistency

---

# Key Features of AWS Control Tower

## 1. Landing Zone

A landing zone is a secure, scalable, multi-account AWS environment.

AWS Control Tower creates and manages a landing zone that includes:

* AWS Organizations
* Organizational Units
* Shared accounts
* Security baseline
* Centralized logging
* IAM Identity Center
* Controls
* Account provisioning

### Benefits

* Provides a ready AWS foundation
* Supports enterprise cloud adoption
* Helps enforce security and compliance standards
* Provides a consistent multi-account structure

---

## 2. AWS Organizations Integration

AWS Control Tower uses AWS Organizations to manage AWS accounts centrally.

### Capabilities

* Create AWS accounts
* Manage member accounts
* Group accounts into Organizational Units
* Apply organization-level controls
* Use consolidated billing
* Enable service integrations

### Benefits

* Centralized account governance
* Better policy management
* Easier multi-account administration
* Improved security and billing control

---

## 3. Organizational Units

Organizational Units, also called OUs, are logical groups of AWS accounts.

### Common OU Examples

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

* Groups accounts by purpose
* Makes governance easier
* Allows different controls for different environments
* Supports enterprise account structure

---

## 4. Shared Accounts

AWS Control Tower creates or uses shared accounts that support centralized governance.

### Common Shared Accounts

| Account                | Purpose                                     |
| ---------------------- | ------------------------------------------- |
| Management Account     | Manages AWS Organizations and billing       |
| Log Archive Account    | Stores centralized logs                     |
| Audit/Security Account | Supports security and compliance monitoring |

### Best Practice

Do not run application workloads in the management account.

---

## 5. Account Factory

Account Factory is an AWS Control Tower feature used to provision AWS accounts with a standard baseline.

It allows cloud administrators and authorized IAM Identity Center users to create accounts within the landing zone.

### Account Factory Can Configure

* Account name
* Account email
* Organizational Unit placement
* IAM Identity Center access
* Network baseline
* Standard governance controls

### Benefits

* Faster account creation
* Consistent account setup
* Reduced manual errors
* Automatic governance alignment
* Easier onboarding for application teams

---

## 6. Account Factory for Terraform

Account Factory for Terraform, also called AFT, provides Terraform-based account provisioning and customization for AWS Control Tower environments.

AFT sets up a Terraform pipeline to provision and customize accounts while keeping them governed by AWS Control Tower.

### Benefits

* Uses Terraform workflow
* Supports account customization
* Enables Git-based account provisioning
* Helps standardize account vending
* Supports infrastructure as code practices

---

## 7. Controls and Guardrails

AWS Control Tower uses controls, also commonly called guardrails, to help govern AWS accounts.

AWS Control Tower supports preventive, detective, and proactive controls to govern resources and monitor compliance across groups of AWS accounts.

## Types of Controls

### Preventive Controls

Preventive controls stop risky actions before they happen.

Examples:

* Prevent disabling CloudTrail
* Prevent deleting AWS Config
* Restrict use of unapproved AWS Regions
* Prevent changes to protected resources

### Detective Controls

Detective controls identify violations after they occur.

Examples:

* Detect public S3 buckets
* Detect unencrypted resources
* Detect unrestricted security groups
* Detect missing logging configuration

### Proactive Controls

Proactive controls check resources before they are deployed.

Examples:

* Validate CloudFormation resources before provisioning
* Check whether resources meet policy requirements
* Prevent non-compliant infrastructure from being deployed

---

## 8. Centralized Logging

AWS Control Tower sets up centralized logging through a log archive account.

### Logs May Include

* AWS CloudTrail logs
* AWS Config logs
* Account activity logs
* Compliance-related logs

### Benefits

* Central audit trail
* Better investigation support
* Improved compliance evidence
* Reduced risk of log tampering
* Stronger security visibility

---

## 9. Security and Audit Account

AWS Control Tower includes an audit or security account for security monitoring and governance.

### Purpose

* Security reviews
* Compliance visibility
* Audit access
* Cross-account security monitoring
* Incident investigation

### Benefits

* Separates security responsibility from workload teams
* Improves audit readiness
* Provides centralized security visibility
* Supports least privilege access

---

## 10. IAM Identity Center Integration

AWS Control Tower can integrate with IAM Identity Center for centralized user access.

### Benefits

* Centralized workforce access
* Role-based access to AWS accounts
* Easier onboarding and offboarding
* Supports federation with identity providers
* Reduces individual IAM user usage

---

## 11. Dashboard Visibility

AWS Control Tower provides a dashboard for monitoring landing zone health, accounts, OUs, and controls.

### Benefits

* Central visibility
* Easier governance monitoring
* View account enrollment status
* Track control compliance
* Identify drift and governance issues

---

## 12. Drift Detection

Drift happens when AWS Control Tower-managed resources are changed outside of AWS Control Tower.

AWS Control Tower can detect certain types of governance drift, such as changes to expected controls, account baselines, or trusted access settings.

### Examples of Drift

* Control removed outside AWS Control Tower
* Required baseline changed manually
* Trusted access disabled
* Managed resources modified directly

### Benefits

* Helps maintain landing zone integrity
* Detects unauthorized or manual changes
* Improves governance consistency
* Supports operational control

---

## 13. Region Governance

AWS Control Tower allows administrators to configure governance across supported AWS Regions.

AWS recommends avoiding expansion into Regions where workloads do not need to run, because resources deployed in non-governed Regions can remain outside AWS Control Tower governance.

### Benefits

* Limits unnecessary regional exposure
* Supports compliance requirements
* Reduces governance complexity
* Helps enforce approved Region usage

---

## 14. Customization Options

AWS Control Tower can be customized using additional AWS tools and solutions.

### Common Customization Methods

* Account Factory
* Account Factory for Terraform
* Customizations for AWS Control Tower
* Landing Zone Accelerator
* CloudFormation StackSets
* Terraform
* AWS Service Catalog

### Benefits

* Supports enterprise-specific requirements
* Allows standard baseline extension
* Enables custom security controls
* Supports infrastructure as code

---

# Characteristics of AWS Control Tower

| Characteristic | Description                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------- |
| Managed        | AWS provides a managed service for landing zone setup and governance                          |
| Multi-Account  | Built for managing multiple AWS accounts                                                      |
| Secure         | Provides security baselines, logging, and controls                                            |
| Governed       | Uses controls to enforce and monitor compliance                                               |
| Scalable       | Supports growing AWS environments with many accounts and OUs                                  |
| Automated      | Automates account provisioning and baseline setup                                             |
| Centralized    | Provides central visibility and governance                                                    |
| Integrated     | Works with AWS Organizations, IAM Identity Center, CloudTrail, Config, and other AWS services |
| Auditable      | Supports centralized logs and compliance evidence                                             |
| Customizable   | Can be extended with AFT, CfCT, LZA, Terraform, and StackSets                                 |

---

# Common AWS Control Tower Components

| Component              | Purpose                                            |
| ---------------------- | -------------------------------------------------- |
| Landing Zone           | Secure multi-account AWS foundation                |
| AWS Organizations      | Central account management                         |
| Organizational Units   | Logical grouping of accounts                       |
| Management Account     | Organization and billing administration            |
| Log Archive Account    | Centralized log storage                            |
| Audit/Security Account | Security and compliance visibility                 |
| Account Factory        | Standard AWS account provisioning                  |
| Controls               | Governance rules for accounts and OUs              |
| IAM Identity Center    | Centralized workforce access                       |
| Dashboard              | Visibility into accounts, controls, and compliance |

---

# Example AWS Control Tower Account Structure

```text
AWS Control Tower Landing Zone
│
├── Management Account
│
├── Security OU
│   ├── Audit/Security Account
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

---

# Example AWS Control Tower Governance Flow

```text
New account request
        |
        v
Account Factory
        |
        v
Account created in selected OU
        |
        v
Baseline applied
        |
        v
Controls applied
        |
        v
CloudTrail and Config enabled
        |
        v
Account available for workload team
```

---

# AWS Control Tower Use Cases

## 1. Enterprise Landing Zone

Use AWS Control Tower to create a secure AWS foundation for enterprise workloads.

## 2. Multi-Account Governance

Use it to manage multiple AWS accounts with consistent controls and account structure.

## 3. Standard Account Provisioning

Use Account Factory to create accounts with approved configurations.

## 4. Compliance Monitoring

Use controls and centralized logging to monitor compliance.

## 5. Security Baseline Deployment

Use AWS Control Tower to apply baseline security services and configurations.

## 6. Cloud Adoption Acceleration

Use it to speed up AWS adoption while maintaining governance and control.

---

# AWS Control Tower vs AWS Organizations

| Area              | AWS Organizations                   | AWS Control Tower                                     |
| ----------------- | ----------------------------------- | ----------------------------------------------------- |
| Purpose           | Central account management          | Managed landing zone and governance                   |
| Main Function     | Create accounts, OUs, SCPs, billing | Automate landing zone setup and controls              |
| Account Structure | Root, OUs, accounts                 | Uses AWS Organizations underneath                     |
| Guardrails        | SCPs and policies                   | Preventive, detective, and proactive controls         |
| Account Creation  | Supports account creation           | Account Factory provides standardized account vending |
| Logging           | Must be designed/configured         | Central logging is part of the landing zone baseline  |
| Best For          | Multi-account foundation            | Enterprise-ready governed AWS environment             |

---

# AWS Control Tower vs Landing Zone

| Area           | Landing Zone                                              | AWS Control Tower                                           |
| -------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Meaning        | Secure cloud foundation design                            | AWS managed service that creates and governs a landing zone |
| Scope          | Account, identity, network, security, logging, governance | Automates and manages many landing zone components          |
| Implementation | Can be custom or AWS-managed                              | AWS-managed implementation option                           |
| Best For       | Enterprise cloud foundation                               | Faster setup with AWS best practices                        |

---

# Best Practices

* Use AWS Control Tower to start a secure multi-account environment.
* Do not run workloads in the management account.
* Use separate accounts for production and non-production.
* Use a dedicated log archive account.
* Use a dedicated audit or security account.
* Use Organizational Units to group accounts logically.
* Apply controls based on account purpose and risk level.
* Use Account Factory for standardized account creation.
* Use IAM Identity Center for centralized access.
* Enable centralized logging and monitoring.
* Avoid changing AWS Control Tower-managed resources manually.
* Use AFT if your organization prefers Terraform-based account provisioning.
* Use approved AWS Regions only.
* Monitor for drift regularly.
* Test controls before applying them broadly.
* Use automation for custom baselines and account extensions.

---

# Interview Questions and Sample Answers

## Q1: What is AWS Control Tower?

AWS Control Tower is an AWS managed service that helps set up and govern a secure multi-account AWS environment. It creates a landing zone using AWS Organizations, organizational units, shared accounts, centralized logging, IAM Identity Center, Account Factory, and governance controls.

---

## Q2: What problem does AWS Control Tower solve?

AWS Control Tower solves the problem of manually building and governing a multi-account AWS environment. It automates landing zone setup, account provisioning, security baselines, centralized logging, and governance controls.

---

## Q3: What is Account Factory?

Account Factory is an AWS Control Tower feature used to create AWS accounts with a standard baseline. It helps provision accounts into the correct Organizational Unit with required governance and configuration.

---

## Q4: What are controls in AWS Control Tower?

Controls are governance rules that help enforce and monitor compliance across AWS accounts and OUs. They can be preventive, detective, or proactive.

---

## Q5: What is the difference between AWS Organizations and AWS Control Tower?

AWS Organizations provides the foundation for managing accounts, OUs, policies, and billing. AWS Control Tower builds on AWS Organizations by adding a managed landing zone, account factory, centralized logging, IAM Identity Center integration, and governance controls.

---

## Q6: What is drift in AWS Control Tower?

Drift occurs when AWS Control Tower-managed resources are changed outside of AWS Control Tower. Drift can cause the landing zone, accounts, or controls to no longer match the expected governed configuration.

---

## Q7: Why should workloads not run in the management account?

Workloads should not run in the management account because it is used for organization-level administration and billing. Keeping it free of workloads reduces risk, limits blast radius, and protects critical management functions.

---

# Solution Architect Tips

For AWS Solutions Architect interviews and exams, remember:

* AWS Control Tower is used to set up and govern a landing zone.
* It uses AWS Organizations underneath.
* Account Factory provisions standardized AWS accounts.
* Controls provide governance across accounts and OUs.
* Preventive controls block actions.
* Detective controls detect violations.
* Proactive controls check resources before deployment.
* Centralized logging uses a log archive account.
* Security visibility is supported through an audit or security account.
* IAM Identity Center supports centralized access.
* Avoid modifying AWS Control Tower-managed resources manually.
* Use AFT when Terraform-based account vending is required.

---

# Key Takeaways

* AWS Control Tower provides a managed landing zone for AWS.
* It helps automate multi-account setup and governance.
* It uses AWS Organizations, OUs, shared accounts, controls, and Account Factory.
* It supports centralized logging, security baselines, and account provisioning.
* It reduces manual setup and improves consistency.
* It is commonly used for enterprise AWS cloud adoption.
