"""
Programa 1: Factorial de un número
Descripción: Calcula el factorial de un número entero ingresado por el usuario.
"""

def main():
    # Entrada de datos
    numero = int(input("Ingresa un número entero no negativo: "))

    # Proceso
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i

    # Salida
    print(f"El factorial de {numero} es: {factorial}")

if __name__ == "__main__":
    main()
