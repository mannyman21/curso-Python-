import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]

cursor = connect[1]

class Nota:
    
    def __init__(self,usuario_id, titulo ="", descripcion=""): # constructor 
                self.usuario_id = usuario_id
                self.titulo = titulo 
                self.descripcion = descripcion
                
    def guardar(self): # se utiliza self para poder acceder a las propiedades de la funcion (metodo)
        sql  = "INSERT INTO notas VALUES(null, %s, %s, %s, Now()) " # la funcion Now()guarda la fecha actual
        nota = (self.usuario_id, self.titulo,self.descripcion)
       
        cursor.execute(sql, nota)
        database.commit()
        return [cursor.rowcount, self]
    
    def listar(self):
        sql = (f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}")
        
        # ejecutamos la consulta 
        cursor.execute(sql)
        result = cursor.fetchall() # recogemos todos los datos almacenados y los guardamos en la variable result
        
        return result   
    def eliminar(self, titulo): # debemos que colocar el titulo que deseamos eliminar 
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE  '%{self.titulo}%' "
         # %{titulo}% esto es para comprobar que el titulo buscado, sea igual al titulo contenido
         
        cursor.execute(sql)
        database.commit() # para guardar los cambios hechos 
        
        return [cursor.rowcount, self]  # rowcount sirve para ver el numero de filas afectadas, por el ultimo metodo
    
        