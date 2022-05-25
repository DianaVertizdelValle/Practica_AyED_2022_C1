# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 08:13:55 2021

@author: je_su
"""

def busquedaBinaria(unaLista, item):
    primero = 0
    ultimo = len(unaLista) - 1
    encontrado = False
    
    while primero <= ultimo and not encontrado:

        puntoMedio = (primero + ultimo)//2
        
        if unaLista[puntoMedio] == item:
            encontrado = True
        else:
            if unaLista[puntoMedio] < item:
                primero = puntoMedio + 1
            else:
                ultimo = puntoMedio -1        
    
    return encontrado



def busquedaBinariaRec(unaLista, item):
    inicio = 0
    fin = len(unaLista) - 1
    
    puntoMedio = (inicio + fin)//2
    
    if len(unaLista) == 0:
        return False
        
    if unaLista[puntoMedio] == item:
        return True
    else:
        if unaLista[puntoMedio] < item:
            return busquedaBinariaRec(unaLista[puntoMedio+1 : ], item)
        else:
            return busquedaBinariaRec(unaLista[ : puntoMedio], item)


if __name__ == '__main__':

    listaPrueba = [2, 4, 5, 9, 11, 13, 14, 15, 19, 20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
    print(busquedaBinariaRec(listaPrueba, 100))