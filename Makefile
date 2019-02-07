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
py36: astropy six pyds9 pyro4 sep demjson
py34: pyephem sysv_ipc pyserial pymysql Flask Flask-OAuthlib click itsdangerous Werkzeug oauthlib Jinja2 MarkupSafe Pillow jsonschema strict-rfc3339 pytesseract

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

pyephem:
	mkdir -p build
	py2pack fetch pyephem 3.7.6.0
	${RPMBUILD} -ba python34-pyephem.spec
	mv build/x86_64/*.rpm .
	rm -rf build

sysv_ipc:
	mkdir -p build
	py2pack fetch sysv_ipc 0.7.0
	${RPMBUILD} -ba python34-sysv_ipc.spec
	mv build/x86_64/*.rpm .
	rm -rf build

pymysql:
	mkdir -p build
	py2pack fetch PyMySQL 0.7.11
	${RPMBUILD} -ba python34-PyMySQL.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyserial:
	mkdir -p build
	py2pack fetch pyserial 3.4
	${RPMBUILD} -ba python34-pyserial.spec
	mv build/noarch/*.rpm .
	rm -rf build

# All needed for Flask

Werkzeug:
	mkdir -p build
	py2pack fetch Werkzeug 0.12.2
	${RPMBUILD} -ba python34-Werkzeug.spec
	mv build/noarch/*.rpm .
	rm -rf build

itsdangerous:
	mkdir -p build
	py2pack fetch itsdangerous 0.24
	${RPMBUILD} -ba python34-itsdangerous.spec
	mv build/noarch/*.rpm .
	rm -rf build

click:
	mkdir -p build
	py2pack fetch click 6.7
	${RPMBUILD} -ba python34-click.spec
	mv build/noarch/*.rpm .
	rm -rf build

Flask:
	mkdir -p build
	py2pack fetch Flask 0.12.2
	${RPMBUILD} -ba python34-Flask.spec
	mv build/noarch/*.rpm .
	rm -rf build

Flask-OAuthlib:
	mkdir -p build
	py2pack fetch Flask-OAuthlib 0.9.4
	${RPMBUILD} -ba python34-Flask-OAuthlib.spec
	mv build/noarch/*.rpm .
	rm -rf build

Jinja2:
	mkdir -p build
	py2pack fetch Jinja2 2.9.6
	${RPMBUILD} -ba python34-Jinja2.spec
	mv build/noarch/*.rpm .
	rm -rf build

MarkupSafe:
	mkdir -p build
	py2pack fetch MarkupSafe 1.0
	${RPMBUILD} -ba python34-MarkupSafe.spec
	mv build/x86_64/*.rpm .
	rm -rf build

oauthlib:
	mkdir -p build
	py2pack fetch oauthlib 2.0.4
	${RPMBUILD} -ba python34-oauthlib.spec
	mv build/noarch/*.rpm .
	rm -rf build

Pillow:
	mkdir -p build
	py2pack fetch Pillow 4.3.0
	${RPMBUILD} -ba python34-Pillow.spec
	mv build/x86_64/*.rpm .
	rm -rf build

jsonschema:
	mkdir -p build
	py2pack fetch jsonschema 2.6.0
	${RPMBUILD} -ba python34-jsonschema.spec
	mv build/noarch/*.rpm .
	rm -rf build

strict-rfc3339:
	mkdir -p build
	py2pack fetch strict-rfc3339 0.7
	${RPMBUILD} -ba python34-strict-rfc3339.spec
	mv build/noarch/*.rpm .
	rm -rf build

pytesseract:
	mkdir -p build
	py2pack fetch pytesseract 0.2.5
	${RPMBUILD} -ba python34-pytesseract.spec
	mv build/noarch/*.rpm .
	rm -rf build

