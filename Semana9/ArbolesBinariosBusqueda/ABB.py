# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:41:49 2022

@author: je_su
"""

class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
    
    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo
    
    def tieneHijoDerecho(self):
        return self.hijoDerecho
    
    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self
    
    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self
    
    def esRaiz(self):
        return not self.padre
    
    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)
    
    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo
    
    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo
    
    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self
    
    def encontrarSucesor(self):
        """devuelve el sucesor del nodo"""
        sucesor = None
        if self.tieneHijoDerecho():
            sucesor = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    sucesor = self.padre
                else:
                    self.padre.hijoDerecho = None
                    sucesor = self.padre.encontrarSucesor()
        return sucesor
    
    def encontrarMin(self):
        """devuelve el nodo de menor clave"""
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def empalmar(self):
        """realiza el empalme entre el hijo del nodo actual y su padre"""
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                   self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                   self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                   self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                   self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre
            
    def __str__(self):
        return f'{self.clave}: {self.cargaUtil} '
    
    def __iter__(self):
        '''
        recorrido inorden del nodo: hijoIzq -> raiz -> hijoDer
        '''
        if self:
            if self.tieneHijoIzquierdo():
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.__str__()
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho:
                    yield elem 
       
class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano
    
    def agregar(self, clave, valor): 
        """inserta un nuevo nodo (clave,valor)"""
        
        if self.raiz:
            self._agregar(clave, valor, self.raiz)
        else:
            self.raiz = NodoArbol(clave, valor)
            
        self.tamano = self.tamano + 1

    def _agregar(self, clave, valor, nodoActual): 
        """función recursiva auxiliar de agregar"""     
        #------------------------------------------------------
        
        
        
        #-----------------------------------------------------
        
        
    def obtener(self, clave):
        """
        Devuelve el valor almacenado en un nodo del árbol dada su clave
        """
        if self.raiz:
            res = self._obtener(clave, self.raiz)
            if res:
                return res.cargaUtil
            else:
                return None
        else:
            return None

    def _obtener( self, clave, nodoActual):
        """función recursiva auxiliar de obtener"""
        #--------------------------------------------------
        
        
        #---------------------------------------------------
        
        
        
    def eliminar(self, clave):
        """elimina un nodo dada una clave"""
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave, self.raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano - 1
            else:
                raise KeyError('Error, la clave no está en el árbol')
                
        elif self.tamano == 1 and self.raiz.clave == clave:
            self.raiz = None
            self.tamano = self.tamano - 1
            
        else:
            raise KeyError('Error, la clave no está en el árbol')
    
    def remover(self, nodoActual):
        '''
        una vez encontrado el nodo con la clave que se quiere eliminar, 
        esta función elimina el nodo.
        Hay 3 casos a considerar para remover un nodo del árbol            
        '''
        
        if nodoActual.esHoja(): #el nodoActual no tiene hijos -> nodo hoja
            #---------------------------------------------------------------------
            
            
            #---------------------------------------------------------------------        
        elif nodoActual.tieneAmbosHijos(): # el nodoActual tiene ambos hijos
            
            sucesor = nodoActual.encontrarSucesor()
            sucesor.empalmar()
            nodoActual.clave = sucesor.clave
            nodoActual.cargaUtil = sucesor.cargaUtil
        
        else: # el nodoActual tiene un hijo   
         
            if nodoActual.tieneHijoIzquierdo(): #tiene hijo izquierdo
            
                if nodoActual.esHijoIzquierdo():    # el nodoActual es hijo izquierdo
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                    
                elif nodoActual.esHijoDerecho():    # el nodoActual es hijo derecho
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                    
                else:
                    # no es hijo izquierdo ni derecho ---> nodo raiz
                    nodoActual.reemplazarDatoDeNodo( nodoActual.hijoIzquierdo.clave,
                                                     nodoActual.hijoIzquierdo.cargaUtil,
                                                     nodoActual.hijoIzquierdo.hijoIzquierdo,
                                                     nodoActual.hijoIzquierdo.hijoDerecho )
            
            else: # tiene hijo derecho
                #--------------------------------------------------------------------------




                #--------------------------------------------------------------------------
                         
        
    def __delitem__(self,clave):
        self.eliminar(clave)
        
    def __contains__(self,clave):
        if self.obtener(clave):
            return True
        else:
            return False

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()

    def __getitem__(self,clave):
        return self.obtener(clave)

    def __setitem__(self, clave, valor):
        self.agregar(clave, valor)