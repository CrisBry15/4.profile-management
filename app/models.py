from config import DBConnections

# Obtener datos de perfil del cliente
def get_client_profile(user_id):
    conn = DBConnections.get_client_connection()
    if not conn:
        raise Exception("No se pudo establecer conexión con la base de datos de clientes")

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email, phone, status FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# Obtener datos de perfil del organizador
def get_organizer_profile(organizer_id):
    conn = DBConnections.get_organizer_connection()
    if not conn:
        raise Exception("No se pudo establecer conexión con la base de datos de organizadores")

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email, phone, status FROM organizers WHERE id = %s", (organizer_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

