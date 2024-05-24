import asyncio

from playwright.async_api import async_playwright

url = 'https://testfb.tostar.top/cn/signal/stockFilters'
login_url = 'https://testfb.tostar.top/cn/login?next=https://testfb.tostar.top/cn/signal/user-j32w0yel4v/account'


async def main():
    async with async_playwright() as p:
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

        # 筛选器部分
        # await page.screenshot(path='stockFilters.png')  # 可选：截取页面屏幕快照
        # print(await page.title())  # 可选：打印当前页面的标题

        # 市场
        market_locator = page.locator('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/span/span/div')
        await market_locator.hover()
        nasdaq_locator = await page.wait_for_selector('text=纳斯达克', state='visible')
        await nasdaq_locator.click()
        us_locator = await page.wait_for_selector('text=美交所', state='visible')
        await us_locator.click()
        nj_locator = await page.wait_for_selector('text=纽交所', state='visible')
        await nj_locator.click()

        # 行业
        industry_locator = page.locator('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/span/span/div')
        await industry_locator.hover()
        energy_locator = await page.wait_for_selector('text=能源', state='visible')
        await energy_locator.click()
        ycl_locator = await page.wait_for_selector('text=原材料', state='visible')
        await ycl_locator.click()
        industry_locator = await page.wait_for_selector('text=工业', state='visible')
        industry_locator_hover = await industry_locator.hover()
        dqsb_locator = await page.wait_for_selector('text=电气设备', state='visible')
        await dqsb_locator.click()

        # 指标
        debt_indicator_locator = await page.wait_for_selector('text=债务指标', state='visible')
        await debt_indicator_locator.click()
        current_ratio_locator = await page.wait_for_selector('text=<1', state='visible')
        await current_ratio_locator.click()

        # 保存设置
        save_button_locator = await page.wait_for_selector('text=保存', state='visible')
        await save_button_locator.click()

        # 可能需要等待页面更新完成
        await page.wait_for_timeout(3000)  # 延迟1秒确保页面加载完成

        # 关闭浏览器
        await browser.close()


asyncio.run(main())
