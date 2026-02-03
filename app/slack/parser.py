from app.core.config import settings


def parse_camera_event(text: str):
    """
    Slack 메시지에서 camera on/off 감지
    닉네임은 부분일치 허용
    """
    print(f"[PARSER] Raw text: {text}")

    keyword = settings.SLACK_TARGET_NICKNAME
    if keyword and keyword not in text:
        print("[PARSER] Nickname keyword not matched")
        return None

    if "카메라가 on 되었습니다" in text:
        print("[PARSER] Camera ON detected")
        return "on"

    if "카메라가 off 되었습니다" in text:
        print("[PARSER] Camera OFF detected")
        return "off"

    if "camera has been turned on" in text:
        return "on"

    if "camera has been turned off" in text:
        return "off"

    return None