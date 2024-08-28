import os
from bs4 import BeautifulSoup
from xmind import Workbook

def html_to_xmind(html_file, xmind_file):
    # 解析HTML文件
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    # 创建XMind工作簿
    workbook = Workbook()
    sheet = workbook.getPrimarySheet()

    # 递归函数来创建思维导图节点
    def create_nodes(parent_topic, element):
        topic = sheet.addTopic(element.text.strip() if element.text else '无标题', parent_topic)
        for child in element.children:
            if child.name and child.name != 'meta':
                create_nodes(topic, child)

    # 遍历HTML元素并创建思维导图节点
    root_topic = sheet.getRootTopic()
    for element in soup.body.children:
        if element.name and element.name != 'meta':
            create_nodes(root_topic, element)

    # 保存XMind文件
    workbook.save(xmind_file)

# 使用示例
html_file_path = 'path_to_your_html_file.html'
xmind_output_path = 'output.xmind'

if not os.path.exists(html_file_path):
    print(f"Error: HTML file '{html_file_path}' not found.")
else:
    html_to_xmind(html_file_path, xmind_output_path)
    print(f"Successfully created '{xmind_output_path}' from '{html_file_path}'.")

