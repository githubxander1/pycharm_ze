# 在处理之前，token灵魂三连问：
#
# 如何获取token？
#
# 获取的token如何管理？
#
# 其他接口如何携带token？
# 
#
# 思路如下：
#
# 1.抽取登录接口返回值中的token；
#
# 2.使用全局变量存储token。token可以存到yaml或者json或者ini的配置文件里，以下介绍将token作为类属性；
#
# 3.其他接口将token值放入请求头，发送请求；