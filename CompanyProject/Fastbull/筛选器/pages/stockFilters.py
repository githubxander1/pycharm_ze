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

        # 筛选器部分
        # await page.screenshot(path='stockFilters.png')  # 可选：截取页面屏幕快照
        # print(await page.title())  # 可选：打印当前页面的标题

        # 市场
        await page.wait_for_timeout(3000)
        market_locator = page.locator('//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span/span/div')
        await market_locator.hover()
        US = await page.wait_for_selector('text=美国', state='visible')
        await US.click()

        Exchange = page.locator('//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/span/span/div')
        await Exchange.hover()
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
        await page.mouse.move(x=0, y=0)
        # ycl_locator = await page.wait_for_selector('text=原材料', state='visible')
        # await ycl_locator.click()
        # industry_locator = await page.wait_for_selector('text=工业', state='visible')
        # industry_locator_hover = await industry_locator.hover()
        # dqsb_locator = await page.wait_for_selector('text=电气设备', state='visible')
        # await dqsb_locator.click()

        # 指标
        debt_indicator_locator = await page.wait_for_selector('text=估值指标', state='visible')
        await debt_indicator_locator.click()
        PE_locator = await page.wait_for_selector('text=<12', state='visible')
        await PE_locator.click()

        # 保存设置
        # create_button_locator = await page.wait_for_selector('text=新建', state='visible')
        await page.wait_for_timeout(1000)
        create_button_locator = page.locator('#__layout > div > div.layout-box-left.container-layer > div.page.layout-content.container > div:nth-child(1) > div.panel-filter-wrap > div.panel-filter.panel-filter-box > div.panel-filter-content > div.panel-filter-content-footer > div > button.el-button.el-button--primary.el-button--mini > span')
        await create_button_locator.click()

        # 保存弹窗
        # save_input =
        await page.get_by_placeholder('请输入筛选器名称').fill('筛选器2')
        save_button = page.get_by_role('button', name='保存')
        await save_button.click()

        await page.wait_for_timeout(1000)
        add_view = page.locator('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/div[1]/table/thead/tr/th[12]/div/button')
        await add_view.click()

        # search_zhibiao =
        await page.get_by_placeholder('请搜索指标名').fill('市值')


        #
        # # 可能需要等待页面更新完成
        await page.wait_for_timeout(5000)  # 延迟1秒确保页面加载完成
        #
        # # 关闭浏览器
        # await browser.close()


asyncio.run(main())
