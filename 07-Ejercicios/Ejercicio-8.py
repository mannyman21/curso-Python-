"""
Ejercicio-8
 Cuanto es el x por ciento de x numero
 """

numero = int(input("Introduce el numero:"))
porcentaje= int(input(f"¿Que porcentaje desea sacar de {numero} ?"))


operacion = (numero*(porcentaje/100))

print(f"El {porcentaje}% del {numero} es: {operacion}")