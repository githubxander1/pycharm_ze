from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置webdriver路径和选项
driver_path = 'path/to/your/webdriver'  # 比如： driver_path = '/usr/bin/chromedriver'
browser = webdriver.Chrome()

# 访问页面
browser.get('https://www.shanghairanking.cn/rankings/bcur/2023')

# 等待元素加载
wait = WebDriverWait(browser, 10)
# 导入必要的异常类
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

# 初始化时找到并等待下一页按钮可点击
next_page_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ant-pagination-item-link')))

while True:
    # 点击下一页
    # next_page_button.click()

    # 等待页面更新
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//tbody/tr'))
    )

    # 获取当前页的表格数据
    school_list = browser.find_elements(By.XPATH, '//tbody/tr')

    # 处理每一页的数据
    for school in school_list:
        # 提取数据
        cn_name = school.find_element(By.XPATH, './/a[@class="name-cn"]').text.strip()
        en_name = school.find_element(By.XPATH, './/a[@class="name-en"]').text.strip()
        tags = school.find_element(By.XPATH, './/p[@class="tags"]').text.strip()
        address = school.find_element(By.XPATH, './td[3]').text.strip()
        ranking = school.find_element(By.XPATH, './/div[contains(@class,"ranking")]').text.strip()
        score = school.find_element(By.XPATH, './td[5]').text.strip()

        # 处理数据（打印或保存）
        print(f"中文名：{cn_name}, 英文名：{en_name}, 标签：{tags}, 地址：{address}, 排名：{ranking}, 分数：{score}")
        # print('-' * 10)

    # 打印完成信息
    print("当前页数据爬取完成，准备切换到下一页...")

    # 检查是否是最后一页，如果不是则继续
    try:
        # 重新查找下一页按钮以确保它仍然存在
        next_page_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ant-pagination-item-link')))
        next_page_button.click()

        # 确保等待下一页加载完成
        # WebDriverWait(browser, 10).until_not(
        #     EC.presence_of_element_located((By.CLASS_NAME, 'loading-indicator'))  # 假设有一个类名为'loading-indicator'的加载指示器
        # )
    except (NoSuchElementException, StaleElementReferenceException):
        # 如果找不到下一页按钮或者元素过时，结束循环
        print("已到达最后一页，停止抓取...")
        break
