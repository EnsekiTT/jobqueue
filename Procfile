web: gunicorn web:app --log-file -
worker: celery worker --app=worker --loglevel=info
