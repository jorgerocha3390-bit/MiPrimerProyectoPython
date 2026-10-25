"""
Programa 5: Estación del año con match-case
"""
mes = int(input("Ingrese el número del mes (1-12): "))

match mes:
    case 12 | 1 | 2:
        print(f"Mes {mes}: Invierno")
    case 3 | 4 | 5:
        print(f"Mes {mes}: Primavera")
    case 6 | 7 | 8:
        print(f"Mes {mes}: Verano")
    case 9 | 10 | 11:
        print(f"Mes {mes}: Otoño")
    case _:
        print("Error: Mes debe estar entre 1 y 12.")