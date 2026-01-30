const API_BASE = "/record";

const recordingEl = document.getElementById("recording");
const pausedEl = document.getElementById("paused");

const btnStart = document.getElementById("btn-start");
const btnPause = document.getElementById("btn-pause");
const btnResume = document.getElementById("btn-resume");
const btnStop = document.getElementById("btn-stop");

/**
 * UI 상태를 즉시 반영하는 함수
 */
function setRecordingUI(isRecording, isPaused) {
  if (isRecording) {
    recordingEl.innerText = "녹화 중";
    recordingEl.className = "badge bg-danger";
  } else {
    recordingEl.innerText = "녹화 안 함";
    recordingEl.className = "badge bg-secondary";
  }

  if (isPaused) {
    pausedEl.innerText = "일시정지";
    pausedEl.className = "badge bg-warning";
  } else {
    pausedEl.innerText = "진행 중";
    pausedEl.className = "badge bg-success";
  }

  btnStart.disabled = isRecording;
  btnPause.disabled = !isRecording || isPaused;
  btnResume.disabled = !isRecording || !isPaused;
  btnStop.disabled = !isRecording;
}

/**
 * 실제 OBS 상태와 동기화
 */
async function fetchStatus() {
  try {
    const res = await fetch(`${API_BASE}/status`);
    const data = await res.json();
    setRecordingUI(data.is_recording, data.is_paused);
  } catch (e) {
    console.error("상태 조회 실패", e);
  }
}

/**
 * ▶ 녹화 시작
 * OBS 특성상 Start는 지연되므로
 * → UI 즉시 반영 + 나중에 동기화
 */
btnStart.onclick = async () => {
  // ✅ 즉각 반응
  setRecordingUI(true, false);

  try {
    await fetch(`${API_BASE}/start`, { method: "POST" });
  } catch (e) {
    console.error("녹화 시작 실패", e);
  }

  // 🔁 OBS 상태 확정 후 동기화
  setTimeout(fetchStatus, 1000);
};

/**
 * ⏸ 일시정지
 * (OBS 즉시 반영 → 그냥 동기화)
 */
btnPause.onclick = async () => {
  try {
    await fetch(`${API_BASE}/pause`, { method: "POST" });
    fetchStatus();
  } catch (e) {
    console.error("일시정지 실패", e);
  }
};

/**
 * ▶️ 재개
 * (OBS 즉시 반영 → 그냥 동기화)
 */
btnResume.onclick = async () => {
  try {
    await fetch(`${API_BASE}/resume`, { method: "POST" });
    fetchStatus();
  } catch (e) {
    console.error("재개 실패", e);
  }
};

/**
 * ⏹ 녹화 종료
 * Stop도 Start와 마찬가지로 지연됨
 */
btnStop.onclick = async () => {
  // ✅ 즉각 반응
  setRecordingUI(false, false);

  try {
    await fetch(`${API_BASE}/stop`, { method: "POST" });
  } catch (e) {
    console.error("녹화 종료 실패", e);
  }

  // 🔁 OBS 상태 확정 후 동기화
  setTimeout(fetchStatus, 1000);
};

// 최초 페이지 진입 시 상태 조회
fetchStatus();