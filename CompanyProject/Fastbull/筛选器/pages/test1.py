
import asyncio
from playwright.async_api  import async_playwright

url='https://testfb.tostar.top/cn/login?next=https://testfb.tostar.top/cn/signal/user-j32w0yel4v/account'
async def stockFilters(url):
    # 使用async_playwright异步模式启动Chromium浏览器
    async with (async_playwright() as p):
        browser = await p.chromium.launch(headless=False)   # 启动Chromium浏览器，非头less模式
        page = await browser.new_page()   # 创建新的页面对象

        # 这里添加最大化窗口的代码
        # await page.set_viewport_size({'width': 1920, 'height': 1080})  # 设置浏览器窗口大小为1920x1080

        await page.goto(url)   # 导航到指定的URL

        await page.wait_for_timeout(3000)
        email = page.locator("text=邮箱/ID")
        await email.click()

        await page.locator('#inputMailText').fill('7@qq.com')
        await page.locator('#inputMailPwd').fill('a1234567')
        await page.locator('#mailBtn').click()


        # 可能需要等待页面更新完成
        await page.wait_for_timeout(3000)  # 延迟1秒确保页面加载完成

# 运行函数
asyncio.run(stockFilters(url))