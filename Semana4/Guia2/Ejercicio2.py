# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:56:29 2022

@author: je_su
"""

import time
import matplotlib.pyplot as plt

n_operaciones = list(range(10, 1500, 100))
tiempos = []

def problema1(n):    
    prueba = 0
    for i in range(n):
       for j in range(n):         
          prueba = prueba + i * j


for operaciones in n_operaciones:
    tic = time.perf_counter()
    problema1(operaciones)
    toc = time.perf_counter()
    tiempos.append(toc-tic)
    
plt.clf()   
#plt.plot(n_elementos, n_comparaciones)
plt.plot(n_operaciones, tiempos)
plt.xlabel("nro elementos n")
plt.ylabel("comparaciones en fn de n")