import unittest
from Laba2_Task2 import MyJson
import json


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_json = MyJson()
        test = [True, False, 523, 43.21, {"Town": "Minsk", "aaa": 32}, [222, 111]]
        self.assertEqual(my_json.to_json(test), json.dumps(test))

    def test_1(self):
        my_json = MyJson()
        test = {"kek": 100}
        self.assertEqual(my_json.to_json(test), json.dumps(test))

    def test_2(self):
        my_json = MyJson()
        test = 100
        self.assertEqual(my_json.to_json(test), json.dumps(test))

    def test_3(self):
        my_json = MyJson()
        test = {"Town": "Minsk", "aaa": [32, "str"]}
        self.assertEqual(my_json.to_json(test), json.dumps(test))

if __name__ == '__main__':
    unittest.main()
