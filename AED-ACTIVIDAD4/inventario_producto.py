# Actividad 4.3 - Inventario de productos
inventario = {
    "P001": {"nombre": "Laptop", "precio": 15000, "stock": 3},
    "P002": {"nombre": "Mouse", "precio": 200, "stock": 15},
    "P003": {"nombre": "Teclado", "precio": 500, "stock": 2},
    "P004": {"nombre": "Monitor", "precio": 3000, "stock": 8}
}

# Valor total del inventario
valor_total = sum(d["precio"] * d["stock"] for d in inventario.values())
print(f"Valor total del inventario: ${valor_total}")

# Producto mas caro y mas barato
mas_caro = max(inventario.values(), key=lambda x: x["precio"])
mas_barato = min(inventario.values(), key=lambda x: x["precio"])
print(f"Mas caro: {mas_caro['nombre']} - ${mas_caro['precio']}")
print(f"Mas barato: {mas_barato['nombre']} - ${mas_barato['precio']}")

# Stock bajo (menos de 5)
print("\nProductos con stock bajo (<5):")
for codigo, datos in inventario.items():
    if datos["stock"] < 5:
        print(f"{codigo}: {datos['nombre']} - Stock: {datos['stock']}")