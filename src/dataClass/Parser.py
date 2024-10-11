from pydantic import BaseModel


class SubParser(BaseModel):
    name: str
    help: str


class Param(BaseModel):
    name: str
    help: str
