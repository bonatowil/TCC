# P1 x V1 = P2 x V2
from time import sleep
incognita = input("Qual incógnita deseja descobrir?\nP1\nV1\nP2\nV2\n> ").lower()

if incognita == "p1" :
    p2 = float(input("Insira o valor de P2: "))
    v1 = float(input("Insira o valor de V1: "))
    v2 = float(input("Insira o valor de V2: "))
    resultado = (p2 * v2) / v1
    print(resultado)
    sleep(10)
if incognita == "v1" :
    p1 = float(input("Insira o valor de P1: "))
    p2 = float(input("Insira o valor de P2: "))
    v2 = float(input("Insira o valor de V2: "))
    resultado = (p2 * v2) / p1
    print(resultado)
    sleep(10)
if incognita == "p2" :
    p1 = float(input("Insira o valor de P1: "))
    v1 = float(input("Insira o valor de V1: "))
    v2 = float(input("Insira o valor de V2: "))
    resultado = (p1 * v1) / v2
    print(resultado)
    sleep(10)
if incognita == "v2" :
    p1 = float(input("Insira o valor de P1: "))
    p2 = float(input("Insira o valor de P2: "))
    v1 = float(input("Insira o valor de V1: "))
    resultado = (p1 * v1) / p2
    print(resultado)
    sleep(10)

sleep(10)