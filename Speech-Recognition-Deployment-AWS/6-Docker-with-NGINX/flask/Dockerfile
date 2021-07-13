 
# Extraimos la imagen de tensorflow con Python3
FROM tensorflow/tensorflow:2.1.0-py3

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Transferimos el contenido del directorio actual a /app en el contenedor
ADD . /app

# Instalamos las bibliotecas de audio
RUN apt-get update && apt-get install -y libsndfile1 libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg

# Instalamos los paquetes de python
RUN pip install -r requirements.txt

# Iniciamos uWSGI usando el archivo de configuración
CMD ["uwsgi", "app.ini"]