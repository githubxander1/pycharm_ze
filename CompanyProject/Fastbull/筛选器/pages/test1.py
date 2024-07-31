import asyncio

from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright


async def stockFilters():
    # 使用async_playwright异步模式启动Chromium浏览器
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        page = await browser.new_page()  # 创建新的页面对象
        await page.goto('https://testfb.tostar.top/cn/signal/stockFilters')  # 导航到指定的URL

        await page.set_viewport_size({'width': 1920, 'height': 1080})
        await page.wait_for_timeout(2000)  # 延迟2秒确保页面加载完成

        # 定位到包含“越南股”图像和文本的div元素
        vietnamese_stock_locator = page.locator('//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]')

        # 首先触发下拉菜单的展开
        # await vietnamese_stock_locator.click()  # 或者使用mouseover方法，取决于具体的行为需求
        await vietnamese_stock_locator.hover()  # 如果点击不起作用，尝试hover

        # 等待“越南股”选项变得可交互
        # await page.wait_for_selector('//*[@id="el-popover-4178"]/div/ul/li[2]', state='attached')

        # 然后定位并选择“越南股”
        # vietnamese_stock_option = page.locator('//*[@id="el-popover-4178"]/div/ul/li[2]').first
        # await vietnamese_stock_option.click()

        collect = page.locator('//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/div[@class="code-box"]/svg')
        await collect.click()

        await page.wait_for_timeout(2000)

        # await page.screenshot(path='stockFilters.png')  # 截取页面屏幕快照，并保存为stockFilters.png
        # print(await page.title())  # 打印当前页面的标题

        # 点击下拉菜单以展开更多国家选项
        # dropdown_button =await page.wait_for_selector('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/span/span/div/i')
        # await dropdown_button.hover()
        #
        # # HK_option = await page.wait_for_selector('//*[@id="el-popover-3945"]/div/ul/li[3]')
        # US_option = await page.wait_for_selector('text=美国')
        # await US_option.click()
        #
        # # 选择交易所
        # market = page.locator('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/span/span/div')
        # await market.hover()
        # nsdk = await page.wait_for_selector('text=纳斯达克')
        # await nsdk.click()
        # mjs = await page.wait_for_selector('text=美交所')
        # await mjs.click()
        # njs = await page.wait_for_selector('text=纽交所')
        # await njs.click()

        # 行业
 #        industry = page.locator('//*[@id="__layout"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/span/span/div')
 #        await industry.hover()
 #        ny = await page.wait_for_selector('text=能源')
 #        await ny.click()
 #        ycl = await page.wait_for_selector('text=原材料')
 #        await ycl.click()
 #        indust = await page.wait_for_selector('text=工业')
 #        await indust.hover()
 #        dqsb = await page.wait_for_selector('text=电气设备')
 #        await dqsb.click()
 #
 #        # 指标
 #        Debt_index = await page.wait_for_selector('text=债务指标')
 #        await Debt_index.click()
 #        CurrentRatio = await page.wait_for_selector('text=<1')
 #        await CurrentRatio.click()
 #
 #        save = await page.wait_for_selector('text=保存')
 #        await save.click()
 # # 可能需要等待页面更新完成


asyncio.run(stockFilters())