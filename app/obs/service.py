from obswebsocket import obsws, requests


class ObsService:
    def __init__(self):
        self.client = obsws(
            host="host.docker.internal",
            port=4455,
            password="gksdbf1234",  # 나중에 인증 쓰면 추가
        )

    def connect(self):
        self.client.connect()

    def disconnect(self):
        self.client.disconnect()

    # =====================
    # 상태 조회
    # =====================
    def get_record_status(self):
        res = self.client.call(requests.GetRecordStatus())
        return {
            "is_recording": res.getOutputActive(),
            "is_paused": res.getOutputPaused(),
        }

    # =====================
    # 녹화 시작
    # =====================
    def start_record(self):
        status = self.get_record_status()

        if status["is_recording"]:
            return {"message": "already recording"}

        self.client.call(requests.StartRecord())
        return {"message": "recording started"}

    # =====================
    # 녹화 일시정지
    # =====================
    def pause_record(self):
        status = self.get_record_status()

        if not status["is_recording"]:
            return {"message": "not recording"}

        if status["is_paused"]:
            return {"message": "already paused"}

        self.client.call(requests.PauseRecord())
        return {"message": "recording paused"}

    # =====================
    # 정지한 거 시작 (재개)
    # =====================
    def resume_record(self):
        status = self.get_record_status()

        if not status["is_recording"]:
            return {"message": "not recording"}

        if not status["is_paused"]:
            return {"message": "not paused"}

        self.client.call(requests.ResumeRecord())
        return {"message": "recording resumed"}

    # =====================
    # 녹화 종료
    # =====================
    def stop_record(self):
        status = self.get_record_status()

        if not status["is_recording"]:
            return {"message": "not recording"}

        self.client.call(requests.StopRecord())
        return {"message": "recording stopped"}