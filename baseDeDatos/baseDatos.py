import mysql.connector
from mysql.connector import Error

def crearConexion():
    #1 Establecer una conexion con la base de datos
    connection=mysql.connector.connect(
        host='localhost',    #direccion del servidor sql
        database='tienda_koaj', #nomre de la base de datos
        user='root',   #Nombre de usuario
        password=''  #contraseña del usuario
    )
    return connection


def verificacion_conexion(datosConexion):
    if datosConexion.is_connected():
        print("Conexion exitosa a la base de datos")
        #2.Crear un objeto cursor para ejecutar consultas
        cursor=datosConexion.cursor()
        #3 Ejecutar una consulta sql
        #Consulta para seleccionar todos los registros de 'tabla_ejemplo'
        cursor.execute("SELECT * FROM usuario")
        #4 Recuperar los resultados de la consulta
        resultados = cursor.fetchall() #Recupera todas las filas de la consulta
        print (resultados)
    else:
        print ("Error")


def buscar_datos(datosConexion):
    try:
        cursor=datosConexion.cursor()
        #6. Realizar una operacion de insercion
        id=input("Digite el id del usuario: ")
        nombre=input("Digite el nombre del usuario: ")
        contraseña=int(input("Digite la contraseña del usuario: "))
        rol=int(input("Digite el rol del usuario: "))
        cursor.execute("INSERT INTO usuario (ID, nombre, contraseña, rol) VALUES (%s,%s,%s,%s)",(id,nombre,contraseña,rol))
        print("Registro insertado")
        #7. Confirmar los cambios en la base de datos
        datosConexion.commit()#Guarda los cambios realizados en la base de datos
    except Error as e:
        print(f"Error al insertar datos: {e}")
    finally:
        cursor.close()
#--------codigo principal--------
if __name__ == "__main__":
    conexion = crearConexion()
    if conexion:
        verificacion_conexion(conexion)
        buscar_datos(conexion)
        conexion.close()