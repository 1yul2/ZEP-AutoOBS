import os
from dotenv import load_dotenv

load_dotenv()

def str_to_bool(v, default=False):
    if v is None:
        return default
    return str(v).strip().lower() in ("1", "true", "yes", "y", "on")

class Settings:
    # OBS
    OBS_HOST: str = os.getenv("OBS_HOST", "localhost")
    OBS_PORT: int = int(os.getenv("OBS_PORT", 4455))
    OBS_PASSWORD: str = os.getenv("OBS_PASSWORD", "")

    # Slack
    SLACK_ENABLED: bool = str_to_bool(os.getenv("SLACK_ENABLED"), default=True)
    SLACK_BOT_TOKEN: str = os.getenv("SLACK_BOT_TOKEN", "")
    SLACK_APP_TOKEN: str = os.getenv("SLACK_APP_TOKEN", "")
    SLACK_CHANNEL_ID: str = os.getenv("SLACK_CHANNEL_ID", "")
    SLACK_TARGET_NICKNAME: str = os.getenv("SLACK_TARGET_NICKNAME", "")
    SLACK_DETECT_CAMERA: bool = str_to_bool(os.getenv("SLACK_DETECT_CAMERA"), default=True)
    SLACK_DETECT_JOIN_LEAVE: bool = str_to_bool(os.getenv("SLACK_DETECT_JOIN_LEAVE"), default=True)

    # ZEP
    ZEP_ENABLED: bool = str_to_bool(os.getenv("ZEP_ENABLED"), default=True)
    ZEP_URL: str = os.getenv("ZEP_URL", "")
    ZEP_SUPER_ADMINS: set[str] = {
        name.strip()
        for name in os.getenv("ZEP_SUPER_ADMINS", "").split(",")
        if name.strip()
    }


settings = Settings()

# 필수 값 체크 (서버 시작 시 바로 터지게)
if not settings.SLACK_BOT_TOKEN:
    raise RuntimeError("SLACK_BOT_TOKEN is not set")

if not settings.SLACK_CHANNEL_ID:
    raise RuntimeError("SLACK_CHANNEL_ID is not set")

