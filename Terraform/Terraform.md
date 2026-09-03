<a id="top"></a>

# Terraform Study Notes — Basic to Advanced

A single reference covering Terraform from first principles through advanced,
production-grade usage, with runnable configuration examples and a
troubleshooting guide organized by topic.

## Table of Contents

1. [Introduction to Terraform](#1-introduction-to-terraform)
2. [Installation and Setup](#2-installation-and-setup)
3. [Core Concepts](#3-core-concepts)
4. [The Terraform Workflow](#4-the-terraform-workflow)
5. [Variables Deep Dive](#5-variables-deep-dive)
6. [Outputs and Locals](#6-outputs-and-locals)
7. [State Management](#7-state-management)
8. [Remote Backends](#8-remote-backends)
9. [Meta-Arguments: count, for_each, depends_on, lifecycle](#9-meta-arguments-count-for_each-depends_on-lifecycle)
10. [Expressions and Built-in Functions](#10-expressions-and-built-in-functions)
11. [Data Sources](#11-data-sources)
12. [Modules](#12-modules)
13. [Provider Configuration and Aliases](#13-provider-configuration-and-aliases)
14. [Workspaces](#14-workspaces)
15. [Provisioners (and Why to Avoid Them)](#15-provisioners-and-why-to-avoid-them)
16. [Import and Drift Detection](#16-import-and-drift-detection)
17. [Testing, Linting, and Security Scanning](#17-testing-linting-and-security-scanning)
18. [CI/CD Integration](#18-cicd-integration)
19. [Terraform Cloud and Terraform Enterprise](#19-terraform-cloud-and-terraform-enterprise)
20. [Advanced Patterns](#20-advanced-patterns)
21. [Security Best Practices](#21-security-best-practices)
22. [Troubleshooting Guide by Topic](#22-troubleshooting-guide-by-topic)
23. [CLI Command Cheat Sheet](#23-cli-command-cheat-sheet)
24. [Study Checklist](#24-study-checklist)
25. [Interview Questions](#25-interview-questions)
26. [Reference Links](#26-reference-links)

---

# 1. Introduction to Terraform

Terraform (HashiCorp) is an **Infrastructure as Code (IaC)** tool that lets you
define cloud and on-prem infrastructure in declarative configuration files,
then plan and apply changes in a repeatable, version-controlled way.

## Why Infrastructure as Code

- Infrastructure changes go through the same review process as application code.
- Environments (dev/test/stage/prod) are reproducible from the same source.
- Changes are previewed (`plan`) before they happen (`apply`).
- Infrastructure history lives in git, not in someone's memory or the console.

## Declarative vs Imperative

- **Declarative** (Terraform, CloudFormation): you describe the *desired end
  state*; the tool figures out the steps to get there.
- **Imperative** (a Bash/Python script, Ansible in most usage): you describe
  the *steps* to take.

## Terraform vs Other IaC Tools

| Tool | Style | Scope | Notes |
|---|---|---|---|
| **Terraform** | Declarative | Multi-cloud | Uses providers to talk to any API; large ecosystem |
| **AWS CloudFormation** | Declarative | AWS-only | Native AWS integration, no separate state file to manage |
| **Ansible** | Imperative (mostly) | Config management + provisioning | Agentless, better for OS/app configuration than resource lifecycle |
| **Pulumi** | Declarative | Multi-cloud | Uses real programming languages (Python, TypeScript, Go) instead of HCL |
| **Terragrunt** | Wrapper around Terraform | Multi-cloud | Adds DRY config and orchestration on top of Terraform |

## How Terraform Works

1. You write `.tf` configuration files describing resources.
2. `terraform init` downloads the providers/modules referenced.
3. `terraform plan` compares desired configuration to the current **state**
   and the real infrastructure, producing an execution plan.
4. `terraform apply` calls the relevant provider APIs to create, update, or
   destroy resources to match the plan.
5. Terraform records the result in a **state file** (`terraform.tfstate`).

[⬆ Back to top](#top)

---

# 2. Installation and Setup

## Install (Windows)

```powershell
choco install terraform
# or download the binary from developer.hashicorp.com and add it to PATH
terraform -version
```

## Install (Linux/macOS)

```bash
# macOS
brew install terraform

# Linux (apt)
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

## Recommended tooling

| Tool | Purpose |
|---|---|
| `tfenv` / `tfswitch` | Manage multiple Terraform versions per project |
| VS Code + HashiCorp Terraform extension | Syntax highlighting, formatting, validation |
| `tflint` | Linting for provider-specific mistakes |
| `checkov` / `tfsec` | Security and misconfiguration scanning |

## Minimal Project Layout

```text
project/
├── main.tf          # Primary resources
├── variables.tf      # Input variable declarations
├── outputs.tf        # Output declarations
├── providers.tf       # Provider + required_providers block
├── terraform.tfvars   # Variable values (not committed if sensitive)
└── modules/
    └── vpc/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

[⬆ Back to top](#top)

---

# 3. Core Concepts

## Terraform Block

Pins the Terraform version and declares required providers.

```hcl
terraform {
  required_version = ">= 1.7.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

## Provider

Configures a plugin that talks to an API (AWS, Azure, GitHub, Kubernetes...).

```hcl
provider "aws" {
  region = "us-east-1"
}
```

## Resource

The fundamental building block — describes one infrastructure object.

```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c101f26f147fa7fd"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

Syntax: `resource "<PROVIDER_TYPE>" "<LOCAL_NAME>" { ... }`. Reference it
elsewhere as `aws_instance.web.id`.

## Data Source

Reads existing infrastructure/data without managing it.

```hcl
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-*-x86_64"]
  }
}
```

## Variable

An input parameter for the configuration.

```hcl
variable "instance_type" {
  type    = string
  default = "t3.micro"
}
```

## Output

A value exposed after `apply`, usable by other configs, CI/CD, or the CLI.

```hcl
output "instance_public_ip" {
  value = aws_instance.web.public_ip
}
```

## Local Value

A named expression to avoid repetition (not an input, not an output).

```hcl
locals {
  name_prefix = "${var.project}-${var.environment}"
}
```

[⬆ Back to top](#top)

---

# 4. The Terraform Workflow

```bash
terraform init      # Download providers/modules, configure backend
terraform fmt        # Rewrite files to canonical formatting
terraform validate   # Check syntax and internal consistency (no API calls)
terraform plan        # Show what would change
terraform apply        # Make the changes (prompts for confirmation)
terraform destroy       # Tear down everything Terraform manages here
```

## Typical Day-to-Day Sequence

```bash
git pull
terraform init -upgrade         # only when providers/modules changed
terraform fmt -recursive
terraform validate
terraform plan -out=tfplan
# review the plan, get it peer-reviewed in a PR
terraform apply tfplan
```

## Useful Flags

```bash
terraform plan -var="environment=prod"
terraform plan -var-file="prod.tfvars"
terraform apply -auto-approve       # skips interactive confirmation — use with care in CI
terraform apply -target=aws_instance.web   # apply only one resource — use sparingly
terraform destroy -target=aws_instance.web
```

`-target` and `-auto-approve` are useful in emergencies or CI pipelines, but
routine use of `-target` is a smell — it usually means the configuration
should be split into smaller, more focused modules/states.

[⬆ Back to top](#top)

---

# 5. Variables Deep Dive

## Types

```hcl
variable "instance_count" {
  type    = number
  default = 2
}

variable "enable_monitoring" {
  type    = bool
  default = true
}

variable "availability_zones" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

variable "tags" {
  type    = map(string)
  default = { Environment = "dev" }
}

variable "server_config" {
  type = object({
    name          = string
    instance_type = string
    disk_size_gb  = number
  })
  default = {
    name          = "app-server"
    instance_type = "t3.micro"
    disk_size_gb  = 20
  }
}
```

## Validation

```hcl
variable "environment" {
  type = string

  validation {
    condition     = contains(["dev", "test", "stage", "prod"], var.environment)
    error_message = "environment must be one of: dev, test, stage, prod."
  }
}
```

## Sensitive Variables

```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```

Marking a variable `sensitive` hides its value in `plan`/`apply` output — it
is **not** encryption; the value is still stored in plaintext in the state
file unless the backend itself encrypts state (e.g., S3 with SSE-KMS).

## Providing Values (in order of precedence, highest wins)

1. `-var` or `-var-file` command-line flags
2. `*.auto.tfvars` / `*.auto.tfvars.json` (auto-loaded)
3. `terraform.tfvars` (auto-loaded)
4. `TF_VAR_<name>` environment variables
5. Variable `default` value in the declaration

```bash
export TF_VAR_db_password="s3cr3t"
terraform apply -var-file="prod.tfvars"
```

```hcl
# prod.tfvars
environment    = "prod"
instance_count = 4
```

[⬆ Back to top](#top)

---

# 6. Outputs and Locals

## Outputs

```hcl
output "vpc_id" {
  description = "ID of the created VPC"
  value       = aws_vpc.main.id
}

output "db_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

Read outputs after apply:

```bash
terraform output
terraform output vpc_id
terraform output -json > outputs.json
```

Consume another configuration's outputs via a `terraform_remote_state` data
source (see [Remote Backends](#8-remote-backends)).

## Locals

```hcl
locals {
  name_prefix = "${var.project}-${var.environment}"

  common_tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_s3_bucket" "data" {
  bucket = "${local.name_prefix}-data"
  tags   = local.common_tags
}
```

[⬆ Back to top](#top)

---

# 7. State Management

## What State Is

`terraform.tfstate` is a JSON file mapping your configuration's resources to
real-world object IDs. It is how Terraform knows what it manages, detects
drift, and computes diffs on the next `plan`. See
[§16 Detecting Drift](#16-import-and-drift-detection) for the full
detect/accept-or-revert/prevent-recurrence workflow — this section covers
the state file itself (anatomy, locking, versioning, recovery), not the
drift-handling process.

**Never edit the state file by hand.** Use `terraform state` subcommands.

## State File Anatomy

A simplified look at what's actually inside `terraform.tfstate`:

```json
{
  "version": 4,
  "terraform_version": "1.9.0",
  "serial": 27,
  "lineage": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "outputs": {
    "vpc_id": {
      "value": "vpc-0abc123",
      "type": "string"
    }
  },
  "resources": [
    {
      "mode": "managed",
      "type": "aws_instance",
      "name": "web",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 1,
          "attributes": {
            "id": "i-0123456789abcdef0",
            "ami": "ami-0c101f26f147fa7fd",
            "instance_type": "t3.micro"
          },
          "dependencies": []
        }
      ]
    }
  ]
}
```

| Field | Meaning |
|---|---|
| `version` | State file format version (an internal schema, not the Terraform version) |
| `terraform_version` | Terraform CLI version that last wrote this state |
| `serial` | Monotonically incremented on every state write — the basis for detecting a stale/conflicting write |
| `lineage` | A UUID identifying this state's history; changes only if state is fundamentally replaced (e.g., `state push` of an unrelated file) |
| `resources[].instances[].attributes` | Every attribute of the resource **as last recorded**, including secrets, in plaintext |
| `resources[].instances[].dependencies` | The dependency edges used to build the graph |

Two state files with the same `lineage` but different `serial` values are
comparable (one is simply newer); different `lineage` values mean the
backend is being asked to reconcile two unrelated histories, which is why
`terraform state push` of the wrong file is dangerous — it can silently
overwrite an unrelated lineage if you bypass the safety checks.

## State Commands

```bash
terraform state list                                   # list all resources in state
terraform state show aws_instance.web                    # show one resource's attributes
terraform state mv aws_instance.web aws_instance.web_app  # rename in state (matches a .tf rename)
terraform state rm aws_instance.web                        # stop tracking, don't destroy
terraform state pull > state-backup.json                    # download raw state
terraform state push state-backup.json                        # upload raw state (dangerous)
```

## Local State Problems

Local state (the default, a file on your machine) does not work for teams:

- No locking — two people running `apply` at once can corrupt state.
- No shared source of truth — everyone needs the same file.
- Secrets in state live unencrypted on a laptop.

This is why real projects use a [remote backend](#8-remote-backends).

## State Versioning

Versioning means every write to the state file is preserved, not just the
latest one — so a bad `apply`, an accidental `state rm`, or a corrupting
concurrent write can be undone by going back to a known-good copy.

### S3 Backend

Enable bucket versioning on the backend bucket — every `apply` writes a new
object version instead of overwriting in place:

```hcl
resource "aws_s3_bucket_versioning" "state" {
  bucket = aws_s3_bucket.state.id
  versioning_configuration {
    status = "Enabled"
  }
}
```

List and inspect prior versions:

```bash
aws s3api list-object-versions \
  --bucket company-terraform-state \
  --prefix app/prod/terraform.tfstate

aws s3api get-object \
  --bucket company-terraform-state \
  --key app/prod/terraform.tfstate \
  --version-id <VERSION_ID> \
  state-old.json
```

Pair versioning with:

- **SSE-KMS encryption** (`aws_s3_bucket_server_side_encryption_configuration`) —
  state at rest is encrypted, and every read/write is auditable via
  CloudTrail against the KMS key.
- **MFA delete** or a bucket policy denying `s3:DeleteObject`/
  `s3:DeleteObjectVersion` for anyone but a break-glass role, so a version
  history can't itself be deleted.
- **Lifecycle rules** that move old versions to cheaper storage after N days
  rather than expiring them outright — state history is small and cheap to
  keep indefinitely.

### Terraform Cloud / Enterprise

State versioning is automatic and built in — every run creates a new,
retrievable state version visible in the workspace's **States** tab, each
tagged with the run that produced it, with one-click rollback to any prior
version via the UI or API.

### Local Backend

Terraform itself keeps exactly **one** local backup automatically:
`terraform.tfstate.backup`, overwritten on every subsequent apply — this is
not real version history, just a single-step undo, and is one more reason
local state doesn't belong in a team workflow.

## Backup and Restore

### Manual, Point-in-Time Backup

Regardless of backend, you can always snapshot the current state on demand:

```bash
terraform state pull > "backups/terraform.tfstate.$(date +%Y%m%d%H%M%S)"
```

Do this before any risky operation — a bulk `state mv`/`state rm`, a backend
migration, or a manual `state push`.

### Restoring After a Bad Apply or Corruption (S3 Backend)

```bash
# 1. Identify the last known-good version
aws s3api list-object-versions \
  --bucket company-terraform-state \
  --prefix app/prod/terraform.tfstate \
  --query 'Versions[*].[VersionId,LastModified]' \
  --output table

# 2. Download it for inspection first — don't restore blind
aws s3api get-object \
  --bucket company-terraform-state \
  --key app/prod/terraform.tfstate \
  --version-id <GOOD_VERSION_ID> \
  state-restore-candidate.json

# 3. Push it back as the current state (acquires the lock, so no
#    concurrent apply can be running)
terraform state push state-restore-candidate.json

# 4. Verify — expect either no diff, or a diff you understand and intend
terraform plan
```

`terraform state push` refuses to push a state with a different `lineage`
than the currently configured backend expects unless you force it
(`-force`) — treat that refusal as a hard stop, not an obstacle to push
past, until you're certain the file you're restoring is actually meant for
this backend/configuration.

### Restoring in Terraform Cloud/Enterprise

Use the workspace's **States** tab (or the State Versions API) to select a
prior version and roll back — no manual `pull`/`push` required, and the
rollback itself is recorded in the run history.

### Recovering When State Is Gone Entirely

If no backup/version exists at all:

1. Re-create empty state in the correct backend (`terraform init`).
2. Re-establish tracking per resource with `terraform import` or an
   `import` block — `terraform plan -generate-config-out=generated.tf` can
   scaffold matching HCL for each imported resource in 1.5+.
3. Run `terraform plan` after each import batch and resolve any diff before
   moving on — a diff means the written configuration doesn't yet match the
   real resource's attributes exactly.
4. Prioritize importing resources in dependency order (network before
   compute before application) so cross-resource references resolve
   correctly as you go.

### Disaster Recovery Checklist for State

- [ ] Backend bucket/store has versioning enabled and verified (test a
      restore before you need one for real).
- [ ] State is encrypted at rest, with access restricted to the
      roles/people who need it.
- [ ] A recent `state pull` backup exists before any bulk state operation.
- [ ] The restore procedure has been rehearsed at least once, not just
      documented.
- [ ] Locking is confirmed working (a concurrent apply attempt correctly
      blocks) before relying on it in production.

## Sensitive Data in State

Every attribute of every managed resource — including passwords generated by
`random_password` or retrieved from a data source — is stored in state, in
plaintext, whether or not the source variable was `sensitive`. Treat state as
a secret and restrict/encrypt access accordingly.

[⬆ Back to top](#top)

---

# 8. Remote Backends

## S3 + DynamoDB (the classic AWS pattern)

```hcl
terraform {
  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "app/prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

- The S3 bucket stores the state file (versioned + encrypted).
- The DynamoDB table (with a `LockID` primary key) provides **state locking**
  so two `apply` runs can't collide.
- As of Terraform 1.10+/AWS provider updates, S3-native locking (via
  conditional writes) is also supported without DynamoDB — check your
  provider version before dropping the lock table.

## Bootstrapping the Backend

The backend resources (bucket, lock table) usually can't be created by the
same configuration that uses them as a backend — bootstrap them first, in
their own small configuration with local state, then migrate.

```hcl
resource "aws_s3_bucket" "state" {
  bucket = "company-terraform-state"
}

resource "aws_s3_bucket_versioning" "state" {
  bucket = aws_s3_bucket.state.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_dynamodb_table" "locks" {
  name         = "terraform-locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}
```

## Migrating Backends

```bash
# after changing the backend {} block
terraform init -migrate-state
```

## Referencing Another State's Outputs

```hcl
data "terraform_remote_state" "network" {
  backend = "s3"
  config = {
    bucket = "company-terraform-state"
    key    = "network/prod/terraform.tfstate"
    region = "us-east-1"
  }
}

resource "aws_instance" "app" {
  subnet_id = data.terraform_remote_state.network.outputs.private_subnet_id
}
```

## Other Backends

| Backend | Notes |
|---|---|
| `s3` | Most common for AWS-only shops |
| `azurerm` | Azure Storage Account container, native locking via blob leases |
| `gcs` | Google Cloud Storage, native locking |
| `remote` / `cloud` | Terraform Cloud/Enterprise — state, locking, run history, policy checks all managed for you |
| `local` | Default; fine for solo learning, not for teams |

[⬆ Back to top](#top)

---

# 9. Meta-Arguments: count, for_each, depends_on, lifecycle

## count

```hcl
resource "aws_instance" "web" {
  count         = 3
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  tags = {
    Name = "web-${count.index}"
  }
}
```

Reference: `aws_instance.web[0].id`. **Downside:** inserting/removing an item
in the middle shifts every index after it, forcing unrelated
resources to be destroyed/recreated.

## for_each (preferred over count for named resources)

```hcl
variable "buckets" {
  type    = set(string)
  default = ["logs", "backups", "artifacts"]
}

resource "aws_s3_bucket" "this" {
  for_each = var.buckets
  bucket   = "${local.name_prefix}-${each.value}"
}
```

With a map, `each.key` and `each.value` differ:

```hcl
variable "instances" {
  type = map(object({
    instance_type = string
  }))
  default = {
    web = { instance_type = "t3.micro" }
    app = { instance_type = "t3.small" }
  }
}

resource "aws_instance" "this" {
  for_each      = var.instances
  ami           = data.aws_ami.amazon_linux.id
  instance_type = each.value.instance_type

  tags = { Name = each.key }
}
```

Reference: `aws_instance.this["web"].id`. Adding/removing one key does not
affect the others — this is why `for_each` is preferred for anything beyond
throwaway identical copies.

## depends_on

Terraform infers most dependencies automatically from references. Use
explicit `depends_on` only when a dependency isn't visible in the
configuration (e.g., IAM eventual consistency, or side effects from a
provisioner).

```hcl
resource "aws_iam_role_policy" "logging" {
  # ...
}

resource "aws_lambda_function" "processor" {
  # ...
  depends_on = [aws_iam_role_policy.logging]
}
```

## lifecycle

```hcl
resource "aws_instance" "web" {
  # ...

  lifecycle {
    create_before_destroy = true
    prevent_destroy        = true
    ignore_changes          = [tags["LastDeployedBy"]]
  }
}
```

| Setting | Effect |
|---|---|
| `create_before_destroy` | New resource is created before the old one is destroyed (avoids downtime on replacement) |
| `prevent_destroy` | `terraform destroy`/replacement fails with an error — safety rail for critical resources like production databases |
| `ignore_changes` | Terraform stops trying to reconcile drift on the listed attributes (e.g., autoscaler-managed `desired_capacity`) |

[⬆ Back to top](#top)

---

# 10. Expressions and Built-in Functions

## Conditionals

```hcl
resource "aws_instance" "web" {
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"
}
```

## for Expressions

```hcl
locals {
  upper_names = [for name in var.names : upper(name)]

  name_to_length = { for name in var.names : name => length(name) }

  prod_only = [for env in var.environments : env if env == "prod"]
}
```

## Splat Expressions

```hcl
output "all_instance_ids" {
  value = aws_instance.web[*].id
}
```

## Dynamic Blocks

Generate repeated nested blocks (e.g., security group rules) from a list:

```hcl
variable "ingress_rules" {
  type = list(object({
    port        = number
    cidr_blocks = list(string)
  }))
  default = [
    { port = 443, cidr_blocks = ["0.0.0.0/0"] },
    { port = 22,  cidr_blocks = ["10.0.0.0/8"] },
  ]
}

resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = "tcp"
      cidr_blocks = ingress.value.cidr_blocks
    }
  }
}
```

## Commonly Used Functions

| Category | Functions | Example |
|---|---|---|
| String | `join`, `split`, `format`, `lower`, `upper`, `trimspace` | `format("%s-%s", var.a, var.b)` |
| Collection | `length`, `merge`, `concat`, `contains`, `keys`, `values`, `flatten` | `merge(local.common_tags, { Name = "x" })` |
| Numeric | `min`, `max`, `ceil`, `floor` | `ceil(var.count / 2)` |
| Encoding | `jsonencode`, `jsondecode`, `base64encode` | `jsonencode({ role = "admin" })` |
| Filesystem | `file`, `templatefile`, `fileexists` | `templatefile("user_data.tpl", { name = "x" })` |
| Type conversion | `tostring`, `tonumber`, `tolist`, `tomap` | `tonumber(var.port_string)` |
| IP/CIDR | `cidrsubnet`, `cidrhost` | `cidrsubnet("10.0.0.0/16", 8, 1)` |

Check any expression interactively:

```bash
terraform console
> cidrsubnet("10.0.0.0/16", 8, 1)
"10.0.1.0/24"
```

[⬆ Back to top](#top)

---

# 11. Data Sources

Data sources read information Terraform doesn't manage — existing AMIs, VPCs
created outside this config, caller identity, secrets, etc.

```hcl
data "aws_caller_identity" "current" {}

data "aws_availability_zones" "available" {
  state = "available"
}

data "aws_vpc" "existing" {
  tags = {
    Name = "shared-vpc"
  }
}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}
```

Data sources are read on every `plan`/`apply` (no state drift concept the way
resources have) — they always reflect current real-world values.

[⬆ Back to top](#top)

---

# 12. Modules

A module is a reusable, parameterized bundle of resources — anything from a
single VPC to an entire application stack.

## Module Structure

```text
modules/vpc/
├── main.tf         # resources
├── variables.tf     # inputs
├── outputs.tf         # outputs
└── README.md
```

```hcl
# modules/vpc/variables.tf
variable "cidr_block" {
  type = string
}

variable "name" {
  type = string
}
```

```hcl
# modules/vpc/main.tf
resource "aws_vpc" "this" {
  cidr_block = var.cidr_block
  tags       = { Name = var.name }
}
```

```hcl
# modules/vpc/outputs.tf
output "vpc_id" {
  value = aws_vpc.this.id
}
```

## Calling a Module

```hcl
module "network" {
  source     = "./modules/vpc"
  cidr_block = "10.0.0.0/16"
  name       = "prod-vpc"
}

resource "aws_subnet" "app" {
  vpc_id     = module.network.vpc_id
  cidr_block = "10.0.1.0/24"
}
```

## Module Sources

```hcl
# Local path
source = "./modules/vpc"

# Terraform Registry
source  = "terraform-aws-modules/vpc/aws"
version = "~> 5.0"

# Git
source = "git::https://github.com/org/repo.git//modules/vpc?ref=v1.2.0"
```

## Module Design Guidelines

- Keep modules focused (one VPC, one ECS service — not "everything").
- Expose only what callers need via `variables.tf`; keep internals private.
- Pin module `version` in production; use ranges (`~>`) deliberately.
- Document required/optional variables and outputs in a `README.md`.
- Compose small modules into environment configs rather than one giant module.

[⬆ Back to top](#top)

---

# 13. Provider Configuration and Aliases

## Multiple Regions / Accounts with the Same Provider

```hcl
provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

resource "aws_instance" "east" {
  provider      = aws
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
}

resource "aws_instance" "west" {
  provider      = aws.west
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
}
```

## Passing Providers into Modules

```hcl
module "network_west" {
  source = "./modules/vpc"
  providers = {
    aws = aws.west
  }
}
```

## Assuming a Cross-Account Role

```hcl
provider "aws" {
  region = "us-east-1"

  assume_role {
    role_arn = "arn:aws:iam::222233334444:role/terraform-execution"
  }
}
```

[⬆ Back to top](#top)

---

# 14. Workspaces

Terraform CLI workspaces let one configuration manage multiple, isolated
state files (not to be confused with Terraform Cloud "workspaces," which are
a different, larger concept).

```bash
terraform workspace list
terraform workspace new staging
terraform workspace select staging
terraform workspace show
```

```hcl
resource "aws_instance" "web" {
  instance_type = terraform.workspace == "prod" ? "t3.large" : "t3.micro"

  tags = {
    Environment = terraform.workspace
  }
}
```

## Limitations

- All workspaces share the same backend config and the same `.tf` code —
  only variable values and state differ. There's no way to give `prod` a
  different backend bucket than `dev` using CLI workspaces alone.
- For meaningfully different environments (different accounts, different
  approval flows), most teams prefer **separate directories/configurations
  per environment** (or Terraform Cloud workspaces) over CLI workspaces.

[⬆ Back to top](#top)

---

# 15. Provisioners (and Why to Avoid Them)

Provisioners run scripts on a resource at creation/destruction time. HashiCorp
calls them a **last resort** — prefer AMI baking (Packer), user data, or
configuration management (Ansible/SSM) instead, because provisioners aren't
tracked in the plan and can silently fail in ways Terraform can't reconcile.

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo systemctl start httpd",
    ]

    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("~/.ssh/id_rsa")
      host        = self.public_ip
    }
  }

  provisioner "local-exec" {
    command = "echo ${self.public_ip} >> inventory.txt"
  }
}
```

Preferred alternative — `user_data` (idempotent, visible in the plan, no SSH
needed):

```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
  user_data     = templatefile("${path.module}/user_data.tpl", { role = "web" })
}
```

[⬆ Back to top](#top)

---

# 16. Import and Drift Detection

## Importing Existing Infrastructure

Console-created ("click-ops") resources exist for real but Terraform has no
record of them. Import links an existing real-world object to a `resource`
block in state, so Terraform starts managing it going forward. **Import
never infers your HCL for you** (aside from the config-generation flag
below) — the resource block's arguments must already match the real
object's actual settings, or the next `plan` will show a diff and try to
change the resource back to whatever the (wrong) config says.

### The End-to-End Workflow

```text
1. Identify the resource and its cloud-specific import ID
   (the format is documented per resource type -- e.g., an S3 bucket's ID
   is just its name; an EC2 instance's ID is i-0123456789abcdef0; some
   resources use composite, colon-separated IDs).

2. Write (or generate) a resource block that will receive the import.

3. Run the import -- either the declarative import block or the
   imperative terraform import command.

4. Run terraform plan and read the diff carefully:
     - No diff    -> the HCL already matches reality, done.
     - Diff shown -> either update your HCL to match the real resource's
                     current settings, or apply to push the real resource
                     to match your HCL -- know which one you intend
                     before applying either way.

5. Commit the resource block (and any generated file) to version control --
   the resource isn't really under IaC management until the config is
   reviewed and merged like any other change.
```

### Import Methods

**Declarative `import` block (1.5+, preferred)** — plannable and reviewable
in a PR, and supports importing many resources in a single `plan`/`apply`:

```hcl
import {
  to = aws_instance.web
  id = "i-0123456789abcdef0"
}

resource "aws_instance" "web" {
  # must be filled in to match the real instance's actual attributes --
  # see config generation below to scaffold this automatically
}
```

**Auto-generate the matching HCL** instead of hand-writing it (1.5+):

```bash
terraform plan -generate-config-out=generated.tf
```

This writes a best-effort `resource` block for every resource named in an
`import` block, populated with the real object's current attribute values.
Review it, move it into your real `.tf` files, then re-run `plan` to
confirm it now shows zero diff.

**Imperative `terraform import` (older, still common in ad-hoc/scripted use)**:

```bash
terraform import aws_instance.web i-0123456789abcdef0
```

Requires the `resource "aws_instance" "web" {}` block to already exist
(it can start empty) before running the command — it only writes to
state, and has no `-generate-config-out` equivalent of its own.

### Example: Importing a Manually Created S3 Bucket

```hcl
# 1. Write the resource block (or leave it empty and use config generation)
resource "aws_s3_bucket" "reports" {
  bucket = "company-reports-manual"
}

# 2. Declare the import
import {
  to = aws_s3_bucket.reports
  id = "company-reports-manual"   # S3 import ID is just the bucket name
}
```

```bash
terraform plan    # review: does the written config match the real bucket's
                   # versioning, encryption, tags, etc.? Fill in any gaps.
terraform apply    # links the object in state; if the plan showed no diff,
                    # this makes no real-world changes at all
```

### Bulk Import (Many Resources at Once)

Hand-writing one `import` block per resource doesn't scale past a handful
of objects:

- **Multiple `import` blocks in one `plan`/`apply`** — still manual per
  resource, but batched into a single review instead of one-at-a-time CLI
  calls.
- **`terraform plan -generate-config-out` across many `import` blocks at
  once**, then review the generated file as a batch.
- **Terraformer** (open-source, community-maintained) — reverse-engineers
  existing cloud infrastructure into both `.tf` HCL and imported state in
  one pass, for an entire account or resource type rather than
  resource-by-resource; treat its output as a rough draft to clean up, not
  final production HCL.

```bash
# Example: bulk-importing every S3 bucket in an account with Terraformer
terraformer import aws --resources=s3 --regions=us-east-1
```

### Common Pitfalls

- **ID format is resource-specific** — don't assume it's always the name;
  check the provider's resource documentation, whose "Import" section
  states the exact ID format, including any composite/colon-separated IDs.
- **Sensitive/computed attributes won't appear in generated config** —
  e.g., a database password can't be reverse-engineered from a live
  resource since providers don't expose it back out; supply it separately
  (variable, Secrets Manager data source) after import.
- **Parent/child resource splits** — some real-world objects are actually
  managed as several Terraform resources (e.g., a security group's rules
  might be separate `aws_security_group_rule` resources) — importing only
  the parent leaves the children still invisible to Terraform.
- **Skipping the "no diff" verification** — importing and immediately
  committing without running `plan` risks the very next `apply` silently
  changing the real resource to match a subtly wrong HCL block.

## Detecting Drift

**Drift** = someone or something changed a resource outside of
Terraform (console click-ops, another tool, an auto-scaling event) —
the real infrastructure no longer matches what's recorded in
`terraform.tfstate`. Undetected drift is dangerous specifically because
the *next* `plan`/`apply` will try to silently "fix" the resource back
to the old configured value, even when the out-of-band change was
intentional. (For the state file itself — anatomy, locking, versioning,
recovery from a bad state — see [§7 State Management](#7-state-management).)

```bash
terraform plan -refresh-only        # show what changed in real infra vs state, without touching config or resources
```

`-refresh-only` surfaces drift safely, as a read-only comparison,
before a normal `plan`/`apply` would try to reconcile it.

### Accept the Drift or Revert It — Two Different Commands

| Situation | Command | Effect |
|---|---|---|
| The out-of-band change was legitimate and should become the new baseline | `terraform apply -refresh-only` | Updates *state* to match reality — does not touch the real resource |
| The out-of-band change was accidental/unauthorized and should be undone | `terraform apply` (normal) | Pushes the *configured* value back onto the real resource — reverts the drift |

Picking the wrong one either permanently accepts an unauthorized change
into your source of truth, or reverts a legitimate emergency fix
someone made by hand — know which case you're in before running either.

### At Scale: Don't Wait to Discover Drift Manually

Run `plan -refresh-only` on a schedule (a cron job in CI) and alert on
any nonzero diff, rather than waiting for someone to notice unexpected
changes during a routine `plan`. Terraform Cloud/Enterprise's paid
tiers offer this as a built-in "health assessment" feature.

### Caveat

Not every attribute is refreshable — some provider attributes are
write-only or only meaningfully known at creation time — so
refresh-based drift detection is not a 100% guarantee of catching every
out-of-band change.

### Preventing Recurrence, Not Just Cleaning Up Once

A one-time `apply -refresh-only`/`apply` fixes the drift you already
found; it doesn't stop the next one. Durable fixes:

- **Restrict console/CLI write access** to Terraform-managed resources
  via SCPs/IAM, so the out-of-band change path is closed, not just
  monitored.
- **Tagging conventions** (e.g., `ManagedBy = terraform`) that make an
  out-of-band change on a Terraform-owned resource obvious at a glance
  in the console, not just in a `plan` diff.
- **A scheduled drift-detection job** (the CI cron job above) that
  alerts proactively, instead of relying on someone stumbling onto the
  diff manually.

[⬆ Back to top](#top)

---

# 17. Testing, Linting, and Security Scanning

| Tool | Purpose |
|---|---|
| `terraform validate` | Syntax + internal consistency, no cloud calls |
| `terraform fmt -check` | Enforce canonical formatting in CI |
| `tflint` | Catches provider-specific mistakes (e.g., invalid instance type) beyond what `validate` checks |
| `checkov` | Scans HCL for security/compliance misconfigurations |
| `tfsec` | Similar security scanning, now folded into `trivy` |
| `terratest` (Go) | Writes real integration tests: apply, assert, destroy |
| `terraform test` (native, 1.6+) | Built-in test framework using `.tftest.hcl` files |

## Native `terraform test` Example

```hcl
# tests/vpc.tftest.hcl
run "vpc_has_correct_cidr" {
  command = plan

  assert {
    condition     = aws_vpc.this.cidr_block == "10.0.0.0/16"
    error_message = "VPC CIDR block did not match expected value"
  }
}
```

```bash
terraform test
```

## Example Checkov Run

```bash
checkov -d . --framework terraform
```

[⬆ Back to top](#top)

---

# 18. CI/CD Integration

## Example GitHub Actions Pipeline

```yaml
name: terraform

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.9.0

      - name: Format Check
        run: terraform fmt -check -recursive

      - name: Init
        run: terraform init

      - name: Validate
        run: terraform validate

      - name: Security Scan
        run: checkov -d . --framework terraform --quiet

      - name: Plan
        run: terraform plan -out=tfplan

      - name: Apply
        if: github.ref == 'refs/heads/main'
        run: terraform apply -auto-approve tfplan
```

## Example AWS CodeBuild `buildspec.yml`

```yaml
version: 0.2

phases:
  install:
    commands:
      - terraform version
  pre_build:
    commands:
      - terraform init
      - terraform fmt -check
      - terraform validate
      - checkov -d . --framework terraform
  build:
    commands:
      - terraform plan -out=tfplan

artifacts:
  files:
    - tfplan
```

## Pipeline Best Practices

- Run `plan` on every pull request; require human review of the plan output.
- Gate `apply` on production behind manual approval.
- Store state remotely with locking (never rely on a CI runner's local disk).
- Pin the Terraform and provider versions used in CI to match local dev.
- Never print secrets — mark sensitive outputs/variables `sensitive = true`.

[⬆ Back to top](#top)

---

# 19. Terraform Cloud and Terraform Enterprise

Terraform Cloud and Terraform Enterprise are HashiCorp's managed control
planes on top of open-source ("Core") Terraform — same HCL, same
providers, same state model, but with a shared backend for remote
execution, collaboration, and governance instead of running `plan`/
`apply` from individual laptops or a bare CI runner.

> **Naming note**: HashiCorp rebranded Terraform Cloud as **HCP Terraform**
> in February 2024. Terraform Enterprise kept its name as the self-hosted
> product. Job postings, docs, and interviewers may still say either
> "Terraform Cloud" or "HCP Terraform" interchangeably — they're the same
> product.

## Shared Feature Set (Both Products)

| Feature | What It Does |
|---|---|
| **Workspaces** | Each maps to a working directory + variable set + state file — roughly a persistent CI job scoped to one configuration/environment. |
| **Remote execution** | `plan`/`apply` run on HashiCorp-managed (TFC) or customer-managed (TFE) infrastructure, not a laptop — consistent environment, no "works on my machine." |
| **VCS-driven runs** | A workspace auto-triggers a plan on every commit/PR against a connected GitHub/GitLab/Bitbucket/Azure DevOps repo; can auto-apply on merge to main. |
| **Remote state management** | Built-in state locking, versioning, and encryption — no S3 bucket/DynamoDB table to provision and secure yourself. |
| **Sentinel / OPA policy-as-code** | Block a `plan`/`apply` that violates an organizational policy (e.g., "no public S3 buckets," "every resource must have a `CostCenter` tag") before it ever runs. |
| **Private Module Registry** | Internal, versioned module sharing across teams, with usage examples and a browsable UI, same experience as the public registry. |
| **Run Triggers / Run Tasks** | Chain workspaces (e.g., apply the VPC workspace before the app workspace) or call out to external systems (Snyk, Checkov, custom webhooks) as a required check in the run pipeline. |
| **Teams and RBAC** | Fine-grained permissions per workspace (plan-only, apply, admin) mapped to teams, not just all-or-nothing API tokens. |
| **Cost Estimation** | Shows the estimated monthly cost delta of a plan before it's applied (cloud-provider dependent). |
| **Variable Sets** | Share a common set of variables (e.g., provider credentials) across many workspaces without copy-pasting into each one. |
| **Notifications** | Send run status to Slack, email, or a generic webhook. |

## Deployment Model — the Actual Difference

| Aspect | Terraform Cloud (HCP Terraform) | Terraform Enterprise |
|---|---|---|
| **Hosting** | Fully managed SaaS, run by HashiCorp | Self-hosted — installed in the customer's own VPC/datacenter (VM, Docker, or Kubernetes/Helm) |
| **Network isolation / data residency** | Runs in HashiCorp's infrastructure; private networking to customer resources requires **HCP Terraform Agents** | Runs entirely inside the customer's network; can be fully **air-gapped** (no outbound internet) — common requirement in regulated/government environments |
| **Pricing model** | Per-resource-under-management (RUM) subscription; **Free tier** available for small teams | License-based enterprise agreement; no free tier, typically higher floor cost |
| **Upgrade cadence** | Continuous, automatic — HashiCorp ships updates, customer takes no action | Customer controls when to apply new releases — needed where change control processes require scheduled maintenance windows |
| **SSO/SAML** | Available on higher paid tiers (Business) | Included, since the product is licensed at the "enterprise" tier by definition |
| **Audit logging** | Business tier and above | Included |
| **Compliance boundary** | Inherits HashiCorp's SOC 2 / compliance posture as a shared responsibility | Inherits the *customer's own* infrastructure compliance boundary — the deciding factor for FedRAMP, air-gapped, or strict data-sovereignty requirements |
| **Support** | Tiered by plan (community → premium) | Premium enterprise support bundled in |
| **Typical adopter** | Most organizations — fastest to start, zero infrastructure to maintain | Regulated industries (finance, government, healthcare), air-gapped networks, or orgs with a hard data-residency requirement that rules out SaaS |

## Terraform Cloud (HCP Terraform) Pricing Tiers

| Tier | Who It's For |
|---|---|
| **Free** | Individuals/small teams — remote state, remote runs, VCS integration, up to a limited number of resources under management |
| **Standard** | Small-to-mid teams needing team management and more resources under management |
| **Plus** | Larger orgs needing Sentinel policy-as-code, SSO, audit logging, and higher scale |
| *(Terraform Enterprise)* | Self-hosted equivalent of the top tier, licensed separately, deployed on-prem |

## HCP Terraform Agents (Bridging SaaS to Private Networks)

Since HCP Terraform's execution environment lives in HashiCorp's cloud,
reaching a provider endpoint that's only reachable privately (an
internal vCenter API, a private VPC with no public exposure) needs a
lightweight **agent** installed inside that private network — it polls
outward for run jobs so no inbound firewall rule into the private
network is required. Terraform Enterprise doesn't need this because the
whole control plane already runs inside the private network.

```hcl
# Workspace configured to execute via an agent pool instead of
# HCP Terraform's own default execution environment
terraform {
  cloud {
    organization = "my-org"
    workspaces {
      name = "app-prod"
    }
  }
}
```

```hcl
# Agent pool assignment is set at the workspace level in the UI/API,
# not in HCL — the workspace's "Execution Mode" is set to "Agent" and
# bound to a named agent pool that has agents polling from inside the
# private network.
```

## Decision Guide

```text
Choose HCP Terraform (SaaS) when:
  - You want to be running in minutes with no infrastructure to operate.
  - Your compliance posture allows a third-party-hosted control plane.
  - Team size/usage fits comfortably in Free/Standard/Plus pricing.

Choose Terraform Enterprise (self-hosted) when:
  - Regulatory/compliance requirements mandate the control plane stays
    inside your own network (FedRAMP, air-gapped, strict data residency).
  - You need full control over upgrade timing for change-control reasons.
  - You're already operating the infrastructure to host and patch it
    (Kubernetes cluster, VM fleet) and have the ops capacity to do so.
```

## Example Configuration (Same Block for Either — TFE Adds a `hostname`)

```hcl
# HCP Terraform (SaaS) — default hostname, omitted
terraform {
  cloud {
    organization = "my-org"
    workspaces {
      name = "app-prod"
    }
  }
}
```

```hcl
# Terraform Enterprise (self-hosted) — points at the customer's own
# TFE instance instead of HashiCorp's SaaS endpoint
terraform {
  cloud {
    hostname     = "tfe.internal.company.com"
    organization = "my-org"
    workspaces {
      name = "app-prod"
    }
  }
}
```

[⬆ Back to top](#top)

---

# 20. Advanced Patterns

## Environment Layout: Directory-per-Environment

```text
environments/
├── dev/
│   ├── main.tf        # calls shared modules with dev-sized inputs
│   └── backend.tf       # dev state key
├── stage/
│   ├── main.tf
│   └── backend.tf
└── prod/
    ├── main.tf
    └── backend.tf

modules/
├── vpc/
├── ecs-service/
└── rds/
```

Each environment is a separate state file and separate `terraform apply`,
sharing the same versioned modules — this avoids the CLI-workspace limitation
of sharing one backend/config across environments.

## Terragrunt (DRY Wrapper)

Terragrunt keeps backend/provider config in one place and generates it for
every environment, reducing copy-paste across `environments/*/backend.tf`:

```hcl
# terragrunt.hcl
remote_state {
  backend = "s3"
  config = {
    bucket = "company-terraform-state"
    key    = "${path_relative_to_include()}/terraform.tfstate"
    region = "us-east-1"
  }
}
```

## Zero-Downtime Replacement Pattern

```hcl
resource "aws_launch_template" "app" {
  name_prefix   = "app-"
  image_id      = data.aws_ami.app.id
  instance_type = "t3.small"

  lifecycle {
    create_before_destroy = true
  }
}
```

## Conditional Resource Creation

```hcl
variable "create_bastion" {
  type    = bool
  default = false
}

resource "aws_instance" "bastion" {
  count         = var.create_bastion ? 1 : 0
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
}
```

## Managing Secrets Without Storing Them in Code

```hcl
data "aws_secretsmanager_secret_version" "db" {
  secret_id = "prod/db/password"
}

resource "aws_db_instance" "main" {
  password = data.aws_secretsmanager_secret_version.db.secret_string
}
```

The password still ends up in state — combine with an encrypted, access
controlled backend (see [State Management](#7-state-management)).

[⬆ Back to top](#top)

---

# 21. Terraform Security Best Practices

- Store state remotely, encrypted (SSE-KMS on S3), with access restricted by
  IAM to the roles/people who need it.
- Enable state locking so concurrent applies can't corrupt state.
- Never commit `*.tfvars` files containing secrets, or `.terraform/` (add to
  `.gitignore`).
- Use `sensitive = true` on variables/outputs that hold secrets.
- Pull secrets from Secrets Manager/Parameter Store/Vault at apply time
  instead of hard-coding them.
- Apply least-privilege IAM to the role/user that runs Terraform — scope to
  only the resource types the configuration actually manages.
- Require pull-request review and a passing `plan` before any `apply` reaches
  production.
- Run `checkov`/`tfsec` in CI and fail the build on high-severity findings.
- Use `prevent_destroy` on irreplaceable resources (production databases,
  state buckets themselves).
- Separate production credentials/roles from non-production; require manual
  approval before production applies.

[⬆ Back to top](#top)

---

# 22. Troubleshooting Guide by Topic

## Authentication and Provider Errors

**`Error: error configuring Terraform AWS Provider: no valid credential sources found`**
- Check `aws configure list` / `AWS_PROFILE` / `AWS_ACCESS_KEY_ID` env vars.
- If using `assume_role`, confirm the trust policy allows your identity.

**`Error: InvalidClientTokenId` / `AccessDenied`**
- Credentials are present but wrong/expired, or the IAM policy lacks the
  action being called. Check `aws sts get-caller-identity` matches the
  account/role you expect.

## State Locking Errors

**`Error: Error acquiring the state lock ... ConditionalCheckFailedException`**
- Another `apply` is genuinely running — wait for it to finish.
- If a previous run crashed and left a stale lock:
  ```bash
  terraform force-unlock <LOCK_ID>
  ```
  Only do this after confirming no other process is actually running —
  force-unlocking during a real concurrent apply can corrupt state.

## Corrupt or Invalid State File

**`Error: Failed to read state file` / "state file is invalid JSON" / unexpected parse error**
- The file itself is truncated or malformed — typically caused by a killed
  process mid-write on a local backend, a manual hand-edit that broke JSON
  syntax, or a disk-full/interrupted upload on a remote backend.
- Recovery steps:
  1. **Preserve what's there first**, even if it looks broken — don't
     delete or overwrite it:

     ```bash
     terraform state pull > corrupt-state-backup.json
     # or, for a local backend, just cp terraform.tfstate
     ```

  2. Confirm it's genuinely invalid, not a different error being
     misreported: `jq . terraform.tfstate` (a real parse error means jq
     also fails).
  3. Restore the last known-good version from backend versioning (S3
     object version, or the TFC/TFE workspace **States** tab) — see the
     full restore procedure in [§7 State Management](#7-state-management).
  4. If no backup/version exists at all, rebuild state via
     `terraform import` / `import` blocks — see
     [§7 Recovering When State Is Gone Entirely](#7-state-management).

**`Error: state snapshot was created by Terraform vX.Y.Z, which is newer than current vA.B.C`**
- Someone (often CI, running a newer pinned version) wrote state with a
  newer Terraform CLI than the one you're running locally; the state
  format can add fields between versions that an older CLI won't
  understand and refuses to touch, to avoid silently dropping data.
- Fix: upgrade your local CLI to match or exceed the version named in the
  error (`tfenv install X.Y.Z`, or align with whatever version CI has
  pinned) — don't try to force an older CLI to downgrade/rewrite a
  newer-format state.

**`Error: state data in S3 does not have the expected content` (checksum/etag mismatch)**
- The S3 object was modified outside Terraform's normal write path — a
  manual console edit, or a second tool/process writing to the same key.
- Pull the object directly (`aws s3api get-object`) and inspect it before
  deciding whether to restore a prior version or validate and
  `terraform state push` a corrected copy.

A few general principles apply to any state corruption:

- Always pull/archive the current file *before* attempting a fix — even a
  suspect state is a useful diff target against whatever you restore, and
  you may need it to figure out exactly what changed.
- Never hand-edit `terraform.tfstate` to patch JSON syntax and push it
  back without running `terraform plan` against the result — a
  syntactically valid but semantically wrong state is worse than an
  error, because Terraform will silently act on incorrect data instead of
  refusing to proceed.
- A stuck lock file is not the same problem as a corrupt state file —
  don't reach for `force-unlock` (see [State Locking Errors](#state-locking-errors)
  above) when the actual issue is the state content itself.

## Plan/Apply Errors

**`Error: creating ... : ... already exists`**
- The real resource exists but isn't in state (created manually, or state was
  lost/reset). Import it:
  ```bash
  terraform import aws_s3_bucket.data existing-bucket-name
  ```

**`Error: Cycle: ...`**
- A dependency loop, usually from `depends_on` pointing both directions or
  resources referencing each other's attributes circularly. Remove the
  unneeded explicit `depends_on`; let Terraform infer the dependency graph
  from references where possible.

**`Error: Provider produced inconsistent final plan` / "inconsistent result after apply"**
- Usually a provider bug or a resource whose value is only known after
  creation being used somewhere Terraform expected stability. Try upgrading
  the provider version; check the provider's GitHub issues.

**Resource replaced unexpectedly ("forces replacement")**
- Run `terraform plan` and read the `# forces replacement` annotation — it
  names the exact attribute. Common causes: changing an immutable attribute
  (e.g., `availability_zone` on some resource types), or a computed value
  that isn't actually stable across applies.

## Drift and State Mismatches

**Plan shows changes you didn't make**
- Someone/something modified the resource outside Terraform. Run
  `terraform plan -refresh-only` to see exactly what drifted, then decide
  whether to accept it (`apply -refresh-only`) or revert it (`apply` normally
  to push your configuration's value back).

**`Error: Resource already managed by Terraform`**
- Two `resource` blocks (often across a refactor/module split) claim the same
  real object. Use `terraform state mv` to relocate the object in state
  instead of creating a duplicate `resource` block.

## Module Errors

**`Error: Module not installed` after pulling changes**
- Someone added/changed a module `source`. Run:
  ```bash
  terraform init -upgrade
  ```

**`Error: Unsupported argument` inside a module call**
- The module version changed its variables. Check the module's
  `variables.tf`/CHANGELOG and pin `version` explicitly going forward.

## Performance Issues

- **Slow `plan`/`refresh` on a large state**: split the configuration into
  smaller states (per environment, per layer — network/data/app) so each
  `plan` only has to refresh a subset of resources.
- **`-parallelism=n`**: lower it (default 10) if you're hitting API rate
  limits; raise it cautiously if the provider/API can handle more concurrent
  calls.

## General Debugging

```bash
export TF_LOG=DEBUG          # or TRACE for maximum verbosity
export TF_LOG_PATH=./terraform.log
terraform plan
```

Set `TF_LOG` back to unset (or `TF_LOG=OFF`) afterward — DEBUG/TRACE logs can
contain sensitive values and are very large.

[⬆ Back to top](#top)

---

# 23. CLI Command Cheat Sheet

```bash
# Lifecycle
terraform init                 # download providers/modules, configure backend
terraform init -upgrade          # also upgrade providers/modules to latest allowed version
terraform init -migrate-state      # move state after a backend config change
terraform fmt -recursive             # format all .tf files
terraform validate                     # syntax + internal consistency check
terraform plan -out=tfplan               # preview + save a plan file
terraform apply tfplan                     # apply a saved plan
terraform apply -auto-approve                # apply without interactive confirmation
terraform destroy                              # tear down everything in this state

# State
terraform state list
terraform state show <resource>
terraform state mv <old> <new>
terraform state rm <resource>
terraform force-unlock <lock_id>

# Inspection
terraform show                    # human-readable current state
terraform show -json tfplan         # machine-readable plan (for policy checks/CI)
terraform output
terraform graph | dot -Tpng > graph.png   # visualize the dependency graph

# Workspaces
terraform workspace list
terraform workspace new <name>
terraform workspace select <name>

# Import / drift
terraform import <resource_address> <real_id>
terraform plan -refresh-only
terraform apply -refresh-only

# Debugging
TF_LOG=DEBUG terraform plan
```

[⬆ Back to top](#top)

---

# 24. Study Checklist

- [ ] Explain declarative vs imperative IaC, and where Terraform fits vs
      CloudFormation/Ansible/Pulumi.
- [ ] Write a configuration with providers, resources, variables, outputs,
      and locals from scratch.
- [ ] Explain what the state file is for and why it must be remote + locked
      for team use.
- [ ] Set up an S3 + DynamoDB (or S3-native locking) backend.
- [ ] Use `count` vs `for_each` correctly and explain the index-shift problem
      with `count`.
- [ ] Write a module with its own variables/outputs and call it with a
      pinned version.
- [ ] Use `dynamic` blocks to generate nested blocks from a list/map.
- [ ] Import an existing resource and explain the difference between the
      `import` block and `terraform import` CLI command.
- [ ] Detect and explain drift using `plan -refresh-only`.
- [ ] Explain `lifecycle` options: `create_before_destroy`,
      `prevent_destroy`, `ignore_changes`.
- [ ] Explain why provisioners are a last resort and what to use instead.
- [ ] Diagnose a state lock error and safely resolve it.
- [ ] Diagnose an unexpected "forces replacement" in a plan.
- [ ] Describe a secure CI/CD pipeline for Terraform (fmt, validate, scan,
      plan, manual approval, apply).
- [ ] Explain what Terraform Cloud/Enterprise adds over open-source Terraform
      (remote execution, Sentinel/OPA, private registry).

[⬆ Back to top](#top)

---

# 25. Terraform Interview Questions

## Basic

**1. What is Terraform, and how does it differ from a configuration management tool like Ansible?**
Terraform is a declarative Infrastructure as Code tool built around a
provider plugin architecture: Terraform core talks to each provider binary
over gRPC, negotiates a resource schema, and uses that schema to build a
dependency graph and compute a diff between desired configuration and
tracked state. Ansible is fundamentally different in architecture — it's
agentless and push-based, executing an ordered list of tasks over
SSH/WinRM against hosts named in an inventory, with no persistent record of
"desired end state" to diff against. That has real consequences: Terraform
can tell you *before* you act exactly what will change and can refuse to
proceed if reality has drifted from its state; Ansible playbooks are
generally idempotent by convention (each module tries to only act if
necessary) but there's no independent state file underwriting that
guarantee. In practice the two are complementary rather than competing:
Terraform provisions the resource (VPC, EC2 instance, RDS instance), and
Ansible/SSM/cloud-init handles what happens *inside* it — package
installation, config files, service state — because re-running a full
Terraform apply is not the idiomatic way to enforce configuration drift
inside a running OS.

**2. What is the difference between Terraform and AWS CloudFormation?**
Beyond "multi-cloud vs AWS-only," the operationally significant differences
are: (1) **rollback semantics** — CloudFormation automatically rolls back a
stack to its last known-good state on a failed update; Terraform stops
mid-apply, leaves whatever succeeded in place, and requires you to fix
forward or manually intervene, so partial applies are a real operational
concern you must plan for (idempotent re-apply, `-target` as an escape
hatch). (2) **State ownership** — CloudFormation's "state" is managed
internally by AWS and isn't a file you can lose or corrupt; Terraform's
state is an artifact you are responsible for securing, locking, and backing
up. (3) **Native drift detection** — CloudFormation has a built-in
`detect-stack-drift` API; Terraform's equivalent (`plan -refresh-only`) is a
plan-time operation you have to run and interpret yourself. (4) **Change
previews** — CloudFormation change sets and `terraform plan` serve the same
purpose, but Terraform's plan is generally considered more readable and
attribute-precise. (5) **Multi-account/region fan-out** — CloudFormation
StackSets natively deploy across accounts/regions; Terraform needs provider
aliases, separate state per account, or a wrapper like Terragrunt to achieve
the same thing.

**3. What is a provider?**
A provider is a separate, versioned binary that implements the Terraform
Plugin Protocol (now built on the Plugin Framework, formerly SDKv2) and
exposes a set of resource and data source schemas. Terraform core doesn't
know anything AWS-, Azure-, or Kubernetes-specific — at `init` time it
downloads the requested provider binary (per the `required_providers`
constraint) and launches it as a subprocess; all subsequent CRUD operations
for that provider's resources happen via gRPC calls into that binary, which
in turn calls the underlying cloud API (e.g., AWS's SDK). Provider versions
are locked precisely in `.terraform.lock.hcl` — a file that should be
committed to version control so every teammate and CI run resolves to the
exact same provider build, not just something matching the version
constraint.

**4. What is the Terraform state file, and why does it matter?**
It's a JSON document containing, per resource: its provider-specific
attributes as last known (including sensitive ones, in plaintext), its
dependency edges, and metadata — notably a `lineage` (a UUID identifying
"this state's history") and a `serial` number incremented on every write.
The serial/lineage pair is what lets a locking backend detect a stale write
attempt. State is what makes `plan` fast and precise — Terraform diffs
*configuration vs. state*, then optionally *refreshes* state against real
infrastructure, rather than having to reverse-engineer everything from the
provider API on every run. Losing it means Terraform has no record of what
it manages; corruption (two concurrent unlocked applies, a bad manual edit)
can produce a state that references resources that no longer exist or is
missing ones that do, either of which causes incorrect plans until repaired.

**5. What's the difference between `terraform plan` and `terraform apply`?**
`plan` refreshes (by default) its view of real infrastructure, diffs that
against configuration, and prints a proposed set of create/update/destroy
actions — it makes no API calls that mutate infrastructure. `apply` executes
those actions. The subtlety worth knowing: if you run bare `apply` without
`-out=tfplan`, Terraform computes a *fresh* plan internally right before
applying it, which means infrastructure could have changed between when you
read a plan on screen and when apply executes it (a TOCTOU gap) — using
`terraform plan -out=tfplan` followed by `terraform apply tfplan` closes that
gap by applying the *exact* saved plan, refusing if the state has moved on
since.

**6. What happens if you delete the state file?**
Terraform loses all record of what it manages. The next `plan` treats every
resource in configuration as new, which for most resources produces
"already exists" errors from the provider (since the real infrastructure is
still there) rather than silently duplicating everything — but for
resources without a global uniqueness constraint, it genuinely can create
duplicates. Recovery paths: restore a previous version of the state file
(this is the strongest argument for enabling versioning on an S3 state
bucket or using Terraform Cloud, which versions state automatically), or
re-establish tracking resource-by-resource with `terraform import` /
`import` blocks — the latter is faster in 1.5+ since
`-generate-config-out` can scaffold the matching HCL for you, though
generated config typically needs manual cleanup.

**7. What is idempotency, and how does Terraform achieve it?**
Applying the same configuration repeatedly converges to, and then stays at,
the same real-world state without unintended side effects on subsequent
runs. Terraform achieves this structurally — via schema-aware diffing
between desired config and tracked state — but idempotency in practice also
depends on the *provider's* implementation being correct. It's not
uncommon to hit provider bugs that produce a "perpetual diff": a resource
that shows a planned change every single run even though nothing in
configuration changed, usually because the provider is comparing against a
normalized/default value the API silently applies. Recognizing that pattern
(a diff that never resolves after repeated applies) is a strong signal to
check the provider's GitHub issues rather than assume your configuration is
wrong.

## Intermediate

**8. What's the difference between `count` and `for_each`?**
`count` indexes resources numerically (`aws_instance.web[0]`,
`aws_instance.web[1]`); removing or inserting an item anywhere but the end
of the list shifts every subsequent index, and Terraform treats a shifted
index as "destroy the old resource at that index, create a new one" even
though conceptually nothing about that particular instance changed —
that's the classic count pitfall in interviews. `for_each` keys resources
by a stable string (a map key, or a member of a `set(string)`), so identity
is tied to the key rather than position — removing "app" from a map removes
exactly the "app" resource and leaves every other key's resource untouched.
The trade-off: `for_each` requires the keys to be *known at plan time* —
you can't `for_each` over a value derived from an attribute of a resource
that doesn't exist yet (you'll hit "Invalid for_each argument: ... depends
on resource attributes that cannot be determined until apply"), whereas
`count` can sometimes tolerate a computed number more easily. Use `count`
only for genuinely interchangeable, disposable copies with no meaningful
identity (e.g., a fixed number of NAT gateways); default to `for_each` for
anything you'd ever refer to by name.

**9. When would you use a data source instead of a resource?**
When you need to read something Terraform does not own the lifecycle of —
an existing VPC created by another team/config, the latest AMI ID, the
caller's account ID via `aws_caller_identity`. The operational subtlety:
data sources are (re-)read on essentially every `plan`, which at scale can
contribute meaningfully to plan time and to provider API rate limits.
Also, a data source that reads a resource created *earlier in the same
apply* needs either an implicit dependency (referencing an attribute of
that resource) or an explicit `depends_on` on the data block — otherwise
Terraform may try to read it before it exists, since data sources don't
automatically wait the way resource-to-resource references do unless the
reference is actually present in the data source's arguments.

**10. What is a module, and why use one?**
A parameterized, reusable bundle of resources with its own input/output
contract. Beyond avoiding copy-paste, modules are usually the unit at which
teams draw **blast-radius boundaries** — a well-factored module maps to
something you'd reasonably want to plan, review, and roll out
independently. The design trade-off to watch for in an interview: modules
that expose too many outputs (or accept too many "escape hatch" variables)
become a leaky abstraction that's barely different from inlining the
resources — the value of a module is in encoding an opinionated, correct
pattern, not just wrapping resources 1:1. Modules should be
semantically versioned when shared (via a registry or Git tag), and pinned
explicitly (`version = "~> 5.0"` or a Git `?ref=v1.2.0`) in every caller so
an upstream module change can't silently alter every consumer's plan.

**11. How do you manage secrets in Terraform?**
Pull them at apply time from Secrets Manager/Parameter Store/Vault via a
data source instead of hard-coding values, and mark variables/outputs that
carry them `sensitive = true`. It's important to be precise about what
`sensitive` actually does: it suppresses the value from CLI/plan output —
it is **not** encryption, and the value is still written in plaintext into
the state file. That means real secret protection comes from the backend:
encrypt state at rest (SSE-KMS on an S3 backend, or Terraform
Cloud/Enterprise's built-in encryption), restrict who/what can read it via
IAM, and treat any exported plan file (`tfplan`) as equally sensitive, since
a saved plan can also embed the same values — don't leave `tfplan` artifacts
lying around in CI logs or unprotected build caches. For CI credentials
themselves, prefer short-lived, federated credentials (OIDC from
GitHub Actions/GitLab into an AWS IAM role) over long-lived static access
keys.

**12. Explain remote state and why it matters for teams.**
Remote state stores `terraform.tfstate` in a shared, typically versioned
location (S3, Terraform Cloud, Azure Storage, GCS) instead of a file on one
person's disk, so every teammate and CI job reads and writes the same
source of truth, gated by locking. A second, less obvious reason remote
state matters: it enables **cross-stack references** via
`terraform_remote_state`, letting a downstream configuration (e.g., an
application stack) read a `vpc_id` or `subnet_ids` output from an upstream
network stack without duplicating that data. The trade-off to be aware of:
this creates an implicit coupling between stacks — renaming or removing an
output in the upstream state silently breaks every downstream config that
references it, with no compile-time warning, only a `plan`-time error. Some
teams deliberately avoid `terraform_remote_state` for exactly this reason
and instead publish cross-stack values to SSM Parameter Store/SSM
Parameters or a similar loosely-coupled store.

**13. What is state locking, and why is it needed?**
A mechanism that ensures only one write to state happens at a time. On the
classic AWS backend, this was implemented via a DynamoDB table with a
`LockID` hash key: Terraform performs a conditional put that fails if a lock
item already exists, and cleans it up (deletes the item) on completion.
Newer Terraform/AWS-provider versions also support S3-native locking using
conditional writes (`If-None-Match`) directly against the state object,
removing the need for a separate DynamoDB table. Without locking, two
concurrent `apply` runs can both read the same starting state, both write
their own updated version, and the second write silently clobbers the
first's changes — producing a state file that no longer matches either
intended outcome, and potentially "losing" resources Terraform created but
never recorded.

**14. What's the difference between `variables.tf`, `terraform.tfvars`, and `TF_VAR_*` environment variables?**
`variables.tf` *declares* a variable — its type, default, description, and
validation rules; it never supplies a runtime value on its own. Values are
supplied from multiple possible sources, and Terraform documents an exact
precedence order (later overrides earlier): environment variables
(`TF_VAR_<name>`) are the lowest-precedence explicit source, then
`terraform.tfvars`/`terraform.tfvars.json` (auto-loaded), then
`*.auto.tfvars`/`*.auto.tfvars.json` files in alphabetical order
(auto-loaded), then `-var` and `-var-file` flags on the command line, in the
order given, with later flags winning. If none of these provide a value,
the variable's declared `default` is used, and if there's no default and no
supplied value, Terraform prompts interactively (or fails, in
non-interactive contexts like CI). `TF_VAR_*` is most useful for injecting
secrets in CI without writing them to a file on disk.

**15. What is the `lifecycle` block used for?**
Customizing how Terraform manages create/update/destroy behavior for a
specific resource: `create_before_destroy` (provision the replacement before
destroying the original, to avoid downtime on a forced replacement),
`prevent_destroy` (hard-fail any plan that would destroy this resource — a
safety rail, though note it still blocks *replacement*-driven destroys, not
just explicit `destroy` calls), and `ignore_changes` (tell Terraform to stop
reconciling drift on specific attributes it doesn't actually control, e.g.
an Auto Scaling Group's `desired_capacity` when a separate scaling policy
manages it). Less commonly asked but worth knowing for a senior interview:
`precondition`/`postcondition` custom condition blocks (validate an
assumption about a resource before/after apply) and `replace_triggered_by`
(force replacement when a *referenced* resource/attribute changes, even if
this resource's own arguments didn't).

**16. Explain `depends_on` vs implicit dependencies.**
Terraform infers dependencies automatically whenever one resource's
arguments reference another resource's attribute — that reference is both a
value flow and an ordering constraint. `depends_on` is a purely
*ordering* constraint with no value flow, for the cases where a real
dependency exists but nothing in the configuration's arguments expresses
it — classic examples are IAM permission propagation delays (the role
exists per the API response, but isn't consistently usable for a few
seconds) or ordering relative to a provisioner's side effect. It's worth
calling out the cost: `depends_on` (and any manufactured dependency) forces
strictly sequential execution between those nodes, which can reduce how
much of the graph Terraform can execute in parallel — overusing it
measurably slows down large applies. A common, more surgical alternative for
the IAM-propagation case specifically is a `time_sleep` resource with an
explicit `depends_on`, rather than blanket-ordering unrelated resources.

## Advanced

**17. How would you handle multi-region or multi-account deployments?**
Within one configuration and one AWS account, use provider aliases
(`provider "aws" { alias = "west"; region = "us-west-2" }`) and pass the
aliased provider into resources directly or into modules via the
`providers = { aws = aws.west }` map. The thing worth flagging in an
advanced interview: provider configuration (including aliases) **cannot be
generated dynamically** — you cannot `for_each` or `count` over a list of
regions to produce N provider aliases; the set of providers a configuration
uses must be static in the code. For genuinely separate accounts (not just
regions), the practical pattern is separate state per account — via
distinct backend keys/workspaces, `assume_role` per account, or a
Terragrunt layer that generates the boilerplate per account/region
combination — rather than trying to force one configuration to fan out
across account boundaries.

**18. What's the difference between the `import` block and the `terraform import` CLI command?**
The `import` block (1.5+) is declarative and lives in your configuration:
it shows up as a proposed action in `terraform plan` *before* anything
happens, can be reviewed/approved like any other planned change, and — with
`terraform plan -generate-config-out=generated.tf` — can scaffold the
matching `resource` block for you, saving the tedious "write the config to
match reality exactly" step. The older `terraform import` CLI command is
imperative and one-off: it immediately links a resource address to a real
object ID with no plan/review step, and you must have *already* written the
matching `resource` block, because import only populates state — it never
generates configuration. A subtlety that trips people up either way: if the
resource block's arguments don't exactly match the imported object's real
attributes, the very next `plan` will show a diff trying to "correct" the
real resource to match your (wrong) config — so import is only half done
until that first post-import plan comes back clean.

**19. How do you detect and handle drift?**
`terraform plan -refresh-only` refreshes state against real infrastructure
and shows exactly what changed, without touching configuration or real
resources — the safe first step whenever a normal `plan` shows unexpected
changes. From there: `terraform apply -refresh-only` accepts the drift into
state (useful when the out-of-band change was legitimate and should become
the new baseline), or a normal `apply` pushes the *configured* value back
onto the real resource (useful when the drift was accidental/unauthorized).
At scale, teams often run `plan -refresh-only` on a schedule (a cron job in
CI) and alert on any nonzero diff, rather than waiting to discover drift
the next time someone happens to run a real `plan`. Terraform Cloud/
Enterprise's paid tiers also offer this as a built-in "health assessment"
feature. Caveat worth knowing: not every attribute is refreshable — some
provider attributes are write-only or only meaningfully known at creation
time, so refresh-based drift detection isn't a 100% guarantee of catching
every out-of-band change.

**20. What is Sentinel/OPA, and how does it relate to Terraform?**
Policy-as-code frameworks that evaluate a Terraform plan's structured
output (Sentinel operates on Terraform Cloud/Enterprise's internal plan
representation; OPA/`conftest` typically evaluates `terraform show -json`
of a plan) against organizational rules before an apply is allowed to
proceed — e.g., "no security group may allow 0.0.0.0/0 on port 22," "every
resource must have a `CostCenter` tag." Sentinel policies have three
enforcement levels: **advisory** (warn only), **soft-mandatory** (block, but
can be overridden by an authorized user), and **hard-mandatory** (block,
no override) — knowing this distinction signals real experience with
Terraform Cloud/Enterprise governance rather than just having heard the
term. These checks run as a required gate between `plan` and `apply`,
functioning like a policy-specific CI check that has full visibility into
the exact plan about to be applied, not just the source HCL.

**21. How would you structure Terraform code for a large, multi-team organization?**
Typical "paved road" structure: a platform/infra team owns a small set of
opinionated, semantically-versioned modules in a shared (often private)
registry; service teams consume those modules from their own thin
environment configurations rather than writing raw resource blocks. State
is split by blast radius and change velocity — network/foundational layers
that change rarely live in their own state, application-layer resources
that change often live in another — so a routine app deployment's `plan`
doesn't have to refresh and reason about the entire account's
infrastructure. CI enforces `fmt`/`validate`/security scanning
(Checkov/Trivy) and requires a human-reviewed `plan` before any `apply`;
production applies are gated behind manual approval and often behind cost
estimation tooling (e.g., Infracost) so reviewers see both correctness and
cost impact. Environment promotion happens by bumping a pinned module
version through dev → stage → prod, never by teams maintaining divergent
copies of the same module.

**22. What are the risks of `-target` and `-auto-approve`, and when would you still use them?**
`-target` restricts Terraform's reasoning to the targeted resource and its
dependencies, deliberately ignoring the rest of the configuration graph —
HashiCorp's own documentation warns a plan produced this way is not
guaranteed to be safe to apply broadly afterward, because it can miss
changes elsewhere that would normally be considered together. It's a
legitimate incident-response escape hatch (e.g., surgically fixing one
broken resource without waiting on an unrelated, currently-broken part of
the graph), but routine reliance on it is a sign the configuration should be
split into smaller, independently-applicable units. The correct follow-up
after any `-target` apply is to immediately run a full, untargeted `plan` to
confirm the whole configuration is still consistent. `-auto-approve` removes
the human confirmation step entirely; it's appropriate in CI pipelines
where the *exact* plan being applied was already reviewed and gated (e.g.,
via a saved `tfplan` artifact reviewed in a PR), and risky when run
ad hoc against production from a local machine, since there's no
independent check on what's about to happen.

**23. Explain `create_before_destroy`, and describe a case where a resource is still destroyed and recreated despite it.**
It reorders replacement so the new resource is created first and the old one
destroyed only after the new one exists, avoiding a downtime gap. It fails
to prevent downtime/errors when the resource has a uniqueness constraint
that can't tolerate two live copies simultaneously — a globally unique S3
bucket name, an EIP association that can't be double-assigned, or a security
group still referenced by another resource that would need to be updated
first. In those cases the *create* step of the replacement itself fails
(name/constraint collision), so Terraform never gets to the destroy step at
all — the old resource is never "safely retired," it's just that the whole
replacement aborts. The fix is usually to make the identifying attribute
generated/unique (e.g., a `name_prefix` instead of a fixed `name`) so a
second copy can coexist briefly, or to explicitly sequence the dependent
resources so nothing else references the old copy by the time it's
destroyed.

**24. What is a Terraform workspace, and what are its limitations versus directory-per-environment?**
A CLI workspace lets one configuration and one backend manage multiple named
state files — internally, most backends store each workspace's state under
a prefix keyed by the workspace name (e.g., `env:/staging/...` on the S3
backend) — with `terraform.workspace` available in configuration to vary
behavior (instance size, tags) and separate `.tfvars` supplying the rest.
The hard limitation: every workspace shares the *same* backend configuration
and the *same* code, so you cannot give `prod` a different state bucket,
different account, or different approval flow purely through CLI
workspaces — that requires separate directories/configurations (each with
its own `backend` block and possibly its own provider `assume_role`), which
is what most teams use for meaningfully different environments. It's also
worth flagging the operational risk: nothing stops someone from forgetting
to `terraform workspace select prod` and applying dev-sized changes against
prod state, or vice versa — teams mitigate this with CI that enforces
workspace-to-branch mapping rather than trusting manual `workspace select`.
Separately, Terraform Cloud's own "workspace" concept is a much larger unit
(closer to a full separate configuration + state + variable set + run
history) and shouldn't be conflated with the CLI feature of the same name.

**25. How does Terraform decide the order to create/destroy resources?**
It builds a directed acyclic graph (DAG) from every resource reference and
explicit `depends_on`, then walks it in topological order — resources with
no dependencies between them can execute concurrently, up to
`-parallelism` (default 10) simultaneous graph nodes. Creates/updates walk
the graph forward (dependencies before dependents); destroys walk it in
reverse (dependents before their dependencies, so you don't try to delete a
VPC while a subnet inside it still exists). Note that `-parallelism`
controls how many graph nodes Terraform *itself* processes concurrently — it
doesn't protect you from the underlying provider API's own rate limits, so
lowering it is a legitimate fix for API throttling errors even though it
looks like a "Terraform" setting.

## Troubleshooting-Focused

**26. A `terraform apply` fails with a state lock error. How do you resolve it safely?**
First confirm no other apply/plan is genuinely running — check CI for an
in-flight job, check with teammates, and where possible inspect the lock
directly (e.g., `aws dynamodb get-item` against the lock table to see who
holds it and when it was acquired). Only once you've confirmed the lock is
stale (commonly: a CI job was killed or timed out mid-run and never released
it) do you run `terraform force-unlock <LOCK_ID>` — force-unlocking during a
genuinely concurrent run is exactly the scenario locking exists to prevent,
and can corrupt state. As a preventive measure, prefer `-lock-timeout=<dur>`
in CI so a run waits for a legitimately-held lock to release instead of
failing immediately, and add a job-level timeout so a hung run can't hold
the lock indefinitely.

**27. `terraform plan` shows a resource will be destroyed and recreated unexpectedly. How do you investigate?**
Start with the plan's `# forces replacement` annotation, which names the
exact attribute responsible. Then determine *why* that attribute changed:
is it genuinely immutable for this resource type (e.g., changing an EC2
instance's `availability_zone`), or did an upstream data source/module
return a new computed value this run that it didn't before (a provider
upgrade changing a default, or an AMI data source resolving to a newer
"most recent" image)? Cross-reference the provider's CHANGELOG for the
specific resource around the version you're on/upgrading to — a
surprisingly large share of "forces replacement out of nowhere" issues are
a provider version bump changing how an attribute is read or normalized, not
an actual configuration change on your part. If it's expected and
destructive, `create_before_destroy` (see Q23) can reduce impact.

**28. How do you fix a "resource already exists" error?**
It means the real object exists but Terraform's state doesn't know about
it — typically created manually (click-ops), created by a previous
Terraform run whose state write got lost, or left over after a state file
was deleted/reset. Bring it under management with `terraform import` or an
`import` block rather than trying to force a fresh create; for bulk
recovery (many resources at once), `-generate-config-out` can scaffold the
HCL for each. Immediately follow up with a `plan` — if it's not clean, your
written configuration doesn't exactly match the real object's attributes
yet, and Terraform will try to "correct" it on the next apply.

**29. How would you migrate Terraform state to a new backend without downtime?**
Update the `backend` block to the new target and run
`terraform init -migrate-state`, which copies existing state into the new
backend — no infrastructure is touched, only where the *state file itself*
lives changes. Do this with nobody else applying against the old backend
(hold the lock, or do it during a change freeze) so a concurrent write
can't land in the old location after you've started migrating. Immediately
after, run `terraform plan` and confirm it reports no changes — that's your
verification that the migrated state still accurately reflects reality
before anyone applies against the new backend.

**30. How do you debug a provider authentication failure in a CI pipeline?**
Add a step that calls `aws sts get-caller-identity` (or the equivalent for
the provider in question) as early as possible in the pipeline, to
separate "no credentials reached the job at all" from "credentials arrived
but lack permission." If using `assume_role`, check the target role's trust
policy conditions — a mismatched `sub` or `aud` claim is the most common
failure when using OIDC federation (e.g., GitHub Actions), since the trust
policy has to match the exact repo/branch/environment claims the token
carries. Reproduce locally by assuming the same role with the same
mechanism (`aws sts assume-role` using the same source identity) to isolate
whether the problem is CI-environment-specific (missing OIDC provider
config, wrong region, a proxy stripping headers) or a genuine permissions
gap in the role/policy itself.

## Behavioral / Scenario Questions

**31. Tell me about a time Terraform state got out of sync with real infrastructure.**
Frame around: how you detected it (an unexpected diff in routine `plan`
output, or noticing an out-of-band console change), how you used
`plan -refresh-only` to see the *entire* scope of drift before touching
anything (rather than reacting to the first line you noticed), and the
judgment call between accepting the drift (`apply -refresh-only`, if the
manual change was legitimate and should become the new baseline) versus
reverting it (a normal `apply` to restore the configured value). Close with
the durable fix, not just the one-time cleanup: what you changed afterward
so it wouldn't recur — SCPs/IAM restricting console write access on
Terraform-managed resources, tagging conventions that make drift
obvious at a glance, or a scheduled drift-detection job that alerts before
someone stumbles onto it manually.

**32. Describe how you introduced Terraform to a team that previously made manual changes.**
Frame around: starting with `import` of existing resources rather than a
risky tear-down-and-recreate, so day one has zero infrastructure impact —
just Terraform catching up to reality. Building confidence in a low-risk
environment first (dev/sandbox) before touching anything customer-facing,
and using that period to also validate that your written configuration
matches imported resources exactly (a clean `plan` post-import, not just a
successful import command). Then describe the review/approval process you
introduced before production was ever touched — PR review of `plan` output,
a manual approval gate, and probably `prevent_destroy` on the handful of
resources where a mistake would be genuinely costly (production databases,
the state backend itself).

**33. How do you handle a disagreement about using a module versus copy-pasting a resource block?**
Frame around: naming the actual trade-off rather than treating "always use a
module" as dogma — a module adds a layer of indirection and a versioning
surface to manage, and is worth it once a pattern is duplicated in more than
a couple of places or is likely to need a coordinated change later (e.g., a
security-relevant default you'll want to update everywhere at once).
Copy-paste is sometimes genuinely fine for a one-off or a pattern unlikely
to be touched again. Bring the conversation back to a concrete decision
rule (something like "duplicated 3+ times, or security/compliance-relevant
→ module") rather than a personal preference, and mention how you'd validate
the decision later (if the "duplicate" copies keep silently drifting apart,
that's the signal a module was overdue).

**34. Tell me about a production incident caused by a `terraform apply`.**
Use STAR: the **situation** (what broke and the specific mechanism — an
unreviewed plan that included an unexpected forced replacement, a
destructive change nobody caught because `-auto-approve` was on in a path
that shouldn't have had it, or a `-target` apply that left the broader
configuration inconsistent), the **action** taken to stabilize (how you
diagnosed it using `plan`/`state show`/provider console cross-checks, and
whether recovery was a rollback, a forward-fix, or a restore from a
versioned state backup), and the **result** plus the lasting process change
— mandatory plan review for that class of change, `prevent_destroy` added to
the specific resource type involved, removing blanket `-auto-approve` from
any pipeline path that touches production, or splitting a state file so the
blast radius of a similar mistake would be smaller next time.

[⬆ Back to top](#top)

---

# 26. Reference Links

## Official Documentation

- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs) — full language, CLI, and provider documentation hub
- [Terraform Language Reference](https://developer.hashicorp.com/terraform/language) — resources, variables, expressions, functions
- [Terraform CLI Reference](https://developer.hashicorp.com/terraform/cli) — every subcommand and flag
- [Terraform Cloud Documentation](https://developer.hashicorp.com/terraform/cloud-docs) — workspaces, VCS-driven runs, Sentinel
- [Terraform Registry](https://registry.terraform.io/) — public providers and modules
- [AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) — every AWS resource/data source Terraform supports

## Learning and Tutorials

- [HashiCorp Developer Tutorials — Terraform](https://developer.hashicorp.com/terraform/tutorials) — official guided tutorials by topic
- [Terraform Best Practices](https://www.terraform-best-practices.com/) — community-maintained style and structure guide
- [HashiCorp Certified: Terraform Associate](https://developer.hashicorp.com/certifications/infrastructure-automation) — certification exam details and study guide

## Source and Issue Tracking

- [Terraform Core (GitHub)](https://github.com/hashicorp/terraform) — CLI/engine source and issue tracker
- [Terraform AWS Provider (GitHub)](https://github.com/hashicorp/terraform-provider-aws) — provider source, changelog, and known issues
- [Terraform CDK (CDKTF)](https://github.com/hashicorp/terraform-cdk) — define Terraform using TypeScript/Python/Go instead of HCL

## Tooling

- [tflint](https://github.com/terraform-linters/tflint) — provider-aware linting
- [Checkov](https://github.com/bridgecrewio/checkov) — static analysis for security/compliance misconfigurations
- [Trivy](https://github.com/aquasecurity/trivy) — vulnerability and misconfiguration scanner (absorbed tfsec)
- [Terragrunt](https://terragrunt.gruntwork.io/) — DRY wrapper for multi-environment Terraform
- [Terratest](https://terratest.gruntwork.io/) — Go library for writing real infrastructure integration tests

[⬆ Back to top](#top)
