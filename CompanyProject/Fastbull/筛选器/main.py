import asyncio
from playwright.async_api import async_playwright

from CompanyProject.Fastbull.筛选器.LoginPage import LoginPage
from CompanyProject.Fastbull.筛选器.StockFiltersPage import StockFiltersPage


# from pages.LoginPage import LoginPage
# from pages.StockFiltersPage import StockFiltersPage

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        login_page = LoginPage(page)
        await login_page.goto('https://testfb.tostar.top/cn/login?next=https://testfb.tostar.top/cn/signal/user-j32w0yel4v/account')
        await login_page.login('7@qq.com', 'a1234567')

        await page.wait_for_timeout(2000)
        stock_filters_page = StockFiltersPage(page)
        await stock_filters_page.goto('https://testfb.tostar.top/cn/signal/stockFilters')
        await stock_filters_page.set_viewport_size({'width': 1920, 'height': 1080})
        await page.wait_for_timeout(1000)
        await stock_filters_page.select_market()
        await page.wait_for_timeout(1000)
        await stock_filters_page.select_exchange()
        await page.wait_for_timeout(1000)
        await stock_filters_page.select_industry()

        await stock_filters_page.select_indicator()
        await stock_filters_page.save_filter('筛选器2')
        await stock_filters_page.collect()
        await stock_filters_page.add_view()
        await stock_filters_page.search_indicator('市值')

        await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(main())
