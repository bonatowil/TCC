#(P1*V1) = (P2*V2)
# V = volume em litro
# P = Pressão em atm, mmHg ou Pa
# Eu nao tenho certeza de como esse codigo foi feito, favor nao mexer.

def boyle(p1=0, p2=0,v1=0,v2=0):
    if v1 == 0 and (v2 and p1 and p2) != 0:
        resultado = (v2 * p2) / p1
        return resultado
    elif v2 == 0 and (v1 and p1 and p2) != 0:
        resultado = (v1 * p1) / p2
        return resultado
    elif p1 == 0 and (v2 and v1 and p2) != 0:
        resultado = (v2 * p2) / p1
        return resultado
    elif p2 == 0 and (v2 and p1 and v1) != 0:
        resultado = (v1 * p1) / v2
        return resultado
    elif v1 and v2 and p1 and p2 != 0:
        return None
    elif (v1 and v2 and p1 and p2) == 0:
        return None    
    else:
        pass
        
    


if __name__ == "__main__":
    print(boyle())
