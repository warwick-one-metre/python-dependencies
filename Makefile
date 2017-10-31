# HACK: Expand the _topdir path to work around "Dest dir longer than base dir is not supported" errors from rpmbuild
RPMBUILD = rpmbuild --define "_topdir %(pwd)/build/../build/../build/../build/" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

# Generate spec files for new packages using:
# py2pack generate -t opensuse-legacy.spec <package name> <package version>
# then rename and modify spec file to use python3 and depend on python34-*
all: serpent pyro4 demjson pyephem sysv_ipc pyds9 astropy sep pyserial pymysql Flask Flask-OAuthlib click itsdangerous Werkzeug oauthlib Jinja2

serpent:
	mkdir -p build
	py2pack fetch serpent 1.12
	${RPMBUILD} -ba python34-serpent.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyro4:
	mkdir -p build
	py2pack fetch Pyro4 4.63
	${RPMBUILD} -ba python34-Pyro4.spec
	mv build/noarch/*.rpm .
	rm -rf build

demjson:
	mkdir -p build
	py2pack fetch demjson 2.2.4
	${RPMBUILD} -ba python34-demjson.spec
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

pyds9:
	mkdir -p build
	wget -N https://github.com/ericmandel/pyds9/archive/v1.8.1.zip
	${RPMBUILD} -ba python34-pyds9.spec
	mv build/x86_64/*.rpm .
	rm -rf x86_64

astropy:
	mkdir -p build
	py2pack fetch astropy 2.0.2
	${RPMBUILD} -ba python34-astropy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

sep:
	mkdir -p build
	py2pack fetch sep 1.0.1
	${RPMBUILD} -ba python34-sep.spec
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

oauthlib:
	mkdir -p build
	py2pack fetch oauthlib 2.0.4
	${RPMBUILD} -ba python34-oauthlib.spec
	mv build/noarch/*.rpm .
	rm -rf build

