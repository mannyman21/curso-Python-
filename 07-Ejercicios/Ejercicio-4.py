"""
Ejercicio- 4 Pedir dos numeros al usuario y hacer todas --
las operaciones basicas de una calculadora
"""

numero1= int(input("Ingrese el numero 1:"))
numero2 = int(input("Ingrese el numero 2:"))

print("#### Calculadora ####")
operacion= input("Ingrese la operacion a realizar ")

if operacion== '+' or operacion == 'suma':
    print(f"La suma es:{numero1+numero2}")
elif operacion == '-' or operacion == 'Resta':
    print(f"La resta es:{numero1-numero2}")
elif operacion == 'x' or operacion == 'Multiplicacion':
    print(f"La multiplicacion es:{numero1*numero1}")
elif operacion== '/' or operacion=='Division':
    print(f"La division es:{numero1/numero2}")
else:
    print("error de operacion ")
