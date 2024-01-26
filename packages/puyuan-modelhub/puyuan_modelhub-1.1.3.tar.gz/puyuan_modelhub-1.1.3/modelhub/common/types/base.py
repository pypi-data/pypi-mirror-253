from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    def to_event(self, prefix="data: ") -> str:
        return f"{prefix}{self.json()}\r\n\r\n"

    class Config:
        arbitrary_types_allowed = True
