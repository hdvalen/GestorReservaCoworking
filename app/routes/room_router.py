from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from typing import Annotated
from app.config.database import SessionLocal, Base
from app.models.room_model import Rooms
from sqlalchemy import Column, Integer, String
from app.auth.auth import get_current_user
from app.controllers.room_controller import CreateRoomSchema

app=APIRouter()

#GET /rooms
#POST /rooms (admin)
#PUT /rooms/{id} (admin)
#DELETE /rooms/{id} (admin)


    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]



@app.post("/rooms", tags=["Rooms"], status_code=status.HTTP_201_CREATED)
def create_room(
    create_room_request: CreateRoomSchema,
    db: db_dependency,
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin": 
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para crear salas"
        )

    new_room = Rooms(
        name=create_room_request.name,
        sede=create_room_request.sede,
        capacidad=create_room_request.capacidad,
        recursos=create_room_request.recursos
    )

    db.add(new_room)
    db.commit()
    db.refresh(new_room)

    return {"message": "Room created successfully", "room": new_room}


