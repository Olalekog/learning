<a id="top"></a>

# United Airlines Senior AWS DevOps Interview Guide

Prepared for Olalekan Gabriel Ogundare

This guide aligns the job requirements with Olalekan's experience in AWS production support, Terraform, EKS, CI/CD, observability, security, reliability, and technical leadership. Answers are intentionally concise enough for approximately 30 to 60 seconds of spoken delivery. Replace any example detail with the exact facts of the situation if an interviewer asks for deeper evidence.

## Index

| Section | Questions |
|---|---:|
| [Essential Service and Technology Definitions](#essential-service-and-technology-definitions) | — |
| [1 AWS Production Support and Troubleshooting](#1-aws-production-support-and-troubleshooting) | 1–15 |
| [2 Terraform and Infrastructure as Code](#2-terraform-and-infrastructure-as-code) | 16–35 |
| [3 Kubernetes and Amazon EKS](#3-kubernetes-and-amazon-eks) | 36–57 |
| [4 CI CD and GitOps](#4-ci-cd-and-gitops) | 58–70 |
| [5 Observability and Incident Response](#5-observability-and-incident-response) | 71–81 |
| [6 Security and Operational Readiness](#6-security-and-operational-readiness) | 82–90 |
| [7 Reliability Disaster Recovery Performance and Cost](#7-reliability-disaster-recovery-performance-and-cost) | 91–100 |
| [8 Leadership and Behavioral Questions](#8-leadership-and-behavioral-questions) | 101–115 |
| [9 Scenario Based Questions](#9-scenario-based-questions) | 116–125 |
| [Questions to Ask the Interviewer](#questions-to-ask-the-interviewer) | — |
| [Final Interview Reminder](#final-interview-reminder) | — |

<details>
<summary>All 125 questions (click to expand)</summary>

**[1 AWS Production Support and Troubleshooting](#1-aws-production-support-and-troubleshooting)**

1. [Describe your experience supporting business-critical AWS workloads in production.](#1-describe-your-experience-supporting-business-critical-aws-workloads-in-production)
2. [Walk me through how you would investigate a production application that suddenly became unavailable.](#2-walk-me-through-how-you-would-investigate-a-production-application-that-suddenly-became-unavailable)
3. [How do you lead root-cause analysis after a major incident?](#3-how-do-you-lead-root-cause-analysis-after-a-major-incident)
4. [How would you troubleshoot an ECS task that repeatedly stops or fails health checks?](#4-how-would-you-troubleshoot-an-ecs-task-that-repeatedly-stops-or-fails-health-checks)
5. [How would you diagnose an EKS application returning HTTP 502 or 503 errors?](#5-how-would-you-diagnose-an-eks-application-returning-http-502-or-503-errors)
6. [What is the difference between an ECS task execution role and a task role?](#6-what-is-the-difference-between-an-ecs-task-execution-role-and-a-task-role)
7. [How would you troubleshoot a Lambda function experiencing timeouts or throttling?](#7-how-would-you-troubleshoot-a-lambda-function-experiencing-timeouts-or-throttling)
8. [How do you diagnose an application that cannot access an S3 bucket?](#8-how-do-you-diagnose-an-application-that-cannot-access-an-s3-bucket)
9. [How would you troubleshoot high latency or connection failures in DocumentDB?](#9-how-would-you-troubleshoot-high-latency-or-connection-failures-in-documentdb)
10. [What causes DynamoDB throttling, and how would you resolve it?](#10-what-causes-dynamodb-throttling-and-how-would-you-resolve-it)
11. [How do you troubleshoot AWS networking problems?](#11-how-do-you-troubleshoot-aws-networking-problems)
12. [How would you investigate an unexpected IAM AccessDenied error?](#12-how-would-you-investigate-an-unexpected-iam-accessdenied-error)
13. [Which AWS tools do you use for logs, metrics, traces, and audit events?](#13-which-aws-tools-do-you-use-for-logs-metrics-traces-and-audit-events)
14. [Explain a critical AWS production incident you resolved independently.](#14-explain-a-critical-aws-production-incident-you-resolved-independently)
15. [How do you prevent the same incident from happening again?](#15-how-do-you-prevent-the-same-incident-from-happening-again)

**[2 Terraform and Infrastructure as Code](#2-terraform-and-infrastructure-as-code)**

16. [Describe the most complex AWS infrastructure you have provisioned using Terraform.](#16-describe-the-most-complex-aws-infrastructure-you-have-provisioned-using-terraform)
17. [How do you design reusable Terraform modules?](#17-how-do-you-design-reusable-terraform-modules)
18. [What is the difference between a root module and a child module?](#18-what-is-the-difference-between-a-root-module-and-a-child-module)
19. [How do you manage Terraform remote state securely?](#19-how-do-you-manage-terraform-remote-state-securely)
20. [What would you do if a Terraform state file became corrupted or unavailable?](#20-what-would-you-do-if-a-terraform-state-file-became-corrupted-or-unavailable)
21. [How do you detect and resolve infrastructure drift?](#21-how-do-you-detect-and-resolve-infrastructure-drift)
22. [How do you review a Terraform execution plan?](#22-how-do-you-review-a-terraform-execution-plan)
23. [How do you import an existing AWS resource into Terraform?](#23-how-do-you-import-an-existing-aws-resource-into-terraform)
24. [How do you handle resource dependencies?](#24-how-do-you-handle-resource-dependencies)
25. [What is the difference between implicit and explicit dependencies?](#25-what-is-the-difference-between-implicit-and-explicit-dependencies)
26. [How do you manage Terraform module versions?](#26-how-do-you-manage-terraform-module-versions)
27. [How do you promote Terraform changes from development to production?](#27-how-do-you-promote-terraform-changes-from-development-to-production)
28. [How do you prevent accidental deletion of critical resources?](#28-how-do-you-prevent-accidental-deletion-of-critical-resources)
29. [What happens when two engineers run Terraform against the same state?](#29-what-happens-when-two-engineers-run-terraform-against-the-same-state)
30. [How do you troubleshoot a partially failed Terraform deployment?](#30-how-do-you-troubleshoot-a-partially-failed-terraform-deployment)
31. [Which Terraform validation and security tools have you used?](#31-which-terraform-validation-and-security-tools-have-you-used)
32. [How have you integrated Terraform into CI/CD?](#32-how-have-you-integrated-terraform-into-cicd)
33. [How do Sentinel and OPA improve Terraform governance?](#33-how-do-sentinel-and-opa-improve-terraform-governance)
34. [What standards do you enforce during Terraform code review?](#34-what-standards-do-you-enforce-during-terraform-code-review)
35. [Have you built Terraform modules directly or mainly consumed existing modules?](#35-have-you-built-terraform-modules-directly-or-mainly-consumed-existing-modules)

**[3 Kubernetes and Amazon EKS](#3-kubernetes-and-amazon-eks)**

36. [Describe your production experience managing EKS clusters.](#36-describe-your-production-experience-managing-eks-clusters)
37. [Explain the Kubernetes control plane and worker-node architecture.](#37-explain-the-kubernetes-control-plane-and-worker-node-architecture)
38. [How do you troubleshoot a pod in CrashLoopBackOff?](#38-how-do-you-troubleshoot-a-pod-in-crashloopbackoff)
39. [How do you troubleshoot a pod stuck in Pending?](#39-how-do-you-troubleshoot-a-pod-stuck-in-pending)
40. [What would you check when a pod cannot connect to another service?](#40-what-would-you-check-when-a-pod-cannot-connect-to-another-service)
41. [How do readiness liveness and startup probes differ?](#41-how-do-readiness-liveness-and-startup-probes-differ)
42. [How do you manage Kubernetes deployments using Helm?](#42-how-do-you-manage-kubernetes-deployments-using-helm)
43. [How do Helm values templates releases and rollbacks work?](#43-how-do-helm-values-templates-releases-and-rollbacks-work)
44. [How do you troubleshoot a failed Helm deployment?](#44-how-do-you-troubleshoot-a-failed-helm-deployment)
45. [How do you perform an EKS upgrade with minimal disruption?](#45-how-do-you-perform-an-eks-upgrade-with-minimal-disruption)
46. [How do you configure autoscaling in EKS?](#46-how-do-you-configure-autoscaling-in-eks)
47. [Compare HPA Cluster Autoscaler and Karpenter.](#47-compare-hpa-cluster-autoscaler-and-karpenter)
48. [How do you integrate AWS IAM with Kubernetes service accounts?](#48-how-do-you-integrate-aws-iam-with-kubernetes-service-accounts)
49. [Explain the difference between AWS IAM and Kubernetes RBAC.](#49-explain-the-difference-between-aws-iam-and-kubernetes-rbac)
50. [How do you secure a multi-tenant EKS cluster?](#50-how-do-you-secure-a-multi-tenant-eks-cluster)
51. [How do Services Ingress and AWS load balancers work together?](#51-how-do-services-ingress-and-aws-load-balancers-work-together)
52. [How do you troubleshoot DNS resolution inside EKS?](#52-how-do-you-troubleshoot-dns-resolution-inside-eks)
53. [How do you collect and centralize Kubernetes logs?](#53-how-do-you-collect-and-centralize-kubernetes-logs)
54. [What are Kubernetes network policies?](#54-what-are-kubernetes-network-policies)
55. [How do you manage Kubernetes secrets securely?](#55-how-do-you-manage-kubernetes-secrets-securely)
56. [How would you recover from a failed Kubernetes deployment?](#56-how-would-you-recover-from-a-failed-kubernetes-deployment)
57. [Describe your experience deploying distributed applications.](#57-describe-your-experience-deploying-distributed-applications)

**[4 CI CD and GitOps](#4-ci-cd-and-gitops)**

58. [Describe a production CI CD pipeline you implemented from start to finish.](#58-describe-a-production-ci-cd-pipeline-you-implemented-from-start-to-finish)
59. [How do you integrate Terraform validation planning approval and deployment into a pipeline?](#59-how-do-you-integrate-terraform-validation-planning-approval-and-deployment-into-a-pipeline)
60. [What security gates should be included in a cloud infrastructure pipeline?](#60-what-security-gates-should-be-included-in-a-cloud-infrastructure-pipeline)
61. [How do you prevent unreviewed changes from reaching production?](#61-how-do-you-prevent-unreviewed-changes-from-reaching-production)
62. [How do you securely authenticate a CI CD pipeline to AWS?](#62-how-do-you-securely-authenticate-a-ci-cd-pipeline-to-aws)
63. [Why is OIDC preferred over long-lived AWS access keys?](#63-why-is-oidc-preferred-over-long-lived-aws-access-keys)
64. [How do you troubleshoot an invalid role ARN or OIDC trust-policy failure?](#64-how-do-you-troubleshoot-an-invalid-role-arn-or-oidc-trust-policy-failure)
65. [Describe your experience with GitHub Actions Jenkins GitLab CI or Harness.](#65-describe-your-experience-with-github-actions-jenkins-gitlab-ci-or-harness)
66. [How have you used Argo CD or another GitOps platform?](#66-how-have-you-used-argo-cd-or-another-gitops-platform)
67. [How do you promote Kubernetes changes across development UAT and production?](#67-how-do-you-promote-kubernetes-changes-across-development-uat-and-production)
68. [How do you design a safe rollback strategy?](#68-how-do-you-design-a-safe-rollback-strategy)
69. [How do you manage configuration differences between environments?](#69-how-do-you-manage-configuration-differences-between-environments)
70. [What is your approach to artifact and container-image versioning?](#70-what-is-your-approach-to-artifact-and-container-image-versioning)

**[5 Observability and Incident Response](#5-observability-and-incident-response)**

71. [What does production readiness mean to you?](#71-what-does-production-readiness-mean-to-you)
72. [What metrics would you monitor for ECS EKS Lambda DynamoDB and DocumentDB?](#72-what-metrics-would-you-monitor-for-ecs-eks-lambda-dynamodb-and-documentdb)
73. [How do you design useful alerts without creating alert fatigue?](#73-how-do-you-design-useful-alerts-without-creating-alert-fatigue)
74. [Explain the difference between logs metrics and traces.](#74-explain-the-difference-between-logs-metrics-and-traces)
75. [How have you used CloudWatch Prometheus Grafana or OpenSearch?](#75-how-have-you-used-cloudwatch-prometheus-grafana-or-opensearch)
76. [How do you establish SLIs and SLOs?](#76-how-do-you-establish-slis-and-slos)
77. [What is your role during a severity-one incident?](#77-what-is-your-role-during-a-severity-one-incident)
78. [How do you communicate technical status during an active incident?](#78-how-do-you-communicate-technical-status-during-an-active-incident)
79. [What should be included in a post-incident report?](#79-what-should-be-included-in-a-post-incident-report)
80. [Describe a time observability identified a problem before a major outage.](#80-describe-a-time-observability-identified-a-problem-before-a-major-outage)
81. [How do you improve MTTD and MTTR?](#81-how-do-you-improve-mttd-and-mttr)

**[6 Security and Operational Readiness](#6-security-and-operational-readiness)**

82. [How do you apply least privilege across AWS and EKS?](#82-how-do-you-apply-least-privilege-across-aws-and-eks)
83. [How do you protect sensitive values used by Terraform and Kubernetes?](#83-how-do-you-protect-sensitive-values-used-by-terraform-and-kubernetes)
84. [How do you secure S3 buckets?](#84-how-do-you-secure-s3-buckets)
85. [How do you implement encryption at rest and in transit?](#85-how-do-you-implement-encryption-at-rest-and-in-transit)
86. [How do GuardDuty Security Hub Inspector Config and CloudTrail work together?](#86-how-do-guardduty-security-hub-inspector-config-and-cloudtrail-work-together)
87. [How do you scan Terraform code and container images?](#87-how-do-you-scan-terraform-code-and-container-images)
88. [How do you handle patching and vulnerability remediation in production?](#88-how-do-you-handle-patching-and-vulnerability-remediation-in-production)
89. [How do you balance security requirements with deployment speed?](#89-how-do-you-balance-security-requirements-with-deployment-speed)
90. [What security controls should be validated before production release?](#90-what-security-controls-should-be-validated-before-production-release)

**[7 Reliability Disaster Recovery Performance and Cost](#7-reliability-disaster-recovery-performance-and-cost)**

91. [How do you design AWS workloads for high availability?](#91-how-do-you-design-aws-workloads-for-high-availability)
92. [How do you determine RTO and RPO requirements?](#92-how-do-you-determine-rto-and-rpo-requirements)
93. [Describe a backup disaster-recovery or failover test you performed.](#93-describe-a-backup-disaster-recovery-or-failover-test-you-performed)
94. [How do you identify and remove single points of failure?](#94-how-do-you-identify-and-remove-single-points-of-failure)
95. [How would you troubleshoot intermittent performance problems?](#95-how-would-you-troubleshoot-intermittent-performance-problems)
96. [How do you perform capacity planning for Kubernetes workloads?](#96-how-do-you-perform-capacity-planning-for-kubernetes-workloads)
97. [How do you improve AWS cost efficiency without compromising reliability?](#97-how-do-you-improve-aws-cost-efficiency-without-compromising-reliability)
98. [Describe your experience with rightsizing Savings Plans Spot and lifecycle policies.](#98-describe-your-experience-with-rightsizing-savings-plans-spot-and-lifecycle-policies)
99. [How do you validate that a disaster-recovery plan will work?](#99-how-do-you-validate-that-a-disaster-recovery-plan-will-work)
100. [What operational checks should be completed before a major production release?](#100-what-operational-checks-should-be-completed-before-a-major-production-release)

**[8 Leadership and Behavioral Questions](#8-leadership-and-behavioral-questions)**

101. [Tell me about yourself and how your experience aligns with this position.](#101-tell-me-about-yourself-and-how-your-experience-aligns-with-this-position)
102. [Why are you interested in working for United Airlines?](#102-why-are-you-interested-in-working-for-united-airlines)
103. [Describe a time you took ownership of an ambiguous production issue.](#103-describe-a-time-you-took-ownership-of-an-ambiguous-production-issue)
104. [Tell me about a major incident you led from detection through resolution.](#104-tell-me-about-a-major-incident-you-led-from-detection-through-resolution)
105. [Describe a technical decision where you explained risks and tradeoffs to leadership.](#105-describe-a-technical-decision-where-you-explained-risks-and-tradeoffs-to-leadership)
106. [Tell me about a disagreement during a code or architecture review.](#106-tell-me-about-a-disagreement-during-a-code-or-architecture-review)
107. [Describe a time you improved an operational process or engineering standard.](#107-describe-a-time-you-improved-an-operational-process-or-engineering-standard)
108. [How do you mentor junior and mid-level engineers?](#108-how-do-you-mentor-junior-and-mid-level-engineers)
109. [How do you balance project delivery with production support?](#109-how-do-you-balance-project-delivery-with-production-support)
110. [Describe a time you made a mistake in production.](#110-describe-a-time-you-made-a-mistake-in-production)
111. [How do you prioritize multiple critical incidents or requests?](#111-how-do-you-prioritize-multiple-critical-incidents-or-requests)
112. [What information do you include in runbooks?](#112-what-information-do-you-include-in-runbooks)
113. [Describe a time automation improved reliability or reduced manual effort.](#113-describe-a-time-automation-improved-reliability-or-reduced-manual-effort)
114. [How do you work with application networking security and product teams?](#114-how-do-you-work-with-application-networking-security-and-product-teams)
115. [What would you focus on during your first 90 days?](#115-what-would-you-focus-on-during-your-first-90-days)

**[9 Scenario Based Questions](#9-scenario-based-questions)**

116. [A production EKS application is unavailable immediately after deployment. Walk through your response.](#116-a-production-eks-application-is-unavailable-immediately-after-deployment-walk-through-your-response)
117. [Terraform proposes replacing a production resource. What do you do?](#117-terraform-proposes-replacing-a-production-resource-what-do-you-do)
118. [An application works in development but fails in production with AccessDenied. How do you investigate?](#118-an-application-works-in-development-but-fails-in-production-with-accessdenied-how-do-you-investigate)
119. [DynamoDB requests are throttled during peak customer activity. How do you stabilize the service?](#119-dynamodb-requests-are-throttled-during-peak-customer-activity-how-do-you-stabilize-the-service)
120. [A Terraform pipeline completed but the expected AWS resource is missing. How do you troubleshoot?](#120-a-terraform-pipeline-completed-but-the-expected-aws-resource-is-missing-how-do-you-troubleshoot)
121. [An EKS pod is healthy but customers cannot access it through the load balancer. What do you check?](#121-an-eks-pod-is-healthy-but-customers-cannot-access-it-through-the-load-balancer-what-do-you-check)
122. [A Helm upgrade failed halfway through production. How do you recover?](#122-a-helm-upgrade-failed-halfway-through-production-how-do-you-recover)
123. [CloudWatch shows increasing latency but CPU and memory are normal. What else do you investigate?](#123-cloudwatch-shows-increasing-latency-but-cpu-and-memory-are-normal-what-else-do-you-investigate)
124. [An engineer manually changed a production AWS resource and created Terraform drift. What do you do?](#124-an-engineer-manually-changed-a-production-aws-resource-and-created-terraform-drift-what-do-you-do)
125. [A major AWS regional disruption affects a critical airline application. How do you coordinate recovery and communication?](#125-a-major-aws-regional-disruption-affects-a-critical-airline-application-how-do-you-coordinate-recovery-and-communication)

</details>

[⬆ Back to top](#top)

---

## Essential Service and Technology Definitions

- **Amazon ECS:** A managed AWS container orchestration service that runs and scales containers using EC2 instances or the serverless AWS Fargate compute engine.
- **Amazon EKS:** A managed Kubernetes service in which AWS operates the Kubernetes control plane while customers manage workloads, access, networking, observability, and either managed nodes, Fargate profiles, or other compute choices.
- **Amazon S3:** Durable object storage used for files, logs, backups, data lakes, and static content. Access is controlled through IAM policies, bucket policies, access points, and block-public-access settings.
- **AWS Lambda:** Event-driven serverless compute that executes code without managing servers. Important operational controls include memory, timeout, concurrency, retries, dead-letter handling, and VPC connectivity.
- **Amazon DynamoDB:** A managed NoSQL key-value and document database designed for low-latency access at scale, with on-demand or provisioned capacity modes.
- **Amazon DocumentDB:** An AWS-managed document database with MongoDB compatibility. It separates compute from distributed storage and requires careful connection, indexing, scaling, and compatibility planning.
- **AWS IAM:** The AWS authorization service for users, roles, and policies. It should be designed around temporary credentials and least-privilege access.
- **Amazon VPC:** A logically isolated AWS network containing subnets, route tables, gateways, security groups, NACLs, endpoints, and DNS settings.
- **Elastic Load Balancing:** AWS-managed load distribution. An Application Load Balancer handles Layer 7 HTTP and HTTPS traffic, while a Network Load Balancer handles high-performance Layer 4 TCP, UDP, and TLS traffic.
- **Amazon CloudWatch:** AWS monitoring and observability service for metrics, logs, alarms, dashboards, and events.
- **AWS CloudTrail:** Records AWS API activity for auditing, security investigation, and change attribution.
- **Terraform:** A declarative infrastructure-as-code tool that compares configuration, state, and provider data to create an execution plan and converge infrastructure toward the desired state.
- **Terraform state:** Terraform's mapping between configuration and real infrastructure. It may contain sensitive data and must be remotely stored, encrypted, versioned, access-controlled, and protected from concurrent writes.
- **Kubernetes:** A container orchestration platform that schedules, scales, networks, and manages containerized workloads through declarative APIs.
- **Helm:** A Kubernetes package manager that combines templates, default values, and release history into reusable charts.
- **GitOps:** An operating model in which Git is the approved source of desired system state and an automated controller, such as Argo CD or Flux, reconciles the target environment to that state.
- **RBAC:** Role-based access control. In Kubernetes, Roles or ClusterRoles define permissions and RoleBindings or ClusterRoleBindings assign them to subjects.
- **IRSA:** IAM Roles for Service Accounts allows an EKS workload to assume a dedicated IAM role through its Kubernetes service account instead of inheriting broad node permissions.
- **Horizontal Pod Autoscaler:** Adjusts the number of pod replicas according to metrics such as CPU, memory, or custom application signals.
- **Cluster Autoscaler:** Adds or removes worker nodes when pods cannot be scheduled or nodes are underutilized.
- **Karpenter:** An open-source Kubernetes node lifecycle project that provisions appropriately sized compute based on pending workload requirements.
- **SLI SLO and SLA:** An SLI is a measured reliability indicator; an SLO is its internal target; an SLA is a formal customer commitment that may carry consequences.
- **RTO and RPO:** Recovery Time Objective is the acceptable restoration time. Recovery Point Objective is the acceptable amount of data loss measured in time.
- **MTTD and MTTR:** Mean Time to Detect measures detection speed, while Mean Time to Restore or Resolve measures recovery speed.

[⬆ Back to top](#top)

---

## 1 AWS Production Support and Troubleshooting

### 1. Describe your experience supporting business-critical AWS workloads in production.

I have more than seven years of AWS experience across regulated financial, healthcare, and consulting environments. At Citi, I supported production platforms using EKS, EC2, S3, IAM, Lambda, RDS, DynamoDB, DocumentDB, CloudWatch, EventBridge, and related services. My responsibilities included incident response, root-cause analysis, automation, security hardening, capacity management, and continuous reliability improvement.

### 2. Walk me through how you would investigate a production application that suddenly became unavailable.

I first confirm impact, scope, recent changes, and whether the failure affects one instance, one Availability Zone, or the whole service. I then trace the request path from DNS and load balancer through networking, compute, application, and data services while reviewing dashboards, logs, traces, health checks, and CloudTrail events. I stabilize the service through rollback, failover, scaling, or traffic isolation, then preserve evidence and lead a blameless root-cause review.

### 3. How do you lead root-cause analysis after a major incident?

I construct a factual timeline from alerts, logs, metrics, traces, deployment records, and operator actions. I distinguish the triggering event from contributing control failures, document customer and business impact, and use techniques such as five whys without blaming individuals. The final review assigns owners and deadlines for corrective actions, updates runbooks and monitoring, and verifies that the actions actually reduce recurrence risk.

### 4. How would you troubleshoot an ECS task that repeatedly stops or fails health checks?

I inspect the ECS service events, stopped-task reason, container exit code, CloudWatch logs, task definition, image tag, environment variables, secrets, CPU and memory limits, and port mappings. I also test target-group health checks, security groups, IAM task and execution roles, service discovery, and dependency connectivity. I correct the failing layer and use a controlled deployment with rollback protection.

### 5. How would you diagnose an EKS application returning HTTP 502 or 503 errors?

I check the load balancer and target health, Ingress configuration, Service selectors, endpoints, pod readiness, application logs, and network policies. A 502 often suggests an invalid or prematurely closed upstream response, while a 503 frequently indicates that no healthy backend is available. I compare the failure with recent Helm or manifest changes, restore healthy capacity, and then address the underlying routing or application issue.

### 6. What is the difference between an ECS task execution role and a task role?

The execution role is used by the ECS agent to perform platform actions such as pulling an image from ECR, retrieving configured secrets, and writing logs. The task role is assumed by the application running inside the container to call AWS APIs such as S3 or DynamoDB. Separating them supports least privilege and clearer troubleshooting.

### 7. How would you troubleshoot a Lambda function experiencing timeouts or throttling?

I review duration, errors, throttles, concurrent executions, memory usage, cold starts, retry behavior, and downstream latency. I validate the timeout and memory settings, reserved concurrency, VPC routing and endpoints, database connection behavior, and service quotas. Depending on the cause, I optimize code, increase memory, tune concurrency, add backoff or queues, reuse connections, or remove unnecessary VPC dependencies.

### 8. How do you diagnose an application that cannot access an S3 bucket?

I reproduce the exact API call and inspect the caller identity, IAM policy, bucket policy, permissions boundary, SCP, KMS key policy, VPC endpoint policy, object ownership, and block-public-access settings. I use CloudTrail and IAM policy simulation to locate the explicit or implicit denial. I then apply the narrowest required permission instead of granting broad S3 access.

### 9. How would you troubleshoot high latency or connection failures in DocumentDB?

I review cluster and instance metrics, connection counts, CPU, memory, storage pressure, replica lag, slow queries, index usage, and application timeouts. I also validate TLS configuration, DNS, security groups, subnet routing, driver compatibility, connection pooling, and retry behavior. The solution may involve index tuning, query changes, better pooling, instance scaling, or failover testing.

### 10. What causes DynamoDB throttling, and how would you resolve it?

Throttling can result from insufficient provisioned capacity, a hot partition, uneven key design, account limits, or a global secondary index with inadequate capacity. I inspect consumed capacity and throttled-request metrics, identify affected keys or indexes, and verify retry behavior. I may enable on-demand mode or auto scaling, improve partition-key distribution, add caching, batch requests, and use exponential backoff with jitter.

### 11. How do you troubleshoot AWS networking problems?

I trace traffic in both directions and validate DNS resolution, routes, security groups, NACLs, gateways, load balancer listeners, target health, and service endpoint configuration. I use VPC Flow Logs, Reachability Analyzer, load balancer logs, `dig`, `curl`, `traceroute`, `ss`, and packet capture when appropriate. I pay close attention to return paths, ephemeral ports, asymmetric routing, and overlapping CIDR ranges.

### 12. How would you investigate an unexpected IAM AccessDenied error?

I capture the failed action, resource ARN, principal, session context, and request conditions from the error and CloudTrail. I evaluate identity policies, resource policies, permissions boundaries, session policies, SCPs, KMS policies, and explicit denies. After identifying the controlling policy, I grant only the specific actions and resources required and validate with the same identity path.

### 13. Which AWS tools do you use for logs, metrics, traces, and audit events?

I use CloudWatch Metrics, Logs, Alarms, dashboards, and Container Insights for operational signals; X-Ray or OpenTelemetry for distributed traces; CloudTrail for API audit activity; and AWS Config for configuration history. I have also integrated Prometheus, Grafana, OpenSearch, Fluent Bit, Kafka or MSK, and ServiceNow to centralize telemetry and incident workflows.

### 14. Explain a critical AWS production incident you resolved independently.

At Citi, I supported high-throughput AWS platforms where application symptoms had to be correlated across infrastructure, Kubernetes, logs, and service dependencies. I used CloudWatch, Prometheus, Grafana, and centralized logging to isolate the failing layer, stabilized the workload, and coordinated the permanent fix. Those observability and response improvements contributed to a 35 percent reduction in incident detection and recovery time.

### 15. How do you prevent the same incident from happening again?

I convert the lessons into durable controls: code fixes, automated tests, safer deployment checks, actionable alerts, capacity thresholds, updated runbooks, and ownership with due dates. I verify corrective actions through failure testing or monitored releases rather than closing them when documentation is written. I also review whether similar systems share the same risk.

[⬆ Back to top](#top)

---

## 2 Terraform and Infrastructure as Code

### 16. Describe the most complex AWS infrastructure you have provisioned using Terraform.

At Citi, I designed reusable Terraform modules and golden templates for VPCs, EC2, ALB, Auto Scaling, RDS, S3, IAM, KMS, EKS, CloudWatch, EventBridge, messaging services, and FSx. These patterns supported development, UAT, and production accounts with remote state, CI/CD approvals, security policies, and standardized observability. The value was repeatable delivery with fewer manual changes and faster provisioning.

### 17. How do you design reusable Terraform modules?

I give each module a clear responsibility, stable inputs and outputs, secure defaults, validation rules, and minimal hidden behavior. I avoid embedding environment-specific values, document examples, version releases, and test common and failure paths. Composition happens in environment root modules, where teams select approved versions and supply configuration.

### 18. What is the difference between a root module and a child module?

The root module is the Terraform configuration executed by the CLI or pipeline and normally represents an environment or deployment unit. A child module is called by another module to encapsulate reusable infrastructure. Root modules handle composition and environment values, while child modules should expose a focused and stable interface.

### 19. How do you manage Terraform remote state securely?

I store state in an encrypted S3 backend with versioning, restricted IAM access, audit logging, and locking appropriate to the Terraform and backend version in use. I separate state by environment and blast radius, avoid outputs that expose secrets, and back up or replicate state according to recovery requirements. Pipeline roles receive only the access needed for their specific state and resources.

### 20. What would you do if a Terraform state file became corrupted or unavailable?

I stop all applies, preserve the current state and logs, and determine whether the problem is access, locking, versioning, or actual corruption. I restore a known-good S3 object version when appropriate, compare it with the live infrastructure using refresh-only planning, and import or remove bindings carefully. I test the recovery in a controlled context before resuming production automation.

### 21. How do you detect and resolve infrastructure drift?

Scheduled `terraform plan` or `plan -refresh-only` runs reveal differences between state, configuration, and provider data. I investigate who or what made the change through CloudTrail and change records, then decide whether the approved result belongs in code or the resource should be returned to the declared configuration. I never apply blindly because some drift may represent an emergency change that first needs formal review.

### 22. How do you review a Terraform execution plan?

I examine every create, update, replacement, and destroy action, paying special attention to production data, IAM, network paths, and resources marked `ForceNew`. I confirm variable and provider inputs, dependencies, unknown values, policy results, change tickets, backup readiness, and rollback options. A saved plan should be applied by the same controlled pipeline after approval.

### 23. How do you import an existing AWS resource into Terraform?

I first write configuration that reflects the desired management boundary, then use an import block or `terraform import` to bind the real resource to its Terraform address. I run a plan, reconcile every unexpected difference, and avoid applying until the configuration accurately represents the resource. I also import dependencies or document resources intentionally left unmanaged.

### 24. How do you handle resource dependencies?

I prefer implicit dependencies created through references, such as passing a VPC ID from one resource or module to another. I use `depends_on` only when a real operational dependency exists but is not represented by data flow. Excessive explicit dependencies serialize execution and can hide poor module boundaries.

### 25. What is the difference between implicit and explicit dependencies?

An implicit dependency is inferred when one resource references an attribute of another. An explicit dependency is declared with `depends_on` when ordering is required without a direct value reference. Implicit dependencies are clearer because Terraform can understand the actual relationship.

### 26. How do you manage Terraform module versions?

I publish immutable versions using semantic versioning, maintain release notes and upgrade guidance, and pin production consumers to an approved version instead of a moving branch. Pipelines test module changes and downstream examples before release. Upgrades move through non-production environments with plan review before production promotion.

### 27. How do you promote Terraform changes from development to production?

The same reviewed module version and pipeline logic move through development, UAT, and production, while environment values and state remain separate. Each stage performs formatting, validation, linting, security scanning, policy checks, and plan review. Production requires protected branches, change approval, and a controlled apply using short-lived credentials.

### 28. How do you prevent accidental deletion of critical resources?

I combine protected branches and approvals with plan inspection, policy-as-code rules, narrowly scoped pipeline permissions, backups, and Terraform `prevent_destroy` where appropriate. Critical resources such as production databases also use AWS deletion protection or retention controls. I treat lifecycle rules as one layer, not a replacement for governance and recovery planning.

### 29. What happens when two engineers run Terraform against the same state?

Without locking, both runs can read the same starting state and attempt conflicting changes, which can create failures or inaccurate state. A supported remote-locking mechanism serializes writes so one operation proceeds and the other waits or fails safely. Teams should still use a single deployment pipeline and avoid local production applies.

### 30. How do you troubleshoot a partially failed Terraform deployment?

I do not immediately rerun or edit state. I review the error, plan, logs, state, and actual AWS resources to determine which actions completed and whether the failure is recoverable. After fixing the root cause, I generate a new plan; if resources exist outside state, I import them rather than creating duplicates.

### 31. Which Terraform validation and security tools have you used?

I use `terraform fmt`, `validate`, and `plan`, together with tools such as TFLint, Checkov, Trivy, and policy engines including OPA and Sentinel. I also use automated module tests, cost estimation where available, and credential or secret scanning. These checks run before an apply and block violations based on risk.

### 32. How have you integrated Terraform into CI/CD?

I have implemented PR-triggered validation and planning with GitHub Actions, Jenkins, Harness, Azure DevOps, and other pipeline tools. The workflow uses short-lived cloud credentials, publishes the plan for review, enforces policy and security gates, and requires approval before applying to protected environments. The pipeline records the code, plan, approver, and result for auditability.

### 33. How do Sentinel and OPA improve Terraform governance?

They evaluate infrastructure plans or configuration against machine-enforced policies before deployment. I use them to require encryption, approved regions and instance types, mandatory tags, restricted public exposure, and least-privilege patterns. This turns architectural standards into consistent automated controls rather than relying only on manual review.

### 34. What standards do you enforce during Terraform code review?

I review module purpose, naming, variables, outputs, secure defaults, provider constraints, dependency design, lifecycle behavior, state impact, and documentation. I check for hard-coded values, secrets, overly broad IAM, public exposure, unpinned sources, and unsafe replacement or deletion. I also require tests and a readable execution plan.

### 35. Have you built Terraform modules directly or mainly consumed existing modules?

I have directly designed and maintained reusable modules and golden templates for networking, compute, load balancing, databases, storage, IAM, KMS, monitoring, messaging, EKS, and FSx. I define their interfaces, defaults, outputs, examples, policy requirements, and versioning. I can also assess external modules, but I do not treat them as trusted without code, security, and lifecycle review.

[⬆ Back to top](#top)

---

## 3 Kubernetes and Amazon EKS

### 36. Describe your production experience managing EKS clusters.

At Citi and through consulting engagements, I managed EKS platforms supporting distributed batch, inference, and microservice workloads. My work included Terraform provisioning, upgrades, node scaling, Helm deployments, RBAC, namespace isolation, observability, incident response, and IAM integration. I focused on making the platform secure, repeatable, and operable by multiple teams.

### 37. Explain the Kubernetes control plane and worker-node architecture.

The control plane exposes the API server, stores desired state in etcd, schedules pods, and runs controllers that reconcile actual state. Worker nodes run kubelet, a container runtime, and networking components that host application pods. In EKS, AWS manages the control plane, while customers remain responsible for workload configuration, access, nodes or Fargate, networking, and operational controls.

### 38. How do you troubleshoot a pod in CrashLoopBackOff?

I use `kubectl describe pod`, current and previous container logs, events, exit codes, and the pod specification. I check command and arguments, configuration, secrets, probes, permissions, dependencies, and CPU or memory limits, including whether an OOM kill occurred. After fixing the cause, I validate readiness and watch the rollout rather than only confirming that the container started.

### 39. How do you troubleshoot a pod stuck in Pending?

I inspect scheduling events for insufficient CPU or memory, node selectors, affinity rules, taints and tolerations, topology constraints, quotas, PVC binding, and unavailable nodes. I compare pod requests with node-group capacity and autoscaler behavior. The fix may require capacity, corrected scheduling constraints, storage provisioning, or right-sized requests.

### 40. What would you check when a pod cannot connect to another service?

I validate the Service name and namespace, selectors, endpoints, ports, CoreDNS, network policies, security groups, route tables, and the destination's health. From a diagnostic pod, I test DNS and TCP or HTTP connectivity. I also check service mesh policies, TLS, and whether the application is listening on the expected interface and port.

### 41. How do readiness liveness and startup probes differ?

Readiness determines whether a pod should receive traffic. Liveness determines whether Kubernetes should restart a container that is unhealthy. A startup probe protects slow-starting applications from premature liveness failures; probe thresholds should reflect real application behavior and dependencies.

### 42. How do you manage Kubernetes deployments using Helm?

I package reusable Kubernetes resources into versioned charts, keep defaults safe, and place environment-specific values in controlled repositories or pipelines. I run linting, template rendering, schema validation, security checks, and diff review before upgrade. Releases use atomic or rollback-aware deployment settings, and secrets are referenced from an approved secret-management solution.

### 43. How do Helm values templates releases and rollbacks work?

Templates contain Kubernetes manifests with parameters, while values supply defaults and environment overrides. An install or upgrade creates a versioned release whose history Helm tracks in the cluster. A rollback redeploys an earlier release revision, but database or external-service changes may require a separate recovery plan.

### 44. How do you troubleshoot a failed Helm deployment?

I inspect `helm status`, release history, rendered templates, Kubernetes events, pod logs, hooks, admission-policy failures, RBAC, and immutable-field errors. I determine whether Helm timed out while resources later became healthy or whether the release is genuinely broken. I then correct the chart or dependency and use rollback or a controlled upgrade.

### 45. How do you perform an EKS upgrade with minimal disruption?

I review version compatibility and deprecated APIs, upgrade add-ons and tooling, test in non-production, and confirm PodDisruptionBudgets and workload redundancy. I upgrade the control plane, then roll managed node groups or Karpenter nodes gradually while monitoring application and cluster SLIs. I keep rollback or mitigation options for workloads, even though the control-plane version itself is not simply downgraded.

### 46. How do you configure autoscaling in EKS?

I set realistic pod requests and limits, use HPA for replica scaling, and use Cluster Autoscaler or Karpenter for compute capacity. Scaling metrics should represent demand, and stabilization windows protect against rapid oscillation. I test scale-out speed, disruption behavior, quotas, and scale-in safety under realistic load.

### 47. Compare HPA Cluster Autoscaler and Karpenter.

HPA changes the number of pod replicas based on workload metrics. Cluster Autoscaler changes the size of predefined node groups when pods are unschedulable or nodes are underused. Karpenter provisions nodes directly from workload requirements, allowing faster and more flexible instance selection.

### 48. How do you integrate AWS IAM with Kubernetes service accounts?

I use IRSA or the supported EKS workload-identity mechanism to map a Kubernetes service account to a narrowly scoped IAM role. The trust relationship is restricted to the correct cluster identity provider, namespace, and service account. This avoids storing AWS keys and prevents applications from inheriting broad node-role permissions.

### 49. Explain the difference between AWS IAM and Kubernetes RBAC.

AWS IAM controls access to AWS APIs and is also used to authenticate principals to EKS. Kubernetes RBAC controls what an authenticated subject can do with Kubernetes API resources. A user may be allowed to connect to the cluster through AWS identity but still require the appropriate Kubernetes role binding.

### 50. How do you secure a multi-tenant EKS cluster?

I use separate namespaces, least-privilege RBAC, dedicated service accounts and IAM roles, network policies, quotas, limit ranges, admission policies, and controlled pod-security settings. Sensitive or high-risk workloads may use dedicated node pools, taints, or separate clusters. Centralized logging, audit visibility, image controls, and secrets management provide additional isolation and evidence.

### 51. How do Services Ingress and AWS load balancers work together?

A Kubernetes Service provides stable access to a set of pods selected by labels. An Ingress defines HTTP or HTTPS routing rules, and an ingress controller translates those rules into actual data-plane configuration. On EKS, the AWS Load Balancer Controller can provision ALBs or NLB-related resources and register targets for the services.

### 52. How do you troubleshoot DNS resolution inside EKS?

I test the full and short service names from a diagnostic pod, inspect `/etc/resolv.conf`, CoreDNS pods, logs, configuration, and service endpoints. I check network policies, node connectivity, upstream VPC DNS settings, and CoreDNS capacity or throttling. I also distinguish DNS failure from a reachable name whose application port is failing.

### 53. How do you collect and centralize Kubernetes logs?

I write application output to standard output and error, deploy a node-level collector such as Fluent Bit, enrich records with cluster and workload metadata, and route them to CloudWatch or OpenSearch. I define retention, encryption, access control, parsing, and correlation identifiers. Metrics and traces are linked to the same service and deployment context.

### 54. What are Kubernetes network policies?

Network policies declare allowed pod ingress and egress traffic based on namespaces, pod labels, and IP blocks. They require a network implementation that enforces them. I normally start from a tested default-deny posture and explicitly allow DNS, observability, required services, and approved external destinations.

### 55. How do you manage Kubernetes secrets securely?

I avoid committing secret values to Git or placing them in ordinary Helm values. I store them in AWS Secrets Manager or another approved vault and expose them through a controlled operator or CSI driver, with KMS encryption, IAM-based access, audit logging, and rotation. Kubernetes etcd encryption and RBAC remain important because mounted values eventually reach the workload.

### 56. How would you recover from a failed Kubernetes deployment?

I stop further promotion, assess customer impact, and inspect rollout status, events, logs, probes, and dependency changes. If the previous version is safe, I roll back the Deployment or Helm release while monitoring service health. I then correct the failure, add a test or guardrail that would have detected it, and redeploy through the normal pipeline.

### 57. Describe your experience deploying distributed applications.

I have deployed containerized microservices, batch-processing, inference, and platform workloads on EKS, ECS, and Kubernetes. I handled image delivery, Helm or manifests, service discovery, ingress, IAM and RBAC, autoscaling, observability, and CI/CD promotion. I also supported the production issues that emerge across application, cluster, network, and cloud-service boundaries.

[⬆ Back to top](#top)

---

## 4 CI CD and GitOps

### 58. Describe a production CI CD pipeline you implemented from start to finish.

I built pipelines that begin with a pull request and run formatting, tests, security scans, Terraform validation, policy checks, and a reviewed execution plan. After approval, the pipeline uses short-lived AWS credentials to deploy infrastructure, build and scan container images, promote immutable artifacts, and deploy through Helm or GitOps. Post-deployment health checks and monitoring determine success or trigger rollback, while approvals and results remain auditable.

### 59. How do you integrate Terraform validation planning approval and deployment into a pipeline?

The pull-request stage runs `fmt`, `validate`, linting, security and policy checks, then creates a plan using the target environment's state. Reviewers inspect the plan, and the protected deployment stage applies a saved or freshly verified plan after approval. Production credentials are short-lived, environment-scoped, and unavailable to untrusted branches.

### 60. What security gates should be included in a cloud infrastructure pipeline?

I include code review, secret scanning, dependency and license checks, IaC misconfiguration scanning, policy-as-code, container vulnerability scanning, image signing or provenance checks, and least-privilege authorization. High-risk findings block deployment; documented exceptions need an owner and expiration. Production also requires approval, change traceability, health validation, and rollback readiness.

### 61. How do you prevent unreviewed changes from reaching production?

I use protected branches, required reviewers, status checks, environment approvals, restricted deployment roles, and policy enforcement. Engineers cannot apply production Terraform locally or bypass the GitOps controller with broad standing access. Emergency access is time-bound, audited, and followed by reconciliation into code.

### 62. How do you securely authenticate a CI CD pipeline to AWS?

I configure OIDC federation between the CI/CD platform and AWS so the job assumes an IAM role and receives short-lived credentials. The role trust policy restricts repository, branch, workflow, environment, and audience claims as appropriate. The permissions policy then grants only the AWS actions required by that pipeline stage.

### 63. Why is OIDC preferred over long-lived AWS access keys?

OIDC eliminates stored static AWS keys and issues temporary credentials only when an authorized job runs. Claims in the signed token allow AWS to restrict which repository, branch, or environment may assume the role. This reduces credential leakage, rotation burden, and the impact window if a token is exposed.

### 64. How do you troubleshoot an invalid role ARN or OIDC trust-policy failure?

I first verify the account ID, role name, partition, and exact ARN used by the job. I then compare the token issuer, audience, subject and other claims with the IAM provider and role trust-policy conditions, and review CloudTrail or pipeline errors for the failing assumption. Finally, I confirm the workflow has permission to request an identity token and that the assumed role has the required deployment permissions.

### 65. Describe your experience with GitHub Actions Jenkins GitLab CI or Harness.

I have built and maintained infrastructure and application pipelines using GitHub Actions, Jenkins, Harness, Azure DevOps, GitLab CI, Bitbucket, and AWS-native services. At Citi, I helped migrate legacy Jenkins workloads toward GitHub Actions and Harness to reduce maintenance and improve consistency. I focus on reusable templates, short-lived credentials, policy gates, artifact promotion, approvals, and observable deployments.

### 66. How have you used Argo CD or another GitOps platform?

I use Git as the approved source of Kubernetes desired state and Argo CD to detect and reconcile drift. Application definitions, Helm chart versions, environment values, sync policies, health checks, and access controls are versioned and reviewed. Promotion occurs through pull requests, while rollback normally reverts the Git commit or selects a previously approved version.

### 67. How do you promote Kubernetes changes across development UAT and production?

I build an immutable image once, identify it by digest or version, and promote that same artifact through environments. Environment repositories or overlays contain approved configuration differences, and pull requests trigger validation, policy checks, deployment, and health verification. Production promotion requires approval and has a tested rollback path.

### 68. How do you design a safe rollback strategy?

I separate application, infrastructure, and data changes because each has different rollback constraints. Deployments use immutable artifacts, backward-compatible interfaces, progressive release methods, and automated health gates; infrastructure changes require reviewed reverse plans or restoration procedures. Database migrations use expand-and-contract patterns so the previous application version can operate safely.

### 69. How do you manage configuration differences between environments?

I keep shared logic in reusable modules or base manifests and isolate legitimate differences in typed variables, values files, or overlays. Secrets come from a secret manager rather than configuration repositories. I minimize divergence so non-production testing remains representative, and I validate every environment through the same pipeline controls.

### 70. What is your approach to artifact and container-image versioning?

I produce immutable artifacts once and assign a unique semantic version, commit SHA, or digest. Registries prevent tag mutation for release artifacts, and deployment records identify the exact digest, source commit, scan results, and approvals. Promotion reuses the same artifact instead of rebuilding it for each environment.

[⬆ Back to top](#top)

---

## 5 Observability and Incident Response

### 71. What does production readiness mean to you?

Production readiness means the service has clear ownership, tested scaling and failure behavior, actionable telemetry, defined SLOs, security controls, backups, recovery procedures, capacity expectations, and safe deployment and rollback mechanisms. It must also have runbooks, support rotation readiness, dependency mapping, and known operational limits. Passing functional tests alone is not enough.

### 72. What metrics would you monitor for ECS EKS Lambda DynamoDB and DocumentDB?

For ECS and EKS, I monitor availability, replica or task health, CPU, memory, restart rate, scheduling, latency, traffic, and error rate. For Lambda, I monitor invocations, errors, duration, throttles, concurrency, iterator age, and dead-letter outcomes; for DynamoDB, latency, throttles, consumed capacity, errors, and replication; for DocumentDB, connections, CPU, memory, storage, replica lag, latency, and slow-query indicators. Business SLIs remain the primary customer-impact view.

### 73. How do you design useful alerts without creating alert fatigue?

I alert on customer symptoms, SLO burn, and conditions that require a timely human action. Alerts include severity, impact, supporting signals, owner, and a linked runbook, while dashboards carry informational data that does not need paging. I regularly review noisy, duplicate, and non-actionable alerts and tune or remove them.

### 74. Explain the difference between logs metrics and traces.

Metrics are aggregated numeric measurements that efficiently show trends and trigger alerts. Logs record discrete events with detailed context, while distributed traces follow an individual request across service boundaries. Together they help answer whether a problem exists, where it occurred, and why.

### 75. How have you used CloudWatch Prometheus Grafana or OpenSearch?

I have used CloudWatch for AWS metrics, logs, alarms, dashboards, and event-driven operations; Prometheus for Kubernetes and application metrics; Grafana for correlated operational views; and OpenSearch or ELK for centralized log search. I integrated Fluentd or Fluent Bit for forwarding and ServiceNow for incident workflows. These improvements helped reduce detection and recovery time by 35 percent.

### 76. How do you establish SLIs and SLOs?

I begin with the user journey and select measurable indicators such as successful request rate, latency, data freshness, or job completion. I define the measurement window, exclusions, target, and error budget with product and engineering stakeholders. Alerts then use error-budget burn rates so teams respond before the SLO is exhausted.

### 77. What is your role during a severity-one incident?

I establish clear incident command, confirm customer and business impact, assign technical investigation and communication roles, and keep the team focused on restoration before deep root-cause work. I make or recommend mitigation decisions based on evidence and risk, maintain a timeline, and provide regular stakeholder updates. After recovery, I lead or contribute to the post-incident review and corrective actions.

### 78. How do you communicate technical status during an active incident?

I use a consistent structure: impact, scope, current service state, actions completed, actions in progress, risks, owner, and next update time. I separate confirmed facts from hypotheses and translate technical findings into customer and operational consequences. Updates remain brief so responders can focus while leadership receives reliable information.

### 79. What should be included in a post-incident report?

It should include an executive summary, impact and duration, detection method, detailed timeline, technical root cause, contributing factors, mitigation, recovery, and what went well or poorly. Corrective actions need owners, priorities, due dates, and verification criteria. The report should be blameless and useful for preventing similar failures across other systems.

### 80. Describe a time observability identified a problem before a major outage.

At Citi, I built CloudWatch, Prometheus, Grafana, and centralized-log dashboards with threshold and trend-based alerts for distributed workloads. Those signals exposed degrading capacity or dependency behavior early enough for the team to investigate and stabilize services before the impact expanded. The broader observability program reduced detection and recovery time by about 35 percent.

### 81. How do you improve MTTD and MTTR?

I improve MTTD through user-centered SLIs, better instrumentation, SLO-based alerts, synthetic checks, and clear service ownership. I improve MTTR through dependency maps, searchable logs and traces, tested runbooks, automated diagnostics, safe rollback, and regular incident exercises. Post-incident actions then remove recurring causes and shorten future decisions.

[⬆ Back to top](#top)

---

## 6 Security and Operational Readiness

### 82. How do you apply least privilege across AWS and EKS?

In AWS, I prefer assumed roles and temporary credentials, restrict actions and resources, use conditions, and assess policies with IAM Access Analyzer and CloudTrail evidence. In EKS, I use scoped RBAC, dedicated service accounts, workload IAM roles, namespace boundaries, and controlled administrative access. I review access periodically and remove unused privileges.

### 83. How do you protect sensitive values used by Terraform and Kubernetes?

I keep secrets in AWS Secrets Manager or another approved vault, restrict access with IAM and KMS, rotate them, and prevent them from entering source control or ordinary logs. Pipelines retrieve values only at runtime through short-lived identities. Because Terraform state may contain sensitive values, I encrypt, version, isolate, and tightly control the state backend.

### 84. How do you secure S3 buckets?

I enable block public access, use least-privilege IAM and bucket policies, enforce TLS, encrypt objects with an appropriate KMS key, and apply ownership and access-point patterns where needed. I enable CloudTrail data events or relevant access logging for sensitive buckets, along with versioning, retention, lifecycle, and replication controls based on business requirements. AWS Config and Security Hub help detect drift.

### 85. How do you implement encryption at rest and in transit?

At rest, I use AWS-managed or customer-managed KMS keys based on control requirements and configure services such as S3, EBS, RDS, and logs to encrypt by default. In transit, I require modern TLS, validated certificates, secure load-balancer policies, and private endpoints where appropriate. I also design key policies, rotation, separation of duties, and recovery so encryption does not create an availability risk.

### 86. How do GuardDuty Security Hub Inspector Config and CloudTrail work together?

CloudTrail records API activity, while Config records resource configuration and evaluates compliance. GuardDuty analyzes activity and telemetry for threats; Inspector scans supported workloads and images for vulnerabilities or exposure; Security Hub aggregates and normalizes findings and control status. I centralize these services, route high-severity findings to response workflows, and automate safe remediation where possible.

### 87. How do you scan Terraform code and container images?

Pull requests run Terraform formatting, validation, linting, Checkov or Trivy configuration scans, policy-as-code, and secret scanning. Container builds use minimal trusted bases, dependency checks, vulnerability scans, software bill-of-materials generation, and image signing or provenance controls where supported. Critical findings block release unless a formally approved, time-limited exception exists.

### 88. How do you handle patching and vulnerability remediation in production?

I inventory and prioritize findings by exploitability, exposure, business impact, and severity, then test fixes in lower environments. For hosts, I use hardened golden images and controlled replacement or patch windows; at Citi I integrated EC2 Image Builder with CrowdStrike, Qualys, Tanium, and SSM. I verify remediation after deployment and track exceptions to expiration.

### 89. How do you balance security requirements with deployment speed?

I make the secure path the easiest path through approved Terraform modules, golden images, reusable pipelines, automated policies, and self-service patterns. High-confidence controls run automatically and provide specific remediation guidance. Risk-based exceptions remain possible, but they require ownership, evidence, compensating controls, and an expiration date.

### 90. What security controls should be validated before production release?

I validate identity and least privilege, network exposure, encryption, secrets handling, image and dependency findings, logging and audit coverage, backup and recovery, data classification, and policy compliance. I also confirm that monitoring, incident ownership, rollback, and emergency-access procedures work. The exact gate depth is proportional to the workload's risk and criticality.

[⬆ Back to top](#top)

---

## 7 Reliability Disaster Recovery Performance and Cost

### 91. How do you design AWS workloads for high availability?

I deploy stateless capacity across multiple Availability Zones behind health-aware load balancing and use Auto Scaling or Kubernetes scheduling for replacement. Data services use Multi-AZ or replicated designs appropriate to their consistency and recovery needs. I remove hidden single points of failure in NAT, DNS, secrets, queues, deployment systems, and operational access, then test failure behavior.

### 92. How do you determine RTO and RPO requirements?

I work with business, product, security, and data owners to quantify outage impact, transaction criticality, regulatory needs, and the cost of recovery options. RTO determines how quickly the service must return, while RPO determines the maximum acceptable data-loss window. Those targets drive backup frequency, replication, architecture, staffing, runbooks, and testing.

### 93. Describe a backup disaster-recovery or failover test you performed.

I have designed AWS and Azure recovery strategies with cross-region replication, backup policies, tiered RTO and RPO targets, and documented failover and failback procedures. I validate them through recovery drills that restore data and exercise application dependencies, not just confirm that backup jobs completed. Results become evidence for gaps, timing, and updated runbooks.

### 94. How do you identify and remove single points of failure?

I map every request and operational dependency, including identity, DNS, network egress, load balancing, compute, state, secrets, observability, CI/CD, and support access. I compare the design with actual failure domains and test component or Availability Zone loss. The remedy may be redundancy, decoupling, queueing, replicated state, alternate access, or a documented recovery procedure.

### 95. How would you troubleshoot intermittent performance problems?

I correlate latency percentiles, traffic, errors, saturation, deployments, dependency timing, and infrastructure events instead of relying on averages. Traces identify the slow hop, logs explain request context, and metrics show resource or queue pressure. I reproduce safely, compare healthy and unhealthy periods, and change one variable at a time while protecting production.

### 96. How do you perform capacity planning for Kubernetes workloads?

I use historical and forecast demand, pod resource utilization, requests and limits, node efficiency, startup time, scaling latency, disruption requirements, and service quotas. I model normal, peak, and failure scenarios, including the loss of an Availability Zone. Load tests verify that HPA and node provisioning scale early enough and that budgets cover surge capacity.

### 97. How do you improve AWS cost efficiency without compromising reliability?

I begin with allocation and utilization data, then rightsize compute and storage, schedule non-production resources, apply lifecycle policies, remove waste, and match pricing models to stable or interruptible demand. I protect availability targets and load-test changes before reducing headroom. At Citi, these practices delivered sustained 20 to 25 percent savings while maintaining resilience.

### 98. Describe your experience with rightsizing Savings Plans Spot and lifecycle policies.

I use utilization and performance data to rightsize services rather than cutting capacity blindly. Savings Plans cover predictable compute, while Spot is appropriate for fault-tolerant workloads with diversified capacity and interruption handling. I have also automated storage and FSx lifecycle controls, contributing to 20 to 25 percent infrastructure savings.

### 99. How do you validate that a disaster-recovery plan will work?

I run scheduled exercises that restore backups, fail traffic or workloads to the recovery environment, validate data integrity and dependencies, measure actual RTO and RPO, and test stakeholder communication. I include failback because recovery is incomplete if the organization cannot return safely. Gaps receive owners and are retested.

### 100. What operational checks should be completed before a major production release?

I confirm approvals, tested artifacts, dependency readiness, capacity, backups, observability, runbooks, support coverage, rollback criteria, and stakeholder communication. I review change collisions, freeze periods, feature flags, database compatibility, and error-budget status. The release proceeds only when success and abort conditions are understood.

[⬆ Back to top](#top)

---

## 8 Leadership and Behavioral Questions

### 101. Tell me about yourself and how your experience aligns with this position.

I am a senior Cloud, DevOps, and Platform Engineer with more than 10 years of infrastructure experience and over seven years working with AWS. At Citi and in consulting roles, I built reusable Terraform modules, supported production AWS and EKS platforms, automated delivery with GitHub Actions, Jenkins, and Harness, and implemented observability that reduced incident detection and recovery time by 35 percent. My AWS Solutions Architect Professional, AWS Security Specialty, Terraform, and CKA certifications reinforce the hands-on experience this role requires.

### 102. Why are you interested in working for United Airlines?

I am interested in United because airline technology requires the production reliability, rapid incident response, security, and scalability that have shaped my career. I want to apply my AWS, Terraform, EKS, and observability experience to platforms where availability directly affects employees, operations, and customers. The role also fits my preference for senior hands-on ownership while mentoring engineers and improving platform standards.

### 103. Describe a time you took ownership of an ambiguous production issue.

At Citi, distributed workload issues often crossed EKS, AWS services, networking, and application dependencies, so the first alert did not identify one owner. I established the impact and timeline, correlated CloudWatch, Prometheus, Grafana, and centralized logs, and coordinated the right teams while driving mitigation. I then converted the findings into better dashboards, alerts, and runbooks, contributing to a 35 percent improvement in detection and recovery time.

### 104. Tell me about a major incident you led from detection through resolution.

During a production degradation, I began by validating customer impact and recent changes, then organized investigation across application, infrastructure, and dependency signals. I used dashboards and logs to isolate the failing layer, implemented the safest mitigation, communicated status at defined intervals, and monitored recovery. Afterward, I documented the timeline and assigned automation, alerting, and runbook improvements to prevent recurrence.

### 105. Describe a technical decision where you explained risks and tradeoffs to leadership.

When evaluating platform changes, I present the decision in terms of reliability, security, delivery time, operational effort, and cost. For example, I have recommended reusable Terraform and policy-enforced pipelines over manual provisioning because the initial engineering investment reduces drift, audit risk, and recovery time across many teams. I explain alternatives and residual risks, then provide a phased implementation and measurable success criteria.

### 106. Tell me about a disagreement during a code or architecture review.

I focus the discussion on requirements and evidence rather than personal preference. In an infrastructure review, I would compare the options against blast radius, security controls, operational complexity, cost, and recovery, and use a plan or small test to resolve uncertain assumptions. Once the team decides, I document the rationale and fully support the agreed approach.

### 107. Describe a time you improved an operational process or engineering standard.

At Citi, I helped standardize AWS delivery through reusable Terraform modules, golden templates, automated policy gates, and CI/CD promotion. This reduced manual provisioning, increased deployment consistency, and made security and observability part of the default platform pattern. I also improved dashboards and ServiceNow-integrated alerts so responders received clearer, more actionable information.

### 108. How do you mentor junior and mid-level engineers?

I use design reviews, pairing, incident debriefs, and code-review comments that explain why a change matters, not only what to modify. I give engineers bounded ownership, point them to repeatable troubleshooting methods, and gradually expand scope as they demonstrate judgment. I also create examples, runbooks, and modules so knowledge becomes part of the platform rather than remaining with one person.

### 109. How do you balance project delivery with production support?

Production stability receives immediate priority based on severity and customer impact, but I protect planned work through clear on-call ownership, escalation paths, and capacity planning. I track recurring operational demand and invest in automation, monitoring, and problem elimination so support work does not permanently consume delivery capacity. Risks and tradeoffs are communicated early to stakeholders.

### 110. Describe a time you made a mistake in production.

When I make or contribute to a mistake, I first protect the service by stopping the change, rolling back, or isolating the impact. I communicate the facts promptly, preserve evidence, and participate openly in the review without minimizing my role. The important outcome is a durable control—such as a test, approval, policy, or safer deployment pattern—that prevents the same class of error.

### 111. How do you prioritize multiple critical incidents or requests?

I rank them by safety, customer and operational impact, scope, data risk, time sensitivity, and availability of workarounds. I establish incident ownership so parallel teams can respond without competing changes, and I escalate resource conflicts quickly. Stakeholders receive clear priorities and expected update times instead of silent queueing.

### 112. What information do you include in runbooks?

A runbook includes purpose, scope, ownership, prerequisites, access requirements, dashboards, alert meaning, diagnostic commands, decision points, mitigation and rollback steps, validation, escalation contacts, and evidence to capture. Commands are safe, specific, and tested. I review runbooks after incidents, platform changes, and exercises.

### 113. Describe a time automation improved reliability or reduced manual effort.

At Citi, I used Terraform, Ansible, Jenkins, and other CI/CD tools to automate infrastructure and platform deployment. The work reduced manual provisioning by about 45 percent and improved deployment speed by up to 65 percent while adding consistent reviews and security gates. Automation also made recovery more repeatable because environments could be recreated from controlled code.

### 114. How do you work with application networking security and product teams?

I begin with the shared business outcome and make interfaces, ownership, dependencies, and decision deadlines explicit. I translate infrastructure risks into application and customer impact while listening to domain-specific constraints from each team. During incidents, I maintain one timeline and clear workstreams; during delivery, I use design records, pull requests, and acceptance criteria to keep decisions visible.

### 115. What would you focus on during your first 90 days?

In the first 30 days, I would learn the platform architecture, critical services, team responsibilities, incident history, deployment process, and reliability objectives. By 60 days, I would take ownership of production support areas, identify high-value risks, and deliver a small operational improvement. By 90 days, I would propose a prioritized roadmap for Terraform standards, EKS reliability, observability, security, and recurring-incident reduction based on measured evidence.

[⬆ Back to top](#top)

---

## 9 Scenario Based Questions

### 116. A production EKS application is unavailable immediately after deployment. Walk through your response.

I declare and scope the incident, pause further promotion, and compare the deployment time with the service failure. I check rollout status, pods, events, logs, probes, Services, endpoints, Ingress, load-balancer targets, configuration, secrets, and policy changes. If the previous release is known good, I roll back quickly, validate customer recovery, preserve evidence, and then fix the deployment and missing guardrail.

### 117. Terraform proposes replacing a production resource. What do you do?

I do not approve until I know which attribute forces replacement and what data, traffic, identity, or dependency impact it creates. I compare configuration, state, provider changes, and drift, then evaluate alternatives such as an in-place AWS change, state correction, `moved` block, staged migration, or blue-green replacement. Backups, rollback, maintenance timing, and explicit approval are required before proceeding.

### 118. An application works in development but fails in production with AccessDenied. How do you investigate?

I compare the runtime identity and exact request in both environments, then use CloudTrail to capture the denied action, resource, and context. I review IAM and resource policies, permissions boundaries, SCPs, KMS policies, endpoint policies, tags, and condition keys for environment-specific differences. I correct the narrow policy or configuration difference and test through the production identity path.

### 119. DynamoDB requests are throttled during peak customer activity. How do you stabilize the service?

I confirm the affected table or index and determine whether the pressure is broad or caused by a hot partition. Immediate actions may include enabling or increasing capacity, reducing nonessential traffic, using caching or queues, and verifying exponential backoff with jitter. The long-term solution may require a better partition key, write sharding, revised indexes, auto scaling, or on-demand mode.

### 120. A Terraform pipeline completed but the expected AWS resource is missing. How do you troubleshoot?

I verify the target account, region, workspace, variables, conditional expressions, module version, and actual applied plan. I inspect pipeline logs, state with `terraform state list` or `show`, CloudTrail, and whether a later stage destroyed or replaced the resource. I then correct the configuration or pipeline targeting and reconcile state carefully rather than creating an unmanaged duplicate.

### 121. An EKS pod is healthy but customers cannot access it through the load balancer. What do you check?

Pod health alone does not validate the complete request path. I check DNS, certificate and listener rules, load-balancer security groups, target-group health, Ingress, Service type and ports, selectors, endpoints, readiness gates, controller logs, subnets, routes, and network policies. I test each hop from outside and inside the cluster to identify where connectivity stops.

### 122. A Helm upgrade failed halfway through production. How do you recover?

I pause changes and inspect the release status, history, hooks, events, rendered manifests, and resource health. If the previous revision remains compatible, I use a Helm rollback and validate the service; otherwise I restore individual components according to the runbook. I then address chart defects, immutable fields, timeouts, or dependency changes and improve predeployment validation.

### 123. CloudWatch shows increasing latency but CPU and memory are normal. What else do you investigate?

I inspect dependency latency, database connections and locks, storage and network performance, DNS, thread or connection pools, queue depth, throttling, garbage collection, external APIs, and error or retry rates. Traces and latency percentiles help isolate the slow hop, while logs reveal request-specific behavior. Normal CPU and memory do not exclude saturation in another constrained resource.

### 124. An engineer manually changed a production AWS resource and created Terraform drift. What do you do?

I first determine why the change was made and whether reverting it would harm the service. If the change is approved and should remain, I update code and review the plan; otherwise I use Terraform to restore the declared state safely. I then reduce recurrence through permissions, emergency-change procedures, drift detection, and a faster approved delivery path.

### 125. A major AWS regional disruption affects a critical airline application. How do you coordinate recovery and communication?

I activate the disaster-recovery plan, establish incident command, verify the scope and integrity of data, and choose failover actions according to the service's RTO and RPO. Teams execute application, data, network, identity, and validation workstreams while communications provide impact, actions, risks, and next update times. After service restoration, I monitor stability, plan controlled failback, and document any gaps between tested and actual recovery behavior.

[⬆ Back to top](#top)

---

## Questions to Ask the Interviewer

1. Which AWS and EKS platforms are most critical to United's daily operations, and what are their current SLOs?
2. What percentage of this role is planned engineering versus production support and incident response?
3. How are Terraform modules owned, versioned, tested, and promoted across environments?
4. What are the most common production incidents the team wants this person to help eliminate?
5. How mature are the team's GitOps, observability, and automated rollback practices?
6. How are architectural decisions and operational risks communicated across engineering, product, and leadership?
7. What would successful performance look like during the first 90 days?
8. Which platform modernization initiatives are the highest priorities during the next year?

[⬆ Back to top](#top)

---

## Final Interview Reminder

Use a clear structure for experience-based answers: situation, responsibility, action, measurable result, and lesson. Lead with the outcome, explain your personal contribution, and connect the result to United's need for secure, reliable, production-ready airline technology.

[⬆ Back to top](#top)
