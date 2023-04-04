#DE DECIMAL A ROMANO

#detecta la unidad y busca el equivalente en romano
def unidadestorom (decim):
    unid1 = { "":"", "0":"", "1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}
    if len (decim) >= 1:
        unidades = decim [-1]
        for part, uni in unid1.items():
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
    
#DE ROMANO A DECIMAL

def romantodecimal (numero):
    letra = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}
    num = []
    
    for c in numero[::-1]:
        for v, x in letra.items():
            if c == v:
                num.append(x)
    for d in range(len(num)-1):
        if num[d+1] < num[d]:
            resta = num[d] - num[d+1]
            num.append(resta)
    if 4 in num:
        num.remove(5)
        num.remove(1)
    if 9 in num:
        num.remove(10)
        num.remove(1)
    if 40 in num:
        num.remove(50)
        num.remove(10)
    if 90 in num:
        num.remove(100)
        num.remove(10)
    if 400 in num:
        num.remove (500)
        num.remove (100)
    if 900 in num:
        num.remove (1000)
        num.remove (100)

    resp = sum(num) 
    return resp



if __name__ == "__main__":
    print(entero(2))