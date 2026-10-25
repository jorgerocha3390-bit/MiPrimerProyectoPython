"""
Programa 1: Calculadora básica con menú
Descripción: Despliega un menú iterativo para realizar operaciones básicas.
"""

def main():
    while True:
        print("\n--- CALCULADORA BÁSICA ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        # Salir
        if opcion == '5':
            print("¡Hasta luego!")
            break

        # Si no es salir, pide números
        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif opcion == '3':
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif opcion == '4':
                if num2 != 0:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: No se puede dividir entre cero.")
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()