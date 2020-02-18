Name:           python3-sip_tpv
Version:        1.1
Release:        0
Url:            https://github.com/stargaser/sip_tpv
Summary:        Conversion of distortion representations in FITS headers between SIP and TPV formats.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/sip_tpv/sip_tpv-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python3-devel
Requires:       python3-numpy, python3-astropy, python3-sympy
BuildArch:      noarch

%description


%prep
%setup -q -n sip_tpv-%{version}

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
