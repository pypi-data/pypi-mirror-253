from typing import Optional


class Context(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, **kwargs):
        super().__init__()

        self._is_success: bool = True
        self._error: Optional[str] = None

        for field, value in kwargs.items():
            self[field] = value

    def failure(self, error_message: str) -> 'Context':
        self._error = error_message
        self._is_success = False

        return self

    def success(self, **kwargs) -> 'Context':
        self.update(kwargs)
        self._is_success = True

        return self

    def is_failure(self) -> bool:
        return not self._is_success

    def is_success(self) -> bool:
        return self._is_success

    @property
    def error(self):
        return self._error
