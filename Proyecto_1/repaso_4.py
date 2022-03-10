# -*- coding: utf-8 -*-
"""
@author: je_su
"""
# Tuplas
# se los usa para representar registros
# representan un objeto con distintas partes

paciente_1 = ("Ana", 25, 55)

print(paciente_1[0])

# El contenido de las tuplas no puede ser modificado.
#paciente_1[1] = 30 # Nooo

nombre, edad, peso = paciente_1
print(f'paciente 1: {nombre}, edad: {edad}, peso: {peso}')

#%%
# las tuplas suelen usarse para un solo ítem de múltiples partes
# las listas suelen usarse para una colección de diferentes elementos,
# pero del mismo tipo.

paciente_1 = ("Ana", 25, 55)
paciente_2 = ("Pedro", 22, 75)

nombres_pacientes = ["Ana", "Pedro", "Jeremías"]


# lista de tuplas

registros = []
registros.append(paciente_1)
registros.append(paciente_2)

print(registros)

#%%
# Diccionarios
# Un diccionario almacena elementos organizados mediante claves 
# y valores. Las claves sirven como índices para acceder a los
# valores.

pacientes = { 'Ana': 25, 'Pedro': 22, 'Jeremías': 30 }

print(pacientes['Ana'])

pacientes['Ana'] = 26

print(pacientes)

#%%

# Casi cualquier valor puede usarse como clave en un diccionario
# La principal restricción es que una clave debe ser de tipo inmutable
# Por ejemplo, tuplas:
    

feriados = { (1, 1):'Año nuevo', (1, 5):'Día del trabajador' }
print( feriados[(1,1)] )

# las listas, los diccionarios y los conjuntos no pueden ser claves
#%%
# Conjuntos
# Un conjunto es una colección de elementos únicos 
# sin orden y sin repetición.

#conjunto1 = {"banana", "naranja", "pera"}

conjunto1 = set(["banana", "naranja", "pera"])

#print(conjunto1)

# No permiten indexación ni slicing
# .add(), .remove()

conjunto1.add("manzana")
print(conjunto1)

conjunto2 = set(["kiwi", "naranja", "sandía"])

# s1 | s2                 # Unión de conjuntos s1 y s2
# s1 & s2                 # Intersección de conjuntos
# s1 - s2                 # Diferencia de conjuntos
print(conjunto2)
conjunto = conjunto2 - conjunto1
print()

print(conjunto)
