"""
Ejercicio 4
Crear un script que tenga cuatro variables
1- listya
2- string
3- entero
4- boolean
e imprimir mensaje segun el tipo de dato
"""

#creamos funcion para comprobar

def tipoDato(tipo):
    result =None
    if result == list:
        result = "listas"
    elif result == str:
        result = "cadena de texto"
    elif result == int:
        result = "numero entero"
    elif result == bool:
        result = "Booleano"
    return result

def comprobarDato(dato,tipo):
    test = isinstance(dato,tipo)
    result = ""
    if test:
        result = f"Este dato es de tipo {tipoDato(tipo)}"
    else:
        result = "Tipo de dato no correcto"
    return result

lista=["hola",4,"gato"]
nombre = "Manny"
num = 5
verdadero= True

#mandamos a llamar a la funcion
print(comprobarDato(lista,list)) #ponemos adentro nombre de la variable y tipo de dato
# a comprobar

print(comprobarDato(nombre,str))
print(comprobarDato(num,str))
