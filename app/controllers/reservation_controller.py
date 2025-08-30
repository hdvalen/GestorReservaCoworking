from pydantic import BaseModel

class CreateReservationSchema(BaseModel):
    room_id: int
    user_id: int
    date: str
    start_time: str
    end_time: str
    state: str