from os import system
system("cls")

concepcion=[]
chiguayante=[]
talcahuano=[]
hualpen=[]
san_pedro=[]
sectores=[concepcion, chiguayante, talcahuano, hualpen, san_pedro]
pedidos=[]

def registrar_pedido():
    nombre=input("Ingrese su nombre y apellido: ")
    direccion=input("Ingrese su direccion: ")
    while True:
        sector=input("Ingrese su sector: ")
        if sector=="concepcion":
            break
        else:
            if sector=="chiguayante":
                break
            else:
                if sector=="talcahuano":
                    break
                else:
                    if sector=="hualpen":
                        break
                    else:
                        if sector=="san pedro":
                            break
                        else:
                            print("Sector invalido")
    while True:
        disp_6=int(input("Cuantos dispensadores de 6 litros desea llevar: "))
        disp_10=int(input("Cuantos dispensadores de 10 litros desea llevar: "))
        disp_20=int(input("Cuantos dispensadores de 20 litros desea llevar: "))
        vali=disp_6+disp_10+disp_20
        if vali == 0:
            print("Debe ordenar almenos un dispensador...")
        else:
            break
        system("cls")
    print("Pedido tomado...")
    mostrar_pedido=[nombre,direccion,sector,disp_6,disp_10,disp_20]
    pedidos.append(mostrar_pedido)


def listar_pedidos():
    print(pedidos)

def imprimir_hoja_ruta():
    archivo=open("archivo.csv", "w")

def buscar_pedido_id():
    print("Trabajo en proceso...")

print("Bienvenido a CleanWasser")
while True: #MENU
    print('''
    1. Registrar pedido
    2. Listar los todos los pedidos
    3. Imprimir hoja de ruta
    4. Buscar un pedido por ID
    5. Salir del programa
        ''')
    op=input("Ingrese una opcion: ")
    match op:
        case "1":
            system("cls")
            registrar_pedido()
        case "2":
            system("cls")
            listar_pedidos()
        case "3":
            system("cls")
            imprimir_hoja_ruta()
            print("Trabajo en proceso...")
        case "4":
            system("cls")
            buscar_pedido_id()
        case "5":
            break
system("cls")
print("ADIOS!!!")
