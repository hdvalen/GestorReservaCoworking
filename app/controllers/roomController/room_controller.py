from pydantic import BaseModel

class CreateRoomSchema(BaseModel):
    name: str
    sede: str
    capacidad: int
    recursos: str