import unittest
from my_romanos import decimal2roman
class MyTest(unittest.TestCase):
    def test_r(self):
        self.assertEqual(decimal2roman(1), "I")

if __name__ == "__main__":
    unittest.main()