salario_basico = float(input("Ingresa el salario básico del empleado: "))
retencion = salario_basico * 0.18
bonificacion = salario_basico * 0.013
salario_neto = salario_basico - retencion + bonificacion
print("\n--- Cálculos del Salario ---")
print(f"Salario Básico: ${salario_basico:.2f}")
print(f"Retención (18%): ${retencion:.2f}")
print(f"Bonificación (1.3%): ${bonificacion:.2f}")
print(f"Salario Neto: ${salario_neto:.2f}")
