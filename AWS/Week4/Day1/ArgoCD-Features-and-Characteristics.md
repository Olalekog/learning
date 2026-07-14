# Features and Characteristics of Argo CD

**Argo CD** is an open-source, Kubernetes-native continuous delivery tool that implements the **GitOps** deployment model. It continuously compares the desired application configuration stored in Git with the resources running in Kubernetes.

## Core Features

### 1. GitOps-Based Deployment

Git acts as the source of truth for Kubernetes application configuration.

Changes are made through:

- Git commits
- Pull requests
- Code reviews
- Approved merges

Argo CD detects changes in Git and applies them to the target Kubernetes environment.

### 2. Continuous State Reconciliation

Argo CD continuously compares:

```text
Desired State in Git
        versus
Live State in Kubernetes
```

An application can have states such as:

- **Synced** – Git and the cluster match.
- **OutOfSync** – the cluster differs from Git.
- **Unknown** – Argo CD cannot determine the current state.

When configuration drift occurs, Argo CD can display the differences and restore the cluster to the desired state.

### 3. Automatic and Manual Synchronization

Argo CD supports two deployment approaches:

**Manual synchronization**

An operator reviews the changes and selects **Sync** through the UI or CLI.

**Automatic synchronization**

Argo CD automatically deploys changes when it detects that the Git configuration differs from the cluster.

```yaml
syncPolicy:
  automated:
    prune: true
    selfHeal: true
```

- `prune: true` removes resources deleted from Git.
- `selfHeal: true` restores resources that were manually modified in the cluster.

### 4. Configuration Drift Detection

Argo CD detects changes made directly to Kubernetes resources.

For example:

```bash
kubectl edit deployment todo-backend
```

If the replica count is changed manually, Argo CD identifies the application as **OutOfSync**. With self-healing enabled, it can automatically restore the value defined in Git.

### 5. Declarative Configuration

Argo CD resources can be defined as Kubernetes YAML manifests, including:

- Applications
- ApplicationSets
- AppProjects
- Repositories
- Clusters
- Argo CD configuration

Example:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: todo-application
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/example/todo-app-config.git
    targetRevision: main
    path: kubernetes/dev
  destination:
    server: https://kubernetes.default.svc
    namespace: todo-dev
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

### 6. Multiple Configuration-Management Tools

Argo CD supports:

- Plain Kubernetes YAML
- Helm
- Kustomize
- Jsonnet
- Custom configuration-management plugins

### 7. Web User Interface

The Argo CD web interface displays:

- Application synchronization status
- Application health
- Kubernetes resource relationships
- Deployment history
- Manifest differences
- Synchronization events
- Pods, Services, Deployments, and other resources

### 8. Command-Line Interface

Common commands include:

```bash
argocd app list
argocd app get todo-application
argocd app sync todo-application
argocd app diff todo-application
argocd app history todo-application
```

### 9. Application Health Monitoring

Common health statuses include:

- **Healthy**
- **Progressing**
- **Degraded**
- **Suspended**
- **Missing**
- **Unknown**

An application may be synchronized but unhealthy:

```text
Synchronization status: Synced
Health status: Degraded
```

### 10. Deployment History and Rollback

Argo CD records:

- Previous Git revisions
- Deployment times
- Deployed manifests
- Deployment initiators
- Synchronization results

Applications can be rolled back to a previous revision.

### 11. Multi-Cluster Deployment

A single Argo CD installation can manage multiple Kubernetes clusters:

```text
Argo CD
 ├── Development EKS Cluster
 ├── UAT EKS Cluster
 └── Production EKS Cluster
```

Supported platforms include:

- Amazon EKS
- Azure Kubernetes Service
- Google Kubernetes Engine
- OpenShift
- On-premises Kubernetes
- Self-managed Kubernetes

### 12. Multi-Environment Management

Argo CD can manage environment-specific configurations:

```text
gitops-repository/
├── base/
│   ├── deployment.yaml
│   └── service.yaml
└── overlays/
    ├── dev/
    ├── uat/
    └── production/
```

### 13. ApplicationSet Controller

ApplicationSet automates the creation of multiple Argo CD Applications.

Common generators include:

- Git generator
- List generator
- Cluster generator
- Matrix generator
- Merge generator
- Pull-request generator
- SCM-provider generator

### 14. AppProjects

AppProjects provide logical isolation and can restrict:

- Permitted Git repositories
- Destination clusters
- Destination namespaces
- Allowed Kubernetes resource types
- Denied Kubernetes resource types
- User and team permissions

### 15. Role-Based Access Control

Argo CD RBAC controls who can:

- View applications
- Create applications
- Synchronize applications
- Delete applications
- Access logs
- Manage repositories or clusters

Example:

```csv
p, role:developer, applications, get, development/*, allow
p, role:developer, applications, sync, development/*, allow
p, role:developer, applications, delete, production/*, deny
```

### 16. Single Sign-On

Argo CD can integrate with:

- GitHub
- GitLab
- Microsoft Entra ID
- Google
- Okta
- LDAP-based identity systems

### 17. Private Repository and Secret Support

Argo CD can authenticate to private repositories using:

