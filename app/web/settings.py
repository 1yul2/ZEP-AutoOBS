from fastapi import APIRouter
from app.core.env_writer import write_env, read_env

router = APIRouter(prefix="/api/settings")
print("🔥 settings.py LOADED", flush=True)

@router.get("")
def get_settings():
    env = read_env()

    return {
        # OBS
        "obs_host": env.get("OBS_HOST", ""),
        "obs_port": env.get("OBS_PORT", ""),
        "obs_password": env.get("OBS_PASSWORD", ""),

        # Slack
        "slack_enabled": env.get("SLACK_ENABLED", "false") == "true",
        "slack_detect_camera": env.get("SLACK_DETECT_CAMERA", "false") == "true",
        "slack_detect_join_leave": env.get("SLACK_DETECT_JOIN_LEAVE", "false") == "true",
        "slack_bot_token": env.get("SLACK_BOT_TOKEN", ""),
        "slack_app_token": env.get("SLACK_APP_TOKEN", ""),
        "slack_channel_id": env.get("SLACK_CHANNEL_ID", ""),
        "slack_target_nickname": env.get("SLACK_TARGET_NICKNAME", ""),

        # ZEP
        "zep_enabled": env.get("ZEP_ENABLED", "false") == "true",
        "zep_super_admins": env.get("ZEP_SUPER_ADMINS", ""),
        "zep_url": env.get("ZEP_URL", ""),
    }


@router.post("")
def update_settings(data: dict):
    # OBS
    write_env("OBS_HOST", data["obs_host"])
    write_env("OBS_PORT", data["obs_port"])
    write_env("OBS_PASSWORD", data["obs_password"])

    # Slack
    write_env("SLACK_ENABLED", str(data["slack_enabled"]).lower())
    write_env("SLACK_DETECT_CAMERA", str(data["slack_detect_camera"]).lower())
    write_env("SLACK_DETECT_JOIN_LEAVE", str(data["slack_detect_join_leave"]).lower())
    write_env("SLACK_BOT_TOKEN", data["slack_bot_token"])
    write_env("SLACK_APP_TOKEN", data["slack_app_token"])
    write_env("SLACK_CHANNEL_ID", data["slack_channel_id"])
    write_env("SLACK_TARGET_NICKNAME", data["slack_target_nickname"])

    # ZEP
    write_env("ZEP_ENABLED", str(data["zep_enabled"]).lower())
    write_env("ZEP_SUPER_ADMINS", data["zep_super_admins"])
    write_env("ZEP_URL", data["zep_url"])

    return {"ok": True}