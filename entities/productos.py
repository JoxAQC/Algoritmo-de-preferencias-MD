import json

file_path = "files/productos.json"

class Producto:
    def __init__(self, nombre, id, stock, categorias):
        self._nombre = nombre
        self._id = id
        self._stock = stock
        self._categorias = categorias
    
    def mostrarProducto():
        with open(file_path, "r") as f:
            productos = json.load(f)
        for element in productos:
            if element["Stock"] > 0:
                print()
                print("------------------------------------------------------")
                print("Nombre: " + element["Nombre"])
                print("Id: " + str(element["ID"]))
                print("Precio: " + str(element["Precio"]))
                print("------------------------------------------------------")
            #if tipo == "admin":
            #    if element["estado"] == "No disponible":
            #        print("------------------------------------------------------")
            #        print("DATOS DE LA HABITACION " + str(element["numHabitacion"]))
            #        print("Estado:" + element["estado"])
            #        print("Precio:" + str(element["precio"]))
            #        print("Tipo de la habitacion:" + element["tipoHabitacion"])
            #        print("Numero de la habitacion:" + str(element["numHabitacion"]))
            #        print("------------------------------------------------------")