#
# spec file for package python3-click
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


Name:           python34-click
Version:        6.7
Release:        0
License:        UNKNOWN
Summary:        A simple wrapper around optparse for powerful command line utilities
Url:            http://github.com/mitsuhiko/click
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/7a/00/c14926d8232b36b08218067bcd5853caefb4737cda3f0a47437151344792/click-%{version}.tar.gz
BuildRequires:  python34-devel
BuildArch:      noarch

%description
$ click_

  Click is a Python package for creating beautiful command line interfaces
  in a composable way with as little code as necessary.  It's the "Command
  Line Interface Creation Kit".  It's highly configurable but comes with
  sensible defaults out of the box.

  It aims to make the process of writing command line tools quick and fun
  while also preventing any frustration caused by the inability to implement
  an intended CLI API.

  Click in three points:

  -   arbitrary nesting of commands
  -   automatic help page generation
  -   supports lazy loading of subcommands at runtime

  Read the docs at http://click.pocoo.org/

 This library is stable and active. Feedback is always welcome!


%prep
%setup -q -n click-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
