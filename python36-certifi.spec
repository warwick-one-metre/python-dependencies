Name:           python36-certifi
Version:        2018.11.29
Release:        0
Url:            https://certifi.io/
Summary:        Python package for providing Mozilla's CA Bundle.
License:        MPL-2.0 (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/c/certifi/certifi-%{version}.tar.gz
BuildRequires:  python36-devel
BuildArch:      noarch

%description
Certifi: Python SSL Certificates
================================

`Certifi`_ is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the identity
of TLS hosts. It has been extracted from the `Requests`_ project.

Installation
------------

``certifi`` is available on PyPI. Simply install it with ``pip``::

    $ pip install certifi

Usage
-----

To reference the installed certificate authority (CA) bundle, you can use the
built-in function::

    >>> import certifi

    >>> certifi.where()
    '/usr/local/lib/python2.7/site-packages/certifi/cacert.pem'

Enjoy!

1024-bit Root Certificates
~~~~~~~~~~~~~~~~~~~~~~~~~~

Browsers and certificate authorities have concluded that 1024-bit keys are
unacceptably weak for certificates, particularly root certificates. For this
reason, Mozilla has removed any weak (i.e. 1024-bit key) certificate from its
bundle, replacing it with an equivalent strong (i.e. 2048-bit or greater key)
certificate from the same CA. Because Mozilla removed these certificates from
its bundle, ``certifi`` removed them as well.

In previous versions, ``certifi`` provided the ``certifi.old_where()`` function
to intentionally re-add the 1024-bit roots back into your bundle. This was not
recommended in production and therefore was removed at the end of 2018.

.. _`Certifi`: https://certifi.io/en/latest/
.. _`Requests`: http://docs.python-requests.org/en/latest/

%prep
%setup -q -n certifi-%{version}

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
