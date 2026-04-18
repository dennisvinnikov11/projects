# CySA+ Chapter 2 Study Notes
March 13, 2026
## System and  Network Architecture
### Serverless Computing
The term describes cloud computing technology called function as a service (FaaS). Users can write and deploy code without having to worry about infrastructure. This is benificial due to reduced cost, because the user is charged only based on computation, and doesn't have to pay for maintenance and upgrades of the servers provided. 
### Virtualization
Virtualization technology allows creation of virtual, simulated environments within one physical host. This means one physical system, can run multiple systems that act as if they're operating on their own hardware. This provides a better control over available resources, to share them accross multiple systems.
It's also used to implement Virtual Desktop Infrastructure (VDI), which runs operating systems on central hardware and streams the desktops accross the network to individual systems. 
### Containerization
It's concept of packaging software code with everything that it needs into one lightweight executable(container) that runs consistently on any kind of infrastructure.
Containers share the host machine's operating system kernel, but have their own file system, process ID space, network stack, and hostname using namespaces. This can be described as an application-level virtualization.






## Sources
* CompTIA CySA+ Study Guide. Mike Chapple, David Seidl 
* https://www.cloudflare.com/learning/serverless/what-is-serverless/
* https://www.ibm.com/think/topics/virtualization
* https://www.ibm.com/think/topics/containerization
* https://ericchiang.github.io/post/containers-from-scratch/
