#
# spec file for package python-Pyro4
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


Name:           python3-Pyro4
Version:        4.45
Release:        0
License:        MIT
Summary:        distributed object middleware for Python (RPC)
Url:            http://pythonhosted.org/Pyro4/
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/P/Pyro4/Pyro4-%{version}.tar.gz
BuildRequires:  python3-devel
Requires:       python3-serpent
BuildArch:      noarch

%description
Pyro means PYthon Remote Objects. 
It is a library that enables you to build applications in which
objects can talk to eachother over the network, with minimal programming effort.
You can just use normal Python method calls, with almost every possible parameter
and return value type, and Pyro takes care of locating the right object on the right
computer to execute the method. It is designed to be very easy to use, and to 
generally stay out of your way. But it also provides a set of powerful features that
enables you to build distributed applications rapidly and effortlessly.
Pyro is written in 100% pure Python and therefore runs on many platforms and Python versions,
including Python 2.x, Python 3.x, IronPython, and Pypy.

The source code repository is on Github: https://github.com/irmen/Pyro4

%prep
%setup -q -n Pyro4-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE
%{python3_sitelib}/*
/usr/bin/*

%changelog
