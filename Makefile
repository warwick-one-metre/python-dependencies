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
web: flask werkzeug github-flask pyparsing bibtexparser biplist
general: astropy astroquery astroplan scipy keyring skyfield sgp4 jplephem sep pyds9 pyro4 photutils strict-rfc3339 demjson mpmath sympy sip_tpv

numpy:
	echo 'Packaging numpy' && echo -en "travis_fold:start:numpy"
	mkdir -p build
	${RPMBUILD} -ba python3-numpy.spec
	mv build/x86_64/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:numpy\r"

astropy:
	echo 'Packaging astropy' && echo -en "travis_fold:start:astropy"
	mkdir -p build
	${RPMBUILD} -ba python3-astropy.spec
	mv build/x86_64/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:astropy\r"

astroplan:
	echo 'Packaging astroplan' && echo -en "travis_fold:start:astroplan"
	mkdir -p build
	${RPMBUILD} -ba python3-astroplan.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:astroplan\r"

pybind11:
	echo 'Packaging pybind11' && echo -en "travis_fold:start:pybind11"
	mkdir -p build
	${RPMBUILD} -ba python3-pybind11.spec
	mv build/x86_64/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:pybind11\r"

scipy:
	echo 'Packaging scipy' && echo -en "travis_fold:start:scipy"
	mkdir -p build
	${RPMBUILD} -ba python3-scipy.spec
	mv build/x86_64/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:scipy\r"

pyds9:
	echo 'Packaging pyds9' && echo -en "travis_fold:start:pyds9"
	mkdir -p build
	${RPMBUILD} -ba python3-pyds9.spec
	mv build/x86_64/*.rpm .
	rm -rf x86_64
	echo -en "\ntravis_fold:end:pyds9\r"

serpent:
	echo 'Packaging serpent' && echo -en "travis_fold:start:serpent"
	mkdir -p build
	${RPMBUILD} -ba python3-serpent.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:serpent\r"

pyro4:
	echo 'Packaging Pyro4' && echo -en "travis_fold:start:Pyro4"
	mkdir -p build
	${RPMBUILD} -ba python3-Pyro4.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:Pyro4\r"

sep:
	echo 'Packaging sep' && echo -en "travis_fold:start:sep"
	mkdir -p build
	${RPMBUILD} -ba python3-sep.spec
	mv build/x86_64/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:sep\r"

demjson:
	echo 'Packaging demjson' && echo -en "travis_fold:start:demjson"
	mkdir -p build
	${RPMBUILD} -ba python3-demjson.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:demjson\r"

strict-rfc3339:
	echo 'Packaging strict-rfc3339' && echo -en "travis_fold:start:strict-rfc3339"
	mkdir -p build
	${RPMBUILD} -ba python3-strict-rfc3339.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:strict-rfc3339\r"

skyfield:
	echo 'Packaging skyfield' && echo -en "travis_fold:start:skyfield"
	mkdir -p build
	${RPMBUILD} -ba python3-skyfield.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:skyfield\r"

sgp4:
	echo 'Packaging sgp4' && echo -en "travis_fold:start:sgp4"
	mkdir -p build
	${RPMBUILD} -ba python3-sgp4.spec
	mv build/x86_64/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:sgp4\r"

jplephem:
	echo 'Packaging jplephem' && echo -en "travis_fold:start:jplephem"
	mkdir -p build
	${RPMBUILD} -ba python3-jplephem.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:jplephem\r"

astroquery:
	echo 'Packaging astroquery' && echo -en "travis_fold:start:astroquery"
	mkdir -p build
	${RPMBUILD} -ba python3-astroquery.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:astroquery\r"

keyring:
	echo 'Packaging keyring' && echo -en "travis_fold:start:keyring"
	mkdir -p build
	${RPMBUILD} -ba python3-keyring.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:keyring\r"

click:
	echo 'Packaging click' && echo -en "travis_fold:start:click"
	mkdir -p build
	${RPMBUILD} -ba python3-click.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:click\r"

pyparsing:
	echo 'Packaging pyparsing' && echo -en "travis_fold:start:pyparsing"
	mkdir -p build
	${RPMBUILD} -ba python3-pyparsing.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:pyparsing\r"

bibtexparser:
	echo 'Packaging bibtexparser' && echo -en "travis_fold:start:bibtexparser"
	mkdir -p build
	${RPMBUILD} -ba python3-bibtexparser.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:bibtexparser\r"

biplist:
	echo 'Packaging biplist' && echo -en "travis_fold:start:biplist"
	mkdir -p build
	${RPMBUILD} -ba python3-biplist.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:biplist\r"

photutils:
	echo 'Packaging photutils' && echo -en "travis_fold:start:photutils"
	mkdir -p build
	${RPMBUILD} -ba python3-photutils.spec
	mv build/x86_64/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:photutils\r"

flask:
	echo 'Packaging flask' && echo -en "travis_fold:start:flask"
	mkdir -p build
	${RPMBUILD} -ba python3-flask.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:flask\r"

werkzeug:
	echo 'Packaging werkzeug' && echo -en "travis_fold:start:werkzeug"
	mkdir -p build
	${RPMBUILD} -ba python3-werkzeug.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:werkzeug\r"

github-flask:
	echo 'Packaging github-flask' && echo -en "travis_fold:start:github-flask"
	mkdir -p build
	${RPMBUILD} -ba python3-github-flask.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:github-flask\r"

mpmath:
	echo 'Packaging mpmath' && echo -en "travis_fold:start:mpmath"
	mkdir -p build
	${RPMBUILD} -ba python3-mpmath.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:mpmath\r"

sympy:
	echo 'Packaging sympy' && echo -en "travis_fold:start:sympy"
	mkdir -p build
	${RPMBUILD} -ba python3-sympy.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:sympy\r"

sip_tpv:
	echo 'Packaging sip_tpv' && echo -en "travis_fold:start:sip_tpv"
	mkdir -p build
	${RPMBUILD} -ba python3-sip_tpv.spec
	mv build/noarch/*.rpm .
	rm -rf build
	echo -en "\ntravis_fold:end:sip_tpv\r"

