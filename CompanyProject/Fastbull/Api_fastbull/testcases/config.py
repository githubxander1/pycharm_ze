#多环境配置
class Config:
    """多套环境的公共配置"""
    version = "v1.0"


class TestConfig(Config):
    """测试环境"""
    BASE_URL = 'http://192.168.1.1:8000'
    MYSQL_HOST = "192.168.1.1"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_PORT = 3306
    MYSQL_DATABASE = "xxx"   # 连接数据的库名


class UatConfig(Config):
    """联调环境"""
    BASE_URL = 'http://192.168.1.3:8080'
    MYSQL_HOST = "http://192.168.1.3"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "654321"
    MYSQL_PORT = 3306
    MYSQL_DATABASE = "xxx"  # 连接数据的库名


# 环境关系映射，方便切换多环境配置
env = {
    "flashing_icon": TestConfig,
    "uat": UatConfig
}
