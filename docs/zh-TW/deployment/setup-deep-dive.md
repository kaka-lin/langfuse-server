# Langfuse 部署技術全解析 (Setup Deep Dive)

[English](../../en/deployment/setup-deep-dive.md) | [繁體中文](setup-deep-dive.md)

我們專案提供的 `start.sh` 腳本與 `docker-compose.yml` 配置，針對 Langfuse V3 在本機環境遇到的典型問題進行了架構優化。

## 1. 效能優化：Named Volumes vs. Bind Mounts

### 問題背景：Docker 磁碟連通效能

Docker Desktop 在 macOS 下使用 `./data` 這種 Bind Mount 方式時，因為受限於 gRPC FUSE 或 VirtioFS 的同步開銷，資料庫的寫入效能極低。這在 PostgreSQL 的 WAL（寫入前日誌）寫入與 ClickHouse 的磁碟分配時尤為明顯。

### 解決方案：採用 Named Volumes

本專案全面改用 **Docker Named Volumes**：

```yaml
volumes:
  langfuse_postgres_data:
    driver: local
```

這保證了資料庫檔案由 Docker 引擎原生管理，繞過了主機檔案系統的同步開銷，寫入速度提升數倍。

## 2. ClickHouse 單機模式：關閉 Zookeeper 依賴

### 問題背景：叢集遷移報錯

Langfuse V3 的官方遷移腳本預設採用「叢集模式」語法（如 `ON CLUSTER`）。這會強迫 ClickHouse 尋找 Zookeeper 或 Keeper 協調器。若在單機環境下強行執行，將導致 `There is no Zookeeper configuration` 的遷移錯誤。

### 解決方案：環境變數強行干預

我們在容器中注入了以下環境變數：

```bash
CLICKHOUSE_CLUSTER_ENABLED=false
```

這項設定指示 Langfuse 修改其生成的 SQL 指令，改用單點資料表引擎（如 `MergeTree` 代替 `ReplicatedMergeTree`），從而使整個架構在單機環境下極致輕量。

## 3. 認證與安全：密碼強度檢查

### 問題背景：密碼強度驗證失敗

Langfuse V3 內置了嚴格的開發安全檢查（透過 Zod 驗證）。我們在部署中發現，如果資料庫或初始化使用者的密碼低於 8 個字元，整個服務將在「啟動階段的 Instrumentation Hook」發生錯誤。

### 解決方案：強制 8 位數密碼與重置 Volume

我們在 `.env.example` 中標註了最低長度限制：

- **密碼 (Passwords)**：務必 >= 8 位。

- **Minio 帳號 (Access Key)**：務必 >= 3 位。

> [!CAUTION]
> **資料庫初始化陷阱**：PostgreSQL 只會在 **Volume 首次建立** 時初始化密碼。如果您先用 6 位的舊密碼啟動過，再修改 `.env` 變為 8 位，將發生認證失敗。此時必須執行 `docker compose down -v` 清空磁碟後重啟。

## 4. 基礎設施依賴：Minio (S3)

### 問題背景：V3 強制要求 S3 儲存

Langfuse V3 啟動時會強制檢查 S3 設定。這在 V2 是選配件，但在 V3 已成為儲存大型 Traces 附件的基礎設施。

### 解決方案：內建 Minio 容器

我們整合了輕量級的 **Minio** 作為本地端的 S3 替代方案，並配置了開機自動建立專屬 Bucket (`langfuse`) 的指令。

## 5. 更多延伸閱讀

對於想要深入了解 Langfuse 分散式架構或數據收集原理的使用者，請參閱您的個人知識庫：

- [**Langfuse AI 觀測平台原理筆記 (LLM-notes)**](https://github.com/kaka-lin/LLM-notes/blob/main/Langfuse/README.md)

- [**V3 架構數據與儲存技術深潛 (LLM-notes)**](https://github.com/kaka-lin/LLM-notes/blob/main/Langfuse/architecture-deep-dive.md)
