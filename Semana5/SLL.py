class Nodo:
    """Nodo para la estructura interna de la lista simple enlazada"""
        

class ListaSimpleEnlazada:
    
    def __init__(self):
        pass
    
    def __iter__(self):
        """sobrecarga de la función para poder iterar sobre la lista"""
        nodo = self.cabeza
        while nodo:
            yield nodo
            nodo = nodo.siguiente 
        
    def esta_vacia(self):
        """
        devuelve True si la lista está vacía
        """
    
    def tamano(self):
        """
        devuelve el número de ítems de la lista
        """ 
        
    def agregar(self, item):
        """
        agrega un nuevo ítem al inicio de la lista. 
        item: ítem a agregar.
        ------------------
        pre: se asume que el ítem no está en la lista
        pos: modifica la lista con el ítem agregado al inicio       
        
        """
    
    def anexar(self, item):
        """
        agrega un nuevo ítem al final de la lista. 
        item: item a agregar.
        ------------------
        pre: asume que el ítem no está en la lista
        pos: modifica la lista con el ítem agragdo al final
        """
            
    def insertar(self, posicion, item):
        """
        agrega un nuevo ítem a la lista en "posicion".         
        posicion : entero que indica la posición en la lista donde se va a insertar el nuevo elemento.
        item : ítem a agregar.
        ----------
        pre: asume que el ítem aún no está en la lista y que hay suficientes elementos existentes 
        para tener "posición"
        pos: modifica la lista con el nuevo valor insertado en la posición determinada
        """
    
    
    def buscar(self, item):
        """
         busca el ítem en la lista
         item: ítem a buscar
         return: booleano, True si es encontrado sino False
        """
    
    
    def remover(self, item):
        """
        elimina el ítem de la lista. 
        item: ítem a remover.
        ------------------
        pre: se asume que el ítem está presente en la lista.
        pos: se modifica la lista eliminando el ítem 
        """
        
    def extraer_al_final(self):
        """
        elimina y devuelve el último ítem de la lista. 
        pre: asume que la lista tiene al menos un ítem.
        pos: se modifica la lista y se devuelve el valor eliminado
        """
    
    def extraer(self, posicion=-1):
        """
        elimina y devuelve el ítem en la "posición"
        si no se indica el parámetro posición o este es -1, 
        se elimina y devuelve el último elemento de la lista
        pre: se asume que el ítem está presente en la lista y posicion sea válido
        pos: modifica la lista y devuelve el ítem eliminado
        """     
        
    
    def indice(self, item):
        """
        devuelve el índice correspondiente al ítem en la lista
        ----------------
        pre: asume que el ítem está presente en la lista
        pos: retorna la posición del ítem en la lista
        """
    
    def copiar(self):
        """       
        Realiza una copia de la lista elemento a elemento y devuelve 
        dicha copia
        ----------
        """
    
    def invertir(self):
        """
        Retorna una copia de la lista con los elementos invertidos 
        -------
        """
        
        
    def __del__(self):
        """destructor"""
        
    def ordenar(self):
        """   
        Retorna una copia de la lista con los elementos ordenados de menor a mayor 
        -------
        """  
                    
        


if __name__ == '__main__':
    
    SLL = ListaSimpleEnlazada()
    SLL.anexar(1)    
    SLL.anexar(6)
    SLL.anexar(3)
    SLL.anexar(9)
    SLL.anexar(2)
    print([node.dato for node in SLL])
    
    print(SLL.extraer())
    print([node.dato for node in SLL])
    
    SLL.anexar(20)    
    print([node.dato for node in SLL])
   
    SLL.agregar(8)    
    print([node.dato for node in SLL])
    
    SLL.insertar(1, 25)    
    print([node.dato for node in SLL])
   
    Lista_nueva = SLL.copiar()    
    print([node.dato for node in Lista_nueva])
    
    Lista_nueva2 = SLL.ordenar()    
    print([node.dato for node in Lista_nueva2])