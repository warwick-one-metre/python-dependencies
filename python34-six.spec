#
# spec file for package python-six
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python34-six
Version:        1.11.0
Release:        0
License:        MIT
Summary:        Python 2 and 3 compatibility utilities
Url:            http://pypi.python.org/pypi/six/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/six/six-%{version}.tar.gz
BuildRequires:  python34-devel
BuildRequires:  python34-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
.. image:: http://img.shields.io/pypi/v/six.svg
   :target: https://pypi.python.org/pypi/six

.. image:: https://travis-ci.org/benjaminp/six.svg?branch=master
    :target: https://travis-ci.org/benjaminp/six

.. image:: http://img.shields.io/badge/license-MIT-green.svg
   :target: https://github.com/benjaminp/six/blob/master/LICENSE

Six is a Python 2 and 3 compatibility library.  It provides utility functions
for smoothing over the differences between the Python versions with the goal of
writing Python code that is compatible on both Python versions.  See the
documentation for more information on what is provided.

Six supports every Python version since 2.6.  It is contained in only one Python
file, so it can be easily copied into your project. (The copyright and license
notice must be retained.)

Online documentation is at http://six.rtfd.org.

Bugs can be reported to https://github.com/benjaminp/six.  The code can also
be found there.

For questions about six or porting in general, email the python-porting mailing
list: https://mail.python.org/mailman/listinfo/python-porting




%prep
%setup -q -n six-%{version}

%build
python setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
