#
# spec file for package python3-itsdangerous
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


Name:           python34-itsdangerous
Version:        0.24
Release:        0
License:        UNKNOWN
Summary:        Various helpers to pass trusted data to untrusted environments and back
Url:            http://github.com/mitsuhiko/itsdangerous
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-%{version}.tar.gz
BuildRequires:  python34-devel
BuildArch:      noarch

%description
It's Dangerous
   ... so better sign this

Various helpers to pass data to untrusted environments and to get it back
safe and sound.

This repository provides a module that is a port of the django signing
module.  It's not directly copied but some changes were applied to
make it work better on its own.

Also I plan to add some extra things.  Work in progress.


%prep
%setup -q -n itsdangerous-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
