from producto import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, stock, vencimiento):
        super().__init__(nombre, precio, stock)
        self.vencimiento = vencimiento

    def calcular_precio_final(self):
        return self._precio / 0.10

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"   ↳ Vencimiento: {self.vencimiento}")

