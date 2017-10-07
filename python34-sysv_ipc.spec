#
# spec file for package python-sysv_ipc
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


Name:           python34-sysv_ipc
Version:        0.7.0
Release:        0
License:        http://creativecommons.org/licenses/BSD/
Summary:        System V IPC primitives (semaphores, shared memory and message queues) for Python
Url:            http://semanchuk.com/philip/sysv_ipc/
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/s/sysv_ipc/sysv_ipc-%{version}.tar.gz
BuildRequires:  python34-devel
BuildArch:      x86_64

%description
Sysv_ipc gives Python programs access to System V semaphores, shared memory 
and message queues. Most (all?) Unixes (including OS X) support System V IPC. 
Windows+Cygwin 1.7 might also work. 

Sample code is included.

sysv_ipc is free software (free as in speech and free as in beer) released
under a 3-clause BSD license. Complete licensing information is available in 
the LICENSE file.

You might also be interested in the similar POSIX IPC module at:
http://semanchuk.com/philip/posix_ipc/

%prep
%setup -q -n sysv_ipc-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/*

%changelog
