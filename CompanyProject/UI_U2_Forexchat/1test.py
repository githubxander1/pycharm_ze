import unittest
import yaml


class InputBoxTest(unittest.TestCase):
    def load_test_cases(self):
        with open('1testdata.yaml','r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return data['test_cases']

    def test_input_box(self):  # 注意这里不再需要你传入test_cases参数了
        for test in self.load_test_cases():
            name = test['name']
            value = test['value']
            expected = test['expected']
            with self.subTest(name):
                # 在这里执行输入框的测试逻辑，根据实际需求进行断言判断
                # 这里只是一个示例，你可以根据实际情况进行调整
                result = print(test)  # 假设input_box是你要测试的输入框函数
                # self.assertEqual(result, expected, f"Test case '{name}' failed")


if __name__ == '__main__':
    test_cases = InputBoxTest().load_test_cases()
    unittest.main()