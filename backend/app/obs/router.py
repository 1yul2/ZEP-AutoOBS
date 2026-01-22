# app/obs/router.py

from fastapi import APIRouter, HTTPException
from app.obs import service
from app.obs.schema import ObsResponse

router = APIRouter(prefix="/obs", tags=["OBS"])

@router.post("/record/start", response_model=ObsResponse)
def record_start():
    try:
        message = service.start_recording()
        return {"status": "success", "message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/record/stop", response_model=ObsResponse)
def record_stop():
    try:
        message = service.stop_recording()
        return {"status": "success", "message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/record/pause", response_model=ObsResponse)
def record_pause():
    try:
        message = service.pause_recording()
        return {"status": "success", "message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/record/resume", response_model=ObsResponse)
def record_resume():
    try:
        message = service.resume_recording()
        return {"status": "success", "message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))