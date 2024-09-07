from pydantic import BaseModel


class User(BaseModel):
    """User schema."""

    id: int
    username: str
    role: str
