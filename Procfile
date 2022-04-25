release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py createsuperuser
web: gunicorn digital_showcase.wsgi --preload --log-file -