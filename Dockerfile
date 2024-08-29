FROM dwiorderfaz/odoo-enterprise:17.0

LABEL MAINTAINER Luis Miguel Gonzalez
USER root

RUN apt-get update && \
    apt-get install -y \
    netcat \
    && rm -rf /var/lib/apt/lists/*

 
# Copia tu script init-script.sh al contenedor
COPY init-script.sh /init-script.sh

COPY init-db.sql /init-db.sql

# Asegúrate de que el script tiene permisos de ejecución
RUN chmod +x /init-script.sh

# Ejecuta el script init-script.sh
RUN /init-script.sh