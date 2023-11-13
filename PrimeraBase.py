import sqlite3

#conectar la base de datos(o crearla si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')


#crear un objeto cursor para ejecutar sonsultas SQL
cursor = conn.cursor()

#Ejecutar consultas SQL
cursor.execute(''' CREATE TABLE IF NOT EXISTS usuarios (
    id INTERGER PRIMARY KEY, nombre TEXT NOT NULL,edad INTERGER)''')

#INSERTAR Datos
cursor.execute('INSERT INTO usuarios(nombre, edad)VALUES (?, ?)',('juan', 25))
cursor.execute('INSERT INTO usuarios(nombre, edad)VALUES(?,?)', ('MARIA',30))

#Guardar cambios y cerrar la conexión.
conn.commit()

#consultar datos
cursor.execute('SELECT *FROM usuarios')
usuarios = cursor.fetchall()

print('Lista de usuarios: ')
for usuario in usuarios:
    print(usuario)
    
#Actualizar datos
cursor.execute('UPDATE usuarios SET edad=? WHERE nombre=?',(26,'juan'))
conn.commit()

#Eliminar datos
cursor.execute('DELETE FROM usuarios WHERE nombre=?', ('MARIA',))
conn.commit()

#cerrar conexión
conn.close()