# E-Commerce MVP on Kubernetes with KinD

This repository contains a microservice-based e-commerce Minimum Viable Product (MVP) deployed on a local Kubernetes cluster using KinD (Kubernetes IN Docker).

## Features

- View products (frontend + backend)
- Place an order (API + DB write)
- See order confirmation (backend logs)
- Uses PostgreSQL as database with Persistent Volume Claim (PVC)
- Uses Kubernetes Deployments, Services, Ingress, Secrets, and ConfigMaps
- Includes health checks (readiness & liveness probes)

---

## Prerequisites

Make sure you have the following installed on your machine:

- [Docker Desktop](https://docs.docker.com/desktop/install/)
- [KinD](https://kind.sigs.k8s.io/docs/user/quick-start/) (Kubernetes in Docker)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

---

## Setup Instructions

### 1. Create the KinD cluster

```bash
kind create cluster
