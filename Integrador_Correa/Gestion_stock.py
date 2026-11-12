stock_productos = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}
stock_cantidades = {'enlatados': [], 'frutas': [], 'congelados': [], 'panaderia': []}

def inicializar():
   for categoria in stock_productos:
        stock_productos[categoria] = []
        for categoria in stock_cantidades:
            stock_cantidades[categoria] = []
        
        
        
def cargar_stock():
    categoria = input("Ingresa la categoría del producto(enlatados, frutas, congelados, panaderia): ")
    if categoria in stock_productos:
        producto = input("Ingresa qué producto queres añadir: ")
        cantidad = int(input("Ingresa la cantidad del producto: "))
        stock_productos[categoria].append(producto)
        stock_cantidades[categoria].append(cantidad)
        print("El producto se agrego con éxito.")
    else:
        print("Esta categoría no se encontro.")
        
def mostrar_stock():
    print("stock total")
    for categoria in stock_productos:
        print(categoria + ":")
        print("  Productos:", stock_productos[categoria])
        print("  Cantidades:", stock_cantidades[categoria])
        
def contar(lista_productos):
    cantidad_productos = len(lista_productos)
    suma_cantidades = sum(lista_productos)
    print("Cantidad de productos:", cantidad_productos)
    print("Suma total de las cantidades:", suma_cantidades)

