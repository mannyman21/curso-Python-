"""
Ejercicio- 10
El ejercicio tiene que pedir la nota  de 15 alumnos
y sacar por pantalla cuantos han aprobado
y cuantos han suspendido
"""
contador = 0
aprobados = 0
suspendidos =0

numero_alumnos = int(input("cuantos alumnos son en tu clase?"))
while contador <= numero_alumnos:
    nota = int(input("Ingresa la nota del alumno:"))

    if nota>6:
        aprobados += 1

    else:
        suspendidos += 1
    contador += 1

print(f"aprobados {aprobados}")
print(f"suspendidos {suspendidos}")
