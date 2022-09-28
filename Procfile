release: python manage.py makemigrations && python manage.py migrate
web: gunicorn digital_showcase.wsgi --preload --log-file -