# Langfuse Server Installation Guide

[English](setup.md) | [繁體中文](../../zh-TW/deployment/setup.md)

This document provides a step-by-step guide for deploying Langfuse V3 in a local environment.

## 1. Quick Deployment (Using start.sh)

This method is optimized for the current project architecture, incorporating Named Volumes for disk performance and a standalone ClickHouse configuration.

> [!NOTE]
> For a deep dive into the technical details and decisions behind this setup, see: [Deployment Deep Dive](setup-deep-dive.md)

### Deployment Steps

1. **Clone Project Repository**

   First, clone this repository to your local environment:

   ```bash
   git clone https://github.com/kaka-lin/langfuse-server.git
   cd langfuse-server
   ```

2. **Configure Environment Variables**

   Create a concrete environment file from the provided template. This project is preconfigured for standalone mode.

   ```bash
   cp .env.example .env
   ```

3. **Run the Startup Script**

   Execute the automated script which performs environment checks and starts all services:

   ```bash
   chmod +x start.sh stop.sh
   ./start.sh
   ```

4. **Access the Interfaces**

   - Langfuse Web: [http://localhost:3000](http://localhost:3000)

   - MinIO Console: [http://localhost:9091](http://localhost:9091)

## 2. Official Deployment Methods (Official Methods)

If you prefer using the standard Langfuse official distribution (without the macOS performance optimizations included in this project):

### 2.1 Clone Official Repository (Clone Official Repo)

The recommended official way, providing the full development environment and the latest compose configurations.

```bash
git clone https://github.com/langfuse/langfuse.git
cd langfuse
docker compose up -d
```

### 2.2 Quick Start: Download Standalone Compose File

Suitable for users who want to test quickly without keeping the official source code.

```bash
# Download the official docker-compose.yml template
curl -o docker-compose.yml https://raw.githubusercontent.com/langfuse/langfuse/main/docker-compose.yml

# Download the official environment template
curl -o .env http://raw.githubusercontent.com/langfuse/langfuse/main/.env.example

# Edit .env as needed and launch
docker compose up -d
```

> [!WARNING]
> Official methods rely on standard Bind Mounts, which may lead to ClickHouse migration errors and severe performance issues on macOS. For local development, using the project's `start.sh` is strongly recommended.

## 3. Next Steps

After completion, you can begin integrating your AI applications:

- **API Key Configuration**: Access API Keys from the project settings after logging in.

- **SDK Integration**: Refer to the official documentation to integrate Python/JS SDKs into your code code.
