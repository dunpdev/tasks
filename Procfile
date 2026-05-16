web: gunicorn main.wsgi --log-file -
worker: celery -A main worker --loglevel=info
beat: celery -A main beat --loglevel=info
