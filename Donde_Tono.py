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
    def agregar_pedido(self, pedido):
        pedidos=[]
        pedidos.append(pedido)
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
    def mostrar():
