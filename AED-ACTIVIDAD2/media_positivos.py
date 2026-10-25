"""
Programa 8: Calcular la media de números positivos
Descripción: Lee números continuos y calcula el promedio de los positivos,
se detiene cuando se ingresa un número negativo.
"""

def main():
    suma = 0
    contador = 0

    print("Ingresa números positivos. Ingresa un negativo para terminar y calcular el promedio.")

    while True:
        numero = float(input("Ingresa un número: "))

        # Condición de parada
        if numero < 0:
            break
        
        # Solo acumula positivos (ignora el 0 si quieres, o cuéntalo)
        if numero > 0:
            suma += numero
            contador += 1

    # Salida
    if contador > 0:
        promedio = suma / contador
        print(f"\nIngresaste {contador} números positivos.")
        print(f"La suma es: {suma}")
        print(f"El promedio es: {promedio:.2f}")
    else:
        print("\nNo ingresaste ningún número positivo.")

if __name__ == "__main__":
    main()