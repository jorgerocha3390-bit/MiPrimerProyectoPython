# Actividad 3.5 - Comparacion de busquedas
# Alumno: Jorge Rocha
import random

# Generar lista de 1000 numeros aleatorios ordenados
lista = sorted([random.randint(1, 10000) for _ in range(1000)])
buscar = random.choice(lista) # Aseguramos que si existe

print(f"Buscando el numero: {buscar} en 1000 elementos")

# Busqueda Lineal con contador
comp_lineal = 0
for i in range(len(lista)):
    comp_lineal += 1
    if lista[i] == buscar:
        break

# Busqueda Binaria con contador
comp_binaria = 0
inicio, fin = 0, len(lista)-1
while inicio <= fin:
    comp_binaria += 1
    medio = (inicio + fin) // 2
    if lista[medio] == buscar:
        break
    elif lista[medio] < buscar:
        inicio = medio + 1
    else:
        fin = medio - 1

print(f"\nComparaciones busqueda lineal: {comp_lineal}")
print(f"Comparaciones busqueda binaria: {comp_binaria}")

# Comentario exigido por la rubrica
"""
Comentario: La busqueda binaria es mas eficiente porque no revisa uno por uno.
En cada paso divide la lista a la mitad, por eso su complejidad es O(log n) 
mientras que la lineal es O(n). En 1000 datos, la lineal puede hacer 1000 
comparaciones, la binaria solo unas 10.
"""