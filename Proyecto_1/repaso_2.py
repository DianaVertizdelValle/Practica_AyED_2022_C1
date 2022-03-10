# -*- coding: utf-8 -*-
"""
@author: je_su
"""

# Expresiones condicionales
# if/else

# Queremos comprobar si un alumno regulariza la materia o no
# en base a su nota. Si esta es mayor a 6 regulariza, en caso
# contrario no alcanza la regularida





    
# > ,< ,>=, <=, ==, !=
# diferencia entre asignación y chequear condición de igualdad

#%%
# si el alumno alcanza la nota de regularidad, debemos
# fijarnos también que cumple con una asistencia mayor al 50%







#%%
# nota < 60 : no alcanza la regularidad
# nota (60, 80): regulariza
# nota >=80: promociona 







  


    
#%%

nota = 9
asistencia = 50

if nota >= 6 and asistencia >= 50: 
    print("Regulariza la materia")
if not asistencia >= 50:
    print("no alcanza la regularidad")

