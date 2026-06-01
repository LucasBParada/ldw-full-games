from pydantic import BaseModel, Field

class PlayerCreate(BaseModel):
    game_id: int
    nickname: str = Field(min_length=3, max_length=30)
    level: int = Field(ge=1)