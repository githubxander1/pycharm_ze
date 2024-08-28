# import os
#
# print(os.path.dirname(__file__))
# print(os.path.basename(os.path.dirname(__file__)))
#
# import os
#
# def list_files(startpath):
#     for root, dirs, files in os.walk(startpath):
#         level = root.replace(startpath, '').count(os.sep)
#         indent = ' ' * 4 * (level)
#         print('{}{}/'.format(indent, os.path.basename(root)))
#         subindent = ' ' * 4 * (level + 1)
#         for f in files:
#             print('{}{}'.format(subindent, f))
#
# if __name__ == '__main__':
#     start_path = r'D:\1test\PycharmProject\CompanyProject\Fastbull\筛选器\PO_stockFilters'
#     list_files(start_path)
