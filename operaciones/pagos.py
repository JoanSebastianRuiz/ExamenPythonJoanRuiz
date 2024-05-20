from datetime import *
from datos.manejo_archivos import *
from datos.validaciones import *

def registrar_pago(datos):
    bandera=False
    datos_pedidos=cargar_pedidos(RUTA_REGISTRO_PEDIDOS)
    documento_encontrado=False

    while bandera==False:
        documento=input("Ingrese el documento del pedido al que le quiere registrar el pago: ")
        if validar_numero(documento)==True and len(documento)>=8 and len(documento)<=10:
            bandera=True
        else:
            print("Datos invalidos")
            print("")
    bandera=False

    for diccionario in datos_pedidos:
        if diccionario["documento"]==documento and diccionario["pago"]==False:
            fecha=datetime.now().strftime("%d-%m-%Y %H:%M")
            cadena=fecha+"   "+documento+"   $"+str(diccionario["precio total"])
            registrar_venta(datos,cadena)
            diccionario["pago"]=True
            documento_encontrado=True
            subir_pedidos(RUTA_REGISTRO_PEDIDOS,datos_pedidos)
            print("El pago se ha registrado correctamente")
            print("")
            break

        elif diccionario["documento"]==documento and diccionario["pago"]==True:
            documento_encontrado=True
            print("El pedido ya se encuentra pagado")
            print("")
            break

    
    if documento_encontrado==False:
        print("El documento ingresado no se encuentra registrado en la lista de pedidos")
        print("")
