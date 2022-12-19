
import datetime
import json

file_path = "files/pedidos.json"
file_path2 = "files/productos.json"

class Registro:
    def __init__(self, nombre, id, precio):
        self._nombre = nombre
        self._if = id
        self._precio = precio

    def RegistrarPedidos(productosSeleccionados):
        fecha = str(
            datetime.datetime.strftime(datetime.datetime.now(), "%d/%m/%Y %H:%M:%S")
        )
        for element in productosSeleccionados:
            with open(file_path, "r") as f:
                data = json.load(f)
            for productosSeleccionados in data:
                if str(productosSeleccionados["ID"]) == element:
                    nombre = element["Nombre"]
                    id = element["ID"]
                    precio = element["Precio"]
                

        with open(file_path2, "r") as f:
            data = json.load(f)
            
        RegistrarD = dict(nombre, id, precio, fecha )
        data.append(RegistrarD)

        with open(file_path2, "r") as f:
            json.dump(data, f, indent=4)
