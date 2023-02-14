#(V1/T1) = (V2/T2)
# V = volume em litro
# T = temperatura em kelvin
# Eu nao tenho certeza de como esse codigo foi feito, favor nao mexer.

def gay_lussac(v1=0, v2=0,t1=0,t2=0):
    if v1 == 0 and (v2 and t1 and t2) != 0:
        resultado = (v2 * t1) / t2
        return resultado
    elif v2 == 0 and (v1 and t1 and t2) != 0:
        resultado = (v1 * t2) / t1
        return resultado
    elif t1 == 0 and (v2 and v1 and t2) != 0:
        resultado = (v1 * t2) / v2
        return resultado
    elif t2 == 0 and (v2 and t1 and v1) != 0:
        resultado = (v2 * t1) / v1
        return resultado
    elif v1 and v2 and t1 and t2 != 0:
        return None
    elif (v1 and v2 and t1 and t2) == 0:
        return None    
    else:
        pass
        
    


if __name__ == "__main__":
    print(gay_lussac())
