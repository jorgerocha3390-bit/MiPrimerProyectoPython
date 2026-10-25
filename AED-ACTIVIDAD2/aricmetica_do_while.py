"""
Programa 4: Generar una secuencia aritmética (con do-while simulado)
Descripción: Construye una progresión aritmética dados el primer término,
la diferencia y el valor límite.
"""

def main():
    # Entradas
    a1 = float(input("Ingresa el primer término (a1): "))
    d = float(input("Ingresa la diferencia (d): "))
    limite = float(input("Ingresa el valor límite: "))

    print(f"\nProgresión aritmética desde {a1} con diferencia {d} hasta {limite}:")

    termino = a1

    # Simulación de do-while
    while True:
        # Acción - se ejecuta al menos una vez
        # Validamos si aún está dentro del límite según si la progresión es creciente o decreciente
        if (d >= 0 and termino > limite) or (d < 0 and termino < limite):
            break
            
        print(termino, end=" ")

        termino += d

        # Condición de salida al final (lógica extra por si d es positiva o negativa)
        if (d > 0 and termino > limite) or (d < 0 and termino < limite) or (d == 0):
            # Si d == 0, solo imprimimos una vez para no caer en ciclo infinito
            if d == 0:
                break
            # La condición principal ya se valida al inicio de la siguiente vuelta
            # pero dejamos este break para estructura do-while clara
            if (d > 0 and termino > limite) or (d < 0 and termino < limite):
                break

    print()

if __name__ == "__main__":
    main()