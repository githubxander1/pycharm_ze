
from playwright.sync_api import sync_playwright

# 更多
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto('https://www.baidu.com')
#     page.wait_for_timeout(2000)
#     dropdown = page.wait_for_selector("//*[@name='tj_briicon']")
#     dropdown.hover()
#     page.wait_for_timeout(2000)
#     page.wait_for_selector("//*[@name='tj_mp3']").click()
#     page.wait_for_timeout(5000)
#     page.pause()

with sync_playwright() as p:
   browser = p.chromium.launch(headless=False)
   context = browser.new_context(viewport={'width': 1928, 'height': 1080 })
   page = context.new_page()
   page.goto("https://wwww.baidu.com")
   page.wait_for_timeout(3000)
   page.fill("input[name=\"wd\"]", "selenium ap")
   page.wait_for_timeout(3000)
   #自动补全其中一个选择项
   auto_text = page.locator("//*[@id='form'J/div/ul/li[@data-key='selenium appium']").click()
   page.wait_for_timeout(3000)
   page.click("text=百度一下")
   context.close()
   browser.close()