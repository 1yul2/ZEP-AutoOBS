from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from app.core.config import settings
from app.slack.socket import start_socket_mode
from app.obs.router import router as obs_router
from app.web.router import router as web_router
from app.zep.bot import run_zep

import re
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


NICKNAME_PATTERN = re.compile(r"[가-힣a-zA-Z0-9_]{2,}")
MESSAGE_PATTERN = re.compile(r"\"([^\"]{1,100})")

def on_zep_chat(data: bytes):
    text = data.decode("utf-8", errors="ignore")

    if len(text) > 300:
        return

    nicknames = NICKNAME_PATTERN.findall(text)
    if not nicknames:
        return

    nickname = next((n for n in nicknames if any("가" <= c <= "힣" for c in n)), None)
    if not nickname:
        return
    if nickname not in settings.ZEP_SUPER_ADMINS:
        return

    msg_match = MESSAGE_PATTERN.search(text)
    if not msg_match:
        return

    message = msg_match.group(1)
    message = re.sub(r"[^\w\s가-힣!?.:,~@#$%^&*()+=\-_/]", "", message)
    message = re.sub(r"\($", "", message).strip()

    if not message:
        return

    print(f"💬 [ZEP CHAT] {nickname}: {message}", flush=True)

@app.on_event("startup")
def startup_event():
    print("[STARTUP] FastAPI startup event fired")
    start_socket_mode()

    threading.Thread(
        target=lambda: asyncio.run(run_zep(on_zep_chat)),
        daemon=True
    ).start()