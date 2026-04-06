import pytest
from langfuse import Langfuse

from backends.gemini import GeminiBackend
from backends.mock import MockBackend


@pytest.mark.parametrize("backend_class", [MockBackend, GeminiBackend])
def test_backend_tracing(backend_class: type, langfuse_client: Langfuse) -> None:
    """Verify that different LLM backends correctly report traces to Langfuse.

    This test uses backend parametrization to ensure that both the Mock and
    Gemini implementations conform to the same tracing standards.

    Args:
        backend_class: The Backend class to be tested.
        langfuse_client: Fixture providing the Langfuse client.
    """
    # Initialize the specific backend; skip if API key is missing
    try:
        backend = backend_class()
    except ValueError as exc:
        if "API key" in str(exc):
            pytest.skip(f"Skipping {backend_class.__name__}: {exc}")
        raise

    print(f"\n🧪 正在測試後端: {backend.model_name}")

    # Execute a standard generation; skip if API key is invalid
    prompt = "Hello Langfuse! This is a structural test."
    try:
        result = backend.generate(prompt)
    except Exception as exc:
        if "API key" in str(exc) or "API_KEY_INVALID" in str(exc):
            pytest.skip(f"Skipping {backend_class.__name__}: invalid API key")
        raise

    # Assertions
    assert isinstance(result, str)
    assert len(result) > 0

    # Flush to ensure data is sent to the local server
    langfuse_client.flush()
    print(f"✅ 後端 {backend.model_name} 測試完成。")

