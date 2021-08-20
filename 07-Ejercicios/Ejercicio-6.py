"""
Ejercicio-6 mostrar todas las tablas del multiplicar del uno al diez
mostrando el titulo de la tabla y luego multiplicando del 1 al diez

"""
import os

for cabecera in range (1,11):
    print("####################")
    print(f"### tabla del {cabecera} ###")
    print("####################")

    for numero in range (1,11):
        print(f"{numero} x {cabecera}={numero*cabecera}")





