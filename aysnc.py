import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as pw: 
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.whatismybrowser.com/p")
        print(await page.title())
        await browser.close()

asyncio.run(main())
