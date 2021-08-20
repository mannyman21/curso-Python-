"""
Ejercicio- 9
hacer un programa que pida numeros al usuario
indefinidamente hasta meter el numero 111

"""
contador =1
while contador < 100:
  numero = int(input("Ingrese un numero:"))

  if numero == 111:
      break
  else:
    print(f" has introducido el numero {numero}")

