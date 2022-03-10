# -*- coding: utf-8 -*-
"""
@author: je_su
"""
# Módulo random

import random #módulo que genera números pseudoAleatorios

random_int = random.randint(1, 10)
print(random_int)

#%%
random_float = random.random()
print(5*random_float)

#%%
# https://docs.python.org/3.9/library/stdtypes.html#sequence-types-list-tuple-range
# Python tiene tipos de datos integradas un poco
# más complejas que los tipos de datos 
# strings, enteros, flotantes, booleanos, etc

# listas
# tipo de datos primitivo de Python para guardar 
# colecciones ordenadas de valores, es MUTABLE

frutas = ["manzana", "naranja", "uva"]
print(frutas)
# indexado
# métodos: append, extend, insert, remove

frutas.append("Banana")
print(frutas)

frutas.extend(["cereza", "tomate"])

frutas.insert(1, "kiwi")

frutas.remove("uva")

#Observación: es perfectamente válido tener valores duplicados 
#en una lista.

frutas.append("Banana")
print(frutas)
#%%
#A veces las listas son creadas con otros métodos. 
#Por ejemplo, los elementos de una cadena pueden ser separados 
#en una lista usando el método split()

#cadena_nombres = input("Ingrese los nombres separados por comas:\n")
cadena_nombres = 'Diana, Bruno'
lista_nombres = cadena_nombres.split(', ')

print(lista_nombres)


#%% IndexError

print(lista_nombres[2])

#%%
# lista de listas
frutas = ["banana", "pera", "manzana"]
verduras = ["papa", "zapallo", "rúcula"]

mercado = [frutas,verduras]
print(mercado)

#%%
# también podemos hacer slicing en una lista

lista_numeros = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14]

print(lista_numeros[2:8])
print(lista_numeros[:5])
print(lista_numeros[7:])
print(lista_numeros[7::2])
print(lista_numeros[-2])

#%%
# Puedo utilizar un ciclo for para iterar sobre los elementos 
# de una lista
lista_nombres = ["Diana", "Bruno", "Pedro", "Dalia"]

for elemento in lista_nombres[::2]:
    print(elemento)



#%%
# itero para obtener el valor máximo en una lista
notas = [50, 90, 45, 75, 85, 95, 55, 70]

maximo = 0

for nota in notas:
    if nota > maximo:
        maximo = nota


print(f"El valor máximo es: {maximo}")


#%%
# uso enumerate para obtener índice y valor
notas = [50, 90, 45, 75, 85, 95, 55, 70]

maximo = 0
indice_max = 0

for indice,nota in enumerate(notas):
    #print(nota)
    if nota > maximo:
        maximo = nota
        indice_max = indice

print(f"El valor máximo: {maximo} está en la posición: {indice_max}")

#%%
# Ordenar una lista
# Las listas pueden ser ordenadas "in-situ", 
# es decir, sin usar nuevas variables.

enteros = [10, 1, 7, 3]
enteros.sort()
print(enteros)             

#%%
# Orden inverso

enteros.sort(reverse=True)       
print(enteros)   

#%%
# Funciona con cualquier tipo de datos que tengan orden
caracteres = ['f', 'b', 's']
caracteres.sort()                    
print(caracteres)   

#%%
# sorted() si querés generar una nueva lista 
# ordenada en lugar de ordenar la misma:

enteros = [10, 1, 7, 3]
lista_nueva = sorted(enteros, reverse=True)               
print(lista_nueva)                  
print(enteros)  


