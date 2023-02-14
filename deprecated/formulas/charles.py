#(P1/T1) = (P2/T2)
# P = volume em litro
# T = temperatura em kelvin
# Eu nao tenho certeza de como esse codigo foi feito, favor nao mexer.

def charles(p1=0, p2=0,t1=0,t2=0):
    if p1 == 0 and (p2 and t1 and t2) != 0:
        resultado = (p2 * t1) / t2
        return resultado
    elif p2 == 0 and (p1 and t1 and t2) != 0:
        resultado = (p1 * t2) / t1
        return resultado
    elif t1 == 0 and (p2 and p1 and t2) != 0:
        resultado = (p1 * t2) / p2
        return resultado
    elif t2 == 0 and (p2 and t1 and p1) != 0:
        resultado = (p2 * t1) / p1
        return resultado
    elif p1 and p2 and t1 and t2 != 0:
        return None
    elif p1 and p2 and t1 and t2 == 0:
        return None        
    else:
        pass
        
    


if __name__ == "__main__":
    print(charles())
