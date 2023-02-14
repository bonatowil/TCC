#(P*V) = (n*R*T)
# P = Pressao em atm, mmHg ou Pa
# V = Volume em litros
# n = Numero de mols (massa/massa molar)
# R = Constante Universal dos gases ideais{
# atm = 0,082
# mmHg = 62,3
# Pa = 8,314}
# T = Temperatura em Kelvin
# Eu nao tenho certeza de como esse codigo foi feito, favor nao mexer.

def clapeyron(constante="mmHg", p=0, v=0, n=0, r=0, t=0):
                                      #variavel a ser feita
    if constante == "Pa":                 #const sera a varaiavel recebida pelo GUI 
        r = 8.314 
    if constante == "atm":
        r = 0.082
    if constante == "mmHg":
        r = 62.3
    if constante == None:
        pass
    if p == 0 and (v and n and t) != 0:
        resultado = (n * r * t) / v
        return resultado
    elif v == 0 and (p and n and t) != 0:
        resultado = (n * r * t) / p
        return resultado
    elif n == 0 and (p and v and t) != 0:
        resultado = (p * v) / (r * t)
        return resultado
    elif t == 0 and (p and v and n) != 0:
        resultado = (p * v) / (n * r)
        return resultado
    elif p and v and n and t != 0:
        return None
    elif (p and v and n and t) == 0:
        return None    
    else:
        pass
        
    


if __name__ == "__main__":
    print(clapeyron(constante="atm",p=3,v=1,r=10))
