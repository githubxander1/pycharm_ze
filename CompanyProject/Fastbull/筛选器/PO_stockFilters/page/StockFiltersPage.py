# from .BasePage import BasePage
from playwright.sync_api import Page, sync_playwright
from CompanyProject.Fastbull.筛选器.PO_stockFilters.config import STOCK_FILTERS_URL
from CompanyProject.Fastbull.筛选器.PO_stockFilters.page.BasePage import BasePage

class StockFiltersPage(BasePage):
    MARKET_TRIGGER_XPATH = "//*[@id='__layout']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]"
    EXCHANGE_TRIGGER_XPATH = "//*[@id='__layout']/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/span[1]/span[1]/div[1]"
    INDUSTRY_TRIGGER_XPATH = '//*[@id="__layout"]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/span/span/div'

    # CREATE_BUTTON_XPATH = "//span[contains(text(), '新建')]"
    CREATE_BUTTON_XPATH = "//button[contains(string(), '新建')]"
    COLLECT_BUTTON_XPATH = '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/div/svg'

    CLEAR_BUTTON_XPATH = "//*[@id='panel-filter-box']/div[2]/div[2]/div[1]/button[1]/span[1]"
    SELECTED_FILTER_XPATH = "//*[@id='panel-filter-box']/div[2]/div[2]/span[1]"

    FILTER_NAME = '//*[@id="__layout"]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/span[1]/b[1]'
    RENAME_BUTTON_XPATH = "//*[@class='el-popover el-popper pop-filter']/div/ul/li[1]/div"#最后一个svg未定位到
    DELETE_BUTTON_XPATH = "//*[@class=‘el-popover el-popper pop-filter’]/div/ul/li[1]/div"
    POP_DELETE_XPATH = "//button[contains(string(), '删除')]"
    POP_CANCEL_XPATH = "//button[contains(string(), '取消')]"
    POP_CLOSE_XPATH = "/html/body/div[14]/div[1]/div[1]/button[1]/i[1]"

    ADD_VIEW_BUTTON_XPATH = '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div[5]/div[1]/table/thead/tr/th[11]/div/button'

    pop_indicator_clear = '/html/body/div[13]/div[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/div[1]/div[1]/span[2]/span[1]/i[1]'
    pop_indicator_cancel = '/html/body/div[13]/div[1]/div[2]/div[1]/div[2]/button[1]'

    TOAST_SAVED_XPATH = '/html/body/div[2]'
    def __init__(self, page: Page):
        """
        初始化StockFiltersPage类实例。

        :param page: Playwright Page对象。
        """
        super().__init__(page)
        self.page.goto(STOCK_FILTERS_URL)

    def interact_with_element(self, locator, action):
        """
        与页面上的元素交互。

        :param locator: 元素定位器。
        :param action: 要执行的操作（'hover' 或 'click'）。
        :raises ValueError: 如果操作不支持。
        :raises Exception: 如果与元素交互时发生错误。
        """
        try:
            if action == 'hover':
                locator.hover()
            elif action == 'click':
                locator.click()
            else:
                raise ValueError(f"Unsupported action: {action}")
        except Exception as e:
            print(f"Error interacting with element: {e}")

    def select_market(self, market: str):
        """
        选择市场。

        :param market: 市场名称。
        :raises TimeoutError: 如果等待元素超时。
        :raises Exception: 如果选择市场时发生错误。
        """
        market_trigger_locator = self.page.locator(self.MARKET_TRIGGER_XPATH)
        self.interact_with_element(market_trigger_locator, 'hover')

        market_option_locator = self.page.locator(f"//li[contains(text(), '{market}')]")
        market_option_locator.wait_for(state='visible', timeout=10000)
        self.interact_with_element(market_option_locator, 'click')

    def select_exchange(self, exchange: str):
        """
        选择交易所。

        :param exchange: 交易所名称。
        :raises TimeoutError: 如果等待元素超时。
        :raises Exception: 如果选择交易所时发生错误。
        """
        market_locator = self.page.locator(self.EXCHANGE_TRIGGER_XPATH)
        self.interact_with_element(market_locator, 'hover')
        self.page.click(f'text={exchange}')

    def select_industry(self, industry: str):
        """
        选择行业。

        :param industry: 行业名称。
        :raises TimeoutError: 如果等待元素超时。
        :raises Exception: 如果选择行业时发生错误。
        """
        industry_locator = self.page.locator(self.INDUSTRY_TRIGGER_XPATH)
        self.interact_with_element(industry_locator, 'hover')
        self.page.click(f'text={industry}')

    def select_indicator(self, indicator_category: str, indicator_parameters: str):
        """
        选择指标。

        :param indicator_category: 指标类别。
        :param indicator_parameters: 指标参数。
        :raises TimeoutError: 如果等待元素超时。
        :raises Exception: 如果选择指标时发生错误。
        """
        self.page.click(f'text={indicator_category}')
        self.page.click(f'text={indicator_parameters}')

    def clear_filter(self):
        """
        清除筛选器。
        点击清除按钮
        """
        self.page.click(self.CLEAR_BUTTON_XPATH)

    def create_filter(self, name: str):
        """
        创建筛选器。

        :param name: 筛选器名称。
        :raises Exception: 如果创建筛选器时发生错误。
        """
        create_button_locator = self.page.locator(self.CREATE_BUTTON_XPATH)
        self.interact_with_element(create_button_locator, 'click')
        self.page.get_by_placeholder('请输入筛选器名称').fill(name)
        self.page.get_by_role('button', name='保存').click()

    def save_filter(self):
        """
        保存筛选器。

        :raises Exception: 如果保存筛选器时发生错误。
        """
        self.page.get_by_role('button', name='保存').click()

    def add_view(self):
        """
        添加视图。

        :raises Exception: 如果添加视图时发生错误。
        """
        add_view_button = self.page.locator(self.ADD_VIEW_BUTTON_XPATH)
        self.interact_with_element(add_view_button, 'click')

    def delete_filter(self):
        """
        删除筛选器。

        """
        filter_name = self.page.locator(self.FILTER_NAME)
        delete_button = self.page.locator(self.DELETE_BUTTON_XPATH)
        pop_delete = self.page.locator(self.POP_DELETE_XPATH)
        self.interact_with_element(filter_name, 'hover')
        self.interact_with_element(delete_button,'click')
        self.interact_with_element(pop_delete, 'click')

    def search_indicator(self, keyword: str):
        """
        搜索指标。

        :param keyword: 关键词。
        :raises Exception: 如果搜索指标时发生错误。
        """
        self.page.get_by_placeholder('请搜索指标名').fill(keyword)
        keyword_locator = self.page.locator("//div[contains(@class, 'el-popover') and contains(@class, 'panel-filter-content-footer-popper-search')]/div/div[2]/ul/li")
        self.interact_with_element(keyword_locator, 'click')

    def collect(self):
        """
        收藏。

        :raises Exception: 如果收藏时发生错误。
        """
        collect_button = self.page.locator(self.COLLECT_BUTTON_XPATH)
        self.interact_with_element(collect_button, 'click')


