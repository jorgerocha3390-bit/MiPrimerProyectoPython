"""
Programa 7: Conversor de MXN a 10 monedas extranjeras
"""
cantidad = float(input("Cantidad en MXN: $"))
print("1=USD 2=EUR 3=JPY 4=GBP 5=CAD 6=AUD 7=CHF 8=CNY 9=BRL 10=ARS")
op = int(input("Elige moneda: "))

match op:
    case 1: print(f"${cantidad} MXN = ${cantidad*0.058:.2f} USD")
    case 2: print(f"${cantidad} MXN = {cantidad*0.053:.2f} EUR")
    case 3: print(f"${cantidad} MXN = {cantidad*8.85:.2f} JPY")
    case 4: print(f"${cantidad} MXN = {cantidad*0.045:.2f} GBP")
    case 5: print(f"${cantidad} MXN = {cantidad*0.078:.2f} CAD")
    case 6: print(f"${cantidad} MXN = {cantidad*0.088:.2f} AUD")
    case 7: print(f"${cantidad} MXN = {cantidad*0.052:.2f} CHF")
    case 8: print(f"${cantidad} MXN = {cantidad*0.42:.2f} CNY")
    case 9: print(f"${cantidad} MXN = {cantidad*0.29:.2f} BRL")
    case 10: print(f"${cantidad} MXN = {cantidad*52.5:.2f} ARS")
    case _: print("Error: Opción inválida")