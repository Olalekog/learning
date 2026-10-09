# Teradata Staff Virtualization Engineer — Interview Preparation

**Prepared for:** Olalekan Gabriel Ogundare  
**Context:** Tech Consulting / Teradata role preparation  
**Contents:** 38 interview questions and answers, six STAR templates, and questions to ask the interviewer.

These sample answers describe an approach rather than claim unconfirmed experience. The STAR stories are practice templates. Replace bracketed details with your actual work at Tech Consulting, Citi, or another employer. Distinguish production ownership, lab experience, and conceptual knowledge. Aim for approximately 45–60 seconds for an initial spoken answer, then expand when asked.

## Index

| Focus area | Questions | Topics |
|---|---|---|
| [VMware Architecture and Availability](#vmware-architecture-and-availability) | 1–2 | Enterprise design; HA, DRS, vMotion |
| [Performance Troubleshooting](#performance-troubleshooting) | 3–4 | Slow VMs; esxtop, esxcli, pktcap-uw |
| [KVM and Harvester](#kvm-and-harvester) | 5 | Architecture and evaluation |
| [Infrastructure Automation](#infrastructure-automation) | 6 | Terraform, PowerCLI, Python |
| [Network Troubleshooting](#network-troubleshooting) | 7 | Connectivity and traffic paths |
| [Infrastructure Security](#infrastructure-security) | 8 | Access, hardening, patching, auditing |
| [Platform Testing and Release Readiness](#platform-testing-and-release-readiness) | 9–10 | End-to-end testing and release risks |
| [EDW, Analytics, and AI Infrastructure](#edw-analytics-and-ai-infrastructure) | 11 | Mixed workloads and isolation |
| [Staff-Level Engineering Ownership](#staff-level-engineering-ownership) | 12 | Leadership and communication |
| [Behavioral and STAR Stories](#behavioral-and-star-stories) | 13–18 | Availability, incidents, automation, security, upgrades, customer issues |
| [vSAN](#vsan) | 19–27 | Architecture, policies, resilience, performance, maintenance, capacity |
| [Virtual Networking](#virtual-networking) | 28–38 | Switching, VLANs, VMkernel, L2/L3, teaming, MTU, overlays |
| [Questions to Ask the Interviewer](#questions-to-ask-the-interviewer) | — | Team priorities and expectations |
| [Technical References](#technical-references) | — | VMware/Broadcom and Harvester documentation |

### Detailed question index

1. [How would you design an enterprise VMware environment for database and analytics workloads?](#q1)
2. [What is the difference between HA, DRS, and vMotion?](#q2)
3. [How would you troubleshoot a slow VM or database workload?](#q3)
4. [When would you use esxtop, esxcli, and pktcap-uw?](#q4)
5. [What do you understand about KVM and Harvester?](#q5)
6. [How would you automate VMware provisioning?](#q6)
7. [How would you troubleshoot VM network connectivity?](#q7)
8. [How would you secure a virtualized infrastructure?](#q8)
9. [How would you test this platform end to end?](#q9)
10. [How would you detect at-risk features before release?](#q10)
11. [How would you support EDW, analytics, and AI workloads on the same platform?](#q11)
12. [What does staff-level ownership mean to you?](#q12)
13. [Tell me about a highly available virtualization environment you designed or improved.](#q13)
14. [Describe a difficult virtualization performance incident.](#q14)
15. [Tell me about infrastructure automation you implemented.](#q15)
16. [Describe a security improvement you made.](#q16)
17. [Tell me about an upgrade or infrastructure change you validated.](#q17)
18. [Describe a customer issue that required several teams to solve.](#q18)
19. [What is VMware vSAN, and how does it work?](#q19)
20. [What is the difference between vSAN OSA and ESA?](#q20)
21. [What are storage policies and Failures to Tolerate—FTT?](#q21)
22. [How do you compare RAID-1 with RAID-5 or RAID-6 in vSAN?](#q22)
23. [How would you troubleshoot high vSAN latency?](#q23)
24. [What happens when a disk or host fails in vSAN?](#q24)
25. [What are the vSAN maintenance-mode options?](#q25)
26. [What is a vSAN stretched cluster, and why does it need a witness?](#q26)
27. [How would you plan vSAN capacity for an enterprise database platform?](#q27)
28. [What is the difference between a standard switch and a distributed switch?](#q28)
29. [What is the difference between a VMkernel adapter and a VM network adapter?](#q29)
30. [What are VLANs, and how do you use them in VMware?](#q30)
31. [Explain Layer 2 and Layer 3 troubleshooting in a virtual environment.](#q31)
32. [What is NIC teaming, and how is it different from LACP?](#q32)
33. [What is MTU, and how would you troubleshoot a jumbo-frame issue?](#q33)
34. [How would you troubleshoot a failed vMotion?](#q34)
35. [A VM communicates with VMs on the same host but fails across hosts. What do you check?](#q35)
36. [How would you troubleshoot a vSAN network partition?](#q36)
37. [What is the difference between an underlay and an overlay network?](#q37)
38. [How would you design networking for mixed database, analytics, and AI workloads?](#q38)

## VMware Architecture and Availability

<a id="q1"></a>
### 1. How would you design an enterprise VMware environment for database and analytics workloads?

I would start with workload requirements: CPU and memory demand, storage latency and throughput, availability targets, and expected growth. I would then design the cluster with sufficient capacity to handle a host failure and planned maintenance.

I would evaluate host compatibility, storage architecture, redundant networking, and workload placement. I would configure HA, DRS, and admission control around the availability requirements, and separate management, migration, storage, and application traffic appropriately.

Before production, I would validate the design with representative workloads, migration tests, and host-failure scenarios. My deliverables would include the architecture, performance baseline, capacity assumptions, and operational runbooks.

<a id="q2"></a>
### 2. What is the difference between HA, DRS, and vMotion?

| Technology | Purpose |
|---|---|
| vSphere HA | Restarts affected VMs on surviving hosts after a host failure, provided capacity and required resources are available. |
| DRS | Evaluates resource demand and recommends or performs VM placement and balancing within a cluster, depending on configuration. |
| vMotion | Moves a running VM between compatible hosts with minimal interruption. It supports planned maintenance and resource balancing. |

HA addresses recovery after a failure. DRS manages workload placement and resource balance. vMotion provides the live migration mechanism used for maintenance and some DRS actions. I would design and test them together, while remembering that restarting a VM does not automatically guarantee application recovery.

## Performance Troubleshooting

<a id="q3"></a>
### 3. How would you troubleshoot a slow VM or database workload?

I would first establish the scope: whether the problem affects one VM, one host, a datastore, or the entire cluster. I would check when it started and correlate it with deployment, backup, migration, or infrastructure changes.

Using vCenter metrics and `esxtop`, I would examine CPU scheduling, memory pressure, storage latency, and network behavior. High CPU Ready, for example, would prompt me to investigate contention, limits, and VM sizing rather than immediately adding vCPUs.

I would correlate host observations with guest operating system and application metrics, test the most likely cause, and make a controlled change. Finally, I would repeat the same workload and compare the results with the baseline.

**Technical note:** CPU Ready needs interpretation alongside other metrics, VM sizing, and whether the value is per-vCPU or aggregated. See references 1–2.

<a id="q4"></a>
### 4. When would you use esxtop, esxcli, and pktcap-uw?

| Tool | Interview explanation |
|---|---|
| `esxtop` | Investigate live host and VM resource behavior and collect performance samples. |
| `esxcli` | Inspect ESXi configuration and operational state, including network, storage, and system information. Some commands make changes, so verify their impact first. |
| `pktcap-uw` | Capture traffic at selected points in the ESXi networking path to investigate connectivity or packet behavior. |

I choose the tool based on the question I need to answer. For resource contention, I start with performance metrics. For configuration and device state, I use `esxcli`. For suspected packet loss or traffic-path issues, I use a narrowly scoped packet capture and correlate it with the physical network.

## KVM and Harvester

<a id="q5"></a>
### 5. What do you understand about KVM and Harvester?

KVM provides virtualization capabilities in the Linux kernel. Harvester is a hyperconverged infrastructure platform built on technologies including Kubernetes, KubeVirt, KVM, and Longhorn. KubeVirt provides VM management on Kubernetes, while Longhorn provides distributed block storage.

When evaluating Harvester, I would examine the whole operational platform: VM lifecycle, storage performance, networking, availability, backup, upgrades, and monitoring. I would validate those capabilities against the actual database and analytics workload before proposing a migration.

**If your experience is limited, add:** “My strongest hands-on experience is in [platform]. My Harvester experience currently covers [lab work, evaluation, or study], and I would distinguish that from production ownership.”

See reference 3.

## Infrastructure Automation

<a id="q6"></a>
### 6. How would you automate VMware provisioning?

I would define a repeatable provisioning process using approved templates and version-controlled infrastructure code. Terraform would manage supported infrastructure resources, while PowerCLI or Python could handle validation, reporting, and operational tasks.

The workflow would check naming, network mappings, datastore capacity, access permissions, and required inputs before deployment. Changes would go through code review, a reviewed plan, and the appropriate approval.

After provisioning, automated checks would confirm the VM configuration, connectivity, monitoring, and application readiness. I would also protect credentials and state, handle partial failures, and document recovery steps so the automation is safe to operate.

## Network Troubleshooting

<a id="q7"></a>
### 7. How would you troubleshoot VM network connectivity?

I would first determine whether the issue affects a single VM, a VLAN, a host, or multiple networks. Inside the guest, I would validate the IP address, subnet, gateway, routes, DNS, and local firewall.

Then I would follow the traffic path through the virtual NIC, port group, virtual switch, host uplink, physical switch, and routed network. I would check VLAN configuration, interface errors, MTU consistency, and any relevant security controls.

If the configuration looked correct, I would capture traffic at selected points to identify where communication stops. After remediation, I would validate both connectivity and the affected application.

## Infrastructure Security

<a id="q8"></a>
### 8. How would you secure a virtualized infrastructure?

I would begin with controlled administrative access, least-privilege roles, and separation of management traffic from workload traffic. I would maintain supported software versions, apply approved hardening settings, and manage certificates and service credentials.

I would also centralize logs, monitor privileged activity and configuration changes, and restrict unnecessary management services. Automation accounts would receive only the permissions required for their tasks.

Before applying security changes broadly, I would test their impact on availability, migrations, backups, and application connectivity. I would retain evidence of the configuration and document any approved exceptions.

## Platform Testing and Release Readiness

<a id="q9"></a>
### 9. How would you test this platform end to end?

I would test the complete customer workflow, from infrastructure deployment to workload execution, monitoring, backup, and recovery.

Functional tests would confirm provisioning and integration. Performance tests would measure representative workloads under normal and peak demand. Resilience tests would cover controlled host failures, network interruptions, and storage degradation. Upgrade tests would verify compatibility, workload behavior, and recovery procedures.

I would define acceptance criteria before execution, collect consistent results, and integrate repeatable tests into CI/CD. Failed tests would include enough logs and environment details for engineers to reproduce the issue.

<a id="q10"></a>
### 10. How would you detect at-risk features before release?

I would look for changes in test reliability, performance, resource consumption, and unresolved defects. A feature could pass functional tests but still introduce slower queries, excessive storage activity, or recovery problems.

I would compare results against a stable baseline, track recurring failures, and assess customer impact. For a high-risk feature, I would work with the owning team to isolate the regression and agree on a release decision using evidence.

My role would be to make the risk visible early, identify an owner, and ensure the mitigation has clear acceptance criteria.

## EDW, Analytics, and AI Infrastructure

<a id="q11"></a>
### 11. How would you support EDW, analytics, and AI workloads on the same platform?

I would first characterize the workloads because they can have different resource and performance requirements. I would assess database latency, analytics throughput, memory demand, data movement, and any accelerator requirements.

I would then evaluate resource allocation, placement, and isolation to reduce interference between workloads. Capacity planning would include peak demand, failure conditions, and maintenance.

The key validation would be running representative workloads concurrently. I would measure whether one workload degrades another and use those results to adjust the design. I would also confirm that the proposed configuration is supported for the application.

## Staff-Level Engineering Ownership

<a id="q12"></a>
### 12. What does staff-level ownership mean to you?

Staff-level ownership means making sound technical decisions while improving how the team delivers and operates the platform.

I would clarify requirements, document trade-offs, review designs and code, and identify risks early. During incidents, I would help teams build a shared understanding of the evidence and coordinate the investigation.

Beyond resolving the immediate issue, I would look for improvements to testing, automation, monitoring, or documentation. I would communicate technical details to engineers and explain business impact and decisions clearly to customers and leadership.

## Behavioral and STAR Stories

These six examples are templates. Use only verified details and results from your own experience.

<a id="q13"></a>
### 13. Tell me about a highly available virtualization environment you designed or improved.

- **Situation:** At [company], [application] depended on a virtualization environment with [availability or capacity concern].
- **Task:** I was responsible for improving resilience while meeting [availability requirement].
- **Action:** I reviewed resource demand, failure capacity, storage dependencies, and network redundancy. I implemented [actual changes], validated workload placement, and coordinated controlled failure and maintenance tests.
- **Result:** Testing demonstrated [verified recovery behavior or improvement]. I documented the design and operational procedures so the support team could maintain it consistently.

<a id="q14"></a>
### 14. Describe a difficult virtualization performance incident.

- **Situation:** At [company], users experienced [slow queries or application delays] during [specific conditions].
- **Task:** I needed to isolate the infrastructure contribution and restore acceptable performance.
- **Action:** I correlated application timestamps with host and guest metrics. I investigated CPU scheduling, memory pressure, storage latency, and network behavior. The evidence identified [actual cause], so I applied [specific remediation] and repeated the workload.
- **Result:** Performance changed from [baseline] to [verified outcome]. I added [monitoring or preventive control] to improve early detection.

<a id="q15"></a>
### 15. Tell me about infrastructure automation you implemented.

- **Situation:** At [company], provisioning required [manual steps], which caused [delays or inconsistency].
- **Task:** My responsibility was to make deployment repeatable and easier to validate.
- **Action:** I developed [Terraform modules, PowerCLI scripts, or Python automation], stored the code in version control, and added input checks, peer review, and post-deployment validation. I also handled credentials and partial failures.
- **Result:** The process achieved [verified time saving or consistency improvement]. The team could deploy through a documented workflow with clearer ownership and traceability.

<a id="q16"></a>
### 16. Describe a security improvement you made.

- **Situation:** At [company], a review identified [specific access, patching, logging, or configuration issue].
- **Task:** I needed to address the issue while protecting service availability.
- **Action:** I assessed the affected systems and dependencies, tested the remediation, and coordinated implementation through change control. I then validated application behavior and collected evidence that the control was working.
- **Result:** We resolved [specific finding] and introduced [automated check, monitoring, or documented standard] to help prevent recurrence.

<a id="q17"></a>
### 17. Tell me about an upgrade or infrastructure change you validated.

- **Situation:** At [company], we planned to upgrade [platform/component] supporting [workload].
- **Task:** I was responsible for validating compatibility and minimizing disruption.
- **Action:** I reviewed dependencies, established a performance baseline, and tested the upgrade in a representative environment. I verified backup and recovery readiness, workload functionality, migration behavior, and monitoring before a staged rollout.
- **Result:** The change met [verified acceptance criteria]. We captured [issues discovered or lessons learned] and updated the runbook for subsequent maintenance.

<a id="q18"></a>
### 18. Describe a customer issue that required several teams to solve.

- **Situation:** At [company], a customer reported [problem] spanning the application and infrastructure layers.
- **Task:** I coordinated the technical investigation and helped establish a clear cause.
- **Action:** I built a shared timeline, collected logs and metrics, and assigned specific hypotheses to the relevant teams. We reproduced the issue under [conditions], identified [actual cause], and validated the fix against the original failure.
- **Result:** The customer confirmed [verified outcome]. I documented the root cause and helped add a regression test or monitoring improvement.

## vSAN

<a id="q19"></a>
### 19. What is VMware vSAN, and how does it work?

VMware vSAN is software-defined storage integrated with the VMware hypervisor. In a typical hyperconverged deployment, it aggregates storage devices across hosts into shared storage for virtual machines.

It manages VM data as objects, with protection and placement controlled through storage policies. Those policies define requirements such as failure tolerance and the protection method.

When designing a vSAN environment, I consider workload latency, throughput, usable capacity, network reliability, and failure domains. I also plan capacity for maintenance and recovery, because normal operating capacity alone is not enough.

<a id="q20"></a>
### 20. What is the difference between vSAN OSA and ESA?

| Area | Original Storage Architecture—OSA | Express Storage Architecture—ESA |
|---|---|---|
| Storage organization | Disk groups with separate cache and capacity devices | Storage pools without dedicated cache devices |
| Hardware design | Supports certified configurations using several device types | Designed around certified high-performance NVMe configurations |
| Device failure impact | Failure of a cache device can affect its entire disk group | Removes the disk-group dependency on a dedicated cache device |
| Design consideration | Evaluate disk-group layout and cache/capacity requirements | Evaluate ESA-compatible hardware and workload requirements |

I would first identify the architecture and software version because hardware requirements, failure behavior, and operational procedures differ. I would validate the design against the compatibility guidance for that exact release.

See references 4–5.

<a id="q21"></a>
### 21. What are storage policies and Failures to Tolerate—FTT?

A vSAN storage policy defines how an object should be protected and placed. FTT specifies the number of failures the policy is designed to tolerate within the applicable failure model.

For example, a policy using FTT=1 and mirroring maintains redundant data copies across appropriate failure domains. Erasure coding offers another protection method with different capacity and placement requirements.

I would choose policies based on application criticality, available hosts, performance requirements, and usable capacity. I would then verify policy compliance. Assigning a policy does not prove the cluster currently satisfies it.

<a id="q22"></a>
### 22. How do you compare RAID-1 with RAID-5 or RAID-6 in vSAN?

RAID-1 uses mirroring, while RAID-5 and RAID-6 use erasure coding. Mirroring consumes capacity for additional data copies. Erasure coding can provide better capacity efficiency, but the supported layouts and minimum host requirements depend on the architecture and release.

I would evaluate the workload, required failure tolerance, rebuild behavior, and available capacity before selecting a policy. I would also benchmark the actual platform rather than assume that performance comparisons from OSA apply directly to ESA.

<a id="q23"></a>
### 23. How would you troubleshoot high vSAN latency?

I would establish whether the latency affects one VM, several objects, one host, or the entire cluster. Then I would correlate application response times with vSAN performance metrics.

I would check backend device latency, network packet loss, bandwidth utilization, capacity pressure, and active resynchronization. I would also review recent policy changes, failures, or maintenance.

After identifying the likely bottleneck, I would make a controlled change and compare the same workload before and afterward. For Teradata workloads, I would include query response time and throughput in the validation, not just storage metrics.

<a id="q24"></a>
### 24. What happens when a disk or host fails in vSAN?

The outcome depends on the object’s policy, existing health, component placement, and available quorum. If sufficient data and quorum remain, the object can stay accessible, although its redundancy may be reduced.

I would check object health, affected components, and resynchronization activity. I would also confirm that the cluster has sufficient capacity and eligible failure domains to restore protection.

I would avoid additional disruptive maintenance until I understood the remaining tolerance. The recovery process is complete when objects regain the required protection, not simply when the failed host returns.

<a id="q25"></a>
### 25. What are the vSAN maintenance-mode options?

| Option | Behavior | Main consideration |
|---|---|---|
| Ensure accessibility | Moves data as needed to keep affected objects accessible | Objects may have reduced redundancy |
| Full data migration | Evacuates the host’s vSAN data and seeks to maintain policy compliance elsewhere | Requires sufficient capacity and eligible placement |
| No data migration | Does not evacuate vSAN data | Some objects may become inaccessible or lose protection |

Before entering maintenance mode, I would run the data migration pre-check and review object health, capacity, and existing failures. I would select the option based on the maintenance duration and required protection, then verify health and resynchronization after the host returns.

See references 6–7.

<a id="q26"></a>
### 26. What is a vSAN stretched cluster, and why does it need a witness?

A vSAN stretched cluster distributes storage across two data sites and uses a witness in a separate failure domain. With the appropriate policy, data is protected across the sites.

The witness holds witness components used for quorum decisions; it does not store the workload’s normal data replicas. It helps the cluster determine which components can remain available during certain failures.

I would validate intersite connectivity, latency, bandwidth, witness reachability, and capacity at the surviving site. I would also distinguish storage availability from application recovery, because VMs and applications may still need to restart.

See reference 8.

<a id="q27"></a>
### 27. How would you plan vSAN capacity for an enterprise database platform?

I would begin with current data, expected growth, working-set size, and workload performance requirements. Then I would account for policy overhead, snapshots, operational reserves, and space needed for recovery or maintenance.

I would evaluate capacity at both the cluster and host level because uneven utilization can create problems even when aggregate free space appears sufficient.

For a database platform, I would assess throughput and latency alongside capacity. My design would include growth triggers and a tested expansion process so the team can add resources before performance or resilience is affected.

## Virtual Networking

<a id="q28"></a>
### 28. What is the difference between a standard switch and a distributed switch?

| Area | vSphere Standard Switch—vSS | vSphere Distributed Switch—vDS |
|---|---|---|
| Configuration | Managed separately on each host | Centrally managed through vCenter across participating hosts |
| Port groups | Host-local configuration | Distributed port groups provide consistent configuration |
| Operational fit | Straightforward host networking | Centralized enterprise networking |
| LACP | Not supported | Supported with appropriate configuration |

I would choose based on scale, required features, and operational needs. With a distributed switch, I would also plan management-network recovery and maintain configuration backups. LACP requires matching physical-switch configuration; enabling it only on the VMware side can disrupt connectivity.

See references 9–10.

<a id="q29"></a>
### 29. What is the difference between a VMkernel adapter and a VM network adapter?

A VMkernel adapter provides network connectivity for ESXi host services, such as management, vMotion, and vSAN. It has its own IP configuration and is associated with the relevant service.

A VM network adapter belongs to the guest virtual machine and carries the guest’s application traffic through a port group.

That distinction matters during troubleshooting. A successful ping from a VM does not prove that the host’s vSAN or vMotion network works. I test the specific interface and traffic path used by the failing service.

<a id="q30"></a>
### 30. What are VLANs, and how do you use them in VMware?

A VLAN creates a separate Layer 2 broadcast domain. In VMware, I can use VLAN-backed port groups to separate management, storage, migration, and application traffic.

The VLAN configuration must align with the physical network, including the VLANs allowed on the ESXi uplink switch ports. Communication between different VLANs requires Layer 3 routing and must satisfy the relevant firewall rules.

I would document the VLAN-to-port-group mapping and validate it on every participating host. I would also avoid treating VLAN separation alone as a complete security control.

<a id="q31"></a>
### 31. Explain Layer 2 and Layer 3 troubleshooting in a virtual environment.

At Layer 2, I investigate MAC learning, VLAN membership, ARP behavior, uplinks, and switching connectivity. At Layer 3, I investigate IP addressing, subnets, gateways, routing, and routed access controls.

If two VMs on the same subnet cannot communicate, I would start with guest configuration and the Layer 2 path. If communication fails between subnets, I would also examine routing and firewall policies.

I use that distinction to narrow the investigation, while still checking the actual design because overlays and distributed networking can change where those functions occur.

<a id="q32"></a>
### 32. What is NIC teaming, and how is it different from LACP?

NIC teaming allows multiple physical uplinks to support redundancy and traffic distribution for a virtual switch. It does not automatically require link aggregation on the physical switch.

LACP dynamically negotiates a link aggregation group and requires compatible configuration on the distributed switch and physical network.

I would select the teaming policy based on the design and verify failover behavior. I would also explain that multiple uplinks do not necessarily increase the bandwidth of a single flow; traffic distribution depends on the configured policy and hashing behavior.

<a id="q33"></a>
### 33. What is MTU, and how would you troubleshoot a jumbo-frame issue?

MTU defines the maximum IP packet size an interface can transmit without fragmentation. When using jumbo frames, every relevant segment of the path must support the intended packet size.

If small pings work but large packets fail, I would check the VMkernel interface, virtual switch, physical uplinks, and intermediate network devices.

For an IPv4 path intended to support an MTU of 9000, I could use this test from the correct VMkernel adapter:

```bash
vmkping -I vmk2 -d -s 8972 <destination-vmk-ip>
```

Here, `vmk2` is an example and must be replaced with the correct interface. The 8972-byte payload plus IPv4 and ICMP headers tests a 9000-byte IP packet. I would test the affected paths in both directions. If the interface uses a dedicated TCP/IP stack, I would select that stack as appropriate.

See references 11–12.

<a id="q34"></a>
### 34. How would you troubleshoot a failed vMotion?

I would review the migration error and determine whether it indicates networking, compatibility, or resource constraints.

For networking, I would verify the vMotion-enabled VMkernel interfaces, IP configuration, VLANs, uplink selection, routing where applicable, and MTU. I would test connectivity between the actual vMotion interfaces.

I would also examine CPU compatibility, destination capacity, required VM networks, and storage access for the migration type. Once corrected, I would repeat the migration and validate application connectivity.

**Example:** A missing vMotion VLAN on an active physical uplink is one documented cause of migration failure. See reference 13.

<a id="q35"></a>
### 35. A VM communicates with VMs on the same host but fails across hosts. What do you check?

That pattern suggests that local virtual switching works, but the traffic path between hosts may be broken.

I would compare port-group VLAN settings across the hosts, then inspect physical uplinks, allowed VLANs, teaming policies, and physical-switch configuration. If LACP is involved, I would confirm the aggregation state and configuration on both sides.

I would also check packet counters and use targeted captures to see whether traffic leaves the source host and reaches the destination. I would still validate guest firewalls and addressing before declaring the physical network the cause.

<a id="q36"></a>
### 36. How would you troubleshoot a vSAN network partition?

I would check which hosts can communicate and whether the partition followed a network change or failure. I would verify the vSAN VMkernel interface, VLAN, IP configuration, active uplinks, and MTU.

I would use `esxcli vsan network list` to inspect the interfaces assigned to vSAN and `vmkping` to test the relevant host-to-host paths.

After restoring connectivity, I would verify cluster membership, object accessibility, policy compliance, and resynchronization. I would not consider the incident resolved just because the hosts can ping each other.

See reference 14.

<a id="q37"></a>
### 37. What is the difference between an underlay and an overlay network?

The underlay is the physical IP network that connects hosts and network devices. The overlay creates logical networks over that connectivity, typically using encapsulation.

With an overlay platform such as NSX, I would investigate both layers. A logical segment may be configured correctly while physical packet loss, tunnel-endpoint reachability, or insufficient MTU still breaks communication.

My troubleshooting would follow the packet from the guest through the logical network, tunnel endpoints, physical network, and destination. I would also account for encapsulation overhead when validating MTU.

<a id="q38"></a>
### 38. How would you design networking for mixed database, analytics, and AI workloads?

I would identify each traffic type and its bandwidth, latency, availability, and security requirements. That includes application traffic, storage replication, migrations, backups, management, and large data transfers.

I would use appropriate segmentation, redundant physical paths, and resource controls where supported. I would validate that heavy backup or migration activity does not starve storage or application traffic.

Finally, I would test concurrent workloads and uplink failures. The acceptance criteria would include application response time, storage latency, throughput, and recovery behavior under contention.

## Questions to Ask the Interviewer

1. How is the team’s work divided between VMware, KVM, and Harvester?
2. What are the biggest performance or reliability challenges for the current platform?
3. How do you test mixed EDW, analytics, and AI workloads before release?
4. What ownership would this engineer have across architecture, automation, and customer escalations?
5. What would successful performance in the first 90 days look like?

## Technical References

These official sources support the technical points discussed in the guide. Validate release-specific limits and compatibility against the actual environment.

1. [Broadcom: Using ESXTop and Interpreting ESXTop Statistics](https://knowledge.broadcom.com/external/article/382249/using-esxtop-and-interpreting-esxtop-sta.html)
2. [Broadcom: ESXi CPU scheduling and performance counters](https://knowledge.broadcom.com/external/article/387750)
3. [Harvester Overview and Architecture](https://docs.harvesterhci.io/v1.5/)
4. [VMware: Comparing OSA to vSAN 8 ESA](https://blogs.vmware.com/cloud-foundation/2022/08/31/comparing-the-original-storage-architecture-to-the-vsan-8-express-storage-architecture/)
5. [VMware: Storage Device Failure in ESA versus OSA](https://blogs.vmware.com/cloud-foundation/2023/08/02/the-impact-of-a-storage-device-failure-in-vsan-esa-versus-osa/)
6. [Broadcom: Data Migration Pre-check and Non-compliant Objects](https://knowledge.broadcom.com/external/article/405096)
7. [Broadcom: Virtual Machines Inaccessible During Maintenance](https://knowledge.broadcom.com/external/article/410997/virtual-machine-become-inaccessible-duri.html)
8. [VMware: vSAN Stretched Cluster Guide](https://www.vmware.com/docs/vsan-stretched-cluster-guide)
9. [Broadcom: NIC Teaming and Link Aggregation Considerations](https://knowledge.broadcom.com/external/article?legacyId=1001938)
10. [Broadcom: Virtual Machine Network Connection Issues](https://knowledge.broadcom.com/external/article/419771/virtual-machine-network-connection-issue.html)
11. [Broadcom: Troubleshooting vSAN Networking](https://knowledge.broadcom.com/external/article/326954/troubleshooting-vsan-networking.html)
12. [Broadcom: Testing Jumbo-frame Pings from ESXi](https://knowledge.broadcom.com/external/article?articleNumber=313061)
13. [Broadcom: Unable to vMotion Virtual Machines Between Hosts](https://knowledge.broadcom.com/external/article/415366/unable-to-vmotion-virtual-machines-betwe.html)
14. [Broadcom: vSAN Network Partition and VMkernel Connectivity](https://knowledge.broadcom.com/external/article/391883)

