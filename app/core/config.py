import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # ===== OBS =====
    OBS_HOST: str = os.getenv("OBS_HOST", "localhost")
    OBS_PORT: int = int(os.getenv("OBS_PORT", 4455))
    OBS_PASSWORD: str = os.getenv("OBS_PASSWORD", "")

    # ===== Slack =====
    SLACK_BOT_TOKEN: str = os.getenv("SLACK_BOT_TOKEN", "")
    SLACK_APP_TOKEN: str = os.getenv("SLACK_APP_TOKEN", "")
    SLACK_CHANNEL_ID: str = os.getenv("SLACK_CHANNEL_ID", "")
    SLACK_TARGET_NICKNAME: str = os.getenv("SLACK_TARGET_NICKNAME", "")


settings = Settings()

# 필수 값 체크 (서버 시작 시 바로 터지게)
if not settings.SLACK_BOT_TOKEN:
    raise RuntimeError("SLACK_BOT_TOKEN is not set")

if not settings.SLACK_CHANNEL_ID:
    raise RuntimeError("SLACK_CHANNEL_ID is not set")