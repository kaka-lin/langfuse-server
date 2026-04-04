# Langfuse Server (Self-Hosted V3)

[English](README.md) | [繁體中文](README.zh-TW.md)

A self-hosted deployment of the [Langfuse](https://langfuse.com) AI observability platform, specifically optimized for macOS and Linux environments. This project provides a robust, high-performance open-source environment for AI observability and evaluation via Docker.

## 🌟 Key Features

- **Platform Optimized**: Specially tuned for macOS and Linux disk I/O (Named Volumes) and network binding security.

- **Quick Deployment**: Built-in automation scripts for environment checks and one-click startup.

- **Infrastructure Ready**: Fully integrated with PostgreSQL, Clickhouse, MinIO (S3), and Redis, supporting the latest Langfuse V3 architecture.

## 🚀 Quick Start

After completing the [Environment Configuration](./docs/en/deployment/setup.md), you can manage the server using the following commands:

```bash
# Start all services (includes auto-config check)
./start.sh

# Stop all services
./stop.sh
```

- **Langfuse Portal**: [http://localhost:3000](http://localhost:3000)

- **MinIO Console**: [http://localhost:9091](http://localhost:9091)

## 📚 Documentation Navigation

Deployment details and general knowledge are partitioned for better maintainability:

- [**Installation Guide**](./docs/en/deployment/setup.md): Specific step-by-step setup and common maintenance commands.

- [**Setup Deep Dive**](./docs/en/deployment/setup-deep-dive.md): Technical analysis of performance and security decisions in this project.

- [**Knowledge Base (LLM-notes)**](../../LLM-notes/Langfuse/README.md): Langfuse core concepts, architecture deep dives, and S3/OLAP technical notes.