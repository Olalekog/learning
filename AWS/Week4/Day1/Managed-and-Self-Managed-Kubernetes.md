# Managed and Self-Managed Kubernetes

## Overview

Kubernetes can be deployed using either a **managed** or **self-managed** operating model.

- In **managed Kubernetes**, a cloud provider manages the Kubernetes control plane and may also assist with worker-node lifecycle management.
- In **self-managed Kubernetes**, an organization installs, operates, secures, upgrades, and maintains both the control plane and worker nodes.

Common managed Kubernetes services include:

- Amazon Elastic Kubernetes Service (Amazon EKS)
- Azure Kubernetes Service (AKS)
- Google Kubernetes Engine (GKE)

Common tools used to create self-managed Kubernetes clusters include:

- `kubeadm`
- Kubespray
- Rancher Kubernetes Engine
- Ansible
- Terraform

---

# 1. Managed Kubernetes

Managed Kubernetes is a cloud service where the cloud provider operates and maintains the Kubernetes control plane and some supporting cluster services.

## Features of Managed Kubernetes

### Managed Control Plane

The cloud provider manages core control-plane components such as:

- Kubernetes API server
- Scheduler
- Controller Manager
- `etcd`
- Cloud Controller Manager

### High Availability

The control plane is normally distributed across multiple availability zones or fault domains.

### Automated Maintenance

Managed services commonly provide:

- Control-plane patching
- Supported Kubernetes upgrades
- Control-plane monitoring
- Component replacement
- Backup of control-plane state

### Cloud Service Integration

Managed Kubernetes integrates with cloud services such as:

- Load balancers
- Identity and access management
- Virtual networks
- Firewalls
- Container registries
- Block and file storage
- Monitoring and logging
- Key management
- Secrets management

### Managed Node Groups

Providers can assist with:

- Worker-node provisioning
- Node replacement
- Rolling updates
- Node autoscaling
- Health monitoring
- Multiple node pools

### Autoscaling

Managed Kubernetes supports:

- Horizontal Pod Autoscaler
- Vertical Pod Autoscaler
- Cluster Autoscaler
- Node autoscaling
- Serverless Kubernetes compute

### Storage Integration

Managed services commonly support Container Storage Interface drivers for services such as:

- Amazon EBS
- Amazon EFS
- Azure Disk
- Azure Files
- Google Persistent Disk
- Google Filestore

### Security Integration

Managed Kubernetes commonly supports:

- Cloud IAM integration
- Private API endpoints
- Encryption
- Audit logging
- Security groups or firewall rules
- Managed add-ons
- Policy controls

## Characteristics of Managed Kubernetes

- Lower operational overhead
- Faster cluster provisioning
- Simplified control-plane management
- Built-in cloud integrations
- Provider-supported upgrades
- Easier high-availability configuration
- Additional managed-service costs
- Less control over control-plane components
- Possible vendor lock-in
- Shared responsibility for security
- Suitable for cloud-native and enterprise workloads

## Customer Responsibilities

Even when Kubernetes is managed, the customer is normally responsible for:

- Deployments
- Pods
- Services
- ConfigMaps
- Secrets
- Namespaces
- Ingress resources
- NetworkPolicies
- PersistentVolumeClaims
- Container images
- Kubernetes RBAC
- Workload security
- Application monitoring
- Resource requests and limits
- Application-data backups
- Worker nodes, unless managed or serverless compute is used

## Advantages of Managed Kubernetes

- Reduced cluster-administration effort
- Highly available control plane
- Simplified maintenance
- Easier cloud-service integration
- Faster application deployment
- Provider support
- Easier autoscaling
- Managed node-group options

## Disadvantages of Managed Kubernetes

- Additional service costs
- Reduced control over the control plane
- Provider-specific restrictions
- Possible vendor lock-in
- Limited control-plane customization
- Cloud dependency
- Workload security remains the customer's responsibility

