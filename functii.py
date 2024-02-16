#!/usr/bin/python3.10

valoare = input ("Introdu un numar: ")

def calcul_suma(valoare):
    suma = 0
    for i in range(int(valoare) + 1):
        suma = suma + i

    return suma

    rezultat = str(calcul_suma (valoare))
    print ("suma pentru " + valoare + " este" + rezultat)

    x1 = calcul_suma(3)
    x2 = calcul_suma(4)

    print ("Valoare " + str(x1) + " " + str(x2))

