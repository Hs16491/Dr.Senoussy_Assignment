# Cloud and Mobile Computing — Labs

This repository contains the completed lab submissions for the Cloud and Mobile Computing course.

---

## Labs

| Lab | Topic | Link |
|-----|-------|------|
| Lab 01 | Cloud Virtualization and Data Center Architecture | [View Lab](lab1/) |
| Lab 02 | Distributed Consistency and Consensus | [View Lab](lab2/) |
| Lab 03 | Containerization and Cluster Orchestration | [View Lab](lab3/) |
| Lab 04 | Microservices and Cloud-Native Design | [View Lab](lab4/) |

---

## Overview

### Lab 01 — Cloud Virtualization and Data Center Architecture
Explores the difference between Virtual Machines and containers in practice. Covers deploying instances on local and cloud environments (AWS EC2, GCP, Azure), analyzing tail latency patterns, and measuring virtualization overhead using Docker and VirtualBox/QEMU.

### Lab 02 — Distributed Consistency and Consensus
Simulates how distributed systems handle consistency and availability using Redis replication and the Raft consensus protocol via etcd. Includes network partition experiments and leader election observation using Docker Compose.

### Lab 03 — Containerization and Cluster Orchestration
Hands-on work with Linux namespaces, cgroups, and Docker image layering. Involves setting up a local Kubernetes cluster using `kind`, deploying multi-replica applications, configuring health probes, and testing the platform's self-healing behavior.

### Lab 04 — Microservices and Cloud-Native Design
Builds a small cloud-native e-commerce backend from scratch using two Python Flask microservices (`product-service` and `order-service`) orchestrated with Docker Compose. Covers 12-factor app principles, service-to-service communication, health checks, and monolith vs. microservices trade-offs.

---

> **Course:** Cloud and Mobile Computing  
> **Tools used:** Docker, Kubernetes (kind), Redis, etcd, Python Flask, AWS EC2
