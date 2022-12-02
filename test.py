import unittest
from summa import sum_digits


class TestSum(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(TypeError):
            sum_digits('')

    def test_str(self):
        with self.assertRaises(TypeError):
            sum_digits('qwerty')

    def test_float(self):
        with self.assertRaises(TypeError):
            sum_digits('132.5')

if __name__ == '__summa__':
    unittest.summa()
    unittest.summa()
