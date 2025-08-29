from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
import app.auth.model as models
from app.config.database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from app.auth import auth
from app.auth.auth import get_current_user 

app = APIRouter()
app.include_router(auth.app)

models.Base.metadata.create_all(bind=engine)


def get_bd():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_bd)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/", status_code=status.HTTP_200_OK)
async def user(user:user_dependency, db:db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autorizado")
    return {"User":user}

