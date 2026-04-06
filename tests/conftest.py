import sys
from pathlib import Path

# Ensure project root is on sys.path so `backends` can be found by bare `pytest`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import os

import pytest
from dotenv import load_dotenv
from langfuse import Langfuse

from backends.gemini import GeminiBackend
from backends.mock import MockBackend

# Load environment once for all tests
load_dotenv()


@pytest.fixture(scope="session")
def langfuse_client() -> Langfuse:
    """Initialize a persistent Langfuse client for the test session.

    This client is used for manual operations like flushing data.
    """
    public_key = (
        os.getenv("LANGFUSE_INIT_PROJECT_PUBLIC_KEY")
        or os.getenv("LANGFUSE_PUBLIC_KEY")
    )
    secret_key = (
        os.getenv("LANGFUSE_INIT_PROJECT_SECRET_KEY")
        or os.getenv("LANGFUSE_SECRET_KEY")
    )
    return Langfuse(
        public_key=public_key,
        secret_key=secret_key,
        host="http://localhost:3000",
    )


@pytest.fixture
def gemini_backend() -> GeminiBackend:
    """Provide a Gemini backend instance for testing."""
    return GeminiBackend()


@pytest.fixture
def mock_backend() -> MockBackend:
    """Provide a Mock backend instance for testing."""
    return MockBackend()
