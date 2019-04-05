Name:           python36-GitHub-Flask
Version:        3.2.0
Release:        0
Url:            http://github.com/cenkalti/github-flask
Summary:        GitHub extension for Flask microframework
License:        MIT
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/G/GitHub-Flask/GitHub-Flask-%{version}.tar.gz
BuildRequires:  python36-devel
Requires:       python36-Flask, python36-requests
BuildArch:      noarch

%description
GitHub-Flask
------------

Adds support to authorize users with GitHub and make API requests with Flask.

Links
`````

* `documentation <http://github-flask.readthedocs.org>`_
* `development version
  <http://github.com/cenkalti/github-flask/zipball/master#egg=GitHub-Flask-dev>`_

%prep
%setup -q -n GitHub-Flask-%{version}

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
