"""
Programa 5: Contador de dígitos
Descripción: Solicita un número entero y determina su número total de dígitos.
"""

def main():
    # Entrada
    numero = int(input("Ingresa un número entero: "))

    # Caso especial para el 0
    if numero == 0:
        total_digitos = 1
    else:
        total_digitos = 0
        n = abs(numero)  # abs para que funcione con negativos

        # Proceso con while
        while n > 0:
            n = n // 10  # le quitas un dígito cada vuelta
            total_digitos += 1

    # Salida
    print(f"El número {numero} tiene {total_digitos} dígito(s).")

if __name__ == "__main__":
    main()