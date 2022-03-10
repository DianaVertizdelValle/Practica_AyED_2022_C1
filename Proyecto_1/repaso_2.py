# -*- coding: utf-8 -*-
"""
@author: je_su
"""

# Expresiones condicionales
# if/else

# Queremos comprobar si un alumno regulariza la materia o no
# en base a su nota. Si esta es mayor a 6 regulariza, en caso
# contrario no alcanza la regularidad
nota = 7

if nota >= 6:
    print("Estamos dentro del if")
    print(f"{nota} -> regulariza la materia ") 
else:
    print("Estamos dentro del else")    
    print(f"{nota} -> no alcanza la regularidad")

    
# > ,< ,>=, <=, ==, !=
# diferencia entre asignación y chequear condición de igualdad
# Más de una condición en el if
#%%
# si el alumno alcanza la nota de regularidad, debemos
# fijarnos también que cumple con una asistencia mayor al 50%

nota = 9
asistencia = 40

if nota >= 6: # chequear igualdad
    if asistencia >= 50:
        print("regulariza la materia ")  
    else:
        print("No alcanza la regularida por inasistencia")
else:    
    print(f"{nota} -> no alcanza la regularida")

#%%

if nota >= 6 and asistencia >= 50: 
    print("Regulariza la materia")
if not asistencia >= 50:
    print("no alcanza la regularidad")

# Conectores lógicos: and - or - not


#%%
# nota < 60 : no alcanza la regularidad
# nota (60, 80): regulariza
# nota >=80: promociona 

if nota < 60:
    print("no alcanza la regularidad")
elif nota < 80:
    print("alcanza la regularidad")
else:
    print("promociona!!!")
    







