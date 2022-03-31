# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:09:12 2022

@author: je_su
"""

import random
from timeit import Timer
import matplotlib.pyplot as plt

valores_de_n = [10**i for i in range(1, 5)]
tiempos = [[],[]]

def verificar_ordenada(lista):
    i=1
    ordenada = True    
    while i < len(lista) and ordenada:
        if lista[i-1] > lista[i]:
            ordenada = False
        i += 1
    return ordenada

def verificar_sort(lista):    
    lista_copia = lista[:]
    lista_copia.sort()    
    if(lista_copia == lista):
        return True    
    return False

for n in valores_de_n:
    
    lista_ordenada = sorted( [random.randint(-100, 100) for i in range(n)] )
    
    #verificar_ordenada(lista_ordenada)
    t1 = Timer("verificar_ordenada(lista_ordenada)", 
              "from __main__ import lista_ordenada, verificar_ordenada")
    tiempos[0].append(t1.timeit(number=1000))
    
    t2 = Timer("verificar_sort(lista_ordenada)", 
              "from __main__ import lista_ordenada, verificar_sort")
    tiempos[1].append(t2.timeit(number=1000))

labels = ['método naive', 'usando sort']
xlabel = 'n'
ylabel = 't(n)'

plt.clf()
plt.subplot(121)
plt.plot(valores_de_n, tiempos[0], color='g')
plt.title('método naive')
plt.xlabel(xlabel)
plt.ylabel(ylabel)

plt.subplot(122)
plt.plot(valores_de_n, tiempos[1], color='b')
plt.title('usando sort')
plt.xlabel(xlabel)
plt.ylabel(ylabel)