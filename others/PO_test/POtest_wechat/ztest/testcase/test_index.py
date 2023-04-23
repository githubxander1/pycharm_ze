from others.PO_test.POtest_wechat.ztest.page.index import Index


class TestIndex:

    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_register().regester('zhuce')

    def test_login(self):
        self.index.goto_login().goto_regester().regester('测试')
        assert '请选择' in '|'.join('fd')


