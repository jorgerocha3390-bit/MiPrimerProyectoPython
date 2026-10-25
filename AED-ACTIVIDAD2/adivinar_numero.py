"""
Programa 6: Adivinar el número
Descripción: Genera un número aleatorio de 1 a 100 y le da pistas al usuario
hasta que logre adivinarlo.
"""
import random

def main():
    # Genera número secreto entre 1 y 100
    secreto = random.randint(1, 100)
    intentos = 0

    print("¡Adivina el número! Estoy pensando en un número del 1 al 100.")

    while True:
        # Entrada
        intento = int(input("Tu intento: "))
        intentos += 1

        # Proceso con if-elif-else para dar pistas
        if intento < secreto:
            print("Pista: El número es MAYOR. Intenta de nuevo.")
        elif intento > secreto:
            print("Pista: El número es MENOR. Intenta de nuevo.")
        else:
            print(f"¡Correcto! Adivinaste el número {secreto} en {intentos} intentos.")
            break

if __name__ == "__main__":
    main()