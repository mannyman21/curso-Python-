# conexion a la base de datos 
# 1 hacemos el import 


import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]



class Usuario:
    
    
             # constructor
    def __init__(self,nombre, apellidos,email,password): #parametros o atributos
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def registrar(self):
        
        # cifrar contraseña 
        cifrado = hashlib.sha256() #usamos la libreria hashlib para cifrar la contraseña con sha26
        cifrado.update(self.password.encode('utf8'))
        #le pasamos encode, porque al hacer la funcion update los parametros
        #deben que ser bytes no string
        
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)" #nombre,apellidos,email,password,fecha
        #creamos una tupla
        usuario = (self.nombre,self.apellidos,self.email, cifrado.hexdigest(),fecha)
        
        # hacemos un try catch para hacer exepciones si un correo se repite
        try:
            cursor.execute(sql,usuario) # ejecutamos el query
            database.commit()
            result =[cursor.rowcount, self]
        except:
            result = [0, self]
        return  result
        
        
      
        
    
    def identificar(self):
        
          ## hacemos una consulta  a la db para comprobar si existe el usuario  ##
        sql = "SELECT * FROM usuarios WHERE email = %s AND password  = %s   "
        
        
         ## volvemos a cifrar la contraseña ## 
        cifrado = hashlib.sha256() #usamos la libreria hashlib para cifrar la contraseña con sha26
        cifrado.update(self.password.encode('utf8'))
        
        ## datos para la consulta ##
        usuario =(self.email, cifrado.hexdigest())
        
         ## hacemos la consulta ejecutando el comando execute ##
         
        cursor.execute(sql, usuario) # ingresamos la consulta y los datos para hacer la consulta 
        result  = cursor.fetchone()
        
        return result 