---

# 2. Self-Managed Kubernetes

Self-managed Kubernetes is installed, configured, operated, secured, and maintained by an organization.

It can run on:

- Physical servers
- Virtual machines
- Public cloud instances
- Private clouds
- On-premises data centers
- Edge environments
- Air-gapped environments

## Features of Self-Managed Kubernetes

### Full Control

The organization controls:

- API server
- Scheduler
- Controller Manager
- `etcd`
- Certificates
- Networking
- Storage
- Worker nodes
- Security policies

### Custom Cluster Architecture

Administrators can customize:

- Control-plane topology
- Worker-node configuration
- Networking
- Storage
- Authentication
- Authorization
- Admission controls
- Logging
- Monitoring
- Backup and recovery

### Flexible Deployment Location

Self-managed Kubernetes can run in:

- Public clouds
- Private clouds
- On-premises environments
- Edge locations
- Isolated networks

### Custom Networking

Administrators can select networking tools such as:

- Calico
- Cilium
- Flannel
- Weave Net

### Custom Storage

Organizations can integrate storage systems that meet specialized requirements for:

- Performance
- Availability
- Compliance
- Data locality
- Cost

### Custom Authentication

Self-managed clusters can integrate with:

- LDAP
- Active Directory
- OpenID Connect
- Client certificates
- Custom identity systems

### Complete Upgrade Control

Administrators decide:

- Which Kubernetes version to use
- When to upgrade
- How upgrades are performed
- When nodes and components are replaced

## Characteristics of Self-Managed Kubernetes

- Full infrastructure control
- Greater customization
- Higher operational responsibility
- More complex installation
- Manual control-plane maintenance
- Manual backup and recovery
- Greater flexibility
- Requires experienced administrators
- Suitable for specialized or on-premises environments
- Higher risk of configuration errors
- No managed control-plane service fee
- Infrastructure and staffing costs can be significant

## Administrator Responsibilities

The organization is responsible for:

- Installing Kubernetes
- Configuring the control plane
- Managing `etcd`
- Managing certificates
- Configuring networking
- Configuring storage
- Maintaining worker nodes
- Monitoring cluster health
- Performing upgrades
- Applying security patches
- Backing up cluster data
- Designing high availability
- Troubleshooting failures
- Managing disaster recovery

## Advantages of Self-Managed Kubernetes

- Full cluster control
- Extensive customization
- On-premises support
- Flexible networking and storage
- Full Kubernetes-version control
- Reduced dependency on one cloud provider
- Suitable for regulated or isolated environments

## Disadvantages of Self-Managed Kubernetes

- Complex installation
- Higher maintenance burden
- Requires strong Kubernetes expertise
- Manual upgrades and patching
- Greater risk of downtime
- Manual disaster-recovery planning
- Higher staffing costs
- More difficult troubleshooting

---

# 3. Kubernetes Control Plane

The **control plane** manages the Kubernetes cluster.

It makes scheduling decisions, responds to cluster events, stores configuration, and ensures the actual state of the cluster matches the desired state.

## Main Control-Plane Components

| Component | Purpose |
|---|---|
| `kube-apiserver` | Provides the Kubernetes API |
| `etcd` | Stores cluster state and configuration |
| `kube-scheduler` | Selects worker nodes for new Pods |
| `kube-controller-manager` | Runs controllers that maintain desired state |
| `cloud-controller-manager` | Integrates Kubernetes with cloud-provider services |

## Features of the Kubernetes Control Plane

### API Management

The `kube-apiserver` processes requests from:

- `kubectl`
- CI/CD pipelines
- Kubernetes controllers
- Operators
- External automation tools
- Worker nodes

### Cluster-State Management

The control plane stores cluster information in `etcd`.

Examples include:

- Deployments
- Pods
- Services
- ConfigMaps
- Secrets
- Namespaces
- Roles
- RoleBindings
- Node information

