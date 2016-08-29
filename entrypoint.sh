#!/bin/bash
#sleep 5d #for debugging; uncomment this and the container will stay up so you can inspect the environment
python3 /usr/local/lib/python3.4/dist-packages/wheresyourtrash/manage_wheresyourtrash.py migrate
#python /usr/local/lib/python2.7/dist-packages/wheresyourtrash/manage_wheresyourtrash.py collectstatic --noinput

exec gunicorn -w 2 wheresyourtrash.wsgi --bind 0.0.0.0:8000
