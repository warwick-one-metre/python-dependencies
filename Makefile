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
prereq: serpent numpy pybind11
web: flask werkzeug click jinja2 markupsafe requests idna certifi github-flask pyparsing bibtexparser biplist pymysql chardet urllib3 itsdangerous
general: astropy astroquery astroplan scipy jsonschema keyring skyfield sgp4 jplephem sep pyds9 pyro4 photutils pillow pyephem pyserial six strict-rfc3339 sysv_ipc demjson mpmath sympy sip_tpv pytesseract pcomfortcloud libusb1

numpy:
	mkdir -p build
	${RPMBUILD} -ba python3-numpy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

astropy:
	mkdir -p build
	${RPMBUILD} -ba python3-astropy.spec
	mv build/x86_64/*.rpm .
	rm -rf build

astroplan:
	mkdir -p build
	${RPMBUILD} -ba python3-astroplan.spec
	mv build/noarch/*.rpm .
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

pyds9:
	mkdir -p build
	${RPMBUILD} -ba python3-pyds9.spec
	mv build/x86_64/*.rpm .
	rm -rf x86_64

serpent:
	mkdir -p build
	${RPMBUILD} -ba python3-serpent.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyro4:
	mkdir -p build
	${RPMBUILD} -ba python3-Pyro4.spec
	mv build/noarch/*.rpm .
	rm -rf build

sep:
	mkdir -p build
	${RPMBUILD} -ba python3-sep.spec
	mv build/x86_64/*.rpm .
	rm -rf build

demjson:
	mkdir -p build
	${RPMBUILD} -ba python3-demjson.spec
	mv build/noarch/*.rpm .
	rm -rf build

strict-rfc3339:
	mkdir -p build
	${RPMBUILD} -ba python3-strict-rfc3339.spec
	mv build/noarch/*.rpm .
	rm -rf build

skyfield:
	mkdir -p build
	${RPMBUILD} -ba python3-skyfield.spec
	mv build/noarch/*.rpm .
	rm -rf build

sgp4:
	mkdir -p build
	${RPMBUILD} -ba python3-sgp4.spec
	mv build/x86_64/*.rpm .
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

jsonschema:
	mkdir -p build
	${RPMBUILD} -ba python3-jsonschema.spec
	mv build/noarch/*.rpm .
	rm -rf build

click:
	mkdir -p build
	${RPMBUILD} -ba python3-click.spec
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

biplist:
	mkdir -p build
	${RPMBUILD} -ba python3-biplist.spec
	mv build/noarch/*.rpm .
	rm -rf build

photutils:
	mkdir -p build
	${RPMBUILD} -ba python3-photutils.spec
	mv build/x86_64/*.rpm .
	rm -rf build

pyserial:
	mkdir -p build
	${RPMBUILD} -ba python3-pyserial.spec
	mv build/noarch/*.rpm .
	rm -rf build

pyephem:
	mkdir -p build
	${RPMBUILD} -ba python3-pyephem.spec
	mv build/x86_64/*.rpm .
	rm -rf build

six:
	mkdir -p build
	${RPMBUILD} -ba python3-six.spec
	mv build/noarch/*.rpm .
	rm -rf build

sysv_ipc:
	mkdir -p build
	${RPMBUILD} -ba python3-sysv_ipc.spec
	mv build/x86_64/*.rpm .
	rm -rf build

flask:
	mkdir -p build
	${RPMBUILD} -ba python3-flask.spec
	mv build/noarch/*.rpm .
	rm -rf build

jinja2:
	mkdir -p build
	${RPMBUILD} -ba python3-jinja2.spec
	mv build/noarch/*.rpm .
	rm -rf build

markupsafe:
	mkdir -p build
	${RPMBUILD} -ba python3-markupsafe.spec
	mv build/x86_64/*.rpm .
	rm -rf build

requests:
	mkdir -p build
	${RPMBUILD} -ba python3-requests.spec
	mv build/noarch/*.rpm .
	rm -rf build

idna:
	mkdir -p build
	${RPMBUILD} -ba python3-idna.spec
	mv build/noarch/*.rpm .
	rm -rf build

certifi:
	mkdir -p build
	${RPMBUILD} -ba python3-certifi.spec
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

mpmath:
	mkdir -p build
	${RPMBUILD} -ba python3-mpmath.spec
	mv build/noarch/*.rpm .
	rm -rf build

sympy:
	mkdir -p build
	${RPMBUILD} -ba python3-sympy.spec
	mv build/noarch/*.rpm .
	rm -rf build

sip_tpv:
	mkdir -p build
	${RPMBUILD} -ba python3-sip_tpv.spec
	mv build/noarch/*.rpm .
	rm -rf build


pytesseract:
	mkdir -p build
	${RPMBUILD} -ba python3-pytesseract.spec
	mv build/noarch/*.rpm .
	rm -rf build

pymysql:
	mkdir -p build
	${RPMBUILD} -ba python3-pymysql.spec
	mv build/noarch/*.rpm .
	rm -rf build

pillow:
	mkdir -p build
	${RPMBUILD} -ba python3-pillow.spec
	mv build/x86_64/*.rpm .
	rm -rf build

chardet:
	mkdir -p build
	${RPMBUILD} -ba python3-chardet.spec
	mv build/noarch/*.rpm .
	rm -rf build

itsdangerous:
	mkdir -p build
	${RPMBUILD} -ba python3-itsdangerous.spec
	mv build/noarch/*.rpm .
	rm -rf build

urllib3:
	mkdir -p build
	${RPMBUILD} -ba python3-urllib3.spec
	mv build/noarch/*.rpm .
	rm -rf build

pcomfortcloud:
	mkdir -p build
	${RPMBUILD} -ba python3-pcomfortcloud.spec
	mv build/noarch/*.rpm .
	rm -rf build

libusb1:
	mkdir -p build
	${RPMBUILD} -ba python3-libusb1.spec
	mv build/x86_64/*.rpm .
	rm -rf build
