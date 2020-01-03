from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    disable: bool

class UserDb(User):
    pw: str