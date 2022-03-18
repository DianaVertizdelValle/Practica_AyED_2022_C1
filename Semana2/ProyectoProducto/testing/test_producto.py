# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:44:29 2022

@author: je_su
"""
import unittest
from modulos.producto import Producto
from modulos.excepciones_producto import QuantityValueError, PriceValueError, DiscountValueError

class TestProducto(unittest.TestCase):
    
    def setUp(self):
        print()
        print('método setUp')
        self.producto1 = Producto('Celular', 10, 50000)
        
    def tearDown(self):
        print('metodo tearDown')
    
    def test_cantidad(self):
        print('test cantidad')
        
        self.producto1.set_cantidad(20)
        self.assertEqual( self.producto1.get_cantidad() , 20 )        
        #self.assertRaises( QuantityValueError, self.producto1.set_cantidad, 10 )        
        with self.assertRaises(QuantityValueError):
            self.producto1.set_cantidad(10)
    
    def test_precio(self):
        print('test precio')
        
        self.producto1.set_precio(30000)
        self.assertEqual( self.producto1.get_precio() , 30000 )       
        
        with self.assertRaises(PriceValueError):
            self.producto1.set_precio(-10000)  
            
    def test_descuento(self):
        print('test descuento')
        
        self.producto1.aplicar_descuento(20)
        self.assertEqual( self.producto1.get_precio() , 40000 )
        
        self.assertRaises(DiscountValueError, self.producto1.aplicar_descuento, -10 )
        self.assertRaises(DiscountValueError, self.producto1.aplicar_descuento, 120 )
        
        
if __name__ == '__main__':
    unittest.main()
