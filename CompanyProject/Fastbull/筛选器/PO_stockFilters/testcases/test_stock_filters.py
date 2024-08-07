import pytest
from playwright.sync_api import sync_playwright
from CompanyProject.Fastbull.筛选器.PO_stockFilters.page.LoginPage import LoginPage
from CompanyProject.Fastbull.筛选器.PO_stockFilters.page.StockFiltersPage import StockFiltersPage
from CompanyProject.Fastbull.筛选器.PO_stockFilters.config import EMAIL, PASSWORD

@pytest.fixture(scope="module")
def setup_and_teardown():
    """
    同步 fixture，用于设置和清理测试环境。
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})

        login_page = LoginPage(page)
        stock_filters_page = StockFiltersPage(page)

        # 完成登录操作
        login_page.login(EMAIL, PASSWORD)


        try:
            yield stock_filters_page, login_page
        finally:
            page.wait_for_timeout(1000)
            # 这里不需要关闭浏览器和页面，因为作用域为 "module"
            page.close()
            context.close()
            browser.close()

@pytest.mark.skip
def test_create_filter(setup_and_teardown):
    """
    测试创建筛选器。
    """
    stock_filters_page,_ = setup_and_teardown

    stock_filters_page.select_indicator('市场定级', "<5000万")
    # 创建筛选器
    stock_filters_page.create_filter("测试新建1")
    stock_filters_page.screen_shot("test_create_filter.png")


    # toast_saved = stock_filters_page.page.locator('/html/body/div[2]')

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
    # toast_elements = wait_for_toast(stock_filters_page, toast_saved)
    # if toast_elements:
    #     for toast in toast_elements:
    #         print("Toast内容:", toast.inner_text())
    #         # 这里可以添加更多操作，比如断言内容是否符合预期等
    # else:
    #     print("未找到Toast提示")
    # 验证筛选器是否被正确创建
    # assert "TestFilter" in stock_filters_page.page.content(), "筛选器未被正确创建"

@pytest.mark.skip
def test_clear_filter(setup_and_teardown):
    """
    测试清除筛选器。
    """
    stock_filters_page,_ = setup_and_teardown
    stock_filters_page.select_indicator("市场定级", "<5000万")
    stock_filters_page.clear_filter()
    selected_indicators = stock_filters_page.page.locator("//*[@id='panel-filter-box']/div[2]/div[2]/span[1]").all_text_contents()
    print(selected_indicators)
    assert selected_indicators not in stock_filters_page.page.content(), "筛选器未被正确清除"
@pytest.mark.skip
@pytest.mark.parametrize("market", ["越南股", "美股"])
def test_select_market(setup_and_teardown, market):
    """
    测试选择市场。
    """
    stock_filters_page,_ = setup_and_teardown

    # 选择市场
    stock_filters_page.select_market(market)

    # 验证市场是否被正确选择
    assert market in stock_filters_page.page.content(), f"市场 {market} 未被正确选择"

@pytest.mark.skip
@pytest.mark.parametrize('market, exchange', [
    ("越南股", "HOSE"),
    ("越南股", "HNX"),
    ("越南股", "UPCOM"),
    ("美股", "纳斯达克"),
    ("美股", "纽交所"),
    ("美股", "美交所"),
])
def test_select_exchange(setup_and_teardown, market, exchange):
    """
    测试选择交易所。
    """
    stock_filters_page,_ = setup_and_teardown

    # 选择市场
    stock_filters_page.select_market(market)

    # 选择交易所
    stock_filters_page.select_exchange(exchange)

    # 验证交易所是否被正确选择
    assert exchange in stock_filters_page.page.content(), f"交易所 {exchange} 未被正确选择"

@pytest.mark.skip
def test_select_industry(setup_and_teardown):
    """
    测试选择行业。
    """
    stock_filters_page,_ = setup_and_teardown

    # 选择行业
    stock_filters_page.select_industry("金融")

    # 验证行业是否被正确选择
    assert "金融" in stock_filters_page.page.content(), "行业未被正确选择"

# @pytest.mark.skip
@pytest.mark.parametrize("indicator_category, indicator_parameters", [
    ('市场定级','<5000万'),
    ('估值指标','<12'),
     ('权益指标','<30%'),
     ('盈利指标','<0%'),
     ('债务指标','<0.5'),
     ('量价指标','>50%'),
    ('技术指标','>70%')
     ])
def test_select_indicator(setup_and_teardown, indicator_category, indicator_parameters):
    """
    测试选择指标。
    """
    stock_filters_page,_ = setup_and_teardown
    stock_filters_page.select_indicator(indicator_category, indicator_parameters)
    assert indicator_parameters in stock_filters_page.page.content(), f"指标 {indicator_parameters} 未被正确选择"




if __name__ == '__main__':
    pytest.main()
