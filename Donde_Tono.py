import json
from datetime import datetime

class Pedido:
    def __init__(self, mesa, producto, cantidad):
        self.mesa = mesa
        self.producto = producto 
        self.cantidad = cantidad

    def calcular_total(self):
        return self.producto.precio * self.cantidad

    def ticket_cocina(self):
        print("---Ticket Cocina---")
        print(f"Mesa | {self.mesa}")
        print(f"Producto | {self.producto.nombre} | {self.cantidad}")

    def ticket_caja(self):
        print("---Ticket caja---")
        print(f"Mesa | {self.mesa}")
        print(f"Producto | {self.producto.nombre} | {self.cantidad} | {self.producto.precio}")
        print(f"Total | {self.calcular_total()}")

class Mesa:
    def __init__(self, numero):
        self.numero=numero
        self.pedidos=[]
    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)
    def total_mesa(self):
        total=0
        for pedido in self.pedidos:
            total += pedido.calcular_total()
        return total
    def resumen(self):
        print(f"Mesa N°{self.numero}")
        print("Pedidos: ")

        for pedido in self.pedidos:
            print(f"{pedido.cantidad} x {pedido.producto} - {pedido.calcular_total()}")

        print(f"Total actual: {self.total_mesa()}")
    def ticket_total(self):
        print("---Ticket total---")
        print(f"Mesa N°{self.numero}")

        for pedido in self.pedidos:
            print(f"{pedido.producto} x{pedido.cantidad} - ${pedido.calcular_total()}")

        print("------------------")
        print(f"TOTAL: ${self.total_mesa()}")
    
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria
    def mostrar(self):
        print(f"{self.nombre} ${self.precio} ({self.categoria})")
    def aplicar_descuento(self):
        print("---Menu descuentos---")
        print("1. Dia de las Madres\n2. Cumpleaños\n3. Cliente 1000\n")
        desc=input("> ")
        if desc == "1":
            nuevoprecio=0
            nuevoprecio=self.precio-((25/100)*self.precio)
            self.precio=nuevoprecio
        elif desc == "2":
            nuevoprecio=0
            nuevoprecio=self.precio-((50/100)*self.precio)
            self.precio=nuevoprecio
        elif desc == "3":
            nuevoprecio=0
            nuevoprecio=self.precio-((90/100)*self.precio)
            self.precio=nuevoprecio
        else:
            print("Descuento no valido")

class ColaPedidos:

    PRIORIDADES={
        "Salchipapa":2,
        "Coca Cola":3,
        "Pizza":1,
        "Papa rellena":3,
        "Lasaña":1
    }
       
    def __init__(self):
        self.cola=[]
    def encolar(self, pedido):
        prio=self.PRIORIDADES.get(pedido.producto.nombre, 2)
        ahora =  datetime.now()
        entrada = (prio, ahora, pedido)
        pos = 0
        while pos < len(self.cola) and (self.cola[pos][0] < prio or (self.cola[pos][0] == prio and self.cola[pos][1] <= ahora)):
            pos += 1
        self.cola.insert(pos, entrada)
    def procesar_siguiente(self):
        if not self.cola:
            print("No hay pedidos en cola")
        else:
            prio, hora, pedido = self.cola.pop(0)
            print(f"Procesando el pedido {pedido.producto.nombre} con prioridad {prio} en la hora {hora.strftime('%H:%M:%S')}")
            pedido.ticket_cocina()
            return pedido
    def ver_cola(self):
        if not self.cola:
            print("NO HAY COLA")
        else:
            print("----COLA PEDIDOS----")
            for i, (p, hora, ped) in enumerate(self.cola, 1):
                e= ["INMEDIATO","MEDIA","BAJA"][p-1]
                print(f"{i}. [{e}] Mesa {ped.mesa} ({hora.strftime('%H:%M:%S')}): {ped.producto.nombre}")
    def estadisticas(self):
        """Cuenta pedidos por producto en cola"""
        
        conteo = {}

        for prio, hora, pedido in self.cola:
            conteo[pedido.producto.nombre] = conteo.get(pedido.producto.nombre, 0) + 1

        print("\n PEDIDOS EN COLA:")
        
        if not conteo:
            print("No hay pedidos")
            return

        for prod, cant in conteo.items():
            print(f"{prod:15}: {cant} pedido(s)")

#Adaptacion a la actividad en el CMAD

def guardar_datos():
    data = {}

    for num, mesa in mesas.items():
        data[num] = []
        for p in mesa.pedidos:
            data[num].append({
                "producto": p.producto.nombre,
                "precio": p.producto.precio,
                "categoria": p.producto.categoria,
                "cantidad": p.cantidad
            })

    with open("mesas.json", "w") as f:
        json.dump(data, f)


def cargar_datos():
    try:
        with open("mesas.json", "r") as f:
            data = json.load(f)

            for num, pedidos in data.items():
                mesa = Mesa(int(num))

                for p in pedidos:
                    prod = Producto(p["producto"], p["precio"], p["categoria"])
                    pedido = Pedido(int(num), prod, p["cantidad"])
                    mesa.agregar_pedido(pedido)

                mesas[int(num)] = mesa
    except:
        pass


cola=ColaPedidos()
mesas={}

cargar_datos()

def menu():
    print("----Donde Toño----")
    print("1. Crear Pedido\n2. Ver cola de la cocina\n3. Procesar el pedido\n4. Ver cuenta de la mesa\n5. Salir\n")

def menuped():
    print("----Menu----")
    print("1. Salchipapa | $5000\n2. Coca Cola | $2000\n3. Pizza | $20000\n4. Papa rellena | $2000\n5. Lasaña | $15000\n")
    opcped=input("> ")

    mesa=int(input("Numero de mesa: "))
    cantidad=int(input("Cantidad: "))

    if opcped == "1":
        producto = Producto("Salchipapa", 5000, "Comida")
    elif opcped == "2":
        producto = Producto("Coca Cola", 2000, "Bebida")
    elif opcped == "3":
        producto = Producto("Pizza", 20000, "Comida")
    elif opcped == "4":
        producto = Producto("Papa rellena", 2000, "Comida")
    elif opcped == "5":
        producto = Producto("Lasaña", 15000, "Comida")
    else:
        print("Opcion no valida!")
        
    print("¿Aplicar descuento? (s/n)")
    desc = input("> ")

    if desc.lower() == "s":
        producto.aplicar_descuento()

    pedido = Pedido(mesa, producto, cantidad)

    if mesa not in mesas:
        mesas[mesa] = Mesa(mesa)

    mesa_obj = mesas[mesa]
    mesa_obj.agregar_pedido(pedido)

    cola.encolar(pedido)

    return pedido


while True:
    menu()
    opc=input("> ")
    if opc == "1":
        menuped()
        print("Pedido Almacenado!")
    elif opc == "2":
        cola.ver_cola()
    elif opc == "3":
        cola.procesar_siguiente()
    elif opc == "4":

        num = int(input("Numero de mesa: "))
        
        if num in mesas:
            mesas[num].ticket_total()
        else:
            print("Esa mesa no tiene pedidos!")
    elif opc == "5":
        guardar_datos()
        print("Cambios guardados")
        break
    else:
        print("Opcion no valida!")