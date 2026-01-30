from fastapi import FastAPI
from app.obs.router import router as obs_router

app = FastAPI()

app.include_router(obs_router)