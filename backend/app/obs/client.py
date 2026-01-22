from obsws_python import ReqClient
from app.core.config import OBS_HOST, OBS_PORT, OBS_PASSWORD

def get_obs_client() -> ReqClient:
    return ReqClient(
        host=OBS_HOST,
        port=OBS_PORT,
        password=OBS_PASSWORD,
        timeout=3
    )