if __name__ == '__main__':

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # login_page = LoginPage(page)
        filters_page = StockFiltersPage(page)
        # filters_page.setup_stock_filters_page()
        filters_page.select_indicator('估值指标','<12')
        # selected_indicator = filters_page.page.locator(filters_page.SELECTED_FILTER_XPATH)
        # filters_page.clear_filter()
        filters_page.create_filter('测试')

        # toast_saved = filters_page.page.locator(filters_page.TOAST_SAVED_XPATH)
        #
        #
        # def wait_for_toast(page, selector, timeout=5000, interval=500):
        #     start_time = page.timeouts()['timeout']
        #     end_time = start_time + timeout
        #     while page.timeouts()['timeout'] < end_time:
        #         elements = page.query_selector_all(selector)
        #         if elements:
        #             return elements
        #         page.wait_for_timeout(interval)
        #     return None
        #
        #
        # toast_elements = wait_for_toast(filters_page, toast_saved)
        # if toast_elements:
        #     for toast in toast_elements:
        #         print("Toast内容:", toast.inner_text())
        #         # 这里可以添加更多操作，比如断言内容是否符合预期等
        # else:
        #     print("未找到Toast提示")

        # assert '<12' in filters_page.page.content(), f"指标 {'<12'} 未被正确选择"

        page.wait_for_timeout(20000)
