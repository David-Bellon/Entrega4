import math
from typing_extensions import final

def calfica(ls):
    final_grades = []
    for nota in ls:
        if nota >= 40:
            if nota % 10 < 5:
                next_mult = nota - (nota % 10) + 5
                if next_mult - nota <= 3:
                    final_grades.append(next_mult)
                else:
                    final_grades.append(nota)
            else:
                next_mult = nota + 10 - (nota % 10)
                if next_mult - nota <= 3:
                    final_grades.append(next_mult)
                else:
                    final_grades.append(nota)
        else:
            final_grades.append(nota)
    return final_grades
        

n = int(input("Numero de alumnos a calificar: "))
notas = []

for i in range(n):
    notas.append(int(input("Nota del alumno: ")))

print(calfica(notas))