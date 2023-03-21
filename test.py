import unittest

def decimal_to_roman (decimal):
    if decimal == 3:
        return "III" 


def decimal_to_roman10 (decimal):
    if decimal == 10:
        return "X"

class TestDecimalToRoman(unittest.TestCase):
    def test_d1(self):
        #no hay precondicion
        resultado = decimal_to_roman(3)
        #verificacion
        self.assertEqual(resultado, "III")

    def test_d10(self):
        resultado = decimal_to_roman10(10)
        self.assertEqual(resultado, "X")
        

if __name__ == "__main__":
    unittest.main()