- HTTPS credentials
- Personal access tokens
- SSH keys
- GitHub App credentials
- TLS certificates

It can also work with:

- External Secrets Operator
- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- Google Secret Manager
- Sealed Secrets

### 18. Notifications

Argo CD can send notifications through:

- Slack
- Email
- Microsoft Teams
- Webhooks
- PagerDuty

Typical notification events include:

- Application synchronized
- Synchronization failed
- Application became degraded
- Application health changed
- Deployment completed

### 19. Sync Waves and Hooks

Sync waves control deployment order.

```yaml
metadata:
  annotations:
    argocd.argoproj.io/sync-wave: "1"
```

Example order:

```text
Wave -1: Namespace and secrets
Wave 0: Database migration
Wave 1: Backend deployment
Wave 2: Frontend deployment
Wave 3: Validation job
```

Supported hooks include:

- `PreSync`
- `Sync`
- `PostSync`
- `SyncFail`
- `PostDelete`

### 20. Resource Pruning

When a resource is removed from Git, Argo CD can delete the corresponding Kubernetes resource.

Pruning should be carefully controlled for stateful resources such as databases and persistent volumes.

### 21. Sync Windows

Sync windows control when deployments are allowed or denied.

Examples:

- Allow deployments during maintenance windows.
- Block production deployments on weekends.
- Prevent synchronization during critical business periods.
- Permit emergency synchronization for authorized users.

### 22. Auditability and Traceability

Argo CD improves auditability through:

- Git commit history
- Pull-request history
- Code-review evidence
- Change ownership
- Approval history
- Synchronization history

### 23. High Availability and Scalability

Major Argo CD components include:

- API server
- Application controller
- Repository server
- Redis
- ApplicationSet controller
- Notifications controller
- Dex, when used

Argo CD can be deployed in a highly available configuration for production environments.

### 24. Webhooks and Polling

Argo CD periodically checks Git repositories for changes and can also receive webhooks from:

- GitHub
- GitLab
- Bitbucket
- Azure Repos

## Key Characteristics

| Characteristic | Description |
|---|---|
| Kubernetes-native | Runs inside Kubernetes and manages Kubernetes resources |
| Declarative | Applications and settings are described through YAML |
| Git-centric | Git stores and versions the desired deployment state |
| Pull-based | Argo CD pulls configuration from Git |
| Continuously reconciled | Regularly compares live state with Git |
| Self-healing | Can reverse unauthorized manual changes |
| Auditable | Git and synchronization history provide traceability |
| Multi-cluster | One installation can manage several clusters |
| Multi-tenant | AppProjects and RBAC isolate teams and applications |
| Extensible | Supports plugins, custom health checks, and custom actions |
| Secure | Supports SSO, RBAC, TLS, and private repository authentication |
| Observable | Provides UI, CLI, API, metrics, events, and notifications |
| Scalable | Supports ApplicationSet and HA deployments |
| Vendor-neutral | Works across cloud and on-premises Kubernetes platforms |

## Argo CD Deployment Flow

```text
Developer changes Kubernetes manifest
                ↓
Developer opens a pull request
                ↓
Team reviews and approves the change
                ↓
Change is merged into Git
                ↓
Argo CD detects the new desired state
                ↓
Argo CD compares Git with Kubernetes
                ↓
Argo CD synchronizes the application
                ↓
Kubernetes creates or updates resources
                ↓
Argo CD reports sync and health status
```

## Argo CD Versus Traditional CI/CD

### Traditional Push Deployment

```text
CI/CD Pipeline
      ↓
Uses Kubernetes credentials
      ↓
Pushes resources into the cluster
```

### Argo CD Pull-Based GitOps

```text
Git Repository
      ↓
Argo CD inside Kubernetes
      ↓
Pulls and applies desired configuration
```

The pull-based model reduces the need to store powerful Kubernetes credentials in external CI/CD systems.

## Argo CD's Role in CI/CD

Argo CD primarily handles continuous delivery.

```text
GitHub Actions or Jenkins
 ├── Run tests
 ├── Perform security scans
 ├── Build Docker image
 ├── Push image to Amazon ECR
 └── Update image tag in GitOps repository
                 ↓
              Argo CD
                 ↓
        Deploy image to Amazon EKS
```

## Main Benefits

- Consistent Kubernetes deployments
- Faster environment recovery
- Automated drift remediation
- Clear deployment visibility
- Simplified multi-cluster management
- Strong change-control processes
- Reduced direct access to production clusters
- Easier rollback and troubleshooting
- Better separation between CI and CD
- Improved auditability and compliance

## Important Limitations

Argo CD does not normally:

- Build application source code
- Run unit tests
- Create container images
- Replace a complete CI platform
- Automatically manage application secrets without additional tooling
- Deploy non-Kubernetes infrastructure as naturally as Terraform
- Eliminate the need for Kubernetes security and governance

## Common Toolchain

```text
GitHub Actions / Jenkins → Continuous Integration
Terraform                → Infrastructure provisioning
Amazon ECR               → Container registry
Argo CD                   → Kubernetes continuous delivery
Prometheus and Grafana    → Monitoring
External Secrets          → Secret delivery
```
