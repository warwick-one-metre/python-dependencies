RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all: serpent pyro4 demjson pyephem

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
