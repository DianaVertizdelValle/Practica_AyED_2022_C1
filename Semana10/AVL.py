# -*- coding: utf-8 -*-
"""
Created on Thu May 12 00:55:20 2022

@author: Bruno Breggia
"""

from ABB import NodoArbol
from ABB import ArbolBinarioBusqueda as ABB


class AVL(ABB):
    
    def __init__(self):
        ABB.__init__(self)
    
    def _agregar(self,clave,valor,nodoActual):
        if clave < nodoActual.clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave,valor,nodoActual.hijoIzquierdo)
            else:
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoIzquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave,valor,nodoActual.hijoDerecho)
            else:
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual)
                self.actualizarEquilibrio(nodoActual.hijoDerecho)
    
    def actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre is not None:
            if nodo.esHijoIzquierdo():
                    nodo.padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                    nodo.padre.factorEquilibrio -= 1
    
            if nodo.padre.factorEquilibrio != 0:
                    self.actualizarEquilibrio(nodo.padre)
        
    def reequilibrar(self,nodo):
        if nodo.factorEquilibrio < 0:
            if nodo.hijoDerecho.factorEquilibrio > 0:
                self.rotarDerecha(nodo.hijoDerecho)
                self.rotarIzquierda(nodo)
            else:
                self.rotarIzquierda(nodo)
        elif nodo.factorEquilibrio > 0:
            if nodo.hijoIzquierdo.factorEquilibrio < 0:
                self.rotarIzquierda(nodo.hijoIzquierdo)
                self.rotarDerecha(nodo)
            else:
                self.rotarDerecha(nodo)
    
    def rotarIzquierda(self, pivote):
        pass
    
    def rotarDerecha(self, pivote):
        pass
    
    
    
