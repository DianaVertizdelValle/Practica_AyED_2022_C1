# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:38:37 2022

@author: je_su
"""
#%% Lectura
archivo = open("./archivos/archivo.txt", mode='r')

contenido = archivo.read()

print(contenido)

archivo.close()

#%% Leer linea por linea

nro_linea = 0
archivo = open("./archivos/nombres.txt", mode='r')
for linea in archivo:
    nro_linea += 1
    print(f" {nro_linea} {linea.rstrip()}")
    
archivo.close()   
    
#%%

#gestor de contexto   'with'
nro_linea = 0
with open("./archivos/nombres.txt", mode='r') as archivo:
    for linea in archivo:
        nro_linea += 1
        print(f" {nro_linea} {linea.rstrip()}")
    
#%%

#Escritura de archivos   
nro_linea = 0
with open("./archivos/nombres.txt", mode='w+') as archivo:
    for linea in archivo:
        nro_linea += 1
        print(f" {nro_linea} {linea.rstrip()}")    

    
    
    
    
    
    