from .BasePage import BasePage
from playwright.sync_api import Page

class StockFiltersPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def select_market(self):
        # 定位并悬停在触发下拉菜单的元素上
        # market_trigger_locator = self.page.locator('//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]')
        market_trigger_locator = self.page.locator("(//span[@class='el-popover__reference-wrapper']//div)[1]")
        await market_trigger_locator.hover()

        # 定位并等待“越南股”选项变为可见状态
        # 等待下拉菜单中的“越南股”选项变得可见
        # await self.page.wait_for_selector('//*[@id="el-popover-3077"]/div/ul/li[2]', state='visible').nth(1)
        #
        # # 重新定义定位器
        # vietnam_option_locator = self.page.locator('//*[@id="el-popover-3077"]/div/ul/li[2]')
        #
        # # 点击“越南股”选项
        # await vietnam_option_locator.click()

        await self.page.wait_for_timeout(2000)
        vietnam_option_locator = self.page.locator('//*[@id="el-popover-3077"]/div/ul/li[2]').nth(0)
        # vietnam_option_locator = self.page.locator('li:has-text("越南股")')
        await vietnam_option_locator.wait_for(state='visible')
        # # 点击“越南股”选项
        await vietnam_option_locator.click()

    async def select_exchange(self):
        # market_locator = page.locator('//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span/span/div')
        # await market_locator.hover()
        # market_locator = self.page.locator('//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]')
        market_locator = self.page.locator("(//div[contains(text(),'交易所')])[4]")
        # market_locator = self.page.locator("(//div[@class='btn-wrap el-popover__reference'])[2]")
        await market_locator.hover()
        await self.page.click('text=纳斯达克')
        # await self.page.click('text=美交所')
        # await self.page.click('text=纽交所')

    async def select_industry(self):
        industry_locator = self.page.locator('//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/span/span/div')
        await industry_locator.hover()
        await self.page.click('text=能源')

    async def select_indicator(self):
        await self.page.click('text=估值指标')
        await self.page.click('text=<12')

    async def save_filter(self, name: str):
        create_button_locator = self.page.locator('#__layout > div > div.layout-box-left.container-layer > div.page.layout-content.container > div:nth-child(1) > div.panel-filter-wrap > div.panel-filter.panel-filter-box > div.panel-filter-content > div.panel-filter-content-footer > div > button.el-button.el-button--primary.el-button--mini > span')
        await create_button_locator.click()
        await self.page.get_by_placeholder('请输入筛选器名称').fill(name)
        await self.page.get_by_role('button', name='保存').click()

    async def add_view(self):
        add_view_button = self.page.locator('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/div[1]/table/thead/tr/th[12]/div/button')
        await add_view_button.click()

    async def search_indicator(self, keyword: str):
        await self.page.get_by_placeholder('请搜索指标名').fill(keyword)

    async def collect(self):
        collect_button = self.page.locator("//*[@id='__layout']/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[4]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/svg[1]")
        await collect_button.click()