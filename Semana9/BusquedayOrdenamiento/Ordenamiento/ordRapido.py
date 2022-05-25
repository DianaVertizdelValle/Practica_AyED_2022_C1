# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:19:04 2021

@author: je_su
"""


def particion(unaLista, ind_primero, ind_ultimo):
    
    valor_pivote = unaLista[ind_primero]
    
    marca_izq = ind_primero + 1
    marca_der = ind_ultimo
    
    hecho = False
    while not hecho:

        while marca_izq <= marca_der and unaLista[marca_izq] <= valor_pivote:
            marca_izq += 1
            
        while marca_izq <= marca_der and unaLista[marca_der] >= valor_pivote:            
            marca_der -= 1
            
        if marca_der < marca_izq:
            hecho = True
        else:
            temp = unaLista[marca_izq]
            unaLista[marca_izq] =  unaLista[marca_der]
            unaLista[marca_der] = temp
    
    temp = valor_pivote
    unaLista[ind_primero] = unaLista[marca_der]
    unaLista[marca_der] = temp
    return marca_der     
    
    

def ordRapidoAuxiliar(unaLista, ind_primero, ind_ultimo):    
    if ind_primero < ind_ultimo:
        
        ind_particion = particion(unaLista, ind_primero, ind_ultimo)
        
        ordRapidoAuxiliar(unaLista, ind_primero, ind_particion - 1)
        ordRapidoAuxiliar(unaLista, ind_particion + 1, ind_ultimo)
        
def ordRapido(unaLista):    
    ordRapidoAuxiliar(unaLista, 0, len(unaLista) - 1)

        
if __name__ == '__main__':
    
    #unaLista = [12,8,10,12,15,19,21,22,24,1,2,3,5,4,54,26,93,17,77,31,44,55,20]
    unaLista = [7 , 6, 10, 5, 9, 2, 1, 15, 7]
    print('Original: ', unaLista)
    ordRapido(unaLista)
    print('Ordenada: ', unaLista)
    
    
    
    
    