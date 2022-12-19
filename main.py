from entities.user import Usuario
from entities.tarjeta import Tarjeta
from entities.administrador import Administrador
from entities.cliente import Cliente
from entities.paypal import PayPal
from processes.pago import Pago
from entities.productos import Producto
from processes.carrito import Carrito
from processes.preferencia import Preferencia
from entities.Registro import Registro

def menu():
    menu = """
    ---------BIENVENIDOS AL CAFE PELUCHE STAR----------
    1.- Iniciar Sesion
    2.- Registrarse
    Elija una opcion: """
    option = int(input(menu))
    if option == 1:
        usuarioEnSesion, tipo = buscar_usuario()
        while usuarioEnSesion == None:
            print("     No tenemos a ese usuario registrado, intentelo de nuevo")
            usuarioEnSesion, tipo = buscar_usuario()
        if tipo == "admin":
            menu_admin(usuarioEnSesion)
        else:
            menu_usuarios(usuarioEnSesion)

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


def buscar_usuario():
    user = input("      Usuario: ")
    password = input("      Contrasenia: ")
    usuarioEnSesion = Usuario.verify_session(user, password)
    tipo = "user"
    if usuarioEnSesion is None:
        usuarioEnSesion = Cliente.verify_session(user, password)
        tipo = "client"
    if usuarioEnSesion is None:
        usuarioEnSesion = Administrador.verify_session(user, password)
        tipo = "admin"
    return usuarioEnSesion, tipo


def menu_admin(usuarioEnSesion):
    menu = """
    1.- Reporte de Ventas
    2.- Mostrar Cátalogo de Productos 
    Elija una opcion: """
    option = int(input(menu))
    if option == 1:
        ventaTotal = Administrador.calcularVentaTotal()
        ventaBebidas = Administrador.calcularVentaBebidas()
        ventaComidas = Administrador.calcularVentaComidas()
        porcentajeBebidas = Administrador.calcularPorcentaje(ventaTotal,ventaBebidas)
        porcentajeComidas = Administrador.calcularPorcentaje(ventaTotal,ventaComidas)
        print("---------REPORTE DE VENTAS-----------")
        print("--> Venta Total = S/ ",ventaTotal)
        print("--> Venta Bebidas = S/ ",ventaBebidas)
        print("--> Venta Comidas = S/ ",ventaComidas)
        print("--> % Venta Bebidas sobre el Total= "+str(porcentajeBebidas)+"%")
        print("--> % Venta Comidas sobre el Total= "+str(porcentajeComidas)+"%")
        ventaBebidaPotencial = Administrador.calcularBebidaPotencial()
        print("--> Venta Bebida más vendida= S/ ",ventaBebidaPotencial)

    elif option == 2:
        pass

    else:
        print("Opcion no valida")


def menu_usuarios(usuarioEnSesion):
    menu = """
    1.- Actualizar Datos
    2.- Comprar
    Elija una opcion: """
    op = int(input(menu))

    if op == 1:
        usuarioEnSesion.actualizarDatos()
    elif op == 2:
        Producto.mostrarProducto()
        #Se selecciona el pedido
        CantidadPedir = int(input("Cantidad de productos a pedir: "))
        numPedidos = Carrito.pedirProductos(CantidadPedir)
        Monto = Carrito.calcularMonto(numPedidos)
        print("MONTO A PAGAR = " + str(Monto))
        new_Pedido = Registro(numPedidos,Monto)
        new_Pedido.registrar()
        

        menuPago = """
        Seleccione el metodo de pago:
        1.- Tarjeta VISA/Mastercard
        2.- PayPal
        Elija una opcion: """

        opSelec = int(input(menuPago))

        if opSelec == 1:
            metPago = "Tarjeta"
            print("Ingresar los datos de la tarjeta:")
            nombreTarjeta = input("Nombre: ")
            apellidoTarjeta = input("Apellido: ")
            numeroTarjeta = int(input("Tarjeta: "))

            while len(str(numeroTarjeta)) != 16:
                print("El numero de tarjeta debe contener 16 digitos")
                numeroTarjeta = int(input("Tarjeta: "))

            codigoTarjeta = int(input("Codigo de seguridad (CVV): "))

            while len(str(codigoTarjeta)) != 3:
                print("El codigo de verificación debe contener 3 digitos")
                codigoTarjeta = int(input("Tarjeta: "))

            emisorTarjeta = input("Emisor: ")
            fechaCaducidadTarjeta = input("Fecha Caducidad: ")

            metPagoIngresado = Tarjeta(numeroTarjeta, fechaCaducidadTarjeta, codigoTarjeta, nombreTarjeta, apellidoTarjeta, emisorTarjeta)
            cuenta = metPagoIngresado._numTarjeta

        elif opSelec == 2:
            metPago = "PayPal"
            correoPayPal = input("Ingrese su correo:")
            contraseniaPayPal = input("Ingrese su contrasenia:")

            metPagoIngresado = PayPal(correoPayPal, contraseniaPayPal)
            cuenta = metPagoIngresado._correoPayPal

        a = metPagoIngresado.verificar()
        b = metPagoIngresado.verificarBloqueo() == False
        c = metPagoIngresado.verificarCaducidad()

        if a and b and c:
         
            nuevoPago = Pago(numPedidos, Monto, metPago, cuenta)

            if nuevoPago.pagar():
                nuevoPago.registrarTransaccion()
                print("Pago exitoso")
                pago = nuevoPago.cambiarFormato()
                nuevo_cliente = Cliente(usuarioEnSesion._usuario, usuarioEnSesion._contrasenia, usuarioEnSesion._nombre, usuarioEnSesion._apellido, usuarioEnSesion._correo, metPago, pago)
                nuevo_cliente.registrar()

                tipo1 = "bebida"
                tipo2 = "comida"
                arregloBebidas = Preferencia.clasificarProductos(numPedidos,tipo1)
                arregloComidas = Preferencia.clasificarProductos(numPedidos,tipo2)
                if(len(arregloBebidas)>= 1):
                    calificaBebidas = Preferencia.solicitarCalificaciones(arregloBebidas)
                    recomendacionesBebidas = Preferencia.calcularRecomendaciones(numPedidos,tipo1,calificaBebidas)
                    print("Le recomendamos las sgtes. "+tipo1+"s: ")
                    for element in recomendacionesBebidas:
                        print("--> "+element," ")
                if(len(arregloComidas)>= 1):
                    calificaComidas = Preferencia.solicitarCalificaciones(arregloComidas)
                    recomendacionesComidas = Preferencia.calcularRecomendaciones(numPedidos,tipo2,calificaComidas)
                    print("Le recomendamos las sgtes. "+tipo2+"s: ")
                    for element in recomendacionesComidas:
                        print("--> "+element," ")

        else:
            print("Compruebe la información de su " + metPago + "   e inténtalo de nuevo")


if __name__ == "__main__":
    menu()
