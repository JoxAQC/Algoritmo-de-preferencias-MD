from processes.preferencia import *
if __name__ == "__main__":
    productosSeleccionados = [3,9,23,21,15,13]
    calificaBebidas = [6,4,8]
    calificaComidas = [8,5,7]
    tipoProducto = "bebida"
    if tipoProducto == "bebida":
        calificaProductos = calificaBebidas
    else: 
        calificaProductos = calificaComidas
    
    recomendaciones = Preferencia.calcularRecomendaciones(productosSeleccionados,tipoProducto,calificaProductos)
    print("Le recomendamos las sgtes. "+tipoProducto+"s: ")
    for element in recomendaciones:
        print(element," ")


    

    
