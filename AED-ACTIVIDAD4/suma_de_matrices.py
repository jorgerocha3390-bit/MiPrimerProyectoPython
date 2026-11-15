# Actividad 2.5 - Suma de matrices 2x2

matrizA = []
matrizB = []
matrizC = [[0, 0], [0, 0]]

print("Matriz A (2x2):")
for i in range(2):
    fila = []
    for j in range(2):
        num = int(input(f"A[{i}][{j}]: "))
        fila.append(num)
    matrizA.append(fila)

print("\nMatriz B (2x2):")
for i in range(2):
    fila = []
    for j in range(2):
        num = int(input(f"B[{i}][{j}]: "))
        fila.append(num)
    matrizB.append(fila)

# Suma
for i in range(2):
    for j in range(2):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]

print("\nMatriz resultante (A + B):")
for fila in matrizC:
    print(fila)