from obswebsocket import obsws, requests
from app.core.config import settings


class ObsService:
    def __init__(self):
        self.client = obsws(
            settings.OBS_HOST,
            settings.OBS_PORT,
            settings.OBS_PASSWORD,
        )

    def connect(self):
        if not self.client.ws:
            self.client.connect()

    def disconnect(self):
        if self.client.ws:
            self.client.disconnect()

    def start_record(self):
        self.client.call(requests.StartRecord())

    def stop_record(self):
        self.client.call(requests.StopRecord())

    def pause_record(self):
        self.client.call(requests.PauseRecord())

    def resume_record(self):
        self.client.call(requests.ResumeRecord())

    def get_record_status(self):
        res = self.client.call(requests.GetRecordStatus())
        return {
            "output_active": res.getOutputActive(),
            "output_paused": res.getOutputPaused(),
        }