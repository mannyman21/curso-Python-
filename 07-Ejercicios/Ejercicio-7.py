"""
Ejercicio- 7
hacer un programa que muestre todos los numero impares
entre dos numero que decida el usuario
"""

num1= int(input("Ingresa el numero 1"))
num2= int(input("ingresa el numero 2"))

if num1<num2:
    for contador in range(num1,num2):
      if contador%2 ==0:
          print(f"{contador} es un numero par")
      else:
          print(f"{contador} son numeros impares ")

else:
    print("el primer numero debe que ser menor al segundo")