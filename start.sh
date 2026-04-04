#!/bin/bash

echo "🚀 準備啟動 Langfuse Server..."

# 檢查 .env 檔案是否存在
if [ ! -f .env ]; then
    echo "⚠️ 找不到 .env 檔案！"
    if [ -f .env.example ]; then
        echo "👉 正在為您自動從 .env.example Copy 一份建立 .env 檔案..."
        cp .env.example .env
        echo "✅ 建立完成！(※ 重要：若是正式上線環境，請務必先修改 .env 內的密碼與金鑰)"
        echo "-----------------------------------"
    else
        echo "❌ 警告：沒有找到 .env 與 .env.example，啟動可能會因為缺少環境變數而失敗。"
    fi
fi

# 確保抓取到最新的 docker image (選項)
echo "📦 檢查更新..."
docker compose pull

# 背景啟動所有服務
echo "⏳ 正在啟動所有服務..."
docker compose up -d

echo "-----------------------------------"
echo "✅ 啟動成功！"
echo "👉 服務需要大約 10~20 秒進行資料庫初始化。"
echo "🌐 稍後您可以從瀏覽器打開：http://localhost:3000"
echo "📝 若想查看日誌，請輸入指令：docker compose logs -f"
