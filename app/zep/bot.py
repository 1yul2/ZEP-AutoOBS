import asyncio
from playwright.async_api import async_playwright
from app.core.config import settings

async def run_zep(on_chat):

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu"
            ]
        )

        context = await browser.new_context()
        await context.clear_cookies()

        page = await context.new_page()

        def handle_ws(ws):
            ws.on(
                "framereceived",
                lambda frame: on_chat(frame)
            )

        page.on("websocket", handle_ws)

        if settings.LOGGING_ENABLED:
            print("[알림] : ZEP 접속을 시도합니다.")
        await page.goto(settings.ZEP_URL)
        if settings.LOGGING_ENABLED:
            print("[알림] : ZEP 접속을 성공했습니다.")

        while True:
            await asyncio.sleep(1)