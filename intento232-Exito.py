import unittest

#detecta la unidad y busca el equivalente en romano
def unidadestorom (decim):
    unid1 = { "":"", "0":"", "1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}
    if len (decim) >= 1:
        unidades = decim [-1]
        for part, uni in unid1.values():
            if part == unidades:
                
                return uni

#detecta la decena y busca el equivalente en romano
def dectorom (decim):
    dece10 = {"":"","0":"", "1":"X", "2":"XX", "3":"XXX", "4":"XL", "5":"L", "6":"LX", "7":"LXX", "8":"LXXX", "9":"XC"}
    #escribi el numero solo y no la decena para que pueda detectar el num de la decena solo
    if len (decim) >= 2: 
        decena = decim [-2]
        for clave, dece in dece10.items():
            if clave == decena:
                
                return dece

#detecta la centena y busca el equivalente en romano
def centtorom (decim):
    c100 = {"":"", "0":"","1":"C", "2":"CC", "3":"CCC", "4":"CD", "5":"D", "6":"DC", "7":"DCC", "8":"DCCC", "9":"CM"}
    if len (decim) >= 3:
        centena = decim [-3]
        for clave, cent in c100.items():
            if clave == centena:
                
                return cent

#suma al revez las respuestas para formar el numero

def entero (decim):
    if len (decim) >= 3:
        c = centtorom (decim) + dectorom (decim) + unidadestorom (decim) 
        return c
    elif len (decim) >= 2:
        c = dectorom (decim) + unidadestorom (decim) 
        return c
    elif len (decim) >= 1:
        c = unidadestorom (decim)
        return (c)




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

