import random

palos = ["o", "c", "e", "b"]
numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]

def crearBaraja(palos, numeros):
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo)
    return baraja

def intercambio(a, b):
    aux = a
    a = b
    b = aux
    return a, b

def barajar(lista_naipes):
    for i in range(len(lista_naipes)):
        nueva_posicion = random.randrange(len(lista_naipes))
        
        #Intercambio con vasos vacíos
        
        aux = lista_naipes[i]
        lista_naipes[i] = lista_naipes[nueva_posicion]
        lista_naipes[nueva_posicion] = aux
    return lista_naipes

