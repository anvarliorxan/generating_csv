web: gunicorn config.wsgi

worker: celery -A main.taskapp worker -B