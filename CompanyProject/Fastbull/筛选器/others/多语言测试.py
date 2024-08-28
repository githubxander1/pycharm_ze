import asyncio

from playwright.async_api import async_playwright

url = 'https://testfb.tostar.top/cn/signal/stockFilters'
login_url = 'https://testfb.tostar.top/cn/login?next=https://testfb.tostar.top/cn/signal/user-j32w0yel4v/account'


async def main():
    async with (async_playwright() as p):
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # 登录部分
        await page.goto(login_url)
        await page.wait_for_timeout(3000)
        email = page.locator("text=邮箱/ID")
        await email.click()
        await page.locator('#inputMailText').fill('7@qq.com')
        await page.locator('#inputMailPwd').fill('a1234567')
        await page.locator('#mailBtn').click()
        await page.wait_for_timeout(3000)

        # 跳转到目标页面
        await page.goto(url)

        # 设置视口大小
        await page.set_viewport_size({'width': 1920, 'height': 1080})


asyncio.run(main())