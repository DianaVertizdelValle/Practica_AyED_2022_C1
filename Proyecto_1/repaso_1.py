# -*- coding: utf-8 -*-
"""
@author: je_su
"""

# Entrada/salida de datos - 
# string, int, float, boolean
#%%
# print and strings


# "" indican un string: cadena de caracteres

#%%
# concatenación


#%%
# ingreso de datos por consola



#%% 
# uso de variables



#%%
# tipos de datos primitivos o tipos integrados
# https://docs.python.org/es/3/library/stdtypes.html
variable_str = "estudiante"

# print(variable_str[3])
# print("hola"+" mundo")
# print("123"+"456")
# print(type(variable_str))

# También se puede rebanar (slice) o seleccionar subcadenas 
# especificando un rango de índices con :

# print(variable_str[:5])
# print(variable_str[5:])
# print(variable_str[3:8])


# El caracter que corresponde al último índice no se incluye. 
# Si un extremo no se especifica, significa que es desde el 
# comienzo o hasta el final, respectivamente.

########################################################################
# Los strings son "inmutables" o de sólo lectura. Una vez creados, #####
# su valor no puede ser cambiado.
########################################################################
# print(variable_str)
#%%
variable_str = "estudiante"

variable_str[3] = "r"

#%%
# strip(), lower(), upper(), replace() 




#%%
# len() función integradas 
# https://docs.python.org/es/3/library/functions.html
# pertenecn a la biblioteca estándar de python

nombre_usuario = input("¿Cual es tu nombre?: ")
tamanio = len(nombre_usuario)
print("Tu nombre tiene " + tamanio + " letras")

#%%
#enteros
numero_int = 1_253_765



#%%
#float
numero_pi = 3.14159



#%%
# boolean
variable_bool = False
print(type(variable_bool))

#%% Volviendo a nuestro ejemplo



#%%
# + - * / **
# PEMDAS: Parentesis-Exponentes-Mult/Div-Suma/Resta
# la prioridad de solución es de izq a der
#print(3*3+3/3-3)

#%%
#print(int(8/3))
#print(round(8/3, 2))
print(type(8//3)) #obtengo un tipo entero
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

