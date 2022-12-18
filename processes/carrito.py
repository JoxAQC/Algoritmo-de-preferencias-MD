import json

file_path = "files/productos.json"

class Carrito:
    def __init__(self, idpedido, cantidadSeleccionada, cantidad, productosSeleccionados):
        self._idpedido = idpedido
        self._cantidadSeleccionada = cantidadSeleccionada
        self._cantidad = cantidad
        self._productosSeleccionados = productosSeleccionados


    def pedirProductos(cantidadSeleccionada):
        productosSeleccionados = []
        for i in range(cantidadSeleccionada):
            productosSeleccionados.append(int(input("Ingrese el id del "+ str(i + 1)+ " producto a pedir:")))
        return productosSeleccionados

    def calcularMonto(productosSeleccionados):
        monto = 0
        for element in productosSeleccionados:
            with open(file_path, "r") as f:
                data = json.load(f)
            for productosSeleccionados in data:
                if str(productosSeleccionados["ID"]) == element:
                    monto = monto + productosSeleccionados["Precio"]
                    cantidad = productosSeleccionados.count(element)

        return monto * cantidad
