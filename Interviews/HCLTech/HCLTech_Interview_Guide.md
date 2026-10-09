# HCLTech Interview Preparation Guide
## Olalekan Gabriel Ogundare

Focus: Linux systems engineering, automation, programming, VMware/AWS, server lifecycle management, and Agile delivery.

Answers are intended for approximately 45–60 seconds of spoken delivery. STAR stories are sample scenarios based on your stated technical background, not verified incidents. Confirm the details, your ownership, and results before using them as personal experience.

## Index

- [Elevator pitch](#elevator-pitch)
- [Linux, automation, programming, and delivery — questions 1–10](#linux-automation-programming-and-delivery)
- [VMware HA, DR, vMotion, vSAN, and networking — questions 11–22](#vmware-ha-dr-vmotion-vsan-and-networking)
- [STAR stories — five examples](#star-stories)
- [Questions to ask HCLTech](#questions-to-ask-hcltech)

## Elevator pitch

I’m Olalekan Gabriel Ogundare, an infrastructure and cloud engineer with over 15 years of IT experience, including Linux administration, VMware, and AWS/Azure environments.

My strengths are troubleshooting production systems and automating infrastructure with Ansible, Terraform, Python, and Bash. My background includes RHEL support, infrastructure provisioning, configuration management, security hardening, and CI/CD automation.

I also bring experience with VMware technologies such as ESXi, HA, DRS, and vMotion, along with collaborating across development, security, and operations teams.

For this HCLTech opportunity, I would bring a hands-on approach to improving Linux reliability, reducing manual operational work, and managing infrastructure changes through testing, code review, and controlled releases.

## Linux, automation, programming, and delivery

### 1. How do you troubleshoot a slow RHEL server?

**Answer:** I first establish the scope: whether the issue affects the entire host or a specific application, when it started, and what recently changed. I check CPU and load with `top` and `uptime`, memory with `free` and `vmstat`, and disk latency with `iostat`. I review service logs using `journalctl` and check network connections with `ss`. High load does not always mean high CPU; processes waiting on disk can also increase it. I address the identified bottleneck, validate application health, and document the root cause.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 2. How would you troubleshoot a Linux service that fails to start?

**Answer:** I begin with `systemctl status` and `journalctl -u` to identify the failure. I check configuration syntax, file permissions, dependencies, available disk space, and port conflicts. On RHEL, I also investigate SELinux denials instead of disabling SELinux. If the failure follows a deployment, I compare the configuration with the previous working version and use the approved rollback when appropriate. I then verify both service status and application functionality.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 3. How do you automate Linux configuration with Ansible?

**Answer:** I organize automation into reusable roles for packages, users, security settings, monitoring, and application configuration. I use inventories and variables to handle environment differences and handlers to restart services only when needed. I aim for idempotency, so repeated runs preserve the desired state without unnecessary changes. Before production, I review the code, run syntax and lint checks, and test against representative systems. For wider rollouts, I use small batches and health checks.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 4. What is the difference between Terraform and Ansible?

**Answer:** Terraform primarily provisions infrastructure, such as virtual machines, networks, and storage, and tracks managed resources in state. Ansible primarily configures operating systems and applications, such as installing packages, managing users, and updating services. I would use Terraform to create an AWS instance or VMware VM, then Ansible to configure the Linux host. Keeping those responsibilities clear makes troubleshooting and ownership easier.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 5. How would you manage patching across production Linux servers?

**Answer:** I start with inventory, application dependencies, approved repositories, and maintenance requirements. I test updates in a representative nonproduction environment and confirm recovery options. For production, I patch a canary host or small batch first, drain workloads where necessary, and reboot when required. Validation includes service health, application transactions, monitoring, and package or kernel versions. I retain the change record and test evidence before closing the maintenance activity.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 6. How would you use Python in infrastructure engineering?

**Answer:** I use Python when a task needs API integration, structured data processing, or more complex logic than a shell script comfortably supports. Examples include collecting AWS inventory, checking infrastructure compliance, and generating operational reports. I build in logging, exception handling, timeouts, and safe retry behavior. For scripts that modify infrastructure, I include a dry-run option and explicit scope controls.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 7. What VMware concepts should you be comfortable explaining?

**Answer:** ESXi is the hypervisor, while vCenter provides centralized management. HA helps restart virtual machines following host failures. DRS balances workloads across hosts, and vMotion supports live migration between compatible hosts. When troubleshooting performance, I check guest metrics alongside host CPU contention, memory pressure, datastore latency, and networking. I also verify available cluster capacity before maintenance.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 8. How do you approach firmware and server hardware lifecycle management?

**Answer:** I first inventory server models, firmware versions, support status, and hardware health. I review the vendor compatibility matrix for BIOS, management controllers, NICs, storage controllers, and the operating system or hypervisor. I test the update sequence, schedule maintenance, and confirm recovery options. After updating, I validate hardware health, storage paths, networking, and workload performance. I document versions and results for future maintenance.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 9. How do you apply Agile and SDLC practices to infrastructure?

**Answer:** I manage infrastructure changes as version-controlled code. A Jira item captures the requirement and acceptance criteria, and a pull request provides peer review. Automated checks validate syntax, security, and expected behavior before deployment. Changes move through testing and controlled production release, with rollback procedures and monitoring. After deployment, I attach validation evidence and update operational documentation.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 10. Do you have experience with every language and configuration tool listed?

**Answer:** My strongest hands-on tools are Ansible and Terraform, with Python and Bash for automation, and Go where applicable. I would distinguish production experience from familiarity when discussing Puppet, Chef, Perl, C++, or Ruby. The transferable skills are understanding configuration state, reusable code, testing, troubleshooting, and controlled deployment.

[⬆ Go to top](#hcltech-interview-preparation-guide)

## VMware HA, DR, vMotion, vSAN, and networking

### 11. What is VMware HA, and how does it work?

**Answer:** VMware High Availability monitors hosts and virtual machines within a cluster. When an ESXi host fails, HA restarts affected VMs on surviving hosts, provided sufficient capacity and accessible storage are available. It uses management-network heartbeats and datastore heartbeats to help distinguish host failure from network isolation. I check admission control, failover capacity, isolation responses, and VM restart priorities. HA involves a restart, so applications can experience an interruption.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 12. What is the difference between VMware HA and disaster recovery?

**Answer:** HA handles failures within a cluster, such as losing an ESXi host. Disaster recovery addresses larger failures, including losing a site or storage platform. DR requires replicated workloads or recoverable backups, recovery infrastructure, networking, and a tested recovery plan. I define the recovery time objective, or RTO, and recovery point objective, or RPO, with application owners. I then test recovery order, dependencies, application functionality, and failback.

| Capability | VMware HA | Disaster recovery |
| --- | --- | --- |
| Primary scope | Host failure within a cluster | Site or major infrastructure failure |
| Recovery approach | Restart VMs on surviving hosts | Recover workloads at a recovery location |
| Key dependency | Available cluster capacity and storage | Replication/backups and recovery infrastructure |
| Validation | VM restart and application health | RTO, RPO, dependencies, and application health |

**RTO:** Target time to restore service.  
**RPO:** Maximum acceptable data loss expressed as a time interval.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 13. How would you design and test VMware disaster recovery?

**Answer:** I start by identifying critical applications, dependencies, and business-approved RTO and RPO targets. I establish the replication or backup method and confirm recovery-site compute, storage, and network capacity. The recovery plan includes DNS changes, firewall rules, startup order, and application validation. I conduct an isolated recovery test where possible, measure recovery time, and confirm the recovered data meets the RPO. Application owners approve the functional results, and I document gaps and remediation before closing the test.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 14. What is vMotion, and how is it different from Storage vMotion?

**Answer:** vMotion moves a running VM between ESXi hosts while preserving its execution state. It transfers memory and execution state, with a brief switchover during completion. Storage vMotion moves a running VM’s virtual disks between datastores. I use vMotion for host maintenance or workload balancing and Storage vMotion for storage maintenance or migration. Before either operation, I check compatibility, available capacity, connectivity, and destination access.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 15. What would you check if vMotion fails?

**Answer:** I begin with the migration error in vCenter to narrow the cause. I check that the source and destination hosts have correctly configured vMotion VMkernel interfaces and can communicate over the intended network. I validate VLANs, routing where applicable, MTU consistency, and bandwidth. I also check CPU compatibility or EVC, destination resources, storage access, and VM devices that may prevent migration. I use `vmkping` with the appropriate interface or TCP/IP stack and review host logs before retrying.

**EVC:** Enhanced vMotion Compatibility provides a compatible CPU feature baseline across supported hosts.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 16. What is VMware vSAN?

**Answer:** vSAN pools local storage devices across ESXi hosts into shared storage for virtual machines. It uses storage policies to define requirements such as failures to tolerate and the protection method. Depending on the architecture and policy, data can be protected through mirroring or erasure coding. I focus on policy compliance, host and device health, available capacity, network performance, and resynchronization activity. vSAN availability depends on the placement of data components, quorum, and sufficient resources to satisfy the policy.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 17. How do you troubleshoot a vSAN performance problem?

**Answer:** I establish whether the problem affects one VM, one host, or the cluster. I examine VM and backend storage latency, device health, network utilization, packet loss, and resynchronization activity. I also check capacity pressure and whether storage policies are compliant. I correlate the slowdown with recent failures, maintenance, or workload changes. Once I identify the bottleneck, I make a controlled correction and verify both application performance and vSAN health.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 18. What should you consider before putting a vSAN host into maintenance mode?

**Answer:** I check cluster health, policy compliance, free capacity, and whether another failure or resynchronization is already in progress. I then choose the appropriate data migration option. Full data migration evacuates data and requires adequate capacity. Ensure accessibility keeps objects accessible but may reduce redundancy. No data migration leaves components on the host and can affect accessibility depending on the object layout. After maintenance, I verify that the host rejoins correctly and that objects return to the required policy compliance.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 19. Explain VMware networking and the difference between a standard and distributed switch.

**Answer:** A vSphere Standard Switch is configured separately on each ESXi host. A vSphere Distributed Switch provides centralized configuration through vCenter across participating hosts. VM port groups connect VM virtual NICs to networks, while VMkernel adapters support host services such as management, vMotion, and storage traffic. Physical NICs provide uplinks to the physical network. I keep port-group VLANs, uplink configuration, redundancy, and MTU settings consistent with the physical switches.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 20. How would you troubleshoot a VM that cannot reach the network?

**Answer:** I work through the path from the guest to the physical network. I check the guest IP address, subnet mask, gateway, DNS, and firewall. Then I confirm that its virtual NIC is connected to the correct port group and VLAN. On the host, I inspect uplink health, NIC teaming, and relevant switch configuration. I verify that the physical switch allows the VLAN and check routing or firewall rules beyond it. Comparing against a working VM helps isolate whether the fault is in the guest, virtual network, or upstream network.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 21. How do you provide network redundancy in VMware?

**Answer:** I use multiple physical uplinks and, where the design supports it, connect them to separate physical switches. I configure teaming and failover policies to match the physical network design. I also consider management, vMotion, and storage traffic separately so critical services have suitable redundancy and bandwidth. I validate the design by testing an uplink failure and confirming that connectivity and application health remain acceptable.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### 22. What is the difference between HA, DRS, and vMotion?

**Answer:** HA restores availability by restarting VMs following a host failure. DRS evaluates cluster resource demand and recommends or performs VM placement changes. vMotion is the mechanism used to move running VMs between compatible hosts. They work together: HA addresses failure recovery, DRS manages resource placement, and vMotion enables live movement for balancing and maintenance.

[⬆ Go to top](#hcltech-interview-preparation-guide)

## STAR stories

These are adaptable sample answers. Use actual projects and verified results; add a company name or metric only when accurate.

### Story 1. Linux production incident — troubleshooting and recovery

**Interview question:** Tell me about a time you resolved a Linux production performance issue.

**Situation:** A business application running on RHEL experienced slow response times and intermittent timeouts.

**Task:** My responsibility was to identify the infrastructure bottleneck and restore service while keeping the application team informed.

**Action:** I checked CPU, memory, disk latency, and service logs using `top`, `vmstat`, `iostat`, and `journalctl`. The investigation pointed to excessive logging that was consuming disk capacity and increasing I/O pressure. I coordinated with the application owner, safely reclaimed space according to retention requirements, corrected log rotation, and validated the application through functional checks.

**Result:** Application performance recovered. I documented the root cause and added disk-capacity monitoring and log-management checks to reduce recurrence.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### Story 2. Ansible automation — consistent Linux configuration

**Interview question:** Tell me about a time you automated a manual infrastructure process.

**Situation:** Linux servers were being configured manually, which created differences in packages, user permissions, and security settings across environments.

**Task:** I needed to make configuration repeatable and reduce the effort required to prepare and maintain servers.

**Action:** I developed reusable Ansible roles for package installation, user management, SSH settings, monitoring agents, and service configuration. I separated environment-specific values into inventory variables and used handlers for controlled service restarts. I tested the roles in nonproduction, checked that repeated runs produced no unnecessary changes, and deployed in small batches with health checks.

**Result:** Server configuration became more consistent and easier to audit. The team could provision and maintain systems through reviewed automation instead of repeating manual procedures.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### Story 3. Terraform delivery — reusable infrastructure and controlled changes

**Interview question:** Describe a project where you standardized infrastructure using Terraform.

**Situation:** Application teams needed similar cloud infrastructure, but separate implementations were creating inconsistent networking, security, and deployment practices.

**Task:** I was responsible for standardizing infrastructure delivery while allowing teams to supply their application-specific requirements.

**Action:** I developed reusable Terraform modules with documented inputs and outputs. I used remote state, pinned module versions, and integrated planning and security checks into the CI/CD workflow. Pull requests included the proposed infrastructure changes for review. I tested module updates in nonproduction and documented migration steps when a change affected existing consumers.

**Result:** Teams gained a repeatable deployment process with clearer change visibility. Shared modules reduced duplicated work and made infrastructure support and maintenance easier.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### Story 4. VMware maintenance — availability during infrastructure changes

**Interview question:** Tell me about a time you maintained VMware infrastructure while protecting application availability.

**Situation:** A VMware environment supporting business applications required host maintenance while workloads needed to remain available.

**Task:** I needed to prepare the cluster, coordinate the maintenance, and verify that applications remained healthy.

**Action:** I reviewed cluster capacity, HA settings, host health, datastore availability, and migration compatibility. I coordinated the maintenance window with application owners and moved eligible virtual machines using vMotion before placing each host into maintenance mode. After the approved updates, I checked host connectivity, storage paths, networking, and virtual-machine health before returning the host to service.

**Result:** Maintenance was completed in a controlled sequence, with application validation recorded in the change ticket. The documented procedure made subsequent maintenance more predictable.

[⬆ Go to top](#hcltech-interview-preparation-guide)

### Story 5. Server lifecycle management — patching and firmware coordination

**Interview question:** Describe how you managed or supported a server patching and firmware maintenance activity.

Use this story if you participated in hardware or firmware maintenance. Describe your role as coordination or support if another team performed the updates.

**Situation:** Infrastructure servers required operating-system and firmware updates to address supportability and security requirements.

**Task:** My responsibility was to coordinate the changes and ensure that the Linux or virtualization platform remained compatible and operational.

**Action:** I worked with the hardware team to review server inventory, vendor compatibility guidance, and the proposed update sequence. I confirmed recovery procedures and tested the changes on representative systems. During production maintenance, we processed small batches, checked hardware health and platform connectivity, and asked application owners to validate their workloads. I attached the update records and validation evidence to the change ticket.

**Result:** The maintenance activity closed with documented versions, health checks, and application-owner sign-off. This improved lifecycle visibility and provided a repeatable process for future updates.

[⬆ Go to top](#hcltech-interview-preparation-guide)

## Questions to ask HCLTech

1. How is the role split between Linux, VMware, AWS, and physical server operations?
2. Which automation tools are standard today, and what needs improvement?
3. Does this role own firmware updates directly or coordinate with a hardware team?
4. What are the main reliability or lifecycle challenges you want this engineer to solve?

## Final preparation checklist

- Rehearse the elevator pitch and each STAR answer within approximately 60 seconds.
- Be ready to explain the diagnostic evidence behind each troubleshooting decision.
- Distinguish work you owned from work you supported.
- Use verified company names, project details, and metrics.
- Be clear about direct AWS experience versus VMware Cloud on AWS experience.
- Practice explaining HA versus DR, vMotion versus Storage vMotion, and standard versus distributed switches.

