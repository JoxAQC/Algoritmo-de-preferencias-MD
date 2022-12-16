from entities.user import Usuario
from entities.producto import Producto
import json
from werkzeug.security import generate_password_hash, check_password_hash

file_path = "files/admin_Datos.json"
file_path2 = "files/productos_Registradas.json"

class Administrador(Usuario):

    def __init__(self, usuario, contrasenia, nombre, apellido, correo, llaveMaestra):
        super().__init__(usuario, contrasenia, nombre, apellido, correo)
        self._llaveMaestra = llaveMaestra

    def verify_session(given_User, given_Password):
        with open(file_path, "r") as f:
            usuario = json.load(f)

        for element in usuario:
            if element["usuario"] == given_User and check_password_hash(element["contrasenia"], given_Password):
                print("Bienvenido, " + element["nombre"])
                llave = input("Ingrese su llame maestra para continuar: ")
                while check_password_hash(element["llave_maestra"], llave) == False:
                    print("Llave maestra incorrecta, intentelo nuevamente, por favor")
                    llave = input("Ingrese su llame maestra para continuar: ")
                return Administrador(element["usuario"], element["contrasenia"], element["nombre"], element["apellido"], element["correo"], element["llave_maestra"])

    def actualizarContrasenia(self):
        with open(file_path, "r") as f:
            data = json.load(f)

        for admin in data:
            if admin["usuario"] == self._usuario:
                admin_contrasenia = input("Ingrese su contrasenia actual:")
                if check_password_hash(admin["contrasenia"], admin_contrasenia):
                    admin["contrasenia"] = generate_password_hash(input("Ingrese actualiazación de su contraseña: "))
                else:
                    print("Contrasenia incorrecta")

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    def registrarProd():
        print("A continuacion, digite las caracteristicas del nuevo productos:")
        estado = input("Estado: ")
        precio = float(input("Precio: "))
       
        numHabitacion = int(input("Numero de habitacion:"))
        new_Prod = Producto(estado, precio, desProd, numHabitacion)
        roomn = dict(estado=new_Room.estado, precio=new_Room.precio, tipoHabitacion=new_Room.tipoHabitacion, numHabitacion=new_Room.numHabitacion)

        with open(file_path2, "r") as f:
            data = json.load(f)

        data.append(roomn)

        with open(file_path2, "w") as f:
            json.dump(data, f, indent=4)

    def actualizar(dato):
        with open(file_path2, "r") as f:
            habitacionTemp = json.load(f)
        habitacion_buscar = int(input("Ingrese el numero de habitacion a editar:"))

        for element in habitacionTemp:
            if element["numHabitacion"] == habitacion_buscar:
                if dato == 'precio':
                    element[dato] = float(input("Ingrese actualiazación de su " + dato + ": "))
                else:
                    element[dato] = str(input("Ingrese actualiazación de su " + dato + ": "))

        with open(file_path2, "w") as f:
            json.dump(habitacionTemp, f, indent=4)

    def actualizarDatos(self):
        menu = """ACTUALIZAR
        1. Estado
        2. Precio
        3. Tipo de Habitacion
        OPCION: """
        opcion = int(input(menu))
        while opcion > 3 or opcion < 1:
            print("Elija una opción valida")
            opcion = int(input(menu))
        if opcion == 1:
            dato = "estado"
        elif opcion == 2:
            dato = "precio"
        elif opcion == 3:
            dato = "tipoHabitacion"
        self.actualizar(dato)
