#
# spec file for package python3-PyMySQL
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


Name:           python3-PyMySQL
Version:        0.7.9
Release:        0
License:        MIT
Summary:        Pure Python MySQL Driver
Url:            https://github.com/PyMySQL/PyMySQL/
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/a4/c4/c15457f261fda9839637de044eca9b6da8f55503183fe887523801b85701/PyMySQL-%{version}.tar.gz
BuildRequires:  python3-devel
BuildArch:      noarch

%description
UNKNOWN




%prep
%setup -q -n PyMySQL-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check

%files
%defattr(-,root,root,-)
%doc LICENSE README.rst CHANGELOG
%{python3_sitelib}/*

%changelog
