import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("\n Ok!! Vamos a registrarte en el sistema...")
        
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("¿Cual es tu email?: ")
        password = input("Introduce tu contraseña: ")
        
        # se crea el usuario(objeto)
        usuario = modelo.Usuario(nombre,apellidos,email,password) # le pasamos las propiedades
        registro = usuario.registrar()
        
        if registro[0] >=1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")
            
            
    def login(self):
        try: 
             print("\n Vale!! Identificate en el sistema...")
             email = input("¿Cual es tu email?: ")
             password = input("Introduce tu contraseña: ")
                 
        
           ## creamos nuestro usuario ##
             usuario = modelo.Usuario('','', email, password)
             login = usuario.identificar()
        
             if email == login[3]: ## el email se encuentra en la posicion 3
                print(f"\nBienvenido {login[1]} te has registrado en el sistema el {login[5]}") 
                self.proximasAcciones(login)
        except Exception as e:
             print(type(e))
             print(type(e).__name__) # para imprimir el tipo de error
             print(f" Login Incorrecto!! intentalo mas tarde")
             
    def proximasAcciones(self, usuario):
        print("""
        Acciones Disponibles
         - Crear una nota
         - mostrar nota
         - eliminar nota      
         - Salir      
              """)
        
        accion = input("¿Que quieres hacer?: ")
        # creamos una variable llamada hazEl
        hazEl = notas.acciones.Acciones() # creamos el objeto de la clase opciones 
         
         
        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario) # volvemos a llamar a la funcion para poder realizas mas acciones
        elif accion == "mostrar":
             hazEl.mostrar(usuario)
             self.proximasAcciones(usuario)
        elif accion == "eliminar":
             hazEl.borrar(usuario)
             self.proximasAcciones(usuario)
        elif accion  == "salir":
            print(f"Ok {usuario[1]}, hasta pronto")## el indice 1 es el nombre del usuario ##
            exit()
           
            
        

