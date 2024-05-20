def solicitar_opcion():
    bandera=False

    while bandera==False:
        opcion =input("Ingrese el numero de la opcion que desea seleccionar: ")
        if validar_numero(opcion)==True:
            print("")
            return opcion
        else:
            print("Opcion invalida")

def validar_numero(numero):
    if numero.isdigit()==True:
        return True
    return False