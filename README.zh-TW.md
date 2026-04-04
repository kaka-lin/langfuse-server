# Langfuse Server (Self-Hosted V3)

[English](README.md) | [繁體中文](README.zh-TW.md)

一套針對 macOS 與 Linux 環境進行深度優化的 [Langfuse](https://langfuse.com) AI 觀測平台私有化部署方案。本專案透過 Docker 生態系統，提供最穩定且高效能的 Open-Source AI 客觀性監測環境。

## 🚀 快速啟動

在完成 [環境變數配置](./docs/zh-TW/deployment/setup.md) 後，您可以使用以下指令管理伺服器：

```bash
# 啟動全服務 (含自動配置檢查)
./start.sh

# 停止全服務
./stop.sh
```

- **Langfuse Portal**: [http://localhost:3000](http://localhost:3000)

- **MinIO Console**: [http://localhost:9091](http://localhost:9091)

## 📚 文件導覽 (Documentation)

我們將佈署細節與通用知識進行了分層管理，請根據您的需求參閱：

- [**安裝指南 (Installation Guide)**](./docs/zh-TW/deployment/setup.md)：具體的快速啟動步驟與常用指令。

- [**技術全解析 (Setup Deep Dive)**](./docs/zh-TW/deployment/setup-deep-dive.md)：解析本專案在效能與安全上的技術決策。

- [**個人知識庫 (LLM-notes)**](../../LLM-notes/Langfuse/README.md)：Langfuse 核心概念、架構原理與 S3/OLAP 知識筆記。
