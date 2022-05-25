# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:17:56 2021

@author: je_su
"""

def ordenamientoBurbuja(unaLista):
    
    for pasada in range( len(unaLista)-1, 0, -1 ):
        for index in range(pasada):
            if unaLista[index] > unaLista[index + 1]:
                
                temp = unaLista[index]
                unaLista[index] = unaLista[index + 1]
                unaLista[index + 1] = temp



if __name__ == '__main__':

    unaLista = [15, 16, 6, 8, 5]
    print(unaLista)
    print()
    ordenamientoBurbuja(unaLista)
    print()
    print(unaLista)