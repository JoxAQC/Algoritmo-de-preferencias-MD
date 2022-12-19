import datetime
import json

file_path = "files/productos.json"
file_path2 = "files/pedidos.json"

class Carrito:
    def __init__(self, id, cantidadSeleccionada, cantidad, productosSeleccionados):
        self._id = id
        self._cantidadSeleccionada = cantidadSeleccionada
        self._cantidad = cantidad
        self._productosSeleccionados = productosSeleccionados
        self._fecha = str(
            datetime.datetime.strftime(datetime.datetime.now(), "%d/%m/%Y %H:%M:%S")
        )


    def pedirProductos(cantidadSeleccionada):
        productosSeleccionados = []
        for i in range(cantidadSeleccionada):
            productosSeleccionados.append(int(input("Ingrese el id del "+ str(i + 1)+ " producto a pedir:")))
        return productosSeleccionados

    def calcularMonto(productosSeleccionados):
        montoC = 0
        print(productosSeleccionados)
        for element in productosSeleccionados:
            with open(file_path, "r") as f: #abrie el json productos
                data = json.load(f)
                for productosSeleccionados in data: #matriz en el archivo
                    if str(productosSeleccionados["ID"]) == element:
                        montoC = montoC + element["Precio"]
        return montoC

    #def obtenerDatos(productosSeleccionados):
    #    for element in productosSeleccionados:
    #        with open(file_path, "r") as f:
    #            data = json.load(f)
    #        for productosSeleccionados in data:
    #            if str(productosSeleccionados["ID"]) == element:
    #                Nombre = element["Nombre"]
    #                ID = element["ID"]
    #                Precio = element["Precio"]
    #            RegistrarD = dict(Nombre, ID, Precio)
    #    return RegistrarD

