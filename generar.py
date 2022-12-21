import json
from entities.cliente import Cliente
usuarioEnSesion = Cliente.verify_session("JoxSam35", "xdalgo2023")
texto_final = ""
for element in usuarioEnSesion._pago:         
    txt= """
    <div class="perfil-usuario-footer">\n
        <ul class="lista-datos">\n
            <li><i class="icono fas fa-shopping-cart"></i> Producto: """+element["Nombre"]+"""</li>\n
        </ul>\n
        <ul class="lista-datos">\n
            <li><i class="icono fas fa-clock"></i> Fecha: """+element["Fecha"]+"""</li>\n
        </ul>\n
    </div>\n

    """
    texto_final += txt

print (texto_final)


# import json

# file_path = "productos.json"

# with open(file_path, "r") as f:
#     usuarios = json.load(f)
# i =0
# for element in usuarios:
#     i=i+1
#     print("function añadir"+str(element["ID"])+"(){")
#     print("    carrito.push(new Producto(\"static/images/menu-"+str(i)+".png\",\""+str(element["Nombre"])+"\","+str(element["Precio"])+",boton"+str(element["ID"])+".id))")
#     print("    ids.push(boton"+str(element["ID"])+".id)")
#     print("}")

#     # print("")
#     # print("    <div class=\"box\">)")
#     # print("        <div class=\"image\">")
#     # print("            <img src=\"static/images/menu-"+str(i)+".png\" alt="">")
#     # print("            <a href=\"#\" class=\"fas fa-heart\"></a>")
#     # print("        </div>")
#     # print("        <div class=\"content\">")
#     # print("            <div class=\"stars\">")
#     # print("                <i class=\"fas fa-star\"></i>")
#     # print("                <i class=\"fas fa-star\"></i>")
#     # print("                <i class=\"fas fa-star\"></i>")
#     # print("                <i class=\"fas fa-star\"></i>")
#     # print("                <i class=\"fas fa-star-half-alt\"></i>")
#     # print("            </div>")
#     # print("            <h3>"+str(element["Nombre"])+"</h3>")
#     # print("            <a id=\""+str(element["ID"])+"\" class=\"btn\">añadir</a>")
#     # print("            <span class=\"price\">s/"+str(element["Precio"])+"</span>")
#     # print("        </div>")
#     # print("    </div>")    
#     # print("")