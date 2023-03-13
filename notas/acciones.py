import notas.notas as modelo

class Acciones:
    
    def crear(self, usuario):
        
        print(f" ok {usuario[1]}!! Vamos a crear una nueva nota")
        titulo = input("Introduce el titulo de tu nota:")
        descripcion = input("Mete el contenido de tu nota")
        
        ## llamar al modelo ##
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >=1: # guardar[0] indice 0 = id_ usuario
            print(f"\n perfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"No se ha guardado la nota {usuario}, Lo siento")
    
    def mostrar(self, usuario):
        print(f"Vale {usuario[1]}!! Aqui tienes tus notas: \n")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        
        for nota in notas:
            print("\n**********************************************************************")
            print(notas[2])
            print(notas[3])
            print("\n**********************************************************************")
    
    def borrar( self, usuario):
        print(f"\n okey {usuario[1]}!! vamos a borrar notas")    
        titulo = input("Ingresa el titulo de la nota que deseas eliminar ")
        nota = modelo.Nota(usuario[0], titulo) #usuario[0] = id
        eliminar = nota.eliminar()
        
        if eliminar[0] >= 1:
            print(f"Hemos eliminado la nota:{nota.titulo}")
        else:
            print("No se ha eliminado la nota, prueba luego")
            