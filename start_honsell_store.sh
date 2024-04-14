git pull
. /home/honsell-landing-page/venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn --access-logfile - --workers 3 --bind unix:/run/www.honsell.store.sock app.wsgi:application