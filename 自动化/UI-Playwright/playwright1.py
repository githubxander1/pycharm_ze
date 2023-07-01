# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     # 如果使用参数headless = False，那么浏览器不会启动，会以无头模式运行脚本。
#     browser = p.chromium.launch(channel="msedge",headless=False)
#     # browser = p.chromium.launch(channel="chrome"，headless = False)
#     # browser = p.webkit.launch(headless=False)
#     page = browser.new_page()
#     page.goto('http://www.baidu.com')
#     print(page.title)
#     # browser.close()
import asyncio

from playwright.sync_api import sync_playwright

# 同步模式:
with sync_playwright() as p:
    brower=p.chromium.launch(channel='msedge',headless=False)
    page =brower.new_page()
    page.goto('http://www.163.com')
    print(page.title)
    brower.close()

async def main():
    async with sync_playwright() as p:
        brower=p.chromium.launch(channel='msedge',headless=False)
        page = brower.new_page()
        page.goto('http://www.163.com')
        brower.close()
asyncio.run(main())
