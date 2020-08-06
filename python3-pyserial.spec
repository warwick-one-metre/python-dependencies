Name:           python3-pyserial
Version:        3.4
Release:        0
License:        BSD (FIXME:No SPDX)
Summary:        Python Serial Port Extension
Url:            https://github.com/pyserial/pyserial
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pyserial/pyserial-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
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
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(0755,root,root,-)
%{_bindir}/miniterm.py
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
