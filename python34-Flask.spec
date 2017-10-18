#
# spec file for package python3-Flask
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


Name:           python34-Flask
Version:        0.12.2
Release:        0
License:        BSD
Summary:        A microframework based on Werkzeug, Jinja2 and good intentions
Url:            http://github.com/pallets/flask/
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/55/8a/78e165d30f0c8bb5d57c429a30ee5749825ed461ad6c959688872643ffb3/Flask-%{version}.tar.gz
BuildRequires:  python34-devel
Requires:       python34-Werkzeug >= 0.7
Requires:       python34-Jinja2 >= 2.4
Requires:       python34-itsdangerous >= 0.21
Requires:       python34-click >= 2.0
BuildArch:      noarch

%description
Flask
-----

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good
intentions. And before you ask: It's BSD licensed!

Flask is Fun
````````````

Save in a hello.py:

.. code:: python

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()

And Easy to Setup
`````````````````

And run it:

.. code:: bash

    $ pip install Flask
    $ python hello.py
     * Running on http://localhost:5000/

Links
`````

* `website <http://flask.pocoo.org/>`_
* `documentation <http://flask.pocoo.org/docs/>`_
* `development version
  <http://github.com/pallets/flask/zipball/master#egg=Flask-dev>`_

%prep
%setup -q -n Flask-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check

%files
%defattr(-,root,root,-)
%doc README CHANGES LICENSE AUTHORS
%{python3_sitelib}/*
/usr/bin/flask

%changelog
