from .BasePage import BasePage
from playwright.sync_api import Page
class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def login(self, email: str, password: str):
        await self.page.wait_for_selector('text=邮箱/ID')
        await self.page.click('text=邮箱/ID')
        await self.page.fill('#inputMailText', email)
        await self.page.fill('#inputMailPwd', password)
        await self.page.click('#mailBtn')
