# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:26:23 2021

@author: je_su
"""

def busquedaSecuencial(unaLista, item):  
    pos = 0
    encontrado = False
    
    while pos < len(unaLista) and not encontrado:        
        if unaLista[pos] == item:
            encontrado = True
        else:
            pos = pos + 1        
    return encontrado       

def busquedaSecuencialOrdenada(unaLista, item):        
    pos = 0
    encontrado = False
    parar = False
    
    while pos < len(unaLista) and not encontrado and not parar:        
        if unaLista[pos] == item:
            encontrado = True
        else:
            if unaLista[pos] > item:
                parar = True
            else:
                pos = pos + 1
        
    return encontrado