# Langfuse Server 安裝指南 (Installation Guide)

[English](../../en/deployment/setup.md) | [繁體中文](setup.md)

本文件介紹了在本機環境部署 Langfuse V3 的步驟。

## 1. 本專案快速部署 (Using start.sh)

這是針對本專案架構優化過的安裝方式，整合了 Named Volumes 效能優化與單機版 ClickHouse 配置。

> [!NOTE]
> 關於本部署方式的技術細節與原理解析，請參閱：[Langfuse 部署技術全解析 (Setup Deep Dive)](setup-deep-dive.md)

### 部署步驟

1. **Clone 專案 Repository**

   首先，請將本專案 Clone 到您的本機環境：

   ```bash
   git clone https://github.com/kaka-lin/langfuse-server.git
   cd langfuse-server
   ```

2. **配置環境變數**

   根據 `.env.example` 建立實體設定檔。本專案已預設配置為單機運作模式。

   ```bash
   cp .env.example .env
   ```

3. **執行啟動腳本**

   本專案提供自動化檢查腳本：

   ```bash
   chmod +x start.sh stop.sh
   ./start.sh
   ```

4. **造訪介面**

   - Langfuse Web: [http://localhost:3000](http://localhost:3000)

   - Minio Console: [http://localhost:9091](http://localhost:9091)

## 2. 官方標準安裝方式 (Official Methods)

如果您偏好使用 Langfuse 官方提供的標準途徑（未包含本專案的 Mac 效能優化）：

### 2.1 Clone 官方專案 Repository (Clone Official Repo)

這是官方最推薦的方式，可以獲取完整的開發環境與最新版本的 Compose 配置。

```bash
git clone https://github.com/langfuse/langfuse.git
cd langfuse
docker compose up -d
```

### 2.2 快速啟動：僅下載 Compose 檔案 (Download Standalone Compose)

適用於只想快速測試，不打算保留官方原始碼的使用者。

```bash
# 下載官方 docker-compose.yml 範本
curl -o docker-compose.yml https://raw.githubusercontent.com/langfuse/langfuse/main/docker-compose.yml

# 下載官方環境變數範本
curl -o .env http://raw.githubusercontent.com/langfuse/langfuse/main/.env.example

# 依照需求編輯 .env 後啟動
docker compose up -d
```

> [!WARNING]
> 以上官方方式使用的是標準 Bind Mounts。在 Mac 上可能會遇到 ClickHouse 遷移報錯與嚴重的寫入效能問題。建議本地開發優先使用本專案的 `start.sh`。

## 3. 後續步驟 (Next Steps)

完成基礎部署後，您可以開始整合您的 AI 應用：

- **API 金鑰設定**：登入後在專案設定中取得 API Keys。

- **整合 SDK**：參考官方文件將 Python/JS SDK 接入您的程式碼。