### Pod Scheduling

The scheduler selects the most appropriate worker node for a Pod.

Scheduling decisions may consider:

- CPU availability
- Memory availability
- Resource requests
- Node selectors
- Node affinity
- Pod affinity
- Pod anti-affinity
- Taints and tolerations
- Topology-spread constraints

### Desired-State Management

Controllers continuously compare the desired state with the actual state.

For example, when a Deployment requires three replicas but only two Pods are running, Kubernetes creates another Pod.

### Authentication and Authorization

The control plane supports:

- Client certificates
- ServiceAccounts
- OpenID Connect
- Cloud IAM integration
- Role-Based Access Control
- Admission controllers

### Cluster Coordination

The control plane coordinates:

- Pod creation
- Pod deletion
- Rolling updates
- Replica management
- Node-health monitoring
- Endpoint updates
- Namespace management
- Service discovery

### High Availability

A production control plane should be distributed across multiple servers or availability zones.

## Characteristics of the Control Plane

- Manages the cluster
- Maintains desired state
- Provides the Kubernetes API
- Stores cluster data in `etcd`
- Makes scheduling decisions
- Handles authentication and authorization
- Monitors Kubernetes resources
- Should be highly available
- Requires backups and security controls
- Control-plane failure can prevent cluster-management operations
- Existing workloads may continue running temporarily during an outage
- Should be protected from unauthorized network access

---

# 4. Control Plane in Managed Kubernetes

In managed Kubernetes, the cloud provider usually manages the control plane.

## Provider Responsibilities

The provider commonly manages:

- API-server availability
- `etcd`
- Control-plane patching
- Control-plane monitoring
- Control-plane scaling
- Kubernetes version support
- Control-plane backups
- High availability
- Replacement of failed components

## Customer Responsibilities

The customer remains responsible for:

- API endpoint access
- Kubernetes RBAC
- User and ServiceAccount permissions
- Audit-log configuration
- Kubernetes-version selection
- Upgrade planning
- Admission policies
- Workload security

## Characteristics

- Customers normally cannot access control-plane servers directly
- High availability is usually built in
- Maintenance is performed by the provider
- Supported Kubernetes versions may be limited
- Customization may be restricted
- A control-plane service fee may apply

---

# 5. Control Plane in Self-Managed Kubernetes

In self-managed Kubernetes, the organization operates all control-plane components.

## Administrator Responsibilities

Administrators must manage:

- API-server installation
- Scheduler installation
- Controller Manager installation
- `etcd` deployment
- Certificate creation and renewal
- Control-plane networking
- High availability
- Load balancing
- Backups
- Security patches
- Kubernetes upgrades
- Disaster recovery
- Monitoring and alerting

## Characteristics

- Full configuration control
- Greater flexibility
- Greater operational complexity
- Manual high-availability configuration
- Manual `etcd` backup and recovery
- Higher skill requirements
- Greater security responsibility
- Greater risk of downtime from configuration errors

---

# 6. Kubernetes Worker Nodes

A **worker node** is a physical server or virtual machine that runs Kubernetes Pods and application containers.

Pods are assigned to worker nodes by the Kubernetes control plane.

## Main Worker-Node Components

| Component | Purpose |
|---|---|
| `kubelet` | Communicates with the control plane and manages Pods |
| Container runtime | Runs containers, such as `containerd` or CRI-O |
| `kube-proxy` | Maintains network rules for Kubernetes Services |
| CNI plugin | Provides Pod networking |
| CSI driver | Provides persistent-storage integration |
| Pods | Run application containers |

## Features of Worker Nodes

### Container Execution

Worker nodes run application containers through a supported container runtime.

Common runtimes include:

- `containerd`
- CRI-O

### Pod Management

The `kubelet` receives Pod specifications and ensures that required containers are running.

### Networking

Worker nodes provide connectivity between:

