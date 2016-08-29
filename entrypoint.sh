#!/bin/bash
#sleep 5d #for debugging; uncomment this and the container will stay up so you can inspect the environment
gunicorn -w 2 wheresyourtrash.wsgi --bind 0.0.0.0:8000
