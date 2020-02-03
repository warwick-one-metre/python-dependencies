Name:           python3-skyfield
Version:        1.15
Release:        0
Url:            http://github.com/brandon-rhodes/python-skyfield/
Summary:        Elegant astronomy for Python
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/skyfield/skyfield-%{version}.tar.gz
Requires:       python3-sgp4 >= 1.4
Requires:       python3-jplephem >= 2.3
Requires:       python3-numpy
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildArch: noarch

%description

====================================
 Welcome to the Skyfield Repository
====================================

Skyfield is a pure-Python astronomy package
that is compatible with both Python 2 and 3
and makes it easy to generate high precision research-grade
positions for planets and Earth satellites.

::

   from skyfield.api import load

   planets = load('de421.bsp')
   earth, mars = planets['earth'], planets['mars']

   ts = load.timescale()
   t = ts.now()
   position = earth.at(t).observe(mars)
   ra, dec, distance = position.radec()

   print(ra)
   print(dec)
   print(distance)

The result:

::

   10h 47m 56.24s
   +09deg 03' 23.1"
   2.33251 au

Skyfield&#8217;s only binary dependency is NumPy.
Once that is available, Skyfield can usually be installed with::

    pip install skyfield

Here are the essential project links:

* `Home page and documentation
  <http://rhodesmill.org/skyfield>`_.

* `Installing Skyfield
  <http://rhodesmill.org/skyfield/installation.html>`_.

* `Contributing to Skyfield
  <https://github.com/skyfielders/python-skyfield/blob/master/Contrib.rst>`_.

* `Skyfield package <https://pypi.python.org/pypi/skyfield>`_
  on the Python Package Index.

* `Issue tracker
  <https://github.com/brandon-rhodes/python-skyfield/issues>`_
  on GitHub.


%prep
%setup -q -n skyfield-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
