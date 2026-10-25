"""Programa que calcula el promedio de tres números ingresados por el usuario."""

def main():
    # Entrada de datos
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    # Proceso
    promedio = (num1 + num2 + num3) / 3

    # Salida
    print(f"El promedio de los tres números es: {promedio:.2f}")

if __name__ == "__main__":
    main()