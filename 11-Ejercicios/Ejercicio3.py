"""
Ejercicio 3
programa que compruebe si una variable esta vacia
y si esta vacia rellenarla con texto en minusculas
y mostrarla en mayusculas
"""

texto= ""

#sirve para comprar si la variables contiene caracteres
if len(texto.strip()) <=0:
    texto="soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")