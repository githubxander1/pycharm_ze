from pprint import pprint

import yaml


def readYaml(file):
    with open(file, 'r',encoding='utf-8') as f:
        yamldata =yaml.load(f,Loader=yaml.Loader)
        return yamldata
        # return list(yamldata)

def clearYaml(file):
    with open(file, 'w',encoding='utf-8') as f:
        f.truncate()






# pprint(readYaml())
# writeYaml({'/nname':'123'})
# pprint(writeYaml({'name':'123'}))
# import yaml


# def write_and_check_data(data):
#     # 写入数据
#     with open('../data/loginDataParameter.yaml', 'a', encoding='utf-8') as f:
#         yaml.dump(data)
#
#     # 重新打开并读取文件内容
#     with open('../data/loginDataParameter.yaml', 'r', encoding='utf-8') as f:
#         file_content = yaml.safe_load(f)
#         pprint(file_content)
#
#         # 遍历列表查找新添加的数据
#     found = False
#     for item in file_content:
#         if item == data:
#             found = True
#             break
#     # 假设你知道要检查的数据的具体结构和内容，进行断言
#     assert found, "Data not found in the YAML file."
#
#
# # 调用函数并传入待写入的数据
# some_data = {'name': '1231111111111'}
# write_and_check_data(some_data)
