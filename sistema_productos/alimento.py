from producto import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, stock, vencimiento):
        super().__init__(nombre, precio, stock)
        self.vencimiento = vencimiento

    def calcular_precio_final(self):
        # Descuento del 10% para alimentos
        return self._precio * 0.90

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"   ↳ Vencimiento: {self.vencimiento}")

