from entities.user import Usuario

import json

if __name__ == "__main__":
    menu="""
    1.- Iniciar Sesion
    2.- Registrarse
    Elija una opcion: """
    option = int(input(menu))
    if option == 1:
        user = input("      Usuario: ")
        password = input("      Contrasenia: ")
        usuarioEnSesion = Usuario.verify_session(user, password)

        while usuarioEnSesion == None:
            print("     No tenemos a ese usuario registrado, intentelo de nuevo")
            user = input("      Usuario: ")
            password = input("      Contrasenia: ")
            usuarioEnSesion = Usuario.verify_session(user, password)

        menu = """
            1.- Actualizar Datos
            2.- Comprar
            Elija una opcion: """

        op = int(input(menu))
            
        if op == 1:
            usuarioEnSesion.actualizarDatos()
        elif op == 2:
           pass

    elif option == 2:
        user = input("Ingrese nuevo usuario: ")
        password = input("Ingrese nueva contrasenia: ")
        name = input("Ingrese su nombre: ") 
        lastname = input("Ingrese su apellido: ")
        mail = input("Ingrese su correo: ")
        new_User = Usuario(user, password, name, lastname, mail)
        new_User.registrar()

    else:
        print("Opcion no valida")
