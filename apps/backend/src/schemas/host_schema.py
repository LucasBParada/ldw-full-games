from pydantic import BaseModel

class HostCreate(BaseModel):
    name: str
    country: str