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
            
def registrar_pedido(datos_pedidos):
    bandera=False
    informacion_pedido={}
    while bandera==False:
        documento=input("Ingrese su documento: ")
        if validar_numero(documento)==True and len(documento)>=8 and len(documento)<=10:
            bandera=True
        else:
            print("documento invalido")
            print("")


    for diccionario in datos_pedidos:
        if diccionario["documento"]==documento and diccionario["pago"]==False:
            print("No puede realizar mas pedidos hasta que realice el pago del pedido que tiene registrado")
            print("")
            return False
        
        elif diccionario["documento"]==documento and diccionario["pago"]==True:
            diccionario["pago"]=False
            lista=lista_pedido()
            if lista==False:
                print("Su lista de productos se ha cancelado")
                print("")
                return False
            
            diccionario["productos"]=lista
            precio_total=0
            for diccionario in lista:
                precio_total+=int(diccionario["precio"])
            diccionario["precio total"]=precio_total
            subir_pedidos(datos_pedidos)
            return True

    informacion_pedido["documento"]=documento
    informacion_pedido["pago"]=False

    lista=lista_pedido()
    if lista==False:
        print("Su lista de productos se ha cancelado")
        print("")
        return False
    
    informacion_pedido["productos"]=lista
    precio_total=0
    for diccionario in lista:
        precio_total+=int(diccionario["precio"])
    informacion_pedido["precio total"]=precio_total
    print("El pedido se ha registrado correctamente")
    print("")
    return informacion_pedido


def cancelar_pedido(datos_pedidos):
    bandera=False
    documento_encontrado=False

    while bandera==False:
        documento=input("Ingrese el documento al que esta relacionado el pedido que quiere cancelar: ")
        if validar_numero(documento)==True and len(documento)>=8 and len(documento)<=10:
            bandera=True
        else:
            print("Documento invalido")
            print("")

    for diccionario in datos_pedidos:
        if diccionario["documento"]==documento and diccionario["pago"]==False:
            return diccionario
        
        elif diccionario["documento"]==documento and diccionario["pago"]==True:
            print("El pedido no se puede cancelar porque ya ha sido pagado")
            print("")
            return False
            
    
    if documento_encontrado==False:
        print("El documento ingresado no se encuentra asociado a ningun pedido")
        print("")
        return False


def modificar_pedido(datos_pedidos):
    bandera=False
    
    while bandera==False:
        documento=input("Ingrese el documento asociado al pedido que quiere modificar: ")
        if validar_numero(documento)==True and len(documento)>=8 and len(documento)<=10:
            bandera=True
        else:
            print("Documento invalido")
            print("")


    for diccionario in datos_pedidos:
        if diccionario["documento"]==documento and diccionario["pago"]==True:
            print("No se puede modificar el pedido porque ya se ha realizado el pago")
            print("")
            return False
        
        elif diccionario["documento"]==documento and diccionario["pago"]==False:
            lista=lista_pedido()
            if lista==False:
                return False
            
            diccionario["productos"]=lista
            precio_total=0
            for diccionario in lista:
                precio_total+=int(diccionario["precio"])
            diccionario["precio total"]=precio_total
            return datos_pedidos


    print("El documento ingresado no se encuentra asociado a ningun pedido")
    print("")
    return False



    


