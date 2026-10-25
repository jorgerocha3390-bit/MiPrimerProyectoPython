"""
Programa 3: Evaluación de calificaciones con letras
Asigna una letra (A, B, C, D, F) según la calificación numérica ingresada.
"""

# Entrada de datos
calificacion = float(input("Ingrese la calificación numérica (0-100): "))

# Proceso y Salida
if calificacion < 0 or calificacion > 100:
    print("Error: La calificación debe estar dentro del rango de 0 a 100.")
elif calificacion >= 90:
    print(f"Calificación: {calificacion:.1f} -> Letra: A")
elif calificacion >= 80:
    print(f"Calificación: {calificacion:.1f} -> Letra: B")
elif calificacion >= 70:
    print(f"Calificación: {calificacion:.1f} -> Letra: C")
elif calificacion >= 60:
    print(f"Calificación: {calificacion:.1f} -> Letra: D")
else:
    print(f"Calificación: {calificacion:.1f} -> Letra: F")