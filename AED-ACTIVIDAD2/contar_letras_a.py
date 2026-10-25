"""
Programa 3: Contar letras 'a' en una palabra
Descripción: Recorre una palabra ingresada para contar cuántas veces 
contiene la letra 'a' (mayúscula o minúscula).
"""

def main():
    # Entrada
    palabra = input("Ingresa una palabra: ")

    contador = 0

    # Proceso - recorre cada letra con for
    for letra in palabra:
        if letra.lower() == 'a':
            contador += 1

    # Salida
    print(f"La palabra '{palabra}' contiene {contador} letra(s) 'a'.")

if __name__ == "__main__":
    main()