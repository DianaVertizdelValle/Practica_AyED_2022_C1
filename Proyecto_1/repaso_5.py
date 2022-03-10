# -*- coding: utf-8 -*-
"""
@author: je_su
"""

# Funciones

#%%
# Usá funciones para encapsular código que quieras reutilizar.

# Queremos implementar una función que dado un número entero "n" 
# calcule la suma de los primeros n números

def suma_enteros(numero:int):
    """Devuelve la suma de los primeros n enteros
       
        numero: int
    """
    total = 0
    while numero > 0:
        total += numero 
        numero -= 1
    return total

#suma = suma_enteros(10)
print(suma_enteros(10))
suma_enteros()


#%%
# Llamadas a una función
# a) argumentos por orden
# b) usando palabras claves (keywords)
# c) Parámetros por defecto

# Función que recibe una lista de enteros y a cada elemento de la 
# lista le suma numero1 y le divide por numero2

def procesamiento_lista(lista, sumador=5.2, divisor=1.2):
    """
    Función que recibe una lista de enteros y a cada elemento de la 
    lista le suma numero1 y le divide por numero2
    lista : lista de enteros
    sumador : float
    divisor: float
    return: devuelve una lista de enteros
    """
    items = []
    for elemento in lista:
        elemento = round((elemento + sumador)/divisor)
        items.append(elemento)
    return items, sumador
    


    

mi_lista = [50, 90, 45, 75, 85, 95, 55, 70]

lista_resultado, numero = procesamiento_lista(mi_lista, sumador=5.2) 

print(lista_resultado)
print(numero)


#%%
# Clases y Objetos


class Paciente:
    """
    Clase para representar un paciente mediante su nombre, edad y peso
    
    Parametros
    ----------
    
    """
    def __init__(self, nombre, edad, peso):
        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso   
        
    def establecer_nombre(self, nombre):
        self.__nombre = nombre 

    def establecer_edad(self, edad):
        self.__edad = edad

    def establecer_peso(self, peso):
        self.__peso = peso  
        
    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def obtener_peso(self):
        return self.__peso  


paciente1 = Paciente( "Ana" , 25, 55)
paciente2 = Paciente("Pedro", 22, 75)

print(paciente1.obtener_nombre())


