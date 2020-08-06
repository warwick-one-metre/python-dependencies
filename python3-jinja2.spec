%global _python_bytecompile_errors_terminate_build 0

Name:           python3-jinja2
Version:        2.10.3
Release:        0
Url:            http://jinja.pocoo.org/
Summary:        A small but fast and easy to use stand-alone template engine written in pure python.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-markupsafe >= 0.23
BuildArch:      noarch

%description
Jinja2
~~~~~~

Jinja2 is a template engine written in pure Python.  It provides a
`Django`_ inspired non-XML syntax but supports inline expressions and
an optional `sandboxed`_ environment.

Nutshell
--------

Here a small example of a Jinja template::

    {% extends 'base.html' %}
    {% block title %}Memberlist{% endblock %}
    {% block content %}
      <ul>
      {% for user in users %}
        <li><a href="{{ user.url }}">{{ user.username }}</a></li>
      {% endfor %}
      </ul>
    {% endblock %}

Philosophy
----------

Application logic is for the controller but don't try to make the life
for the template designer too hard by giving him too few functionality.

For more informations visit the new `Jinja2 webpage`_ and `documentation`_.

.. _sandboxed: https://en.wikipedia.org/wiki/Sandbox_(computer_security)
.. _Django: https://www.djangoproject.com/
.. _Jinja2 webpage: http://jinja.pocoo.org/
.. _documentation: http://jinja.pocoo.org/2/documentation/

%prep
%setup -q -n Jinja2-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
