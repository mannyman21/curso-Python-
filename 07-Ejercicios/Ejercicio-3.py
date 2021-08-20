'''
Ejercicio 3- Escribir un programa que los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros numeros
naturales, resolver con for y con while

'''

# usando el for
contador =1

for contador in range(1,60):
    cuadrado=contador*contador
    print(cuadrado)


print("##########################################")
# usando el while


while contador <=60:

 cuadrado=contador*contador
 print(f"El cuadrado de {contador} es {cuadrado}")
 contador += 1