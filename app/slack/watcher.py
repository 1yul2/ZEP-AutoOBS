import time
import threading

from app.slack.service import SlackService
from app.slack.parser import parse_camera_event
from app.obs.controller import handle_camera_event


def start_slack_watcher(interval: int = 5):
    """
    Slack 메시지를 주기적으로 확인하는 백그라운드 루프
    """
    def loop():
        print("[WATCHER] Slack watcher started")
        slack = SlackService()
        last_text = None

        while True:
            try:
                texts = slack.get_recent_texts(limit=1)
                if texts:
                    text = texts[0]

                    # 이미 처리한 메시지면 스킵
                    if text != last_text:
                        event = parse_camera_event(text)
                        if event:
                            handle_camera_event(event)
                        last_text = text

            except Exception as e:
                print(f"[Slack Watcher Error] {e}")

            time.sleep(interval)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()