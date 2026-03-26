from pydantic import BaseModel
from typing import List

class Character(BaseModel):
    name: str
    role: str


class StoryRequest(BaseModel):
    title: str
    genre: str
    characters: List[Character]


class StoryResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True