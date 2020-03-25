import unittest
from Laba2_Task3 import Vector


class MyTestCase(unittest.TestCase):

    def test_sum(self):
        vec1 = Vector([-3, 4, 5, 10])
        vec2 = Vector([0, 7, 2, 3])
        self.assertEqual(vec1.sum(vec2), '-3, 11, 7, 13')

    def test_sub(self):
        vec1 = Vector([-3, 4, 5, 10])
        vec2 = Vector([0, 7, 2, 3])
        self.assertEqual(vec1.sub(vec2), '-3, -3, 3, 7')

    def test_mul_const(self):
        vec1 = Vector([-3, 4, 5, 10])
        self.assertEqual(vec1.mul_const(2), '-6, 8, 10, 20')

    def test_mul_scal(self):
        vec1 = Vector([-3, 4, 5, 10])
        vec2 = Vector([0, 7, 2, 3])
        self.assertEqual(vec1.mul_scal(vec2), 68)

    def test_mul_compare_false(self):
        vec1 = Vector([-3, 4, 5, 10])
        vec2 = Vector([0, 7, 2, 3])
        self.assertFalse(vec1.compare(vec2))

    def test_mul_compare_true(self):
        vec1 = Vector([-3, 4, 5, 10])
        self.assertTrue(vec1.compare(vec1))

    def test_lenght(self):
        vec1 = Vector([2, 2, 2, 2])
        self.assertEqual(vec1.len(), 4)


if __name__ == '__main__':
    unittest.main()
