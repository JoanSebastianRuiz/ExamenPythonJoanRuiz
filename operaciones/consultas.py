from datos.validaciones import *

def consultar_pedidos(datos):
    for diccionario in datos:
        for llave, valor in diccionario.items():
            if llave=="productos":
                print("Productos:")
                num=0
                for diccionario in valor:
                    num+=1
                    print(num,". ",diccionario["producto"])
            else:
                print(f"{llave}: {valor}")
        print("")

def consultar_pedidos_documento(datos):
    bandera=False
    documento_encontrado=False

    while bandera==False:
        documento=input("Ingrese su documento: ")
        if validar_numero(documento)==True and len(documento)>=8 and len(documento)<=10:
            bandera=True
        else:
            print("Opcion invalida")

    for diccionario in datos:
        if diccionario["documento"]==documento:
            documento_encontrado=True
            for llave, valor in diccionario.items():
                if llave=="productos":
                    print("Productos:")
                    num=0
                    for diccionario in valor:
                        num+=1
                        print(num,". ",diccionario["producto"])
                else:
                    print(f"{llave}: {valor}")
            print("")
    
    if documento_encontrado==False:
        print("El documento encontrado no tiene pedidos registrados")