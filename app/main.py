from fastapi import FastAPI
from app.auth import router as auth 

app = FastAPI()

app.include_router(auth.app)
    
    