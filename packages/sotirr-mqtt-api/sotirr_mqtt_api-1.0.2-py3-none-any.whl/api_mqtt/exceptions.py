"""Contains custom exceptions."""
from typing import Any, Optional


class Error(Exception):
    """Custom error class.

    Attributes:
        message - explanation of the error.
        data - any other data.
    """

    default_message: str = ''

    def __init__(self, message: Optional[str] = None, data: Any = None, *args: object) -> None:
        """Save initial variables."""
        self.message: str = message if message else self.default_message
        self.data = data
        super().__init__(self.message, self.data, *args)
