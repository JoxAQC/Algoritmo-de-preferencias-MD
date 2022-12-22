from entities.user import Usuario
from entities.tarjeta import Tarjeta
from entities.administrador import Administrador
from entities.cliente import Cliente
from processes.pago import Pago
from processes.preferencia import Preferencia
import json
from bs4 import BeautifulSoup
import requests

def buscar_usuario(user, password):
    usuarioEnSesion = Usuario.verify_session(user, password)
    tipo = "user"
    if usuarioEnSesion is None:
        usuarioEnSesion = Cliente.verify_session(user, password)
        tipo = "client"
    if usuarioEnSesion is None:
        usuarioEnSesion = Administrador.verify_session(user, password)
        tipo = "admin"
    return usuarioEnSesion, tipo

from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

usuarioEnSesion = None  
carrito = []
user = None
password = None
txt = None
txt2 = None
tipo = None

@app.route('/login',methods=['POST', 'GET'])
def iniciar_sesion():
    output = request.form.to_dict()
    print(output)
    global user
    usuario = output["usuario"]
    user = usuario
    global password
    contraseña = output["contraseña"]
    password = contraseña

    global usuarioEnSesion 
    usuarioEnSesion, tipo = buscar_usuario(usuario, contraseña)


    if usuarioEnSesion is None:
        mensaje = "Usuario no registrado, inténtelo nuevamente, por favor"
        global txt
        txt = None
        global txt2
        txt2 = None
        return render_template("index.html", mensaje = mensaje)
    else:
        if tipo == "admin":
            ventaTotal = Administrador.calcularVentaTotal()
            ventaBebidas = Administrador.calcularVentaBebidas()
            ventaComidas = Administrador.calcularVentaComidas()
            porcentajeBebidas = Administrador.calcularPorcentaje(ventaTotal,ventaBebidas)
            porcentajeComidas = Administrador.calcularPorcentaje(ventaTotal,ventaComidas)
            ventaBebidaPotencial, bebida = Administrador.calcularBebidaPotencial()
            ventaComidaPotencial, comida = Administrador.calcularComidaPotencial()
            return render_template("admin.html", bebida = bebida, comida = comida, ventaTotal = "S/"+str(ventaTotal), ventaBebidas = "S/"+str(ventaBebidas), ventaComidas = "S/"+str(ventaComidas), porcentajeBebidas = str(round(porcentajeBebidas,2))+"%", porcentajeComidas = str(round(porcentajeComidas,2))+"%", ventaBebidaPotencial = "S/"+str(ventaBebidaPotencial), ventaComidaPotencial = "S/"+str(ventaComidaPotencial))
        return mostrar_pagina()

# @app.route('/page')
# def mostrar_admin():
    
   
@app.route('/page')
def mostrar_pagina():
    if txt != None and txt2 != None:
        return render_template("page.html", txt = txt, txt2 = txt2)
    else:
        return render_template("page.html")
    

@app.route('/registrar',methods=['POST', 'GET'])
def registrar():
    output = request.form.to_dict()
    user = output["usuario"]
    password = output["contraseña"]
    name = output["nombre"]
    lastname = output["apellido"]
    mail = output["correo"]

    new_User = Usuario(user, password, name, lastname, mail)
    new_User.registrar()

    register = "Registrado correctamente, inicie sesión para continuar"

    return render_template("index.html", register = register)

@app.route('/adminprofile',methods=['POST', 'GET'])
def mostrar_perfil_admin():
    usuario = usuarioEnSesion._usuario
    correo = usuarioEnSesion._correo
    nombre = usuarioEnSesion._nombre
    apellido = usuarioEnSesion._apellido
    admin = "a"
    return render_template("user.html", usuario = usuario, correo = correo, nombre = nombre, apellido = apellido, admin = admin)

@app.route('/profile',methods=['POST', 'GET'])
def mostrar_perfil():
    usuarioEnSesion = Cliente.verify_session(user, password)
    usuario = usuarioEnSesion._usuario
    correo = usuarioEnSesion._correo
    nombre = usuarioEnSesion._nombre
    apellido = usuarioEnSesion._apellido
    texto_final = ""
    try:
        for element in usuarioEnSesion._pago:         
            txt= "------------------------"+element["Nombre"]+"----------------------------------------"+element["Fecha"]+"-----------"
            texto_final += txt

        print (texto_final)

        return render_template("user.html", usuario = usuario, correo = correo, nombre = nombre, apellido = apellido, txt = texto_final)
    except(AttributeError):
       return render_template("user.html", usuario = usuario, correo = correo, nombre = nombre, apellido = apellido)     

    


@app.route('/orden',methods=['POST', 'GET'])
def mostrar_orden():
    return render_template("orden.html")


@app.route('/pagar',methods=['POST', 'GET'])
def pagar():
    output = request.form.to_dict()
    codigo = output["codigo"]
    tarjeta = output["tarjeta"]
    nombre = output["nombre"]
    apellido = output["apellido"]
    emisor = output["emisor"]
    fecha = output["fecha"]
    id = output["ids"].split(",")
    ids = []
    for element in id:
        a = int(element)
        ids.append(a)
    print(ids)

    metPagoIngresado = Tarjeta(tarjeta, fecha, codigo, nombre, apellido, emisor)

    a = metPagoIngresado.verificar()
    b = metPagoIngresado.verificarBloqueo() == False
    c = metPagoIngresado.verificarCaducidad()

    if a and b and c:
        with open("files/productos.json", "r") as f:
            data = json.load(f)

        for element in ids:
            for producto in data:
                if element == producto["ID"]:
                    nuevoPago = Pago(producto["ID"], producto["Nombre"])

                    nuevoPago.registrarTransaccion()
                    pago = nuevoPago.cambiarFormato()
                    nuevo_cliente = Cliente(usuarioEnSesion._usuario, usuarioEnSesion._contrasenia, usuarioEnSesion._nombre, usuarioEnSesion._apellido, usuarioEnSesion._correo, pago)
                    nuevo_cliente.registrar()

        passed = "Pago exitoso"

        tipo1 = "bebida"
        tipo2 = "comida"
        arregloBebidas = Preferencia.clasificarProductos(ids,tipo1)
        arregloComidas = Preferencia.clasificarProductos(ids,tipo2)
        if(len(arregloBebidas)>= 1):
            calificaBebidas = Preferencia.solicitarCalificaciones(arregloBebidas)
            recomendacionesBebidas = Preferencia.calcularRecomendaciones(ids,tipo1,calificaBebidas)
            global txt
            txt = ""
            for element in recomendacionesBebidas:
                txt+=""+element+" "
        if(len(arregloComidas)>= 1):
            calificaComidas = Preferencia.solicitarCalificaciones(arregloComidas)
            recomendacionesComidas = Preferencia.calcularRecomendaciones(ids,tipo2,calificaComidas)
            global txt2
            txt2 = ""
            for element in recomendacionesComidas:
                txt2+=element+" "
        return render_template("orden.html", passed = passed)
    else:
        mensaje = "Compruebe la información de su método de pago e inténtalo de nuevo"

    return render_template("orden.html", mensaje = mensaje)


if __name__ == "__main__":
    app.run(debug=True)
