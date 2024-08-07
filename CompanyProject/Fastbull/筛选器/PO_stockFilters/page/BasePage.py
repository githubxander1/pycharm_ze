from playwright.sync_api import Page, Error as PlaywrightError


class BasePage:
    """
    BasePage类提供了与Page对象交互的基本方法，包括转到特定URL和设置视口大小。
    """
    def __init__(self, page: Page):
        """
        初始化BasePage类实例。

        :param page: Playwright Page对象。
        """
        self.page = page

    def goto(self, url: str):
        """
        导航到指定的URL。

        :param url: 要导航的URL字符串。
        :raises PlaywrightError: 如果导航失败。
        """
        try:
            self.page.goto(url)
        except PlaywrightError as e:
            # 这里可以记录日志，或者重抛异常，或者根据需要处理异常
            raise RuntimeError(f"导航到 {url} 失败。") from e

    def set_viewport_size(self, size: dict):
        """
        设置视口大小。注意，字典必须包含'width'和'height'键。

        :param size: 包含视口宽度和高度的字典（例如 {'width': 1920, 'height': 1080}）。
        :raises ValueError: 如果字典不包含'width'或'height'键。
        :raises PlaywrightError: 如果设置视口大小失败。
        """
        # 验证输入
        if 'width' not in size or 'height' not in size:
            raise ValueError("设置视口大小的字典必须包含'width'和'height'键。")

        # 这里假设宽度和高度的合理范围为正整数。
        if not (isinstance(size['width'], int) and size['width'] > 0) or not (isinstance(size['height'], int) and size['height'] > 0):
            raise ValueError("视口宽度和高度必须是正整数。")

        try:
            self.page.set_viewport_size(size)
        except PlaywrightError as e:
            # 这里可以记录日志，或者重抛异常，或者根据需要处理异常
            raise RuntimeError("设置视口大小失败。") from e

    def click(self, selector: str):
        """
        点击指定的选择器。

        :param selector: 选择器。
        """
        self.page.click(selector)

    def fill(self, selector: str, value: str):
        """
        填充指定的选择器。

        :param selector: 选择器。
        :param value: 填充的值。
        """
        self.page.fill(selector, value)


    def screen_shot(self, filename):
        """
        截图并保存到指定路径。
        """
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_load_state("load")
        self.page.screenshot(path=filename, full_page=True)
        # self.page.screenshot(path=path)
        # return path
