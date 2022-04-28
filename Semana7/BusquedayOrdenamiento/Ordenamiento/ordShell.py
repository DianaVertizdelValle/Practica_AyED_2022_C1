# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:54:24 2021

@author: je_su
"""

#cuentas_comparaciones = 0

def ordenamientoShell(unaLista):
    
    separacion = len(unaLista)//2
    
    while separacion > 0:      
      for posicionInicio in range(separacion):
          OrdenamientoPorInsercion(unaLista,posicionInicio,separacion)
      separacion = separacion // 2
    

def OrdenamientoPorInsercion(unaLista,inicio,brecha):

    for i in range(inicio+brecha,len(unaLista),brecha):        
        valorActual = unaLista[i]
        posicion = i

        while posicion>=brecha and unaLista[posicion-brecha]>valorActual:
            unaLista[posicion]=unaLista[posicion-brecha]
            posicion = posicion-brecha            

        unaLista[posicion]=valorActual
    


unaLista = [4,9,7,1,5,8,2,6,3]

print(unaLista)

ordenamientoShell(unaLista)

# print(cuentas_comparaciones)
print(unaLista)















