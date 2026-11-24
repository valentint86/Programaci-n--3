class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self._precio = precio
        self.__stock = stock

    def get_stock(self):
        return self.__stock

    def set_stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            print("Error: El stock no puede ser negativo.")

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a vender debe ser mayor a cero.")
            return False
        
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            print(f"Venta exitosa: {cantidad} unidades de {self.nombre}.")
            return True
        else:
            print(f"Stock insuficiente para {self.nombre}. Stock actual: {self.__stock}, solicitado: {cantidad}.")
            return False

    def reponer(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad
            print(f"Reposición exitosa: Se agregaron {cantidad} unidades de {self.nombre}. Stock actual: {self.__stock}")
        else:
            print("La cantidad a reponer debe ser mayor a cero.")

    def calcular_precio_final(self):
        return self._precio

    def mostrar_datos(self):
        tipo_prod = type(self).__name__
        print(f"Tipo: {tipo_prod} | Nombre: {self.nombre} | Precio Base: ${self._precio:,.2f} | Stock: {self.__stock}")
