## Microservices on Amazon EKS (Kubernetes)

## Overview

This project demonstrates a containerized microservices architecture deployed on Amazon EKS, focusing on Kubernetes fundamentals, internal service-to-service communication, and operational correctness.

Rather than exposing services publicly by default, the system is designed around private ClusterIP services, with controlled local access using kubectl port-forward for development and validation.

This mirrors real-world production patterns where services communicate internally and external exposure is introduced deliberately.


## Architecture Summary

```
Local Client (Browser / curl)
        ↓
kubectl port-forward
        ↓
Service A (ClusterIP)
        ↓
Service B (ClusterIP)
        ↓
Pods (Docker Containers)
```


📄 A detailed architecture breakdown is available in docs/architecture.md

## Key Components

## Amazon EKS

- Managed Kubernetes control plane

- Worker nodes running containerized workloads

- Core system components (CoreDNS, kube-proxy, metrics server) are healthy and running


## Service A

- Kubernetes Deployment + ClusterIP Service

- Acts as the internal entry point

- Forwards requests to Service B

- Containerized using Docker


## Service B

- Kubernetes Deployment + ClusterIP Service

- Receives traffic only from Service A

- Not directly exposed

- Containerized using Docker


## Kubernetes Networking Design

- ClusterIP Services are used for internal communication

- Kubernetes DNS enables service discovery between services

- No external load balancer is required for internal traffic

- Traffic remains fully inside the cluster

This design emphasizes security, simplicity, and cost awareness.


## Verification & Testing

Check Cluster Resources

```
kubectl get pods
```

```
kubectl get svc
```

Local Access via Port Forwarding
kubectl port-forward svc/service-a 8080:80

Access in Browser
http://localhost:8080


Expected response:

{
  "service": "A",
  "message": "Hello from Service A"
}


- This confirms:

1. Pods are running

2. Services are correctly configured

3. Internal service-to-service communication is working


## Why No Ingress / Load Balancer?

This project intentionally focuses on core Kubernetes networking concepts rather than public exposure.


## Key reasons:

1. Internal microservice communication is the primary goal

2. Avoids unnecessary cloud cost during development

3. Reflects real production environments where services are private

4. External ingress is a future enhancement, not a requirement for correctness


##  Project Structure

```
microservices-eks/
├── docs/
│   ├── architecture.md
│   └── screenshots/
├── k8s/
│   ├── service-a-deployment.yaml
│   ├── service-a-service.yaml
│   ├── service-b-deployment.yaml
│   └── service-b-service.yaml
├── services/
│   ├── service-a/
│   │   ├── Dockerfile
│   │   └── app code
│   ├── service-b/
│   │   ├── Dockerfile
│   │   └── app code
└── README.md
```



## Production Alignment

This project demonstrates:

- Kubernetes deployments and services

- Internal service discovery

- Containerized microservices

- Cloud-managed Kubernetes (EKS)

- Cost-conscious infrastructure design

- Clear separation between internal and external access


## Potential Future Enhancements

- Ingress controller (ALB or NGINX)

- TLS termination

- External DNS

- Observability (Prometheus / Grafana)

- CI/CD pipelines


## Key Learnings

1. ClusterIP services are sufficient for secure internal communication

2. Kubernetes DNS enables seamless service discovery

3. Not every production system needs public exposure

4. Understanding when not to use a load balancer is an important DevOps skill


## Conclusion

This project demonstrates a solid, production-aligned Kubernetes microservices setup with an emphasis on correctness, security, and clarity.

It reflects real-world engineering decisions rather than unnecessary complexity.


I am Onyedika Okoro

Cloud/DevOps Engineer