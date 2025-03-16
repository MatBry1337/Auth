#!/bin/sh

# Wait for database with explicit port
wait_for_db() {
    echo "Waiting for database at $MARIADB_HOST:${MARIADB_PORT:-3306}..."
    timeout=60
    while ! nc -z $MARIADB_HOST ${MARIADB_PORT:-3306}; do
        sleep 1
        timeout=$((timeout-1))
        if [ $timeout -le 0 ]; then
            echo "Database connection timed out!"
            exit 1
        fi
    done
    echo "Database ready!"
}

wait_for_db

# Start application
exec "$@"
