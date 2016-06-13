install:
	virtualenv -p /usr/bin/python3 venv
	venv/bin/python setup.py install
	venv/bin/python manage.py migrate --noinput


deps:
	sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk libxslt-dev libxml2-dev redis-server
	npm install bower
	

deps_mac:
	brew install libtiff libjpeg webp little-cms2 redis


test:
	rm -rf .tox
	detox

clean:
	rm -rf venv

run:
	venv/bin/python manage.py runserver_plus 0.0.0.0:45000

tag-release:
	sed -i "/__version__/c\__version__ = '$(v)'" wheresyourtrash/__init__.py
	git add wheresyourtrash/__init__.py && git commit -m "Automated version bump to $(v)" && git push
	git tag -a release/$(v) -m "Automated release of $(v) via Makefile" && git push origin --tags

package:
	rm -rf build
	python setup.py clean
	python setup.py build sdist bdist_wheel

distribute:
	twine upload -s dist/wheresyourtrash-$(v)*

release:
	$(MAKE) tag-release
	$(MAKE) package
	$(MAKE) distribute
