"""Determina si una persona es elegible para votar según su edad, validando si la edad ingresada es negativa o irreal."""

# Constantes
EDAD_MINIMA_VOTAR = 18
EDAD_MAXIMA_REAL = 120

# Entrada de datos
edad = int(input("Ingrese su edad: "))

# Proceso y Salida
if edad < 0 or edad > EDAD_MAXIMA_REAL:
    print("Error: Ingrese una edad válida y real.")
elif edad >= EDAD_MINIMA_VOTAR:
    print(f"Tiene {edad} años. ¡Es elegible para votar!")
else:
    print(f"Tiene {edad} años. No es elegible para votar. (edad mínima: {EDAD_MINIMA_VOTAR} años)")