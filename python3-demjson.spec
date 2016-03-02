#
# spec file for package python-demjson
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


Name:           python3-demjson
Version:        2.2.4
Release:        0
License:        GNU LGPL 3.0
Summary:        encoder, decoder, and lint/validator for JSON (JavaScript Object Notation) compliant with RFC 7159
Url:            http://deron.meranda.us/python/demjson/
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/d/demjson/demjson-%{version}.tar.gz
BuildRequires:  python3-devel
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
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*
/usr/bin/jsonlint

%changelog
