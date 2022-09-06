#d = m  / V
# V = volume
# m = massa
# d = densidade

def density(d=0,m=0,v=0):
    if v == 0 and (d and m) != 0:
        resultado = m / d
        return [d, m, resultado]
    elif m == 0 and (v and d) != 0:
        resultado = d * v
        return [d, resultado, v]
    elif d == 0 and (v and m) != 0:
        resultado = m / v
        return [resultado, m, v]
    elif d and m and v != 0:
        return [d, m, v]
    elif (d and v and m) == 0:
        return [d, m, v]    
    else:
        return [d, m, v]
        
    


if __name__ == "__main__":
    print(density())
