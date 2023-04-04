import unittest

from my_romanos import entero
from my_romanos import unidadestorom
from my_romanos import dectorom
from my_romanos import centtorom
from my_romanos import romantodecimal
#TEST DE DECIMAL A ROMANO

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


#TEST DE ROMANO A DECIMAL

    def test_r1(self):
        resp= romantodecimal("I")
        self.assertEqual(resp, 1)
    def test_r4(self):
        resp= romantodecimal("IV")
        self.assertEqual(resp, 4)
    def test_r5(self):
        resp= romantodecimal("V")
        self.assertEqual(resp, 5)
    def test_r9(self):
        resp= romantodecimal("IX")
        self.assertEqual(resp, 9)
    def test_r15(self):
        resp= romantodecimal("XV")
        self.assertEqual(resp, 15)
    def test_r34(self):
        resp= romantodecimal("XXXIV")
        self.assertEqual(resp, 34)
    def test_r90(self):
        resp= romantodecimal("XC")
        self.assertEqual(resp, 90)
    def test_r106(self):
        resp= romantodecimal("CVI")
        self.assertEqual(resp, 106)
    def test_r129(self):
        resp= romantodecimal("CXXIX")
        self.assertEqual(resp, 129)
    def test_r180(self):
        resp= romantodecimal("CLXXX")
        self.assertEqual(resp, 180)
    def test_r182(self):
        resp= romantodecimal("CLXXXII")
        self.assertEqual(resp, 182)
    def test_r190(self):
        resp= romantodecimal("CXC")
        self.assertEqual(resp, 190)
    def test_r390(self):
        resp= romantodecimal("CCCXC")
        self.assertEqual(resp, 390)
    def test_r499(self):
        resp= romantodecimal("CDXCIX")
        self.assertEqual(resp, 499)
    def test_r579(self):
        resp= romantodecimal("DLXXIX")
        self.assertEqual(resp, 579)
    def test_r750(self):
        resp= romantodecimal("DCCL")
        self.assertEqual(resp, 750)
    def test_r900(self):
        resp= romantodecimal("CM")
        self.assertEqual(resp, 900)
    def test_r999(self):
        resp= romantodecimal("CMXCIX")
        self.assertEqual(resp, 999)
    def test_r1352(self):
        resp= romantodecimal("MCCCLII")
        self.assertEqual(resp, 1352)
if __name__ == "__main__":
    unittest.main()

