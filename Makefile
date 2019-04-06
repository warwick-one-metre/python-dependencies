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
prereq: numpy serpent
general: astropy astroplan scipy six pyds9 pyro4 sep demjson pyserial pyephem sysv_ipc Pillow pytesseract pymysql strict-rfc3339 jsonschema
web: Flask click itsdangerous Werkzeug Jinja2 MarkupSafe chardet idna urllib3 certifi requests GitHub-Flask

numpy:
	mkdir -p build
	${RPMBUILD} -ba python36-numpy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

astropy:
	mkdir -p build
	${RPMBUILD} -ba python36-astropy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

astroplan:
	mkdir -p build
	${RPMBUILD} -ba python36-astroplan.spec
	mv build/noarch/*.rpm .
	rm -rf build

scipy:
	mkdir -p build
	${RPMBUILD} -ba python36-scipy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

six:
	mkdir -p build
	${RPMBUILD} -ba python36-six.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyds9:
	mkdir -p build
	${RPMBUILD} -ba python36-pyds9.spec
	mv build/x86_64/*.rpm .
	rm -rf x86_64

serpent:
	mkdir -p build
	${RPMBUILD} -ba python36-serpent.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyro4:
	mkdir -p build
	${RPMBUILD} -ba python36-Pyro4.spec
	mv build/noarch/*.rpm .
	rm -rf build

sep:
	mkdir -p build
	${RPMBUILD} -ba python36-sep.spec
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

