import asyncio
from playwright.async_api import async_playwright
from app.core.config import settings

BOT_NICKNAME = "REC_BOT"


async def run_zep(on_chat):
    print("🔥 [ZEP BOT] run_zep started", flush=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu"
            ]
        )

        # =============================
        # 1️⃣ 새 컨텍스트 (닉네임 캐시 차단)
        # =============================
        context = await browser.new_context()
        await context.clear_cookies()

        page = await context.new_page()

        # =============================
        # 2️⃣ WebSocket 프레임 감지
        # =============================
        def handle_ws(ws):
            ws.on(
                "framereceived",
                lambda frame: on_chat(frame)
            )

        page.on("websocket", handle_ws)

        # =============================
        # 3️⃣ ZEP 접속
        # =============================
        print("ZEP 접속 중...", flush=True)
        await page.goto(settings.ZEP_URL)
        print("🔥 [ZEP BOT] page.goto done", flush=True)

        # =============================
        # 4️⃣ 닉네임 자동 설정 (REC_BOT)
        # =============================
        await set_zep_nickname(page, BOT_NICKNAME)

        # =============================
        # 5️⃣ 프로세스 유지
        # =============================
        while True:
            await asyncio.sleep(1)


async def set_zep_nickname(page, nickname: str):
    """
    ZEP 첫 접속 시 뜨는 InitSettingModal에서
    닉네임 input(name="name")에 값을 넣고 확인 클릭
    """
    try:
        # 닉네임 입력 input 대기
        await page.wait_for_selector(
            'input[name="name"]',
            timeout=10000
        )

        # 닉네임 입력
        await page.fill(
            'input[name="name"]',
            nickname
        )

        # 확인 버튼 클릭
        await page.click(
            'button:has-text("확인"), button:has-text("OK"), button:has-text("시작")'
        )

        print(f"🤖 ZEP 캐릭터 닉네임 설정 완료: {nickname}", flush=True)

    except Exception as e:
        # 이미 닉네임이 설정된 경우 or 모달이 없는 경우
        print("ℹ️ ZEP 닉네임 입력 모달 없음 또는 이미 설정됨", flush=True)
        # 필요하면 디버깅용 출력
        # print("DEBUG:", e, flush=True)