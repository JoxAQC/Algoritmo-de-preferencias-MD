# from flask import Flask, render_template, url_for, request

# app = Flask(__name__)

# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template("index.html")

# @app.route('/result',methods=['POST', 'GET'])
# def result():
#     output = request.form.to_dict()
#     print(output)
#     name = output["name"]

#     return render_template('index.html', name = name)

# if __name__ == "__main__":
#     app.run(debug=True)
from entities.user import Usuario
from entities.tarjeta import Tarjeta
from entities.administrador import Administrador
from entities.cliente import Cliente
from entities.paypal import PayPal
from processes.pago import Pago

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
    

@app.route('/login',methods=['POST', 'GET'])
def iniciar_sesion():
    output = request.form.to_dict()
    print(output)
    usuario = output["usuario"]
    contraseña = output["contraseña"]

    usuarioEnSesion, tipo = buscar_usuario(usuario, contraseña)

    if usuarioEnSesion is None:
        mensaje = "Usuario no registrado, inténtelo nuevamente, por favor"
        return render_template("index.html", mensaje = mensaje)
    else:
        return mostrar_pagina()
    
@app.route('/page')
def mostrar_pagina():
    return render_template("page.html")
    

@app.route('/registrar',methods=['POST', 'GET'])
def registrar():
    output = request.form.to_dict()
    print(output)
    user = output["usuario"]
    password = output["contraseña"]
    name = output["nombre"]
    lastname = output["apellido"]
    mail = output["correo"]

    new_User = Usuario(user, password, name, lastname, mail)
    new_User.registrar()

    register = "Registrado correctamente, inicie sesión para continuar"

    return render_template("index.html", mensaje = register)


@app.route('/profile',methods=['POST', 'GET'])
def mostrar_perfil():
    return render_template("user.html")

if __name__ == "__main__":
    app.run(debug=True)
