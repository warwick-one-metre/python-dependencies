#
# spec file for package python-astropy
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           python34-astropy
Version:        1.1.2
Release:        0
License:        BSD
Summary:        Community-developed python astronomy tools
Url:            http://astropy.org
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/a/astropy/astropy-%{version}.tar.gz
BuildRequires:  python34-devel
BuildRequires:  python34-numpy
Requires:       python34-numpy
BuildArch:      x86_64

%description
Astropy is a package intended to contain core functionality and some
common tools needed for performing astronomy and astrophysics research with
Python. It also provides an index for other astronomy packages and tools for
managing them.

%prep
%setup -q -n astropy-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*
/usr/bin/*

%changelog
