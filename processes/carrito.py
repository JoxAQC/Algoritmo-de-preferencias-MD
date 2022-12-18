import json

file_path = "files/productos.json"

class Carrito:
    def __init__(self, idpedido, cantidad, productosSeleccionados):
        self._idpedido = idpedido
        self._cantidad = cantidad
        self._productosSeleccionados = productosSeleccionados


    def pedirProductos(idpedido):
        productosSeleccionados = []
        productosSeleccionados.append(idpedido)

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
