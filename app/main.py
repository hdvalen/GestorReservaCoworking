from fastapi import FastAPI
from app.auth import router as auth 
from app.routes.roomRouter import room_router
from app.routes.reservationRouter import reservation_router



app = FastAPI()

app.include_router(auth.app)
app.include_router(room_router.app)
app.include_router(reservation_router.app)
    
    