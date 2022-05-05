# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:42:39 2022

@author: je_su
"""

class MonticuloBinario:

    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0  
    
    def construirMonticulo(self,unaLista):
         """Construye un montículo nuevo a partir de una lista de claves"""
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
    
    def __str__(self):
        lista = ''
        for i in range(1, len(self.listaMonticulo)):
            lista += str(self.listaMonticulo[i]) + ' '
        return lista
    
    def infiltArriba(self,index):
        """función auxiliar para la inserción de un nodo"""
        #-------------------------------------
        
        
        
        #--------------------------------------     
          
          
    def insertar(self,valor):
        """agrega un nuevo ítem al montículo"""
        self.listaMonticulo.append(valor)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltAbajo(self,index):
        """función auxiliar para eliminación y construcción del montículo"""
        #---------------------------------------
        
        
        
        #--------------------------------------           

    def hijoMin(self,index):
        """función auxiliar para la inflitración hacia abajo"""
        #---------------------------------------------
        
        
        #--------------------------------------------
            
    def eliminarMin(self):
        """devuelve el ítem con el menor valor clave, eliminándolo del montículo"""
        valorEliminado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorEliminado
    
    def buscarMin(self):
        """devuelve el ítem con el menor valor clave, dejándolo en el montículo"""
    
    def estaVacio(self):
        """devuelve True si el montículo está vacío o False de lo contrario"""
        
    def tamano(self):
        """devuelve el número de ítems en el montículo"""

    
 