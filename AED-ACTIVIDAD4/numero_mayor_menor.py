# Actividad 2.3 - Mayor y menor

numeros = []

print("Ingresa 8 numeros enteros:")
for i in range(8):
    num = int(input(f"Numero {i+1}: "))
    numeros.append(num)

mayor = max(numeros)
menor = min(numeros)

print(f"\nLista: {numeros}")
print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")