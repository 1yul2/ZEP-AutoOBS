from app.obs.service import ObsService


def handle_camera_event(event_type: str):
    obs = ObsService()
    obs.connect()

    try:
        status = obs.get_record_status()
        recording = status["output_active"]
        paused = status["output_paused"]

        if event_type == "on":
            if not recording:
                print("[OBS] camera ON → start recording")
                obs.start_record()
            elif paused:
                print("[OBS] camera ON → resume recording")
                obs.resume_record()

        elif event_type == "off":
            if recording and not paused:
                print("[OBS] camera OFF → pause recording")
                obs.pause_record()

    finally:
        obs.disconnect()