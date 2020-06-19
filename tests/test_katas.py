import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(10, 5), 15)
        self.assertEqual(katas.add(-1, 1), 0)
        self.assertEqual(katas.add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(katas.multiply(3, 5), 15)
        self.assertEqual(katas.multiply(5, 10), 50)
        self.assertEqual(katas.multiply(-1, -1), 1)

    def test_power(self):
        self.assertEqual(katas.power(3, 5), 243)
        self.assertEqual(katas.power(5, 10), 9765625)
        self.assertEqual(katas.power(-1, -1), 1)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(3), 6)
        self.assertEqual(katas.factorial(-1), None)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(5), 5)
        self.assertEqual(katas.fibonacci(3), 2)
        self.assertEqual(katas.fibonacci(-1), None)


if __name__ == '__main__':
    unittest.main()
