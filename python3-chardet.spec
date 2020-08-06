Name:           python3-chardet
Version:        3.0.4
Release:        1
Url:            https://github.com/chardet/chardet
Summary:        Universal encoding detector for Python 2 and 3
License:        LGPL (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/c/chardet/chardet-%{version}.tar.gz
BuildRequires:  python3-devel
BuildArch:      noarch

%description
Chardet: The Universal Character Encoding Detector
--------------------------------------------------

.. image:: https://img.shields.io/travis/chardet/chardet/stable.svg
   :alt: Build status
   :target: https://travis-ci.org/chardet/chardet

.. image:: https://img.shields.io/coveralls/chardet/chardet/stable.svg
   :target: https://coveralls.io/r/chardet/chardet

.. image:: https://img.shields.io/pypi/v/chardet.svg
   :target: https://warehouse.python.org/project/chardet/
   :alt: Latest version on PyPI

.. image:: https://img.shields.io/pypi/l/chardet.svg
   :alt: License


Detects
 - ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)
 - Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified Chinese)
 - EUC-JP, SHIFT_JIS, CP932, ISO-2022-JP (Japanese)
 - EUC-KR, ISO-2022-KR (Korean)
 - KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)
 - ISO-8859-5, windows-1251 (Bulgarian)
 - ISO-8859-1, windows-1252 (Western European languages)
 - ISO-8859-7, windows-1253 (Greek)
 - ISO-8859-8, windows-1255 (Visual and Logical Hebrew)
 - TIS-620 (Thai)

.. note::
   Our ISO-8859-2 and windows-1250 (Hungarian) probers have been temporarily
   disabled until we can retrain the models.

Requires Python 2.6, 2.7, or 3.3+.

Installation
------------

Install from `PyPI <https://pypi.python.org/pypi/chardet>`_::

    pip install chardet

Documentation
-------------

For users, docs are now available at https://chardet.readthedocs.io/.

Command-line Tool
-----------------

chardet comes with a command-line script which reports on the encodings of one
or more files::

    % chardetect somefile someotherfile
    somefile: windows-1252 with confidence 0.5
    someotherfile: ascii with confidence 1.0

About
-----

This is a continuation of Mark Pilgrim's excellent chardet. Previously, two
versions needed to be maintained: one that supported python 2.x and one that
supported python 3.x.  We've recently merged with `Ian Cordasco <https://github.com/sigmavirus24>`_'s
`charade <https://github.com/sigmavirus24/charade>`_ fork, so now we have one
coherent version that works for Python 2.6+.

:maintainer: Dan Blanchard

%prep
%setup -q -n chardet-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}
rm %{buildroot}/usr/bin/chardetect

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
