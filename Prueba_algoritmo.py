#Matrices
ListaBebida = ["1","2","3","4","5","24","12","6","7","8","9","10","23","11"]

#Matriz de valoracion de bebidas
#MatrizPrincipalProductosBebida = [
#    [1,1,0,0,0,0],
#    [1,1,0,0,0,0],
#    [1,1,0,0,0,0],
#    [1,1,0,0,0,0],
#    [1,0,1,0,0,0],
#    [1,0,1,0,0,0],
#    [1,0,0,1,0,0],
#    [0,1,0,0,1,0],
#    [0,1,0,0,1,0],
#    [0,1,0,0,1,0],
#    [0,0,0,0,1,1],
#    [0,0,0,1,1,0],
#    [0,0,0,0,1,1],
#    [0,0,0,1,1,0]
#   ]

#Matriz de valoracion de bebidas con el id de productos en [0]
MatrizPrincipalProductosBebida = [
    [1,1,1,0,0,0,0],
    [2,1,1,0,0,0,0],
    [3,1,1,0,0,0,0],
    [4,1,1,0,0,0,0],
    [5,1,0,1,0,0,0],
    [24,1,0,1,0,0,0],
    [12,1,0,0,1,0,0],
    [6,0,1,0,0,1,0],
    [7,0,1,0,0,1,0],
    [8,0,1,0,0,1,0],
    [9,0,0,0,0,1,1],
    [10,0,0,0,1,1,0],
    [23,0,0,0,0,1,1],
    [11,0,0,0,1,1,0]
   ]

ListaComida = ["13","14","15","16","17","18","19","20","21","22"]

#Matriz de valoracion de bebidas
#MatrizPrincipalProductosComida = [
#    [1,1,0,0,0,0],
#    [1,0,1,0,0,0],
#    [1,1,0,0,0,0],
#    [0,0,1,1,0,0],
#    [0,1,0,1,0,0],
#    [0,0,1,1,0,0],
#    [0,1,0,1,0,0],
#    [0,0,0,1,1,0],
#    [0,0,0,0,1,1],
#    [0,1,0,0,1,0]
#    ]

#Matriz de valoracion de bebidas con id del producto en [0]
MatrizPrincipalProductosComida = [
    [13,1,1,0,0,0,0],
    [14,1,0,1,0,0,0],
    [15,1,1,0,0,0,0],
    [16,0,0,1,1,0,0],
    [17,0,1,0,1,0,0],
    [18,0,0,1,1,0,0],
    [19,0,1,0,1,0,0],
    [20,0,0,0,1,1,0],
    [21,0,0,0,0,1,1],
    [22,0,1,0,0,1,0]
    ]

Orden = []


#Se visualiza los productos para comprar
print("Bienvenido a Coffee Peluche")
print("Bebida")
MPB = len(MatrizPrincipalProductosBebida)
for i in range(MPB):
    print(MatrizPrincipalProductosBebida[i][0], end=" ")
    print()
print("Comida")
MPC = len(MatrizPrincipalProductosComida)
for i in range(MPC):
    print(MatrizPrincipalProductosComida[i][0], end=" ")
    print()

#Se selecciona el pedido
menu = """Opcion a elegir
1. Pedir 
2. Salir
"""

OpcionMenu = int(input(menu))
while OpcionMenu != 2:
    Pedido = input("Digite su orden: ")
    Orden.append(Pedido)
    print(Orden)
    menu = """Opcion a elegir
    1. Pedir 
    2. Salir
    """
    OpcionMenu = int(input(menu))
    if OpcionMenu == 2:
        break
    

#Numero de filas
filas = 3
#Numero de columnas
columnas = 3

#El pedido se guarda en una matriz
#for i in MatrizPrincipalProductosBebida:
   #if Orden == MatrizPrincipalProductosBebida[i][0]:
#for i in range(filas):
#    Pedidos.append([])
#    for j in range(columnas):
#        Pedidos[i].append(Orden)
#print(Pedidos)
#for i in MatrizPrincipalProductosComida:
#    if Orden == MatrizPrincipalProductosComida[i][0]:

#Se califica los pedidos

#Se multiplica lo pedido por la matriz de pedidos

#Se suma por colummnas y se guarda en arreglo sumas

#Se pondera las sumas


