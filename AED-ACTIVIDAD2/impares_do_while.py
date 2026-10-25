"""
Programa 2: Contador de números impares (con do-while simulado)
Descripción: Muestra impares desde 1 hasta N simulando do-while con while True.
"""

def main():
    # Entrada
    n = int(input("Ingresa el valor de N: "))

    print(f"\nNúmeros impares del 1 al {n}:")

    i = 1  # Inicializador
    
    # Simulación de do-while
    while True:
        # Acción (se ejecuta al menos una vez)
        if i % 2 != 0:
            print(i, end=" ")

        i += 1

        # Condición al final (como en do-while)
        if i > n:
            break

    print() # Salto de línea final

if __name__ == "__main__":
    main()