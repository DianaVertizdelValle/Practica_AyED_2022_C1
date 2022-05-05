# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:18:28 2021

@author: je_su
"""

def ordenamientoSeleccion(unaLista):

    for limite in range(len(unaLista)):
        posicionMin = limite
        
        for indice in range(limite+1, len(unaLista)):
            if unaLista[indice] < unaLista[posicionMin]:
                posicionMin = indice
                
        temp = unaLista[limite]
        unaLista[limite] = unaLista[posicionMin]
        unaLista[posicionMin] = temp



if __name__ == '__main__':

    unaLista = [12,8,10,12,15,19,21,22,24,1,2,3,5,4,54,26,93,17,77,31,44,55,20]
    
    ordenamientoSeleccion(unaLista)
    
    print(unaLista)
            