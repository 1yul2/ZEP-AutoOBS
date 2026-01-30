import threading
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from app.core.config import settings
from app.slack.parser import parse_camera_event
from app.obs.controller import handle_camera_event


def start_socket_mode():
    print("[SOCKET] starting socket mode thread...")

    app = App(token=settings.SLACK_BOT_TOKEN)

    @app.event("message")
    def handle_message(event, say):
        text = event.get("text", "")
        event_type = parse_camera_event(text)
        if event_type:
            handle_camera_event(event_type)

    def run():
        print("[SOCKET] connecting to Slack...")
        handler = SocketModeHandler(app, settings.SLACK_APP_TOKEN)
        handler.start()

    thread = threading.Thread(target=run, daemon=True)
    thread.start()