from clases.nodos import nodo
class lista_enlazada:
    def __init__(self):
        self.head = None
    
    # Se inserta un dato a la lista enlazada
    def append(self, data):
        if not data:
            print("El dato no puede ser nulo")
            return
        new_node = nodo(data) # El nodo que se va a insertar
        if not self.head: # Si la lista no tiene ningun nodo
            self.head = new_node # Se inserta el nodo en la cabeza
            return
        last = self.head # Se obtiene el ultimo nodo
        while last.siguiente: # Mientras haya un nodo siguiente se sigue buscando cual no tiene un dato despues de si mismo
            last = last.siguiente 
        last.siguiente = new_node #Se inserta el nuevo nodo al final de la cola
    
    def delete(self, key):
        if not key:
            print("El dato a eliminar no puede ser nulo")
            return
        temp = self.head # Se obtiene el primer nodo
        if temp and temp.dato == key: #Si tenemos el nodo y el siguiente nodo es igual al que queremos eliminar
            self.head = temp.siguiente # Se cambia la cabeza
            temp = None # Se elimina el nodo
            return
        prev = None
        while temp and temp.dato != key: # Se busca el nodo que queremos eliminar
            prev = temp # Se guarda el nodo anterior
            temp = temp.siguiente # Se pasa al siguiente
        if temp is None: # Si no se encuentra el nodo, simplemente se retorna
            return
        prev.siguiente = temp.siguiente
        temp = None
    
    def display(self): # Se muestran todos los nodos de la cola
        temp = self.head
        while temp:
            print(temp.dato, end=" -> ")
            temp = temp.siguiente
        print("Vacio")