from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from app.slack.socket import start_socket_mode
from app.obs.router import router as obs_router
from app.web.router import router as web_router
from app.zep.bot import run_zep
from app.zep.chat import handle_zep_chat

import threading
import asyncio
app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/web/static"),
    name="static",
)

app.include_router(obs_router)
app.include_router(web_router)

@app.on_event("startup")
def startup_event():
    print("[STARTUP] FastAPI startup event fired")
    start_socket_mode()

    threading.Thread(
        target=lambda: asyncio.run(run_zep(handle_zep_chat)),
        daemon=True
    ).start()