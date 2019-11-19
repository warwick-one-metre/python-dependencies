%define debug_package %{nil}

Name:           python36-astropy
Version:        3.2.3
Release:        0
Url:            http://astropy.org
Summary:        Community-developed python astronomy tools
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/astropy/astropy-%{version}.tar.gz
BuildRequires:  python36-setuptools
BuildRequires:  python36-numpy >= 1.13
Requires:       python36-numpy >= 1.13
BuildArch:      x86_64

%description
Astropy is a package intended to contain core functionality and some
common tools needed for performing astronomy and astrophysics research with
Python. It also provides an index for other astronomy packages and tools for
managing them.

%prep
%setup -q -n astropy-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py --offline install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
%{_bindir}/*

%changelog
