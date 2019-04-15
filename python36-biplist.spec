Name:           python36-biplist
Version:        1.0.3
Release:        0
Url:            https://bitbucket.org/wooster/biplist
Summary:        biplist is a library for reading/writing binary plists.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/b/biplist/biplist-%{version}.tar.gz
BuildRequires:  python36-devel
BuildArch:      noarch

%description
`biplist` is a binary plist parser/generator for Python.

Binary Property List (plist) files provide a faster and smaller serialization
format for property lists on OS X. This is a library for generating binary
plists which can be read by OS X, iOS, or other clients.

This module requires Python 2.6 or higher or Python 3.4 or higher.

%prep
%setup -q -n biplist-%{version}

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
