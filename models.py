from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


def get_user() -> User:
    return User(id=1, name="ada")
