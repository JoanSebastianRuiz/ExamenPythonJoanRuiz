from datos.validaciones import *
from datos.manejo_archivos import *

def imprimir_productos_y_retornar_diccionario(datos):
    diccionario_productos={}
    num_producto=0
    print("Opciones de producto: ")
    for diccionario in datos:
        num_producto+=1
        print(num_producto,". ",diccionario["nombre"],": $",diccionario["precio"])
        diccionario_productos[str(num_producto)]=diccionario["nombre"]
    print("")
    return diccionario_productos

def lista_pedido():
    catalogo_productos=cargar_productos(RUTA_PRODUCTOS)
    pedido_total=[]
    
     
    bandera=False

    while bandera==False:
        while bandera==False:
            diccionario_productos=imprimir_productos_y_retornar_diccionario(catalogo_productos)
            pedido={} 
            while bandera==False:
                opcion=solicitar_opcion()
                if int(opcion)>0 and int(opcion)<=len(diccionario_productos):
                    bandera=True
                else:
                    print("Numero de opcion fuera de rango")

            bandera=False
            pedido["producto"]=diccionario_productos[opcion]

            for diccionario in catalogo_productos:
                if pedido["producto"]==diccionario["nombre"]:
                    pedido["precio"]=diccionario["precio"]
                    break
            pedido_total.append(pedido)

            print("¿Desea agregar otro producto a su pedido?")
            print("1. Si")
            print("2. No")
            
            while bandera==False:
                opcion=solicitar_opcion()
                if opcion=="1" or opcion=="2":
                    bandera=True
                else:
                    print("Numero de opcion fuera de rango")
            if opcion=="1":
                bandera=False
        
        bandera=False
        print("Esta es su lista de productos seleccionados: ")
        num=0
        for diccionario in pedido_total:
            
            for llave, valor in diccionario.items():
                
                if llave=="producto":
                    num+=1
                    print(num,".",llave,":", valor, end=" ")
                elif llave=="precio":
                    print(", ", llave,":", valor)

            

        print("")
        print("¿Desea confirmar su pedido?")
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
            return pedido_total
        elif opcion=="2":
            return False
            
def registrar_pedido():
    datos_pedidos=cargar_pedidos(RUTA_REGISTRO_PEDIDOS)
    bandera=False
    informacion_pedido={}
    while bandera==False:
        documento=input("Ingrese su documento: ")
        if validar_numero(documento)==True and len(documento)>=8 and len(documento)<=10:
            bandera=True
        else:
            print("Opcion invalida")


    for diccionario in datos_pedidos:
        if diccionario["documento"]==documento and diccionario["pago"]==False:
            print("No puede realizar mas pedidos hasta que realice el pago del pedido que tiene registrado")
            return False
        
        elif diccionario["documento"]==documento and diccionario["pago"]==True:
            informacion_pedido["pago"]=False
            lista=lista_pedido()
            if lista==False:
                return False
            
            informacion_pedido["productos"]=lista
            precio_total=0
            for diccionario in lista:
                precio_total+=int(diccionario["precio"])
            informacion_pedido["precio total"]=precio_total
            print("El pedido se ha registrado correctamente")
            print("")
            return informacion_pedido

    informacion_pedido["documento"]=documento
    informacion_pedido["pago"]=False

    lista=lista_pedido()
    if lista==False:
        return False
    
    informacion_pedido["productos"]=lista
    precio_total=0
    for diccionario in lista:
        precio_total+=int(diccionario["precio"])
    informacion_pedido["precio total"]=precio_total
    print("El pedido se ha registrado correctamente")
    print("")
    return informacion_pedido


    

    


    


