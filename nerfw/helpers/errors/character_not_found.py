class CharacterNotFoundError(Exception):
    """Raised when character can't be found"""

    def __init__(self, character):
        message = f"Can't find character {character}"
        super().__init__(message)
