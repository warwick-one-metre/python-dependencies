# HACK: Expand the _topdir path to work around "Dest dir longer than base dir is not supported" errors from rpmbuild
RPMBUILD = rpmbuild --define "_topdir %(pwd)/build/../build/../build/../build/" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)" \
        --undefine=_disable_source_fetch

# Generate spec files for new packages using:
# py2pack generate -t fedora.spec <package name> <package version>
# then rename and modify spec file to use match the others in the repository
prereq: numpy36 serpent36 serpent numpy pybind11
general: astropy36 astroplan scipy36 six pyds936 pyro436 sep36 demjson pyserial pyephem sysv_ipc Pillow pytesseract pymysql strict-rfc3339 jsonschema astroquery36 html5lib beautifulsoup4 spalipy skyfield36 sgp436 jplephem36
web: Flask click itsdangerous Werkzeug Jinja2 MarkupSafe chardet idna urllib3 certifi requests GitHub-Flask bibtexparser36 biplist36
web-new: flask werkzeug github-flask pyparsing bibtexparser biplist
general-new: astropy astroquery scipy keyring skyfield sgp4 jplephem sep pyds9 pyro

numpy36:
	mkdir -p build
	${RPMBUILD} -ba python36-numpy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

numpy:
	mkdir -p build
	${RPMBUILD} -ba python3-numpy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

astropy36:
	mkdir -p build
	${RPMBUILD} -ba python36-astropy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

astropy:
	mkdir -p build
	${RPMBUILD} -ba python3-astropy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

