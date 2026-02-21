## Architecture Overview

This project demonstrates a containerized microservices application deployed on Amazon EKS, focusing on internal service-to-service communication, Kubernetes networking fundamentals, and operational correctness.

The architecture intentionally emphasizes ClusterIP services and internal routing, with local access enabled via kubectl port-forward for development and validation.



## High-Level Architecture

```
Local Client (Browser / curl)
  ↓
kubectl port-forward
  ↓
Service A (ClusterIP)
  ↓
Service B (ClusterIP)
  ↓
Pods (Dockerized Applications)
```


## Components Breakdown

## Amazon EKS Cluster

Managed Kubernetes control plane provided by AWS

Worker nodes run containerized workloads

Core Kubernetes components (kube-proxy, CoreDNS, metrics server) are running and healthy

## Microservices

## Service A

Exposed internally via ClusterIP

Acts as the entry point within the cluster

Forwards requests to Service B

Runs inside Kubernetes pods using a Docker container


## Service B

Exposed internally via ClusterIP

Receives requests only from Service A

Not exposed directly to the client

Runs inside Kubernetes pods using a Docker container


## Kubernetes Networking

ClusterIP Services are used for internal communication

Kubernetes DNS enables service discovery (service-b.default.svc.cluster.local)

No external load balancer is required for internal traffic

Traffic flow is fully handled inside the cluster


## Local Access Strategy (Development & Verification)

For local testing and validation, port forwarding is used instead of an external ingress:

kubectl port-forward svc/service-a 8080:80


This allows access from a local browser:

http://localhost:8080


This approach:

Keeps services private

Avoids unnecessary cloud load balancer costs

Mirrors real-world internal microservice communication patterns


## Design Decisions

Why No Ingress / ALB?

This project focuses on core Kubernetes networking concepts

Internal service communication is the primary goal

External ingress is intentionally treated as a future enhancement

This mirrors real production environments where services are often private and accessed through internal gateways


## Production Readiness Notes

This architecture is production-aligned for:

Internal microservice communication

Platform engineering and DevOps roles

Kubernetes networking fundamentals

Cost-conscious infrastructure design


## Potential future improvements (out of scope for this implementation):

Ingress controller (ALB / NGINX)

External DNS

TLS termination

Observability (Prometheus / Grafana)

CI/CD automation


## Key Takeaways

Kubernetes Services abstract pod lifecycles

ClusterIP is sufficient for secure internal communication

Not all production systems expose services publicly

Understanding when not to use a load balancer is a valuable DevOps skill

