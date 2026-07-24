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
drift, and computes diffs on the next `plan`.

**Never edit the state file by hand.** Use `terraform state` subcommands.

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

Modern Terraform (1.5+) uses an `import` block (declarative, plannable):

```hcl
import {
  to = aws_s3_bucket.data
  id = "company-existing-bucket"
}

resource "aws_s3_bucket" "data" {
  bucket = "company-existing-bucket"
}
```

```bash
terraform plan     # shows the import + any diff between real config and resource
terraform apply
```

The older, imperative form still works and is common in scripts/CI:

```bash
terraform import aws_s3_bucket.data company-existing-bucket
```

Either way, you must still write the matching `resource` block yourself —
import only links state to a real object, it does not generate HCL (though
`terraform plan -generate-config-out=generated.tf` can scaffold it for you in
recent versions).

## Detecting Drift

```bash
terraform plan -refresh-only        # show what changed in real infra vs state, without changing config
terraform apply -refresh-only        # accept the drift into state (does not change real resources)
```

Drift = someone/something changed a resource outside of Terraform (console
click-ops, another tool, auto-scaling). `-refresh-only` surfaces it safely
before a normal `plan`/`apply` would try to "fix" it back to the configured
value.

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

Terraform Cloud (SaaS) / Terraform Enterprise (self-hosted) add a managed
control plane on top of open-source Terraform:

- **Workspaces** — each maps to a working directory + variable set + state,
  roughly like a persistent CI job for one configuration.
- **Remote execution** — `plan`/`apply` run in HashiCorp's infrastructure, not
  your laptop or a generic CI runner.
- **VCS-driven runs** — a workspace can auto-trigger a plan on every commit or
  PR against a connected GitHub/GitLab/Azure DevOps repo.
- **Sentinel / OPA policy-as-code** — block applies that violate org policy
  (e.g., "no public S3 buckets", "must have a tag `CostCenter`").
- **Private Module Registry** — internal, versioned module sharing.
- **State management** — built-in locking, versioning, and access control,
  no S3/DynamoDB to run yourself.

```hcl
terraform {
  cloud {
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

# 21. Security Best Practices

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
