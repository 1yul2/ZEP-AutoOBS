from fastapi import APIRouter
from app.slack.service import SlackService
from app.slack.parser import parse_camera_event
from app.obs.controller import handle_camera_event


router = APIRouter(prefix="/slack", tags=["Slack"])


@router.post("/sync-camera")
def sync_camera():
    slack = SlackService()
    texts = slack.get_recent_texts(limit=3)

    for text in texts:
        event = parse_camera_event(text)
        if event:
            handle_camera_event(event)
            return {
                "handled": event,
                "text": text
            }

    return {"handled": None}