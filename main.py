"""
gestion de pedidos y ventas de productos de maquillaje
Pedidos: estado si ha sido pagado
Al finalizar la seleccion de productos se debe mostrar la orden completa y confirmar el pedido
Pagos: fecha de pago, valor total y identificador del cliente
Permitir modificacion de pedidos o cancelacion solo si no se han pagado
Permitir realizar consultas sobre los pedidos realizados: mostrar todos los pedidos y mostrar un pedido particular
Para hacer un pedido se debe pedir el documento del cliente y si tiene otro pedido hecho solo puede hacer otro 
si ya lo ha pagado (se sobreescriben los pedidos)
Para finalizar el programa se debe pedir confirmacion
Manejo de excepciones y validaciones para que el programa no se detenga

"""
from datos.menus import *
from datos.manejo_archivos import *
from datos.validaciones import *
from operaciones.pedidos import *
from operaciones.consultas import *

bandera=False

while bandera==False:
    menu_principal()
    opcion=solicitar_opcion()

    if opcion=="1":
        try:
            datos=cargar_pedidos(RUTA_REGISTRO_PEDIDOS)
            pedido=registrar_pedido()
            if pedido!=False:
                datos.append(pedido)
                subir_pedidos(RUTA_REGISTRO_PEDIDOS,datos)
                print("El pedido se ha registrado correctamente")
                print("")
            else:
                print("Su lista de productos se ha cancelado")
            
        except Exception:
            print("Datos erroneos")
            print("")

    elif opcion=="2":
        while bandera==False:
            menu_consulta_pedidos()
            opcion=solicitar_opcion()
            datos=cargar_pedidos(RUTA_REGISTRO_PEDIDOS)

            if opcion=="1":
                try:
                    consultar_pedidos(datos)
                except Exception:
                    print("Datos erroneos")
                    print("")
            elif opcion=="2":
                try:
                    consultar_pedidos_documento(datos)
                except Exception:
                    print("Datos erroneos")
                    print("")
            elif opcion=="3":
                bandera=True
            else:
                print("Numero de opcion fuera de rango")
                print("")
        bandera=False

    elif opcion=="4":
        bandera=True
    else:
        print("Numero de opcion fuera de rango")
        print("")
