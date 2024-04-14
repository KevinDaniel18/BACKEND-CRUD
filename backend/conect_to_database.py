import psycopg2

cursor = None
try:
    connection=psycopg2.connect(
        host="localhost",
        user="postgres",
        password="pruebatecnica",
        dbname="postgres"
    )
    cursor=connection.cursor()
    
    print("datos guardados correctamente")
   
except Exception as ex:
    print(ex)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
