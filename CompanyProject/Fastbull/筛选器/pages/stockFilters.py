import asyncio

from playwright.async_api import async_playwright

url='https://testfb.tostar.top/cn/signal/stockFilters'


async def login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://testfb.tostar.top/cn/login?next=https://testfb.tostar.top/cn/signal/user-j32w0yel4v/account')

        # 登录
        await page.wait_for_timeout(3000)
        email = page.locator("text=邮箱/ID")
        await email.click()

        await page.locator('#inputMailText').fill('7@qq.com')
        await page.locator('#inputMailPwd').fill('a1234567')
        await page.locator('#mailBtn').click()

        await page.wait_for_timeout(3000)

        # product = page.get_by_text("产品", exact=True)
        product = page.get_by_role("link", name="产品").first
        await product.hover()
        await page.wait_for_timeout(3000)
        stock_filter = await page.wait_for_selector('text=筛选器')
        await stock_filter.click()
        # await product.get_by_role("listitem").filter(has_text="筛选器").click()
        await page.wait_for_timeout(3000)
        # product = page.locator('//*[@id="__layout"]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/a')
        # stockFilters = page.locator('//*[@id="__layout"]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div/div[1]/a[3]/span/span/text()')
        # await stockFilters.click()
asyncio.run(login())
async def stockFilters():
    # 使用async_playwright异步模式启动Chromium浏览器
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # 启动Chromium浏览器，非无头模式
        page = await browser.new_page()  # 创建新的页面对象
        await page.goto(url)  # 导航到指定的URL

        await page.set_viewport_size({'width': 1920, 'height': 1080})

        # await page.screenshot(path='stockFilters.png')  # 截取页面屏幕快照，并保存为stockFilters.png
        # print(await page.title())  # 打印当前页面的标题

        # 点击下拉菜单以展开更多国家选项
        # dropdown_button =await page.wait_for_selector('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/span/span/div/i')
        # await dropdown_button.hover()
        #
        # # HK_option = await page.wait_for_selector('//*[@id="el-popover-3945"]/div/ul/li[3]')
        # US_option = await page.wait_for_selector('text=美国')
        # await US_option.click()

        # 选择交易所
        market = page.locator('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/span/span/div')
        await market.hover()
        nsdk = await page.wait_for_selector('text=纳斯达克')
        await nsdk.click()
        mjs = await page.wait_for_selector('text=美交所')
        await mjs.click()
        njs = await page.wait_for_selector('text=纽交所')
        await njs.click()
        
        # 行业
        industry = page.locator('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/span/span/div')
        await industry.hover()
        ny = await page.wait_for_selector('text=能源')
        await ny.click()
        ycl = await page.wait_for_selector('text=原材料')
        await ycl.click()
        indust = await page.wait_for_selector('text=工业')
        await indust.hover()
        dqsb = await page.wait_for_selector('text=电气设备')
        await dqsb.click()

        # 指标
        Debt_index = await page.wait_for_selector('text=债务指标')
        await Debt_index.click()
        CurrentRatio = await page.wait_for_selector('text=<1')
        await CurrentRatio.click()

        save = await page.wait_for_selector('text=保存')
        await save.click()








        # 可能需要等待页面更新完成
        await page.wait_for_timeout(3000)  # 延迟1秒确保页面加载完成
        # await browser.close()  # 注释掉的代码，原意是关闭浏览器实例

# asyncio.run(stockFilters())