astroplan:
	mkdir -p build
	${RPMBUILD} -ba python36-astroplan.spec
	mv build/noarch/*.rpm .
	rm -rf build

scipy36:
	mkdir -p build
	${RPMBUILD} -ba python36-scipy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

pybind11:
	mkdir -p build
	${RPMBUILD} -ba python3-pybind11.spec
	mv build/x86_64/*.rpm .
	rm -rf build

scipy:
	mkdir -p build
	${RPMBUILD} -ba python3-scipy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

six:
	mkdir -p build
	${RPMBUILD} -ba python36-six.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyds936:
	mkdir -p build
	${RPMBUILD} -ba python36-pyds9.spec
	mv build/x86_64/*.rpm .
	rm -rf x86_64

pyds9:
	mkdir -p build
	${RPMBUILD} -ba python3-pyds9.spec
	mv build/x86_64/*.rpm .
	rm -rf x86_64

serpent36:
	mkdir -p build
	${RPMBUILD} -ba python36-serpent.spec
	mv build/noarch/*.rpm .
	rm -rf build

serpent:
	mkdir -p build
	${RPMBUILD} -ba python3-serpent.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyro436:
	mkdir -p build
	${RPMBUILD} -ba python36-Pyro4.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyro4:
	mkdir -p build
	${RPMBUILD} -ba python3-Pyro4.spec
	mv build/noarch/*.rpm .
	rm -rf build

sep36:
	mkdir -p build
	${RPMBUILD} -ba python36-sep.spec
	mv build/x86_64/*.rpm .
	rm -rf build

sep:
	mkdir -p build
	${RPMBUILD} -ba python3-sep.spec
	mv build/x86_64/*.rpm .
	rm -rf build

demjson:
	mkdir -p build
	${RPMBUILD} -ba python36-demjson.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyserial:
	mkdir -p build
	${RPMBUILD} -ba python36-pyserial.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyephem:
	mkdir -p build
	${RPMBUILD} -ba python36-pyephem.spec
	mv build/x86_64/*.rpm .
	rm -rf build

sysv_ipc:
	mkdir -p build
	${RPMBUILD} -ba python36-sysv_ipc.spec
	mv build/x86_64/*.rpm .
	rm -rf build

Pillow:
	mkdir -p build
	${RPMBUILD} -ba python36-Pillow.spec
	mv build/x86_64/*.rpm .
	rm -rf build

pytesseract:
	mkdir -p build
	${RPMBUILD} -ba python36-pytesseract.spec
	mv build/noarch/*.rpm .
	rm -rf build

pymysql:
	mkdir -p build
	${RPMBUILD} -ba python36-PyMySQL.spec
	mv build/noarch/*.rpm .
	rm -rf build

strict-rfc3339:
	mkdir -p build
	${RPMBUILD} -ba python36-strict-rfc3339.spec
	mv build/noarch/*.rpm .
	rm -rf build

jsonschema:
	mkdir -p build
	${RPMBUILD} -ba python36-jsonschema.spec
	mv build/noarch/*.rpm .
	rm -rf build

astroquery36:
	mkdir -p build
	${RPMBUILD} -ba python36-astroquery.spec
	mv build/noarch/*.rpm .
	rm -rf build

html5lib:
	mkdir -p build
	${RPMBUILD} -ba python36-html5lib.spec
	mv build/noarch/*.rpm .
	rm -rf build

beautifulsoup4:
	mkdir -p build
	${RPMBUILD} -ba python36-beautifulsoup4.spec
	mv build/noarch/*.rpm .
	rm -rf build

skyfield36:
	mkdir -p build
	${RPMBUILD} -ba python36-skyfield.spec
	mv build/noarch/*.rpm .
	rm -rf build

skyfield:
	mkdir -p build
	${RPMBUILD} -ba python3-skyfield.spec
	mv build/noarch/*.rpm .
	rm -rf build

sgp436:
	mkdir -p build
	${RPMBUILD} -ba python36-sgp4.spec
	mv build/noarch/*.rpm .
	rm -rf build

sgp4:
	mkdir -p build
	${RPMBUILD} -ba python3-sgp4.spec
	mv build/noarch/*.rpm .
	rm -rf build

jplephem36:
	mkdir -p build
	${RPMBUILD} -ba python36-jplephem.spec
	mv build/noarch/*.rpm .
	rm -rf build

jplephem:
	mkdir -p build
	${RPMBUILD} -ba python3-jplephem.spec
	mv build/noarch/*.rpm .
	rm -rf build

astroquery:
	mkdir -p build
	${RPMBUILD} -ba python3-astroquery.spec
	mv build/noarch/*.rpm .
	rm -rf build

keyring:
	mkdir -p build
	${RPMBUILD} -ba python3-keyring.spec
	mv build/noarch/*.rpm .
	rm -rf build

# All needed for Flask

Werkzeug:
	mkdir -p build
	${RPMBUILD} -ba python36-Werkzeug.spec
	mv build/noarch/*.rpm .
	rm -rf build

itsdangerous:
	mkdir -p build
	${RPMBUILD} -ba python36-itsdangerous.spec
	mv build/noarch/*.rpm .
	rm -rf build

click:
	mkdir -p build
	${RPMBUILD} -ba python36-click.spec
	mv build/noarch/*.rpm .
	rm -rf build

Flask:
	mkdir -p build
	${RPMBUILD} -ba python36-Flask.spec
	mv build/noarch/*.rpm .
	rm -rf build

Jinja2:
	mkdir -p build
	${RPMBUILD} -ba python36-Jinja2.spec
	mv build/noarch/*.rpm .
	rm -rf build

MarkupSafe:
	mkdir -p build
	${RPMBUILD} -ba python36-MarkupSafe.spec
	mv build/x86_64/*.rpm .
	rm -rf build

chardet:
	mkdir -p build
	${RPMBUILD} -ba python36-chardet.spec
	mv build/noarch/*.rpm .
	rm -rf build

requests:
	mkdir -p build
	${RPMBUILD} -ba python36-requests.spec
	mv build/noarch/*.rpm .
	rm -rf build

idna:
	mkdir -p build
	${RPMBUILD} -ba python36-idna.spec
	mv build/noarch/*.rpm .
	rm -rf build

urllib3:
	mkdir -p build
	${RPMBUILD} -ba python36-urllib3.spec
	mv build/noarch/*.rpm .
	rm -rf build

certifi:
	mkdir -p build
	${RPMBUILD} -ba python36-certifi.spec
	mv build/noarch/*.rpm .
	rm -rf build

GitHub-Flask:
	mkdir -p build
	${RPMBUILD} -ba python36-GitHub-Flask.spec
	mv build/noarch/*.rpm .
	rm -rf build

bibtexparser36:
	mkdir -p build
	${RPMBUILD} -ba python36-bibtexparser.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyparsing:
	mkdir -p build
	${RPMBUILD} -ba python3-pyparsing.spec
	mv build/noarch/*.rpm .
	rm -rf build

bibtexparser:
	mkdir -p build
	${RPMBUILD} -ba python3-bibtexparser.spec
	mv build/noarch/*.rpm .
	rm -rf build

biplist36:
	mkdir -p build
	${RPMBUILD} -ba python36-biplist.spec
	mv build/noarch/*.rpm .
	rm -rf build

biplist:
	mkdir -p build
	${RPMBUILD} -ba python3-biplist.spec
	mv build/noarch/*.rpm .
	rm -rf build

spalipy:
	mkdir -p build
	${RPMBUILD} -ba python36-spalipy.spec
	mv build/noarch/*.rpm .
	rm -rf build

# Web packages for CentOS 8
flask:
	mkdir -p build
	${RPMBUILD} -ba python3-flask.spec
	mv build/noarch/*.rpm .
	rm -rf build

werkzeug:
	mkdir -p build
	${RPMBUILD} -ba python3-werkzeug.spec
	mv build/noarch/*.rpm .
	rm -rf build

github-flask:
	mkdir -p build
	${RPMBUILD} -ba python3-github-flask.spec
	mv build/noarch/*.rpm .
	rm -rf build

