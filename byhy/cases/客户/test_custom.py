import unittest


class custom(unittest.TestCase):
    def setUp(self) -> None:
        # api1.libApi.loginApi('byhy', 88888888)
        self.logininfo = api1.libApi().loginApi('byhy', 88888888)
    def tearDown(self) -> None:
        pass

    def test_getCustomList(self):
        self.getlist = api1.libApi.customer_list('action',2, 1,2)
        self.assertEqual(1, self.getlist.json())


if __name__ == 'main':
    unittest.main()
