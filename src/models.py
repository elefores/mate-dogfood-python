"""Domain models, written against the Pydantic **v1** API.

Every construct in this module changed in Pydantic v2, so bumping the pin in
`requirements.txt` from 1.x to 2.x requires editing this file:

* ``@validator``        -> ``@field_validator`` (and the signature changes)
* ``class Config``      -> ``model_config = ConfigDict(...)``
* ``orm_mode``          -> ``from_attributes``
* ``.dict()``           -> ``.model_dump()``
"""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, validator


class User(BaseModel):
    id: int
    name: str
    email: str
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

    @validator("email")
    def email_must_contain_at(cls, value: str) -> str:
        if "@" not in value:
            raise ValueError("email must contain an '@'")
        return value

    class Config:
        orm_mode = True
        anystr_strip_whitespace = True

    def as_payload(self) -> dict:
        # `.dict()` was renamed to `.model_dump()` in Pydantic v2.
        return self.dict()
