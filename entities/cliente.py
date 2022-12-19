from entities.user import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
import json

file_path = "files/clientes.json"


def codificar(dato):
    encriptado = generate_password_hash(dato)
    return encriptado


class Cliente(Usuario):
    def __init__(self, usuario, contrasenia, nombre, apellido, correo, pago):
        super().__init__(usuario, contrasenia, nombre, apellido, correo)
        self._pago = pago

    def verify_session(given_User, given_Password):
        with open(file_path, "r") as f:
            usuario = json.load(f)

        for element in usuario:
            if element["usuario"] == given_User and check_password_hash(
                element["contrasenia"], given_Password
            ):
                print("Bienvenido, " + element["nombre"])
                return Cliente(
                    element["usuario"],
                    element["contrasenia"],
                    element["nombre"],
                    element["apellido"],
                    element["correo"],
                    element["pago"]
                )

    def registrar(self):
        with open(file_path, "r") as f:
            client = json.load(f)

        registrado = False

        for element in client:
            if element["usuario"] == self._usuario:
                registrado = True
                element["pago"].append(self._pago)

        if registrado == False:
            file_path2 = "files/usuarios.json"

            with open(file_path2, "r") as f:
                usuarios = json.load(f)

            for element in usuarios:
                if element["usuario"] == self._usuario:
                    usuarios.remove(element)

            with open(file_path2, "w") as f:
                json.dump(usuarios, f, indent=4)

            usercliente = dict(
                usuario=self._usuario,
                contrasenia = codificar(self._contrasenia),
                nombre=self._nombre,
                apellido=self._apellido,
                correo=self._correo,
                pago=[]
            )
            usercliente["pago"].append(self._pago)
            client.append(usercliente)

        with open(file_path, "w") as f:
            json.dump(client, f, indent=4)

    def actualizar(self, dato):
        with open(file_path, "r") as f:
            usuarios = json.load(f)

        for element in usuarios:
            if element["usuario"] == self._usuario:
                if dato == "contrasenia":
                    element[dato] = generate_password_hash(
                        input("Ingrese actualiazación de su " + dato + ": ")
                    )
                else:
                    element[dato] = input("Ingrese actualiazación de su " + dato + ": ")

        with open(file_path, "w") as f:
            json.dump(usuarios, f, indent=4)
