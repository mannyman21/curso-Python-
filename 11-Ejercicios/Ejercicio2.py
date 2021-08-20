'''
Ejercicio2- Escribir un programa que añada valores -
a una lista mientras que su longitu sea menor a 120
y despues mostrar la lista
plus- usar while y for
'''

lista =[]

l=0
while l <120:
   lista.append(f"Elemento:{l}")
   print("mostrando el:"+ lista[l])
   l +=1
print(lista[115])
'''
lista =[]
for contador in range(0,120):
    lista.append(f"Elemento:{contador}")
    print("mostrando el " + lista[contador])
print(lista)
'''