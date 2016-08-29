[![Stories in Ready](https://badge.waffle.io/mainecivichackday/wheresyourtrash.png?label=ready&title=Ready)](https://waffle.io/mainecivichackday/wheresyourtrash)
Where's Your Trash?
===================

[![Join the chat at https://gitter.im/Code4Maine/wheresyourtrash](https://badges.gitter.im/Code4Maine/wheresyourtrash.svg)](https://gitter.im/Code4Maine/wheresyourtrash?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Build
Status](https://travis-ci.org/Code4Maine/wheresyourtrash.svg?branch=master)](https://travis-ci.org/Code4Maine/wheresyourtrash)

It seemed so simple. When is the city coming to pick up your trash? So why
do we keep forgetting? Well, it doesn't help when recycling is every other
Tuesday. And Monday's trash pickup falls on Patriot's Day. Is that even a real
holiday? Does the city recognize it.

Confusion no more! Enter your phone number or email address here, tell us where
you live in the city and we'll send you a notification first thing in the
morning when it's time to disgard your disgardables.

#Easy bootstrapping!
-------------------

Powered by the ubiquitous Makefile ... this should be pretty easy:

1. make deps (or make deps_mac if you are, you know, on a mac)
2. make install
3. make run
4. open your browser to: http://127.0.0.1:45000

#Docker friendly!
-------------------

###from your docker-config directory:

`git clone https://github.com/mainecivichackday/wheresyourtrash.git`

`cd wheresyourtrash`

`docker-compose up -d --build && docker-compose logs -f`

###get yourself an admin user:
`docker exec -it wheresyourtrash_django-wyt_1 python /usr/local/lib/python2.7/dist-packages/wheresyourtrash/manage_wheresyourtrash.py createsuperuser`

access via (http://<hostname>:8000)
for admin functions, add /admin to the end of the URL (http://<hostname>:8000/admin)
