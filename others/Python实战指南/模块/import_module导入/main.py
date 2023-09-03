import importlib
# import_module函数适用于以下场景：动态生成Python代码文件后再导入当前代码上下文中。
dm=importlib.import_module('demo')
dm.happy()