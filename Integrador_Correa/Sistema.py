from Menu import mostrar_menu 
from Gestion_stock import inicializar, cargar_stock, mostrar_stock, contar, stock_cantidades

def main():
    inicializar()
    opcion = 0
    while opcion != 4:
        opcion = mostrar_menu()
        if opcion == 1:
            cargar_stock()
        elif opcion == 2:
            mostrar_stock()
        elif opcion == 3:
            categoria = input("Ingresa el tipo de producto a contar (enlatados, frutas, congelados, panaderia): ")
            if categoria in stock_cantidades:
                contar(stock_cantidades[categoria])
            else:
                print("Esa categoría no fue encontrada.")
        elif opcion == 4:
            print("Saliendo de este sistema corrupto...")
        else:
            print("Opción incorrecta.")


if __name__ == "__main__":
    main()
