import json

file_path = "files/productos_Registrados.json"

class Producto:

    def __init__(self, estado, precio, tipo, id,cantStock,desProd):
        self.estado = estado
        self.precio = precio
        self.tipo = tipo
        self.id = id
        self.cantStock = cantStock
        self.desProd = desProd

    def buscarProducto():
        with open(file_path, "r") as f:
            prodTemp = json.load(f)
        prod_buscar = int(input("Ingrese el nombre del producto:"))
        for element in prodTemp:
            if element["desProd"] == prod_buscar:
                print("DATOS DEL PRODUCTO "+str(prod_buscar))
                print("------------------------------------------------------")
                print("Tipo de producto:" + str(element["tipo"]))
                print("Estado:" + element["estado"])
                print("Precio:" + str(element["precio"]))
                print("------------------------------------------------------")

    def mostrarDatos():
        with open(file_path, "r") as f:
            proDatos = json.load(f)
        for element in proDatos:
            if element["estado"] == "En stock":
                print("------------------------------------------------------")
                print("DATOS DEL PRODUCTO "+str(element["desProd"]))
                print("ID:" + element["id"])
                print("Estado:" + element["estado"])
                print("Precio:" + str(element["precio"]))
                print("Tipo del producto:" + element["tipo"])
                print("------------------------------------------------------")
