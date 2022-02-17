FROM postgres:13

RUN apt-get update && \
    apt install -y postgis postgresql-13-postgis-3 && \
    echo "CREATE EXTENSION postgis;" > /docker-entrypoint-initdb.d/init_postgis.sql