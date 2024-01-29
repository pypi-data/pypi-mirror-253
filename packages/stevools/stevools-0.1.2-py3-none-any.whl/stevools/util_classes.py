class OpenAIModelManager:
    """OpenAI Model Manager

    An OpenAI Model Manager can apply different OpenAI models through `self.apply_model()`
    and can be read from `self.model_name`. It also applies the model change recursively
    to all its `OpenAIModelManager` type fields.
    """
    def __init__(self, model_name: str = "gpt-3.5-turbo-1106"):
        self._model_name = model_name
        self.apply_model(model_name)

    @property
    def model_name(self) -> str:
        """Return the current model name."""
        return self._model_name

    def apply_model(self, model_name: str):
        """Apply a different OpenAI model.

        Args:
            model_name (str): The name of the model to apply.

        This method also applies the model change recursively to all fields
        of `OpenAIModelManager` type.
        """
        self._model_name = model_name
        for field_name, field_value in self.__dict__.items():
            if isinstance(field_value, OpenAIModelManager) and field_value.model_name != model_name:
                field_value.apply_model(model_name)


__all__ = [
    "OpenAIModelManager",
]
