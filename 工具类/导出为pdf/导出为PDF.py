import os
import pdfkit
from jinja2 import Environment, FileSystemLoader

def read_files_in_dir(directory):
    """ 递归读取目录下所有文件的内容 """
    result = []
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        # 将目录名和空字符串作为一个元组添加
        result.append((f"{indent}{'-' * level} {os.path.basename(root)}/", ""))
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            filepath = os.path.join(root, f)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    # 将文件名和内容作为一个元组添加
                    result.append((f"{sub_indent}{'-' * (level+1)} {f}:", content))
            except Exception as e:
                # 当文件无法读取时，将文件名和错误消息作为一个元组添加
                result.append((f"{sub_indent}{'-' * (level+1)} {f}: [无法读取文件]", ""))
    return result

def create_html_template(content):
    """ 创建HTML模板并填充内容 """
    env = Environment(loader=FileSystemLoader('..'))
    template = env.get_template('template.html')
    html_content = template.render(content=content)
    return html_content

if __name__ == "__main__":
    # 要导出的文件夹路径
    directory = r'D:\1test\PycharmProject\others\项目实战\局域网文件互传'
    content = read_files_in_dir(directory)

    # 创建HTML模板
    html_content = create_html_template(content)

    # 生成PDF
    output_file = os.path.join(r'D:\1test\PycharmProject\others\项目实战\局域网文件互传', '局域网output.pdf')
    pdfkit.from_string(html_content, output_file, options={
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
    })

    print(f"PDF has been created at {output_file}")