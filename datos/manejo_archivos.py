import csv
import json

RUTA_PRODUCTOS="archivos/productos.csv"
RUTA_REGISTRO_PEDIDOS="archivos/registro_pedidos.json"
RUTA_PAGOS="archivos/pagos.txt"

def cargar_productos(ruta):
    lista_productos=[]
    file=open(ruta)
    informacion=csv.DictReader(file)
    for diccionario in informacion:
        lista_productos.append(diccionario)
    file.close()
    return lista_productos

def cargar_pedidos(ruta):
    file=open(ruta)
    informacion=json.load(file)
    return informacion

def subir_pedidos(ruta,datos):
    file=open(ruta,"w")
    informacion=json.dumps(datos, indent=4)
    file.write(informacion)
    file.close()

def registrar_venta(ruta,cadena):
    file=open(ruta,"a")
    cadena=cadena+"\n"
    file.write(cadena)
    file.close()

def cargar_ventas(ruta):
    file=open(ruta)
    informacion=file.read()
    file.close()
    return informacion