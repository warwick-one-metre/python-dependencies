Name:           python36-spalipy
Version:        1.0.1~0328238
Release:        0
Url:            https://github.com/Lyalpha/spalipy
Summary:        Detection-based astronomical image registration.
License:        GPLv3 (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://github.com/Lyalpha/spalipy/archive/03282380140fa724dba50a3b51f9ad48c5cab3dc.zip
BuildRequires:  python36-devel
Requires:       python36-astropy
Requires:       python36-numpy
Requires:       python36-scipy
BuildArch:      noarch

%description

%prep
%setup -q -n spalipy-03282380140fa724dba50a3b51f9ad48c5cab3dc

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
