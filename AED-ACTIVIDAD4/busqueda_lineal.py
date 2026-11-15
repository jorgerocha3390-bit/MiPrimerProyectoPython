# Actividad 3.3 - Busqueda Lineal

n = int(input("¿Cuantos numeros tiene la lista?: "))
lista = []
for i in range(n):
    lista.append(int(input(f"Numero {i+1}: ")))

buscar = int(input("Numero a buscar: "))

posicion = -1
for i in range(len(lista)):
    if lista[i] == buscar:
        posicion = i
        break

if posicion != -1:
    print(f"El numero {buscar} se encontro en la posicion {posicion}")
else:
    print(f"El numero {buscar} no esta en la lista")