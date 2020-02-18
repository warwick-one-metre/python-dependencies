%define debug_package %{nil}

Name:           python3-pybind11
Version:        2.4.3
Release:        0
Url:            https://github.com/pybind/pybind11
Summary:        Seamless operability between C++11 and Python
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pybind11/pybind11-%{version}.tar.gz
BuildRequires:  python3-devel

%description
pybind11 is a lightweight header-only library that
exposes C++ types in Python and vice versa, mainly to create Python bindings of
existing C++ code. Its goals and syntax are similar to the excellent
Boost.Python by David Abrahams: to minimize boilerplate code in traditional
extension modules by inferring type information using compile-time
introspection.

The main issue with Boost.Python-and the reason for creating such a similar
project-is Boost. Boost is an enormously large and complex suite of utility
libraries that works with almost every C++ compiler in existence. This
compatibility has its cost: arcane template tricks and workarounds are
necessary to support the oldest and buggiest of compiler specimens. Now that
C++11-compatible compilers are widely available, this heavy machinery has
become an excessively large and unnecessary dependency.

Think of this library as a tiny self-contained version of Boost.Python with
everything stripped away that isn't relevant for binding generation. Without
comments, the core header files only require ~4K lines of code and depend on
Python (2.7 or 3.x, or PyPy2.7 >= 5.7) and the C++ standard library. This
compact implementation was possible thanks to some of the new C++11 language
features (specifically: tuples, lambda functions and variadic templates). Since
its creation, this library has grown beyond Boost.Python in many ways, leading
to dramatically simpler binding code in many common situations.

%prep
%setup -q -n pybind11-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_includedir}/python3.6m/pybind11/*

%changelog
