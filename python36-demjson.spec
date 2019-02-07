Name:           python36-demjson
Version:        2.2.4
Release:        0
License:        GNU LGPL 3.0
Summary:        encoder, decoder, and lint/validator for JSON (JavaScript Object Notation) compliant with RFC 7159
Url:            http://deron.meranda.us/python/demjson/
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/d/demjson/demjson-%{version}.tar.gz
BuildRequires:  python36-devel
BuildArch:      noarch

%description
The "demjson" module, and the included "jsonlint" script, provide methods
for encoding and decoding JSON formatted data, as well as checking JSON
data for errors and/or portability issues.  The jsonlint command/script
can be used from the command line without needing any programming.

Although the standard Python library now includes basic JSON support
(which it did not when demjson was first written), this module
provides a much more comprehensive implementation with many features
not found elsewhere.  It is especially useful for error checking or
for parsing JavaScript data which may not strictly be valid JSON data.

%prep
%setup -q -n demjson-%{version}

%build
%{__python3_other} setup.py build

%install
%{__python3_other} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_other_sitelib}/*
%{_bindir}/jsonlint

%changelog
