from page.index import Index


class TestBaidu:
    # setup中实例化百度首页
    def setup(self):
        self.index = Index()

    # 登录成功测试
    def test_login_success(self):
        login = self.index.goto_login()
        login.login_success()
        self.index.teardown()

    # 登录失败测试
    def test_login_fail(self):
        login = self.index.goto_login()
        login.login_fail()
        assert "用户名或密码有误，请重新输入或" in login.get_error_message()
        self.index.teardown()

    # 注册测试
    def test_register(self):
        self.index.goto_login().goto_register().register()
        self.index.teardown()

    # 搜索测试
    def test_search(self):
        self.index.goto_search()
        self.index.teardown()
