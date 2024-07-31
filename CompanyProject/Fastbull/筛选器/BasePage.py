from playwright.async_api import Page, ElementHandle

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def goto(self, url: str):
        await self.page.goto(url)

    async def set_viewport_size(self, size: dict):
        await self.page.set_viewport_size(size)
