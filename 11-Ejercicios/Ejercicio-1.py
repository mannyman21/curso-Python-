"""
Crear una lista con 8 numeros enteros
- (realizado) recorrerla y mostrarla
- (realizado) hacer funcion que recorra la lista de numeros
y devuelva String
- ordenarla y mostrarla
- mostrar longitud
- buscar un elemento
"""

# creamos lista
num =[1,10,16,2,5,8,11,20]

# funcion que recorra la lista de numeros
# y devuelva String

def mostrarLista(lista):
    resultado=''
    for numeros in num:
        resultado += "Elementos: " + str(numeros)
        resultado += "\n"
        return resultado


# recorrer y mostrar lista
print("###### Recorrer y mostrar #####")
for numeros in num:
   print(numeros)


#ordenarla y mostrarla
print("#### ordenar y mostrarla ####")
num.sort()
print(num)

print("#### mostrar longitud ####")
print(len(num))

# busqueda en la lista
print("#### Busqueda en la lista ####")

Busqueda= int(input("Introduce un numero:"))
comprobar = isinstance(Busqueda,int)
while not comprobar or Busqueda <=0:
    Busqueda = int(input("Introduce un numero:"))
else:
 print(f"has introducido el numero:{Busqueda}")
print(f"Buscar en la lista el numero:{Busqueda}")
search =num.index(Busqueda)
print(f"El numero buscado existe en la lista, es el indice:{search}")

