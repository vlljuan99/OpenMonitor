# Usar la imagen oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos
COPY ./requirements.txt /app/requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar el resto de la aplicación
COPY . /app

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
