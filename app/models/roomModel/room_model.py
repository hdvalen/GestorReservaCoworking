from app.config.database import Base
from sqlalchemy import Column, Integer, String


class Rooms(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    sede = Column(String(50), nullable=False)
    capacidad = Column(Integer, nullable=False)
    recursos = Column(String(255), nullable=False)