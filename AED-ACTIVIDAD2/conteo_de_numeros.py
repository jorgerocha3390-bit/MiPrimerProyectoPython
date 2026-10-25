"""
Programa 2: Conteo de números
Descripción: Solicita la cantidad de números e identifica cuántos son
mayores, menores o iguales a cero usando if-elif-else dentro de for.
"""

def main():
    # Entrada
    cantidad = int(input("¿Cuántos números vas a ingresar?: "))

    mayores = 0
    menores = 0
    iguales = 0

    # Proceso con for + if-elif-else
    for i in range(cantidad):
        num = float(input(f"Ingresa el número {i+1}: "))

        if num > 0:
            mayores += 1
        elif num < 0:
            menores += 1
        else:
            iguales += 1

    # Salida
    print(f"\nResultados:")
    print(f"Mayores que cero: {mayores}")
    print(f"Menores que cero: {menores}")
    print(f"Iguales a cero: {iguales}")

if __name__ == "__main__":
    main()