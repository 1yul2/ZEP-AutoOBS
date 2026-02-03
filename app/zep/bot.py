import asyncio
from playwright.async_api import async_playwright

async def run_zep(on_chat):
    print("🔥 [ZEP BOT] run_zep started")
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu"
            ]
        )
        page = await browser.new_page()

        # WebSocket 감지
        def handle_ws(ws):
            ws.on(
                "framereceived",
                lambda data: on_chat(data)
            )

        page.on("websocket", handle_ws)

        print("ZEP 접속 중...")
        await page.goto("https://zep.us/play/gG9aqQ")
        print("🔥 [ZEP BOT] page.goto done")
        # 계속 실행 유지
        while True:
            await asyncio.sleep(1)