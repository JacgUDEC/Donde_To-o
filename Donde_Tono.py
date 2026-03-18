import datetime as dt

class Pedido:
    def __init__(self, mesa, producto, cantidad, precio):
        self.mesa=mesa
        self.producto=producto
        self.cantidad=cantidad
        self.precio=precio
    def calcular_total(self):
        totalprod=self.precio*self.cantidad
        return totalprod
    def ticket_cocina(self):
        print("---Ticket Cocina---")
        print(f"Mesa | {self.mesa}")
        print(f"Producto | {self.producto} | {self.cantidad}")
    def ticket_caja(self):
        print("---Ticket caja---")
        print(f"Mesa | {self.mesa}")
        print(f"Producto | {self.producto} | {self.cantidad} | {self.precio}")
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
    def resumen(self, numero):
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
    def __init__(self):
        self.cola=[]
        self.PRIORIDADES={}
    def encolar(self, pedido):
        self.cola.append(pedido)
    def procesar_siguiente(tiempo):
        dt.timedelta(tiempo)