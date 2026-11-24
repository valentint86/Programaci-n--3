from producto import Producto

class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, precio, stock)
        self.garantia_meses = garantia_meses

    def calcular_precio_final(self):
        return self._precio * 1.05

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"   ↳ Garantía: {self.garantia_meses} meses")
