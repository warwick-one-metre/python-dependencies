Name:           python3-astroquery
Version:        0.4
Release:        0
Url:            http://astropy.org/astroquery
Summary:        Functions and classes to access online astronomical data resources
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/astroquery/astroquery-%{version}.tar.gz
BuildRequires:  python3-devel
Requires:       python3-astropy, python3-requests, python3-keyring, python3-beautifulsoup4, python3-html5lib, python3-six
BuildArch:      noarch

%description

%prep
%setup -q -n astroquery-%{version}

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
