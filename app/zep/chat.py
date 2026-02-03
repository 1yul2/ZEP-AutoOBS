import re
from app.core.config import settings
from app.obs.controller import handle_camera_event

NICKNAME_PATTERN = re.compile(r"[가-힣a-zA-Z0-9_]{2,}")
MESSAGE_PATTERN = re.compile(r"\"([^\"]{1,100})")


def handle_zep_chat(data: bytes):
    text = data.decode("utf-8", errors="ignore")

    if len(text) > 300:
        return

    nicknames = NICKNAME_PATTERN.findall(text)
    if not nicknames:
        return

    nickname = next(
        (n for n in nicknames if any("가" <= c <= "힣" for c in n)),
        None
    )
    if not nickname:
        return

    if not any(admin in nickname for admin in settings.ZEP_SUPER_ADMINS):
        return


    msg_match = MESSAGE_PATTERN.search(text)
    if not msg_match:
        return

    message = msg_match.group(1)
    message = re.sub(r"[\x00-\x1f]", "", message)
    message = re.sub(r"[^\w가-힣]+$", "", message).strip()

    if not message:
        return

    msg = message.replace(" ", "")

    if "중지" in msg:
        handle_camera_event("off")
        return

    if "시작" in msg:
        handle_camera_event("on")
        return

    if "종료" in msg:
        handle_camera_event("stop")
        return

    print(f"💬 [ZEP CHAT] {nickname}: {message}", flush=True)