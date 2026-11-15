# Actividad 2.6 - Transpuesta 3x3

matriz = []
transpuesta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("Ingresa matriz 3x3 (9 numeros):")
for i in range(3):
    fila = []
    for j in range(3):
        num = int(input(f"Matriz[{i}][{j}]: "))
        fila.append(num)
    matriz.append(fila)

# Calcular transpuesta
for i in range(3):
    for j in range(3):
        transpuesta[j][i] = matriz[i][j]

print("\nMatriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(fila)