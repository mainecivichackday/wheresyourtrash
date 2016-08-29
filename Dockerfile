FROM ubuntu:14.04
MAINTAINER Colin Powell "colin.powell@gmail.com"
RUN apt-get -qq update && apt-get install -y comerr-dev krb5-multidev libgssrpc4 libkadm5clnt-mit9 libkadm5srv-mit9 libkdb5-7 libpq-dev libpq5 libssl-dev libssl-doc zlib1g-dev postgresql libpq-dev libmemcached-dev python-dev python-setuptools git && easy_install pip && pip install wheresyourtrash virtualenv uwsgi pylibmc && virtualenv --no-site-packages /opt/ve/wheresyourtrash
EXPOSE 8000
