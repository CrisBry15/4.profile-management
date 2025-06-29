import mysql.connector
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Conexión a la base de datos de clientes
try:
    client_conn = mysql.connector.connect(
        host=os.getenv("CLIENT_MYSQL_HOST"),
        user=os.getenv("CLIENT_MYSQL_USER"),
        password=os.getenv("CLIENT_MYSQL_PASSWORD"),
        database=os.getenv("CLIENT_MYSQL_DB"),
        port=int(os.getenv("CLIENT_MYSQL_PORT", 3306))
    )
    print("Conexión exitosa a la base de datos de clientes")
except mysql.connector.Error as err:
    print(f"Error al conectar con la base de datos de clientes: {err}")

# Conexión a la base de datos de organizadores
try:
    organizer_conn = mysql.connector.connect(
        host=os.getenv("ORGANIZER_MYSQL_HOST"),
        user=os.getenv("ORGANIZER_MYSQL_USER"),
        password=os.getenv("ORGANIZER_MYSQL_PASSWORD"),
        database=os.getenv("ORGANIZER_MYSQL_DB"),
        port=int(os.getenv("ORGANIZER_MYSQL_PORT", 3306))
    )
    print("Conexión exitosa a la base de datos de organizadores")
except mysql.connector.Error as err:
    print(f"Error al conectar con la base de datos de organizadores: {err}")
