Name:           python3-idna
Version:        2.8
Release:        0
Url:            https://github.com/kjd/idna
Summary:        Internationalized Domain Names in Applications (IDNA)
License:        BSD-like (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/i/idna/idna-%{version}.tar.gz
BuildRequires:  python3-devel
BuildArch:      noarch

%description
Internationalized Domain Names in Applications (IDNA)
=====================================================

Support for the Internationalised Domain Names in Applications
(IDNA) protocol as specified in `RFC 5891 <http://tools.ietf.org/html/rfc5891>`_.
This is the latest version of the protocol and is sometimes referred to as
&#8220;IDNA 2008&#8221;.

This library also provides support for Unicode Technical Standard 46,
`Unicode IDNA Compatibility Processing <http://unicode.org/reports/tr46/>`_.

This acts as a suitable replacement for the &#8220;encodings.idna&#8221; module that
comes with the Python standard library, but only supports the
old, deprecated IDNA specification (`RFC 3490 <http://tools.ietf.org/html/rfc3490>`_).

Basic functions are simply executed:

.. code-block:: pycon

    # Python 3
    >>> import idna
    >>> idna.encode('&#12489;&#12513;&#12452;&#12531;.&#12486;&#12473;&#12488;')
    b'xn--eckwd4c7c.xn--zckzah'
    >>> print(idna.decode('xn--eckwd4c7c.xn--zckzah'))
    &#12489;&#12513;&#12452;&#12531;.&#12486;&#12473;&#12488;

    # Python 2
    >>> import idna
    >>> idna.encode(u'&#12489;&#12513;&#12452;&#12531;.&#12486;&#12473;&#12488;')
    'xn--eckwd4c7c.xn--zckzah'
    >>> print idna.decode('xn--eckwd4c7c.xn--zckzah')
    &#12489;&#12513;&#12452;&#12531;.&#12486;&#12473;&#12488;

Packages
--------

The latest tagged release version is published in the PyPI repository:

.. image:: https://badge.fury.io/py/idna.svg
   :target: http://badge.fury.io/py/idna


Installation
------------

To install this library, you can use pip:

.. code-block:: bash

    $ pip install idna

Alternatively, you can install the package using the bundled setup script:

.. code-block:: bash

    $ python setup.py install

This library works with Python 2.7 and Python 3.4 or later.


Usage
-----

For typical usage, the ``encode`` and ``decode`` functions will take a domain
name argument and perform a conversion to A-labels or U-labels respectively.

.. code-block:: pycon

    # Python 3
    >>> import idna
    >>> idna.encode('&#12489;&#12513;&#12452;&#12531;.&#12486;&#12473;&#12488;')
    b'xn--eckwd4c7c.xn--zckzah'
    >>> print(idna.decode('xn--eckwd4c7c.xn--zckzah'))
    &#12489;&#12513;&#12452;&#12531;.&#12486;&#12473;&#12488;

You may use the codec encoding and decoding methods using the
``idna.codec`` module:

.. code-block:: pycon

    # Python 2
    >>> import idna.codec
    >>> print u'&#1076;&#1086;&#1084;&#1077;&#1085;&#1072;.&#1080;&#1089;&#1087;&#1099;&#1090;&#1072;&#1085;&#1080;&#1077;'.encode('idna')
    xn--80ahd1agd.xn--80akhbyknj4f
    >>> print 'xn--80ahd1agd.xn--80akhbyknj4f'.decode('idna')
    &#1076;&#1086;&#1084;&#1077;&#1085;&#1072;.&#1080;&#1089;&#1087;&#1099;&#1090;&#1072;&#1085;&#1080;&#1077;

Conversions can be applied at a per-label basis using the ``ulabel`` or ``alabel``
functions if necessary:

.. code-block:: pycon

    # Python 2
    >>> idna.alabel(u'&#27979;&#35797;')
    'xn--0zwm56d'

Compatibility Mapping (UTS #46)
+++++++++++++++++++++++++++++++

As described in `RFC 5895 <http://tools.ietf.org/html/rfc5895>`_, the IDNA
specification no longer normalizes input from different potential ways a user
may input a domain name. This functionality, known as a &#8220;mapping&#8221;, is now
considered by the specification to be a local user-interface issue distinct
from IDNA conversion functionality.

This library provides one such mapping, that was developed by the Unicode
Consortium. Known as `Unicode IDNA Compatibility Processing <http://unicode.org/reports/tr46/>`_,
it provides for both a regular mapping for typical applications, as well as
a transitional mapping to help migrate from older IDNA 2003 applications.

For example, &#8220;K&#246;nigsg&#228;&#223;chen&#8221; is not a permissible label as *LATIN CAPITAL
LETTER K* is not allowed (nor are capital letters in general). UTS 46 will
convert this into lower case prior to applying the IDNA conversion.

.. code-block:: pycon

    # Python 3
    >>> import idna
    >>> idna.encode(u'K&#246;nigsg&#228;&#223;chen')
    ...
    idna.core.InvalidCodepoint: Codepoint U+004B at position 1 of 'K&#246;nigsg&#228;&#223;chen' not allowed
    >>> idna.encode('K&#246;nigsg&#228;&#223;chen', uts46=True)
    b'xn--knigsgchen-b4a3dun'
    >>> print(idna.decode('xn--knigsgchen-b4a3dun'))
    k&#246;nigsg&#228;&#223;chen

Transitional processing provides conversions to help transition from the older
2003 standard to the current standard. For example, in the original IDNA
specification, the *LATIN SMALL LETTER SHARP S* (&#223;) was converted into two
*LATIN SMALL LETTER S* (ss), whereas in the current IDNA specification this
conversion is not performed.

.. code-block:: pycon

    # Python 2
    >>> idna.encode(u'K&#246;nigsg&#228;&#223;chen', uts46=True, transitional=True)
    'xn--knigsgsschen-lcb0w'

Implementors should use transitional processing with caution, only in rare
cases where conversion from legacy labels to current labels must be performed
(i.e. IDNA implementations that pre-date 2008). For typical applications
that just need to convert labels, transitional processing is unlikely to be
beneficial and could produce unexpected incompatible results.

``encodings.idna`` Compatibility
++++++++++++++++++++++++++++++++

Function calls from the Python built-in ``encodings.idna`` module are
mapped to their IDNA 2008 equivalents using the ``idna.compat`` module.
Simply substitute the ``import`` clause in your code to refer to the
new module name.

Exceptions
----------

All errors raised during the conversion following the specification should
raise an exception derived from the ``idna.IDNAError`` base class.

More specific exceptions that may be generated as ``idna.IDNABidiError``
when the error reflects an illegal combination of left-to-right and right-to-left
characters in a label; ``idna.InvalidCodepoint`` when a specific codepoint is
an illegal character in an IDN label (i.e. INVALID); and ``idna.InvalidCodepointContext``
when the codepoint is illegal based on its positional context (i.e. it is CONTEXTO
or CONTEXTJ but the contextual requirements are not satisfied.)

Building and Diagnostics
------------------------

The IDNA and UTS 46 functionality relies upon pre-calculated lookup tables for
performance. These tables are derived from computing against eligibility criteria
in the respective standards. These tables are computed using the command-line
script ``tools/idna-data``.

This tool will fetch relevant tables from the Unicode Consortium and perform the
required calculations to identify eligibility. It has three main modes:

* ``idna-data make-libdata``. Generates ``idnadata.py`` and ``uts46data.py``,
  the pre-calculated lookup tables using for IDNA and UTS 46 conversions. Implementors
  who wish to track this library against a different Unicode version may use this tool
  to manually generate a different version of the ``idnadata.py`` and ``uts46data.py``
  files.

* ``idna-data make-table``. Generate a table of the IDNA disposition
  (e.g. PVALID, CONTEXTJ, CONTEXTO) in the format found in Appendix B.1 of RFC
  5892 and the pre-computed tables published by `IANA <http://iana.org/>`_.

* ``idna-data U+0061``. Prints debugging output on the various properties
  associated with an individual Unicode codepoint (in this case, U+0061), that are
  used to assess the IDNA and UTS 46 status of a codepoint. This is helpful in debugging
  or analysis.

The tool accepts a number of arguments, described using ``idna-data -h``. Most notably,
the ``--version`` argument allows the specification of the version of Unicode to use
in computing the table data. For example, ``idna-data --version 9.0.0 make-libdata``
will generate library data against Unicode 9.0.0.

Note that this script requires Python 3, but all generated library data will work
in Python 2.7.


Testing
-------

The library has a test suite based on each rule of the IDNA specification, as
well as tests that are provided as part of the Unicode Technical Standard 46,
`Unicode IDNA Compatibility Processing <http://unicode.org/reports/tr46/>`_.

The tests are run automatically on each commit at Travis CI:

.. image:: https://travis-ci.org/kjd/idna.svg?branch=master
   :target: https://travis-ci.org/kjd/idna


%prep
%setup -q -n idna-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog