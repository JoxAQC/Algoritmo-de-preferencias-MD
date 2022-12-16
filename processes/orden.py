import uuid
from datetime import datetime
import json

file_path1 = "files/ordenes.json"
file_path2 = "files/productos_Registrados.json"

class Reserva:

    def __init__(self, titular,fechaPedido,cantProductos,productosSolicitados):
        self._codPedido = str(uuid.uuid4())
        self._titular = titular
        self._fechaPedido = fechaPedido
        self._cantProductos = cantProductos
        self._productosSolicitados = productosSolicitados

    def separarProductos(cantProductos):
        productosSolicitados = []
        for i in range(cantProductos):
            productosSolicitados.append(input("Ingrese el numero de ID del "+str(i+1)+" producto que desea ordenar:"))
        return productosSolicitados

    def calcularMonto(productosSolicitados):
            monto = 0
            for element in productosSolicitados:
                with open(file_path2, "r") as f:
                    data = json.load(f)
                for productoSolicitado in data:
                    if str(productoSolicitado["id"]) == element:
                        monto = monto + productoSolicitado["precio"]
            return monto


    def ordenar(self):
        ordenan = dict(codPedido=self._codPedido, titular=self._titular, fechaPedido=self._fechaPedido, cantProductos=self._cantProductos, productosSolicitados=self._productosSolicitados)
        with open(file_path1, "r") as f:
            data = json.load(f)

        data.append(ordenan)

        with open(file_path1, "w") as f:
            json.dump(data, f, indent=4)


    def cambiarEstado(productosSolicitados):
        for element in productosSolicitados:
            with open(file_path2, "r") as f:
                data = json.load(f)
            for productosSolicitado in data:
                if str(productosSolicitado["id"]) == element:
                    productosSolicitado["cantStock"] =  productosSolicitado["cantStock"]-1

            with open(file_path2, "w") as f:
                json.dump(data, f, indent=4)

    def mostrarReserva(codPedido):
        with open(file_path1, "r") as f:
            data = json.load(f)
        for element in data:
            if element["codPedido"] == codPedido:
                print("------------------------------------------------------")
                print("DATOS DEL PEDIDO")
                print("Codigo de pedido:" + str(element["codPedido"]))
                print("Titular:" + str(element["titular"]))
                print("Fecha de pedido:" + str(element["fechaPedido"]))
                print("Numero de productos:", element["cantProductos"])
                print("Cantidad de habitaciones:", element["canthabitaciones"])
                print("Productos solicitados:" + str(element["productosSolicitados"]))
                print("------------------------------------------------------")
