from app.obs.service import ObsService
from app.core.config import settings

def handle_camera_event(event_type: str):
    obs = ObsService()
    obs.connect()

    try:
        status = obs.get_record_status()
        recording = status["output_active"]
        paused = status["output_paused"]

        if event_type == "on":
            if not recording:
                if settings.LOGGING_ENABLED:
                    print(f"[알림] : 카메라(접속)을 감지하여 녹화를 시작합니다.")
                obs.start_record()
            elif paused:
                if settings.LOGGING_ENABLED:
                    print(f"[알림] : 카메라(접속)을 감지하여 녹화를 재개합니다.")
                obs.resume_record()

        elif event_type == "off":
            if recording and not paused:
                if settings.LOGGING_ENABLED:
                    print(f"[알림] : 카메라(접속)을 감지하여 녹화를 정지합니다.")
                obs.pause_record()

        elif event_type == "stop":
            if recording:
                if settings.LOGGING_ENABLED:
                    print(f"[알림] : 채팅을 감지하여 녹화를 종료합니다.")
                obs.stop_record()

    finally:
        obs.disconnect()