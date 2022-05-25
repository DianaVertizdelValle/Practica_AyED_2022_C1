# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:13:02 2021

@author: je_su
"""

def mezclar_arreglos_ordenadas(izquierda, derecha, lista):
    
    len1 = len(izquierda)
    len2 = len(derecha)
    
    i = 0 #iterador izquierda
    j = 0 #iterador derecha
    k = 0 #indice en la lista
    
    while i < len1 and j < len2:
        if izquierda[i] <= derecha[j]:
            lista[k] = izquierda[i]
            i+= 1
        else:
            lista[k] = derecha[j]
            j+= 1
        k+= 1
    
    while i < len1:
        lista[k] = izquierda[i]
        i+= 1
        k+= 1
    
    while j < len2:
        lista[k] = derecha[j]
        j+= 1
        k+= 1

    
def merge_sort(unaLista):
    if len(unaLista) > 1:
       
        mitad = len(unaLista)//2
        mitadIzquierda = unaLista[:mitad]
        mitadDerecha = unaLista[mitad:]
        
        merge_sort(mitadDerecha)
        merge_sort(mitadIzquierda)
        
        mezclar_arreglos_ordenadas(mitadIzquierda, mitadDerecha, unaLista)

if __name__ == '__main__':
    unaLista = [54,26,93,17,77,31,44,55,20]
    print(unaLista)
    
    merge_sort(unaLista)
    
    print(unaLista)
