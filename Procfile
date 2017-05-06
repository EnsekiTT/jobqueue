# web: python web.py --port=$PORT
web: gunicorn web:app --log-file -
worker: celery worker --app=worker --loglevel=info
