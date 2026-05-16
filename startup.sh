#!/usr/bin/env bash
# Startup script for Railway deployment
# Run migrations and other setup tasks

set -e

echo "========================================"
echo "Starting Django Application Setup"
echo "========================================"

echo ""
echo "1. Running database migrations..."
python manage.py migrate --noinput

echo ""
echo "2. Collecting static files..."
python manage.py collectstatic --noinput --clear

echo ""
echo "3. Checking system checks..."
python manage.py check

echo ""
echo "========================================"
echo "Setup completed successfully!"
echo "========================================"
