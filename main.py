"""
gestion de pedidos y ventas de productos de maquillaje
Permitir modificacion de pedidos o cancelacion solo si no se han pagado

"""
from datetime import *
from datos.menus import *
from datos.manejo_archivos import *
from datos.validaciones import *
from operaciones.pedidos import *
from operaciones.consultas import *
from operaciones.pagos import *

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
        try:
            datos=RUTA_PAGOS
            registrar_pago(datos)
        except Exception:
            print("Datos erroneos")
            print("")

    elif opcion=="3":
        while bandera==False:
            menu_consulta()
            opcion=solicitar_opcion()
            
            if opcion=="1":
                try:
                    datos=cargar_pedidos(RUTA_REGISTRO_PEDIDOS)
                    consultar_pedidos(datos)
                except Exception:
                    print("Datos erroneos")
                    print("")

            elif opcion=="2":
                try:
                    datos=cargar_pedidos(RUTA_REGISTRO_PEDIDOS)
                    consultar_pedidos_documento(datos)
                except Exception:
                    print("Datos erroneos")
                    print("")

            elif opcion=="3":
                try:
                    datos=RUTA_PAGOS
                    consultar_pagos(RUTA_PAGOS)
                except Exception:
                    print("Datos erroneos")
                    print("")

            elif opcion=="4":
                bandera=True

            else:
                print("Numero de opcion fuera de rango")
                print("")
        bandera=False

    elif opcion=="4":
        print("¿Esta seguro que quiere finalizar el programa?")
        print("1. Si")
        print("2. No")

        while bandera==False:
            opcion=solicitar_opcion()
            if opcion=="1" or opcion=="2":
                bandera=True
            else:
                print("Numero de opcion fuera de rango")
        bandera=False

        if opcion=="1":
            bandera=True
        elif opcion=="2":
            bandera=False
    else:
        print("Numero de opcion fuera de rango")
        print("")

