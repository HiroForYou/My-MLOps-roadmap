 
# Extraemos la imagen nginx de Docker Hub
FROM nginx

# Eliminamos el archivo de configuración nginx predeterminado y lo reemplazamos con el nuevo
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/