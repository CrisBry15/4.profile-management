# Utilizar imagen base ligera de Python
FROM python:3.11-slim

# Evitar archivos .pyc y habilitar salida en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias del sistema necesarias para mysql-connector
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    && apt-get clean

# Crear y usar el directorio de la aplicación
WORKDIR /app

# Copiar todo el contenido del proyecto al contenedor
COPY . .

# Instalar dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exponer el puerto que usará Flask
EXPOSE 5004

# Comando de ejecución por defecto
CMD ["python", "run.py"]
