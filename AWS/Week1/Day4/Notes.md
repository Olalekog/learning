
AWS Global Infrastructure – Features and Characteristics 

What is AWS Global Infrastructure?
AWS Global Infrastructure is the worldwide network of AWS data centers and networking components that deliver AWS cloud services with high availability, low latency, scalability, and resilience.
It consists of:
	• AWS Regions 
	• Availability Zones 
	• Edge Locations 
	• Regional Edge Caches 
	• The AWS Global Network 

Key Components
1. AWS Regions
A Region is a separate geographic area where AWS hosts multiple Availability Zones.
Characteristics
	• Physically isolated from other Regions 
	• Supports data residency and sovereignty requirements 
	• Each Region has independent power, cooling, and networking 
	• Enables disaster recovery across Regions 
Examples
	• US East (N. Virginia) 
	• US East (Ohio) 
	• Europe (Ireland) 
	• Asia Pacific (Singapore) 
Best for
	• Disaster Recovery 
	• Regulatory compliance 
	• Latency optimization 

2. Availability Zones (AZs)
An Availability Zone is one or more physically separate data centers within a Region.
Characteristics
	• Independent power 
	• Independent cooling 
	• Independent networking 
	• Connected with low-latency, high-bandwidth fiber links 
Typical Regions have three or more AZs.
Best Practice
Deploy applications across at least two AZs for high availability.

3. Edge Locations
Edge Locations are global sites that cache content closer to end users.
Used by:
	• Amazon CloudFront 
	• Amazon Route 53 
	• AWS Shield 
	• AWS Web Application Firewall 
Benefits
	• Lower latency 
	• Faster content delivery 
	• DDoS protection 
	• Global DNS resolution 

4. Regional Edge Caches
These sit between Regions and Edge Locations.
Benefits
	• Larger cache capacity 
	• Reduced requests to the origin server 
	• Improved performance for dynamic content 

5. AWS Global Network
AWS operates one of the world's largest private fiber-optic networks.
Characteristics
	• High bandwidth 
	• Low latency 
	• Redundant connectivity 
	• Secure backbone 
	• Connects Regions, AZs, and Edge Locations 
Unlike public internet traffic, data moving between AWS Regions can stay on AWS's private backbone.

Key Features
High Availability
Applications can be deployed across multiple AZs.
Example:
	• ALB in 2 AZs 
	• EC2 Auto Scaling 
	• Multi-AZ database 
If one AZ fails, the application continues running in the others.

Fault Tolerance
Supports failures at multiple levels:
	• Server 
	• Rack 
	• Data center (AZ) 
	• Region (with multi-region design) 

Low Latency
Choose Regions close to your users and use Edge Locations for content delivery.

Scalability
Resources can scale automatically using services such as:
	• Amazon EC2 Auto Scaling 
	• AWS Lambda 
	• Amazon Elastic Kubernetes Service 

Disaster Recovery
Supports:
	• Backup & Restore 
	• Pilot Light 
	• Warm Standby 
	• Multi-site Active/Active 
Applications can replicate data between Regions for resilience.

Security
Infrastructure is protected by:
	• Physical security 
	• Network isolation 
	• Encryption 
	• Identity management 
	• Compliance certifications 

Global Load Balancing
Traffic can be routed worldwide using:
	• Amazon Route 53 
	• AWS Global Accelerator 

Characteristics Summary
Characteristic	Description
Global Presence	Multiple Regions around the world
Multiple AZs	Each Region contains multiple isolated Availability Zones
Fault Isolation	Failure in one AZ generally does not affect others
High-Speed Network	Private AWS backbone connects infrastructure
Scalability	Supports elastic cloud resources
Low Latency	Edge Locations reduce response times
High Availability	Multi-AZ deployment patterns
Disaster Recovery	Multi-Region replication and failover
Security	Physical and logical security controls
Compliance	Supports global regulatory requirements

Typical Enterprise Architecture

                  Internet Users
                        │
                        ▼
             Amazon CloudFront (Edge Locations)
                        │
                        ▼
          AWS Global Network (Private Backbone)
                        │
      ┌─────────────────┴─────────────────┐
      │                                   │
 Region A                           Region B (DR)
 US-East-1                         US-West-2
      │                                   │
 ┌────┴────┐                       ┌──────┴─────┐
 │ AZ-1    │                       │ AZ-1       │
 │ EC2/ALB │                       │ Standby    │
 └────┬────┘                       └──────┬─────┘
      │                                   │
 ┌────┴────┐                       ┌──────┴─────┐
 │ AZ-2    │                       │ AZ-2       │
 │ EC2/RDS │                       │ Replicas   │
 └─────────┘                       └────────────┘

Interview Questions and Sample Answers
Q1: What is the difference between a Region and an Availability Zone?
Answer:
A Region is a geographically isolated location containing multiple Availability Zones. An Availability Zone consists of one or more physically separate data centers within a Region, each with independent power, cooling, and networking. Regions support geographic isolation and disaster recovery, while AZs provide high availability within a Region.

Q2: Why deploy applications across multiple AZs?
Answer:
Deploying across multiple AZs improves high availability and fault tolerance. If one AZ experiences a failure, traffic can be routed to healthy resources in another AZ with minimal disruption.

Q3: What is the purpose of Edge Locations?
Answer:
Edge Locations cache content closer to users, reducing latency and improving application performance. They are also used by services such as CloudFront, Route 53, AWS WAF, and AWS Shield to deliver content, resolve DNS queries, and protect applications from attacks.

Solution Architect Tip

For the AWS Solutions Architect Associate or Professional exams, remember these design principles:
	• Use multiple AZs for high availability. 
	• Use multiple Regions for disaster recovery or global applications. 
	• Use CloudFront and Edge Locations to reduce latency for global users. 
	• Use Route 53 or Global Accelerator to route users to the healthiest and closest application endpoints. 
	• Keep data close to users while meeting compliance and data residency requirements.
<img width="1110" height="6861" alt="image" src="https://github.com/user-attachments/assets/dd1bc27a-f57d-4ed5-a287-ab6af40e212f" />
