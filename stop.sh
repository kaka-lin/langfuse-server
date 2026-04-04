#!/bin/bash

echo "🛑 準備停止 Langfuse 服務..."

# 停止並移除容器
docker compose down

echo "-----------------------------------"
echo "✅ 服務已完全停止！(您的資料因使用 Named Volume 不會遺失)"
