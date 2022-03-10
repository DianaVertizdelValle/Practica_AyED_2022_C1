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
# Python tiene tipos de datos integradas un poco
# más complejas que los tipos de datos 
# strings, enteros, flotantes, booleanos, etc

# listas
# tipo de datos primitivo de Python para guardar 
# colecciones ordenadas de valores, es MUTABLE

frutas = ["manzana", "naranja", "uva"]

# indexado
# métodos: append, extend, insert, remove







#Observación: es perfectamente válido tener valores duplicados 
#en una lista.

frutas.append("Banana")
print(frutas)
#%%
#A veces las listas son creadas con otros métodos. 
#Por ejemplo, los elementos de una cadena pueden ser separados 
#en una lista usando el método split()




#%% IndexError



#%%
# lista de listas
frutas = ["banana", "pera", "manzana"]
verduras = ["papa", "zapallo", "rúcula"]




#%%
# también podemos hacer slicing en una lista

lista_numeros = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14]

# print(lista_numeros[2:8])
# print(lista_numeros[:5])
# print(lista_numeros[7:])
# print(lista_numeros[7::2])
# print(lista_numeros[-2])

#%%
# Puedo utilizar un ciclo for para iterar sobre los elementos 
# de una lista
lista_nombres = ["Diana", "Bruno", "Pedro", "Dalia"]





#%%
# itero para obtener el valor máximo en una lista
notas = [50, 90, 45, 75, 85, 95, 55, 70]

maximo = 0



print(f"El valor máximo es: {maximo}")


#%%
# uso enumerate para obtener índice y valor
notas = [50, 90, 45, 75, 85, 95, 55, 70]

maximo = 0
indice_max = 0



print(f"El valor máximo: {maximo} está en la posición: {indice_max}")

#%%
# Ordenar una lista
# Las listas pueden ser ordenadas "in-place", 
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
lista_nueva = sorted(enteros)               
                           



