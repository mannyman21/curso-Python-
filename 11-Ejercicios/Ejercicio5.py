"""
Ejercicio 5
crear una lista  con el contenido de esta tabla
Accion    Aventura            Deportes
GTA       assins              FIFA 21
COD       crash               PRO21
Pugb      prince of percia    Moto gp 21

Mostrar esta informacion ordenada
"""

Lista = [
    {
      "Categoria":"accion",
       "Juegos":["GTA","COD","PUGB"]
    },
    {
        "Categoria":"aventura",
        "Juegos":["ASSASINS","CRASH","PRINCE OF PERCIA"]
    },

    {
        "Categoria":"Deportes",
        "Juegos":["FIFA 21","PRO 21","MOTO GP 21"]
    }


]

for categoria in Lista:
 print(f"----{categoria['Categoria']}----")
 for juego in categoria['Juegos']:
     print(juego)
