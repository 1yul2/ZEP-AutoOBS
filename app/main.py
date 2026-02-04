from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.slack.socket import start_socket_mode
from app.web.router import router as web_router
from app.web.settings import router as settings_api_router
from app.zep.bot import run_zep
from app.zep.chat import handle_zep_chat
from app.core.config import settings
import threading
import asyncio

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory="app/web/static"),
    name="static",
)


app.include_router(web_router)
app.include_router(settings_api_router)

@app.on_event("startup")
def startup_event():
    if settings.SLACK_ENABLED:
        if settings.LOGGING_ENABLED:
            print("[알림] : 슬랙 메시지 감지 시스템을 시작합니다.")
    start_socket_mode()
    if settings.ZEP_ENABLED:
        if settings.LOGGING_ENABLED:
            print("[알림] : ZEP 감지 시스템을 시작합니다.")
        threading.Thread(
            target=lambda: asyncio.run(run_zep(handle_zep_chat)),
            daemon=True
        ).start()