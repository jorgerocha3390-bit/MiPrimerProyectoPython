# Actividad 2.1 - Contar pares e impares
# Alumno: Jorge Emilio Rocha Silva

numeros = []
pares = 0
impares = 0

print("Ingresa 10 numeros enteros:")
for i in range(10):
    num = int(input(f"Numero {i+1}: "))
    numeros.append(num)
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nLista ingresada: {numeros}")
print(f"Cantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")