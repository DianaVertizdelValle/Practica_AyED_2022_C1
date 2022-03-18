# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:31:22 2022

@author: je_su
"""

class QuantityValueError(Exception):
    """Error al ingresar cantidades negativas de productos"""
    
class PriceValueError(Exception):
    """Error al ingresar precios con valores negativos"""
    
class DiscountValueError(Exception):
    """Error al ingresar descuento"""