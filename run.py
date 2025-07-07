from app.init import create_app
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Crear la instancia de la aplicación Flask
app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5004))  # Puerto por defecto: 5004
    app.run(debug=True, host="0.0.0.0", port=port)
