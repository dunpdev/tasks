web: gunicorn main.wsgi --log-file -
worker: celery -A main worker -l info
beat: celery -A main beat -l info
