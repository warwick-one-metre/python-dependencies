RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all: serpent pyro4 demjson pyephem sysv_ipc pyds9 astropy sep

serpent:
	mkdir -p build
	py2pack fetch serpent 1.12
	${RPMBUILD} -ba python3-serpent.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyro4:
	mkdir -p build
	py2pack fetch Pyro4 4.41
	${RPMBUILD} -ba python3-Pyro4.spec
	mv build/noarch/*.rpm .
	rm -rf build

demjson:
	mkdir -p build
	py2pack fetch demjson 2.2.4
	${RPMBUILD} -ba python3-demjson.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyephem:
	mkdir -p build
	py2pack fetch pyephem 3.7.6.0
	${RPMBUILD} -ba python3-pyephem.spec
	mv build/noarch/*.rpm .
	rm -rf build

sysv_ipc:
	mkdir -p build
	py2pack fetch sysv_ipc 0.7.0
	${RPMBUILD} -ba python3-sysv_ipc.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyds9:
	mkdir -p build
	wget -N https://github.com/ericmandel/pyds9/archive/v1.8.1.zip
	${RPMBUILD} -ba python3-pyds9.spec
	mv build/noarch/*.rpm .
	rm -rf build

astropy:
	mkdir -p build
	py2pack fetch astropy 1.1.2
	${RPMBUILD} -ba python3-astropy.spec
	mv build/noarch/*.rpm .
	rm -rf build

sep:
	mkdir -p build
	py2pack fetch sep 0.5.2
	${RPMBUILD} -ba python3-sep.spec
	mv build/noarch/*.rpm .
	rm -rf build
