from pydantic import BaseModel
from typing import List, Optional


class SlackMessage(BaseModel):
    user: Optional[str]
    text: str
    ts: str


class SlackMessageListResponse(BaseModel):
    channel_id: str
    messages: List[SlackMessage]