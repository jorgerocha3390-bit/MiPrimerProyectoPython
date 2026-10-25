"""Calcula el promedio ponderado de un estudiante a partir de parciales, proyecto y examen final, validando rango 0 a 100."""

# Constantes de ponderación
PORCENTAJE_PARCIALES = 0.40
PORCENTAJE_PROYECTO = 0.30
PORCENTAJE_EXAMEN = 0.30

# Entrada de datos
calif_parciales = float(input("Ingrese la calificación de Parciales (0-100): "))
calif_proyecto = float(input("Ingrese la calificación del Proyecto (0-100): "))
calif_examen = float(input("Ingrese la calificación del Examen Final (0-100): "))

# Proceso y Salida con if-else
if (0 <= calif_parciales <= 100) and (0 <= calif_proyecto <= 100) and (0 <= calif_examen <= 100):
    promedio_final = (calif_parciales * PORCENTAJE_PARCIALES) + (calif_proyecto * PORCENTAJE_PROYECTO) + (calif_examen * PORCENTAJE_EXAMEN)
    print(f"\nLa calificación final del estudiante es: {promedio_final:.2f}")
else:
    print("\nError: Todas las calificaciones deben estar dentro del rango de 0 a 100.")