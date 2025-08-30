from app.config.database import Base
from sqlalchemy import Column, Integer, String

class Reservations(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    date = Column(String(50), nullable=False)
    start_time = Column(String(50), nullable=False)
    end_time = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
