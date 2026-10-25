"""Programa que calcula el Índice de Masa Corporal (IMC) de una persona."""

def main():
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = peso / (altura * altura)
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

if __name__ == "__main__":
    main()