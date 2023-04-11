from others.PO_test.POtest_wechat.page.index import Index


class TestIndex:
    # 所有步骤前的初始化
    def setup(self):
        self.index = Index()

    # 对注册功能的测试
    def test_register(self):
        # 进入index，然后进入注册页填写信息
        self.index.goto_register().register("霍格沃兹测试学院")

    # 对login功能的测试
    def test_login(self):
        # 从首页进入到注册页
        register_page = self.index.goto_login().goto_registry()\
            .register("测吧（北京）科技有限公司")
        # 对填写结果进行断言，是否填写成功或者填写失败
        assert "请选择" in "|".join(register_page.get_error_message())
    # 关闭driver
    def teardown(self):
        self.index.close()