from producto import Producto
from alimento import Alimento
from electronico import Electronico
from ropa import Ropa

def main():
    leche = Alimento("Leche", 2000, 50, "15/11/2026")
    notebook = Electronico("Notebook", 800000, 10, 12)
    cuaderno = Producto("Cuaderno", 5000, 30)
    remera = Ropa("Remera Básica", 15000, 20, "M", "Remera")
    pantalon = Ropa("Pantalón Jean", 45000, 15, "42", "Pantalón")

    inventario = [leche, notebook, cuaderno, remera, pantalon]

    leche.vender(10)
    
    notebook.vender(15)
   
    notebook.reponer(5)

    valor_total_inventario = 0
    producto_mas_caro = inventario[0]
    max_precio_final = inventario[0].calcular_precio_final()

    for p in inventario:
        p.mostrar_datos()
        precio_final = p.calcular_precio_final() # Polimorfismo en acción
        stock = p.get_stock()
        
        subtotal = stock * precio_final
        valor_total_inventario += subtotal
        
        print(f"   ➔ Precio Final unitario: ${precio_final:,.2f} | Stock actual: {stock} | Subtotal stock: ${subtotal:,.2f}")
        print("-" * 50)

        if precio_final > max_precio_final:
            max_precio_final = precio_final
            producto_mas_caro = p

    print(f"\nVALOR TOTAL DEL INVENTARIO: ${valor_total_inventario:,.2f}")
    print(f"PRODUCTO DE MAYOR PRECIO FINAL: {producto_mas_caro.nombre} (${max_precio_final:,.2f})")


if __name__ == "__main__":
    main()
