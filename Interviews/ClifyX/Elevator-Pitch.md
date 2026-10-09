# Olalekan Ogundare — Elevator Pitch (Storage Specialist / S3)

Tailored to the ClifyX job description's mandatory skills (Big Data,
Hadoop, S3, IaC, Terraform, CI/CD, AWS, Python) and responsibilities
(object storage design/operation, lifecycle policies, encryption,
data-platform support, cost/capacity optimization, reporting,
operational documentation). Built from
[Olalekan G. Ogundare — Storage Specialist (S3).docx](Olalekan%20G.%20Ogundare%20_%20Storage%20Specialist%20\(S3\).docx)
in this folder, plus the Hadoop/Spark/EMR background confirmed real in
the main resume (not listed on this particular resume variant, but the
same actual experience). See also
[Interview-Questions.md](Interview-Questions.md) and
[STAR-Scenarios.md](STAR-Scenarios.md) in this folder.

---

## Full Version

> "I'm a Storage Specialist and Senior Cloud Infrastructure Engineer
> with over a decade of experience, grounded in enterprise storage
> fundamentals before I ever touched the cloud — I spent years leading
> SAN/NAS infrastructure at enterprise scale (Hitachi, EMC VMAX/VSP,
> NetApp) and architecting replication and disaster recovery solutions
> that cut recovery time 40%. Object storage design isn't abstract to
> me; it's the same storage discipline I built my career on, applied to
> a different platform.
>
> On AWS, I've built and operated S3 alongside FSx for Lustre for
> large-scale data processing, and used Hadoop and Apache Spark on AWS
> EMR for big data and ETL workloads — all provisioned through Terraform,
> with remote state management and policy-as-code gates via Sentinel and
> OPA so every storage and infrastructure change is reviewed, not ad
> hoc. I've built the CI/CD pipelines around that in Jenkins, GitHub
> Actions, and Azure DevOps, and I script the operational side in
> Python.
>
> Security and cost are built into how I run storage, not bolted on
> afterward: encryption at rest and in transit via KMS, least-privilege
> IAM access controls, and FinOps-driven lifecycle policies and
> rightsizing that delivered 20-25% sustained infrastructure cost
> savings in my most recent role. I also bring real discipline around
> operational documentation — I've built runbooks and templates that
> measurably cut incident resolution time, which matters as much for a
> storage platform as the technical design itself."

~230 words, roughly 85-95 seconds spoken.

### Tight ~45-Second Version

Drops the SAN/NAS origin story and the security/documentation closing
paragraph, keeping the direct mandatory-skills match (S3, Hadoop/Spark/
EMR, Terraform, CI/CD) front and center — every sentence below is
lifted verbatim from the full version above.

> "I'm a Storage Specialist and Senior Cloud Infrastructure Engineer
> with over a decade of experience. On AWS, I've built and operated S3
> alongside FSx for Lustre for large-scale data processing, and used
> Hadoop and Apache Spark on AWS EMR for big data and ETL workloads —
> all provisioned through Terraform, with remote state management and
> policy-as-code gates via Sentinel and OPA so every storage and
> infrastructure change is reviewed, not ad hoc. I've built the CI/CD
> pipelines around that in Jenkins, GitHub Actions, and Azure DevOps,
> and I script the operational side in Python."

~90 words, roughly 35-40 seconds spoken.

---

## Mapping to the Job Description

| Requirement | Covered By |
|---|---|
| Big Data, Hadoop | AWS EMR (Hadoop, Apache Spark) — *from the main resume's Big Data & Analytics skills, not listed on this specific resume variant* |
| S3 | Enterprise storage background (SAN/NAS) + hands-on AWS S3 across every cloud role |
| IaC, Terraform | Reusable Terraform modules, remote state (S3 backend + DynamoDB locking), Sentinel/OPA policy gates |
| CI/CD | Jenkins, GitHub Actions, Azure DevOps, Bitbucket CI/CD |
| AWS | 10+ years across EC2, S3, EBS, EFS, FSx, RDS, Lambda, IAM, KMS |
| Python | Listed in Programming & Scripting skills |
| Storage performance & lifecycle policies | FSx Lustre tuning, automated FSx lifecycle policies, backup/DR (Avamar, SRDF, TrueCopy) |
| Data security & encryption | KMS encryption at rest/in transit, least-privilege IAM, Service Control Policies |
| Cost & capacity optimization | FinOps cost governance — rightsizing, Savings Plans, 20–25% sustained savings |
| Operational documentation | Explicit bullet at Computer Warehouse Ltd. — "documentation and operational templates that reduced... incident resolution by 25%" |

[⬆ Back to top](#olalekan-ogundare--elevator-pitch-storage-specialist--s3)
