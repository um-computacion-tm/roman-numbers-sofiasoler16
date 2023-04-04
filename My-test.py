import unittest

from my_romanos import entero
from my_romanos import unidadestorom
from my_romanos import dectorom
from my_romanos import centtorom

class TestDecimalToRoman(unittest.TestCase):
    def test_partedeunidades (self):
        resultado = unidadestorom("3")
        self.assertEqual(resultado, "III")
    def test_partededecenas (self):
        resultado = dectorom("20")
        self.assertEqual(resultado, "XX")
    def test_partedecentenas (self):
        resultado = centtorom("300")
        self.assertEqual(resultado, "CCC")
    def test_entero1 (self):
        resultado = entero("1")
        self.assertEqual(resultado, "I")
    def test_entero500 (self):
        resultado = entero("500")
        self.assertEqual(resultado, "D")
    def test_entero4 (self):
        resultado = entero("4")
        self.assertEqual(resultado, "IV")
    def test_entero9 (self):
        resultado = entero("9")
        self.assertEqual(resultado, "IX")
    def test_entero250 (self):
        resultado = entero("250")
        self.assertEqual(resultado, "CCL")
    def test_entero57 (self):
        resultado = entero("57")
        self.assertEqual(resultado, "LVII")
    def test_entero999 (self):
        resultado = entero("999")
        self.assertEqual(resultado, "CMXCIX")
    
    
if __name__ == "__main__":
    unittest.main()

