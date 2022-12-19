from werkzeug.security import check_password_hash
import uuid
import json
import datetime

file_path1 = "files/pagos.json"

class Pago:
    def _init_(self, monto, metPago, cuenta,id,nombre):
        self._numOperacion = str(uuid.uuid4())
        self._fecha = str(
            datetime.datetime.strftime(datetime.datetime.now(), "%d/%m/%Y %H:%M:%S")
        )
        self._monto = monto
        self._metPago = {"Metodo de pago": metPago, "Cuenta": cuenta}
        self._id= "ID" + id 
        self._nombre= "Nombre" + nombre

    def pagar(self):
        if "Tarjeta" in self._metPago["Metodo de pago"]:
            key = "numTarjeta"
            file_path = "files/tarjetas.json"
        else:
            key = "correoPayPal"
            file_path = "files/cuentasPayPal.json"

        with open(file_path, "r") as f:
            met_pago = json.load(f)

        for element in met_pago:
            if check_password_hash(element[key], str(self._metPago["Cuenta"])):
                if element["monto"] > self._monto:
                    monto_suficiente = True
                    element["monto"] = element["monto"] - self._monto
                else:
                    monto_suficiente = False

        with open(file_path, "w") as f:
            json.dump(met_pago, f, indent=4)

        return monto_suficiente

    def cambiarFormato(self):
        RegistroPago = dict(
            id=self._id,
            nombre=self._nombre,
        )
        return RegistroPago

    def registrarTransaccion(self):
        RegistroPago = self.cambiarFormato()
        with open(file_path1, "r") as f:
            data = json.load(f)

        data.append(RegistroPago)

        with open(file_path1, "w") as f:
            json.dump(data, f, indent=4)