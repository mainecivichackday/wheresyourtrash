FROM ubuntu:14.04
MAINTAINER Colin Powell "colin.powell@gmail.com"
RUN apt-get -qq update
RUN apt-get install -y python-dev python-setuptools git
RUN easy_install pip
RUN pip install virtualenv
RUN pip install uwsgi
RUN virtualenv --no-site-packages /opt/ve/wheresyourtrash
ADD . /opt/apps/wheresyourtrash
ADD etc/gunicorn.conf /opt/gunicorn_wheresyourtrash.conf
ADD etc/run.sh /usr/local/bin/run_wheresyourtrash
RUN (cd /opt/apps/wheresyourtrash && git remote rm origin)
RUN (cd /opt/apps/wheresyourtrash && git remote add origin https://github.com/powellc/wheresyourtrash.git)
RUN (cd /opt/apps/wheresyourtrash && python setup.py install)
EXPOSE 30321
CMD ["/bin/sh", "-e", "/usr/local/bin/run_wheresyourtrash"]
