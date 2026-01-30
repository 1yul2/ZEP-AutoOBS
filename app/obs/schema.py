from pydantic import BaseModel


class RecordStatusResponse(BaseModel):
    is_recording: bool
    is_paused: bool