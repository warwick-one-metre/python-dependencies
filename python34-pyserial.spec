#
# spec file for package python-pyserial
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python34-pyserial
Version:        3.4
Release:        0
License:        BSD (FIXME:No SPDX)
Summary:        Python Serial Port Extension
Url:            https://github.com/pyserial/pyserial
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pyserial/pyserial-%{version}.tar.gz
BuildRequires:  python34-devel
BuildRequires:  python34-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Python Serial Port Extension for Win32, OSX, Linux, BSD, Jython, IronPython

Stable:

- Documentation: http://pythonhosted.org/pyserial/
- Download Page: https://pypi.python.org/pypi/pyserial

Latest:

- Documentation: http://pyserial.readthedocs.io/en/latest/
- Project Homepage: https://github.com/pyserial/pyserial




%prep
%setup -q -n pyserial-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(0755,root,root,-)
/usr/bin/miniterm.py
%defattr(-,root,root,-)
%{python3_sitelib}/*


%changelog
