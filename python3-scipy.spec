%define debug_package %{nil}

Name:           python3-scipy
Version:        1.4.1
Release:        0
Url:            https://www.scipy.org
Summary:        SciPy: Scientific Library for Python
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/scipy/scipy-%{version}.tar.gz
BuildRequires:  python3-devel, python3-pybind11, gcc-c++, gcc-gfortran, openblas, lapack
Requires:       python3, openblas, lapack


%description
SciPy (pronounced "Sigh Pie") is open-source software for mathematics,
science, and engineering. The SciPy library
depends on NumPy, which provides convenient and fast N-dimensional
array manipulation. The SciPy library is built to work with NumPy
arrays, and provides many user-friendly and efficient numerical
routines such as routines for numerical integration and optimization.
Together, they run on all popular operating systems, are quick to
install, and are free of charge.  NumPy and SciPy are easy to use,
but powerful enough to be depended upon by some of the world's
leading scientists and engineers. If you need to manipulate
numbers on a computer and display or publish the results,
give SciPy a try!

%prep
%setup -q -n scipy-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog
