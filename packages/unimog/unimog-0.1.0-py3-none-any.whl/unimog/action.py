from abc import abstractmethod

from typing import Any, Optional
from unimog.context import Context


class Action:
    def __init__(self):
        self.context = Context()

    def __call__(self, context: Context = None, **kwargs) -> Context:
        if context:
            self.context = context
        else:
            self.context = Context(**kwargs)

        try:
            additional_data = self.perform()
            if not additional_data:
                additional_data = {}
            return self.context.success(**additional_data)
        except Exception as e:
            return self.context.failure(str(e))

    @abstractmethod
    def perform(self) -> Optional[dict[str, Any]]:
        pass
