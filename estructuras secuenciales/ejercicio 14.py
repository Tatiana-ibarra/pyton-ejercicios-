taller1 = float(input("Ingresa la nota del Taller 1: "))
taller2 = float(input("Ingresa la nota del Taller 2: "))
nota1 = (taller1 + taller2) / 2 * 0.15

evaluacion1 = float(input("Ingresa la nota de la Evaluación 1: "))
evaluacion2 = float(input("Ingresa la nota de la Evaluación 2: "))
evaluacion3 = float(input("Ingresa la nota de la Evaluación 3: "))
nota2 = (evaluacion1 + evaluacion2 + evaluacion3) / 3 * 0.30

trabajo_final = float(input("Ingresa la nota del Trabajo Final: "))
nota3 = trabajo_final * 0.30

quiz1 = float(input("Ingresa la nota del Quiz 1: "))
quiz2 = float(input("Ingresa la nota del Quiz 2: "))
quiz3 = float(input("Ingresa la nota del Quiz 3: "))
quiz4 = float(input("Ingresa la nota del Quiz 4: "))
nota4 = (quiz1 + quiz2 + quiz3 + quiz4) / 4 * 0.25

nota_definitiva = nota1 + nota2 + nota3 + nota4

print("\n--- Cálculo de la Nota Definitiva ---")
print(f"Nota de los Talleres (15%): {nota1:.2f}")
print(f"Nota de las Evaluaciones (30%): {nota2:.2f}")
print(f"Nota del Trabajo Final (30%): {nota3:.2f}")
print(f"Nota de los Quizzes (25%): {nota4:.2f}")
print(f"Nota Definitiva: {nota_definitiva:.2f}")
