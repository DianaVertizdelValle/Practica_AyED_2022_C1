# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:38:10 2022

@author: je_su
"""
import random
import time
import matplotlib.pyplot as plt

valores_de_n = [10**i for i in range(1, 4)] # [10, 100, 1000]
tiempos = []

def verificar_ordenada(lista):
    i=1
    ordenada = True
    
    while i < len(lista) and ordenada:
        if lista[i-1] > lista[i]:
            ordenada = False
        i += 1
        
    return ordenada


for n in valores_de_n:
    
    lista_ordenada = sorted([random.randint(-100,100) for i in range(n)])
    tic = time.perf_counter()
    verificar_ordenada(lista_ordenada)
    toc = time.perf_counter()
    tiempos.append(toc-tic) #[0.02, 0.05, 0.05]

print(tiempos)
    
#Graficación

plt.clf()
plt.plot(valores_de_n, tiempos, label="verificar lista ordenada")
plt.xlabel("numero de elementos de la lista")
plt.ylabel("tiempo del algoritmo")
plt.title("Tiempos en fn. del nro de elementos")
plt.legend()
    

    
    
    
    
    
    