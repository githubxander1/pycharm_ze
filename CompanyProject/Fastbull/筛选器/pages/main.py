# main.py
import asyncio
from playwright.async_api import async_playwright
from login_page import LoginPage, StockFiltersPage


# from stock_filters_page import StockFiltersPage

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        login_page = LoginPage(page)
        await login_page.login('7@qq.com', 'a1234567')

        stock_filters_page = StockFiltersPage(page)
        await page.goto(url)
        await page.set_viewport_size({'width': 1920, 'height': 1080})

        await stock_filters_page.select_markets(['纳斯达克', '美交所', '纽交所'])
        # 省略其他操作...

        await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(main())
