import unittest
from Laba2_Task1 import Sort


class TestTask1(unittest.TestCase):
    def test_task1(self):
        test = Sort(2000, 1000, 'numbers.txt')
        self.assertTrue(self.check_file('Answer'))



    def check_file(self, name_file):
        cache = [];
        with open(name_file, 'r') as file:
            cache.append(file.readline())
            cache.append(1)
            for line in file:
                cache[1] = line
                cache = list(map(int, cache))
                if cache[0] > cache[1]:
                    return False
                else:
                    cache[0] = cache[1]
        return True

if __name__ == '__main__':
    unittest.main()

