from producto import Producto

class Ropa(Producto):
    def __init__(self, nombre, precio, stock, talle, categoria):
        super().__init__(nombre, precio, stock)
        self.talle = talle
        self.categoria = categoria

    def mostrar_talle(self):
        return self.talle

    def calcular_precio_final(self):
        return self._precio / 0.15

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"   ↳ Categoría: {self.categoria} | Talle: {self.talle}")
