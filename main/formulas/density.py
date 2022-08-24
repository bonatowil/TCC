#d = m  / V
# V = volume
# m = massa
# d = densidade

def density(d=1.66,m=150,v=0):
    if v == 0 and (d and m) != 0:
        resultado = m / d
        return resultado
    elif m == 0 and (v and d) != 0:
        resultado = d * v
        return resultado
    elif d == 0 and (v and m) != 0:
        resultado = m / v
        return resultado
    elif d and m and v != 0:
        return None
    elif (d and v and m) == 0:
        return None    
    else:
        pass
        
    


if __name__ == "__main__":
    print(density())
