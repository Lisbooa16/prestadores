#!/bin/sh

echo "📦 Rodando migrações..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "🚀 Iniciando servidor..."
exec "$@"
