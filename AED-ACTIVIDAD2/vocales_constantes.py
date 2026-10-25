"""
Programa 7: Vocales o consonantes
Descripción: Evalúa caracteres individuales hasta que se ingrese un espacio.
"""

def main():
    print("Ingresa caracteres uno por uno. Ingresa un espacio ' ' para salir.")

    while True:
        caracter = input("Ingresa un caracter: ")

        # Condición de salida
        if caracter == ' ':
            print("Programa terminado. Ingresaste un espacio.")
            break

        # Validar que solo sea un caracter
        if len(caracter) != 1:
            print("Por favor ingresa solo UN caracter.")
            continue

        # Proceso con if-elif
        if caracter.lower() in 'aeiou':
            print(f"'{caracter}' es una VOCAL.")
        elif caracter.isalpha():
            print(f"'{caracter}' es una CONSONANTE.")
        else:
            print(f"'{caracter}' no es una letra.")

if __name__ == "__main__":
    main()