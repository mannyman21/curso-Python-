"""
 proyecto python-mysql
 - abrir asistente
 -login o registro
 -si elegimos registro, creara un usuario en la db
 - si elegimos login, identificara al usuario y nos preguntara
 -crear nota, mostrar notas, borrarlas.
 """
 
 #importamos modulo  de acciones desde usuarios

from usuarios import acciones
 
print("""
 Acciones disponibles      
        - registro
        - login
       
       """)
# instanciamos el objeto  o creamos clase (Acciones)
hazEl = acciones.Acciones() 

accion = input("¿Que quieres hacer?:")


if accion == "registro":
    hazEl.registro()

elif accion == "login":
      hazEl.login()

    