"""
Programa 3: Generar secuencia de cuadrados (con do-while simulado)
Descripción: Imprime los cuadrados de 1 a N utilizando do-while simulado.
"""

def main():
    # Entrada
    n = int(input("Ingresa el valor de N: "))

    print(f"\nCuadrados del 1 al {n}:")

    i = 1

    # Simulación de do-while
    while True:
        # Acción - se ejecuta al menos una vez
        cuadrado = i ** 2
        print(f"{i}^2 = {cuadrado}")

        i += 1

        # Condición al final
        if i > n:
            break

if __name__ == "__main__":
    main()