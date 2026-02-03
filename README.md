# Deployment of Microservices Application on Amazon EKS

## Overview
This project demonstrates the deployment of a simple microservices-based application on **Amazon Elastic Kubernetes Service (EKS)** using **Docker**, **AWS ECR**, and **Kubernetes manifests**.

The application consists of two microservices:
- **service-a**: Public-facing API exposed via an AWS LoadBalancer
- **service-b**: Internal service accessible only within the Kubernetes cluster

The project showcases real-world DevOps practices including containerization, cluster provisioning, internal service communication, and public service exposure.


## Architecture
- Amazon EKS (managed Kubernetes)
- Managed Node Group (EC2)
- Amazon ECR for container images
- Kubernetes Deployments and Services
- Internal communication via ClusterIP
- External access via AWS LoadBalancer

See `docs/architecture.md` for details.


## Microservices
### service-a (Public)
- FastAPI application
- Exposed via LoadBalancer
- Communicates with service-b using internal DNS

### service-b (Internal)
- FastAPI application
- Exposed internally via ClusterIP
- Not accessible from the internet


## Deployment Steps (High Level)
1. Containerized both services using Docker
2. Pushed images to Amazon ECR
3. Created an EKS cluster using `eksctl`
4. Deployed service-b as an internal service
5. Deployed service-a and exposed it publicly
6. Verified end-to-end communication


## End-to-End Test
Accessing the following endpoint confirms successful communication:

## GET /call-service-b

Response
{"from":"Service-a","service-b-response":{"Service":"B","message":"Hello from service B"}}



## Screenshots

Screenshots of key steps are available in the docs/screenshots directory:

EKS cluster creation

Node readiness

Service deployments

Public LoadBalancer access

End-to-end working response



## Key Learnings

How to provision and access an EKS cluster

Difference between ClusterIP and LoadBalancer services

Service-to-service communication using Kubernetes DNS

Debugging image pull and pod startup issues

Importance of correct image tagging in ECR


## Author

Built by Onyedika Okoro
Cloud / DevOps Engineer