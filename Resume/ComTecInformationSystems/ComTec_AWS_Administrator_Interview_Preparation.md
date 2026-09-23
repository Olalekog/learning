# ComTec Information Systems — AWS Administrator Interview Preparation

**Prepared for:** Olalekan Gabriel Ogundare  
**Role:** AWS Administrator  
**Contents:** 36 interview questions and sample answers across 12 focus areas

Answers use “I would” for scenarios. Adapt them to your actual experience, and distinguish production work from labs or conceptual knowledge.

## Index

| Focus area | Questions |
| --- | --- |
| [1. EC2 administration and patching](#1-ec2-administration-and-patching) | 1–3 |
| [2. S3 storage and security](#2-s3-storage-and-security) | 4–6 |
| [3. Terraform and CloudFormation](#3-terraform-and-cloudformation) | 7–9 |
| [4. IAM and IAM Identity Center](#4-iam-and-iam-identity-center) | 10–12 |
| [5. Organizations, Control Tower, and Landing Zone Accelerator](#5-organizations-control-tower-and-landing-zone-accelerator) | 13–15 |
| [6. Security monitoring and incident response](#6-security-monitoring-and-incident-response) | 16–18 |
| [7. ECS, Lambda, and API Gateway](#7-ecs-lambda-and-api-gateway) | 19–21 |
| [8. AWS Glue and ETL](#8-aws-glue-and-etl) | 22–24 |
| [9. EMR Serverless and Apache Iceberg](#9-emr-serverless-and-apache-iceberg) | 25–27 |
| [10. Redshift, Snowflake, and DynamoDB](#10-redshift-snowflake-and-dynamodb) | 28–30 |
| [11. Secrets Manager, KMS, and Bedrock](#11-secrets-manager-kms-and-bedrock) | 31–33 |
| [12. Availability, recovery, and government cloud](#12-availability-recovery-and-government-cloud) | 34–36 |
| [Reference documentation](#reference-documentation) | Official sources |

## 1. EC2 administration and patching

### 1. An EC2 instance is running, but users cannot access the application. How would you troubleshoot?

I would determine whether the issue affects one instance or the entire application. I would check EC2 status checks, load balancer target health, security groups, routes, and network ACLs. Inside the server, I would verify that the application is running and listening on the correct port, then examine CPU, memory, disk space, and logs. I would test locally and through the user’s access path to isolate the failure.

### 2. Why might an EC2 instance fail to appear in Systems Manager?

I would check that SSM Agent is installed and running, that the instance has the required IAM permissions, and that it can reach the appropriate Systems Manager endpoints over HTTPS. For a private instance, I would inspect its NAT connectivity or VPC endpoints, endpoint security groups, and DNS resolution. I would also verify the account and Region before reviewing agent logs.

### 3. What would you do if patching caused an application failure?

I would stop the remaining patch rollout and assess the affected capacity. For redundant applications, I would remove unhealthy instances from service and restore capacity using a known-good image. For stateful servers, I would follow the tested recovery procedure and coordinate with the application owner. After restoring service, I would investigate the patch dependency, revise testing, and resume only after validation.

## 2. S3 storage and security

### 4. A user has S3 read permission but receives AccessDenied. What would you check?

I would confirm the actual caller identity and requested operation. Listing a bucket and reading an object require different permissions and resource scopes. I would then inspect the bucket policy, SCPs, permission boundaries, session policies, and VPC endpoint policy for restrictions. If the object uses SSE-KMS, I would also check KMS decrypt authorization. For cross-account objects, I would investigate ownership where relevant.

### 5. How would you protect S3 data against accidental deletion?

I would enable versioning and define recovery and retention requirements. For stronger protection, I would consider Object Lock and a separately controlled backup or replication destination. I would restrict deletion permissions and protect the encryption keys. I would also test restoration because retaining object versions is useful only if the team can recover the required data within its recovery target.

### 6. How would you reduce S3 costs without affecting business requirements?

I would review storage usage, access patterns, request costs, and retention obligations. I would use lifecycle policies to transition suitable objects, expire unnecessary noncurrent versions, and remove incomplete multipart uploads. Before moving data to archival tiers, I would evaluate retrieval time, retrieval cost, and minimum storage duration. I would measure the results rather than assuming the lowest storage price produces the lowest total cost.

## 3. Terraform and CloudFormation

### 7. How would you structure Terraform for multiple environments?

I would create reusable modules and separate environment configurations and state. Each environment would have its own deployment permissions and inputs. Changes would pass formatting, validation, security checks, and plan review before deployment. Production would require approval, and the pipeline would apply the reviewed plan. I would also pin dependencies and avoid sharing state between unrelated workloads.

### 8. How do you secure Terraform state and prevent simultaneous changes?

I would store state in a restricted, encrypted S3 backend with versioning and enable state locking. Supported Terraform versions can use S3 lockfiles through `use_lockfile = true`. I would limit access to deployment identities and authorized operators because state can contain secrets. Marking a value `sensitive` hides it from normal output but does not automatically remove it from state.

### 9. How would you handle infrastructure drift?

I would run a Terraform plan and investigate differences between the declared configuration and deployed resources. I would determine whether each change was authorized and whether it should be preserved. Approved changes should be represented in code; unauthorized changes should be corrected through a reviewed deployment. A refresh-only operation updates Terraform’s recorded state—it does not, by itself, reconcile the configuration or repair infrastructure.

## 4. IAM and IAM Identity Center

### 10. How would you provide access to multiple AWS accounts through IAM Identity Center?

I would connect the approved identity source, organize users into job-based groups, and assign permission sets to the required accounts. I would separate administrative, operational, and read-only access, configure appropriate session durations, and enforce MFA through the identity setup. Permission sets define the account permissions available to assigned users and groups.

### 11. What is the difference between a role trust policy and a permissions policy?

A trust policy defines who or what can assume a role. A permissions policy defines what the assumed role can do. For example, a CI/CD role might trust a specific OIDC provider and repository context, while its permissions allow deployment actions. When troubleshooting, I first separate failure to assume the role from failure to perform an action after assumption.

### 12. How would you integrate a third-party system securely with AWS?

I would prefer temporary credentials and role-based access over long-lived access keys. For a vendor assuming a cross-account role, I would restrict the trusted principal and use the vendor’s external ID where appropriate to address the confused-deputy risk. I would scope permissions to the required resources, enable auditing, and document how access is revoked when the integration ends.

## 5. Organizations, Control Tower, and Landing Zone Accelerator

### 13. Do service control policies grant access?

No. SCPs establish permission limits for affected accounts; they do not grant permissions. An identity still needs an applicable allow, and an explicit SCP deny can block an otherwise permitted action. I would test SCP changes in a limited organizational unit before broader deployment and verify that essential operations continue to work.

### 14. How would you organize a multi-account AWS environment?

I would separate workloads according to environment, ownership, and security requirements. I would use dedicated accounts for centralized logging and security operations, then organize workload accounts into appropriate organizational units. I would establish identity access, account provisioning, network connectivity, budgets, and baseline controls. I would keep application workloads out of the management account.

### 15. What does Landing Zone Accelerator add to Control Tower?

Control Tower helps establish and govern a multi-account landing zone. Landing Zone Accelerator provides configurable automation for additional networking, security, logging, and operational requirements. I would manage its configuration through version control, review changes, and test deployments carefully because foundation changes can affect many accounts. Together, the services support a more comprehensive cloud foundation.

## 6. Security monitoring and incident response

### 16. How do Security Hub, GuardDuty, Inspector, and Config differ?

GuardDuty focuses on threat detection. Inspector identifies supported workload vulnerabilities and exposures. Config records resource configurations and evaluates configuration rules. Security Hub CSPM evaluates security posture, while Security Hub correlates security findings to help prioritize exposures. I would use these services together and connect findings to a defined response process.

### 17. How would you respond to a suspected compromised EC2 instance?

I would validate the finding, assess its scope, and follow the incident-response runbook. I would isolate the instance using an approved approach while preserving access needed for investigation. I would preserve relevant logs and disk evidence, investigate credentials and connected resources, and restore service from a trusted image. I would coordinate credential containment and recovery with security and application teams.

### 18. How would you reduce alert fatigue?

I would define severity using business impact and route alerts to clear owners. I would remove duplicates, tune thresholds and evaluation periods, and suppress expected maintenance events using controlled rules. Every page should require a meaningful action. I would review false positives and missed incidents regularly, and include diagnostic context and a runbook in each actionable alert.

## 7. ECS, Lambda, and API Gateway

### 19. What is the difference between an ECS task role and task execution role?

The task role gives application code inside the container permission to access AWS services, such as S3 or DynamoDB. The execution role gives the ECS or Fargate agent permissions needed to start and operate the task, such as pulling an image or delivering logs. I would investigate startup failures and application authorization failures against the appropriate role.

### 20. An ECS deployment repeatedly replaces tasks. How would you troubleshoot?

I would inspect service events, stopped-task reasons, exit codes, and application logs. I would check image availability, startup configuration, secrets access, CPU and memory limits, and networking. If a load balancer is involved, I would verify the health-check path, port, expected response, and startup grace period. I would restore the previous working task definition if the deployment is causing an outage.

### 21. API Gateway returns errors when invoking Lambda. What would you inspect?

I would correlate the API request with API Gateway and Lambda logs. I would check invocation permissions, integration configuration, request handling, and the expected response format. I would then review Lambda errors, duration, throttling, and downstream dependencies. If the function uses a VPC, I would examine its routes and service connectivity. I would distinguish authentication failures from backend failures before changing anything.

## 8. AWS Glue and ETL

### 22. What is the difference between a Glue crawler, Data Catalog, and ETL job?

A crawler discovers data structures and can create or update metadata. The Data Catalog stores metadata such as table definitions and locations. An ETL job reads, transforms, and writes data. A crawler does not perform the application’s business transformation, and the Data Catalog does not replace the underlying data storage.

### 23. A Glue job succeeds but produces duplicate records. What would you investigate?

I would examine retries, overlapping input paths, job-bookmark configuration, and the destination write strategy. I would check whether repeated execution processes the same source records and whether the target supports a safe merge. I would design processing to be idempotent using stable business keys and controlled writes. I would not assume incremental source tracking alone guarantees duplicate-free output.

### 24. How would you troubleshoot a slow Glue job?

I would review job metrics and Spark execution details to identify data skew, expensive shuffles, small files, or insufficient resources. I would reduce unnecessary columns and records, improve partition pruning, and optimize joins and file sizes. I would adjust worker capacity after identifying the bottleneck, then compare runtime and cost using a representative workload.

## 9. EMR Serverless and Apache Iceberg

### 25. When would you choose Glue versus EMR Serverless?

I would consider Glue for managed data-integration workflows that benefit from its ETL tooling and catalog integration. I would consider EMR Serverless for Spark or Hive workloads needing the EMR runtime and greater control over processing configuration. Both can support analytical pipelines, so I would evaluate compatibility, operational effort, runtime, and cost with the actual workload.

### 26. An EMR Serverless job cannot read encrypted S3 data. What would you check?

I would verify the job execution role, S3 object and bucket permissions, bucket policy, and KMS decrypt authorization. I would check endpoint policies and organizational restrictions, then review the exact failing operation. If the job accesses cataloged tables, I would also inspect Glue Data Catalog permissions and Lake Formation authorization where enabled.

### 27. What is Apache Iceberg, and what maintenance does it require?

Iceberg is an open table format for analytical data, with metadata and snapshots that support reliable table updates and evolution. Operational tasks include compacting small files and managing snapshot retention. I would use supported table-maintenance procedures and avoid manually deleting S3 files, because files may still be referenced by valid snapshots or active operations.

## 10. Redshift, Snowflake, and DynamoDB

### 28. How would you troubleshoot a slow Redshift query?

I would determine whether the query is waiting for resources or executing slowly. I would inspect its execution plan, scanned data, joins, skew, spill, and competing workloads. I would review table design, statistics, and workload management before adding capacity. I would also compare the query with its previous behavior to identify changes in data volume or SQL.

### 29. How would you configure Snowflake access to S3 securely?

I would use a Snowflake storage integration backed by a scoped AWS IAM role. I would configure the role trust relationship with the Snowflake-provided principal and external ID, restrict allowed storage locations, and grant only required S3 and KMS permissions. I would test the external stage and verify that unrelated buckets remain inaccessible.

### 30. How would you investigate DynamoDB throttling?

I would examine the throttling reason and affected table or index. Possible causes include insufficient provisioned capacity, account limits, configured on-demand limits, or hot partitions. I would review traffic distribution and partition-key design, then apply the appropriate capacity or application change. Retries should use backoff and jitter, but increasing total capacity alone may not resolve concentrated access to a hot key.

## 11. Secrets Manager, KMS, and Bedrock

### 31. What is the difference between Secrets Manager and KMS?

Secrets Manager stores and manages secrets such as database credentials and API tokens. KMS manages cryptographic keys and performs supported cryptographic operations. Secrets Manager uses KMS to protect stored secret values. Rotating a KMS key does not change a database password; credential rotation requires updating the secret and the target system through the appropriate workflow.

### 32. An application fails after secret rotation. How would you troubleshoot?

I would check whether rotation completed successfully and whether the secret matches the target system’s current credentials. I would inspect the application’s caching behavior, connection pools, permissions, and network access. I would verify which secret version the application retrieves and whether it refreshes credentials correctly. Any rollback must keep the stored secret and actual database credentials synchronized.

### 33. How would you securely support a Bedrock application?

I would scope model-invocation permissions to the application’s needs and verify model availability in the selected Region. I would work with security and application teams on input data, retrieval access, output handling, and logging. I would monitor errors, latency, usage, and cost, and evaluate guardrails against the use case. Bedrock provides managed foundation-model access, but application security still requires deliberate design.

## 12. Availability, recovery, and government cloud

### 34. How would you design a highly available AWS application?

I would start with the availability target and identify every critical dependency. I would distribute application capacity across Availability Zones, use health-based routing, and select suitable database resilience options. I would include automated recovery, monitoring, backups, and tested runbooks. I would also test dependency failures because redundant application servers cannot compensate for an unprotected database or identity dependency.

### 35. What is the difference between RTO and RPO, and how would you validate them?

RTO is the target time to restore service after disruption. RPO is the acceptable amount of data loss measured in time. I would select backup and recovery methods based on those targets, then run recovery exercises. Validation includes application checks, data checks, access, networking, and measured restoration time—not simply confirmation that a backup job succeeded.

### 36. What changes when administering AWS GovCloud compared with commercial AWS?

Core administration principles still apply, but GovCloud uses a separate AWS partition and isolated authentication. I would verify service availability, endpoints, ARN formats, credentials, and the customer’s operating requirements. I would avoid assuming commercial deployments can be copied unchanged. I would also distinguish AWS’s compliance capabilities from the customer’s responsibility to configure and operate its workloads correctly.

## Reference documentation

Official documentation referenced in preparing the interview answers:

- **Terraform state (Q8):** [S3 backend and locking](https://developer.hashicorp.com/terraform/language/backend/s3); [Sensitive data](https://developer.hashicorp.com/terraform/language/manage-sensitive-data).
- **Identity Center (Q10):** [Permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsets.html).
- **Governance (Q15):** [Landing Zone Accelerator](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/).
- **Security services (Q16):** [Introduction to Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html); [Security Hub FAQs](https://aws.amazon.com/security-hub/faqs/).
- **ECS roles (Q19):** [Task execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html); [Task IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html).
- **Glue (Q22, Q25):** [Catalog and crawlers](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html); [Glue concepts](https://docs.aws.amazon.com/glue/latest/dg/components-key-concepts.html); [How Glue works](https://docs.aws.amazon.com/glue/latest/dg/how-it-works.html).
- **EMR (Q25–26):** [Amazon EMR documentation](https://docs.aws.amazon.com/emr/); [Iceberg with EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/using-iceberg.html).
- **Iceberg (Q27):** [Reliability](https://iceberg.apache.org/docs/1.5.1/reliability/); [Table specification](https://iceberg.apache.org/spec/).
- **Snowflake (Q29):** [Configure an S3 storage integration](https://docs.snowflake.com/en/user-guide/data-load-s3-config-storage-integration.html).
- **DynamoDB (Q30):** [Throttling resolution guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/troubleshooting-throttling-diagnostics.html); [Diagnosing throttling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/throttling-diagnosing-workflow.html).
- **Bedrock (Q33):** [Bedrock overview](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html).
- **GovCloud (Q36):** [Differences from standard Regions](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-differences.html); [AWS partitions](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/partitions.html).
