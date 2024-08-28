# LoginPage.py
from playwright.sync_api import Page, TimeoutError
from CompanyProject.Fastbull.筛选器.PO_stockFilters.page.BasePage import BasePage
from CompanyProject.Fastbull.筛选器.PO_stockFilters.config import LOGIN_URL


class LoginPage(BasePage):
    """
    LoginPage类用于处理登录流程。
    """
    def __init__(self, page: Page):
        """
        初始化LoginPage类实例。

        :param page: Playwright Page对象。
        """
        super().__init__(page)

    def login(self,email, password):
        """
        执行登录操作。

        :raises TimeoutError: 如果等待元素超时。
        :raises PlaywrightError: 如果页面导航失败。
        """
        try:
            # 导航到登录页面
            self.page.goto(LOGIN_URL)

            # 等待邮箱/ID文本出现
            self.page.wait_for_selector('text=邮箱/ID', timeout=10000)

            # 点击邮箱/ID文本
            self.page.click('text=邮箱/ID')

            # 填充邮箱
            self.page.fill('#inputMailText', email)

            # 填充密码
            self.page.fill('#inputMailPwd', password)

            # 点击登录按钮
            self.page.click('#mailBtn')
        except TimeoutError as e:
            # 这里可以记录日志，或者重抛异常，或者根据需要处理异常
            raise TimeoutError("等待元素超时。") from e
        except Exception as e:
            # 这里可以记录日志，或者重抛异常，或者根据需要处理异常
            raise RuntimeError("登录过程中发生错误。") from e


# if __name__ == '__main__':
#     # 初始化 Playwright
#     def main():
#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)
#             context = browser.new_context()
#             page = context.new_page()
#
#             # 创建 LoginPage 实例并登录
#             login_page = LoginPage(page)
#             login_page.login()
#
#     # 运行同步函数
#     main()
