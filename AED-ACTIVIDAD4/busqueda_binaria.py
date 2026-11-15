# Actividad 3.4 - Busqueda Binaria

n = int(input("¿Cuantos numeros tiene la lista?: "))
lista = []
for i in range(n):
    lista.append(int(input(f"Numero {i+1}: ")))

lista.sort() # Requisito: debe estar ordenada
print(f"Lista ordenada: {lista}")

buscar = int(input("Numero a buscar: "))

# Algoritmo busqueda binaria
inicio = 0
fin = len(lista) - 1
encontrado = False

while inicio <= fin:
    medio = (inicio + fin) // 2
    if lista[medio] == buscar:
        print(f"El numero {buscar} se encontro en la posicion {medio}")
        encontrado = True
        break
    elif lista[medio] < buscar:
        inicio = medio + 1
    else:
        fin = medio - 1

if not encontrado:
    print(f"El numero {buscar} no esta en la lista")