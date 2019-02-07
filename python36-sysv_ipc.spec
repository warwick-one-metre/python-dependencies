Name:           python36-sysv_ipc
Version:        1.0.0
Release:        0
License:        http://creativecommons.org/licenses/BSD/
Summary:        System V IPC primitives (semaphores, shared memory and message queues) for Python
Url:            http://semanchuk.com/philip/sysv_ipc/
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/s/sysv_ipc/sysv_ipc-%{version}.tar.gz
BuildRequires:  python36-devel
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
%{__python3_other} setup.py build

%install
%{__python3_other} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_other_sitearch}/*

%changelog
