"""
Ejercicio 5. hacer un programa que muestre todos los
numero entre dos numero que diga el usuario
"""

numero1= int(input("Ingrese el numero 1:"))
numero2 = int(input("Ingrese el numero 2:"))

if numero1<numero2:
 for contador in range(numero1,numero2):
     print(contador)




else:
    print(f"el numero 1 debe ser menor al dos")