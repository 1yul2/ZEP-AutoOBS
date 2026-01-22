from app.obs.client import get_obs_client

def start_recording():
    obs = get_obs_client()
    obs.start_record()
    return "녹화 시작"

def stop_recording():
    obs = get_obs_client()
    obs.stop_record()
    return "녹화 중지"

def pause_recording():
    obs = get_obs_client()
    obs.pause_record()
    return "녹화 일시정지"

def resume_recording():
    obs = get_obs_client()
    obs.resume_record()
    return "녹화 재개"