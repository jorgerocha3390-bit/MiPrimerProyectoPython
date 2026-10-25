"""Programa que calcula el salario neto de un empleado con impuestos y deducciones."""

def main():
    salario_bruto = float(input("Ingresa el salario bruto mensual: "))
    porcentaje_impuestos = float(input("Ingresa el porcentaje de impuestos: "))
    deducciones = float(input("Ingresa las deducciones adicionales: "))
    impuesto = salario_bruto * (porcentaje_impuestos / 100)
    salario_neto = salario_bruto - impuesto - deducciones
    print(f"\n--- Resultado ---")
    print(f"Impuesto a pagar: ${impuesto:.2f}")
    print(f"Salario neto: ${salario_neto:.2f}")

if __name__ == "__main__":
    main()