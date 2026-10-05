<a id="top"></a>

# ExxonMobil — Terraform and Azure Interview Guide

Prepared for Olalekan Gabriel Ogundare.

20 interview questions with sample answers tailored to the supplied role. Most answers take approximately 30–60 seconds to deliver.

These are practice answers, not verified accounts of your work history. For scenario questions, substitute a real project, company, and outcome you can explain confidently.

## Index

1. [Tell me about yourself and why you fit this role.](#1-tell-me-about-yourself-and-why-you-fit-this-role)
2. [How would you maintain and improve a large enterprise Terraform codebase?](#2-how-would-you-maintain-and-improve-a-large-enterprise-terraform-codebase)
3. [Describe how you would troubleshoot a failed Terraform deployment.](#3-describe-how-you-would-troubleshoot-a-failed-terraform-deployment)
4. [How do you design reusable Terraform modules, and who should consume them?](#4-how-do-you-design-reusable-terraform-modules-and-who-should-consume-them)
5. [How do you version modules and handle a breaking change?](#5-how-do-you-version-modules-and-handle-a-breaking-change)
6. [Where would you publish Terraform modules, and how would teams consume them?](#6-where-would-you-publish-terraform-modules-and-how-would-teams-consume-them)
7. [How do you manage and protect Terraform state in Azure?](#7-how-do-you-manage-and-protect-terraform-state-in-azure)
8. [What would you do if Terraform state were locked or damaged?](#8-what-would-you-do-if-terraform-state-were-locked-or-damaged)
9. [How do you detect and remediate infrastructure drift?](#9-how-do-you-detect-and-remediate-infrastructure-drift)
10. [How do you use Terraform workspaces for development, test, and production?](#10-how-do-you-use-terraform-workspaces-for-development-test-and-production)
11. [Describe a Terraform deployment pipeline using Azure DevOps or GitHub Actions.](#11-describe-a-terraform-deployment-pipeline-using-azure-devops-or-github-actions)
12. [What checks should run beyond terraform validate?](#12-what-checks-should-run-beyond-terraform-validate)
13. [How do you manage Terraform variables, secrets, and provider upgrades?](#13-how-do-you-manage-terraform-variables-secrets-and-provider-upgrades)
14. [How would you troubleshoot an Azure application that suddenly became unavailable?](#14-how-would-you-troubleshoot-an-azure-application-that-suddenly-became-unavailable)
15. [How do you implement least-privilege RBAC and Azure governance?](#15-how-do-you-implement-least-privilege-rbac-and-azure-governance)
16. [How would you design high availability and disaster recovery?](#16-how-would-you-design-high-availability-and-disaster-recovery)
17. [Give an example of an Azure cost optimization opportunity.](#17-give-an-example-of-an-azure-cost-optimization-opportunity)
18. [How would you support SQL Server infrastructure alongside DBAs?](#18-how-would-you-support-sql-server-infrastructure-alongside-dbas)
19. [How would you deploy Terraform in a restricted or disconnected network?](#19-how-would-you-deploy-terraform-in-a-restricted-or-disconnected-network)
20. [Do you have ArcGIS Enterprise experience, and how would you support it?](#20-do-you-have-arcgis-enterprise-experience-and-how-would-you-support-it)

[⬆ Back to top](#top)

---

## Role priorities

| Focus | Allocation |
|---|---:|
| Infrastructure as Code and automation | 60% |
| Azure engineering | 25% |
| Enterprise platform administration | 10% |
| SQL Server infrastructure support | 5% |

[⬆ Back to top](#top)

---

## Questions and answers

### 1. Tell me about yourself and why you fit this role.

“I’m a cloud and DevOps engineer with over 15 years of IT experience, including extensive work with Azure, AWS, infrastructure automation, and production support. My strongest areas are Terraform, reusable infrastructure modules, CI/CD, networking, and cloud security.

My approach is to make infrastructure consistent, repeatable, and easier to operate. That includes improving existing code, reviewing deployment plans, troubleshooting failures, and partnering with application and security teams. This role appeals to me because Terraform is the primary responsibility, supported by hands-on Azure engineering and operational ownership.”

[⬆ Back to top](#top)

### 2. How would you maintain and improve a large enterprise Terraform codebase?

“I would first understand its structure, resource ownership, dependencies, state boundaries, and deployment process. I’d review provider versions, module versions, duplicated code, and known operational issues.

Then I would prioritize improvements that reduce deployment risk, such as consistent naming, variable validation, documented interfaces, and reusable modules. I would make changes incrementally through pull requests and review plans for unexpected replacement or deletion. For example, I would improve one application’s network configuration before rolling the pattern across other environments.”

[⬆ Back to top](#top)

### 3. Describe how you would troubleshoot a failed Terraform deployment.

“Suppose a pipeline failed while creating an Azure VM. I would identify the first meaningful error and determine whether it came from authentication, permissions, configuration, policy, quota, or an Azure service issue.

If the deployment identity lacked permission to attach a network interface, I would verify the identity, resource scope, and required action, then request the narrowest appropriate access. Before rerunning, I would check which resources were already created and generate a fresh plan. After recovery, I would add a preventive check or improve the deployment documentation.”

[⬆ Back to top](#top)

### 4. How do you design reusable Terraform modules, and who should consume them?

“I design modules around stable infrastructure capabilities, such as networking, virtual machines, or storage accounts. Each module should have a clear purpose, documented inputs and outputs, variable validation, and examples.

For a VM module, I would expose approved settings such as size, subnet, image, and disk configuration, while incorporating required monitoring and tagging. Application and platform teams could consume it without duplicating implementation details. I would collect feedback from those teams and avoid creating one oversized module with too many unrelated responsibilities.”

For an experience-based answer, name the actual consuming teams and approximate number only if you know them.

[⬆ Back to top](#top)

### 5. How do you version modules and handle a breaking change?

“I use semantic versioning and release notes. A compatible enhancement receives a minor release, while a change requiring consumers to modify their configuration receives a major release. Consumers pin their module versions.

For example, changing a single subnet input into a structured network object could be a breaking change. I would publish a migration guide, validate the upgrade in a representative nonproduction environment, and coordinate adoption with application teams. If resource addresses changed during refactoring, I would include appropriate migration instructions to avoid unnecessary recreation.”

Registry modules support version constraints; Git-sourced modules can use a pinned ref.

[⬆ Back to top](#top)

### 6. Where would you publish Terraform modules, and how would teams consume them?

“I would use the organization’s approved private module registry or controlled Git repositories. A registry makes modules easier to discover and provides a consistent versioned interface. With Git repositories, teams can consume a release tag or commit reference.

The release process would include review, automated checks, examples, a changelog, and an identifiable owner. Production consumers should use an approved version rather than a moving branch. I would also document dependencies and supported Terraform and provider versions.”

[⬆ Back to top](#top)

### 7. How do you manage and protect Terraform state in Azure?

“I would use an Azure Storage remote backend with Microsoft Entra authentication, restricted access, and separate state boundaries for environments and infrastructure components. The Azure backend supports locking, which helps prevent concurrent changes to the same state.

I would protect state as sensitive data, enable suitable recovery controls, and ensure the pipeline can reach the storage endpoint. I would also limit who can modify state directly and document recovery procedures. Separate deployment workflows should never accidentally target the same production state.”

[⬆ Back to top](#top)

### 8. What would you do if Terraform state were locked or damaged?

“For a lock, I would first check whether another deployment was still running. I would not force-unlock an active operation. If the lock were abandoned, I would confirm ownership and clear it through the approved process.

For damaged state, I would stop deployments and compare the last known good state with current Azure resources. Restoring an older state alone may not be sufficient because infrastructure could have changed afterward. I would reconcile the differences, import resources where needed, and review a new plan before applying.”

[⬆ Back to top](#top)

### 9. How do you detect and remediate infrastructure drift?

“I would schedule Terraform plans and investigate unexpected differences. Suppose someone changed a VM size in the Azure portal during an incident. I would determine whether that change was approved and still required.

If it was valid, I would update the code through a reviewed pull request. If it was unauthorized or temporary, I would plan a controlled return to the desired configuration. A refresh-only operation can reconcile state with observed infrastructure, but it does not update the configuration to make the change permanent.”

[⬆ Back to top](#top)

### 10. How do you use Terraform workspaces for development, test, and production?

“CLI workspaces provide separate state for the same configuration, but I would not rely on them alone for production isolation. Where environments require different identities, permissions, or access controls, I prefer separate root configurations and backend boundaries.

I would still reuse the same modules, with environment-specific inputs. That gives us consistent infrastructure patterns while keeping production access and deployment approvals separate. I would also distinguish CLI workspaces from HCP Terraform workspaces, which include their own configuration, variables, and run history.”

[⬆ Back to top](#top)

### 11. Describe a Terraform deployment pipeline using Azure DevOps or GitHub Actions.

“My workflow starts with a feature branch and pull request. The pipeline checks formatting, validates configuration, performs security and policy checks, and generates a plan using the correct environment identity.

Reviewers examine the proposed changes, especially deletion, replacement, networking, and access changes. After approval, the deployment stage applies the approved plan and performs operational checks. I would use workload identity federation where supported, restrict deployment permissions, and retain the commit, plan, approval, and deployment evidence. Each environment receives its own plan and approval process.”

[⬆ Back to top](#top)

### 12. What checks should run beyond terraform validate?

“Validation checks configuration correctness, but I also want to verify security, policy, and behavior. I would use tools such as Checkov for infrastructure scanning, secret scanning for repository content, and OPA or Sentinel where those platforms are part of the organization’s workflow.

Policies could reject public storage access, unapproved regions, or prohibited module versions. Module tests would check meaningful behavior, including whether required settings and outputs work. For significant changes, I would deploy a representative test environment and confirm that the infrastructure supports the application.”

[⬆ Back to top](#top)

### 13. How do you manage Terraform variables, secrets, and provider upgrades?

“I keep ordinary configuration in reviewed variable files and retrieve credentials through approved identity or secret-management mechanisms. I avoid hardcoding secrets or committing them to Git.

Marking a value sensitive hides it from normal output, but does not automatically keep it out of state. State and saved plans therefore need protection. For upgrades, I pin provider constraints, commit the provider lock file, review release notes, and test changes through a separate pull request. Module versions are managed separately from the provider lock file.”

[⬆ Back to top](#top)

### 14. How would you troubleshoot an Azure application that suddenly became unavailable?

“I would first establish the scope: one instance, one application, or a wider platform issue. I would check recent changes, Azure service health, application logs, VM health, and load-balancer backend status.

Then I would trace the request path through DNS, routing, security rules, the load balancer, and the application listener. For example, a healthy application might become unreachable because an NSG change blocks its health probe. I would restore service with the smallest approved change, validate recovery, and document the root cause and prevention.”

[⬆ Back to top](#top)

### 15. How do you implement least-privilege RBAC and Azure governance?

“I separate human access from deployment identities and assign permissions at the smallest practical scope. I prefer group-based assignments for people and dedicated workload identities for automation.

For example, an application deployment identity should manage its approved resources without automatically receiving subscription-wide ownership. Privileged human access should be time-bound where appropriate, using PIM. I would use Azure Policy for requirements such as approved locations or mandatory resource settings, then retain policy results, access reviews, and approved exceptions as evidence.”

[⬆ Back to top](#top)

### 16. How would you design high availability and disaster recovery?

“I would begin with business requirements: how much downtime and data loss are acceptable? Those define the recovery time objective and recovery point objective.

For availability, I would remove single points of failure and distribute supported application components across availability zones. For regional recovery, I would plan replication or restoration, networking, identity, DNS, and application dependencies. Azure Site Recovery can support VM replication and failover, but recovery must include application and data validation. I would test the runbook and measure actual recovery time.”

[⬆ Back to top](#top)

### 17. Give an example of an Azure cost optimization opportunity.

“Suppose utilization data showed that several application VMs were consistently oversized. I would review CPU, memory, disk performance, and peak demand with the application owner before recommending smaller sizes.

I would test the change in a lower environment, schedule the production change, and compare performance afterward. Other opportunities include deallocating nonproduction VMs outside working hours and reviewing unused storage. Once demand is understood, I would evaluate commitment discounts. I would report savings alongside application performance so the business can see the full outcome.”

[⬆ Back to top](#top)

### 18. How would you support SQL Server infrastructure alongside DBAs?

“My responsibility would focus on the platform: VM capacity, disk latency and throughput, connectivity, patching, monitoring, and recovery infrastructure. The DBA would lead database-specific diagnosis and tuning.

For example, if users reported slow queries, I would correlate the timing with CPU pressure, memory, disk latency, throughput limits, and recent infrastructure changes. I would share that evidence with the DBA rather than immediately resizing the VM. For availability and recovery, we would jointly validate the selected SQL Server architecture, backups, failover, and application connectivity.”

[⬆ Back to top](#top)

### 19. How would you deploy Terraform in a restricted or disconnected network?

“I would first clarify whether the environment has controlled outbound access or is fully disconnected. That distinction determines which services and deployment methods are feasible.

For a restricted environment, I would place self-hosted agents where they can reach approved Azure endpoints and the state backend. I would arrange approved distribution of providers, modules, and tools, then validate DNS, certificates, proxies, and required service access. For a fully disconnected environment, I would verify the target platform’s capabilities before assuming ordinary Azure public-cloud deployment will work.”

[⬆ Back to top](#top)

### 20. Do you have ArcGIS Enterprise experience, and how would you support it?

Use this answer if you do not have direct ArcGIS experience:

“My strongest experience is in the Azure infrastructure that supports enterprise applications. I would be transparent that I have not directly administered ArcGIS Enterprise.

I would work with the GIS team to understand the supported architecture, sizing, networking, certificates, storage, identity, and recovery requirements. I could contribute by automating the Azure foundation, improving monitoring, and managing infrastructure changes. I would also learn the application-specific health checks and upgrade procedures so that platform changes are validated against GIS functionality.”

[⬆ Back to top](#top)

---

## Technical references

- Questions 5–6: [HashiCorp Terraform style guide](https://developer.hashicorp.com/terraform/language/style) and [Module configuration](https://developer.hashicorp.com/terraform/language/modules/configuration).
- Questions 7–8: [Azure Storage backend](https://developer.hashicorp.com/terraform/language/backend/azurerm), [State locking](https://developer.hashicorp.com/terraform/language/state/locking), and [State backends](https://developer.hashicorp.com/terraform/language/state/backends).
- Question 9: [Refresh-only state reconciliation](https://developer.hashicorp.com/terraform/tutorials/state/refresh).
- Question 10: [CLI workspaces](https://developer.hashicorp.com/terraform/cli/workspaces) and [State workspaces](https://developer.hashicorp.com/terraform/language/state/workspaces).
- Question 11: [Azure DevOps Terraform OIDC deployment sample](https://github.com/Azure-Samples/azure-devops-terraform-oidc-ci-cd).
- Question 13: [Terraform style guide](https://developer.hashicorp.com/terraform/language/style) and [Provider dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock).
- Question 14: [Azure VM connectivity troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-network/troubleshoot-vm-connectivity) and [Load-balancer health probe troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/azure/load-balancer/troubleshoot-load-balancer-health-probe-failures).
- Question 15: [Azure RBAC best practices](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices).
- Question 16: [Azure Site Recovery reliability](https://learn.microsoft.com/en-us/azure/reliability/reliability-site-recovery).
- Question 17: [Azure VM cost optimization](https://learn.microsoft.com/en-us/azure/virtual-machines/cost-optimization-best-practices).
- Question 18: [SQL Server Always On availability groups on Azure VMs](https://learn.microsoft.com/en-us/azure/azure-sql/virtual-machines/windows/availability-group-overview?view=azuresql).

[⬆ Back to top](#top)
