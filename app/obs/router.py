from fastapi import APIRouter
from app.obs.service import ObsService
from app.obs.schema import RecordStatusResponse

router = APIRouter(prefix="/record", tags=["OBS"])


def with_obs(action):
    obs = ObsService()
    obs.connect()
    try:
        result = action(obs)
        return result
    finally:
        obs.disconnect()


@router.get(
    "/status",
    response_model=RecordStatusResponse,
    summary="방송 상태 보기",
    description="현재 OBS 녹화 상태(녹화 중 여부, 일시정지 여부)를 반환합니다."
)
def record_status():
    return with_obs(lambda obs: obs.get_record_status())


@router.post(
    "/start",
    summary="방송 시작",
    description="OBS 녹화를 시작합니다. 이미 녹화 중이면 아무 동작도 하지 않습니다."
)
def record_start():
    return with_obs(lambda obs: obs.start_record())


@router.post(
    "/pause",
    summary="방송 일시정지",
    description="녹화 중인 방송을 일시정지합니다."
)
def record_pause():
    return with_obs(lambda obs: obs.pause_record())


@router.post(
    "/resume",
    summary="방송 재개",
    description="일시정지된 방송을 다시 시작합니다."
)
def record_resume():
    return with_obs(lambda obs: obs.resume_record())


@router.post(
    "/stop",
    summary="방송 종료",
    description="진행 중인 OBS 녹화를 종료합니다."
)
def record_stop():
    return with_obs(lambda obs: obs.stop_record())