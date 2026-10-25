"""
Programa 6: Convertidor de temperatura
"""
temp = float(input("Ingrese la temperatura en °C: "))
opcion = int(input("Convertir a: 1=Fahrenheit, 2=Kelvin: "))

match opcion:
    case 1:
        f = (temp * 9/5) + 32
        print(f"{temp}°C = {f:.2f}°F")
    case 2:
        k = temp + 273.15
        print(f"{temp}°C = {k:.2f}K")
    case _:
        print("Error: Opción inválida. Elija 1 o 2.")