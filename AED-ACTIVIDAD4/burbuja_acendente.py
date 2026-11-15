# Actividad 3.1 - Burbuja Ascendente
# Alumno: Jorge Rocha

n = int(input("¿Cuantos numeros quieres ingresar?: "))
lista = []

for i in range(n):
    num = int(input(f"Numero {i+1}: "))
    lista.append(num)

# Algoritmo burbuja ascendente
for i in range(n-1):
    for j in range(n-1-i):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(f"\nLista ordenada ascendente: {lista}")