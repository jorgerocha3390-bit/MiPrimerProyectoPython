"""
Programa 4: Imprimir números divisibles por 3 y 5
Descripción: Muestra del 1 al 100 los números divisibles entre 3 y 5 simultáneamente.
"""

def main():
    print("Números del 1 al 100 divisibles entre 3 y 5:")
    
    # Recorre del 1 al 100
    for i in range(1, 101):
        # Si el residuo al dividir entre 3 y entre 5 es 0, es divisible por ambos
        if i % 3 == 0 and i % 5 == 0:
            print(i)

if __name__ == "__main__":
    main()