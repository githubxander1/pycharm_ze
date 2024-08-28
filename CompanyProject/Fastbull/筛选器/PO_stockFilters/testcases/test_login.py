
import os
import pytest
from playwright.sync_api import sync_playwright
from CompanyProject.Fastbull.筛选器.PO_stockFilters.page.LoginPage import LoginPage
from CompanyProject.Fastbull.筛选器.PO_stockFilters.page.StockFiltersPage import StockFiltersPage
from CompanyProject.Fastbull.筛选器.PO_stockFilters.config import EMAIL, PASSWORD

# 推荐从环境变量获取敏感信息，增加安全性
EMAIL = os.getenv("TEST_EMAIL", EMAIL)
PASSWORD = os.getenv("TEST_PASSWORD", PASSWORD)

@pytest.fixture(scope="module")
def setup_and_teardown():
    """
    同步 fixture，用于设置和清理测试环境。
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login_page = LoginPage(page)
        stock_filters_page = StockFiltersPage(page)

        try:
            yield login_page, stock_filters_page
        finally:
            page.close()
            context.close()
            browser.close()

# 使用参数化测试，简化测试用例的编写
@pytest.mark.parametrize("test_case", [
    {"description": "使用无效邮箱登录", "email": "invalid-email@example.com", "password": "password123", "expected_error": "您还没注册账号，请先创建账号"},
    {"description": "使用无效密码登录", "email": EMAIL, "password": "wrongpassword", "expected_error": "密码为6-20位，含数字/字母/字符至少两种组合"},
    {"description": "使用错误密码登录", "email": EMAIL, "password": "a123456", "expected_error": "账号或密码错误"}
    # {"description": "正确的账密，登录成功", "email": EMAIL, "password": PASSWORD}
],ids = lambda tc: tc["description"]) # 添加ids参数，自定义测试用例名称
def test_login(setup_and_teardown, test_case):
    """
    测试使用无效的登录凭据登录。
    """
    login_page, _ = setup_and_teardown

    # 执行登录
    login_page.login(email=test_case["email"], password=test_case["password"])
    login_page.page.wait_for_timeout(1000)
    error_message_selector = login_page.page.locator("//*[@id='mailLgoin']/div[3]/div[1]/span[1]").text_content()
    print(error_message_selector)

    # 验证错误信息
    assert  error_message_selector == test_case["expected_error"], f"{test_case['description']}失败"
    print(f"{test_case['description']}，断言符合预期")


if __name__ == '__main__':
    pytest.main()
