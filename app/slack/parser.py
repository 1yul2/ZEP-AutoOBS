from app.core.config import settings


def parse_camera_event(text: str):
    """
    Slack 메시지에서 camera on/off 감지
    닉네임은 부분일치 허용
    """
    if settings.LOGGING_ENABLED:
        print(f"[슬랙] : {text}")

    keyword = settings.SLACK_TARGET_NICKNAME
    if keyword and keyword not in text:
        return None

    if settings.SLACK_DETECT_CAMERA:
        if "카메라가 on 되었습니다" in text:
            return "on"

        if "카메라가 off 되었습니다" in text:
            return "off"

        if "camera has been turned on" in text:
            return "on"

        if "camera has been turned off" in text:
            return "off"

    if settings.SLACK_DETECT_JOIN_LEAVE:
        if "교실에 접속했습니다" in text:
            return "on"

        if "접속을 종료했습니다" in text:
            return "off"

    return None