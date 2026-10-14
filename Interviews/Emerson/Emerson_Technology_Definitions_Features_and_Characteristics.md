# Emerson — Technology Definitions, Features, and Characteristics

**Candidate:** Olalekan G. Ogundare  
**Target role:** Cloud Platform Infrastructure Engineer (DevOps)

Emerson’s job description names Kubernetes, Docker, Terraform, AWS, Azure, GCP, Argo CD, Flux, and several programming languages. It also includes practices such as CI/CD, DevSecOps, disaster recovery, Scrum, and SAFe.

This guide covers their definitions, features, and characteristics, with examples relevant to your interview. Individual cloud services in the comparison table are illustrative equivalents; the job description names the cloud platforms broadly.

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

## 11. Service discovery

**Definition:** A mechanism that allows applications to locate the services they need.

**Features and characteristics:**

- Uses stable names or registries.
- Accommodates changing backend instances.
- Reduces dependency on hardcoded addresses.
- Often integrates with DNS and health information.

**Kubernetes example:** An application calls a Service DNS name while the pods behind that Service change over time.

**Source:** [Kubernetes services and networking](https://kubernetes.io/docs/concepts/services-networking/).

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

## 16. Architecture and cybersecurity reviews

These are review activities mentioned in the job description.

| Review | Definition | Typical focus |
|---|---|---|
| Architecture review | Evaluates whether a design meets technical and business requirements | Availability, scalability, integrations, cost, recovery, ownership |
| Cybersecurity review | Evaluates threats and security controls | Identity, least privilege, encryption, exposure, secrets, logging, vulnerabilities |

**Interview example:** Bring a diagram showing components, data flows, trust boundaries, dependencies, and operational responsibilities, together with documented decisions and open risks.
