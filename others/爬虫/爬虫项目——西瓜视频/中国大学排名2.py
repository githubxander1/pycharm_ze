import time

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
wait = WebDriverWait(browser, 30)
# 导入必要的异常类
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

# 初始化时找到并等待下一页按钮可点击
# next_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content-box"]/ul/li[9]/a/i')))
count=0
while True:
    # 点击下一页
    # next_page_button.click()

    # 等待页面更新
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, '//tbody/tr'))
    )

    # 获取当前页的表格数据
    school_list = browser.find_elements(By.XPATH, '//tbody/tr')

    # 处理每一页的数据
    for school in school_list:
        # 提取数据
        cn_name = school.find_element(By.XPATH, './/a[@class="name-cn"]').text.strip()
        en_name = school.find_element(By.XPATH, './/a[@class="name-en"]').text.strip()
        tag_element = None

        try:
            tag_element = school.find_element(By.XPATH, './/p[@class="tags"]')
        except NoSuchElementException:
            pass

        address = school.find_element(By.XPATH, './td[3]').text.strip()
        ranking = school.find_element(By.XPATH, './/div[contains(@class,"ranking")]').text.strip()
        score = school.find_element(By.XPATH, './td[5]').text.strip()

        # 处理数据（打印或保存）
        output_info = f"中文名：{cn_name}, 英文名：{en_name}, 地址：{address}, 排名：{ranking}, 分数：{score}"

        if tag_element:
            tags = tag_element.text.strip()
            output_info += f", 标签：{tags}"

        print(output_info)

    # 打印完成信息
    print("当前页数据爬取完成，准备切换到下一页...")
    count += 1
    print(f"总共已爬取{count}页数据...")

    # 检查是否是最后一页，如果不是则继续
    try:

        # 依次查找三个可能存在的下一页按钮，并点击存在的那个
        for xpath_expression in [
            '//*[@id="content-box"]/ul/li[9]/a/i',
            '//*[@id="content-box"]/ul/li[10]/a/i',
            '//*[@id="content-box"]/ul/li[11]/a/i'
        ]:
            try:
                next_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
                next_page_button.click()
                # return xpath_expression
                break  # 找到并点击后，跳出循环
            except NoSuchElementException:
                # pass  # 如果元素未找到，则忽略此异常并继续尝试下一个表达式
                print(f'当前xpath对应的元素不存在或已失效，则尝试下一个{xpath_expression}')  # 当前xpath对应的元素不存在或已失效，则尝试下一个
                pass
    except (NoSuchElementException, StaleElementReferenceException):
        # 如果找不到下一页按钮或者元素过时，结束循环
        print("已到达最后一页，停止抓取...")
        break
