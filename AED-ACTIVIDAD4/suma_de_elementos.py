# Actividad 2.2 - Suma de elementos

numeros = []

print("Ingresa 5 numeros enteros:")
for i in range(5):
    num = int(input(f"Numero {i+1}: "))
    numeros.append(num)

suma = sum(numeros)

print(f"\nLista: {numeros}")
print(f"La suma total es: {suma}")