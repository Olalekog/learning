# Senior Consultant Interview Preparation

**Container Platform | Kubernetes | DevSecOps | Site Reliability Engineering**

**Candidate:** Olalekan Gabriel Ogundare  
**Interview context:** Pantha Kundu  
**Role location:** Charlotte, NC — 100% onsite, six-month contract  
**Relocation:** Open to Charlotte, North Carolina, or Detroit, Michigan.

These 45 questions are grouped by focus area. The Claude troubleshooting example uses the details you confirmed. Other scenario answers describe approaches you can explain without claiming unverified experience. Adjust experience statements to match your work.

## Index

| Focus Area | Topic | Questions |
|---|---|---|
| 1 | [Claude AI for CI/CD Troubleshooting](#focus-area-1-claude-ai-for-cicd-troubleshooting) | 1–6 |
| 2 | [GitHub Actions, Jenkins, and AWS Identity](#focus-area-2-github-actions-jenkins-and-aws-identity) | 7–14 |
| 3 | [Kubernetes, EKS, and Docker](#focus-area-3-kubernetes-eks-and-docker) | 15–23 |
| 4 | [AWS Platform Troubleshooting](#focus-area-4-aws-platform-troubleshooting) | 24–28 |
| 5 | [Terraform and DevSecOps](#focus-area-5-terraform-and-devsecops) | 29–33 |
| 6 | [Observability and Performance](#focus-area-6-observability-and-performance) | 34–37 |
| 7 | [SLOs, Incident Management, and Reliability](#focus-area-7-slos-incident-management-and-reliability) | 38–43 |
| 8 | [Automation and Role Alignment](#focus-area-8-automation-and-role-alignment) | 44–45 |

## Focus Area 1: Claude AI for CI/CD Troubleshooting

### 1. How have you used Claude AI to troubleshoot pipelines?

I used Claude AI to investigate AWS authentication and authorization failures in GitHub Actions and Jenkins. The problems involved an incorrect role ARN, an OIDC trust policy mismatch, and missing IAM permissions. Claude helped interpret the errors and identify configuration to review. I validated the recommendations against the environment and tested the corrections through pipeline reruns.

### 2. What was different between the GitHub Actions and Jenkins failures?

GitHub Actions used OIDC to assume an AWS role, so the investigation involved the role ARN and federation trust conditions. Jenkins used an IAM role attached to its agent, so the investigation focused on the identity the job was actually using and its permissions. Separating those authentication methods helped avoid applying the wrong fix.

### 3. What information would you provide to Claude?

I would provide the failing stage, sanitized error output, relevant workflow or Jenkinsfile sections, and recent changes. For IAM issues, I would include sanitized policy excerpts. I would explain the expected behavior and ask Claude to rank possible causes with verification steps. I would exclude credentials, tokens, and confidential data.

### 4. Give an example of a prompt you would use.

“GitHub Actions fails while assuming an AWS role through OIDC. Here are the sanitized error, workflow permissions, role ARN, and trust policy. Identify likely mismatches and suggest checks to distinguish them. Propose the smallest correction, explain why it works, and avoid broadening access beyond the intended repository and deployment context.”

### 5. How do you validate an AI-generated recommendation?

I treat it as a hypothesis. I compare it with the actual configuration and official documentation, inspect the proposed change, and test it in a controlled scope. I verify the resulting AWS identity and the operation that previously failed. Successful authentication alone does not prove the deployment has all the required permissions.

### 6. What would you do if Claude suggested administrator permissions?

I would identify the exact denied action and resource instead of applying broad permissions. I would check whether the failure came from an identity policy, resource policy, permissions boundary, or organizational restriction. Then I would propose a narrowly scoped correction and test it. The objective is to resolve the failure while preserving least privilege.

## Focus Area 2: GitHub Actions, Jenkins, and AWS Identity

### 7. How do you troubleshoot GitHub Actions OIDC failures?

I separate token generation, role assumption, and service authorization. I check `id-token: write`, the role ARN, the configured identity provider, and the trust policy’s audience and subject conditions. I compare those conditions with the workflow’s branch or environment context. After assumption succeeds, I confirm the identity before investigating service permissions.

### 8. What is the difference between authentication and authorization?

Authentication establishes which identity is making the request. Authorization determines whether that identity can perform the requested operation. A pipeline can successfully assume an AWS role and still receive AccessDenied when pushing an image or deploying infrastructure. That distinction tells me whether to investigate credentials and trust or the permissions governing the operation.

### 9. What is the difference between a trust policy and a permissions policy?

A trust policy controls who can assume a role. A permissions policy controls what the assumed role can do. For GitHub Actions, trust conditions can restrict access to a particular repository and deployment context. The role’s permissions then determine which AWS resources the workflow can access.

### 10. Why can OIDC work on one branch but fail on another?

The role’s trust policy may only allow a specific subject claim. A branch workflow and a workflow using a GitHub environment can have different subject formats. I would compare the failing run’s context with the configured trust conditions and authorize only the intended deployment context, rather than adding an unrestricted wildcard.

### 11. How would you troubleshoot Jenkins using the wrong AWS identity?

I would run `aws sts get-caller-identity` inside the failing job. Then I would inspect credential sources such as environment variables, configured profiles, and Jenkins credential bindings that might override the agent’s role. I would also confirm that the job’s execution environment can obtain the intended role credentials.

### 12. The role has an Allow policy, but access is still denied. Why?

An Allow in one policy is not always sufficient. An explicit Deny, permissions boundary, session policy, organizational policy, or resource policy can restrict access. Some operations also require related permissions, such as access to an encryption key. I would examine the exact action, resource, identity, and applicable policy layers.

### 13. How would you design a reliable CI/CD pipeline?

I would separate validation, testing, security checks, artifact creation, and deployment. I would build an identifiable artifact once and promote it through environments. Production deployment would include appropriate approvals, health checks, and a recovery path. Clear stage boundaries and useful logs make failures easier to diagnose and prevent unsafe partial releases.

### 14. A pipeline succeeds, but the application is unavailable. What do you do?

I would check what the pipeline actually validated. A successful deployment command may only mean the platform accepted the request. I would inspect rollout status, readiness, routing, and dependencies, then run a user-facing health check. I would strengthen the pipeline so it verifies application availability before reporting deployment success.

## Focus Area 3: Kubernetes, EKS, and Docker

### 15. How do you troubleshoot a failed Kubernetes deployment?

I start with deployment status, pod state, and events to classify the failure. Then I investigate scheduling, image access, startup, readiness, or networking as appropriate. I compare the new deployment with the previous version. If users are affected, I consider a safe rollback while continuing the investigation.

### 16. How do you troubleshoot CrashLoopBackOff?

CrashLoopBackOff indicates repeated container failures with increasing restart delays. I inspect current and previous container logs, termination reasons, exit codes, and events. Common areas to investigate include application configuration, startup commands, missing secrets, memory limits, and probes. I correct the underlying failure rather than repeatedly deleting the pod.

### 17. Why would a pod remain Pending?

I would inspect scheduling events first. Possible causes include insufficient resources, incompatible node selectors or affinity, untolerated taints, or unresolved storage requirements. I would compare the pod’s requests and constraints with available nodes. The fix depends on the evidence: adding capacity will not resolve an incompatible scheduling rule.

### 18. How do readiness, liveness, and startup probes differ?

Readiness determines whether a pod is ready to receive traffic. Liveness can trigger a container restart when the application becomes unhealthy. Startup probes protect slow initialization by delaying the other probes until startup succeeds. I configure each around application behavior to avoid removing healthy capacity or causing unnecessary restart cycles.

### 19. How would you troubleshoot a Kubernetes Service that cannot reach its pods?

I would check that the Service selector matches the intended pods, that ready endpoints exist, and that the target port matches the application’s listening port. Then I would test connectivity and DNS from within the cluster. If necessary, I would inspect network policies and the relevant ingress or load-balancer configuration.

### 20. How would you design an EKS workload for high availability?

I would distribute replicas and capacity across Availability Zones, configure resource requests and autoscaling, and use appropriate topology constraints. I would add readiness checks, controlled rollouts, and disruption budgets for voluntary disruptions. I would also test dependency failures and recovery because multiple replicas alone do not guarantee service availability.

### 21. What is the difference between pod autoscaling and node autoscaling?

Pod autoscaling changes workload replica counts based on configured metrics. Node autoscaling adjusts cluster capacity to support workloads. They need to work together: increasing replicas does not help if those pods cannot be scheduled. I would monitor application demand, pending pods, scaling limits, and the time needed to add capacity.

### 22. How do you troubleshoot an OOMKilled container?

I would compare memory usage with the configured limit and investigate whether the increase follows traffic, startup behavior, or a possible leak. I would review application metrics and recent changes. Increasing the limit can be a temporary mitigation, but I would also verify node capacity and investigate why memory consumption changed.

### 23. What makes a Docker image suitable for production?

I would use a trusted, minimal base image, a repeatable build, and only the dependencies required at runtime. I would avoid embedding secrets, run as a non-root user where practical, and scan the image. I would deploy an identifiable version or digest so releases and rollbacks use known artifacts.

## Focus Area 4: AWS Platform Troubleshooting

### 24. What is the difference between an ECS task role and execution role?

The task role provides AWS permissions to the application inside the container. The execution role supports operations ECS performs on the task’s behalf, such as image pulls and configured logging. Keeping them separate helps enforce least privilege and distinguish application access failures from task startup failures.

### 25. An ECS service keeps replacing tasks. What would you investigate?

I would review service events, stopped-task reasons, container exit codes, and logs. Then I would inspect startup configuration, resource limits, image access, and health checks. If a load balancer is involved, I would check its path, port, security rules, and startup allowance. I would determine whether tasks crash or fail health checks.

### 26. How would you troubleshoot an application that cannot connect to RDS?

I would distinguish connection timeout, authentication failure, and connection exhaustion. I would check endpoint resolution, routing, security groups, database availability, credentials, and connection limits. Testing from the application’s network context helps isolate the issue. I would avoid changing database accessibility before identifying the failed layer.

### 27. How would you troubleshoot Lambda errors or timeouts?

I would inspect invocation logs, error patterns, duration, throttling, and dependency latency. I would review recent changes and, where relevant, network access and IAM permissions. Increasing the timeout may hide a slow dependency, so I would establish where execution time is spent before choosing the correction.

### 28. How would you investigate S3 AccessDenied?

I would verify the caller identity, requested action, bucket, and object key. Then I would inspect applicable identity and bucket policies and any explicit restrictions. For encrypted objects, I would also check relevant KMS permissions. I would distinguish bucket-level operations from object-level operations because their permissions and resource scopes differ.

## Focus Area 5: Terraform and DevSecOps

### 29. How do you structure reusable Terraform modules?

I organize modules around clear infrastructure responsibilities, with documented inputs, outputs, and dependencies. I use validation and appropriate defaults while allowing necessary environment differences. I version modules and review changes before adoption. The goal is consistent infrastructure without creating a module so complex that teams struggle to understand its behavior.

### 30. What would you do after a partially failed Terraform apply?

I would inspect the error, state, and actual resources to understand what succeeded. Then I would correct the underlying issue and review a fresh plan before applying again. I would not assume the operation was atomic or manually delete resources just to restart. Any state repair would require careful verification.

### 31. How do you prevent unintended destruction with Terraform?

I review plans for deletions and replacements, separate environment state, and restrict production execution. I use resource deletion protections and lifecycle controls where appropriate, alongside backups and approval gates. I also investigate unexpected replacement plans rather than accepting them automatically. No single safeguard replaces understanding the proposed change.

### 32. How would you handle infrastructure drift?

I would inspect the difference and determine why the live configuration changed. If it was an approved emergency fix, I would update the code to preserve the intended configuration. If it was unauthorized or accidental, I would plan a controlled correction. I would also address the process or access gap that allowed recurring drift.

### 33. What security checks belong in the pipeline?

I would include secret detection, code analysis, dependency and container scanning, and infrastructure policy checks. My relevant tools include SonarQube, Trivy, and Checkov. I would define meaningful failure thresholds and documented exceptions with owners and expiration dates. Findings should be actionable, and production access should remain tightly controlled.

## Focus Area 6: Observability and Performance

### 34. How would you use Dynatrace, Splunk, and Grafana together?

I would use the available integrations to correlate service behavior across metrics, logs, and traces. Dynatrace can support application and dependency investigation, Splunk can support log analysis, and Grafana can present operational metrics and trends. I would connect findings using timestamps, request identifiers, and deployment markers, while being clear about my hands-on depth in each tool.

### 35. What metrics would you monitor for a critical service?

I would start with user-facing latency, traffic, errors, and saturation, then add dependency and platform metrics that explain those outcomes. For containers, that includes resource usage, restarts, and pending workloads. I would also monitor deployment health and relevant business transactions. Infrastructure health alone does not establish that users can complete their work.

### 36. How do logs, metrics, and traces complement each other?

Metrics reveal trends and help detect abnormal behavior. Logs provide detailed events and error context. Traces show how a request moves across components and where time or failures accumulate. I use them together: metrics identify the symptom, traces narrow the affected path, and logs help explain the failure.

### 37. How would you reduce alert fatigue?

I would review alerts for actionability, duplication, ownership, and user impact. I would route urgent symptoms to paging and lower-priority findings to tickets or dashboards. I would tune thresholds and durations using incident evidence, then review missed incidents as well as noisy alerts. Reducing noise should improve detection, not conceal failures.

## Focus Area 7: SLOs, Incident Management, and Reliability

### 38. Explain SLI, SLO, SLA, and error budget.

An SLI measures service behavior. An SLO sets a target for that measurement over a defined period. An SLA is an agreement that may include consequences for missing a commitment. The error budget is the unreliability allowed by the SLO. For a request-based 99.9% success target, 0.1% of eligible requests form the error budget.

### 39. How would you establish SLO governance?

I would agree on critical user journeys, indicator definitions, targets, measurement windows, and ownership with service stakeholders. We would define how error-budget consumption affects release decisions and reliability work. Regular reviews would examine actual performance and whether the indicators reflect user experience. Governance matters when the objectives guide decisions rather than simply populate a dashboard.

### 40. What is error-budget burn rate?

Burn rate describes how quickly a service consumes its error budget relative to the rate that would exhaust it over the SLO window. A high burn rate signals that the service is spending its reliability allowance too quickly. I would use appropriate short and long evaluation windows to detect urgent degradation while avoiding pages for insignificant spikes.

### 41. How do you manage a major production incident?

I first establish impact, severity, and incident ownership. I coordinate investigation and communication while prioritizing a safe mitigation, such as rollback or traffic shifting. I preserve a timeline and verify recovery through user-facing checks. Afterward, I contribute to a blameless review with concrete actions, owners, and follow-up dates.

### 42. What is the difference between mitigation and root-cause analysis?

Mitigation reduces user impact and restores service, even when the full cause is not yet known. Root-cause analysis explains the failure and contributing conditions afterward. For example, rollback may restore service immediately, while investigation identifies the configuration defect and missing validation that allowed it into production.

### 43. How do RTO and RPO influence recovery planning?

RTO defines the targeted time to restore service. RPO defines the acceptable data-loss window. Those objectives influence backup frequency, replication, recovery architecture, and operational procedures. I would validate them through recovery exercises because configured backups do not prove that a service can recover within its agreed objectives.

## Focus Area 8: Automation and Role Alignment

### 44. How would you use Python and Bash to reduce operational work?

I would use Bash for small command-based tasks and Python for more complex API workflows, validation, and reporting. A useful example is deployment verification that checks rollout status and application health. I would include timeouts, bounded retries, logging, and clear failure results. Infrastructure-changing automation would also need safeguards such as dry-run support and scoped permissions.

### 45. Why are you interested in this role, and are you comfortable working onsite?

This role aligns with my strengths in cloud infrastructure, Terraform, CI/CD, containers, and troubleshooting. I’m particularly interested in combining automation with production reliability and applying my Claude-assisted pipeline troubleshooting experience.

I’m currently based in Atlanta, Georgia, and I’m open to relocating to either Charlotte, North Carolina, or Detroit, Michigan. I understand the role requires working onsite five days a week.

---

**Preparation priority:** Start with questions 1–12. Claude-assisted pipeline troubleshooting is the mandatory screening requirement. Be ready to explain the exact error, configuration correction, and verification from your real example.
