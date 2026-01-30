from slack_sdk import WebClient
from app.core.config import settings


class SlackService:
    def __init__(self):
        self.client = WebClient(token=settings.SLACK_BOT_TOKEN)