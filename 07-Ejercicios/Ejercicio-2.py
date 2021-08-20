'''
 Ejercicio 2 Escribir un script que muestre,
 todos los numeros pares del 1 al 100
 
'''
numero =1
for numero in range (1,121):
    if numero%2==0:
        print(numero)
    else:
        print(f"{numero} es impar")