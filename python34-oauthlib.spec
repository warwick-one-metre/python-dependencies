#
# spec file for package python3-oauthlib
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


Name:           python34-oauthlib
Version:        2.0.4
Release:        0
License:        BSD
Summary:        A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
Url:            https://github.com/idan/oauthlib
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/ce/92/7f07412a4f04e55c1e83a09c6fd48075b5df96c1dbd4078c3407c5be1dff/oauthlib-%{version}.tar.gz
BuildRequires:  python34-devel
BuildArch:      noarch

%description
OAuthLib
========

*A generic, spec-compliant, thorough implementation of the OAuth request-signing
logic for python*

.. image:: https://travis-ci.org/idan/oauthlib.png?branch=master
  :target: https://travis-ci.org/idan/oauthlib
.. image:: https://coveralls.io/repos/idan/oauthlib/badge.png?branch=master
  :target: https://coveralls.io/r/idan/oauthlib


OAuth often seems complicated and difficult-to-implement. There are several
prominent libraries for handling OAuth requests, but they all suffer from one or
both of the following:

1. They predate the `OAuth 1.0 spec`_, AKA RFC 5849.
2. They predate the `OAuth 2.0 spec`_, AKA RFC 6749.
3. They assume the usage of a specific HTTP request library.

.. _`OAuth 1.0 spec`: http://tools.ietf.org/html/rfc5849
.. _`OAuth 2.0 spec`: http://tools.ietf.org/html/rfc6749

OAuthLib is a generic utility which implements the logic of OAuth without
assuming a specific HTTP request object or web framework. Use it to graft OAuth
client support onto your favorite HTTP library, or provide support onto your
favourite web framework. If you're a maintainer of such a library, write a thin
veneer on top of OAuthLib and get OAuth support for very little effort.


Documentation
--------------

Full documentation is available on `Read the Docs`_. All contributions are very
welcome! The documentation is still quite sparse, please open an issue for what
you'd like to know, or discuss it in our `G+ community`_, or even better, send a
pull request!

.. _`G+ community`: https://plus.google.com/communities/101889017375384052571
.. _`Read the Docs`: https://oauthlib.readthedocs.io/en/latest/index.html

Interested in making OAuth requests?
------------------------------------

Then you might be more interested in using `requests`_ which has OAuthLib
powered OAuth support provided by the `requests-oauthlib`_ library.

.. _`requests`: https://github.com/kennethreitz/requests
.. _`requests-oauthlib`: https://github.com/requests/requests-oauthlib

Which web frameworks are supported?
-----------------------------------

The following packages provide OAuth support using OAuthLib.

- For Django there is `django-oauth-toolkit`_, which includes `Django REST framework`_ support.
- For Flask there is `flask-oauthlib`_ and `Flask-Dance`_.
- For Pyramid there is `pyramid-oauthlib`_.

If you have written an OAuthLib package that supports your favorite framework,
please open a Pull Request, updating the documentation.

.. _`django-oauth-toolkit`: https://github.com/evonove/django-oauth-toolkit
.. _`flask-oauthlib`: https://github.com/lepture/flask-oauthlib
.. _`Django REST framework`: http://django-rest-framework.org
.. _`Flask-Dance`: https://github.com/singingwolfboy/flask-dance
.. _`pyramid-oauthlib`: https://github.com/tilgovi/pyramid-oauthlib

Using OAuthLib? Please get in touch!
------------------------------------
Patching OAuth support onto an http request framework? Creating an OAuth
provider extension for a web framework? Simply using OAuthLib to Get Things Done
or to learn?

No matter which we'd love to hear from you in our `G+ community`_ or if you have
anything in particular you would like to have, change or comment on don't
hesitate for a second to send a pull request or open an issue. We might be quite
busy and therefore slow to reply but we love feedback!

Chances are you have run into something annoying that you wish there was
documentation for, if you wish to gain eternal fame and glory, and a drink if we
have the pleasure to run into eachother, please send a docs pull request =)

.. _`G+ community`: https://plus.google.com/communities/101889017375384052571

License
-------

OAuthLib is yours to use and abuse according to the terms of the BSD license.
Check the LICENSE file for full details.

Changelog
---------

*OAuthLib is in active development, with the core of both OAuth 1 and 2
completed, for providers as well as clients.* See `supported features`_ for
details.

.. _`supported features`: https://oauthlib.readthedocs.io/en/latest/feature_matrix.html

For a full changelog see ``CHANGELOG.rst``.

%prep
%setup -q -n oauthlib-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
