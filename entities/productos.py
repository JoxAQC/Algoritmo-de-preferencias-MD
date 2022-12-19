import json

file_path = "files/productos.json"
file_path2 = "files/pedidos.json"

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
  
    #def guardarBD(self,productosSeleccionados):
    #    with open(file_path2, "r") as f:
    #        guardar = json.load(f)
    #    for element in guardar:
    #        for i in productosSeleccionados:
    #            if element["ID"] == i:
    #                nombre = element["Nombre"]
    #                precio = element["Precio"]
    #                id = element["ID"]
    #    RegistrarDatos = dict(id, nombre, precio, fecha=self._fecha)
    #    return RegistrarDatos

    #def registrarDatos(self):
    #    RegistrarD = self.guardarBD()    
    #    with open(file_path, "r") as f:

    #        guardar = json.load(f)

    #   guardar.append(RegistrarD)

    #    with open(file_path2, "w") as f:
    #        json.dump(guardar,f ,indent=4)
