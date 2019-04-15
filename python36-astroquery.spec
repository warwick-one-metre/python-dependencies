Name:           python36-astroquery
Version:        0.3.9
Release:        0
Url:            http://astropy.org/astroquery
Summary:        Functions and classes to access online astronomical data resources
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/astroquery/astroquery-%{version}.tar.gz
BuildRequires:  python36-devel
Requires:       python36-html5lib
Requires:       python36-beautifulsoup4
Requires:       python36-keyring
Requires:       python36-requests
Requires:       python36-astropy
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
