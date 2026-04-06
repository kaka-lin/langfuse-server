# Langfuse Backend Abstraction 測試指南

本目錄包含了針對 Langfuse 伺服器的整合測試。我們採用了「後端抽象架構 (Backend Abstraction)」，這使得測試邏輯與具體的 LLM 模型實作分離。

## 1. 測試架構說明

為了對應現代業界的中大型專案配置，我們將代碼劃分為兩個核心部分：

- **`backends/`**：封裝了不同的 LLM 調用邏輯（如 Gemini、Mock）。它們繼承自一個抽象基底，並自動掛載了 Langfuse 的 `@observe()` 追蹤。
- **`tests/`**：包含實際的測試案例，透過參數化功能同時驗證所有後端。

## 2. 快速開始 (Quick Start)

我們使用 `pytest` 作為測試框架。請確保你已經安裝了依賴：

```bash
pip install -r requirements.txt
```

### 2.1 執行所有測試

這會掃描 `tests/` 目錄下所有以 `test_` 開頭的檔案：

```bash
pytest tests/
```

### 2.2 顯示詳細輸出 (-s, -v)

如果你想看見測試過程中的 `print` 輸出（例如模型回傳的內容）與詳細進度：

```bash
pytest tests/test_tracing.py -s -v
```

## 3. 進階用法

### 3.1 跳過缺少金鑰的測試

如果你目前沒有設定 `GEMINI_API_KEY`，測試腳本會自動「Skip」Gemini 的部分，優先確保 `MockBackend` 測試通過，這不會影響最終的測試成功判定。

### 3.2 共用配置 (Fixtures)

我們在 `tests/conftest.py` 中定義了共用的 Fixtures：

- `langfuse_client`：自動初始化 Langfuse 並處理 `.env`。
- `mock_backend` / `gemini_backend`：自動實例化對應的後端物件。

## 4. 如何新增測試後端？

如果你想新增一個後端（例如 OpenAI）：

1. 在 `backends/` 下建立新檔案（如 `openai.py`）。
2. 繼承 `GenericModelBackend` 並實作 `generate()` 方法。
3. 在 `tests/test_tracing.py` 的 `@pytest.mark.parametrize` 清單中加入你的新類別。
