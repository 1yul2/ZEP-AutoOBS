from pydantic import BaseModel

class ObsResponse(BaseModel):
    status: str
    message: str