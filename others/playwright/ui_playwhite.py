import playwright
# 异步模式
import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright


async def run(playwright):
    # 创建一个浏览器实例
    chromium = playwright.chromium
    browser = await chromium.launch()
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://testfb.tostar.top/cn/")
    # browser = await chromium.launch(channel="msedge")
    # page=await browser.new_page()
    # await page.goto("https://www.baidu.com")
    # await page.screenshot(path="baidu.png")
    # print(await page.title())
    # 创建两个浏览器上下文
    user_context = await browser.new_context()
    admin_context = await browser.new_context()

    # 创建各种页面和上下文的交互

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
# asyncio.run(main())

with sync_playwright() as playwrigh:
    brower = playwright.chromium.lunch()
