#
# spec file for package python3-Flask-OAuthlib
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           python3-Flask-OAuthlib
Version:        0.9.3
Release:        1
License:        BSD
Summary:        OAuthlib for Flask
Url:            https://github.com/lepture/flask-oauthlib
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/82/14/0d1a39ab2cc5aa2519b51dca9d253d38f2c1296d66529e08f8c7fd36aaa1/Flask-OAuthlib-%{version}.tar.gz
BuildRequires:  python3-devel
Requires: python3-oauthlib
BuildArch:      noarch

%description
Flask-OAuthlib
==============

.. image:: https://img.shields.io/pypi/wheel/flask-oauthlib.svg
   :target: https://pypi.python.org/pypi/flask-OAuthlib/
   :alt: Wheel Status
.. image:: https://img.shields.io/pypi/v/flask-oauthlib.svg
   :target: https://pypi.python.org/pypi/flask-oauthlib/
   :alt: Latest Version
.. image:: https://travis-ci.org/lepture/flask-oauthlib.svg?branch=master
   :target: https://travis-ci.org/lepture/flask-oauthlib
   :alt: Travis CI Status
.. image:: https://coveralls.io/repos/lepture/flask-oauthlib/badge.svg?branch=master
   :target: https://coveralls.io/r/lepture/flask-oauthlib
   :alt: Coverage Status
.. image:: https://img.shields.io/badge/donate-lepture-green.svg
   :target: https://lepture.herokuapp.com/?amount=1000&reason=lepture%2Fflask-oauthlib
   :alt: Donate leptjure


Flask-OAuthlib is an extension to Flask that allows you to interact with
remote OAuth enabled applications. On the client site, it is a replacement
for Flask-OAuth. But it does more than that, it also helps you to create
OAuth providers.

Flask-OAuthlib relies on oauthlib_.

.. _oauthlib: https://github.com/idan/oauthlib

Features
--------

- Support for OAuth 1.0a, 1.0, 1.1, OAuth2 client
- Friendly API (same as Flask-OAuth)
- Direct integration with Flask
- Basic support for remote method invocation of RESTful APIs
- Support OAuth1 provider with HMAC and RSA signature
- Support OAuth2 provider with Bearer token

And request more features at `github issues`_.

.. _`github issues`: https://github.com/lepture/flask-oauthlib/issues


Security Reporting
------------------

If you found security bugs which can not be public, send me email at `me@lepture.com`.
Attachment with patch is welcome.


Installation
------------

Installing flask-oauthlib is simple with pip_::

    $ pip install Flask-OAuthlib

If you don't have pip installed, try with easy_install::

    $ easy_install Flask-OAuthlib

.. _pip: http://www.pip-installer.org/


Additional Notes
----------------

We keep documentation at `flask-oauthlib@readthedocs`_.

.. _`flask-oauthlib@readthedocs`: https://flask-oauthlib.readthedocs.io

If you are only interested in the client part, you can find some examples
in the ``example`` directory.

There is also a `development version <https://github.com/lepture/flask-oauthlib/archive/master.zip#egg=Flask-OAuthlib-dev>`_ on GitHub.

%prep
%setup -q -n Flask-OAuthlib-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
