import mysql.connector
from config import Config

# Obtener datos de perfil del cliente
def get_client_profile(user_id):
    try:
        conn = mysql.connector.connect(
            host=Config.CLIENT_DB["host"],
            port=Config.CLIENT_DB["port"],
            user=Config.CLIENT_DB["user"],
            password=Config.CLIENT_DB["password"],
            database=Config.CLIENT_DB["database"]
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email, phone, status FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()
    except mysql.connector.Error as err:
        raise Exception(f"Error al obtener perfil del cliente: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# Obtener datos de perfil del organizador
def get_organizer_profile(organizer_id):
    try:
        conn = mysql.connector.connect(
            host=Config.ORGANIZER_DB["host"],
            port=Config.ORGANIZER_DB["port"],
            user=Config.ORGANIZER_DB["user"],
            password=Config.ORGANIZER_DB["password"],
            database=Config.ORGANIZER_DB["database"]
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email, phone, status FROM organizers WHERE id = %s", (organizer_id,))
        return cursor.fetchone()
    except mysql.connector.Error as err:
        raise Exception(f"Error al obtener perfil del organizador: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
