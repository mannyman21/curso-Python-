"""
Ejercicio 5 repaso
"""

tabla = [
    {
        "Categoria":"Pelea",
        "Juegos":["king of fighter","Mortal combat"]
    },
    {
        "Categoria":"Aventura",
         "Juegos":["Zelda", "breath of the wild"]
    },
    {
        "Categoria":"Accion",
        "Juegos":["COD","Gears of war"]
    }
]
for categoria in tabla:
 print(f"----{categoria['Categoria']}----")
 for juego in categoria['Juegos']:
     print(juego)
