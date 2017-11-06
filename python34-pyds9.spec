#
# spec file for package python-pyds9
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

Name:           python34-pyds9
Version:        1.8.1
Release:        3
License:        GPL2
Summary:        Python connection to ds9 via XPA
Url:            https://github.com/ericmandel/pyds9/
Group:          Development/Languages/Python
Source:         https://github.com/ericmandel/pyds9/archive/v1.8.1.zip
BuildRequires:  python34-devel, libXt-devel
Requires:       python34-six
BuildArch:      x86_64

%description
The XPA messaging system provides seamless communication between many kinds of Unix programs, including Tcl/Tk programs such as ds9. The pyds9 module uses a Python interface to XPA to communicate with ds9. It supports communication with all of ds9's XPA access points. See http://hea-www.harvard.edu/saord/ds9/ref/xpa.html for more info.

%prep
%setup -q -n pyds9-1.8.1

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
