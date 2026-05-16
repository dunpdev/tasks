#!/bin/bash
# Release script for Railway deployment
# This script runs database migrations and other setup tasks

set -e

echo "Running database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if not exists..."
python manage.py shell << END
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Superuser created successfully")
else:
    print("Superuser already exists")
END

echo "Release script completed successfully!"
