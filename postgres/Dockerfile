FROM postgres:15

RUN /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh -y \
    && apt install -y pgbadger pgbouncer

# COPY init-db-bso.sql /docker-entrypoint-initdb.d/
COPY init-db.sh /docker-entrypoint-initdb.d/
