# -*- coding: utf-8 -*-

import unittest
from modulos.colaCircular import ColaCircular
# from modulos.excepciones import ErrorQueueFull, ErrorQueueEmpty

class TestColaCircular(unittest.TestCase):
    
    def setUp(self):
        self.miColaCircular = ColaCircular(3)
    
    def tearDown(self):
        pass
    
    def test_inicializacion(self):
        with self.assertRaises(Exception, msg='Debe arrojar error si se pasa tamaño cero') as _:
            ColaCircular(0)
        with self.assertRaises(Exception, msg='Debe arrojar error si se pasa tamaño negativo') as _:
            ColaCircular(-5)
        with self.assertRaises(Exception, msg='Debe arrojar error si se pasa tamaño no numerico') as _:
            ColaCircular('hola')

    def test_correcto_funcionamiento(self):
        items = [23, 75, 100]
        for i in range(101):
            for i in items:
                self.miColaCircular.encolar(i)
            for i in items:
                self.assertEqual(self.miColaCircular.desencolar(), i,
                                 msg='Elementos extraidos en orden no son iguales a los ingresados')

    def test_errorVacio(self):
        self.assertRaises( Exception, self.miColaCircular.desencolar,
                          msg='No advierte que la cola esta vacia')
    
    def test_errorLleno(self):
        for i in range(3):
            self.miColaCircular.encolar(i)
        self.assertRaises( Exception, self.miColaCircular.encolar, 3,
                          msg='No advierte que la cola esta llena')
    
    def test_control_vacio(self):
        self.assertIs( self.miColaCircular.estaVacio(), True )
        for i in range(3):
            self.miColaCircular.encolar(i)
        self.assertIs( self.miColaCircular.estaVacio(), False )
        
    def test_control_lleno(self):
        self.assertIs( self.miColaCircular.estaLleno(), False )
        for i in range(3):
            self.miColaCircular.encolar(i)
        self.assertIs( self.miColaCircular.estaLleno(), True )
        self.miColaCircular.vaciar()
        self.assertIs( self.miColaCircular.estaLleno(), False, 
                      msg='No se vacio correctamente' )
        
    
if __name__ == '__main__':
    
    unittest.main()
