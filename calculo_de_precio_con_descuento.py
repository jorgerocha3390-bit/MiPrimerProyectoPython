"""
Programa 4: Calculadora de descuentos
Aplica descuento según el monto total de la compra.
"""

# Entrada
total = float(input("Ingrese el total de la compra: $"))

# Proceso y Salida
if total < 0:
    print("Error: El total no puede ser negativo.")
elif total < 100:
    print(f"Total: ${total:.2f} - Sin descuento. Paga: ${total:.2f}")
elif total <= 200:
    descuento = total * 0.10
    print(f"Total: ${total:.2f} - Descuento 10% (${descuento:.2f}). Paga: ${total - descuento:.2f}")
elif total <= 500:
    descuento = total * 0.20
    print(f"Total: ${total:.2f} - Descuento 20% (${descuento:.2f}). Paga: ${total - descuento:.2f}")
else:
    descuento = total * 0.30
    print(f"Total: ${total:.2f} - Descuento 30% (${descuento:.2f}). Paga: ${total - descuento:.2f}")