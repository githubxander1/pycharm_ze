import asyncio
from playwright.async_api import async_playwright

class DetailPage:
    def __init__(self, url):
        self.url = url
        self.browser = None
        self.page = None
        self.playwright = None

    async def start(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        # 创建一个没有JavaScript的上下文
        # context = await self.browser.new_context(javascript_enabled=False)
        self.page = await self.browser.new_page()
        # 禁止图片加载
        # await self.page.set_extra_http_headers({"Accept-Language": "en-US,en;q=0.9"})
        # await self.page.route('**/*.{jpg,png}', lambda route: route.abort())
        await self.page.goto(self.url,timeout=30000)
        # 等待页面的主要资源加载完成:networkidle 表示网络请求基本静止，domcontentloaded 表示 DOM 完全加载，而 load 则表示页面及其所有资源都加载完毕。
        await self.page.wait_for_load_state('domcontentloaded')
        # await self.page.wait_for_load_state('load')
        await self.page.set_viewport_size({'width': 1920, 'height': 1080})

    async def stop(self):
        await self.browser.close()
        await self.playwright.stop()

    async def _click_element(self, xpath):
        try:
            element = self.page.locator(xpath)
            await element.click()
        except Exception as e:
            print(f'点击元素失败：{xpath},{e}')

    # 截图
    async def _screenshot(self,filename):
        await self.page.wait_for_load_state("networkidle")
        await self.page.wait_for_load_state("load")
        await self.page.screenshot(path=filename, full_page=True)

    # 各大tab
    async def click_news(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[2]")

    async def click_technicals(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[3]")

    async def click_finance(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[4]")

    async def click_analysis(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[5]")

    async def click_company(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[6]")

    # 技术指标_15m
    async def click_technicals_15m(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[1]")

    async def click_technicals_1h(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[3]")
        # Technicals_15m = page.locator()
    # 技术指标
    async def click_oscillators(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[1]/div[1]")
        # Oscillators = page.locator("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[1]/div[1]")
        # await Oscillators.click()
        # # 移动平均指数
        # Moving_Averages = page.locator("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[1]")
        # await Moving_Averages.evaluate("node => node.scrollIntoViewIfNeeded(true)")
        # await page.wait_for_timeout(2000)
        # await page.screenshot(path="技术指标.png", full_page=True)

        # Optionally wait for the element to become visible
        # await Moving_Averages.wait_for(state="visible")

    # 蜡烛形态
    async def click_candlestick_patterns(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[1]/div[2]")
        # Candlestick_Patterns = page.locator("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[1]/div[2]")
        # await Candlestick_Patterns.click()

        # 周期选择
    async def click_timeframes(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[3]/div[1]/div[1]/span[1]")
        # Period = page.locator("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[3]/div[1]/div[1]/span[1]")
        # await Period.click()

        # 选择15分钟
    async def click_candlestick_fifteen_minutes(self):
        await self._click_element("//li[text()='15m' ]")
        # await self._click_element("//*[@id='k_cycle-select-main']/li[2]")
        # fifteen = page.locator("//li[text()='15m' ]")
        # await fifteen.click()

        # 周期选择
        # Period = page.locator(
        #     "//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[3]/div[1]/div[1]/span[1]")
        # await page.wait_for_timeout(4000)
        # await Period.click()
        # # 选择15分钟
        # thirty = page.locator("//li[text()='30m' ]")
        # await thirty.click()

        # 选择1H
    async def click_one_hour(self):
        await self._click_element("//li[text()='1H' ]")
        # one_h = page.locator("//li[text()='1H' ]")
        # await one_h.click()

        # 选择1M
    async def click_one_minute(self):
        await self._click_element("//li[text()='1M' ]")
        # one_m = page.locator("//li[text()='1M' ]")
        # await one_m.click()

        # 图表形态


    # 状态选择
    async def click_all_trends(self):
        await self._click_element("//span[text()='所有状态' ]")
        # All_Trends = page.locator("//span[text()='所有状态' ]")
        # await All_Trends.click()
        # Bearish = page.locator("//span[text()='看涨' ]")

    # 看涨
    async def click_bearish(self):
        await self._click_element("//li[text()='看涨' ]")
        # Bearish = page.locator('//*[@id="k_symbol-select-main"]/li[2]')
        # await Bearish.click()
        # 所有形态

        # 所有形态
    async def click_all_patterns(self):
        await self._click_element("//span[text()='所有形态' ]")
        # All_Patterns = page.locator("//span[text()='所有形态' ]")
        # await All_Patterns.click()

    async def click_doji(self):
        await self._click_element("//li[text()='十字星' ]")
        # Doji = page.locator('//*[@id="k_form-select-main"]/li[2]')
        # await Doji.click()

    # 查看形态
    async def click_view(self):
        await self._click_element("//*[@id='candle_shape_body']/div[1]/div[1]/div[6]/div[1]")
        # View = page.locator('//*[@id="candle_shape_body"]/div/div[1]/div[6]/div')
        # await View.click()

        # await page.screenshot(path="../Doji.png", full_page=True)

    # 关闭查看窗口
    async def click_close_view(self):
        await self._click_element("//*[@id='getEnvironment']/div[1]/div[1]/div[2]/div[1]/i[1]")
        # close_view = page.locator('//*[@id="getEnvironment"]/div/div/div[2]/div[1]/i')
        # await close_view.click()


    # 图表形态
    async def click_chart_patterns(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[1]/div[3]")
        # Chart_Patterns = page.locator("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[1]/div[3]")
        # await Chart_Patterns.click()



        # 支撑阻力
    async def click_pivot_points(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[1]/div[4]")
        # Support_Resistance = page.locator("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[1]/div[4]")
        # await Support_Resistance.click()

    # 标准
    async def click_standard(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[5]/div[1]/div[2]/div[1]/span[1]")
        # Finance = page.locator("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[4]")
        # await Finance.click()

    async def click_woodie(self):
        await self._click_element("//*[@id='category_resistance-select-main']/li[5]")
        # Analysis = page.locator("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[5]")
        # await Analysis.click()

    # 选择1周
    async def click_pivot_1w(self):
        await self._click_element("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[5]/div[1]/div[5]/div[1]/div[1]/div[3]")
        # Company = page.locator("//*[@id='leftBox']/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[6]")
        # await Company.click()

    # 冒烟-点击各tab
    async def perform_actions(self):
        await self.click_news()
        # await asyncio.sleep(1)
        await self._screenshot("screenshots/news.png")
        await self.click_technicals()
        # await asyncio.sleep(1)
        await self._screenshot("screenshots/technicals.png")
        await self.click_finance()
        # await asyncio.sleep(1)
        await self._screenshot("screenshots/finance.png")
        await self.click_analysis()
        # await asyncio.sleep(1)
        await self._screenshot("screenshots/analysis.png")
        await self.click_company()
        # await asyncio.sleep(1)
        await self._screenshot("screenshots/company.png")

    # 技术指标切换各周期
    async def perform_technical_indicators(self):
        await self.click_technicals()
        await self.click_technicals_15m()
        await self._screenshot("screenshots/fifteen_minutes.png")
        await self.click_technicals_1h()
        await self._screenshot("screenshots/one_hour.png")

    # 蜡烛形态：周期-看涨-十字星-查看形态-关闭查看窗口
    async def perform_candlestick_patterns(self):
        await self.click_technicals()
        await self.click_candlestick_patterns()
        await self.click_timeframes()
        await self.click_candlestick_fifteen_minutes()
        await self.click_all_trends()
        await self.click_bearish()
        await self.click_all_patterns()
        await self.click_doji()
        await self.click_view()
        await self._screenshot("screenshots/doji.png")
        await self.click_close_view()

    # 支撑阻力
    async def perform_pivot_points(self):
        await self.click_technicals()
        await self.click_pivot_points()
        await self.click_standard()
        await self.click_woodie()
        await self.click_pivot_1w()
        await self._screenshot("screenshots/woodie.png")
    async def run(self):
        await self.start()
        try:
            # await self.perform_actions()
            # await self.perform_technical_indicators()
            # await self.perform_candlestick_patterns()
            await self.perform_pivot_points()
        finally:
            await self.stop()

# Usage
async def main():
    detail_page = DetailPage("https://testfb.tostar.top/cn/quotation-detail/NASDAQ-AAPL")
    await detail_page.run()

asyncio.run(main())