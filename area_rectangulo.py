"""Programa que calcula el área de un rectángulo a partir de datos del usuario."""

def main():
    # Entrada de datos
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))

    # Proceso
    area = base * altura

    # Salida
    print(f"El área del rectángulo es: {area:.2f}")

if __name__ == "__main__":
    main()