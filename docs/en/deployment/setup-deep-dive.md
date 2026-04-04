# Deployment Deep Dive

[English](setup-deep-dive.md) | [繁體中文](../../zh-TW/deployment/setup-deep-dive.md)

The `start.sh` script and `docker-compose.yml` configuration provided in this project incorporate architectural optimizations addressing typical issues encountered with Langfuse V3 in a local environment.

## 1. Performance Optimization: Named Volumes vs. Bind Mounts

### Background: Docker Disk I/O Performance

When using Bind Mounts like `./data` with Docker Desktop on macOS, the sync overhead of gRPC FUSE or VirtioFS results in extremely low database write performance. This is particularly noticeable during PostgreSQL's WAL (Write-Ahead Logging) writes and ClickHouse's disk space allocation.

### Solution: Adopting Named Volumes

This project exclusively uses **Docker Named Volumes**:

```yaml
volumes:
  langfuse_postgres_data:
    driver: local
```

This ensures database files are managed natively by the Docker engine, bypassing host file system sync overhead and increasing write speeds by several orders of magnitude.

## 2. ClickHouse Standalone Mode: Disabling ZooKeeper dependency

### Background: Cluster Migration Errors

Langfuse V3's official migration scripts default to "cluster mode" syntax (e.g., `ON CLUSTER`). This forces ClickHouse to look for a ZooKeeper or Keeper coordinator. Attempting this in a standalone environment results in `There is no Zookeeper configuration` migration errors.

### Solution: Implicit Environment Intervention

We inject the following environment variable into the container:

```bash
CLICKHOUSE_CLUSTER_ENABLED=false
```

This setting instructs Langfuse to modify its generated SQL commands to use single-node table engines (e.g., `MergeTree` instead of `ReplicatedMergeTree`), making the entire architecture extremely lightweight for standalone environments.

## 3. Authentication and Security: Password length checks

### Background: Password Validation Failure

Langfuse V3 includes strict development security checks (via Zod validation). We discovered that if the database or initialization user's password is less than 8 characters, the service fails during the "Instrumentation Hook" startup phase.

### Solution: Enforcing 8-Character Passwords and Volume Reset

We have marked the minimum length requirements in `.env.example`:

- **Passwords**: Must be >= 8 characters.

- **MinIO Access Key**: Must be >= 3 characters.

> [!CAUTION]
> **Database Initialization Pitfall**: PostgreSQL only initializes the password on **Initial Volume Creation**. If you previously started with a 6-character password and then updated `.env` to 8 characters, authentication will fail. You must run `docker compose down -v` to clear the disk before restarting.

## 4. Infrastructure: Minio (S3)

### Background: V3 Mandatory S3 Requirement

Langfuse V3 enforces S3 configuration checks upon startup. This was optional in V2 but has become essential in V3 for storing large Trace attachments.

### Solution: Built-in Minio Container

We have integrated a lightweight **Minio** container as a local S3 alternative, configured to automatically create the required bucket (`langfuse`) on startup.

## 5. Further Reading

For users who want to dive deeper into the distributed architecture of Langfuse or the principles of data collection, please refer to your personal knowledge base:

- [**Langfuse AI Observability Principle Notes (LLM-notes)**](../../../../LLM-notes/Langfuse/README.md)

- [**V3 Architecture: Data & Storage Technical Deep Dive (LLM-notes)**](../../../../LLM-notes/Langfuse/architecture-deep-dive.md)
