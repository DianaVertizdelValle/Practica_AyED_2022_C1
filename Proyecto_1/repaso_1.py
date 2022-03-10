# -*- coding: utf-8 -*-
"""
@author: je_su
"""

# Entrada/salida de datos - 
# string, int, float, boolean
#%%
# print and strings
# https://docs.python.org/3.9/library/stdtypes.html#text-sequence-type-str
print("Hola mundo")


# "" indican un string: cadena de caracteres
#%%
# concatenación de strings
variable = "Mundo"
print("Hola " + variable)


#%%
# ingreso de datos por consola

input("¿Cual es tu nombre?: ")

#%% 
# uso de variables

nombre = input('¿Cual es tu nombre?" ": ')
print(nombre)

#%%
# tipos de datos primitivos o tipos integrados
# https://docs.python.org/es/3/library/stdtypes.html
variable_str = "estudiante"

print(variable_str[0])
print("hola"+" mundo")
print("123"+"456")
print(type(variable_str))

#%%
# También se puede rebanar (slice) o seleccionar subcadenas 
# especificando un rango de índices con :
variable_str = "estudiante"
print(variable_str[:5])
print(variable_str[5:])
print(variable_str[3:8])
print(variable_str[3:8:2])
a = variable_str[-2:]
print(a)
print(variable_str)
# El caracter que corresponde al último índice no se incluye. 
# Si un extremo no se especifica, significa que es desde el 
# comienzo o hasta el final, respectivamente.

########################################################################
# Los strings son "inmutables" o de sólo lectura. Una vez creados, #####
# su valor no puede ser cambiado.
########################################################################
# print(variable_str)
#%%
# No puedo hacer lo siguiente
variable_str = "estudiante"

variable_str[3] = "r"

#%%
# strip(), lower(), upper(), replace() 
variable_str = "  estudiante  "
print(variable_str.strip())

variable1= "Estudiante"
print(variable1.lower())
print(variable1)

variable2 = "estudiante"
print(variable2.upper())

variable3 = "estudiante primaria"
print(variable3.title())

#%%
# len() función integradas 
# https://docs.python.org/es/3/library/functions.html
# pertenecn a la biblioteca estándar de python

nombre_usuario = input("¿Cual es tu nombre?: ")
tamanio = len(nombre_usuario)
#print("Tu nombre tiene " + tamanio + " letras")
print(type(tamanio))
#%%
# https://docs.python.org/3.9/library/stdtypes.html#numeric-types-int-float-complex
# enteros
numero_int = 1_253_765
print(numero_int)


#%%
#float
numero_pi = 3.14159
print(numero_pi)
print(type(numero_pi))

#%%
# boolean
variable_bool = False
print(type(variable_bool))

#%% Volviendo a nuestro ejemplo

nombre_usuario = input("¿Cual es tu nombre?: ")
tamanio = len(nombre_usuario)
print("Tu nombre tiene " + str(tamanio) + " letras")
#print(type(tamanio))



#%%
# + - * / **
# PEMDAS: Parentesis-Exponentes-Mult/Div-Suma/Resta
# la prioridad de solución es de izq a der
# print(3*3+3/3-3)

#%%
# División entera
print((8/2))
print(round(8/3, 2))
print((8//3)) #obtengo un tipo entero
print(type(8/3))
#%%
# import math
# a = math.sqrt(x)
# b = math.sin(x)
# c = math.cos(x)
# d = math.tan(x)
# e = math.log(x)
#%%
# f-strings python 3.6
# https://realpython.com/python-f-strings/#:~:text=Also%20called%20%E2%80%9Cformatted%20string%20literals,the%20__format__%20protocol.
tamanio = 9
altura = 1.559
gano = True

print(f"El tamaño es: {tamanio}, la altura: {altura:.2f} y su estado: {gano}")


