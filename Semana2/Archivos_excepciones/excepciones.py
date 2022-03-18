# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:09:06 2022

@author: je_su
"""

#%% KeyError

un_diccionario = {'clave1':1 , 'clave2': 2}
print(un_diccionario['clave3'])

#%% TypeError
texto = "abc"
print(texto + 4)

print("Mi programa sigue acá .....")

#%%
# Ante la presencia de alguna de estas excepciones podemos elegir
# que se realice alguna acción utilizando las siguientes instrucciones

# try:
    
    # aquí ejecutamos un código que potencialmente puede causar
    # una excepción
    
# except:
    
    # Este es el bloque de código que querés que se ejecute
    # si hay excepción
    
# else:
    
    # Este bloque se ejecuta si no hubo excepción
    # Siempre que mi programa no falle
    
# finally:
    
    # Este bloque se ejecuta si hubo o no excepción
    
    
#%%
try:
    archivo = open("un_archivo.txt")

except FileNotFoundError as mensaje:
    #print("El archivo no existe")
    print(mensaje)
    archivo = open("un_archivo.txt", mode='w')
    archivo.write("escribo algo")
else: 
    print('Leo el archivo')
    print(archivo.read())
finally:
    print("cierro el archivo")
    archivo.close()

# try: 
#     un_diccionario = {'clave1': 2, 'clave2': 6}
#     print(un_diccionario['clave3'])
# except KeyError:
#     print("La clave no existe")
    
    
print("Sigue acá")

#%%#
# Podemos lanzar nuestras propias excepciones!

class MiError(Exception):
    """Error para manejar mensajes"""

def funcion_prueba():
    raise MiError("Esta es una excepción")

try:
    funcion_prueba()
except MiError as mensaje:
    print(mensaje)
#%%

from excepciones_imc import ImcErrorAltura, ImcErrorPeso

def calcularIMC(altura, peso):
    if not (0<altura<3):
        raise ImcErrorAltura("Un humano tiene altura positiva y menor a 3m")
    if peso<0:
        raise ImcErrorPeso
    
    #peso en kg, altura en m
    imc = peso/(altura ** 2)
    return imc

if __name__ == '__main__':

    altura = float(input("Ingrese su altura: "))
    peso = int(input("Ingrese su peso: ")) 

    try:
        calcularIMC(altura, peso)
        
    except ImcErrorAltura as mensaje_error:
        print(mensaje_error)
            
    except ImcErrorPeso:
        print("mensaje_error")












