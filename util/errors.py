class InputError(Exception):
    """Raised when the puzzle input is malformed."""

    def __init__(self, message):
        self.message = message
