<a id="top"></a>

# DevSecOps Study Notes — Basic to Advanced

A single reference covering DevSecOps from first principles through
advanced, production-grade practice, with runnable configuration examples
and a troubleshooting guide organized by topic.

## Table of Contents

1. [Introduction to DevSecOps](#1-introduction-to-devsecops)
2. [Core Principles and Culture](#2-core-principles-and-culture)
3. [The Secure Software Development Lifecycle](#3-the-secure-software-development-lifecycle)
4. [Threat Modeling](#4-threat-modeling)
5. [Static Application Security Testing (SAST)](#5-static-application-security-testing-sast)
6. [Software Composition Analysis (SCA) / Dependency Scanning](#6-software-composition-analysis-sca--dependency-scanning)
7. [Secrets Detection and Management](#7-secrets-detection-and-management)
8. [Infrastructure as Code Security Scanning](#8-infrastructure-as-code-security-scanning)
9. [Container Security](#9-container-security)
10. [Dynamic Application Security Testing (DAST)](#10-dynamic-application-security-testing-dast)
11. [Kubernetes Security](#11-kubernetes-security)
12. [Secure CI/CD Pipeline Design](#12-secure-cicd-pipeline-design)
13. [Supply Chain Security (SBOM, Signing, SLSA)](#13-supply-chain-security-sbom-signing-slsa)
14. [Cloud Security Posture Management (CSPM)](#14-cloud-security-posture-management-cspm)
15. [Compliance as Code](#15-compliance-as-code)
16. [Identity and Access Management Security](#16-identity-and-access-management-security)
17. [Vulnerability Management](#17-vulnerability-management)
18. [Logging, Monitoring, and Incident Response](#18-logging-monitoring-and-incident-response)
19. [End-to-End Example: Secure CI/CD Pipeline](#19-end-to-end-example-secure-cicd-pipeline)
20. [Metrics and KPIs](#20-metrics-and-kpis)
21. [DevSecOps Tools Landscape](#21-devsecops-tools-landscape)
22. [Troubleshooting Guide by Topic](#22-troubleshooting-guide-by-topic)
23. [CLI Command Cheat Sheet](#23-cli-command-cheat-sheet)
24. [Study Checklist](#24-study-checklist)

---

# 1. Introduction to DevSecOps

DevSecOps extends DevOps by making security a shared, continuous
responsibility across the entire delivery lifecycle, instead of a
gate applied only at the end (traditionally, a manual pentest right before
release).

## DevOps vs DevSecOps

| | DevOps | DevSecOps |
|---|---|---|
| Security ownership | A separate team, engaged late | Every engineer, engaged from design |
| When security runs | Before release (gate) | Continuously, in every pipeline stage |
| Feedback loop | Slow (manual review) | Fast (automated scans on every commit/PR) |
| Failure mode | Vulnerabilities found in production | Vulnerabilities found before merge |

## Shift-Left Security

"Shift-left" means moving security activities earlier in the lifecycle —
threat modeling at design time, SAST/dependency scanning at commit time,
IaC scanning before `apply` — because the cost of fixing a defect grows
by roughly an order of magnitude at each later stage (design → code →
build → test → production).

## The Four Pillars (commonly cited model)

1. **People** — security champions embedded in each team, shared
   accountability, security training as part of onboarding.
2. **Process** — threat modeling, secure code review, defined severity/SLA
   for vulnerability remediation.
3. **Technology** — SAST, SCA, DAST, IaC scanning, container scanning,
   secrets detection, all automated in CI/CD.
4. **Governance** — policy as code, compliance evidence generation,
   auditability of every change.

[⬆ Back to top](#top)

---

# 2. Core Principles and Culture

- **Security is everyone's job**, not a single team's gate — developers fix
  their own SAST/SCA findings the same way they fix a failing unit test.
- **Automate everything repeatable** — manual security review doesn't scale
  to the deployment frequency DevOps enables; automated scanning does.
- **Fail fast, fail cheap** — a blocked pull request costs minutes; a
  vulnerability found in production costs an incident.
- **Immutable, auditable pipelines** — every security-relevant decision
  (a scan result, an approval, a policy exception) should be logged and
  traceable to a specific commit and person.
- **Least privilege by default** — pipelines, service accounts, and runtime
  workloads get only the permissions they demonstrably need.
- **Blameless postmortems** — incidents (including a bad security finding
  that shipped) are treated as process gaps to close, not individual
  failures to punish.

[⬆ Back to top](#top)

---

# 3. The Secure Software Development Lifecycle

A typical secure SDLC overlays security activities onto each traditional
phase:

| Phase | Traditional Activity | Security Activity |
|---|---|---|
| Requirements | Define features | Define security/compliance requirements, data classification |
| Design | Architecture diagrams | Threat modeling (STRIDE), security architecture review |
| Development | Write code | SAST, secrets detection, secure coding standards, peer review |
| Build | Compile/package | SCA (dependency scanning), IaC scanning, container image scanning |
| Test | Functional/integration tests | DAST, penetration testing, fuzzing |
| Release | Deploy | Image signing, SBOM generation, policy-as-code gate |
| Operate | Monitor uptime | Runtime security monitoring, vulnerability management, incident response |

## Example: Security Gates Mapped to a Pipeline

```text
commit → PR opened
  ├─ SAST (Semgrep/SonarQube)
  ├─ Secrets scan (gitleaks)
  └─ Unit tests

merge to main → build
  ├─ SCA (Snyk/OWASP Dependency-Check)
  ├─ Container image build + scan (Trivy)
  ├─ IaC scan (Checkov/tfsec) if infra changed
  └─ SBOM generation

deploy to staging
  ├─ DAST (OWASP ZAP baseline scan)
  └─ Policy-as-code gate (OPA/Conftest)

deploy to production
  ├─ Manual approval
  ├─ Image signature verification (cosign)
  └─ Runtime monitoring enabled (Falco/GuardDuty)
```

[⬆ Back to top](#top)

---

# 4. Threat Modeling

Threat modeling identifies what could go wrong *before* code is written,
so security requirements shape the design instead of being retrofitted.

## STRIDE Model

| Category | Question |
|---|---|
| **S**poofing | Can someone impersonate a user or system? |
| **T**ampering | Can data be modified in transit or at rest without detection? |
| **R**epudiation | Can an action be denied due to lack of logging/evidence? |
| **I**nformation Disclosure | Can sensitive data be exposed to unauthorized parties? |
| **D**enial of Service | Can the system be made unavailable? |
| **E**levation of Privilege | Can a user gain more access than intended? |

## Example: Threat Model for a Web API + RDS Backend

```text
Asset: Customer PII in RDS PostgreSQL

Threat: Attacker gains DB credentials from a leaked config file
  → Mitigation: Secrets Manager + IAM auth, no credentials in code/config

Threat: SQL injection via unsanitized API input
  → Mitigation: Parameterized queries, SAST rule enforcing ORM usage

Threat: Unencrypted data in transit between ALB and app servers
  → Mitigation: Enforce TLS 1.2+ on ALB listener, internal mTLS optional

Threat: Over-privileged application IAM role (can read all S3 buckets)
  → Mitigation: Least-privilege IAM policy scoped to specific bucket ARNs
```

## Lightweight Threat Modeling in Practice

Most teams don't run a formal STRIDE workshop for every change — a
lightweight version embedded in PR templates works well:

```markdown
## Security Considerations
- What new data does this change handle, and how sensitive is it?
- What new trust boundaries does this cross (new API, new IAM role, new
  external dependency)?
- What's the worst case if this component is fully compromised?
```

[⬆ Back to top](#top)

---

# 5. Static Application Security Testing (SAST)

SAST scans source code (without executing it) for insecure patterns —
SQL injection, hardcoded secrets, unsafe deserialization, XSS sinks.

## Example SAST Tools

| Tool | Short Description |
|---|---|
| **SonarQube** | Static analysis platform covering bugs, vulnerabilities, code smells, and duplication, with quality gates that can block a pipeline. |
| **Semgrep** | Fast, rule-based scanner using lightweight pattern-matching rules (YAML); easy to write custom rules and run in seconds on a PR diff. |
| **Checkmarx** | Enterprise SAST platform with deep, cross-file data-flow analysis across many languages; commonly used where compliance mandates a commercial tool. |
| **Fortify (OpenText)** | Enterprise SAST with broad language support and detailed remediation guidance; often used in large regulated organizations. |
| **CodeQL** | GitHub's semantic code analysis engine; queries code as if it were data, strong for finding complex data-flow vulnerabilities, integrates natively with GitHub Advanced Security. |
| **Bandit** | Lightweight SAST scanner specifically for Python, checking for common security issues (e.g., use of `eval`, hardcoded passwords). |

## SonarQube Quality Gate Example

```yaml
# sonar-project.properties
sonar.projectKey=app-backend
sonar.sources=src
sonar.tests=test
sonar.exclusions=**/vendor/**,**/node_modules/**
sonar.qualitygate.wait=true
```

```bash
sonar-scanner \
  -Dsonar.projectKey=app-backend \
  -Dsonar.host.url=https://sonarqube.company.com \
  -Dsonar.login=$SONAR_TOKEN
```

A quality gate blocks the pipeline when new code fails thresholds — e.g.,
zero new **Blocker**/**Critical** vulnerabilities, coverage on new code
above 80%.

## Semgrep Example (Lightweight, Fast, Rule-Based)

```yaml
# .semgrep.yml
rules:
  - id: hardcoded-aws-key
    pattern: $KEY = "AKIA..."
    message: Hardcoded AWS access key detected
    languages: [python, javascript]
    severity: ERROR

  - id: flask-debug-true
    pattern: app.run(debug=True)
    message: Flask debug mode must not be enabled in production code
    languages: [python]
    severity: WARNING
```

```bash
semgrep --config .semgrep.yml --error src/
semgrep --config "p/owasp-top-ten" src/   # use a curated public ruleset
```

## SAST in a CI Pipeline

```yaml
# GitHub Actions step
- name: SAST Scan
  run: |
    semgrep --config "p/owasp-top-ten" --error --json --output semgrep-results.json src/
- name: Upload SARIF
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: semgrep-results.json
```

## SAST Best Practices

- Run on every pull request, not just nightly — feedback while the change
  is still fresh in the developer's mind.
- Tune rulesets to the actual language/framework; a noisy, generic ruleset
  trains developers to ignore findings ("alert fatigue").
- Fail the build only on new findings above a severity threshold;
  don't require fixing pre-existing debt to merge an unrelated change.
- Track findings over time (SARIF upload to GitHub/GitLab security tab)
  so trend, not just point-in-time count, is visible.

[⬆ Back to top](#top)

---

# 6. Software Composition Analysis (SCA) / Dependency Scanning

SCA identifies known vulnerabilities (CVEs) in third-party
libraries/packages your application depends on — most real-world breaches
trace back to a vulnerable dependency, not custom code.

## Example SCA Tools

| Tool | Short Description |
|---|---|
| **Snyk** | SaaS/CLI SCA scanner covering dependencies, containers, and IaC; tracks a project continuously (`snyk monitor`) and alerts on newly disclosed CVEs. |
| **OWASP Dependency-Check** | Free, open-source SCA tool that cross-references dependencies against the National Vulnerability Database (NVD); strong default choice with no vendor lock-in. |
| **Trivy** | Originally a container scanner, now also scans filesystems/lockfiles for dependency CVEs, IaC misconfigurations, and secrets in one tool. |
| **npm audit / pip-audit** | Package-manager-native auditing for Node.js and Python respectively; fast, zero-setup first line of defense. |
| **GitHub Dependabot** | Native GitHub feature that scans dependency manifests, opens automated PRs to bump vulnerable packages to a patched version. |
| **Black Duck** | Enterprise SCA platform with license-compliance scanning alongside vulnerability detection, common where OSS license risk is also tracked. |

## OWASP Dependency-Check

```bash
dependency-check.sh \
  --project "app-backend" \
  --scan ./ \
  --format HTML \
  --out reports/ \
  --failOnCVSS 7
```

## Snyk Example

```bash
snyk auth
snyk test --severity-threshold=high
snyk monitor    # continuously track this project's dependency graph in Snyk's dashboard
```

```yaml
# .snyk policy file — document and time-box exceptions, don't silently ignore
version: v1.5.0
ignore:
  SNYK-JS-LODASH-1234567:
    - '*':
        reason: No fix available yet; low exploitability in our usage
        expires: 2026-09-01T00:00:00.000Z
```

## npm / pip Native Auditing

```bash
npm audit --audit-level=high
npm audit fix

pip install pip-audit
pip-audit -r requirements.txt
```

## Trivy for Dependency + Container Scanning

```bash
trivy fs --severity HIGH,CRITICAL --exit-code 1 .
trivy image --severity HIGH,CRITICAL myapp:latest
```

## SCA Best Practices

- Fail the build on **HIGH/CRITICAL** findings with a known fix available;
  track (don't silently allow) findings with no fix yet, with an expiry
  date on the exception.
- Scan lockfiles (`package-lock.json`, `requirements.txt`, `go.sum`), not
  just declared dependencies — transitive dependencies are the most common
  source of surprise CVEs.
- Re-scan on a schedule, not only at commit time — a dependency can become
  vulnerable (new CVE disclosed) without any code change on your side.

[⬆ Back to top](#top)

---

# 7. Secrets Detection and Management

## Preventing Secrets From Being Committed

**gitleaks** (pre-commit hook + CI):

```yaml
# .gitleaks.toml
title = "gitleaks config"

[[rules]]
id = "aws-access-key"
description = "AWS Access Key"
regex = '''AKIA[0-9A-Z]{16}'''
tags = ["key", "aws"]

[[rules]]
id = "generic-api-key"
description = "Generic API Key"
regex = '''(?i)api[_-]?key["']?\s*[:=]\s*["'][0-9a-zA-Z]{32,}["']'''
tags = ["key"]
```

```bash
gitleaks detect --source . --config .gitleaks.toml --exit-code 1
```

Pre-commit hook (`.pre-commit-config.yaml`):

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

**git-secrets** (AWS-focused alternative):

```bash
git secrets --install
git secrets --register-aws
git secrets --scan
```

## Runtime Secrets Management

Never hard-code secrets in application config or environment files checked
into source control. Retrieve them at runtime instead:

```hcl
# Terraform — pull at apply time, not in code
data "aws_secretsmanager_secret_version" "db" {
  secret_id = "prod/db/password"
}
```

```yaml
# Kubernetes — external secret reference, not a plaintext Secret manifest
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: db-credentials
spec:
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  target:
    name: db-credentials
  data:
    - secretKey: password
      remoteRef:
        key: prod/db/password
```

## HashiCorp Vault Example

```hcl
# Enable a KV secrets engine and a policy scoped to one path
resource "vault_mount" "kv" {
  path = "secret"
  type = "kv-v2"
}

resource "vault_policy" "app_read" {
  name   = "app-read"
  policy = <<EOT
path "secret/data/app/*" {
  capabilities = ["read"]
}
EOT
}
```

```bash
vault kv put secret/app/db password="s3cr3t"
vault kv get secret/app/db
```

## Secrets Management Best Practices

- Rotate credentials on a schedule and immediately after any suspected
  exposure — automate rotation (Secrets Manager rotation Lambdas, Vault
  dynamic secrets) rather than relying on someone remembering.
- Use short-lived, dynamically issued credentials (Vault dynamic database
  credentials, AWS STS/OIDC federation) over long-lived static secrets
  wherever possible.
- Scan git history, not just the current commit — a secret committed and
  later "removed" is still in history unless the repo is rewritten
  (`git filter-repo`/BFG) and old commits are invalidated.
- Treat a leaked secret as compromised immediately — rotate first,
  investigate second; don't wait for confirmation of misuse.

[⬆ Back to top](#top)

---

# 8. Infrastructure as Code Security Scanning

IaC scanning catches misconfigurations (public S3 buckets, open security
groups, missing encryption) before `terraform apply` — much cheaper to fix
than after the resource exists.

## Checkov

```bash
checkov -d . --framework terraform --compact --quiet
checkov -d . --framework terraform --skip-check CKV_AWS_20   # document any skip with a reason
```

```yaml
# .checkov.yaml — pin checks and severity thresholds explicitly
framework:
  - terraform
skip-check:
  - CKV_AWS_20  # public bucket allowed for this specific static-assets bucket
compact: true
quiet: true
```

## tfsec (folded into Trivy, still usable standalone)

```bash
tfsec . --minimum-severity HIGH
```

## Terrascan

```bash
terrascan scan -i terraform -d . --severity HIGH
```

## Example Finding and Fix

```hcl
# Before — flagged: CKV_AWS_18 (S3 bucket without access logging),
# CKV_AWS_21 (no versioning), CKV_AWS_145 (no default encryption)
resource "aws_s3_bucket" "data" {
  bucket = "company-app-data"
}

# After
resource "aws_s3_bucket" "data" {
  bucket = "company-app-data"
}

resource "aws_s3_bucket_versioning" "data" {
  bucket = aws_s3_bucket.data.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
    }
  }
}

resource "aws_s3_bucket_logging" "data" {
  bucket        = aws_s3_bucket.data.id
  target_bucket = aws_s3_bucket.logs.id
  target_prefix = "data-access-logs/"
}
```

## IaC Scanning in CI

```yaml
- name: IaC Security Scan
  run: |
    checkov -d . --framework terraform --compact --quiet --output cli --output sarif --output-file-path console,checkov-results.sarif
- name: Upload SARIF
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: checkov-results.sarif
```

[⬆ Back to top](#top)

---

# 9. Container Security

## Dockerfile Hardening

```dockerfile
# Before — root user, large attack surface, no pinned digest
FROM node:latest
COPY . /app
RUN npm install
CMD ["node", "server.js"]
```

```dockerfile
# After — pinned digest, minimal base, non-root user, multi-stage build
FROM node:20.11.1-alpine@sha256:abcdef... AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .

FROM gcr.io/distroless/nodejs20-debian12
WORKDIR /app
COPY --from=build /app /app
USER nonroot:nonroot
EXPOSE 3000
CMD ["server.js"]
```

## Image Scanning

```bash
trivy image --severity HIGH,CRITICAL --exit-code 1 myapp:1.4.0
grype myapp:1.4.0 --fail-on high
```

## Scanning in the Build Pipeline

```yaml
- name: Build Image
  run: docker build -t myapp:${{ github.sha }} .

- name: Scan Image
  run: trivy image --severity HIGH,CRITICAL --exit-code 1 myapp:${{ github.sha }}

- name: Push (only if scan passed)
  run: docker push myapp:${{ github.sha }}
```

## Runtime Container Security

```yaml
# Kubernetes SecurityContext — enforce non-root, read-only filesystem,
# drop all Linux capabilities except what's explicitly needed
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
    - name: app
      image: myapp:1.4.0
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        readOnlyRootFilesystem: true
        allowPrivilegeEscalation: false
        capabilities:
          drop: ["ALL"]
```

## Container Security Best Practices

- Pin base images by digest, not just tag (`node:20-alpine` can change
  underneath you; `node:20-alpine@sha256:...` cannot).
- Prefer distroless or minimal (Alpine) base images — fewer packages means
  fewer CVEs to track.
- Never run as root in the container; set `USER` explicitly.
- Scan images at build time **and** on a schedule for already-deployed
  images (a new CVE can be disclosed for a library already running in
  production).
- Use multi-stage builds so build tools/dependencies never ship in the
  final runtime image.

[⬆ Back to top](#top)

---

# 10. Dynamic Application Security Testing (DAST)

DAST tests a *running* application from the outside — the way an attacker
would — catching issues SAST can't see (misconfigurations, auth flaws,
runtime behavior).

## Example DAST Tools

| Tool | Short Description |
|---|---|
| **OWASP ZAP** | Free, open-source DAST proxy/scanner; supports quick baseline (passive) scans and deeper authenticated full scans, widely used in CI pipelines. |
| **Burp Suite** | Industry-standard web app testing toolkit (manual + automated scanning); the Pro edition is a staple for manual pentesting alongside its automated crawler/scanner. |
| **Nikto** | Lightweight, fast web server scanner focused on known-bad files, outdated server software, and common misconfigurations. |
| **Acunetix** | Commercial DAST scanner with strong coverage of modern JavaScript-heavy single-page applications and APIs. |
| **StackHawk** | DAST built specifically for CI/CD pipelines, designed to run automatically on every deploy with developer-friendly findings. |
| **Nuclei** | Fast, template-based vulnerability scanner; community-maintained templates cover CVEs, misconfigurations, and exposed panels. |

## OWASP ZAP Baseline Scan

```bash
docker run --rm -v $(pwd):/zap/wrk/:rw \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py -t https://staging.app.company.com \
  -r zap-report.html -x zap-report.xml
```

## ZAP in CI (Fail the Build on High-Risk Findings)

```yaml
- name: DAST Scan
  run: |
    docker run --rm -v $(pwd):/zap/wrk/:rw \
      ghcr.io/zaproxy/zaproxy:stable \
      zap-baseline.py -t https://staging.app.company.com \
      -r zap-report.html || true
    # zap-baseline.py exits 2 on WARN-level findings by default;
    # parse zap-report.xml and fail explicitly on any High-risk alert
```

## OWASP ZAP Full Scan (Authenticated, Deeper — Usually Scheduled, Not Per-PR)

```bash
docker run --rm -v $(pwd):/zap/wrk/:rw \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-full-scan.py -t https://staging.app.company.com \
  -r zap-full-report.html
```

## DAST Best Practices

- Run baseline (fast, unauthenticated) scans on every deploy to staging;
  reserve full/authenticated scans for a nightly or weekly schedule — they
  take much longer and generate more noise.
- Scan a staging environment that mirrors production configuration, not a
  stripped-down dev environment — DAST is only as good as its target's
  fidelity.
- Combine with SAST/SCA rather than relying on DAST alone — DAST won't
  catch a vulnerable dependency that's never exercised by the crawled paths.

[⬆ Back to top](#top)

---

# 11. Kubernetes Security

## Pod Security Standards

Kubernetes replaced PodSecurityPolicy with **Pod Security Admission**,
enforced via namespace labels:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
```

`restricted` requires non-root, no privilege escalation, dropped
capabilities, and a seccomp profile — the same properties covered in
[Container Security](#9-container-security) §SecurityContext.

## RBAC — Least Privilege

```yaml
# Before — cluster-wide admin, far broader than needed
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: app-binding
subjects:
  - kind: ServiceAccount
    name: app-sa
    namespace: production
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
```

```yaml
# After — namespaced Role scoped to exactly what the app needs
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: production
  name: app-role
rules:
  - apiGroups: [""]
    resources: ["configmaps", "secrets"]
    verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  namespace: production
  name: app-binding
subjects:
  - kind: ServiceAccount
    name: app-sa
    namespace: production
roleRef:
  kind: Role
  name: app-role
  apiGroup: rbac.authorization.k8s.io
```

## Network Policies (Default-Deny)

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-app-to-db
  namespace: production
spec:
  podSelector:
    matchLabels: { app: backend }
  policyTypes: ["Egress"]
  egress:
    - to:
        - podSelector:
            matchLabels: { app: postgres }
      ports:
        - protocol: TCP
          port: 5432
```

## Admission Control — OPA/Gatekeeper Policy Example

```yaml
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8srequiredlabels
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredLabels
      validation:
        openAPIV3Schema:
          properties:
            labels:
              type: array
              items: { type: string }
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequiredlabels

        violation[{"msg": msg}] {
          required := input.parameters.labels
          provided := input.review.object.metadata.labels
          missing := required[_]
          not provided[missing]
          msg := sprintf("missing required label: %v", [missing])
        }
```

```yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredLabels
metadata:
  name: require-team-label
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
  parameters:
    labels: ["team", "environment"]
```

Kyverno is a common alternative that expresses the same policies in plain
YAML instead of Rego:

```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-non-root
spec:
  validationFailureAction: Enforce
  rules:
    - name: check-runAsNonRoot
      match:
        resources:
          kinds: ["Pod"]
      validate:
        message: "Containers must run as non-root"
        pattern:
          spec:
            securityContext:
              runAsNonRoot: true
```

## Kubernetes Security Best Practices

- Enforce `restricted` Pod Security Standards on every namespace except
  where a documented exception exists.
- Default-deny network policy per namespace, then explicitly allow only the
  traffic paths the application needs.
- Never use `cluster-admin` for application service accounts; scope RBAC to
  the specific namespace and verbs required.
- Scan manifests before apply the same way you scan Terraform (Checkov and
  Trivy both support Kubernetes manifests).
- Enable audit logging on the API server and ship it to your SIEM.

[⬆ Back to top](#top)

---

# 12. Secure CI/CD Pipeline Design

## Principles

- **Least privilege for pipeline identities** — a CI job should hold only
  the permissions needed for that specific job, ideally via short-lived
  OIDC-federated credentials rather than long-lived static secrets.
- **Immutable, versioned pipeline definitions** — pipeline-as-code in the
  same repo (or a centrally governed shared pipeline), reviewed like any
  other change.
- **Segregation of duties** — the person who approves a production deploy
  should not be the only person who can also disable the security gates.
- **No secrets in logs** — mask/redact sensitive values; treat build logs
  as a potential leak vector.
- **Signed, verifiable artifacts** — what gets deployed is provably what
  was built and scanned, not something swapped in between stages.

## Example: OIDC Federation Instead of Static Cloud Credentials

```yaml
# GitHub Actions — no long-lived AWS keys stored as secrets
permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-actions-deploy
          aws-region: us-east-1
```

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
        },
        "StringLike": {
          "token.actions.githubusercontent.com:sub": "repo:my-org/app-backend:ref:refs/heads/main"
        }
      }
    }
  ]
}
```

## Example: Required Status Checks (Branch Protection)

```text
Required checks before merge to main:
  - sast-scan
  - secrets-scan
  - sca-scan
  - unit-tests
  - iac-scan (only if terraform/** changed)

Required reviewers: 1 code owner + 1 security champion for changes under
security-sensitive paths (auth/, iam/, terraform/)
```

## Secure Pipeline Checklist

- [ ] Every stage's identity is scoped to least privilege, ideally via OIDC.
- [ ] Branch protection requires all security scans to pass before merge.
- [ ] Production deploys require manual approval from someone other than
      the author.
- [ ] Build artifacts are signed and verified before deployment.
- [ ] Pipeline definitions themselves are version-controlled and reviewed.
- [ ] Secrets are pulled from a vault/secrets manager at runtime, never
      stored as plaintext pipeline variables.

[⬆ Back to top](#top)

---

# 13. Supply Chain Security (SBOM, Signing, SLSA)

## Software Bill of Materials (SBOM)

An SBOM lists every component (direct and transitive) in a build artifact —
essential for knowing, when a new CVE is disclosed, whether you're affected
at all, without re-scanning everything from scratch.

```bash
# Generate an SPDX-format SBOM with Syft
syft myapp:1.4.0 -o spdx-json > sbom.spdx.json

# Generate a CycloneDX SBOM
syft myapp:1.4.0 -o cyclonedx-json > sbom.cdx.json

# Check an SBOM against known vulnerabilities
grype sbom:sbom.cdx.json
```

## Artifact Signing with Sigstore/cosign

```bash
# Sign a container image (keyless, using OIDC identity)
cosign sign --yes myregistry.io/myapp:1.4.0

# Verify before deployment
cosign verify \
  --certificate-identity "https://github.com/my-org/app-backend/.github/workflows/build.yml@refs/heads/main" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
  myregistry.io/myapp:1.4.0
```

## Admission-Time Signature Verification (Kubernetes)

```yaml
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: require-signed-images
spec:
  images:
    - glob: "myregistry.io/**"
  authorities:
    - keyless:
        identities:
          - issuer: https://token.actions.githubusercontent.com
            subject: https://github.com/my-org/app-backend/.github/workflows/build.yml@refs/heads/main
```

## SLSA Framework (Supply-chain Levels for Software Artifacts)

| Level | Requirement |
|---|---|
| SLSA 1 | Build process is scripted/automated (no manual build steps) |
| SLSA 2 | Build runs on a hosted build service; provenance is generated and signed |
| SLSA 3 | Build platform prevents tampering between steps (isolated, ephemeral runners) |
| SLSA 4 | Two-person review of every change; hermetic, reproducible builds |

## Dependency Confusion Prevention

- Scope internal/private package names so they can never collide with a
  public registry name (a documented namespace/prefix convention).
- Configure package managers to prefer the private registry explicitly
  rather than falling back to public by default.
- Pin exact versions (and, where supported, hashes) in lockfiles rather
  than open version ranges.

[⬆ Back to top](#top)

---

# 14. Cloud Security Posture Management (CSPM)

CSPM continuously evaluates cloud account configuration against security
best practices/benchmarks and flags drift toward insecure states.

## AWS Security Hub

```bash
aws securityhub enable-security-hub
aws securityhub batch-enable-standards \
  --standards-subscription-requests '[{"StandardsArn":"arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0"}]'
aws securityhub get-findings --filters '{"SeverityLabel":[{"Value":"CRITICAL","Comparison":"EQUALS"}]}'
```

## Amazon GuardDuty

```bash
aws guardduty create-detector --enable
aws guardduty list-findings --detector-id <detector-id> \
  --finding-criteria '{"Criterion":{"severity":{"Gte":7}}}'
```

## AWS Config — Continuous Compliance Rules

```hcl
resource "aws_config_config_rule" "s3_encrypted" {
  name = "s3-bucket-server-side-encryption-enabled"

  source {
    owner             = "AWS"
    source_identifier = "S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED"
  }
}

resource "aws_config_config_rule" "no_public_sg" {
  name = "restricted-ssh"

  source {
    owner             = "AWS"
    source_identifier = "INCOMING_SSH_DISABLED"
  }
}
```

## Open-Source CSPM Tools

```bash
# Prowler — AWS security best-practice assessment
prowler aws --severity critical high

# ScoutSuite — multi-cloud security auditing
scout aws --report-dir ./scout-report
```

## CSPM Best Practices

- Enable Security Hub/GuardDuty/Config in every account, including
  sandbox/dev — misconfigurations there are still real exposure.
- Route findings to a ticketing system (not just a dashboard nobody
  checks) with an SLA per severity.
- Use Config rules or Sentinel/OPA to *prevent* drift, not just detect it
  after the fact.

[⬆ Back to top](#top)

---

# 15. Compliance as Code

## Policy as Code — OPA/Conftest Against Terraform Plans

```rego
# policy/s3.rego
package terraform.s3

deny[msg] {
  resource := input.resource_changes[_]
  resource.type == "aws_s3_bucket"
  resource.change.after.acl == "public-read"
  msg := sprintf("S3 bucket '%s' must not be publicly readable", [resource.address])
}
```

```bash
terraform show -json tfplan > plan.json
conftest test plan.json --policy policy/
```

## HashiCorp Sentinel (Terraform Cloud/Enterprise)

```python
import "tfplan/v2" as tfplan

s3_buckets = filter tfplan.resource_changes as _, rc {
  rc.type is "aws_s3_bucket" and
  (rc.change.actions contains "create" or rc.change.actions contains "update")
}

main = rule {
  all s3_buckets as _, bucket {
    bucket.change.after.acl != "public-read"
  }
}
```

## CIS Benchmarks with InSpec

```ruby
# controls/cis_ssh.rb
control 'cis-5.2.10' do
  impact 1.0
  title 'Ensure SSH root login is disabled'
  describe sshd_config do
    its('PermitRootLogin') { should cmp 'no' }
  end
end
```

```bash
inspec exec controls/ -t ssh://user@host --sudo
```

## Compliance as Code Best Practices

- Encode the specific benchmark (CIS, NIST 800-53, PCI-DSS) as automated
  checks, not a static PDF someone re-reads before an audit.
- Run compliance checks continuously, not just before an audit window —
  drift happens constantly, audits happen once or twice a year.
- Generate audit evidence (pass/fail reports with timestamps) automatically
  as a pipeline artifact, so evidence collection isn't a manual scramble.

[⬆ Back to top](#top)

---

# 16. Identity and Access Management Security

- **Least privilege** — start from zero permissions, add only what's
  demonstrably needed; use IAM Access Analyzer / policy simulators to
  validate before granting broader access "just in case."
- **No long-lived static credentials where avoidable** — prefer IAM roles,
  OIDC federation, and STS temporary credentials over IAM users with
  access keys.
- **MFA everywhere it's supported**, especially for any human identity with
  console or API access to production.
- **Service accounts scoped per workload**, not shared across
  applications — a compromise of one workload shouldn't grant access to
  every other workload's resources.
- **Regular access reviews** — remove permissions/accounts that are no
  longer needed; a common finding in audits is stale access from a role
  change or offboarding that didn't fully propagate.

## Example: Least-Privilege IAM Policy (Scoped, Not Wildcard)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::company-app-data/uploads/*"
    }
  ]
}
```

```json
// Avoid this — broad, unscoped, and grants far more than needed
{
  "Version": "2012-10-17",
  "Statement": [
    { "Effect": "Allow", "Action": "s3:*", "Resource": "*" }
  ]
}
```

[⬆ Back to top](#top)

---

# 17. Vulnerability Management

## CVE and CVSS Scoring

- **CVE** (Common Vulnerabilities and Exposures) — a unique identifier for
  a publicly known vulnerability.
- **CVSS** (Common Vulnerability Scoring System) — a 0–10 severity score;
  commonly bucketed as Low (0.1–3.9), Medium (4.0–6.9), High (7.0–8.9),
  Critical (9.0–10.0).

## Example Remediation SLA Policy

| Severity | Remediation SLA |
|---|---|
| Critical | 24–48 hours |
| High | 7 days |
| Medium | 30 days |
| Low | Best effort / next release cycle |

## Vulnerability Management Workflow

```text
1. Detect  — SAST/SCA/container/CSPM scan surfaces a finding
2. Triage  — confirm it's a true positive and assess actual exploitability
             in this context (is the vulnerable code path even reachable?)
3. Prioritize — CVSS score + exploitability + asset criticality
4. Remediate — patch, upgrade, or apply a compensating control
5. Verify  — re-scan to confirm the finding is resolved
6. Report  — track time-to-remediate against SLA for trend reporting
```

## Handling a Finding With No Available Fix

- Apply a compensating control (WAF rule, network segmentation, disabling
  the affected feature) if the underlying library can't yet be upgraded.
- Document the exception with an owner and expiry date (see the `.snyk`
  policy example in [§6](#6-software-composition-analysis-sca--dependency-scanning)) —
  never a silent, permanent suppression.
- Re-evaluate on every scan run; don't let a "temporary" exception outlive
  its expiry unnoticed.

[⬆ Back to top](#top)

---

# 18. Logging, Monitoring, and Incident Response

## What to Log

- Authentication events (success and failure), especially privilege
  escalation and admin actions.
- All API activity in cloud accounts (AWS CloudTrail, Azure Activity Log).
- Application-level security events (failed input validation, auth
  failures, rate-limit triggers).
- Kubernetes API server audit logs.

## Example: CloudTrail + Security Hub + SNS Alerting

```hcl
resource "aws_cloudtrail" "main" {
  name                          = "org-trail"
  s3_bucket_name                = aws_s3_bucket.trail.id
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true
}

resource "aws_cloudwatch_event_rule" "guardduty_findings" {
  name = "guardduty-high-severity"
  event_pattern = jsonencode({
    source      = ["aws.guardduty"]
    detail-type = ["GuardDuty Finding"]
    detail      = { severity = [{ numeric = [">=", 7] }] }
  })
}

resource "aws_cloudwatch_event_target" "notify" {
  rule = aws_cloudwatch_event_rule.guardduty_findings.name
  arn  = aws_sns_topic.security_alerts.arn
}
```

## Runtime Container Threat Detection — Falco Example

```yaml
# falco_rules.local.yaml
- rule: Unexpected outbound connection from container
  desc: Detect a container making an outbound connection to an unexpected port
  condition: >
    outbound and container and
    not fd.sport in (allowed_outbound_ports)
  output: >
    Unexpected outbound connection
    (command=%proc.cmdline connection=%fd.name container=%container.name)
  priority: WARNING
```

## Incident Response Runbook (Skeleton)

```markdown
# Security Incident Response Runbook

## 1. Detect and Triage
- Confirm the alert is a true positive.
- Classify severity and assemble the response team.

## 2. Contain
- Isolate affected resources (revoke credentials, quarantine instance/pod,
  restrict security group).
- Preserve evidence before making further changes (snapshot, log export).

## 3. Eradicate
- Remove the root cause (patch, rotate compromised credentials, remove
  malicious artifact).

## 4. Recover
- Restore from known-good state/backup.
- Validate the fix; monitor closely for recurrence.

## 5. Post-Incident
- Root-cause analysis, blameless postmortem.
- Update detection rules/runbooks based on what was missed or slow.
```

## Logging and IR Best Practices

- Centralize logs in a SIEM (Security Hub, Splunk, ELK, Datadog) — logs
  scattered per-service are effectively unsearchable during an incident.
- Alert on the smallest reasonable signal, then tune — starting too noisy
  and reducing is safer than starting silent and missing real incidents.
- Rehearse the incident response runbook (tabletop exercises) before a
  real incident forces you to improvise it.

[⬆ Back to top](#top)

---

# 19. End-to-End Example: Secure CI/CD Pipeline

A single GitHub Actions pipeline combining most of the controls above:

```yaml
name: secure-pipeline

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

permissions:
  id-token: write
  contents: read
  security-events: write

jobs:
  security-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0   # full history, needed for gitleaks

      - name: Secrets Scan
        run: |
          docker run --rm -v $(pwd):/repo zricethezav/gitleaks:latest \
            detect --source /repo --exit-code 1

      - name: SAST
        run: semgrep --config "p/owasp-top-ten" --error src/

      - name: Dependency Scan (SCA)
        run: |
          npm ci
          npm audit --audit-level=high

      - name: IaC Scan
        if: contains(github.event.pull_request.changed_files, 'terraform/')
        run: checkov -d terraform/ --compact --quiet

      - name: Unit Tests
        run: npm test

  build-and-scan-image:
    needs: security-checks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Scan Image
        run: trivy image --severity HIGH,CRITICAL --exit-code 1 myapp:${{ github.sha }}

      - name: Generate SBOM
        run: syft myapp:${{ github.sha }} -o cyclonedx-json > sbom.json

      - name: Sign Image
        if: github.ref == 'refs/heads/main'
        run: cosign sign --yes myregistry.io/myapp:${{ github.sha }}

  deploy-staging:
    needs: build-and-scan-image
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Staging
        run: echo "deploy to staging"

      - name: DAST Baseline Scan
        run: |
          docker run --rm -v $(pwd):/zap/wrk/:rw ghcr.io/zaproxy/zaproxy:stable \
            zap-baseline.py -t https://staging.app.company.com

  deploy-production:
    needs: deploy-staging
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production   # requires manual approval via GitHub Environments
    steps:
      - name: Verify Signature
        run: |
          cosign verify \
            --certificate-identity-regexp "https://github.com/my-org/.*" \
            --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
            myregistry.io/myapp:${{ github.sha }}

      - name: Deploy to Production
        run: echo "deploy to production"
```

[⬆ Back to top](#top)

---

# 20. Metrics and KPIs

| Metric | Why It Matters |
|---|---|
| Mean time to remediate (MTTR) by severity | Shows whether the org actually closes findings within SLA |
| Number of vulnerabilities by severity, over time | Trend, not point-in-time snapshot, shows if posture is improving |
| % of pipelines with security gates enabled | Coverage — a scan that isn't run everywhere isn't protecting everywhere |
| % of findings with an expired exception | Surfaces exceptions that were meant to be temporary but weren't followed up |
| Deployment frequency vs. incident rate | Confirms security controls aren't just slowing delivery without reducing risk |
| Time from CVE disclosure to patched in production | Measures real exposure window, not just detection speed |
| % of production images signed and verified | Supply chain integrity coverage |

[⬆ Back to top](#top)

---

# 21. DevSecOps Tools Landscape

| Category | Tools |
|---|---|
| SAST | SonarQube, Semgrep, Checkmarx, Fortify |
| SCA / Dependency Scanning | Snyk, OWASP Dependency-Check, Trivy, pip-audit, npm audit |
| Secrets Detection | gitleaks, git-secrets, TruffleHog |
| IaC Scanning | Checkov, tfsec, Terrascan |
| Container Scanning | Trivy, Grype, Clair |
| DAST | OWASP ZAP, Burp Suite |
| Kubernetes Policy | OPA/Gatekeeper, Kyverno |
| Secrets Management | HashiCorp Vault, AWS Secrets Manager, Azure Key Vault |
| SBOM | Syft, CycloneDX CLI |
| Artifact Signing | Sigstore/cosign, Notary |
| CSPM | AWS Security Hub, GuardDuty, Prowler, ScoutSuite |
| Compliance as Code | OPA/Conftest, Sentinel, InSpec |
| Runtime Security | Falco, AWS GuardDuty, Datadog CSM |

[⬆ Back to top](#top)

---

# 22. Troubleshooting Guide by Topic

## SAST/SCA Pipeline Failures

**Pipeline fails on a finding that's a false positive**
- Confirm it's genuinely a false positive (not just inconvenient) — check
  the rule's documentation for the exact pattern it matches.
- Suppress at the narrowest possible scope (inline comment/annotation for
  that specific line, not a blanket rule disable for the whole project).

**Scan takes too long / times out in CI**
- Cache dependency scan databases (`trivy` DB, `dependency-check` NVD
  cache) between runs instead of re-downloading every time.
- Scan only changed paths on PRs; run a full scan on a schedule instead of
  every commit.

## Secrets Detection Issues

**gitleaks/git-secrets flags a false positive (e.g., a test fixture key)**
- Add an explicit allowlist entry scoped to that exact file/pattern, not a
  blanket exclusion for the whole repo.

**A real secret was already committed and merged**
- Rotate the credential immediately — treat it as compromised the moment
  it hit any branch, regardless of whether the repo is private.
- Purge it from history (`git filter-repo` or BFG Repo-Cleaner), force-push
  the rewritten history, and have every clone re-fetch — but rotation
  matters more than history-rewriting, since the old value must be assumed
  seen already.

## IaC Scan Failures

**Checkov/tfsec blocks a resource you believe is intentionally configured this way**
- Use a scoped skip with a documented reason and, ideally, an expiry/review
  date — not a blanket `--skip-check` across the whole pipeline.
- Re-verify periodically that the exception is still needed; a scoped skip
  from 18 months ago for a resource that's since changed purpose is a
  common audit finding.

## Container Scan Failures

**Trivy/Grype reports a CVE with "no fix available"**
- Check whether the vulnerable code path is actually reachable in your
  usage — not all CVEs in a dependency are exploitable given how you use it.
- Apply a compensating control and document a time-boxed exception (see
  [§17 Vulnerability Management](#17-vulnerability-management)) rather than
  blocking every deploy indefinitely on an unfixable transitive dependency.

**Image scan passes locally but fails in CI**
- Confirm both environments are scanning the same image digest, not a
  locally cached older layer — pull fresh and re-scan.
- Check whether the vulnerability database itself was updated between the
  two scans (a CVE disclosed between your local scan and the CI run).

## DAST Failures

**ZAP flags an alert that's a known/accepted risk**
- Add a scoped rule exclusion in ZAP's context config rather than lowering
  the overall scan's failure threshold.

**DAST scan can't authenticate against the target**
- Verify the scan's auth script/session handling matches the app's actual
  login flow (common cause: CSRF tokens or MFA breaking a scripted login).

## Kubernetes Policy Failures

**Gatekeeper/Kyverno blocks a legitimate deployment**
- Check `validationFailureAction` — start new policies in `audit`/`warn`
  mode, observe for false positives, then switch to `enforce` once tuned.
- Use narrowly scoped `match` selectors (namespace, label) so a new policy
  doesn't apply org-wide before it's been validated.

## CSPM / Compliance Failures

**Security Hub/Config shows a finding for a resource created outside Terraform**
- Reconcile the drift the same way as Terraform state drift — decide
  whether the manual change was legitimate (bring it under IaC management)
  or should be reverted (see the Terraform troubleshooting notes on drift).

**A Sentinel/OPA policy blocks an apply that should be allowed**
- Check the policy's enforcement level — soft-mandatory policies support an
  authorized override; confirm the reviewer actually has override
  permission rather than assuming the policy is simply wrong.

[⬆ Back to top](#top)

---

# 23. CLI Command Cheat Sheet

```bash
# SAST
semgrep --config "p/owasp-top-ten" src/
sonar-scanner -Dsonar.projectKey=app -Dsonar.host.url=$SONAR_URL

# SCA
snyk test --severity-threshold=high
npm audit --audit-level=high
pip-audit -r requirements.txt
trivy fs --severity HIGH,CRITICAL .

# Secrets
gitleaks detect --source . --exit-code 1
git secrets --scan

# IaC
checkov -d . --framework terraform --compact --quiet
tfsec . --minimum-severity HIGH
terrascan scan -i terraform -d .

# Containers
trivy image --severity HIGH,CRITICAL myapp:latest
grype myapp:latest --fail-on high
docker build --no-cache -t myapp:latest .

# DAST
docker run --rm -v $(pwd):/zap/wrk/:rw ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py -t https://staging.app.company.com

# Supply chain
syft myapp:latest -o cyclonedx-json > sbom.json
grype sbom:sbom.json
cosign sign --yes myapp:latest
cosign verify --certificate-identity-regexp ".*" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com" myapp:latest

# Cloud posture
aws securityhub get-findings --filters '{"SeverityLabel":[{"Value":"CRITICAL","Comparison":"EQUALS"}]}'
aws guardduty list-findings --detector-id <id>
prowler aws --severity critical high

# Compliance
conftest test plan.json --policy policy/
inspec exec controls/ -t ssh://user@host --sudo
```

[⬆ Back to top](#top)

---

# 24. Study Checklist

- [ ] Explain DevSecOps vs DevOps, and what "shift-left" actually means in
      practice.
- [ ] Run a STRIDE threat model on a simple system diagram.
- [ ] Configure a SAST scan (Semgrep or SonarQube) with a quality gate.
- [ ] Configure an SCA scan and write a time-boxed exception for a
      no-fix-available finding.
- [ ] Set up gitleaks as both a pre-commit hook and a CI gate.
- [ ] Scan a Terraform configuration with Checkov and fix a real finding.
- [ ] Harden a Dockerfile: pinned digest, non-root user, multi-stage build.
- [ ] Run a DAST baseline scan against a staging environment.
- [ ] Write a Kubernetes NetworkPolicy implementing default-deny.
- [ ] Write an OPA/Gatekeeper or Kyverno policy and test it in audit mode
      before enforce.
- [ ] Generate an SBOM and sign a container image with cosign.
- [ ] Explain the SLSA levels and what distinguishes each.
- [ ] Set up a Config rule or Sentinel/OPA policy that blocks a specific
      insecure configuration.
- [ ] Write an incident response runbook skeleton for a specific scenario
      (leaked credential, compromised container).
- [ ] Explain how you'd measure whether a DevSecOps program is actually
      working (metrics, not just tool coverage).

[⬆ Back to top](#top)
