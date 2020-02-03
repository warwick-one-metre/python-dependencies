%define debug_package %{nil}

Name:           python3-numpy
Version:        1.16.1
Release:        0
License:        BSD (FIXME:No SPDX)
Summary:        NumPy is the fundamental package for array computing with Python
Url:            https://www.numpy.org
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/n/numpy/numpy-%{version}.zip
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  unzip
BuildRequires:  atlas-devel
BuildRequires:  lapack-devel
BuildRequires:  gcc-gfortran
BuildRequires:  libquadmath

%description
 NumPy is the fundamental package for array computing with Python.

%prep
%setup -q -n numpy-%{version}

%build

%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
%{_bindir}/f2py
%{_bindir}/f2py3
%{_bindir}/f2py3.6

%changelog
