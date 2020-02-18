Name:           python3-mpmath
Version:        1.1.0
Release:        0
Url:            http://mpmath.org
Summary:        Python library for arbitrary-precision floating-point arithmetic
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/m/mpmath/mpmath-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python3-devel
BuildArch:      noarch

%description


%prep
%setup -q -n mpmath-%{version}

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