- Pods on the same node
- Pods on different nodes
- Pods and Services
- Pods and external systems

Common CNI plugins include:

- Calico
- Cilium
- Flannel
- Amazon VPC CNI
- Azure CNI

### Service Networking

`kube-proxy`, or an alternative networking implementation, routes traffic to Kubernetes Services.

### Persistent Storage

Worker nodes mount volumes requested by Pods through CSI drivers.

Examples include:

- Amazon EBS
- Amazon EFS
- Azure Disk
- Azure Files
- Google Persistent Disk
- Network File System storage

### Resource Management

Worker nodes provide:

- CPU
- Memory
- Local storage
- Networking

Kubernetes uses resource requests and limits to manage workload placement and consumption.

### Health Reporting

The `kubelet` reports node conditions such as:

- Ready
- MemoryPressure
- DiskPressure
- PIDPressure
- NetworkUnavailable

### Workload Isolation

Worker nodes support workload isolation through:

- Linux namespaces
- Control groups
- Security contexts
- AppArmor
- SELinux
- Seccomp
- Taints and tolerations
- Node affinity

### Scaling

Worker nodes can be added or removed manually or automatically.

Scaling options include:

- Manual node provisioning
- Cluster Autoscaler
- Managed node groups
- Serverless Kubernetes compute

## Characteristics of Worker Nodes

- Run application workloads
- Provide compute, memory, storage, and networking
- Communicate with the control plane
- Can run multiple Pods
- Require a container runtime
- Require networking configuration
- Can be physical or virtual machines
- Can be added or removed from the cluster
- Failed Pods can be rescheduled
- Node failure affects Pods running on that node
- Require operating-system updates and patches
- Should be monitored for capacity and health
- Production clusters should use multiple nodes

---

# 7. Worker Nodes in Managed Kubernetes

Managed Kubernetes platforms offer several node-management options.

## Managed Node Groups

The provider may assist with:

- Automated provisioning
- Node replacement
- Autoscaling
- Rolling updates
- Health monitoring
- IAM integration
- Network integration
- Storage integration

Examples include:

- Amazon EKS managed node groups
- AKS node pools
- GKE node pools

## Self-Managed Nodes in a Managed Cluster

A customer can use a managed control plane while managing worker nodes independently.

The customer is then responsible for:

- Creating virtual machines
- Installing node components
- Joining nodes to the cluster
- Updating machine images
- Replacing failed nodes
- Configuring autoscaling
- Applying operating-system patches

## Serverless Worker Compute

Some managed Kubernetes platforms can run Pods without customer-managed nodes.

Examples include:

- AWS Fargate for Amazon EKS
- GKE Autopilot
- Azure virtual nodes

## Characteristics

- Easy integration with cloud services
- Multiple node pools
- Support for different instance types
- Availability-zone distribution
- Easier autoscaling
- Customer still manages Pod configuration
- Compute costs depend on selected resources
- Provider-specific features may increase vendor dependency

---

# 8. Worker Nodes in Self-Managed Kubernetes

In self-managed Kubernetes, the organization manages the complete worker-node lifecycle.

## Administrator Responsibilities

Administrators must:

- Provision servers or virtual machines
- Install the operating system
- Install the container runtime
- Install and configure `kubelet`
- Join nodes to the cluster
- Configure networking
- Configure storage
- Apply security patches
- Monitor node health
- Replace failed nodes
- Drain nodes before maintenance
- Upgrade node components
- Configure autoscaling
- Manage node certificates

## Characteristics

- Full hardware and operating-system control
- Support for customized machine configurations
- Greater networking and storage flexibility
- Higher maintenance effort
- Manual node replacement
- Manual upgrade coordination
- Greater operational responsibility
- Suitable for on-premises and specialized environments

---

# 9. Control Plane vs Worker Nodes

