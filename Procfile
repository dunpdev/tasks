web: gunicorn main.wsgi:application --bind 0.0.0.0:$PORT --workers 2
worker: celery -A main.celery worker --loglevel=info
beat: celery -A main.celery beat --loglevel=info
flower: celery -A main.celery flower --port=$PORT