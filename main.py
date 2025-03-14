from clases.lista_enlazada import lista_enlazada
import os
def main():
    # Instaciamos la clase de lista enlazada
    llist = lista_enlazada()
    # Funcion para mostrar el menu
    def menu():
        print("1. Agregar")
        print("2. Eliminar")
        print("3. Mostrar")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")
        return opcion
    
    while True:
        opcion = menu()
        #Funcion para agregar los dato
        if opcion == "1":
            try:
                dato = input("Ingrese el dato a agregar: ")
                llist.append(dato)
            except Exception as e:
                print(e)
        #Funcion para eliminar los datos
        elif opcion == "2":
            try:
                dato = input("Ingrese el dato a eliminar: ")
                llist.delete(dato)
            except Exception as e:
                print(e)
        #Funcion para mostrar los datos
        elif opcion == "3":
            llist.display()
        #Cierra la aplicacion
        elif opcion == "4":
            break
    

if __name__ == "__main__":
    main()