from abc import ABC, abstractmethod

from langfuse import observe


class GenericModelBackend(ABC):
    """Abstract base class for all LLM model backends.

    This class defines the unified interface for generating content and ensures
    that all derived backends are automatically observed by Langfuse.
    """

    def __init__(self, model_name: str) -> None:
        """Initialize the backend with a specific model name.

        Args:
            model_name: The identifier of the model (e.g., 'gemini-2.5-flash').
        """
        self.model_name = model_name

    @abstractmethod
    @observe()
    def generate(self, prompt: str) -> str:
        """Generate content based on the provided prompt.

        All implementations must override this method. Tracing is handled
        automatically by the @observe decorator on this base method.

        Args:
            prompt: The text prompt to be processed by the model.

        Returns:
            The generated response as a string.
        """
