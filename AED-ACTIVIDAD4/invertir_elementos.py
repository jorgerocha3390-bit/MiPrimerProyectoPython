# Actividad 2.4 - Invertir lista

numeros = []

print("Ingresa 6 numeros enteros:")
for i in range(6):
    num = int(input(f"Numero {i+1}: "))
    numeros.append(num)

print(f"\nLista original: {numeros}")
numeros.reverse() # o numeros[::-1]
print(f"Lista invertida: {numeros}")