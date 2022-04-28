# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:19:18 2021

@author: je_su

"""

def ordenamientoInsercion(unaLista):
    
    for indice in range(1, len(unaLista)):
        valorActual = unaLista[indice]
        posicion = indice
        
        while posicion > 0 and unaLista[posicion-1] > valorActual:

            unaLista[posicion] = unaLista[posicion-1]
            posicion = posicion -1            
            
        unaLista[posicion] = valorActual

        
if __name__ == '__main__':
    
    unaLista = [12,8,10,12,15,19,21,22,24,1,2,3,5,4,54,26,93,17,77,31,44,55,20]
    # unaLista = [70,60,50,40,30,20,10]
    ordenamientoInsercion(unaLista)
    print(unaLista)        

