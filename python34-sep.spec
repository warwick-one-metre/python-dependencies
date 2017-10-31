#
# spec file for package python-sep
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

Name:           python34-sep
Version:        1.0.1
Release:        0
License:        LGPL-3.0+
Summary:        Astronomical source extraction and photometry library
Url:            https://github.com/kbarbary/sep
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/35/51/66f6f441d8b85b2c5b32b0ca768737f3dd45c321a86f96d9b86054caf8fe/sep-%{version}.tar.gz
BuildRequires:  python34-devel
BuildArch:      x86_64

%description
http://sep.readthedocs.org

%prep
%setup -q -n sep-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog
