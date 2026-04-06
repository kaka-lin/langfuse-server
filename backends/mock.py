from langfuse import observe

from backends.base import GenericModelBackend


class MockBackend(GenericModelBackend):
    """Mock backend for connectivity and logic verification.

    Returns deterministic responses without making any real API calls.
    """

    def __init__(self, model_name: str = "mock-model") -> None:
        """Initialize the mock backend.

        Args:
            model_name: The name of the simulated model.
        """
        super().__init__(model_name)

    @observe()
    def generate(self, prompt: str) -> str:
        """Return a mock string for testing purposes.

        Args:
            prompt: The text prompt (ignored).

        Returns:
            A static mock response string.
        """
        return (
            f"This is a mock response from {self.model_name} "
            f"for your prompt '{prompt}'."
        )
