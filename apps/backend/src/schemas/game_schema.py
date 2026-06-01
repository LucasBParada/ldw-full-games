from pydantic import BaseModel

class GameCreate(BaseModel):
    host_id: int
    name: str
    genre: str