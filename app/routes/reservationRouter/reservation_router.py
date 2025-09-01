from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from typing import Annotated, List
from app.config.database import SessionLocal, Base
from app.models.reservationModel.reservation_model import Reservations
from sqlalchemy import Column, Integer, String
from app.auth.auth import get_current_user
from app.controllers.reservationController.reservation_controller import  CreateReservationSchema


app=APIRouter()

#POST /reservations
#GET /reservations/me
#GET /reservations/room/{room_id}
#GET /reservations/date/{yyyy-mm-dd}
#DELETE /reservations/{id} (cancelar)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/reservations", tags=["Reservations"], status_code=status.HTTP_201_CREATED)
def create_reservation(
    create_reservation_request: CreateReservationSchema,
    db: db_dependency,
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para crear reservas"
        )

    new_reservation = Reservations(
        room_id=create_reservation_request.room_id,
        user_id=create_reservation_request.user_id,
        date=create_reservation_request.date,
        start_time=create_reservation_request.start_time,
        end_time=create_reservation_request.end_time,
        state=create_reservation_request.state
    )

    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)

    return {"message": "Reservation created successfully", "reservation": new_reservation}

@app.get("/reservations/me", tags=["Reservations"], response_model=List[CreateReservationSchema], status_code=status.HTTP_200_OK)
def get_my_reservations(
    db: db_dependency,
    current_user: dict = Depends(get_current_user)
):
    reservations = db.query(Reservations).filter(Reservations.user_id == current_user["id"]).all()
    return {"reservations": reservations}

@app.get("/reservations/room/{room_id}", tags=["Reservations"], response_model=List[CreateReservationSchema], status_code=status.HTTP_200_OK)
def get_reservations_by_room(
    room_id: int,
    db: db_dependency
):
    reservations = db.query(Reservations).filter(Reservations.room_id == room_id).all()
    return {"reservations": reservations}

@app.get("/reservations/date/{date}", tags=["Reservations"], response_model=List[CreateReservationSchema], status_code=status.HTTP_200_OK)
def get_reservations_by_date(
    date: str,
    db: db_dependency
):
    reservations = db.query(Reservations).filter(Reservations.date == date).all()
    return {"reservations": reservations}

@app.delete("/reservations/{id}", tags=["Reservations"], status_code=status.HTTP_204_NO_CONTENT)
def cancel_reservation(
    id: int,
    db: db_dependency,
    current_user: dict = Depends(get_current_user)
):
    reservation = db.query(Reservations).filter(Reservations.id == id, Reservations.user_id == current_user["id"]).first()
    if not reservation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reservation not found"
        )

    db.delete(reservation)
    db.commit()