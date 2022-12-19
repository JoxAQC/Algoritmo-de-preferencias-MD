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


    def pedirProductos(cantidadSeleccionada):
        productosSeleccionados = []
        for i in range(cantidadSeleccionada):
            productosSeleccionados.append(int(input("Ingrese el id del "+ str(i + 1)+ " producto a pedir:")))
        return productosSeleccionados

    def calcularMonto(productosSeleccionados):
        montoC = 0
        for element in productosSeleccionados:
            with open(file_path, "r") as f: #abrie el json productos
                data = json.load(f)
            for productosSeleccionados in data: #matriz en el archivo
                if productosSeleccionados["ID"] == element:
                    montoC = montoC + productosSeleccionados["Precio"]
        return montoC

    def nombrepd(productosSeleccionados):
        for element in productosSeleccionados:
            with open(file_path, "r") as f: #abrie el json productos
                data = json.load(f)
            for productosSeleccionados in data: #matriz en el archivo
                if productosSeleccionados["ID"] == element:
                    nombre = productosSeleccionados["Nombre"]
        return nombre
    
    def preciopd(productosSeleccionados):
        for element in productosSeleccionados:
            with open(file_path, "r") as f: #abrie el json productos
                data = json.load(f)
            for productosSeleccionados in data: #matriz en el archivo
                if productosSeleccionados["ID"] == element:
                    precio = productosSeleccionados["Precio"]
        return precio
    
    def idpd(productosSeleccionados):
        for element in productosSeleccionados:
            with open(file_path, "r") as f: #abrie el json productos
                data = json.load(f)
            for productosSeleccionados in data: #matriz en el archivo
                if productosSeleccionados["ID"] == element:
                    id = productosSeleccionados["ID"]
        return id


