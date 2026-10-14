<a id="top"></a>

# Emerson — Technology Definitions, Features, and Characteristics

**Candidate:** Olalekan G. Ogundare  
**Target role:** Cloud Platform Infrastructure Engineer (DevOps)

Emerson’s job description names Kubernetes, Docker, Terraform, AWS, Azure, GCP, Argo CD, Flux, and several programming languages. It also includes practices such as CI/CD, DevSecOps, disaster recovery, Scrum, and SAFe.

This guide covers their definitions, features, and characteristics, with examples relevant to your interview. Individual cloud services in the comparison table are illustrative equivalents; the job description names the cloud platforms broadly.

## Index

- [1. Kubernetes](#1-kubernetes)
- [2. Docker](#2-docker)
- [3. Terraform](#3-terraform)
- [4. Argo CD](#4-argo-cd)
- [5. Flux](#5-flux)
- [6. AWS, Azure, and GCP](#6-aws-azure-and-gcp)
- [7. Programming and scripting languages](#7-programming-and-scripting-languages)
- [8. Infrastructure as Code — IaC](#8-infrastructure-as-code--iac)
- [9. CI/CD](#9-cicd)
- [10. DevSecOps](#10-devsecops)
- [11. Service discovery](#11-service-discovery)
- [12. Load balancing](#12-load-balancing)
- [13. Backup and disaster recovery](#13-backup-and-disaster-recovery)
- [14. Agile and Scrum](#14-agile-and-scrum)
- [15. SAFe — Scaled Agile Framework](#15-safe--scaled-agile-framework)
- [16. Architecture and cybersecurity reviews](#16-architecture-and-cybersecurity-reviews)
- [17. AWS services — individual definitions](#17-aws-services--individual-definitions)
  - [17.1 Amazon EC2 — Elastic Compute Cloud](#171-amazon-ec2--elastic-compute-cloud)
  - [17.2 Amazon EKS — Elastic Kubernetes Service](#172-amazon-eks--elastic-kubernetes-service)
  - [17.3 Amazon S3 — Simple Storage Service](#173-amazon-s3--simple-storage-service)
  - [17.4 Amazon VPC — Virtual Private Cloud](#174-amazon-vpc--virtual-private-cloud)
  - [17.5 AWS IAM — Identity and Access Management](#175-aws-iam--identity-and-access-management)
  - [17.6 Amazon CloudWatch](#176-amazon-cloudwatch)
- [18. Microsoft Azure services — individual definitions](#18-microsoft-azure-services--individual-definitions)
  - [18.1 Azure Virtual Machines](#181-azure-virtual-machines)
  - [18.2 AKS — Azure Kubernetes Service](#182-aks--azure-kubernetes-service)
  - [18.3 Azure Blob Storage](#183-azure-blob-storage)
  - [18.4 Azure Virtual Network — VNet](#184-azure-virtual-network--vnet)
  - [18.5 Microsoft Entra ID](#185-microsoft-entra-id)
  - [18.6 Azure RBAC — Role-Based Access Control](#186-azure-rbac--role-based-access-control)
  - [18.7 Azure Monitor](#187-azure-monitor)
- [19. Google Cloud services — individual definitions](#19-google-cloud-services--individual-definitions)
  - [19.1 Compute Engine](#191-compute-engine)
  - [19.2 GKE — Google Kubernetes Engine](#192-gke--google-kubernetes-engine)
  - [19.3 Cloud Storage](#193-cloud-storage)
  - [19.4 Google Cloud VPC — Virtual Private Cloud](#194-google-cloud-vpc--virtual-private-cloud)
  - [19.5 Google Cloud IAM — Identity and Access Management](#195-google-cloud-iam--identity-and-access-management)
  - [19.6 Cloud Monitoring](#196-cloud-monitoring)
- [20. Interview comparison reminders](#20-interview-comparison-reminders)

## 1. Kubernetes

**Definition:** An open-source platform for deploying, managing, and scaling containerized applications.

| Feature | Meaning |
|---|---|
| Declarative configuration | You describe the desired state; controllers work to maintain it. |
| Scheduling | Places pods on suitable worker nodes based on resources and constraints. |
| Self-healing | Restarts failed containers and replaces pods through workload controllers. |
| Scaling | Supports application scaling and integration with node autoscaling. |
| Rolling updates | Gradually replaces application replicas during deployment. |
| Service discovery | Provides stable service names for applications with changing pod addresses. |
| Storage integration | Supports persistent storage through volumes and storage drivers. |

**Characteristics:** API-driven, extensible, portable, and based on continuous reconciliation. Reliability depends on appropriate application design and cluster configuration.

Key components to understand:

| Component | Purpose |
|---|---|
| Control plane | Manages cluster state and scheduling decisions. |
| API server | Entry point for Kubernetes API requests. |
| etcd | Stores cluster configuration and state. |
| Scheduler | Assigns unscheduled pods to nodes. |
| Controller manager | Runs controllers that reconcile resources. |
| Worker node | Runs application pods. |
| kubelet | Ensures assigned containers run on a node. |
| Container runtime | Executes containers, commonly through containerd or CRI-O. |

**Interview connection:** “At Citibank, I managed EKS workloads with RBAC, namespace isolation, resource governance, and monitoring.”

**Sources:** [Kubernetes concepts](https://kubernetes.io/docs/concepts/), [Kubernetes components](https://kubernetes.io/docs/concepts/overview/components/), [Services and networking](https://kubernetes.io/docs/concepts/services-networking/).

[⬆ Go to top](#top)

## 2. Docker

**Definition:** A platform and toolset for building, distributing, and running containerized applications.

| Feature | Meaning |
|---|---|
| Dockerfile | Instructions for building an image. |
| Image | Packaged application, dependencies, and runtime filesystem. |
| Container | Running instance of an image. |
| Registry | Stores and distributes images. |
| Volumes | Persist data beyond an individual container’s lifecycle. |
| Networks | Provide connectivity between containers and external systems. |
| Multistage builds | Separate build tooling from the final runtime image. |

**Characteristics:** Containers are isolated processes that share the host kernel. Image portability depends on compatible operating-system and CPU architecture support. Containers are typically designed to be replaceable.

**Interview connection:** “Docker packages the application consistently; Kubernetes manages its deployment and operation across a cluster.”

**Source:** [Docker overview](https://docs.docker.com/get-started/docker-overview/).

[⬆ Go to top](#top)

## 3. Terraform

**Definition:** An Infrastructure as Code tool for defining and managing cloud and on-premises resources using configuration files.

| Feature | Meaning |
|---|---|
| Providers | Integrations with AWS, Azure, GCP, Kubernetes, and other APIs. |
| Resources | Infrastructure objects Terraform manages. |
| Modules | Reusable groups of infrastructure configuration. |
| Plan | Previews proposed changes. |
| Apply | Executes the approved changes. |
| State | Tracks relationships between configuration and actual resources. |
| Dependency graph | Determines the ordering of resource operations. |

**Characteristics:** Declarative, versionable, reusable, and suitable for multiple providers. Provider-specific resource definitions still differ across clouds.

**Interview connection:** “I built reusable Terraform modules at Citibank to standardize infrastructure across development, UAT, and production.”

**Source:** [What is Terraform?](https://developer.hashicorp.com/terraform/intro).

[⬆ Go to top](#top)

## 4. Argo CD

**Definition:** A declarative GitOps continuous delivery tool for Kubernetes.

| Feature | Meaning |
|---|---|
| Desired-state comparison | Compares deployed resources with the declared configuration. |
| Synchronization | Applies the desired configuration to the cluster. |
| Health visibility | Reports application resource health. |
| Automated sync | Can deploy approved configuration changes automatically. |
| Self-healing | Can correct live configuration drift when enabled. |
| Pruning | Can remove resources deleted from the desired configuration. |

**Characteristics:** Kubernetes-focused, controller-based, and commonly uses Git as the source of deployment configuration. It supports tools such as Helm and Kustomize.

**Example:** CI publishes an application image, a reviewed Git change updates its image reference, and Argo CD synchronizes the deployment.

**Sources:** [Argo CD documentation](https://argo-cd.readthedocs.io/en/stable/), [Automated sync policy](https://github.com/argoproj/argo-cd/blob/master/docs/user-guide/auto_sync.md).

[⬆ Go to top](#top)

## 5. Flux

**Definition:** A collection of Kubernetes controllers for continuous delivery using declarative configuration.

| Feature | Meaning |
|---|---|
| Source management | Retrieves configuration from supported sources such as Git and OCI artifacts. |
| Kustomize integration | Builds and reconciles Kubernetes configurations. |
| Helm integration | Manages Helm-based releases. |
| Image automation | Can update deployment configuration when new images meet defined policies. |
| Reconciliation | Continuously evaluates desired and actual state. |

**Characteristics:** Modular, Kubernetes-native, and designed around composable controllers and custom resources.

| Comparison | Argo CD | Flux |
|---|---|---|
| Common operating experience | Application-oriented UI, CLI, and API | Controller and Kubernetes API-oriented |
| Configuration model | Application resources and related configuration | Specialized source, Kustomize, and Helm resources |
| Shared purpose | Declarative continuous delivery | Declarative continuous delivery |

**Sources:** [Flux documentation](https://fluxcd.io/flux/), [Flux core concepts](https://fluxcd.io/flux/concepts/).

[⬆ Go to top](#top)

## 6. AWS, Azure, and GCP

**Definition:** Public cloud platforms providing on-demand infrastructure and managed services.

The job description names the platforms broadly. The individual services below are illustrative equivalents for interview preparation.

| Capability | AWS | Microsoft Azure | Google Cloud |
|---|---|---|---|
| Virtual machines | EC2 | Azure Virtual Machines | Compute Engine |
| Managed Kubernetes | EKS | AKS | GKE |
| Object storage | S3 | Blob Storage | Cloud Storage |
| Virtual networking | VPC | Virtual Network | VPC |
| Access management | IAM | Entra ID and Azure RBAC | Cloud IAM |
| Monitoring | CloudWatch | Azure Monitor | Cloud Monitoring |

**Shared features:** On-demand provisioning, API-driven automation, elastic capacity, managed services, and usage-based charging. Security and operational responsibilities depend on the service selected. These platforms offer broad infrastructure and application capabilities.

**Interview connection:** Your strongest documented platform experience is AWS and Azure. Explain transferable concepts when discussing GCP.

**Sources:** [AWS cloud computing](https://aws.amazon.com/what-is-cloud-computing/), [What is Azure?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-azure/), [Google Cloud documentation](https://docs.cloud.google.com/docs).

[⬆ Go to top](#top)

## 7. Programming and scripting languages

The job description lists these as examples; it does not require equal proficiency in every language.

| Language | Definition | Key features and characteristics | Infrastructure use |
|---|---|---|---|
| Python | General-purpose programming language | Readable syntax, dynamic typing, extensive libraries | Cloud API automation, inventory, reporting, validation |
| Bash | Unix shell and scripting language | Command execution, pipelines, redirection, environment variables | Linux administration, deployment scripts, troubleshooting |
| Go | Compiled programming language | Static typing, goroutines, compiled executables | Kubernetes controllers, operators, CLIs |
| C# | Statically typed language commonly used with .NET | Managed runtime, object-oriented features, asynchronous programming | Enterprise services and Azure applications |
| Java | Statically typed language commonly executed on the JVM | Garbage collection, mature libraries, concurrency support | Enterprise applications and microservices |
| JavaScript | Dynamic programming language | Event-driven programming, browser and server execution | Web applications and Node.js automation |
| TypeScript | JavaScript with a static type system | Compile-time checks, interfaces, JavaScript ecosystem compatibility | Application development and typed automation tooling |

**Interview connection:** “My strongest scripting languages are Python and Bash. I use Python for structured automation and API integration, and Bash for operating-system tasks and command orchestration.”

[⬆ Go to top](#top)

## 8. Infrastructure as Code — IaC

**Definition:** Managing infrastructure through machine-readable definitions stored and reviewed as code.

**Features:**

- Repeatable provisioning.
- Version history and peer review.
- Reusable infrastructure patterns.
- Automated validation and deployment.
- Consistent configuration across environments.

**Characteristics:** Infrastructure changes become traceable and reviewable. Configuration, state, credentials, and deployment permissions still need careful management.

**Example:** A Terraform module provisions an application’s network, compute, access controls, and monitoring.

[⬆ Go to top](#top)

## 9. CI/CD

**Definition:** Practices that automate software integration and delivery.

| Term | Definition | Typical activities |
|---|---|---|
| Continuous integration | Frequently integrate and validate changes | Build, test, lint, scan |
| Continuous delivery | Keep validated changes ready for release | Package, publish, validate, approve |
| Continuous deployment | Automatically release changes that pass required checks | Deploy and verify without a separate manual release decision |

**Characteristics:** Frequent feedback, repeatable execution, traceable artifacts, and smaller changes. Approval gates and deployment automation depend on the organization’s release model.

**Interview connection:** Your resume includes Jenkins, GitHub Actions, Harness, Azure DevOps, and AWS delivery tooling.

**Source:** [Microsoft — What is DevOps?](https://learn.microsoft.com/en-us/devops/what-is-devops).

[⬆ Go to top](#top)

## 10. DevSecOps

**Definition:** Integrating security into development, delivery, and operations.

| Feature | Purpose |
|---|---|
| Static analysis | Identifies potential security issues in source code. |
| Dependency scanning | Identifies known vulnerabilities in dependencies. |
| Secret scanning | Detects exposed credentials and tokens. |
| Container scanning | Identifies vulnerabilities in container images. |
| IaC scanning | Detects risky infrastructure configuration. |
| Policy as code | Enforces defined requirements automatically. |
| Runtime monitoring | Detects security issues after deployment. |

**Characteristics:** Shared responsibility, early feedback, automation, and continued security validation throughout the lifecycle.

**Interview connection:** “At Citibank, I integrated security scanning and OPA/Sentinel policy checks into delivery pipelines.”

**Source:** [Microsoft — Development and testing in DevSecOps](https://learn.microsoft.com/en-us/devops/devsecops/development-testing).

[⬆ Go to top](#top)

## 11. Service discovery

**Definition:** A mechanism that allows applications to locate the services they need.

**Features and characteristics:**

- Uses stable names or registries.
- Accommodates changing backend instances.
- Reduces dependency on hardcoded addresses.
- Often integrates with DNS and health information.

**Kubernetes example:** An application calls a Service DNS name while the pods behind that Service change over time.

**Source:** [Kubernetes services and networking](https://kubernetes.io/docs/concepts/services-networking/).

[⬆ Go to top](#top)

## 12. Load balancing

**Definition:** Distributing traffic across multiple backend instances.

| Feature | Purpose |
|---|---|
| Health checks | Identify eligible backends. |
| Traffic distribution | Spread requests or connections. |
| Layer 4 balancing | Routes using transport information such as TCP ports. |
| Layer 7 balancing | Routes using application information such as HTTP paths. |
| TLS termination | Handles encrypted client connections where configured. |

**Characteristics:** Helps availability and capacity utilization. Successful traffic distribution still requires healthy backends and sufficient application capacity.

Kubernetes Services and networking integrations provide mechanisms for reaching changing sets of application endpoints.

**Source:** [Kubernetes services and networking](https://kubernetes.io/docs/concepts/services-networking/).

[⬆ Go to top](#top)

## 13. Backup and disaster recovery

**Backup definition:** A recoverable copy of data or configuration.

**Disaster recovery definition:** The coordinated process for restoring a workload after a major disruption.

| Concept | Definition |
|---|---|
| RTO | Target time to restore service after disruption. |
| RPO | Target maximum data-loss window, measured in time. |
| Retention | How long recovery copies are preserved. |
| Replication | Maintaining another copy of data, synchronously or asynchronously. |
| Failover | Moving service to an alternate environment. |
| Failback | Returning service to the preferred environment. |
| Recovery drill | Testing recovery procedures and measuring results. |

| Strategy | Main characteristic |
|---|---|
| Backup and restore | Rebuild and restore following disruption. |
| Pilot light | Keep essential components available in the recovery location. |
| Warm standby | Maintain a running environment with reduced capacity. |
| Active-active | Serve traffic from multiple locations. |

**Characteristics:** Recovery requires infrastructure, data, identity, networking, application dependencies, and validation. Replication alone may also replicate corruption or deletion, so recovery copies remain important. Strategy selection depends on recovery objectives and cost.

**Sources:** [AWS — Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), [AWS — Plan for disaster recovery](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html).

[⬆ Go to top](#top)

## 14. Agile and Scrum

**Agile definition:** An approach to delivery emphasizing collaboration, feedback, incremental progress, and adaptation.

**Scrum definition:** A framework for managing complex work through timeboxed Sprints.

| Scrum element | Purpose |
|---|---|
| Product Backlog | Ordered work toward the Product Goal. |
| Sprint Planning | Establish the Sprint Goal and plan the work. |
| Daily Scrum | Inspect progress and adapt the plan. |
| Sprint Review | Inspect results with stakeholders. |
| Sprint Retrospective | Improve quality and team effectiveness. |
| Definition of Done | Shared quality criteria for completed work. |

**Characteristics:** Transparency, inspection, adaptation, and a self-managing team.

**Interview example:** Plan a Kubernetes upgrade with compatibility assessment, nonproduction testing, production execution, and validation as visible work.

**Source:** [The Scrum Guide](https://scrumguides.org/scrum-guide.html).

[⬆ Go to top](#top)

## 15. SAFe — Scaled Agile Framework

**Definition:** A framework for coordinating Lean and Agile delivery across multiple teams.

**Features and characteristics:**

- Shared priorities across teams.
- Coordinated planning and delivery.
- Cross-team dependency management.
- Alignment between delivery and business objectives.
- Practices for improving delivery at organizational scale.

SAFe is intended to support Agile coordination beyond an individual team.

**Interview connection:** Your resume does not explicitly establish formal SAFe experience. Discuss your enterprise coordination experience accurately and explain how you would adapt to Emerson’s framework.

**Source:** [Scaled Agile — Why SAFe?](https://scaledagile.com/what-is-safe/why-safe/).

[⬆ Go to top](#top)

## 16. Architecture and cybersecurity reviews

These are review activities mentioned in the job description.

| Review | Definition | Typical focus |
|---|---|---|
| Architecture review | Evaluates whether a design meets technical and business requirements | Availability, scalability, integrations, cost, recovery, ownership |
| Cybersecurity review | Evaluates threats and security controls | Identity, least privilege, encryption, exposure, secrets, logging, vulnerabilities |

**Interview example:** Bring a diagram showing components, data flows, trust boundaries, dependencies, and operational responsibilities, together with documented decisions and open risks.

[⬆ Go to top](#top)

## 17. AWS services — individual definitions

The following services expand the AWS column in section 6. These are representative services for preparing for the role, rather than individually named requirements in the job description.

[⬆ Go to top](#top)

### 17.1 Amazon EC2 — Elastic Compute Cloud

**Definition:** A service providing on-demand virtual servers, called instances, in AWS.

**Features:**

- Instance families with different CPU, memory, storage, network, and GPU capabilities.
- Amazon Machine Images (AMIs) for repeatable server deployment.
- Integration with EBS storage, VPC networking, security groups, and IAM roles.
- Integration with EC2 Auto Scaling and load balancing.
- Multiple purchasing and capacity options, including On-Demand and Spot.

**Characteristics:** Infrastructure as a Service (IaaS). Each instance runs in an Availability Zone. Customers manage the guest operating system, application configuration, and appropriate security controls. One instance alone does not provide application high availability.

**Example:** Run Linux application servers in an Auto Scaling group across multiple Availability Zones.

**Source:** [What is Amazon EC2?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)

[⬆ Go to top](#top)

### 17.2 Amazon EKS — Elastic Kubernetes Service

**Definition:** An AWS service for running Kubernetes with an AWS-managed Kubernetes control plane.

**Features:**

- Managed control-plane availability and operation.
- Worker options including managed node groups and other supported compute modes.
- Integration with AWS identity, networking, load balancing, and storage.
- Support for Kubernetes APIs and ecosystem tools such as Helm and GitOps controllers.
- Cluster observability and add-on integrations.

**Characteristics:** A managed Kubernetes service with shared operational responsibility. Management of nodes, networking, and add-ons depends on the operating mode. Application configuration, access controls, and workload reliability remain important customer responsibilities.

**Example:** Host microservices on EKS, provision infrastructure using Terraform, and reconcile application deployments with Argo CD.

**Source:** [What is Amazon EKS?](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)

[⬆ Go to top](#top)

### 17.3 Amazon S3 — Simple Storage Service

**Definition:** A scalable object storage service that stores objects in buckets.

**Features:**

- Storage classes for different access and retention needs.
- Versioning, lifecycle policies, and configurable replication.
- Encryption and access controls through policies and identity permissions.
- Object Lock for supported retention and immutability requirements.
- API access and event integrations.

**Characteristics:** Object storage rather than a conventional VM block disk. Bucket location and storage class affect resilience, availability, and cost. Durability concerns preserving data; versioning and recovery controls help address accidental changes or deletion.

**Example:** Store deployment artifacts, backups, datasets, and centralized logs.

**Source:** [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

[⬆ Go to top](#top)

### 17.4 Amazon VPC — Virtual Private Cloud

**Definition:** A logically isolated virtual network for AWS resources.

**Features:**

- Configurable IP address ranges and subnets.
- Route tables, internet gateways, and NAT connectivity options.
- Security groups and network access control lists.
- Private service connectivity through VPC endpoints.
- Connectivity options for other networks and on-premises environments.

**Characteristics:** A VPC is regional; each subnet is scoped to one Availability Zone. A subnet’s internet routing helps determine whether it is public or private. Resources also require suitable addressing and security rules to communicate.

**Example:** Place application nodes in private subnets and internet-facing load balancers in public subnets.

**Source:** [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

[⬆ Go to top](#top)

### 17.5 AWS IAM — Identity and Access Management

**Definition:** A service for controlling access to AWS resources through identities and permissions.

**Features:**

- Users, groups, roles, and permission policies.
- Role assumption and temporary credential workflows.
- Resource- and action-level permissions with supported conditions.
- Federation and cross-account access patterns.
- Integration with AWS services for authorization.

**Characteristics:** Identity-based access control with least privilege as a design principle. IAM is global within an AWS partition rather than tied to one Region. Effective access depends on applicable identity policies, resource policies, organizational controls, and other authorization limits.

**Example:** Give a deployment pipeline a narrowly scoped role to assume in a target account instead of distributing long-lived access keys.

**Source:** [What is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)

[⬆ Go to top](#top)

### 17.6 Amazon CloudWatch

**Definition:** An AWS monitoring and observability service for infrastructure and applications.

**Features:**

- Metrics, dashboards, and alarms.
- Log collection, retention, and querying.
- Container and application monitoring integrations.
- Custom telemetry and agent-based collection.
- Alerting integrations for operational response.

**Characteristics:** Combines service-generated and configured telemetry. Not every operating-system or application signal is collected automatically; agents or instrumentation may be required. Collection, retention, and queries can contribute to cost.

**Example:** Alert on application error rates and correlate them with EKS resource metrics and logs.

**Source:** [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

[⬆ Go to top](#top)

## 18. Microsoft Azure services — individual definitions

Microsoft Entra ID and Azure RBAC are explained separately because identity management and Azure resource authorization have distinct roles.

[⬆ Go to top](#top)

### 18.1 Azure Virtual Machines

**Definition:** An IaaS service for running Windows and Linux virtual machines in Azure.

**Features:**

- VM sizes for different compute, memory, storage, and GPU requirements.
- Managed disks, images, network interfaces, and extensions.
- Availability options including supported Availability Zones and availability sets.
- Integration with Virtual Machine Scale Sets for groups of VMs.
- Monitoring, backup, and identity integrations.

**Characteristics:** Provides control over the guest operating system and installed applications. Customers remain responsible for appropriate OS maintenance, configuration, and workload resilience. Availability choices depend on Region and VM support.

**Example:** Run an enterprise application on Linux VMs with monitoring and a tested backup strategy.

**Source:** [Azure Virtual Machines overview](https://learn.microsoft.com/en-us/azure/virtual-machines/overview)

[⬆ Go to top](#top)

### 18.2 AKS — Azure Kubernetes Service

**Definition:** A managed Kubernetes service for deploying and operating containerized applications in Azure.

**Features:**

- Azure-managed Kubernetes control plane.
- Node pools for workload capacity and isolation requirements.
- Scaling, upgrade, and networking capabilities.
- Microsoft Entra identity and authorization integrations.
- Azure storage and monitoring integrations.

**Characteristics:** Uses Kubernetes APIs with Azure-managed platform capabilities. Operational responsibility varies by configuration and service mode. Workload health, resource settings, security, and application recovery still require deliberate design.

**Example:** Deploy Helm-packaged services to AKS with separate node pools for different workload needs.

**Source:** [What is AKS?](https://learn.microsoft.com/en-us/azure/aks/what-is-aks)

[⬆ Go to top](#top)

### 18.3 Azure Blob Storage

**Definition:** Azure’s object storage service for large amounts of unstructured data such as documents, images, logs, and backups.

**Features:**

- Storage accounts containing containers and blobs.
- Access tiers and lifecycle management for suitable data.
- Redundancy options to support different resilience requirements.
- Access controls, encryption, and data-protection capabilities.
- HTTP/API access and integration with analytics and application services.

**Characteristics:** Object storage with account, container, and blob organization. Cost and recovery behavior depend on storage configuration and tier. Some archive-tier operations require rehydration before data can be read.

**Example:** Retain application logs and backups, moving older data to an appropriate lower-cost tier.

**Source:** [Azure Blob Storage overview](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview)

[⬆ Go to top](#top)

### 18.4 Azure Virtual Network — VNet

**Definition:** A private virtual network that enables Azure resources to communicate with each other, external networks, and on-premises environments.

**Features:**

- Address spaces and subnets.
- Network security groups and routing controls.
- VNet peering and private connectivity options.
- Integration with VPN Gateway and ExpressRoute.
- Private endpoints for supported Azure services.

**Characteristics:** A VNet is regional, and its subnets can contain resources across Availability Zones in that Region. Connectivity depends on routes, security rules, DNS, and service-specific settings.

**Example:** Use a hub-and-spoke architecture to centralize connectivity while isolating application networks.

**Source:** [What is Azure Virtual Network?](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)

[⬆ Go to top](#top)

### 18.5 Microsoft Entra ID

**Definition:** Microsoft’s cloud identity and access management service for users, applications, and workload identities.

**Features:**

- Authentication and single sign-on.
- Multifactor authentication and Conditional Access capabilities.
- Application registrations and enterprise application integration.
- Support for service principals and managed identities.
- Privileged access and identity governance capabilities, subject to licensing.

**Characteristics:** Tenant-based identity service. It provides authentication and related identity capabilities, while Azure RBAC governs authorization to Azure resources. It has a different architecture from traditional Windows Server Active Directory Domain Services.

**Example:** Require MFA for administrators and use workload identities for applications accessing Azure services.

**Source:** [Microsoft Entra overview](https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra)

[⬆ Go to top](#top)

### 18.6 Azure RBAC — Role-Based Access Control

**Definition:** Azure’s authorization system for controlling who can perform which actions on Azure resources at a specified scope.

**Features:**

- Built-in and custom roles.
- Assignments to users, groups, service principals, and managed identities.
- Scope at management group, subscription, resource group, or resource level.
- Permission inheritance through the resource hierarchy.
- Separate management-plane and supported data-plane permissions.

**Characteristics:** A role assignment combines a principal, role definition, and scope. Narrow scopes and appropriate roles support least privilege. Azure resource roles are distinct from Microsoft Entra directory roles.

**Example:** Give an application’s managed identity access to read blobs in a designated storage scope without granting subscription-wide administration.

**Source:** [Azure RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)

[⬆ Go to top](#top)

### 18.7 Azure Monitor

**Definition:** Azure’s observability service for collecting, analyzing, and acting on telemetry from applications and infrastructure.

**Features:**

- Metrics, logs, alerts, and visualization.
- Log Analytics for log querying and analysis.
- Application Insights for application performance monitoring.
- Container and Kubernetes monitoring integrations.
- Action groups and integrations for incident notification.

**Characteristics:** Supports platform and instrumented telemetry across multiple environments. Coverage depends on diagnostic settings, agents, collection rules, and application instrumentation. Retention and ingestion choices affect cost.

**Example:** Investigate an AKS latency increase using application telemetry, cluster metrics, and logs.

**Source:** [Azure Monitor overview](https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/overview)

[⬆ Go to top](#top)

## 19. Google Cloud services — individual definitions

### 19.1 Compute Engine

**Definition:** Google Cloud’s IaaS service for running virtual machine instances.

**Features:**

- Predefined and supported custom machine configurations.
- Images, persistent storage options, and GPU configurations.
- Instance templates and managed instance groups.
- Integration with autoscaling, networking, and load balancing.
- Spot VM options for interruption-tolerant workloads.

**Characteristics:** Individual VMs are zonal resources. Customers manage the guest OS and applications. Regional managed instance groups can distribute instances across zones for a more resilient architecture.

**Example:** Run application instances in a managed instance group behind a load balancer.

**Source:** [Compute Engine overview](https://docs.cloud.google.com/compute/docs/overview)

[⬆ Go to top](#top)

### 19.2 GKE — Google Kubernetes Engine

**Definition:** Google Cloud’s managed service for deploying and operating Kubernetes clusters.

**Features:**

- Google-managed Kubernetes control plane.
- Standard and Autopilot operating modes.
- Cluster scaling and lifecycle-management capabilities.
- Integration with Google Cloud networking, identity, and storage.
- Logging and monitoring integrations.

**Characteristics:** Standard and Autopilot provide different levels of infrastructure management and control. Workload design, application configuration, access management, and recovery planning remain important in both modes.

**Example:** Select an operating mode based on workload constraints and the level of node management the team wants to retain.

**Source:** [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)

[⬆ Go to top](#top)

### 19.3 Cloud Storage

**Definition:** Google Cloud’s managed object storage service for storing objects in buckets.

**Features:**

- Multiple storage classes for different access patterns.
- Location choices for storage placement and resilience requirements.
- Lifecycle management and retention capabilities.
- Object versioning and recovery-related controls.
- IAM-based access and API integration.

**Characteristics:** Object storage rather than a VM block disk. Storage class affects pricing and access-related charges; location determines data placement. Appropriate retention and protection settings help address accidental deletion.

**Example:** Store backups, build artifacts, and data-processing inputs with lifecycle policies.

**Source:** [Cloud Storage overview](https://docs.cloud.google.com/storage/docs/introduction)

[⬆ Go to top](#top)

### 19.4 Google Cloud VPC — Virtual Private Cloud

**Definition:** A virtual networking service connecting Google Cloud resources and supporting connectivity to other networks.

**Features:**

- Subnets, routes, and firewall controls.
- Shared VPC for centralized networking across projects.
- VPC Network Peering and hybrid connectivity integrations.
- Private access capabilities for supported Google services.
- Flow logging and network observability integrations.

**Characteristics:** A VPC network is global; subnets are regional. This scope differs from AWS VPCs and Azure VNets. Routing, firewall controls, DNS, and address planning determine actual connectivity.

**Example:** Use Shared VPC to let a central networking team manage subnets consumed by application projects.

**Source:** [Google Cloud VPC overview](https://docs.cloud.google.com/vpc/docs/overview)

[⬆ Go to top](#top)

### 19.5 Google Cloud IAM — Identity and Access Management

**Definition:** Google Cloud’s system for controlling which principals can perform which actions on resources.

**Features:**

- Predefined and custom roles.
- Policies binding principals to roles.
- Organization, folder, project, and supported resource-level scopes.
- Policy inheritance through the resource hierarchy.
- Conditional access bindings and workload identity integrations where supported.

**Characteristics:** Authorization is permission- and resource-based. Effective access depends on applicable policies and controls. Narrowly scoped roles and federated workload identities help reduce unnecessary privilege and reliance on service-account keys.

**Example:** Grant a workload permission to read a specific Cloud Storage bucket instead of giving it broad project permissions.

**Source:** [Google Cloud IAM overview](https://docs.cloud.google.com/iam/docs/overview)

[⬆ Go to top](#top)

### 19.6 Cloud Monitoring

**Definition:** Google Cloud’s service for collecting and analyzing metrics and monitoring infrastructure and application health.

**Features:**

- Metrics, dashboards, and alerting policies.
- Uptime checks and service monitoring capabilities.
- Integrations with Google Cloud services and supported external telemetry.
- Managed Service for Prometheus integration.
- Notification channels for operational alerts.

**Characteristics:** Focuses on metric-based visibility and alerting. Cloud Logging is a separate, integrated service for log storage and analysis. Application coverage depends on instrumentation and configured collection.

**Example:** Monitor GKE workload health and notify the support team when latency or error-rate thresholds are exceeded.

**Source:** [Cloud Monitoring overview](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)

[⬆ Go to top](#top)

## 20. Interview comparison reminders

| Topic | AWS | Azure | Google Cloud |
|---|---|---|---|
| VM service | EC2 | Virtual Machines | Compute Engine |
| Managed Kubernetes | EKS | AKS | GKE |
| Object storage hierarchy | Bucket → object | Storage account → container → blob | Bucket → object |
| Virtual network scope | Regional VPC | Regional VNet | Global VPC |
| Subnet scope | Availability Zone | Region; can span zones | Region; can span zones |
| Resource permissions | IAM policies and roles | Azure RBAC with Entra identities | IAM policies and roles |
| Monitoring | CloudWatch | Azure Monitor | Cloud Monitoring, integrated with Cloud Logging |

**Practice answer:** “The common building blocks are compute, Kubernetes, storage, networking, identity, and observability. I map those capabilities across providers while checking differences in resource scope, permissions, operating responsibility, and recovery behavior.”

[⬆ Go to top](#top)
