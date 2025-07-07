import os
import mysql.connector
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

class DBConnections:
    @staticmethod
    def get_client_connection():
        try:
            return mysql.connector.connect(
                host=os.getenv("CLIENT_MYSQL_HOST"),
                port=int(os.getenv("CLIENT_MYSQL_PORT", 3306)),
                user=os.getenv("CLIENT_MYSQL_USER"),
                password=os.getenv("CLIENT_MYSQL_PASSWORD"),
                database=os.getenv("CLIENT_MYSQL_DB")
            )
        except mysql.connector.Error as err:
            print(f"Error al conectar con la base de datos de clientes: {err}")
            return None

    @staticmethod
    def get_organizer_connection():
        try:
            return mysql.connector.connect(
                host=os.getenv("ORGANIZER_MYSQL_HOST"),
                port=int(os.getenv("ORGANIZER_MYSQL_PORT", 3306)),
                user=os.getenv("ORGANIZER_MYSQL_USER"),
                password=os.getenv("ORGANIZER_MYSQL_PASSWORD"),
                database=os.getenv("ORGANIZER_MYSQL_DB")
            )
        except mysql.connector.Error as err:
            print(f"Error al conectar con la base de datos de organizadores: {err}")
            return None