| Area | Control Plane | Worker Nodes |
|---|---|---|
| Primary purpose | Manages the cluster | Runs application workloads |
| API server | Yes | No |
| Scheduler | Yes | No |
| `etcd` | Yes | No |
| `kubelet` | Sometimes | Yes |
| Container runtime | May be present | Required |
| Application workloads | Normally avoided | Yes |
| Scheduling decisions | Makes decisions | Executes scheduled Pods |
| Stores cluster state | Yes | No |
| Reports node health | Receives reports | Sends reports |
| Failure effect | Management operations may stop | Workloads on the node may stop |
| Scaling purpose | Management capacity | Application demand |

---

# 10. Managed vs Self-Managed Kubernetes

| Area | Managed Kubernetes | Self-Managed Kubernetes |
|---|---|---|
| Control plane | Provider-managed | Organization-managed |
| Installation | Mostly automated | Manual or tool-assisted |
| High availability | Usually built in | Must be designed |
| Upgrades | Provider-supported | Organization-managed |
| Patching | Partially automated | Fully organization-managed |
| `etcd` | Provider-managed | Organization-managed |
| Customization | Limited | Extensive |
| Operational effort | Lower | Higher |
| Cloud integration | Built in | Manually configured |
| Monitoring | Provider integration available | Must be installed |
| Security | Shared responsibility | Organization responsibility |
| Service cost | Service fee plus infrastructure | Infrastructure plus staffing |
| Vendor lock-in | Possible | Usually lower |
| On-premises support | Limited | Strong |
| Required expertise | Moderate | High |
| Deployment speed | Faster | Slower |
| Troubleshooting | Shared with provider | Organization handles everything |
| Disaster recovery | Shared | Organization-designed |

---

# 11. Managed vs Self-Managed Component Responsibilities

| Component | Managed Kubernetes | Self-Managed Kubernetes |
|---|---|---|
| API server | Provider-managed | Customer-managed |
| Scheduler | Provider-managed | Customer-managed |
| Controller Manager | Provider-managed | Customer-managed |
| `etcd` | Provider-managed | Customer-managed |
| Control-plane backups | Provider-managed or supported | Customer-managed |
| Control-plane high availability | Usually built in | Customer-designed |
| Worker nodes | Provider-assisted or customer-managed | Customer-managed |
| Operating-system patching | Shared or provider-assisted | Customer-managed |
| Container runtime | Shared or customer-managed | Customer-managed |
| CNI networking | Provider-supported | Customer-configured |
| CSI storage | Provider-supported | Customer-configured |
| Pod workloads | Customer-managed | Customer-managed |
| Kubernetes RBAC | Customer-managed | Customer-managed |
| Application security | Customer-managed | Customer-managed |
| Node scaling | Often automated | Customer-configured |
| Disaster recovery | Shared responsibility | Customer responsibility |

---

# 12. When to Choose Managed Kubernetes

Managed Kubernetes is appropriate when:

- Faster cluster deployment is required
- The team wants lower operational overhead
- Applications primarily run in a public cloud
- Cloud-service integration is important
- Built-in high availability is required
- Provider support is preferred
- The team has limited control-plane administration experience

---

# 13. When to Choose Self-Managed Kubernetes

Self-managed Kubernetes is appropriate when:

- Full control is required
- Kubernetes must run on-premises
- Specialized networking or storage is needed
- The environment is isolated or air-gapped
- Provider restrictions are unacceptable
- The organization has experienced Kubernetes administrators
- Custom security or compliance requirements must be implemented

---

# 14. Summary

Managed Kubernetes reduces operational complexity because the cloud provider manages the control plane and may also help manage worker nodes.

Self-managed Kubernetes provides maximum control and customization, but the organization is responsible for installation, upgrades, security, monitoring, high availability, backup, and disaster recovery.

The control plane manages the Kubernetes cluster, stores its state, schedules workloads, and maintains the desired configuration.

Worker nodes provide the compute resources where Pods and application containers run.
