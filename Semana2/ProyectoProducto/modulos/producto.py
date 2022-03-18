# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:30:36 2022

@author: je_su
"""

from modulos.excepciones_producto import QuantityValueError, DiscountValueError, PriceValueError

class Producto:
    
    def __init__(self, nombre, cantidad, precio):
        
        self.nombre = nombre
        self.cantidad = cantidad
        #self.set_cantidad(cantidad)
        self.precio = precio
        #self.set_precio(precio)
        
    def set_cantidad(self, cantidad):
        """
        Función para modificar la cantidad de producto        
        cantidad : int
            valor entero que representa el número de unidades        
        QuantityValueError: 
            excepción lanzada al ingresar cantidades negativas
        """
        if cantidad < 0:
            raise QuantityValueError
        else:
            self.cantidad = cantidad
        
    def set_precio(self, precio):
        """
        Función que modifica el precio del producto        
        precio : float 
            valor flotante que representa el precio        
        PriceValueError: 
            excepción lanzada al ingresar valores negativos del precio
        """
        if precio < 0:
            raise PriceValueError
        else:
            self.precio = precio
            
    def get_nombre(self):
       """
       Devuelve el nombre del producto
       """
       return self.nombre
        
    def get_cantidad(self):
        """
        Devuelve la cantidad del producto
        """
        return self.cantidad
    
    def get_precio(self):
        """
        Devuelve el precio del producto
        """
        return self.precio
    
    def aplicar_descuento(self, descuento:int):
        """
        Función que aplica un descuento al precio del producto        
        descuento : int
            valor entero expresado en porcentaje entre 0 y 100        
        DiscountValueError: 
            excepción lanzada al ingresar valores de descuento negativos o mayores a 100
        """
        if 0<= descuento <= 100:
            precio_nuevo = (self.precio * ( 1.0 - float(descuento/100) ))
            self.set_precio(precio_nuevo)
        else:
            raise DiscountValueError("El descuento no puede ser negativo ni mayor a 100")
        
    def __str__(self):
        """Función para mostrar la información de producto como string"""
        
        return f'{self.nombre},{self.cantidad},{self.precio}'
    
    def __lt__(self, otro_producto):
        """Función que implementa la forma de compararse dos instancias de producto"""
        return self.cantidad < otro_producto.get_cantidad()
    
    
if __name__ == '__main__':
      
    producto1 = Producto('Celular', 20, 50000)
    cantidad = int(input("Ingrese la cantidad a modificar: ")) 
    
    try:              
        producto1.set_cantidad(cantidad)        
        print(f"producto1: {producto1}") 
        
    except QuantityValueError:
        print("La cantidad de producto no puede ser negativa")  
        
           
    entrada2 = int(input("Ingrese un porcentaje:")) 
    
    try:
        producto1.aplicar_descuento(entrada2)    
    except DiscountValueError as msg:
        print(msg)
    
    print()
    print("Producto1 con descuento")
    print(producto1)
    
    producto2 = Producto('Celular', 10, 50000)
    print()
    print("Comparo dos productos por su cantidad: ")
    print(f"producto1: {producto1}") 
    print(f"producto2: {producto2}") 
    
    if producto1 > producto2:
        print("producto1 tiene un número de unidades mayor que producto2")
    else:
        print("producto2 tiene un número de unidades mayor que producto1")
    
    
    
    
    
